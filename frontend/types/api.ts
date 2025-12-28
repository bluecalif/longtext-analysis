/**
 * API 타입 정의
 *
 * 백엔드 Pydantic 모델과 1:1 매핑하는 TypeScript 타입 정의
 * API Contract 동기화를 보장하기 위해 백엔드 모델과 정확히 일치해야 합니다.
 *
 * 참고: backend/core/models.py
 */

// ============================================================================
// Enum 타입 정의 (백엔드 Enum과 정확히 일치)
// ============================================================================

export type EventType =
  | 'status_review'
  | 'plan'
  | 'code_generation'
  | 'debug'
  | 'completion'
  | 'next_step'
  | 'turn'

export type ArtifactAction =
  | 'read'
  | 'create'
  | 'modify'
  | 'execute'
  | 'mention'

export type ExportFormat = 'json' | 'md'

export type IssueStatus = 'confirmed' | 'hypothesis'

// ============================================================================
// 기본 모델 정의
// ============================================================================

export interface SessionMeta {
  session_id: string
  exported_at?: string
  cursor_version?: string
  phase?: number
  subphase?: number
  source_doc: string
}

export interface CodeBlock {
  turn_index: number
  block_index: number
  lang: string
  code: string
}

export interface Turn {
  turn_index: number
  speaker: string // "User", "Cursor", "Unknown"
  body: string
  code_blocks: CodeBlock[]
  path_candidates: string[]
}

export interface Event {
  seq: number
  session_id: string
  turn_ref: number
  phase?: number
  subphase?: number
  type: EventType
  summary: string
  artifacts: Array<{
    kind?: string
    path?: string
    action?: ArtifactAction | string
    [key: string]: unknown
  }>
  snippet_refs: string[]
  processing_method: string // "regex" 또는 "llm"
}

export interface TimelineEvent {
  seq: number
  session_id: string
  phase?: number
  subphase?: number
  type: EventType
  summary: string
  artifacts: Array<{
    kind?: string
    path?: string
    action?: ArtifactAction | string
    [key: string]: unknown
  }>
  snippet_refs: string[]
}

export interface TimelineSection {
  section_id: string
  title: string
  summary: string
  phase?: number
  subphase?: number
  events: number[] // Event seq 리스트
  has_issues: boolean
  issue_refs: string[] // Issue Card ID 리스트
  detailed_results: {
    code_snippets?: string[]
    files?: string[]
    artifacts?: Array<{
      path: string
      action: ArtifactAction | string
      [key: string]: unknown
    }>
    git_commit?: string
    [key: string]: unknown
  }
}

export interface IssueCard {
  issue_id: string
  scope: {
    session_id: string
    phase?: number
    subphase?: number
    [key: string]: unknown
  }
  title: string
  symptoms: string[]
  root_cause?: {
    status: IssueStatus
    text: string
    [key: string]: unknown
  }
  evidence: Array<{
    type?: string
    text_or_ref?: string
    [key: string]: unknown
  }>
  fix: Array<{
    summary: string
    snippet_refs?: string[]
    [key: string]: unknown
  }>
  validation: string[]
  related_artifacts: Array<{
    path?: string
    kind?: string
    [key: string]: unknown
  }>
  snippet_refs: string[]
  // Phase 4.7 추가 필드
  section_id?: string
  section_title?: string
  related_events: number[] // Event seq 리스트
  related_turns: number[] // Turn 인덱스 리스트
  confidence_score?: number // 0.0 ~ 1.0
}

export interface Snippet {
  snippet_id: string
  lang: string
  code: string
  source: {
    turn_index: number
    block_index: number
    [key: string]: unknown
  }
  links: {
    issue_id?: string
    event_seq?: number
    paths?: string[]
    [key: string]: unknown
  }
  snippet_hash: string
  aliases: string[]
}

// ============================================================================
// API Request/Response 타입 정의
// ============================================================================

export interface ParseResponse {
  session_meta: SessionMeta
  turns: Turn[]
  events: Event[]
  content_hash?: string
}

export interface TimelineRequest {
  session_meta: SessionMeta
  events: Event[]
  issue_cards?: IssueCard[]
  content_hash?: string
}

export interface TimelineResponse {
  session_meta: SessionMeta
  sections: TimelineSection[]
  events: TimelineEvent[]
}

export interface IssuesRequest {
  session_meta: SessionMeta
  turns: Turn[]
  events: Event[]
  timeline_sections?: TimelineSection[]
  content_hash?: string
}

export interface IssuesResponse {
  session_meta: SessionMeta
  issues: IssueCard[]
}

export interface SnippetResponse {
  snippet: Snippet
}

export interface SnippetsProcessRequest {
  session_meta: SessionMeta
  turns: Turn[]
  events: Event[]
  issue_cards: IssueCard[]
}

export interface SnippetsProcessResponse {
  session_meta: SessionMeta
  snippets: Snippet[]
  events: Event[]
  issue_cards: IssueCard[]
}

export interface ExportTimelineRequest {
  session_meta: SessionMeta
  sections: TimelineSection[]
  events: TimelineEvent[]
  format?: ExportFormat
}

export interface ExportIssuesRequest {
  session_meta: SessionMeta
  issues: IssueCard[]
  format?: ExportFormat
}

export interface ExportAllRequest {
  session_meta: SessionMeta
  sections: TimelineSection[]
  events: TimelineEvent[]
  issues: IssueCard[]
  snippets: Snippet[]
  format?: ExportFormat
}

