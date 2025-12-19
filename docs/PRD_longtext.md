# PRD — Cursor 세션 타임라인 & 디버깅 히스토리 정리 앱

## 1. 목적 / 배경
Cursor IDE에서 export된 “세션 대화 마크다운 파일(하루/일정 시간 단위)”을 입력으로 받아,
1) 프로젝트 단계별 진행 작업(Timeline)  
2) 디버깅 이슈 히스토리(Issue Cards)  
를 구조화된 산출물(JSON/Markdown)로 생성한다.

최종 목표는:
- 사람이 읽기 쉬운 “프로젝트 진행 플레이북 + 이슈 해결집”을 축적하고,
- LLM IDE(Cursor Rule 등)에 규칙/노하우로 재사용할 수 있는 형태로 제공하는 것.

---

## 2. 핵심 사용자 시나리오
1) 사용자는 Cursor export 마크다운 파일을 업로드한다.
2) 앱은 파일을 파싱하여 세션 메타(phase/subphase/date/version)와 Turn(사용자/커서 발화)을 구조화한다.
3) 앱은 Timeline과 Issue Cards를 자동 생성한다.
4) 앱은 결과를 미리보기로 보여주고, JSON/MD 및 코드 스니펫 파일을 다운로드할 수 있게 한다.
5) 여러 세션 파일을 순서대로 누적하여 “프로젝트 전체 마스터 타임라인/이슈DB”로 병합할 수 있다.

---

## 3. 입력 / 출력 정의

