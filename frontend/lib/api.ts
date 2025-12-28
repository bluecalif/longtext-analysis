/**
 * API 클라이언트
 * 
 * 백엔드 API와 통신하는 타입 안전한 클라이언트
 * Query 파라미터는 snake_case 유지 (use_llm)
 */

import type {
  ParseResponse,
  TimelineRequest,
  TimelineResponse,
  IssuesRequest,
  IssuesResponse,
  SnippetResponse,
  SnippetsProcessRequest,
  SnippetsProcessResponse,
  ExportTimelineRequest,
  ExportIssuesRequest,
  ExportAllRequest,
} from '@/types/api'

// API 기본 URL (환경 변수에서 가져오기)
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

/**
 * API 에러 클래스
 */
export class ApiError extends Error {
  constructor(
    message: string,
    public statusCode?: number,
    public detail?: string
  ) {
    super(message)
    this.name = 'ApiError'
  }
}

/**
 * Query 파라미터를 URL에 추가하는 헬퍼 함수
 */
function buildQueryString(params: Record<string, unknown>): string {
  const searchParams = new URLSearchParams()
  
  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined && value !== null) {
      searchParams.append(key, String(value))
    }
  }
  
  const queryString = searchParams.toString()
  return queryString ? `?${queryString}` : ''
}

/**
 * API 클라이언트 객체
 */
export const api = {
  /**
   * 파일 업로드 및 파싱
   * 
   * @param file 업로드할 마크다운 파일
   * @param use_llm LLM 사용 여부 (기본값: true, snake_case 유지)
   * @returns ParseResponse
   */
  async parseFile(
    file: File,
    use_llm: boolean = true
  ): Promise<ParseResponse> {
    const formData = new FormData()
    formData.append('file', file)
    
    const queryString = buildQueryString({ use_llm })
    const url = `/api/parse${queryString}`
    
    const response = await fetch(`${API_BASE_URL}${url}`, {
      method: 'POST',
      body: formData,
      // FormData 사용 시 Content-Type 헤더를 설정하지 않음 (브라우저가 자동 설정)
    })

    if (!response.ok) {
      let detail: string | undefined
      try {
        const errorData = await response.json()
        detail = errorData.detail || errorData.message
      } catch {
        detail = response.statusText
      }
      
      throw new ApiError(
        `Parse failed: ${response.statusText}`,
        response.status,
        detail
      )
    }

    return response.json()
  },

  /**
   * Timeline 생성
   * 
   * @param request TimelineRequest
   * @param use_llm LLM 사용 여부 (기본값: true, snake_case 유지)
   * @returns TimelineResponse
   */
  async createTimeline(
    request: TimelineRequest,
    use_llm: boolean = true
  ): Promise<TimelineResponse> {
    const queryString = buildQueryString({ use_llm })
    return apiRequest<TimelineResponse>(
      `/api/timeline${queryString}`,
      {
        method: 'POST',
        body: JSON.stringify(request),
      }
    )
  },

  /**
   * Issue Cards 생성
   * 
   * @param request IssuesRequest
   * @param use_llm LLM 사용 여부 (기본값: true, snake_case 유지)
   * @returns IssuesResponse
   */
  async createIssues(
    request: IssuesRequest,
    use_llm: boolean = true
  ): Promise<IssuesResponse> {
    const queryString = buildQueryString({ use_llm })
    return apiRequest<IssuesResponse>(
      `/api/issues${queryString}`,
      {
        method: 'POST',
        body: JSON.stringify(request),
      }
    )
  },

  /**
   * 스니펫 처리
   * 
   * @param request SnippetsProcessRequest
   * @returns SnippetsProcessResponse
   */
  async processSnippets(
    request: SnippetsProcessRequest
  ): Promise<SnippetsProcessResponse> {
    return apiRequest<SnippetsProcessResponse>(
      '/api/snippets/process',
      {
        method: 'POST',
        body: JSON.stringify(request),
      }
    )
  },

  /**
   * 스니펫 조회
   * 
   * @param snippetId 스니펫 ID
   * @returns SnippetResponse
   */
  async getSnippet(snippetId: string): Promise<SnippetResponse> {
    return apiRequest<SnippetResponse>(
      `/api/snippets/${encodeURIComponent(snippetId)}`,
      {
        method: 'GET',
      }
    )
  },

  /**
   * Timeline 다운로드
   * 
   * @param request ExportTimelineRequest
   * @returns Blob (JSON 또는 MD 파일)
   */
  async exportTimeline(request: ExportTimelineRequest): Promise<Blob> {
    return apiRequest<Blob>(
      '/api/export/timeline',
      {
        method: 'POST',
        body: JSON.stringify(request),
      }
    )
  },

  /**
   * Issues 다운로드
   * 
   * @param request ExportIssuesRequest
   * @returns Blob (JSON 또는 MD 파일)
   */
  async exportIssues(request: ExportIssuesRequest): Promise<Blob> {
    return apiRequest<Blob>(
      '/api/export/issues',
      {
        method: 'POST',
        body: JSON.stringify(request),
      }
    )
  },

  /**
   * 전체 산출물 다운로드
   * 
   * @param request ExportAllRequest
   * @returns Blob (ZIP 파일)
   */
  async exportAll(request: ExportAllRequest): Promise<Blob> {
    return apiRequest<Blob>(
      '/api/export/all',
      {
        method: 'POST',
        body: JSON.stringify(request),
      }
    )
  },
}

/**
 * JSON 요청을 처리하는 내부 헬퍼 함수
 */
async function apiRequest<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const url = `${API_BASE_URL}${endpoint}`
  
  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  })

  if (!response.ok) {
    let detail: string | undefined
    try {
      const errorData = await response.json()
      detail = errorData.detail || errorData.message
    } catch {
      detail = response.statusText
    }
    
    throw new ApiError(
      `API request failed: ${response.statusText}`,
      response.status,
      detail
    )
  }

  // Export API는 Blob 반환
  const contentType = response.headers.get('content-type')
  if (
    contentType?.includes('application/zip') ||
    contentType?.includes('text/markdown') ||
    (contentType?.includes('application/json') && endpoint.startsWith('/api/export'))
  ) {
    return response.blob() as Promise<T>
  }

  // 일반 JSON 응답
  return response.json()
}

