****# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**:
- 백엔드: Python FastAPI (Poetry)
- 프론트엔드: Next.js 14+ (App Router, TypeScript)
- LLM: OpenAI API (옵션, 요약/라벨링 보조)
- 저장: 로컬 파일 기반 (JSON/MD)
- 배포: 로컬 개발 환경

**참고 문서**:
- [PRD](docs/PRD_longtext.md)
- [상세 지침](docs/instruction_detail.md)
- [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**:
- 실제 Cursor export 파일: `docs/cursor_phase_6_3.md` (각 Phase별 E2E 테스트에서 사용)

---

## 아키텍처 개요

```
마크다운 파일 업로드
  ↓
Ingest & Normalize
  ↓
Session Meta 추출
  ↓
Turn 파싱
  ↓
Artifact 추출
  ↓
Event 정규화
  ↓
Timeline 생성 + Issue Cards 생성 + 코드 스니펫 분리
  ↓
JSON/MD 출력
  ↓
다운로드
```

---

## Phase 1: 프로젝트 초기 설정 및 환경 구성

**목표**: 프로젝트 기본 구조 생성 및 개발 환경 설정

### 백엔드 설정
- [ ] Poetry 프로젝트 초기화 (`pyproject.toml`, `poetry.lock`)
- [ ] 백엔드 의존성 패키지 설치
  - [ ] `fastapi`
  - [ ] `uvicorn`
  - [ ] `pydantic`
  - [ ] `python-dotenv`
  - [ ] `openai`
  - [ ] `regex`
- [ ] 백엔드 디렉토리 구조 생성
  - [ ] `backend/parser/` (마크다운 파서 모듈)
  - [ ] `backend/builders/` (Timeline/Issue Cards 빌더)
  - [ ] `backend/render/` (Markdown 렌더러)
  - [ ] `backend/api/routes/` (FastAPI 라우터)
  - [ ] `backend/core/` (상수, 유틸리티)

### 프론트엔드 설정
- [ ] Next.js 프로젝트 초기화 (`frontend/` 디렉토리)
- [ ] 프론트엔드 의존성 패키지 설치
  - [ ] `next`
  - [ ] `react`
  - [ ] `typescript`
  - [ ] `tailwindcss`
  - [ ] `shadcn/ui` (선택)
- [ ] 프론트엔드 디렉토리 구조 생성
  - [ ] `frontend/app/` (App Router 페이지)
  - [ ] `frontend/components/` (UI 컴포넌트)
  - [ ] `frontend/lib/` (유틸리티, API 클라이언트)
  - [ ] `frontend/types/` (TypeScript 타입 정의)

### 프로젝트 공통 설정
- [ ] `tests/` 디렉토리 생성
  - [ ] `tests/fixtures/` (샘플 마크다운 파일)
  - [ ] `tests/golden/` (예상 결과)
- [ ] `.env` 파일 템플릿 생성 (OpenAI API 키 등)
- [ ] `.env.example` 파일 생성
- [ ] `.gitignore` 설정
- [ ] `README.md` 작성
- [ ] Cursor Rules 초기 설정 (`.cursor/rules/`)
  - [ ] `backend-api.mdc` (API 설계 규칙)
  - [ ] `parser-rules.mdc` (파서 규칙)
  - [ ] `api-contract-sync.mdc` (API 계약 동기화)

**산출물**: 프로젝트 기본 구조, 개발 환경 설정 완료, 기본 README 및 문서

---

## Phase 2: 백엔드 파서 구현 (마크다운 파싱)

**목표**: Cursor export 마크다운 파일을 구조화된 데이터로 파싱

### 텍스트 정규화 (`backend/parser/normalize.py`)
- [ ] 줄바꿈 통일 (`\r\n` → `\n`, `\r` → `\n`)
- [ ] BOM 제거 (`\ufeff`)
- [ ] 공백 정리 (코드블록 제외 옵션)
- [ ] 트레일링 공백 제거
- [ ] 너무 긴 공백 축소 (3개 이상 → 2개, 코드블록 제외)

### 세션 메타 추출 (`backend/parser/meta.py`)
- [ ] Phase 추출 (정규식: `(?i)\bPhase\s+(\d+)\b`)
- [ ] Subphase 추출 (정규식: `(?i)\bSub\s*Phase\s+(\d+)\b`)
- [ ] Exported at 추출 (정규식: `(?i)Exported\s+(\d{4}-\d{2}-\d{2}[^,\n]*?(?:KST|UTC|GMT|[+\-]\d{2}:\d{2})?)`)
- [ ] Cursor version 추출 (정규식: `(?i)\bCursor\s+(\d+\.\d+\.\d+)\b`)
- [ ] Session ID 생성 규칙 구현 (`cursor_export_{exported_at_or_fallback}`)
- [ ] 상단 2000~4000 chars 범위에서 best-effort 추출

### Turn 블록 파싱 (`backend/parser/turns.py`)
- [ ] 구분선(`---`) 기준 분할 (정규식: `^\s*---\s*$`)
- [ ] Speaker 추출 (정규식: `^\s*\*\*(User|Cursor)\*\*\s*$`)
- [ ] Body 텍스트 추출 (코드블록 제외)
- [ ] Fallback 파서 구현 (구분선 없을 때 `**User**`/`**Cursor**` 라벨 기준)
- [ ] Parse Health Check (Unknown 비율 높으면 포맷 감지 실패 처리)

### 코드 스니펫 추출 (`backend/parser/snippets.py`)
- [ ] 코드펜스 추출 (정규식: ````(\w+)?\n(.*?)```)
- [ ] 언어 판별 (lang 누락 시 빈 문자열 처리)
- [ ] 스니펫 중복 제거 로직
- [ ] 스니펫 ID 생성 규칙

### Artifact 추출 (`backend/parser/artifacts.py`)
- [ ] 파일/경로 후보 추출 (정규식 기반)
- [ ] 파일 타입 분류 (md/mdc/py/ts/tsx/sql 등)
- [ ] Action 추정 (mention/create/modify/execute)

### 테스트
**⚠️ 중요**: AGENTS.md 규칙 준수 - 단위 테스트는 실제 데이터 사용, Mock 사용 절대 금지

- [ ] `tests/test_parser.py` 작성
  - [ ] `test_normalize()` - 정규화 테스트 (실제 데이터 사용)
  - [ ] `test_meta_extraction()` - 메타 추출 테스트 (실제 데이터 사용)
  - [ ] `test_turn_parsing()` - Turn 파싱 테스트 (실제 데이터 사용)
  - [ ] `test_snippet_extraction()` - 스니펫 추출 테스트 (실제 데이터 사용)
  - [ ] `test_artifact_extraction()` - Artifact 추출 테스트 (실제 데이터 사용)
- [ ] `tests/fixtures/*.md` 샘플 마크다운 파일 준비
  - [ ] `tests/fixtures/cursor_phase_6_3.md` (실제 입력 데이터 복사)
- [ ] `tests/golden/*.json` 예상 결과 (Golden 파일) 준비
  - [ ] Golden 파일 비교 테스트 구현 (회귀 테스트용)

### E2E 테스트 (Phase 2 완료 검증)
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

- [ ] `tests/test_parser_e2e.py` 작성
  - [ ] **실제 입력 데이터 사용**: `docs/cursor_phase_6_3.md` 파일로 전체 파서 파이프라인 테스트
  - [ ] **정합성 검증**: 파싱 결과의 구조적 정확성 확인
    - [ ] Session Meta 추출 정확성 (phase, subphase, exported_at, cursor_version)
    - [ ] Turn 블록 분할 정확성 (User/Cursor 구분)
    - [ ] 코드 스니펫 추출 정확성 (언어 판별, 중복 제거)
    - [ ] Artifact 추출 정확성 (파일 경로, 타입 분류)
  - [ ] **타당성 검증**: 실제 상황에서의 파싱 품질 확인
    - [ ] 파싱 실패율 검증 (Unknown speaker 비율 < 20%)
    - [ ] 누락된 정보 처리 확인
    - [ ] 예외 케이스 처리 확인
  - [ ] **결과 분석 및 자동 보고**: 파싱 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 실행 후 자동으로 상세 보고 출력 (사용자 질문 없이)
    - [ ] 정량적 데이터 제시 (total_turns, user_turns, cursor_turns, unknown_ratio, code_blocks 수 등)
    - [ ] 문제 발견 시 원인 분석 포함
    - [ ] 리포트 파일 저장 (`tests/reports/parser_e2e_report.json`)

**산출물**: 완전한 파서 모듈, 단위 테스트 및 테스트 데이터, 파싱 결과 데이터 모델 (Pydantic), E2E 테스트 완료 및 검증 리포트

---

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

### 데이터 모델 정의 (`backend/core/models.py`)
- [ ] `SessionMeta` 모델 정의
  - [ ] `session_id: str`
  - [ ] `exported_at: Optional[str]`
  - [ ] `cursor_version: Optional[str]`
  - [ ] `phase: Optional[int]`
  - [ ] `subphase: Optional[int]`
  - [ ] `source_doc: str`
- [ ] `Turn` 모델 정의
  - [ ] `speaker: str` (User/Cursor/Unknown)
  - [ ] `body: str`
  - [ ] `code_blocks: List[CodeBlock]`
  - [ ] `path_candidates: List[str]`
- [ ] `Event` 기본 모델 정의
- [ ] `MessageEvent` 모델 정의 (사용자 요청/응답 이벤트)
- [ ] `ArtifactEvent` 모델 정의 (파일 생성/수정 이벤트)
- [ ] `DebugEvent` 모델 정의 (디버깅 이벤트)

### 이벤트 정규화 (`backend/builders/event_normalizer.py`)
- [ ] Turn → Event 변환 로직 구현
- [ ] Event 타입 분류 로직
  - [ ] `status_review`
  - [ ] `plan`
  - [ ] `artifact`
  - [ ] `debug`
  - [ ] `completion`
  - [ ] `next_step`
  - [ ] `turn`
- [ ] Phase/Subphase 연결 로직
- [ ] Artifact 연결 로직
- [ ] Snippet 참조 연결 로직

### LLM 서비스 (`backend/core/llm_service.py`) - 옵션
- [ ] OpenAI API 클라이언트 구현
- [ ] 긴 Cursor 응답 요약 기능
- [ ] 디버그 텍스트에서 symptom/root_cause/fix/validation 추출 기능
- [ ] 캐싱 로직 구현 (동일 입력 재사용)
  - [ ] 파일 기반 캐시 또는 메모리 캐시
  - [ ] 캐시 키 생성 규칙 (입력 텍스트 해시)

### 테스트
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지 (LLM은 캐싱으로 처리)

- [ ] `tests/test_event_normalizer.py` 작성
  - [ ] `test_turn_to_event_conversion()` - Turn → Event 변환 테스트 (실제 데이터 사용)
  - [ ] `test_event_type_classification()` - 이벤트 타입 분류 테스트 (실제 데이터 사용)
  - [ ] `test_artifact_linking()` - Artifact 연결 테스트 (실제 데이터 사용)
  - [ ] `test_snippet_linking()` - Snippet 참조 연결 테스트 (실제 데이터 사용)
- [ ] LLM 서비스 테스트 (캐싱 확인)
  - [ ] LLM 호출 결과 캐싱 확인 (파일 기반 캐시)
  - [ ] 동일 입력 재사용 확인

### E2E 테스트 (Phase 3 완료 검증)
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

- [ ] `tests/test_event_normalizer_e2e.py` 작성
  - [ ] **실제 입력 데이터 사용**: Phase 2에서 파싱한 `docs/cursor_phase_6_3.md` 결과를 입력으로 사용
  - [ ] **정합성 검증**: 이벤트 정규화 결과의 구조적 정확성 확인
    - [ ] Turn → Event 변환 정확성
    - [ ] Event 타입 분류 정확성 (status_review/plan/artifact/debug/completion/next_step/turn)
    - [ ] Phase/Subphase 연결 정확성
    - [ ] Artifact 연결 정확성
    - [ ] Snippet 참조 연결 정확성
  - [ ] **타당성 검증**: 실제 상황에서의 이벤트 정규화 품질 확인
    - [ ] 이벤트 타입 분류의 적절성
    - [ ] 연결 관계의 정확성
    - [ ] LLM 요약 품질 (LLM 사용 시, 캐싱 확인)
  - [ ] **결과 분석 및 자동 보고**: 이벤트 정규화 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 실행 후 자동으로 상세 보고 출력 (사용자 질문 없이)
    - [ ] 정량적 데이터 제시 (total_events, event_type_distribution, artifact_linking_rate 등)
    - [ ] 문제 발견 시 원인 분석 포함
    - [ ] 리포트 파일 저장 (`tests/reports/event_normalizer_e2e_report.json`)

**산출물**: 이벤트 정규화 모듈, LLM 서비스 (옵션), 이벤트 데이터 모델, E2E 테스트 완료 및 검증 리포트

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

### 상수 정의 (`backend/core/constants.py`)
- [ ] Event 타입 Enum 정의
- [ ] Issue 상태 Enum 정의 (`confirmed`, `hypothesis`)
- [ ] 파일 타입 목록 정의

### Timeline 생성 (`backend/builders/timeline_builder.py`)
- [ ] 이벤트 시퀀스 번호 부여 로직
- [ ] Phase/Subphase별 그룹화 로직
- [ ] 요약 생성 (LLM 옵션)
- [ ] Artifact 연결 로직
- [ ] Snippet 참조 연결 로직
- [ ] Timeline JSON 구조 생성

### Issue Cards 생성 (`backend/builders/issues_builder.py`)
- [ ] DebugEvent 기반 이슈 탐지 로직
- [ ] 이슈 그룹화 로직 (트리거 기반)
- [ ] Symptom 추출 (주로 User 발화)
- [ ] Root cause 추출 (주로 Cursor 발화, LLM 옵션)
- [ ] Fix 추출
- [ ] Validation 추출
- [ ] 관련 Artifact 연결 로직
- [ ] Snippet 참조 연결 로직
- [ ] Issue Cards JSON 구조 생성

### 테스트
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

- [ ] `tests/test_timeline_builder.py` 작성
  - [ ] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트 (실제 데이터 사용)
  - [ ] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트 (실제 데이터 사용)
  - [ ] `test_timeline_artifact_linking()` - Artifact 연결 테스트 (실제 데이터 사용)
- [ ] `tests/test_issues_builder.py` 작성
  - [ ] `test_issue_detection()` - 이슈 탐지 테스트 (실제 데이터 사용)
  - [ ] `test_issue_grouping()` - 이슈 그룹화 테스트 (실제 데이터 사용)
  - [ ] `test_symptom_extraction()` - Symptom 추출 테스트 (실제 데이터 사용)
  - [ ] `test_root_cause_extraction()` - Root cause 추출 테스트 (실제 데이터 사용)
- [ ] Golden 파일 비교 테스트 작성
  - [ ] Timeline Golden 파일 비교
  - [ ] Issues Golden 파일 비교

### E2E 테스트 (Phase 4 완료 검증)
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

- [ ] `tests/test_timeline_issues_e2e.py` 작성
  - [ ] **실제 입력 데이터 사용**: Phase 3에서 정규화한 이벤트를 입력으로 사용
  - [ ] **정합성 검증**: Timeline 및 Issue Cards 생성 결과의 구조적 정확성 확인
    - [ ] Timeline 시퀀스 번호 부여 정확성
    - [ ] Timeline Phase/Subphase 그룹화 정확성
    - [ ] Timeline Artifact/Snippet 연결 정확성
    - [ ] Issue Cards 탐지 정확성 (DebugEvent 기반)
    - [ ] Issue Cards 그룹화 정확성
    - [ ] Issue Cards symptom/root_cause/fix/validation 추출 정확성
    - [ ] Issue Cards Artifact/Snippet 연결 정확성
  - [ ] **타당성 검증**: 실제 상황에서의 Timeline/Issue Cards 품질 확인
    - [ ] Timeline 요약의 적절성
    - [ ] Issue Cards 탐지의 적절성 (과다/과소 탐지 확인)
    - [ ] Issue Cards 내용의 완전성 (symptom/root_cause/fix/validation)
  - [ ] **JSON Schema 검증**: 생성된 Timeline/Issue Cards JSON이 스키마를 준수하는지 확인
  - [ ] **결과 분석 및 자동 보고**: Timeline/Issue Cards 생성 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 실행 후 자동으로 상세 보고 출력 (사용자 질문 없이)
    - [ ] 정량적 데이터 제시 (timeline_events_count, issues_count, linking_completeness 등)
    - [ ] 문제 발견 시 원인 분석 포함
    - [ ] 리포트 파일 저장 (`tests/reports/timeline_issues_e2e_report.json`)

**산출물**: Timeline 빌더 모듈, Issue Cards 빌더 모듈, Timeline/Issue Cards 데이터 모델, E2E 테스트 완료 및 검증 리포트

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

### 스니펫 관리 (`backend/builders/snippet_manager.py`)
- [ ] 스니펫 ID 생성 규칙 구현
- [ ] 스니펫 중복 제거 로직
  - [ ] 코드 내용 해시 기반 중복 검사
- [ ] 스니펫 파일 저장 기능 (선택: `snippets/` 디렉토리)
  - [ ] 파일명 규칙: `ISSUE-xxx_lang_001.ext`
- [ ] Issue/Timeline과의 링킹 로직

### 스니펫 저장소 (`backend/core/snippet_storage.py`)
- [ ] `snippets.json` 생성 로직
- [ ] 파일별 저장 기능 (선택)
- [ ] ZIP 압축 기능 (선택)
- [ ] 스니펫 조회 API 준비

### 테스트
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트 (실제 데이터 사용)
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트 (실제 데이터 사용)
  - [ ] `test_snippet_linking()` - 링킹 테스트 (실제 데이터 사용)
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트 (실제 파일 시스템 사용)

### E2E 테스트 (Phase 5 완료 검증)
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

- [ ] `tests/test_snippet_e2e.py` 작성
  - [ ] **실제 입력 데이터 사용**: Phase 2에서 추출한 코드 스니펫과 Phase 4에서 생성한 Timeline/Issue Cards를 입력으로 사용
  - [ ] **정합성 검증**: 스니펫 분리 및 저장 결과의 구조적 정확성 확인
    - [ ] 스니펫 ID 생성 규칙 준수
    - [ ] 스니펫 중복 제거 정확성
    - [ ] 스니펫 파일 저장 정확성 (파일명 규칙, 내용)
    - [ ] Issue/Timeline과의 링킹 정확성
    - [ ] `snippets.json` 생성 정확성
  - [ ] **타당성 검증**: 실제 상황에서의 스니펫 관리 품질 확인
    - [ ] 중복 제거 효과 확인
    - [ ] 링킹의 완전성 확인
    - [ ] 파일 저장의 적절성 확인
  - [ ] **결과 분석 및 자동 보고**: 스니펫 분리 및 저장 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 실행 후 자동으로 상세 보고 출력 (사용자 질문 없이)
    - [ ] 정량적 데이터 제시 (total_snippets, deduplication_rate, linking_completeness 등)
    - [ ] 문제 발견 시 원인 분석 포함
    - [ ] 리포트 파일 저장 (`tests/reports/snippet_e2e_report.json`)

**산출물**: 스니펫 관리 모듈, 스니펫 저장소 모듈, E2E 테스트 완료 및 검증 리포트

---

## Phase 6: 백엔드 API 구현

**목표**: FastAPI 엔드포인트 구현

### 파싱 API (`backend/api/routes/parse.py`)
- [ ] `POST /api/parse` 엔드포인트 구현
  - [ ] 파일 업로드 처리 (multipart/form-data)
  - [ ] 파싱 실행
  - [ ] 파싱 결과 반환 (SessionMeta, Turns, Events)

### Timeline API (`backend/api/routes/timeline.py`)
- [ ] `POST /api/timeline` 엔드포인트 구현
  - [ ] 요청: 파싱 결과 또는 세션 ID
  - [ ] Timeline 생성
  - [ ] Timeline JSON 반환

### Issues API (`backend/api/routes/issues.py`)
- [ ] `POST /api/issues` 엔드포인트 구현
  - [ ] 요청: 파싱 결과 또는 세션 ID
  - [ ] Issue Cards 생성
  - [ ] Issues JSON 반환

### Snippets API (`backend/api/routes/snippets.py`)
- [ ] `GET /api/snippets/{snippet_id}` 엔드포인트 구현
  - [ ] 스니펫 조회
- [ ] `POST /api/snippets/export` 엔드포인트 구현
  - [ ] 스니펫 다운로드 (ZIP)

### Export API (`backend/api/routes/export.py`)
- [ ] `POST /api/export/timeline` 엔드포인트 구현
  - [ ] Timeline JSON/MD 다운로드
- [ ] `POST /api/export/issues` 엔드포인트 구현
  - [ ] Issues JSON/MD 다운로드
- [ ] `POST /api/export/all` 엔드포인트 구현
  - [ ] 전체 산출물 다운로드 (ZIP)

### Markdown 렌더러 (`backend/render/render_md.py`)
- [ ] Timeline Markdown 템플릿 구현
- [ ] Issues Markdown 템플릿 구현
- [ ] Snippets 목록 Markdown 구현

### FastAPI 앱 초기화 (`backend/main.py`)
- [ ] FastAPI 앱 생성
- [ ] CORS 설정
- [ ] 라우터 등록
  - [ ] `/api/parse`
  - [ ] `/api/timeline`
  - [ ] `/api/issues`
  - [ ] `/api/snippets`
  - [ ] `/api/export`
- [ ] 예외 처리 미들웨어
- [ ] OpenAPI/Swagger 문서 자동 생성 확인

### 테스트
**⚠️ 중요**: AGENTS.md 규칙 준수 - 단위 테스트는 실제 데이터 사용, Mock 사용 절대 금지

- [ ] `tests/test_api.py` 작성 (단위 테스트 - 실제 서버 실행 없이 함수 직접 호출)
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트 (실제 데이터 사용)
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트 (실제 데이터 사용)
  - [ ] `test_issues_endpoint()` - Issues API 테스트 (실제 데이터 사용)
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트 (실제 데이터 사용)
  - [ ] `test_export_endpoint()` - Export API 테스트 (실제 데이터 사용)
  
**참고**: 실제 서버 실행 E2E 테스트는 아래 "E2E 테스트" 섹션에서 진행

### E2E 테스트 (Phase 6 완료 검증 - 백엔드 서버 단계 최종 검증)
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 서버 실행 필수, TestClient 사용 금지, Mock 사용 절대 금지

- [ ] `tests/conftest_e2e.py` fixture 작성
  - [ ] `test_server` fixture: 실제 uvicorn 서버 실행
    - [ ] 서버 시작 대기 로직 (최대 30회 재시도)
    - [ ] 서버 종료 자동화
  - [ ] `httpx.Client` fixture: 실제 HTTP 요청 클라이언트
    - [ ] `TestClient` 사용 금지 (백그라운드 작업이 제대로 실행되지 않음)
    - [ ] 타임아웃 설정 (30초)
  - [ ] 서버 시작/종료 자동화
- [ ] `tests/test_api_e2e.py` 작성
  - [ ] **실제 입력 데이터 사용**: `docs/cursor_phase_6_3.md` 파일을 실제로 업로드하여 전체 파이프라인 테스트
  - [ ] **정합성 검증**: API 응답의 구조적 정확성 확인
    - [ ] `POST /api/parse` 엔드포인트 테스트
      - [ ] 파일 업로드 처리 정확성
      - [ ] 파싱 결과 반환 정확성 (SessionMeta, Turns, Events)
      - [ ] 응답 스키마 검증
    - [ ] `POST /api/timeline` 엔드포인트 테스트
      - [ ] Timeline 생성 정확성
      - [ ] Timeline JSON 구조 검증
      - [ ] Artifact/Snippet 연결 확인
    - [ ] `POST /api/issues` 엔드포인트 테스트
      - [ ] Issue Cards 생성 정확성
      - [ ] Issues JSON 구조 검증
      - [ ] Issue Cards 내용 완전성 확인
    - [ ] `GET /api/snippets/{snippet_id}` 엔드포인트 테스트
      - [ ] 스니펫 조회 정확성
    - [ ] `POST /api/snippets/export` 엔드포인트 테스트
      - [ ] 스니펫 ZIP 다운로드 정확성
    - [ ] `POST /api/export/timeline` 엔드포인트 테스트
      - [ ] Timeline JSON/MD 다운로드 정확성
    - [ ] `POST /api/export/issues` 엔드포인트 테스트
      - [ ] Issues JSON/MD 다운로드 정확성
    - [ ] `POST /api/export/all` 엔드포인트 테스트
      - [ ] 전체 산출물 ZIP 다운로드 정확성
  - [ ] **타당성 검증**: 실제 상황에서의 API 동작 품질 확인
    - [ ] 전체 파이프라인 E2E 테스트 (파일 업로드 → 파싱 → Timeline 생성 → Issues 생성 → Export)
    - [ ] 에러 처리 확인 (잘못된 파일 형식, 누락된 필드 등)
    - [ ] 성능 확인 (대용량 파일 처리 시간)
  - [ ] **프론트엔드 구현 전 백엔드 서비스 완전성 검증**
    - [ ] 모든 API 엔드포인트가 정상 동작하는지 확인
    - [ ] API 응답 형식이 프론트엔드에서 사용 가능한지 확인
    - [ ] 에러 응답 형식의 일관성 확인
    - [ ] CORS 설정 확인
  - [ ] **결과 분석 및 자동 보고**: API E2E 테스트 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 실행 후 자동으로 상세 보고 출력 (사용자 질문 없이)
    - [ ] 정량적 데이터 제시 (각 엔드포인트 응답 시간, 성공률, 에러 케이스 등)
    - [ ] 문제 발견 시 원인 분석 포함
    - [ ] 테스트 결과 리포트 생성 (`tests/reports/api_e2e_report.json`)
    - [ ] 발견된 문제점 및 개선 사항 문서화
  - [ ] **백엔드 서비스 완전성 검증 (프론트엔드 구현 전 필수)**
    - [ ] 모든 API 엔드포인트가 정상 동작하는지 확인
    - [ ] API 응답 형식이 프론트엔드에서 사용 가능한지 확인
    - [ ] 에러 응답 형식의 일관성 확인
    - [ ] CORS 설정 확인
    - [ ] 백엔드 E2E 테스트 완료 후에만 Phase 7(프론트엔드) 진행

**산출물**: 완전한 FastAPI 백엔드, API 문서 (OpenAPI/Swagger), E2E 테스트 완료 및 검증 리포트, 백엔드 서비스 완전성 검증 완료

---

## Phase 7: 프론트엔드 UI 구현

**목표**: Next.js 기반 웹 UI 구현

### 메인 페이지 (`frontend/app/page.tsx`)
- [ ] 레이아웃 구성
  - [ ] 좌측: 입력 패널
  - [ ] 중앙: 결과 미리보기 탭
  - [ ] 우측: Export 패널
- [ ] 상태 관리 (React hooks)
- [ ] API 연동 로직

### 입력 패널 컴포넌트
- [ ] `frontend/components/FileUpload.tsx` 구현
  - [ ] 드래그&드롭 기능
  - [ ] 파일 선택 기능
  - [ ] 파일 미리보기
- [ ] `frontend/components/SessionMetaPreview.tsx` 구현
  - [ ] Session Meta 표시
  - [ ] Phase/Subphase 수동 입력 기능 (누락 시)
- [ ] 파싱 옵션 토글 구현
  - [ ] LLM 사용 on/off
  - [ ] 스니펫 분리 저장 on/off
  - [ ] 이슈 탐지 민감도 (low/med/high)

### 결과 미리보기 컴포넌트
- [ ] `frontend/components/TimelinePreview.tsx` 구현
  - [ ] 이벤트 리스트 표시 (Seq, Type, Summary)
  - [ ] 이벤트 클릭 시 연관 artifacts/snippets 표시
- [ ] `frontend/components/IssuesPreview.tsx` 구현
  - [ ] 이슈 카드 리스트 표시 (제목/상태/phase/subphase)
  - [ ] 카드 클릭 시 증상/원인/조치/검증 + 연결된 snippet 목록 표시
- [ ] `frontend/components/SnippetsPreview.tsx` 구현
  - [ ] 언어별 필터 (sql/ts/py)
  - [ ] snippet_id, 언어, 코드 일부 표시 (접기/펼치기)

### Export 패널
- [ ] 다운로드 버튼 구현
  - [ ] timeline.json / Timeline.md
  - [ ] issues.json / Issues.md
  - [ ] snippets.json + snippets/zip (선택)

### API 클라이언트 (`frontend/lib/api.ts`)
- [ ] 파일 업로드 함수
- [ ] 파싱 요청 함수
- [ ] Timeline 생성 요청 함수
- [ ] Issues 생성 요청 함수
- [ ] 다운로드 함수

### 타입 정의 (`frontend/types/api.ts`)
- [ ] 백엔드 Pydantic 모델과 동기화된 TypeScript 타입 정의
  - [ ] `SessionMeta`
  - [ ] `TimelineEvent`
  - [ ] `IssueCard`
  - [ ] `Snippet`
  - [ ] API 요청/응답 타입

### 상수 정의 (`frontend/lib/constants.ts`)
- [ ] 백엔드 constants와 동기화된 상수
  - [ ] Event 타입
  - [ ] Issue 상태
  - [ ] 파일 타입 목록

### 스타일링
- [ ] Tailwind CSS 설정
- [ ] shadcn/ui 컴포넌트 설정 (선택)
- [ ] 반응형 디자인 구현
- [ ] 다크모드 지원 (선택)

### 테스트
- [ ] 컴포넌트 단위 테스트 작성 (선택)
- [ ] E2E 테스트 작성 (Playwright 등, 선택)

**산출물**: 완전한 Next.js 프론트엔드, 반응형 UI, API 연동 완료

---

## Phase 8: 통합 테스트 및 QA

**목표**: 전체 시스템 통합 테스트 및 품질 보증

### 통합 테스트
- [ ] `tests/test_integration.py` 작성
  - [ ] 전체 파이프라인 E2E 테스트
    - [ ] 실제 입력 데이터 사용: `docs/cursor_phase_6_3.md` 파일로 전체 시스템 테스트
    - [ ] 백엔드 + 프론트엔드 통합 테스트
  - [ ] 다양한 마크다운 파일 형식 테스트
  - [ ] 에러 케이스 테스트
- [ ] 실제 Cursor export 파일로 테스트
  - [ ] `docs/cursor_phase_6_3.md` 파일로 실제 시나리오 테스트
- [ ] 대용량 파일 처리 테스트

### 품질 체크 (QA)
- [ ] JSON Schema 검증 구현
- [ ] root_cause 미확정 → status=hypothesis 처리
- [ ] path 미해결 → unresolved_paths 기록
- [ ] 파싱 실패 케이스 처리
- [ ] 에러 메시지 명확성 확인

### 성능 최적화
- [ ] 대용량 파일 처리 최적화
- [ ] LLM 호출 최적화 (캐싱 강화)
- [ ] 프론트엔드 로딩 성능 최적화

### 문서화
- [ ] API 문서 업데이트 (OpenAPI/Swagger)
- [ ] 사용자 가이드 작성
- [ ] 개발자 가이드 작성
- [ ] README.md 업데이트

**산출물**: 통합 테스트 완료, 품질 보증 완료, 문서화 완료

---

## 데이터 모델

### SessionMeta
```python
class SessionMeta(BaseModel):
    session_id: str
    exported_at: Optional[str]
    cursor_version: Optional[str]
    phase: Optional[int]
    subphase: Optional[int]
    source_doc: str
```

### Timeline Event
```python
class TimelineEvent(BaseModel):
    seq: int
    session_id: str
    phase: Optional[int]
    subphase: Optional[int]
    type: EventType  # status_review|plan|artifact|debug|completion|next_step|turn
    summary: str
    artifacts: List[ArtifactRef]
    snippet_refs: List[str]  # snippet_id
```

### Issue Card
```python
class IssueCard(BaseModel):
    issue_id: str
    scope: IssueScope
    title: str
    symptoms: List[str]
    root_cause: Optional[RootCause]
    evidence: List[Evidence]
    fix: List[Fix]
    validation: List[str]
    related_artifacts: List[ArtifactRef]
    snippet_refs: List[str]
```

### Snippet
```python
class Snippet(BaseModel):
    snippet_id: str
    lang: str
    code: str
    source: SnippetSource
    links: SnippetLinks
```

---

## 주요 파일 구조

```
longtext-analysis/
├── backend/
│   ├── api/
│   │   └── routes/
│   │       ├── parse.py
│   │       ├── timeline.py
│   │       ├── issues.py
│   │       ├── snippets.py
│   │       └── export.py
│   ├── parser/
│   │   ├── normalize.py
│   │   ├── meta.py
│   │   ├── turns.py
│   │   ├── snippets.py
│   │   └── artifacts.py
│   ├── builders/
│   │   ├── event_normalizer.py
│   │   ├── timeline_builder.py
│   │   ├── issues_builder.py
│   │   └── snippet_manager.py
│   ├── render/
│   │   └── render_md.py
│   ├── core/
│   │   ├── models.py
│   │   ├── constants.py
│   │   ├── llm_service.py
│   │   └── snippet_storage.py
│   ├── main.py
│   └── pyproject.toml
├── frontend/
│   ├── app/
│   │   └── page.tsx
│   ├── components/
│   │   ├── FileUpload.tsx
│   │   ├── SessionMetaPreview.tsx
│   │   ├── TimelinePreview.tsx
│   │   ├── IssuesPreview.tsx
│   │   └── SnippetsPreview.tsx
│   ├── lib/
│   │   ├── api.ts
│   │   └── constants.ts
│   ├── types/
│   │   └── api.ts
│   └── package.json
├── tests/
│   ├── fixtures/
│   ├── golden/
│   ├── test_parser.py
│   ├── test_event_normalizer.py
│   ├── test_timeline_builder.py
│   ├── test_issues_builder.py
│   ├── test_api.py
│   └── test_integration.py
├── docs/
│   ├── PRD_longtext.md
│   ├── instruction_detail.md
│   └── instruction_moredetail.md
├── .cursor/
│   └── rules/
├── AGENTS.md
├── api-contract-sync.mdc
└── README.md
```

---

## 성공 기준 (Acceptance Criteria)

- [ ] 입력 파일에서 Turn 블록이 안정적으로 파싱됨 (User/Cursor 구분)
- [ ] Timeline과 Issue Cards가 JSON/MD로 생성됨
- [ ] 코드 스니펫이 별도 (`snippets.json` + 파일/zip)로 저장됨
- [ ] UI에서 입력 미리보기 + 출력 일부 미리보기 + 다운로드 가능
- [ ] phase/subphase 누락 시에도 "Unknown + 수동 입력"으로 진행 가능
- [ ] JSON Schema 검증 통과
- [ ] E2E 테스트 통과

---

## 리스크 및 대응

1. **입력 포맷 변형 (Cursor 버전/템플릿 변경)**
   - 대응: 파서 룰 버전 관리 + fallback (LLM 메타 추출)

2. **이슈 카드 과다/과소 탐지**
   - 대응: 민감도 옵션 + 사용자 수동 편집 (차기)

3. **코드 스니펫 과다 포함 (민감정보/토큰 부담)**
   - 대응: 기본은 "분리 저장 + 본문에는 참조만"

4. **LLM API 비용**
   - 대응: 캐싱 필수, 옵션으로 on/off 가능

---

## 차기 기능 (2차)

- [ ] 다중 세션 업로드 + 자동 정렬/병합 (master timeline/issues)
- [ ] 프로젝트별 저장소 (세션 결과 히스토리 관리)
- [ ] Cursor Rule 자동 생성 ("Rule Pack Export")

---

## 진행 상황 추적

**현재 Phase**: Phase 1 (프로젝트 초기 설정 및 환경 구성)

**마지막 업데이트**: 2025-01-XX

**완료된 Phase**:
- 없음

**진행 중인 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성

**다음 단계**:
- Phase 1 완료 후 Phase 2로 진행