### 3.1 입력(세션 대화 마크다운 파일)
- 형식: Cursor export 기반 Markdown
- 특징(구조):
  - 문서 상단: Phase/Exported at/Cursor version 등 메타 텍스트
  - 본문: `---` 구분선을 기준으로 Turn 블록
  - Turn 블록: `**User**` / `**Cursor**` 라벨 + 본문
  - 코드 스니펫: ```lang ... ``` 펜스 포함(sql/ts/py/bash/powershell 등)
  - 파일 참조: TODOs.md, *.mdc, backend/*.py, *.ts(x) 등 경로/파일명 텍스트 포함

### 3.2 출력(산출물: JSON + Markdown, 그리고 코드 스니펫 분리 저장)
출력은 “세션 단위”로 생성되며, 옵션으로 “병합(merge)” 산출물도 생성한다.

#### A) Timeline 출력
- `timeline.json`
  - session_meta: {session_id, exported_at, cursor_version, phase, subphase, source_doc}
  - timeline: Event[] (seq, type, phase, subphase, summary, artifacts, signals 등)
- `Timeline.md`
  - 사람이 읽기 쉬운 요약(세션 컨텍스트/완료 항목/다음 단계)

#### B) Issue Cards 출력
- `issues.json`
  - issues: IssueCard[]
- `Issues.md`
  - 카드 형식(증상/원인/증거/조치/검증)

#### C) 코드 스니펫 별도 저장(필수 요구사항)
- `snippets.json`
  - snippet_id, lang, code, source_turn_ref, linked_issue_id(optional), linked_event_seq(optional)
- `snippets/` 디렉토리(선택)
  - `ISSUE-xxx_sql_001.sql`, `ISSUE-xxx_ts_001.ts` 등으로 파일 분리 저장
- Timeline/IssueCards에서 코드 본문은 “직접 포함” 대신:
  - snippet_id 참조(링크) 방식 권장
  - Markdown 렌더에서는 필요 시 “코드 미리보기(접기/펼치기)”로 snippet_id를 통해 로드

---

## 4. 처리 과정(입력→출력 파이프라인)

### 4.1 파이프라인 개요
1) Ingest: 파일 로드 및 기본 정규화(줄바꿈/인코딩)
2) Session Meta 추출: phase/subphase/exported_at/cursor_version 등
3) Turn 파싱: `---` 단위로 블록 분리 → speaker/body/code_blocks/path_candidates 추출
4) Artifact 추출/분류: 문서(md/mdc)/python/ts/sql 등으로 분류 + action(mention/create/modify/execute) 추정
5) Event 정규화:
   - MessageEvent: 사용자 요청/커서 응답 요약
   - ArtifactEvent: 파일 생성/수정/실행/참조
   - DebugEvent: 에러/증상/원인/수정/검증 구조화
6) Timeline 생성: seq 부여 + phase/subphase/session_id 포함하여 시간순 이벤트 배열 생성
7) Issue Cards 생성:
   - DebugEvent들을 이슈 단위로 묶고(트리거 기반),
   - symptom(주로 User), root_cause/fix/validation(주로 Cursor)로 카드 구성
8) Snippet 분리 저장:
   - 코드펜스들을 snippet_id로 분리 저장
   - issue/timeline에서 snippet_id 참조로 연결
9) Output Render:
   - JSON 생성 + Markdown 템플릿 렌더
10) 품질 체크(QA):
   - JSON schema validation(필수)
   - root_cause 미확정은 status=hypothesis
   - path 미해결은 unresolved_paths에 기록

### 4.2 규칙 기반 + LLM 보조(하이브리드)
- 기본 원칙: “구조 추출은 정규식/룰”, “요약/라벨링은 LLM(선택)”
- LLM 사용 지점(옵션):
  - 긴 Cursor 응답을 1~2문장 summary로 압축
  - 디버그 텍스트에서 symptom/root_cause/fix/validation 자동 분해
  - 이슈 카드 분리(한 Turn에 여러 이슈가 섞인 경우)

---

## 5. UI 요구사항(입력 로딩 + 출력 미리보기 중심)

### 5.1 화면 구성(단일 페이지 MVP)
#### (1) 좌측: 입력 패널
- 파일 업로드(드래그&드롭 + 파일 선택)
- 입력 파일 미리보기
  - 상단 “Session Meta Preview” (phase/subphase/exported_at/cursor_version)
  - 원본 텍스트 일부(예: 상단 50줄 또는 선택 영역)
- 파싱 옵션 토글
  - “LLM 요약 사용” (on/off)
  - “코드 스니펫 분리 저장” (on/off, 기본 on)
  - “이슈 탐지 민감도” (low/med/high)

#### (2) 중앙: 결과 미리보기 탭
- 탭 1: Timeline Preview
  - 이벤트 리스트(Seq, Type, Summary)
  - 이벤트 클릭 시: 연관 artifacts/snippets 표시
- 탭 2: Issues Preview
  - 이슈 카드 리스트(제목/상태/phase/subphase)
  - 카드 클릭 시: 증상/원인/조치/검증 + 연결된 snippet 목록
- 탭 3: Snippets Preview
  - 언어별 필터(sql/ts/py)
  - snippet_id, 언어, 코드 일부(접기/펼치기)

#### (3) 우측: Export 패널
- 다운로드 버튼
  - timeline.json / Timeline.md
  - issues.json / Issues.md
  - snippets.json + snippets/zip(선택)
- (선택) “세션 병합” 영역
  - 기존 프로젝트 DB/폴더에서 이전 세션 결과 불러오기
  - merge 후 master_timeline.json / master_issues.json 생성

### 5.2 UX 요구사항
- 업로드 즉시 “파싱 상태/오류”를 명확히 표시
- phase/subphase가 추출되지 않으면 “Unknown”으로 표시하고, 사용자가 수동 입력 가능
- 이슈 카드가 0개면 “이 세션에서 감지된 디버깅 이슈 없음” 안내

---

## 6. 데이터 모델(요약)

### 6.1 Timeline Event(핵심 필드)
- seq: number
- session_id: string
- phase: number|null
- subphase: number|null
- type: enum (status_review|plan|artifact|debug|completion|next_step|turn ...)
- summary: string
- artifacts: [{kind, path, action}]
- snippet_refs: [snippet_id] (optional)

### 6.2 Issue Card(핵심 필드)
- issue_id: string
- scope: {session_id, phase, subphase}
- title: string
- symptoms: string[]
- root_cause: {status: confirmed|hypothesis, text: string}|null
- evidence: [{type, text_or_ref}]
- fix: [{summary, snippet_refs[]}]
- validation: string[]
- related_artifacts: [{path, kind}]

### 6.3 Snippet(핵심 필드)
- snippet_id: string
- lang: string
- code: string
- source: {turn_index, block_index}
- links: {issue_id?, event_seq?}

---

## 7. 범위(MVP) / 비범위

### MVP(1차)
- 단일 세션 md 파일 입력 → timeline/issues/snippets 생성 및 다운로드
- UI: 업로드 + 파싱 결과(Timeline/Issues/Snippets) 미리보기 + export
- 규칙 기반 파싱(정규식) + LLM 요약 옵션(선택)

### 차기(2차)
- 다중 세션 업로드 + 자동 정렬/병합(master timeline/issues)
- 프로젝트별 저장소(세션 결과 히스토리 관리)
- Cursor Rule 자동 생성(“Rule Pack Export”)

---

## 8. 기술 스택(간략)
- 프론트: 웹 UI(React 계열 등)
- 백엔드/처리: Python(FastAPI 등) 또는 Node.js(둘 중 1)
- 저장(옵션): 로컬 파일 기반 또는 경량 DB(SQLite 등)
- LLM(옵션): 요약/라벨링 보조(온/오프 가능)

---

## 9. 성공 기준(Acceptance)
- 입력 파일에서 Turn 블록이 안정적으로 파싱되고(User/Cursor 구분),
- Timeline과 Issue Cards가 JSON/MD로 생성되며,
- 코드 스니펫이 별도(snippets.json + 파일/zip)로 저장되고,
- UI에서 입력 미리보기 + 출력 일부 미리보기 + 다운로드가 가능하다.
- phase/subphase 누락 시에도 “Unknown + 수동 입력”으로 진행 가능하다.

---

## 10. 리스크 / 대응
- 입력 포맷 변형(Cursor 버전/템플릿 변경)
  - 대응: 파서 룰 버전 관리 + fallback(LLM 메타 추출)
- 이슈 카드 과다/과소 탐지
  - 대응: 민감도 옵션 + 사용자 수동 편집(차기)
- 코드 스니펫 과다 포함(민감정보/토큰 부담)
  - 대응: 기본은 “분리 저장 + 본문에는 참조만”
