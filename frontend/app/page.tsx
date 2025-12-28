'use client'

import { useState } from 'react'
import { api, ApiError } from '@/lib/api'
import { FileUpload } from '@/components/FileUpload'
import { SessionMetaPreview } from '@/components/SessionMetaPreview'
import { TimelinePreview } from '@/components/TimelinePreview'
import { IssuesPreview } from '@/components/IssuesPreview'
import { SnippetsPreview } from '@/components/SnippetsPreview'
import type {
  SessionMeta,
  Turn,
  Event,
  TimelineSection,
  IssueCard,
  Snippet,
  ParseResponse,
  TimelineResponse,
  IssuesResponse,
  SnippetsProcessResponse,
} from '@/types/api'

/**
 * 메인 페이지 - 3열 레이아웃
 *
 * 좌측: 입력 패널 (파일 업로드, 세션 메타)
 * 중앙: 결과 미리보기 (Timeline, Issues, Snippets 탭)
 * 우측: Export 패널 (다운로드 기능)
 */
export default function Home() {
  // 상태 관리
  const [sessionMeta, setSessionMeta] = useState<SessionMeta | null>(null)
  const [turns, setTurns] = useState<Turn[]>([])
  const [events, setEvents] = useState<Event[]>([])
  const [timelineSections, setTimelineSections] = useState<TimelineSection[]>([])
  const [issueCards, setIssueCards] = useState<IssueCard[]>([])
  const [snippets, setSnippets] = useState<Snippet[]>([])
  const [activeTab, setActiveTab] = useState<'timeline' | 'issues' | 'snippets'>('timeline')
  const [isProcessing, setIsProcessing] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [processingStep, setProcessingStep] = useState<string>('')

  // window 객체에 api 노출 (브라우저 콘솔에서 테스트용)
  if (typeof window !== 'undefined') {
    ;(window as any).api = api
    ;(window as any).ApiError = ApiError
  }

  /**
   * 전체 파이프라인 실행
   * 파일 업로드 → 파싱 → Timeline 생성 → Issues 생성 → Snippets 처리
   */
  const runPipeline = async (file: File) => {
    setIsProcessing(true)
    setError(null)
    setProcessingStep('파일 업로드 중...')

    try {
      // 1. 파일 업로드 및 파싱
      setProcessingStep('파일 파싱 중...')
      const parseResult: ParseResponse = await api.parseFile(file)
      setSessionMeta(parseResult.session_meta)
      setTurns(parseResult.turns)
      setEvents(parseResult.events)

      // 2. Timeline 생성
      setProcessingStep('Timeline 생성 중...')
      const timelineResult: TimelineResponse = await api.createTimeline({
        session_meta: parseResult.session_meta,
        events: parseResult.events,
        content_hash: parseResult.content_hash,
      })
      setTimelineSections(timelineResult.sections)

      // 3. Issues 생성
      setProcessingStep('Issues 생성 중...')
      const issuesResult: IssuesResponse = await api.createIssues({
        session_meta: parseResult.session_meta,
        turns: parseResult.turns,
        events: parseResult.events,
        content_hash: parseResult.content_hash,
      })
      setIssueCards(issuesResult.issues)

      // 4. Snippets 처리
      setProcessingStep('Snippets 처리 중...')
      const snippetsResult: SnippetsProcessResponse = await api.processSnippets({
        session_meta: parseResult.session_meta,
        turns: parseResult.turns,
        events: parseResult.events,
        issue_cards: issuesResult.issues,
      })
      setSnippets(snippetsResult.snippets)

      setProcessingStep('완료!')
    } catch (err) {
      if (err instanceof ApiError) {
        setError(`API 오류 (${err.statusCode}): ${err.detail || err.message}`)
      } else {
        setError(`오류: ${err instanceof Error ? err.message : String(err)}`)
      }
      setProcessingStep('실패')
      console.error('Pipeline error:', err)
    } finally {
      setIsProcessing(false)
      // 완료 후 1초 뒤에 processingStep 초기화
      setTimeout(() => setProcessingStep(''), 1000)
    }
  }

  const handleFileSelect = async (file: File) => {
    await runPipeline(file)
  }

  const handleMetaUpdate = (updates: Partial<SessionMeta>) => {
    if (sessionMeta) {
      setSessionMeta({ ...sessionMeta, ...updates })
    }
  }

  /**
   * 모든 상태 초기화 (파일 업로드 및 결과 삭제)
   */
  const handleReset = () => {
    setSessionMeta(null)
    setTurns([])
    setEvents([])
    setTimelineSections([])
    setIssueCards([])
    setSnippets([])
    setActiveTab('timeline')
    setError(null)
    setProcessingStep('')
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* 헤더 */}
      <header className="bg-white border-b border-gray-200 px-6 py-4">
        <h1 className="text-2xl font-bold text-gray-900">Longtext Analysis</h1>
        <p className="text-sm text-gray-600 mt-1">Cursor IDE 세션 분석 도구</p>
      </header>

      {/* 메인 컨텐츠 - 3열 레이아웃 */}
      <main className="flex gap-4 p-4 h-[calc(100vh-80px)]">
        {/* 좌측: 입력 패널 */}
        <div className="w-80 bg-white rounded-lg shadow-sm border border-gray-200 p-4 overflow-y-auto">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg font-semibold">입력 패널</h2>
            {sessionMeta && (
              <button
                onClick={handleReset}
                className="text-xs text-red-600 hover:text-red-800 px-2 py-1 rounded hover:bg-red-50 transition-colors"
                disabled={isProcessing}
                title="모든 데이터 초기화"
              >
                초기화
              </button>
            )}
          </div>

          {/* 파일 업로드 컴포넌트 */}
          <FileUpload
            onFileSelect={handleFileSelect}
            isProcessing={isProcessing}
            disabled={false}
          />

          {/* 처리 상태 */}
          {isProcessing && processingStep && (
            <div className="mt-4 p-3 bg-blue-50 rounded-lg">
              <div className="text-sm font-medium text-blue-900">{processingStep}</div>
              <div className="mt-2 w-full bg-blue-200 rounded-full h-2">
                <div className="bg-blue-600 h-2 rounded-full animate-pulse" style={{ width: '100%' }}></div>
              </div>
            </div>
          )}

          {/* 에러 메시지 */}
          {error && (
            <div className="mt-4 p-3 bg-red-50 rounded-lg">
              <div className="text-sm font-medium text-red-900">오류</div>
              <div className="text-xs text-red-700 mt-1">{error}</div>
            </div>
          )}

          {/* 세션 메타 정보 컴포넌트 */}
          <div className="mt-4">
            <SessionMetaPreview
              sessionMeta={sessionMeta}
              onMetaUpdate={handleMetaUpdate}
            />
          </div>

          {/* 통계 정보 */}
          {(turns.length > 0 || events.length > 0) && (
            <div className="mt-4 p-3 bg-gray-50 rounded-lg">
              <h3 className="text-sm font-semibold mb-2">통계</h3>
              <div className="text-xs space-y-1">
                <div>Turns: {turns.length}</div>
                <div>Events: {events.length}</div>
                <div>Timeline Sections: {timelineSections.length}</div>
                <div>Issue Cards: {issueCards.length}</div>
                <div>Snippets: {snippets.length}</div>
              </div>
            </div>
          )}
        </div>

        {/* 중앙: 결과 미리보기 */}
        <div className="flex-1 bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden flex flex-col">
          {/* 탭 헤더 */}
          <div className="border-b border-gray-200 px-4 py-2 flex gap-2">
            <button
              onClick={() => setActiveTab('timeline')}
              className={`px-4 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                activeTab === 'timeline'
                  ? 'bg-blue-50 text-blue-700 border-b-2 border-blue-700'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Timeline ({timelineSections.length})
            </button>
            <button
              onClick={() => setActiveTab('issues')}
              className={`px-4 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                activeTab === 'issues'
                  ? 'bg-blue-50 text-blue-700 border-b-2 border-blue-700'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Issues ({issueCards.length})
            </button>
            <button
              onClick={() => setActiveTab('snippets')}
              className={`px-4 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                activeTab === 'snippets'
                  ? 'bg-blue-50 text-blue-700 border-b-2 border-blue-700'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Snippets ({snippets.length})
            </button>
          </div>

          {/* 탭 컨텐츠 */}
          <div className="flex-1 overflow-y-auto p-4">
            {activeTab === 'timeline' && (
              <TimelinePreview sections={timelineSections} events={events} />
            )}

            {activeTab === 'issues' && <IssuesPreview issues={issueCards} />}

            {activeTab === 'snippets' && <SnippetsPreview snippets={snippets} />}
          </div>
        </div>

        {/* 우측: Export 패널 */}
        <div className="w-72 bg-white rounded-lg shadow-sm border border-gray-200 p-4 overflow-y-auto">
          <h2 className="text-lg font-semibold mb-4">Export</h2>

          {!sessionMeta ? (
            <div className="text-sm text-gray-400 text-center py-8">
              파일을 업로드한 후<br />Export 기능을 사용할 수 있습니다.
            </div>
          ) : (
            <div className="space-y-3">
              <div>
                <h3 className="text-sm font-medium mb-2">Timeline</h3>
                <div className="flex gap-2">
                  <button
                    className="flex-1 px-3 py-2 text-xs bg-blue-50 text-blue-700 rounded hover:bg-blue-100 transition-colors"
                    disabled={timelineSections.length === 0}
                  >
                    JSON
                  </button>
                  <button
                    className="flex-1 px-3 py-2 text-xs bg-blue-50 text-blue-700 rounded hover:bg-blue-100 transition-colors"
                    disabled={timelineSections.length === 0}
                  >
                    MD
                  </button>
                </div>
              </div>

              <div>
                <h3 className="text-sm font-medium mb-2">Issues</h3>
                <div className="flex gap-2">
                  <button
                    className="flex-1 px-3 py-2 text-xs bg-blue-50 text-blue-700 rounded hover:bg-blue-100 transition-colors"
                    disabled={issueCards.length === 0}
                  >
                    JSON
                  </button>
                  <button
                    className="flex-1 px-3 py-2 text-xs bg-blue-50 text-blue-700 rounded hover:bg-blue-100 transition-colors"
                    disabled={issueCards.length === 0}
                  >
                    MD
                  </button>
                </div>
              </div>

              <div>
                <h3 className="text-sm font-medium mb-2">전체</h3>
                <button
                  className="w-full px-3 py-2 text-xs bg-green-50 text-green-700 rounded hover:bg-green-100 transition-colors"
                  disabled={!sessionMeta}
                >
                  ZIP 다운로드
                </button>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  )
}
