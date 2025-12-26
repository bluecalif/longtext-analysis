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
- [x] Poetry 프로젝트 초기화 (`pyproject.toml`, `poetry.lock`)
- [x] 백엔드 의존성 패키지 설치
  - [x] `fastapi`
  - [x] `uvicorn`
  - [x] `pydantic`
  - [x] `python-dotenv`
  - [x] `openai`
  - [x] `regex`
- [x] 백엔드 디렉토리 구조 생성
  - [x] `backend/parser/` (마크다운 파서 모듈)
  - [x] `backend/builders/` (Timeline/Issue Cards 빌더)
  - [x] `backend/render/` (Markdown 렌더러)
  - [x] `backend/api/routes/` (FastAPI 라우터)
  - [x] `backend/core/` (상수, 유틸리티)
- [x] FastAPI 앱 초기화 (`backend/main.py`)
  - [x] FastAPI 앱 생성
  - [x] CORS 설정
  - [x] 예외 처리 미들웨어
  - [x] Health Check 엔드포인트 (`/health`)
  - [x] OpenAPI/Swagger 문서 자동 생성 확인

### 프론트엔드 설정
- [x] Next.js 프로젝트 초기화 (`frontend/` 디렉토리)
- [x] 프론트엔드 의존성 패키지 설치
  - [x] `next`
  - [x] `react`
  - [x] `typescript`
  - [x] `tailwindcss`
  - [ ] `shadcn/ui` (선택)
- [x] 프론트엔드 디렉토리 구조 생성
  - [x] `frontend/app/` (App Router 페이지)
  - [x] `frontend/components/` (UI 컴포넌트)
  - [x] `frontend/lib/` (유틸리티, API 클라이언트)
  - [x] `frontend/types/` (TypeScript 타입 정의)

### 프로젝트 공통 설정
- [x] `tests/` 디렉토리 생성
  - [x] `tests/fixtures/` (샘플 마크다운 파일)
  - [x] `tests/golden/` (예상 결과)
- [ ] `.env` 파일 템플릿 생성 (OpenAI API 키 등)
- [x] `.env.example` 파일 생성
- [x] `.gitignore` 설정
- [x] `README.md` 최초 작성
  - [x] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [x] 기술 스택 (FastAPI, Next.js)
  - [x] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [x] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [x] 환경 변수 설정 (`.env.example` 참조)
  - [x] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [x] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
- [x] Cursor Rules 초기 설정 (`.cursor/rules/`)
  - [x] `backend-api.mdc` (API 설계 규칙)
  - [x] `parser-rules.mdc` (파서 규칙)
  - [x] `api-contract-sync.mdc` (API 계약 동기화)

**산출물**: 프로젝트 기본 구조, 개발 환경 설정 완료, 기본 README 및 문서

---

## Phase 2: 백엔드 파서 구현 (마크다운 파싱)

**목표**: Cursor export 마크다운 파일을 구조화된 데이터로 파싱

### 텍스트 정규화 (`backend/parser/normalize.py`)
- [x] 줄바꿈 통일 (`\r\n` → `\n`, `\r` → `\n`)
- [x] BOM 제거 (`\ufeff`)
- [x] 공백 정리 (코드블록 제외 옵션)
- [x] 트레일링 공백 제거
- [x] 너무 긴 공백 축소 (3개 이상 → 2개, 코드블록 제외)

### 세션 메타 추출 (`backend/parser/meta.py`)
- [x] Phase 추출 (정규식: `(?i)\bPhase\s+(\d+)\b`)
- [x] Subphase 추출 (정규식: `(?i)\bSub\s*Phase\s+(\d+)\b`)
- [x] Exported at 추출 (정규식: `(?i)Exported\s+(\d{4}-\d{2}-\d{2}[^,\n]*?(?:KST|UTC|GMT|[+\-]\d{2}:\d{2})?)`)
- [x] Cursor version 추출 (정규식: `(?i)\bCursor\s+(\d+\.\d+\.\d+)\b`)
- [x] Session ID 생성 규칙 구현 (`cursor_export_{exported_at_or_fallback}`)
- [x] 상단 2000~4000 chars 범위에서 best-effort 추출

### Turn 블록 파싱 (`backend/parser/turns.py`)
- [x] 구분선(`---`) 기준 분할 (정규식: `^\s*---\s*$`)
- [x] Speaker 추출 (정규식: `^\s*\*\*(User|Cursor)\*\*\s*$`)
- [x] Body 텍스트 추출 (코드블록 제외)
- [x] Fallback 파서 구현 (구분선 없을 때 `**User**`/`**Cursor**` 라벨 기준)
- [x] Parse Health Check (Unknown 비율 높으면 포맷 감지 실패 처리)

### 코드 스니펫 추출 (`backend/parser/snippets.py`)
- [x] 코드펜스 추출 (정규식: ````(\w+)?\n(.*?)```)
- [x] 언어 판별 (lang 누락 시 빈 문자열 처리)
- [x] 스니펫 중복 제거 로직 (Phase 5에서 구현 예정)
- [x] 스니펫 ID 생성 규칙 (Phase 5에서 구현 예정, `turn_index` 포함하여 고유 식별 가능)

### Artifact 추출 (`backend/parser/artifacts.py`)
- [x] 파일/경로 후보 추출 (정규식 기반)
- [x] 파일 타입 분류 (md/mdc/py/ts/tsx/sql 등, 정규식으로 자동 분류)
- [ ] Action 추정 (mention/create/modify/execute) - Phase 3에서 구현 예정

### 테스트
**⚠️ 중요**: AGENTS.md 규칙 준수 - 단위 테스트는 실제 데이터 사용, Mock 사용 절대 금지

- [x] `tests/test_parser.py` 작성
  - [x] `test_normalize()` - 정규화 테스트 (실제 데이터 사용)
  - [x] `test_meta_extraction()` - 메타 추출 테스트 (실제 데이터 사용)
  - [x] `test_turn_parsing()` - Turn 파싱 테스트 (실제 데이터 사용)
  - [x] `test_snippet_extraction()` - 스니펫 추출 테스트 (실제 데이터 사용)
  - [x] `test_artifact_extraction()` - Artifact 추출 테스트 (실제 데이터 사용)
  - [x] `test_parse_markdown_full()` - 전체 파서 파이프라인 테스트
- [x] `tests/fixtures/*.md` 샘플 마크다운 파일 준비
  - [x] `tests/fixtures/cursor_phase_6_3.md` (실제 입력 데이터 복사)
- [ ] `tests/golden/*.json` 예상 결과 (Golden 파일) 준비
  - [ ] Golden 파일 비교 테스트 구현 (회귀 테스트용) - Phase 4에서 구현 예정

### E2E 테스트 (Phase 2 완료 검증)
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

**⚠️ E2E 테스트 필수 사항**:
- Phase 2-5: 모듈 직접 호출 (서버 불필요)
- 로그 파일 저장 필수 (`tests/logs/`, 자동 적용)
- 실행 결과 저장 필수 (`tests/results/`, 상세 파싱/추출 결과)

- [x] `tests/conftest_e2e.py` fixture 작성
  - [x] 자동 로깅 설정 fixture (`setup_test_logging`)
  - [x] Phase 6+용 서버 실행 fixture (`test_server`, `client`)
- [x] `tests/test_parser_e2e.py` 작성
  - [x] **실제 입력 데이터 사용**: `docs/cursor_phase_6_3.md` 파일로 전체 파서 파이프라인 테스트
  - [x] **정합성 검증**: 파싱 결과의 구조적 정확성 확인
    - [x] Session Meta 추출 정확성 (phase, subphase, exported_at, cursor_version)
    - [x] Turn 블록 분할 정확성 (User/Cursor 구분)
    - [x] 코드 스니펫 추출 정확성 (언어 판별, 중복 제거)
    - [x] Artifact 추출 정확성 (파일 경로, 타입 분류)
  - [x] **타당성 검증**: 실제 상황에서의 파싱 품질 확인
    - [x] 파싱 실패율 검증 (Unknown speaker 비율 < 20%)
    - [x] 누락된 정보 처리 확인
    - [x] 예외 케이스 처리 확인
  - [x] **결과 분석 및 자동 보고**: 파싱 결과를 상세히 분석하여 개선점 도출
    - [x] 테스트 실행 후 자동으로 상세 보고 출력 (사용자 질문 없이)
    - [x] 정량적 데이터 제시 (total_turns, user_turns, cursor_turns, unknown_ratio, code_blocks 수 등)
    - [x] 문제 발견 시 원인 분석 포함
    - [x] 리포트 파일 저장 (`tests/reports/parser_e2e_report.json`)
    - [x] 로그 파일 저장 (`tests/logs/`, 자동 적용)
    - [x] 실행 결과 저장 (`tests/results/`, 상세 파싱 결과)

**산출물**: 완전한 파서 모듈, 단위 테스트 및 테스트 데이터, 파싱 결과 데이터 모델 (Pydantic), E2E 테스트 완료 및 검증 리포트

### README 업데이트 (Phase 2 완료 후)
- [x] `README.md` 업데이트
  - [x] 파서 모듈 설명 추가
  - [x] 파싱 예시 추가
  - [x] 프로젝트 구조 업데이트 (실제 디렉토리 구조 반영)

---

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**

프로젝트는 Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행합니다.
하지만 Phase 4나 Phase 5에서 문제가 발견되면 **Phase 3으로 돌아가서 이벤트 정규화 로직을 개선**한 후, 다시 Phase 4, 5로 넘어가는 iterative cycle을 돌고 있습니다.

**개선 사이클 예시**:
1. Phase 3 기본 구현 완료 → Phase 4 진행
2. Phase 4 E2E 테스트에서 Timeline/Issue Cards 품질 문제 발견
3. **Phase 3.4로 돌아가서** 이벤트 정규화 품질 개선 (타입 분류, Summary 품질 등)
4. 개선 완료 후 다시 **Phase 4 E2E 테스트 재실행**하여 품질 확인
5. 품질이 충분히 개선되면 Phase 4 완료 처리, 필요시 Phase 5로 진행

**주의사항**:
- Phase 3, 4, 5의 **기본 순서는 항상 유지**: 3 → 4 → 5
- 개선 작업은 **Phase 3의 서브 Phase (3.1, 3.2, 3.4 등)**로 진행
- Phase 번호는 **절대 섞이지 않음** (3 → 4 → 3.4 → 5 ❌, 3 → 4 → 3.4 → 4 재검증 → 5 ✅)

**상세 개선 계획**: [docs/phase3_improvement_plan.md](docs/phase3_improvement_plan.md) 참조

### Phase 3.0: 기본 구현 (완료)

#### 데이터 모델 정의 (`backend/core/models.py`)
- [x] `SessionMeta` 모델 정의 (Phase 2에서 완료)
  - [x] `session_id: str`
  - [x] `exported_at: Optional[str]`
  - [x] `cursor_version: Optional[str]`
  - [x] `phase: Optional[int]`
  - [x] `subphase: Optional[int]`
  - [x] `source_doc: str`
- [x] `Turn` 모델 정의 (Phase 2에서 완료)
  - [x] `speaker: str` (User/Cursor/Unknown)
  - [x] `body: str`
  - [x] `code_blocks: List[CodeBlock]`
  - [x] `path_candidates: List[str]`
- [x] `EventType` Enum 정의 (status_review, plan, artifact, debug, completion, next_step, turn)
- [x] `Event` 기본 모델 정의
  - [x] `type: EventType`
  - [x] `turn_ref: int` (원본 Turn 인덱스)
  - [x] `summary: str` (요약)
  - [x] `artifacts: List[dict]` (연결된 Artifact)
  - [x] `snippet_refs: List[str]` (연결된 스니펫 ID)
- [x] `MessageEvent` 모델 정의 (사용자 요청/응답 이벤트) - Event 기본 모델로 대체 완료
- [x] `ArtifactEvent` 모델 정의 (파일 생성/수정 이벤트) - Event 기본 모델로 대체 완료
- [x] `DebugEvent` 모델 정의 (디버깅 이벤트) - Event 기본 모델로 대체 완료

#### 상수 정의 (`backend/core/constants.py`)
- [x] `EventType` Enum 값 정의 (status_review, plan, artifact, debug, completion, next_step, turn)
- [x] Debug 트리거 패턴 정의
  - [x] `error` 패턴 (정규식)
  - [x] `root_cause` 패턴 (정규식)
  - [x] `fix` 패턴 (정규식)
  - [x] `validation` 패턴 (정규식)
- [x] Issue 상태 Enum 정의 (`confirmed`, `hypothesis`)

#### 이벤트 정규화 기본 구현 (`backend/builders/event_normalizer.py`)
- [x] `normalize_turns_to_events()` 함수 구현 (기본 버전)
  - [x] Turn → Event 변환 로직
  - [x] Event 타입 분류 로직 (규칙 기반, 기본 패턴)
  - [x] Artifact 연결 로직
  - [x] Snippet 참조 연결 로직
- [x] `is_debug_turn()` 함수 구현 (디버그 Turn 판별)
- [x] `create_debug_event()` 함수 구현
- [x] `create_artifact_event()` 함수 구현
- [x] `create_message_event()` 함수 구현

#### 테스트 (기본 구현 검증)
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지 (LLM은 캐싱으로 처리)

- [x] `tests/test_event_normalizer.py` 작성
  - [x] `test_turn_to_event_conversion()` - Turn → Event 변환 테스트 (실제 데이터 사용)
  - [x] `test_event_type_classification()` - 이벤트 타입 분류 테스트 (실제 데이터 사용)
  - [x] `test_artifact_linking()` - Artifact 연결 테스트 (실제 데이터 사용)
  - [x] `test_snippet_linking()` - Snippet 참조 연결 테스트 (실제 데이터 사용)
  - [x] `test_debug_turn_detection()` - 디버그 Turn 탐지 테스트
  - [x] `test_event_creation_functions()` - 이벤트 생성 함수 테스트

#### E2E 테스트 (기본 구현 검증)
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

**⚠️ E2E 테스트 필수 사항**:
- Phase 2-5: 모듈 직접 호출 (서버 불필요)
- 로그 파일 저장 필수 (`tests/logs/`, 자동 적용)
- 실행 결과 저장 필수 (`tests/results/`, 상세 이벤트 정규화 결과)

- [x] `tests/test_event_normalizer_e2e.py` 작성
  - [x] **실제 입력 데이터 사용**: Phase 2에서 파싱한 `docs/cursor_phase_6_3.md` 결과를 입력으로 사용
  - [x] **정합성 검증**: 이벤트 정규화 결과의 구조적 정확성 확인
    - [x] Turn → Event 변환 정확성
    - [x] Event 타입 분류 정확성 (status_review/plan/artifact/debug/completion/next_step/turn)
    - [x] Phase/Subphase 연결 정확성 (기본 구조 확인)
    - [x] Artifact 연결 정확성
    - [x] Snippet 참조 연결 정확성
  - [x] **타당성 검증**: 실제 상황에서의 이벤트 정규화 품질 확인
    - [x] 이벤트 타입 분류의 적절성
    - [x] 연결 관계의 정확성
  - [x] **결과 분석 및 자동 보고**: 이벤트 정규화 결과를 상세히 분석하여 개선점 도출
    - [x] 테스트 실행 후 자동으로 상세 보고 출력 (사용자 질문 없이)
    - [x] 정량적 데이터 제시 (total_events, event_type_distribution, artifact_linking_rate 등)
    - [x] 문제 발견 시 원인 분석 포함
    - [x] 리포트 파일 저장 (`tests/reports/event_normalizer_e2e_report.json`)
    - [x] 로그 파일 저장 (`tests/logs/`, 자동 적용)
    - [x] 실행 결과 저장 (`tests/results/`, 상세 이벤트 정규화 결과)

**발견된 문제점** (E2E 테스트 결과 분석):
- 이벤트 중복 생성: 67개 Turn → 117개 Event (1.75배)
- Summary 품질: 200자 단순 자르기, 줄바꿈 미처리
- 타입 분류 정확도: 약 60-70% (정규식 기반, 개선 필요)

---

### Phase 3.1: 즉시 개선 (정규식 기반)

**목표**: 발견된 문제점을 정규식 기반으로 즉시 개선

- [ ] 이벤트 중복 생성 방지 (`backend/builders/event_normalizer.py`)
  - [ ] 우선순위 기반 단일 이벤트 생성 로직 구현
  - [ ] `create_single_event_with_priority()` 함수 구현
- [ ] Summary 품질 개선 (`backend/builders/event_normalizer.py`)
  - [ ] 줄바꿈 정리 로직 추가
  - [ ] 의미 있는 위치에서 자르기 로직 구현 (문장/문단/단어 단위)
- [ ] 타입 분류 엄격화 (`backend/builders/event_normalizer.py`)
  - [ ] `classify_event_type_strict()` 함수 구현 (구체적인 패턴 사용)
  - [ ] 일반 단어 매칭 방지 로직 추가
- [ ] 단위 테스트 업데이트 (`tests/test_event_normalizer.py`)
  - [ ] 우선순위 기반 이벤트 생성 테스트 추가
  - [ ] Summary 품질 개선 테스트 추가
  - [ ] 엄격한 타입 분류 테스트 추가
- [ ] E2E 테스트 업데이트 및 실행 (`tests/test_event_normalizer_e2e.py`)
  - [ ] 개선된 로직 반영
  - [ ] 결과 분석 및 검증

---

### Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료 (2025-12-20)

**목표**: LLM을 사용하여 타입 분류 및 Summary 품질 향상

**⚠️ 중요**: 모델명은 반드시 `"gpt-4.1-mini"` 사용 (사용자 지시)

- [x] Event 모델 확장 (`backend/core/models.py`)
  - [x] `processing_method: str` 필드 추가 ("regex" 또는 "llm")
- [x] LLM 서비스 구현 (`backend/core/llm_service.py`)
  - [x] gpt-4.1-mini API 클라이언트 구현
  - [x] `classify_and_summarize_with_llm()` 함수 구현
    - [x] 타입 분류 및 요약 생성 통합 함수
    - [x] 응답 파싱 로직 (TYPE, SUMMARY)
  - [x] 파일 기반 캐싱 로직 구현
    - [x] 캐시 키 생성 규칙 (텍스트 해시)
    - [x] 캐시 저장/로드 함수
  - [x] `.env` 파일 자동 로드 설정 (`load_dotenv()`)
- [x] 이벤트 정규화 모듈에 LLM 옵션 추가 (`backend/builders/event_normalizer.py`)
  - [x] `normalize_turns_to_events()` 함수에 `use_llm` 파라미터 추가
  - [x] `create_event_with_llm()` 함수 구현
  - [x] LLM/정규식 선택 로직 구현
- [x] LLM 서비스 테스트 작성 (`tests/test_llm_service.py`)
  - [x] LLM 호출 결과 캐싱 확인 (파일 기반 캐시)
  - [x] 동일 입력 재사용 확인
  - [x] 타입 분류 정확도 테스트
  - [x] Summary 품질 테스트
- [x] E2E 테스트에 LLM 옵션 추가 (`tests/test_event_normalizer_e2e.py`)
  - [x] `use_llm=True` 옵션 테스트 추가
  - [x] `processing_method` 필드 검증
  - [x] LLM/정규식 결과 비교 분석
  - [x] `.env` 파일 자동 로드 설정 (`load_dotenv()`)
  - [x] E2E 테스트 실행 및 결과 분석 완료
    - [x] 리포트 생성: `tests/reports/event_normalizer_e2e_llm_report.json`
    - [x] 결과 저장: `tests/results/event_normalizer_e2e_llm_20251220_160031.json`
    - [x] 분석 문서: `docs/phase3_2_e2e_analysis.md`

**E2E 테스트 결과 요약**:
- 총 Turn: 67개, 총 Event: 67개 (1:1 매핑 달성 ✅)
- 이벤트 타입 분포: status_review 25개, plan 21개, next_step 4개, completion 5개, debug 7개, turn 5개
- LLM이 정규식 대비 더 세밀한 타입 분류 제공 (status_review, plan 등)
- Summary 품질 개선 (간결하고 의미 있는 요약)
- **남은 이슈**: LLM 기반에서 `artifact` 타입 이벤트가 0개로 분류됨 (하지만 `artifacts` 배열에는 파일 경로 포함됨)
  - 원인: LLM이 파일 경로를 인식하지만, 이벤트 타입은 텍스트의 주요 목적을 우선시하여 분류
  - 영향: Artifact 연결은 정상 작동하지만, 타입 통계에서만 `artifact` 타입이 0%로 표시
  - 개선 방안: Phase 3.3 평가 후 LLM 프롬프트 개선 또는 하이브리드 접근 검토

#### Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선 (완료)

**목표**: LLM 처리 시간 단축을 위해 순차 처리에서 병렬 처리로 리팩토링 및 캐시 시스템 개선

**⚠️ 중요**: max_workers=5 사용

- [x] 병렬 처리 로직 구현 (`backend/builders/event_normalizer.py`)
  - [x] `_normalize_turns_to_events_parallel()` 함수 구현
    - [x] `ThreadPoolExecutor` 사용 (max_workers=5)
    - [x] Turn 리스트를 병렬로 처리
    - [x] turn_index 기준으로 순서 유지
    - [x] 에러 처리 및 fallback 로직 구현
  - [x] `normalize_turns_to_events()` 함수 수정
    - [x] `use_llm=True`일 때 병렬 처리 로직 호출
- [x] E2E 테스트 실행 및 검증 (`tests/test_event_normalizer_e2e.py`)
  - [x] 병렬 처리 후 결과 일치 확인 (이벤트 순서, 내용 검증)
  - [x] 성능 측정 및 비교 (병렬 처리 전후 실행 시간 기록)
    - [x] 성능 향상 확인: 224초 → 44.99초 (약 5배 향상)
  - [x] 로그 파일 생성 문제 해결 (fixture 개선 완료, 실제 생성 확인 완료)
  - [ ] 에러 케이스 테스트 (네트워크 오류 등) - 선택적
- [x] 캐시 시스템 개선 (`backend/core/cache.py`, `backend/core/llm_service.py`)
  - [x] 결정적 해시 함수 구현 (SHA-256, `hash()` 사용 금지)
  - [x] 원자적 파일 저장 구현 (임시 파일 + 원자적 이동, Race Condition 방지)
  - [x] 텍스트 해시 검증 구현 (캐시 키 충돌 감지)
  - [x] Fallback 캐시 저장 구현 (재시도 실패 시에도 결과 저장)
  - [x] 캐시 메타데이터 추가 (검증 및 디버깅용)
  - [x] 캐시 통계 개선 (히트율, 디렉토리 통계 포함)
- [x] 커서룰 업데이트 (`.cursor/rules/llm-service.mdc`)
  - [x] 캐싱 규칙 섹션 개선 (SHA-256, 원자적 저장, 텍스트 해시 검증)
  - [x] Pattern 1 업데이트 (개선된 LLM 호출 함수 예시)
  - [x] Common Pitfalls 섹션 확장 (비결정적 해시, Race Condition, Fallback 캐시)
  - [x] 캐시 시스템 개선 사항 섹션 추가 (성능 개선 결과 포함)

**실제 효과**:
- 병렬 처리: 224초 → 44.99초 (약 5배 향상) ✅
- 캐시 시스템 개선: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상) ✅
- 캐시 히트율: 0% → 100% (두 번째 실행 기준) ✅
- 비용 절감: LLM 호출 100% 감소 (두 번째 실행 기준) ✅

**검증 완료**:
- 로그 파일 생성 정상 작동 (fixture 개선 완료, 테스트로 검증)
- 캐시 시스템 정상 작동 (SHA-256 해시, 원자적 저장, 텍스트 해시 검증)
- 성능 개선 검증 완료 (캐시 히트율 100%, 실행 시간 215배 향상)

---

### Phase 3.3: 결과 평가 방법 구축

**목표**: 품질 개선 효과를 평가할 수 있는 도구 구축

- [x] 정성적 평가 도구 구현 (`backend/builders/evaluation.py`)
  - [x] `create_manual_review_dataset()` 함수 구현
    - [x] 다양한 타입 균등 샘플링 로직
    - [x] 수동 검증용 JSON 파일 생성
    - [x] 검증 가이드라인 포함
  - [x] `evaluate_manual_review()` 함수 구현
    - [x] 수동 검증 결과 로드 및 분석
    - [x] 타입 분류 정확도 계산
    - [x] Summary 정확도 계산
    - [x] 혼동 행렬 생성
    - [x] 처리 방법별 정확도 비교 (regex vs llm)
- [x] Golden 파일 관리 도구 구현 (`backend/builders/evaluation.py`)
  - [x] `create_golden_file()` 함수 구현
    - [x] 개선 사이클 완료 후 Golden 파일 생성
    - [x] 회귀 테스트용 데이터 저장
  - [x] `compare_with_golden()` 함수 구현
    - [x] Golden 파일과 현재 결과 비교
    - [x] 회귀 감지 로직 (95% 미만 시 회귀)
- [x] E2E 테스트에 평가 도구 통합 (`tests/test_event_normalizer_e2e.py`)
  - [x] 정성적 평가 데이터셋 생성 옵션 추가
  - [x] Golden 파일 비교 옵션 추가
- [x] 수동 검증 프로세스 실행
  - [x] 수동 검증용 데이터셋 생성 및 제공
  - [x] 사용자 라벨링 완료 후 정확도 계산
- [ ] Golden 파일 생성: **보류** (Phase 4 완료 후 Timeline/Issue Cards 생성 결과를 반영하여 이벤트 정규화 품질 재평가 후 작성 예정)

**⚠️ 중요: 이벤트 정규화 품질 재평가 계획**
- Phase 3에서 수동 검증을 통해 이벤트 정규화 품질을 평가했으나, 최종 품질 평가는 Phase 4 완료 후 진행 예정
- Phase 4에서 Timeline 및 Issue Cards 생성 결과를 분석하여 이벤트 정규화 품질의 실제 효과를 검증
- Timeline/Issue Cards 품질이 낮다면 이벤트 정규화 로직 개선 필요
- Phase 4 완료 후 재평가 결과를 바탕으로 Golden 파일 생성 및 최종 품질 확정

---

### Phase 3.4: 이벤트 정규화 품질 개선 (Iterative Improvement Cycle)

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

**⚠️ 컨텍스트**: 
이 섹션은 **Phase 4 완료 후 문제가 발견되어 Phase 3으로 돌아온 개선 작업**입니다.
Phase 4의 Timeline/Issue Cards 생성 결과를 분석하여 이벤트 정규화 품질의 실제 효과를 검증하고, 필요 시 개선 작업을 수행합니다.

**발견된 문제점**:
- Timeline: 이벤트 타입 분류가 부정확 (예: 메타데이터가 "turn" 타입으로 분류됨)
- Timeline: Summary가 단순 텍스트 자르기만 수행하여 의미 있는 요약이 아님
- Issue Cards: 이벤트 Summary 품질 문제로 인해 핵심 내용 추출 실패
- Issue Cards: Root cause, Fix, Validation 추출이 중간 과정 텍스트를 그대로 포함

- [x] 수동 검증 파일 재작성 (2025-12-23 완료)
  - [x] Phase 4 E2E 테스트 결과를 반영한 새로운 수동 검증 데이터셋 생성
    - [x] HTML 형식으로 모든 이벤트 추출 (67개 이벤트 전체 포함)
    - [x] `create_all_events_html_review_dataset()` 함수 구현 및 실행
    - [x] 파일 위치: `tests/manual_review/all_events_html_review_20251223_212658/manual_review.html`
  - [x] 사용자 수동 검증 완료
    - [x] HTML 파일에서 각 이벤트의 correct_type, type_accuracy, summary_quality, summary_completeness, notes 입력
    - [x] 검증 결과 텍스트 파일로 기록: `docs/수동검증_html에 기록.txt`
  - [x] 텍스트 파일 파싱 스크립트 작성 및 실행
    - [x] `scripts/parse_text_review_to_json.py` 스크립트 작성
    - [x] 텍스트 파일에서 수동 검증 데이터 추출 및 JSON 변환
    - [x] 결과 파일 생성: `tests/manual_review/all_events_html_review_20251223_212658/manual_review_updated.json`
    - [x] 67개 이벤트의 검증 데이터 추출 완료 (100% 검증 완료)
    - [x] 타입별 검증 완료 수: debug 23개, plan 17개, status_review 12개, artifact 4개, completion 4개, next_step 4개, turn 3개

- [x] HTML 수동 검증 스크립트 개선 (2025-12-25 완료)
  - [x] 스크립트 분리 완료 (비용 절감)
    - [x] `scripts/create_html_review.py` 생성 (HTML만 생성, 비용 없음, 반복 실행 가능)
    - [x] `scripts/create_events_for_review.py` 생성 (이벤트 정규화만, LLM 사용, 선택적)
    - [x] `scripts/create_all_events_html_review.py` 삭제 (deprecated, 혼선 방지)
  - [x] 워크플로우 명확화
    - [x] 일반적인 경우: E2E 테스트 실행 → `create_html_review.py` 실행 (비용 없음)
    - [x] 특수한 경우: `create_events_for_review.py` 실행 (LLM 사용, 비용 발생)
  - [x] 스크립트 설명 업데이트 (사용 시나리오 명확화)

- [x] 1단계: 정량적 평가 실행 (2025-12-24 완료)
  - [x] `evaluate_manual_review()` 함수 실행
  - [x] 타입 분류 정확도 계산 (62.69%)
  - [x] 혼동 행렬 생성 및 분석
  - [x] 처리 방법별 정확도 비교 (LLM vs Regex)
  - [x] Summary 품질 점수 통계 분석 (평균 3.95점)
  - [x] 평가 결과 리포트 생성 및 저장 (`tests/reports/manual_review_evaluation_20251224_182554.json`)

- [x] 2단계: 정성적 분석 - Notes 내용 확인 (2025-12-24 완료)
  - [x] **⚠️ 중요**: 휴리스틱 기반 평가의 한계를 보완하기 위해 notes 내용을 하나씩 확인
  - [x] `manual_review_updated.json`의 모든 샘플(67개) 순회
  - [x] 각 샘플의 `notes` 필드 내용 확인
  - [x] `correct_type`과 `current_event.type`이 다른 경우 notes 확인
  - [x] `summary_quality` 또는 `summary_completeness`가 3점 이하인 경우 notes 확인
  - [x] `type_accuracy`가 3점 이하인 경우 notes 확인
  - [x] notes 내용을 바탕으로 문제 패턴 분류:
    - [x] 타입 분류 오류 패턴 (예: "status_review로 분류되었지만 실제로는 plan")
    - [x] Summary 품질 문제 패턴 (예: "요약이 너무 길다", "핵심 내용 누락")
    - [x] LLM 프롬프트 문제 (예: "LLM이 잘못 이해함")
    - [x] 정규식 패턴 문제 (예: "패턴이 너무 엄격함")
    - [x] 맥락 부족 문제 (예: "이전 Turn의 맥락이 없어서 어려움")
    - [x] 타입 정의 부족 문제 (예: "새로운 type 정의 필요")
  - [x] Notes 분석 결과 리포트 생성 및 저장 (`tests/reports/manual_review_notes_analysis_20251224_182712.json`, `tests/reports/manual_review_direct_analysis.md`)

- [x] 3단계: 문제 원인 분석 및 개선 방안 도출 (2025-12-24 완료)
  - [x] Notes 분석 결과를 바탕으로 문제 원인 도출:
    - [x] 타입 분류 오류 원인 (LLM 프롬프트, 정규식 패턴, 우선순위 로직, 맥락 부족 등)
    - [x] Summary 품질 문제 원인 (요약 길이, 핵심 내용 추출 실패, 중간 과정 텍스트 포함 등)
  - [x] 개선 방안 도출:
    - [x] Type 추출 로직 개선 방안 (맥락 기반 타입 분류, Artifact 정보 포함)
    - [x] Summary 로직 개선 방안 (LLM 프롬프트 개선, max_tokens 증가)
    - [x] LLM 프롬프트 개선 방안 (요약 규칙, 특수 기호 의미 명시)
    - [x] 맥락 처리 개선 방안 (이전 Turn 정보 활용)
  - [x] 개선 방안 우선순위화
  - [x] 개선 계획 문서 생성 (`tests/reports/phase_3_4_comprehensive_analysis.md`, `tests/reports/root_cause_analysis_20251224_183215.json`)

- [x] 4단계: 개선 방안 검토 및 승인 (2025-12-25 완료)
  - [x] 사용자와 개선 방안 검토
  - [x] 우선순위 조정 (HIGH: 맥락 기반 타입 분류, Summary 품질 개선)
  - [x] 개선 작업 범위 결정 (Artifact 정보 포함, 맥락 정보 활용, 프롬프트 개선)

- [x] 5단계: 개선 작업 실행 (2025-12-25 완료)
  - [x] Type 추출 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [x] LLM 서비스에 Artifact 정보 포함 (code_blocks, path_candidates)
    - [x] 캐시 키 생성 시 Artifact 정보 포함
    - [x] 맥락 정보 수집 함수 구현 (_collect_context_info, _collect_context_info_with_events)
    - [x] 이벤트 정규화 함수에 맥락 정보 전달
    - [x] Artifact 타입 분류 강화 (path_candidates 우선 고려)
  - [x] Summary 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [x] LLM Summary 생성 프롬프트 개선 (요약 규칙, 특수 기호 의미 명시)
    - [x] max_tokens 증가 (150 → 200)
    - [x] 맥락 기반 Summary 생성 로직 개선 (이전 Turn 정보 활용)

- [x] 6단계: E2E 재평가 (2025-12-25 완료)
  - [x] 개선된 이벤트 정규화 로직으로 E2E 테스트 재실행 완료
  - [x] 결과 파일 생성: `tests/results/event_normalizer_e2e_llm_20251225_183334.json`
  - [x] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (2025-12-25 생성 완료)
    - [x] HTML 수동 검증 데이터셋 생성 완료: `tests\manual_review\all_events_html_review_20251225_211525\manual_review.html`
    - [x] 사용자 수동 검증 완료 (2025-12-25)
    - [x] 타입 체계 개선 계획 수립 완료 (2025-12-25)
      - [x] **⚠️ 중요**: `artifact` 타입의 근본적 문제 발견 및 개선 방안 도출
      - [x] 새로운 타입 체계 설계 완료 (`code_generation` 추가, `artifact` 제거)
      - [x] 상세 개선 계획 문서 작성: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md)
      - [x] **다음 세션 시작 가이드**: 위 문서 참조
    - [ ] ⚠️ **중요**: 결과 확인 시 문제가 발견되면 **3단계(문제 원인 분석 및 개선 방안 도출)**로 돌아가서 재분석 및 개선 작업 진행
  - [ ] 개선 전후 비교 분석 (타입 체계 개선 구현 후 진행)
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [x] 7단계: 타입 체계 개선 구현 (2025-12-26 완료)
  - [x] **⚠️ 시작 전 필수**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 문서 읽기
  - [x] Step 1: EventType Enum 수정 (`backend/core/models.py`)
    - [x] `EventType.ARTIFACT` 제거
    - [x] `EventType.CODE_GENERATION = "code_generation"` 추가
    - [x] 관련 주석 업데이트
  - [x] Step 2: Artifact Action 타입 추가 (선택적) (`backend/core/models.py`)
    - [x] `ArtifactAction` Enum 추가 (read, create, modify, execute, mention)
    - [x] 기존 `"mention"` 기본값 유지 (하위 호환성)
  - [x] Step 3: 분류 로직 개선 (`backend/builders/event_normalizer.py`)
    - [x] `is_artifact_turn()` 함수 제거 및 `is_code_generation_turn()`으로 변경
    - [x] `create_artifact_event()` 함수 제거 및 `create_code_generation_event()`로 변경
    - [x] `create_single_event_with_priority()` 함수 수정 (우선순위에서 ARTIFACT 제거, CODE_GENERATION 추가)
    - [x] `create_event_with_llm()` 함수 수정 (EventType.ARTIFACT 참조 제거, CODE_GENERATION 추가)
    - [x] 맥락 기반 분류 로직 추가
  - [x] Step 4: LLM 프롬프트 수정 (`backend/core/llm_service.py`)
    - [x] 프롬프트에서 `artifact` 타입 설명 제거
    - [x] `code_generation` 타입 설명 추가 (정의, 예시, 구분)
    - [x] 타입 분류 우선순위 업데이트 (Artifact 우선 → Code Generation 우선)
  - [x] Step 5: 평가 도구 업데이트 (`backend/builders/evaluation.py`)
    - [x] `artifact` 타입 참조 제거
    - [x] `code_generation` 타입 추가
    - [x] HTML 생성 시 타입 스타일 업데이트
    - [x] 혼동 행렬 생성 시 타입 목록 업데이트
  - [x] Step 6: E2E 테스트 재실행 및 검증 (`tests/test_event_normalizer_e2e.py`)
    - [x] 새로운 타입 체계로 E2E 테스트 실행
    - [x] 결과 분석 및 검증 (code_generation 타입 이벤트 생성 확인, artifact 타입 이벤트 제거 확인)
    - [x] 결과 파일 저장 및 리포트 생성
    - [x] HTML 수동 검증 데이터셋 생성 완료 (2025-12-26)
    - [x] 수동 검증 결과 확인 (전체적으로 나쁘지 않음, 다음 단계 진행 OK)
  - [x] Step 7: 수동 검증 결과 확인 (선택적)
    - [x] HTML 수동 검증 데이터셋 생성 완료 (`scripts/create_html_review.py` 사용)
    - [x] 사용자 수동 검증 완료 (2025-12-26)
    - [x] 결과 확인: 전체적으로 나쁘지 않음, 다음 단계 진행 OK

- [ ] 8단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선 및 타입 체계 개선`)
  - [ ] 사용자 피드백 요청

- [ ] 결과 피드백 (선택적)
  - [ ] 개선 결과 사용자에게 보고
  - [ ] 추가 개선 필요 여부 판단
  - [ ] Golden 파일 생성 (품질이 충분히 개선된 경우)

**산출물**: 개선된 이벤트 정규화 모듈, E2E 테스트 재평가 리포트, Golden 파일 (품질 개선 완료 시)

---

### README 업데이트 (Phase 3 완료 후)
- [x] `README.md` 업데이트
  - [x] 이벤트 정규화 설명 추가
  - [x] 이벤트 타입 설명 추가

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**⚠️ 참고**: 
- Phase 3 완료 후 진행합니다
- E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)**로 돌아가서 개선 작업을 수행한 후 다시 Phase 4 E2E 테스트를 재실행합니다

### 상수 정의 (`backend/core/constants.py`)
- [x] Event 타입 Enum 정의 (이미 `backend/core/models.py`에 정의됨)
- [x] Issue 상태 Enum 정의 (`confirmed`, `hypothesis`) (이미 정의됨)
- [x] 파일 타입 목록 정의 (`md`, `mdc`, `py`, `ts`, `tsx`, `sql`, `json`)

### Timeline 생성 (`backend/builders/timeline_builder.py`)
- [x] TimelineEvent 모델 정의 (`backend/core/models.py`)
- [x] 기본 Timeline 빌더 구현 (`build_timeline()` 함수)
  - [x] 이벤트 시퀀스 번호 부여 로직 (Event.seq 사용)
  - [x] Phase/Subphase 연결 로직 (Event 또는 SessionMeta에서 가져옴)
  - [x] Artifact 연결 로직 (Event.artifacts 사용)
  - [x] Snippet 참조 연결 로직 (Event.snippet_refs 사용)
  - [x] Timeline JSON 구조 생성 (TimelineEvent 리스트)
- [ ] 요약 생성 (LLM 옵션) - 선택적 개선 사항 (현재는 Event.summary 사용)
- [ ] Phase/Subphase별 그룹화 로직 - 선택적 개선 사항 (현재는 순차 리스트)

### Issue Cards 생성 (`backend/builders/issues_builder.py`)
- [x] IssueCard 모델 정의 (`backend/core/models.py`)
- [x] 기본 Issue Cards 빌더 구현 (`build_issue_cards()` 함수)
  - [x] DebugEvent 기반 이슈 탐지 로직 (symptom seed 탐지)
  - [x] 이슈 그룹화 로직 (슬라이딩 윈도우, 최근 10개 Turn)
  - [x] Symptom 추출 (주로 User 발화, 패턴 기반)
  - [x] Root cause 추출 (주로 Cursor 발화, 패턴 기반, confirmed/hypothesis 구분)
  - [x] Fix 추출 (DebugEvent에서 snippet_refs 또는 fix 트리거)
  - [x] Validation 추출 (validation 트리거 패턴)
  - [x] 관련 Artifact 연결 로직 (윈도우 내 Event.artifacts 수집)
  - [x] Snippet 참조 연결 로직 (윈도우 내 Event.snippet_refs 수집)
  - [x] Issue Cards JSON 구조 생성 (IssueCard 리스트)
- [ ] Root cause 추출 (LLM 옵션) - 선택적 개선 사항 (현재는 패턴 기반)

### 테스트
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

- [x] `tests/test_timeline_builder.py` 작성
  - [x] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트 (실제 데이터 사용)
  - [x] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트 (실제 데이터 사용)
  - [x] `test_timeline_artifact_linking()` - Artifact 연결 테스트 (실제 데이터 사용)
  - [x] `test_timeline_snippet_linking()` - Snippet 참조 연결 테스트 (실제 데이터 사용)
  - [x] `test_timeline_event_type_preservation()` - 이벤트 타입 보존 테스트 (실제 데이터 사용)
- [x] `tests/test_issues_builder.py` 작성
  - [x] `test_issue_detection()` - 이슈 탐지 테스트 (실제 데이터 사용)
  - [x] `test_issue_grouping()` - 이슈 그룹화 테스트 (실제 데이터 사용)
  - [x] `test_symptom_extraction()` - Symptom 추출 테스트 (실제 데이터 사용)
  - [x] `test_root_cause_extraction()` - Root cause 추출 테스트 (실제 데이터 사용)
  - [x] `test_fix_extraction()` - Fix 추출 테스트 (실제 데이터 사용)
  - [x] `test_validation_extraction()` - Validation 추출 테스트 (실제 데이터 사용)
  - [x] `test_issue_card_completeness()` - Issue Card 완전성 테스트 (실제 데이터 사용)
- [ ] Golden 파일 비교 테스트 작성
  - [ ] Timeline Golden 파일 비교
  - [ ] Issues Golden 파일 비교

### E2E 테스트 (Phase 4 완료 검증)
**⚠️ 중요**: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지

**⚠️ E2E 테스트 필수 사항**:
- Phase 2-5: 모듈 직접 호출 (서버 불필요)
- 로그 파일 저장 필수 (`tests/logs/`, 자동 적용)
- 실행 결과 저장 필수 (`tests/results/`, 상세 Timeline/Issues 생성 결과)

**⚠️ 중요: E2E 테스트 상태**
- 현재 E2E 테스트는 **구조적 정합성 검증만 완료** (테스트 통과)
- **실제 내용 품질 검증은 미완료** (Timeline 요약, Issue Cards 내용의 실제 적절성 등)
- 결과 파일 위치: `tests/results/timeline_issues_e2e_YYYYMMDD_HHMMSS.json`
- 리포트 파일 위치: `tests/reports/timeline_issues_e2e_report.json`
- **다음 단계**: Phase 4 완료 후 Phase 3 이벤트 정규화 품질 재평가 시 실제 내용 품질 검증 예정

- [x] `tests/test_timeline_issues_e2e.py` 작성
  - [x] **실제 입력 데이터 사용**: Phase 3에서 정규화한 이벤트를 입력으로 사용
  - [x] **정합성 검증 (구조적)**: Timeline 및 Issue Cards 생성 결과의 구조적 정확성 확인
    - [x] Timeline 시퀀스 번호 부여 정확성
    - [x] Timeline Phase/Subphase 그룹화 정확성
    - [x] Timeline Artifact/Snippet 연결 정확성
    - [x] Issue Cards 탐지 정확성 (DebugEvent 기반)
    - [x] Issue Cards 그룹화 정확성
    - [x] Issue Cards symptom/root_cause/fix/validation 추출 정확성
    - [x] Issue Cards Artifact/Snippet 연결 정확성
  - [ ] **타당성 검증 (내용 품질)**: 실제 상황에서의 Timeline/Issue Cards 품질 확인
    - [ ] Timeline 요약의 실제 적절성 검증 (요약이 Turn 내용을 잘 반영하는지)
    - [ ] Issue Cards 탐지의 실제 적절성 검증 (과다/과소 탐지, 실제 symptom/root_cause/fix 연결의 정확성)
    - [ ] Issue Cards 내용의 실제 완전성 검증 (symptom/root_cause/fix/validation이 실제로 의미 있는지)
    - **참고**: 이 검증은 Phase 4 완료 후 Phase 3 이벤트 정규화 품질 재평가 시 함께 진행 예정
  - [ ] **JSON Schema 검증**: 생성된 Timeline/Issue Cards JSON이 스키마를 준수하는지 확인 (선택적)
  - [x] **결과 분석 및 자동 보고**: Timeline/Issue Cards 생성 결과를 상세히 분석하여 개선점 도출
    - [x] 테스트 실행 후 자동으로 상세 보고 출력 (사용자 질문 없이)
    - [x] 정량적 데이터 제시 (timeline_events_count, issues_count, linking_completeness 등)
    - [x] 문제 발견 시 원인 분석 포함
    - [x] 리포트 파일 저장 (`tests/reports/timeline_issues_e2e_report.json`)
    - [x] 로그 파일 저장 (`tests/logs/`, 자동 적용)
    - [x] 실행 결과 저장 (`tests/results/timeline_issues_e2e_YYYYMMDD_HHMMSS.json`, 상세 Timeline/Issues 생성 결과)

**산출물**: Timeline 빌더 모듈, Issue Cards 빌더 모듈, Timeline/Issue Cards 데이터 모델, E2E 테스트 완료 및 검증 리포트

**⚠️ 참고: Phase 3.4와의 관계**
- Phase 4 E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)** 섹션으로 돌아가서 개선 작업을 수행합니다
- 개선 완료 후 다시 Phase 4 E2E 테스트를 재실행하여 품질을 확인합니다

### README 업데이트 (Phase 4 완료 후)
- [ ] `README.md` 업데이트
  - [ ] Timeline/Issue Cards 생성 설명 추가
  - [ ] 출력 예시 추가 (JSON 구조 예시)
  - [ ] 프로젝트 구조 업데이트

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
    - [ ] 로그 파일 저장 (`tests/logs/`, 자동 적용)
    - [ ] 실행 결과 저장 (`tests/results/`, 상세 스니펫 분리/저장 결과)

**산출물**: 스니펫 관리 모듈, 스니펫 저장소 모듈, E2E 테스트 완료 및 검증 리포트

### README 업데이트 (Phase 5 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 스니펫 관리 설명 추가
  - [ ] 스니펫 저장 구조 설명 추가

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

**⚠️ E2E 테스트 필수 사항**:
- Phase 6+: 실제 서버 실행 필수 (API 테스트)
- 로그 파일 저장 필수 (`tests/logs/`, 자동 적용)
- 실행 결과 저장 필수 (`tests/results/`, 상세 API 응답 결과)

- [x] `tests/conftest_e2e.py` fixture 작성
  - [x] `test_server` fixture: 실제 uvicorn 서버 실행 (Phase 6+ 전용)
    - [x] 서버 시작 대기 로직 (최대 30회 재시도)
    - [x] 서버 종료 자동화
  - [x] `httpx.Client` fixture: 실제 HTTP 요청 클라이언트 (Phase 6+ 전용)
    - [x] `TestClient` 사용 금지 (백그라운드 작업이 제대로 실행되지 않음)
    - [x] 타임아웃 설정 (30초)
  - [x] `setup_test_logging` fixture: 자동 로깅 설정 (모든 E2E 테스트에 자동 적용)
    - [x] 로그 파일 저장 (`tests/logs/{test_name}_{timestamp}.log`)
    - [x] DEBUG 레벨 로깅
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
    - [ ] 로그 파일 저장 (`tests/logs/`, 자동 적용)
    - [ ] 실행 결과 저장 (`tests/results/`, 상세 API 응답 결과)
    - [ ] 로그 파일 저장 (`tests/logs/`, 자동 적용)
    - [ ] 실행 결과 저장 (`tests/results/`, 상세 API 응답 결과)
    - [ ] 발견된 문제점 및 개선 사항 문서화
  - [ ] **백엔드 서비스 완전성 검증 (프론트엔드 구현 전 필수)**
    - [ ] 모든 API 엔드포인트가 정상 동작하는지 확인
    - [ ] API 응답 형식이 프론트엔드에서 사용 가능한지 확인
    - [ ] 에러 응답 형식의 일관성 확인
    - [ ] CORS 설정 확인
    - [ ] 백엔드 E2E 테스트 완료 후에만 Phase 7(프론트엔드) 진행

**산출물**: 완전한 FastAPI 백엔드, API 문서 (OpenAPI/Swagger), E2E 테스트 완료 및 검증 리포트, 백엔드 서비스 완전성 검증 완료

### README 업데이트 (Phase 6 완료 후)
- [ ] `README.md` 업데이트
  - [ ] API 엔드포인트 문서 추가
  - [ ] API 사용 예시 추가 (curl 또는 코드 예시)
  - [ ] OpenAPI/Swagger 문서 링크 추가
  - [ ] 프로젝트 구조 업데이트

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

### README 업데이트 (Phase 7 완료 후)
- [ ] `README.md` 업데이트
  - [ ] UI 스크린샷 추가
  - [ ] 사용자 가이드 추가
  - [ ] 전체 사용 흐름 설명 추가

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

### README 최종 업데이트 (Phase 8 완료 후)
- [ ] `README.md` 최종 업데이트
  - [ ] 배포 가이드 추가
  - [ ] 트러블슈팅 섹션 추가
  - [ ] 전체 프로젝트 구조 최종 반영
  - [ ] 변경 이력 섹션 추가 (Phase별 완료 사항)

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

## README 업데이트 가이드라인

### 최초 작성 시점
- **Phase 1 완료 직후**: 프로젝트 기본 구조가 생성된 후 최초 작성
- 실제 디렉토리 구조를 반영하여 작성
- 개발 환경 설정 완료 후 설치/실행 방법을 정확히 기술

### 업데이트 시점 및 주기

#### 1. Phase 완료 시마다 (필수)
각 Phase 완료 후 해당 Phase의 내용을 README에 추가/업데이트:
- Phase 2: 파서 모듈 설명, 파싱 예시
- Phase 3: 이벤트 정규화 설명
- Phase 4: Timeline/Issue Cards 생성 설명, 출력 예시
- Phase 5: 스니펫 관리 설명
- Phase 6: API 엔드포인트 문서, API 사용 예시
- Phase 7: UI 스크린샷, 사용자 가이드
- Phase 8: 배포 가이드, 트러블슈팅

#### 2. 프로젝트 구조 변경 시 (필수)
다음 변경 시 즉시 업데이트:
- 새 디렉토리 추가/삭제
- 주요 파일 위치 변경
- 설정 파일 추가/변경
- 의존성 패키지 추가/변경

#### 3. 정기 업데이트 (권장)
- **주 1회**: 진행 상황 반영 및 전체 내용 검토
- **Phase 시작 전**: 예정 작업 확인 및 README와 일치 여부 점검

### README 업데이트 체크리스트

각 Phase 완료 후 다음 항목 확인:
- [ ] 디렉토리 구조가 실제와 일치하는가?
- [ ] 새로 추가된 디렉토리/파일이 반영되었는가?
- [ ] 설치 명령어가 정확한가?
- [ ] 실행 방법이 최신인가?
- [ ] 환경 변수 설정이 완전한가?
- [ ] 새로 구현된 기능이 설명되었는가?
- [ ] API 엔드포인트가 문서화되었는가?
- [ ] 사용 예시가 최신인가?
- [ ] 링크가 유효한가?
- [ ] 새 문서가 추가되었는가?

### README 구조 권장 사항

```markdown
# Longtext Analysis

## 📋 프로젝트 개요
- 목적 및 배경
- 주요 기능

## 🏗️ 프로젝트 구조
```
실제 디렉토리 구조
```

## 🚀 시작하기
### 필수 요구사항
### 설치 방법
### 환경 변수 설정
### 실행 방법

## 📖 사용 가이드
### 입력 파일 형식
### 출력 형식
### API 사용법

## 🧪 테스트
### 테스트 실행 방법
### E2E 테스트

## 📚 참고 문서
- PRD
- TODOs.md
- AGENTS.md

## 🔧 개발 가이드
### 코드 스타일
### 커밋 규칙
### Phase별 진행 상황

## 📝 변경 이력
- Phase별 완료 사항
- 최근 업데이트
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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선 및 타입 체계 개선)

**마지막 업데이트**: 2025-12-26

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19 완료)
  - Poetry 프로젝트 초기화 완료
  - 백엔드/프론트엔드 디렉토리 구조 생성 완료
  - FastAPI 앱 초기화 완료 (`backend/main.py`)
  - 기본 문서 및 설정 파일 생성 완료
- Phase 2: 백엔드 파서 구현 (마크다운 파싱) (2025-12-19 완료)
  - 텍스트 정규화 모듈 구현 완료
  - 세션 메타데이터 추출 모듈 구현 완료
  - Turn 블록 파싱 모듈 구현 완료
  - 코드 스니펫 추출 모듈 구현 완료 (`turn_index` 포함)
  - Artifact 추출 모듈 구현 완료
  - 단위 테스트 완료 (6개 테스트 통과)
  - E2E 테스트 완료 (로그/결과 자동 저장)
  - README 업데이트 완료
- Phase 3.0: 이벤트 추출 및 정규화 기본 구현 (2025-12-20 완료)
  - EventType Enum 및 Event 모델 정의 완료 (`backend/core/models.py`)
  - 상수 정의 완료 (`backend/core/constants.py`)
  - 이벤트 정규화 모듈 기본 구현 완료 (`backend/builders/event_normalizer.py`)
  - 단위 테스트 완료 (6개 테스트 통과)
  - E2E 테스트 완료 (로그/결과 자동 저장, 리포트 생성)
  - 문제점 발견: 이벤트 중복 생성, Summary 품질, 타입 분류 정확도

**진행 중인 Phase**:
- Phase 3.1: 즉시 개선 (정규식 기반) - 완료 (2025-12-20)
  - ✅ 이벤트 중복 생성 방지 (117개 → 67개, 1:1 매핑 달성)
  - ✅ Summary 품질 개선 (줄바꿈 정리, 의미 있는 위치에서 자르기)
  - ✅ 타입 분류 엄격화 (구체적인 패턴 사용)
  - 대략적 평가 완료: [docs/phase3_1_evaluation.md](docs/phase3_1_evaluation.md)
  - **참고**: Phase 3.3에서 평가 로직 구축 후 재평가 예정
- Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료 (2025-12-20)
  - ✅ Event 모델에 `processing_method` 필드 추가
  - ✅ LLM 서비스 구현 (gpt-4.1-mini, 파일 기반 캐싱, `.env` 자동 로드)
  - ✅ 이벤트 정규화 모듈에 LLM 옵션 추가 (`use_llm` 파라미터)
  - ✅ LLM 서비스 테스트 작성 (API 키 있으면 자동 실행)
  - ✅ LLM 기반 E2E 테스트 완료 (67개 Turn → 67개 Event, 1:1 매핑 달성)
  - ✅ E2E 테스트 결과 분석 완료: [docs/phase3_2_e2e_analysis.md](docs/phase3_2_e2e_analysis.md)
  - ⚠️ 남은 이슈: LLM 기반에서 `artifact` 타입 이벤트가 0개로 분류됨 (artifacts 배열에는 포함됨)
- Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선 - 완료 (2025-12-22)
  - ✅ 병렬 처리 로직 구현 완료 (`ThreadPoolExecutor`, max_workers=5)
  - ✅ 성능 향상 확인: 224초 → 44.99초 (약 5배 향상)
  - ✅ 로그 파일 fixture 개선 완료 (디버깅 로직 추가, FileHandler flush 처리, 테스트로 검증)
  - ✅ 캐시 시스템 개선 완료
    - ✅ 결정적 해시 함수 (SHA-256) 구현
    - ✅ 원자적 파일 저장 (임시 파일 + 원자적 이동) 구현
    - ✅ 텍스트 해시 검증 구현
    - ✅ Fallback 캐시 저장 구현
    - ✅ 캐시 메타데이터 추가
    - ✅ 캐시 통계 개선 (히트율, 디렉토리 통계)
  - ✅ 캐시 성능 검증: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상)
  - ✅ 캐시 히트율 100% 달성 (두 번째 실행 기준)
  - ✅ 커서룰 업데이트 완료 (`.cursor/rules/llm-service.mdc`)
  - [ ] 에러 케이스 테스트 추가 (선택적, Phase 4 이후 진행 가능)
- Phase 3.3: 결과 평가 방법 구축 - 완료 (2025-12-23)
  - ✅ 정성적 평가 도구 구현 완료 (`backend/builders/evaluation.py`)
  - ✅ Golden 파일 관리 도구 구현 완료
  - ✅ E2E 테스트에 평가 도구 통합 완료
  - ✅ 수동 검증 프로세스 실행 완료 (수동 검증 데이터셋 생성 및 검증 완료)
  - ⏸️ Golden 파일 생성: 보류 (Phase 3.4 이벤트 정규화 품질 개선 완료 후 작성 예정)
  - **수동 검증 결과**: 전체적으로 크게 나쁘지 않음, Phase 4 진행 후 재평가 예정
- Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선 - 진행 중 (2025-12-23 시작)
  - **컨텍스트**: Phase 4 완료 후 문제 발견 → Phase 3으로 돌아온 개선 작업 (Iterative Improvement Cycle)
  - Phase 4 E2E 테스트 결과 분석 완료 (Timeline/Issue Cards 품질 문제 발견)
  - ✅ 수동 검증 파일 재작성 완료 (2025-12-23)
    - ✅ HTML 형식으로 모든 이벤트 추출 (67개 이벤트)
    - ✅ 사용자 수동 검증 완료 (텍스트 파일 기록)
    - ✅ 텍스트 파일 파싱 스크립트 작성 및 실행 완료
    - ✅ manual_review_updated.json 생성 완료 (67개 이벤트 검증 데이터 포함)
  - ✅ HTML 수동 검증 스크립트 개선 완료 (2025-12-25)
    - ✅ 스크립트 분리: `create_html_review.py` (HTML만, 비용 없음), `create_events_for_review.py` (이벤트 정규화만, 선택적)
    - ✅ 기존 스크립트 삭제: `create_all_events_html_review.py` (혼선 방지)
    - ✅ 워크플로우 명확화: E2E 테스트 → HTML 생성 (비용 없음)
  - 이벤트 정규화 품질 개선 작업 진행 중
    - [x] 1단계: 정량적 평가 실행 (`evaluate_manual_review()` 실행) - 완료
    - [x] 2단계: 정성적 분석 - Notes 내용 확인 (67개 샘플 순회, notes 필드 하나씩 확인) - 완료
    - [x] 3단계: 문제 원인 분석 및 개선 방안 도출 - 완료
    - [x] 4단계: 개선 방안 검토 및 승인 (with 사용자) - 완료
    - [x] 5단계: 개선 작업 실행 (Type 추출 로직, Summary 로직 수정) - 완료
      - [x] LLM 서비스에 Artifact 정보 포함 (code_blocks, path_candidates)
      - [x] 캐시 키 생성 시 Artifact 정보 포함
      - [x] 맥락 정보 수집 함수 구현 (_collect_context_info, _collect_context_info_with_events)
      - [x] 이벤트 정규화 함수에 맥락 정보 전달
      - [x] Artifact 타입 분류 강화
      - [x] LLM 프롬프트 개선 (요약 규칙, 특수 기호 의미 명시, max_tokens 증가)
    - [x] 6단계: E2E 재평가 (개선 전후 비교) - 완료
      - [x] 개선된 이벤트 정규화 로직으로 E2E 테스트 재실행 완료
      - [x] 결과 파일 생성: `tests/results/event_normalizer_e2e_llm_20251225_183334.json`
      - [x] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 - 완료
        - [x] 사용자 수동 검증 완료 (2025-12-25)
        - [x] 타입 체계 개선 계획 수립 완료
        - [x] 상세 개선 계획 문서 작성: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md)
      - [ ] 개선 전후 비교 분석 (타입 체계 개선 구현 후 진행)
    - [x] 7단계: 타입 체계 개선 구현 (2025-12-26 완료)
      - [x] **⚠️ 시작 전 필수**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 문서 읽기
      - [x] Step 1: EventType Enum 수정 완료
      - [x] Step 2: ArtifactAction Enum 추가 완료
      - [x] Step 3: 분류 로직 개선 완료
      - [x] Step 4: LLM 프롬프트 수정 완료
      - [x] Step 5: 평가 도구 업데이트 완료
      - [x] Step 6: E2E 테스트 재실행 및 검증 완료
      - [x] Step 7: 수동 검증 결과 확인 완료 (HTML 생성 및 사용자 검증 완료)
    - [ ] 8단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 타입 체계 개선 구현 완료 (2025-12-26)
  - ✅ Step 1-7 완료
  - [ ] Step 8: Phase 완료 작업 (TODOs.md 업데이트, Git commit)
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)

