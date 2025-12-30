# Phase 4-2
_Exported on 12/29/2025 at 14:32:44 GMT+9 from Cursor (2.2.44)_

---

**User**

@TODOs.md 를 바탕으로 프로젝트의 현재 상황을 파악하세요

---

**Cursor**

TODOs.md와 관련 파일을 검토해 현재 상황을 파악 중입니다.


TODOs.md를 바탕으로 프로젝트 현황을 정리했습니다.

## 프로젝트 현황 요약

### 현재 진행 상황

**현재 Phase**: Phase 3.4 (이벤트 정규화 품질 개선) - 진행 중

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3.0: 이벤트 정규화 기본 구현 (2025-12-20)
- Phase 3.1: 즉시 개선 (정규식 기반) (2025-12-20)
- Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) (2025-12-20)
- Phase 3.2.1: LLM 병렬 처리 및 캐시 시스템 개선 (2025-12-22)
- Phase 3.3: 결과 평가 방법 구축 (2025-12-23)

**진행 중인 Phase**:
- Phase 3.4: 이벤트 정규화 품질 개선
  - 수동 검증 파일 재작성 완료 (2025-12-23)
  - 67개 이벤트 전체 검증 완료
  - 다음 단계: 수동 검증 결과 평가 및 원인 분석 대기

**부분 완료된 Phase**:
- Phase 4: Timeline 및 Issue Cards 생성
  - 구조적 정합성 검증 완료
  - 내용 품질 검증 미완료 (Phase 3.4 완료 후 재검증 예정)

### 주요 성과

1. 성능 개선
   - 병렬 처리: 224초 → 44.99초 (약 5배)
   - 캐시 시스템: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배)
   - 캐시 히트율: 100% (두 번째 실행 기준)

2. 품질 개선
   - 이벤트 중복 생성 해결: 117개 → 67개 (1:1 매핑)
   - LLM 기반 타입 분류 적용
   - 수동 검증 시스템 구축 완료

### 현재 상태 및 다음 단계

**Phase 3.4 진행 상황**:
- 수동 검증 파일 재작성 완료
  - 파일 위치: `tests/manual_review/all_events_html_review_20251223_212658/manual_review_updated.json`
  - 67개 이벤트 검증 데이터 포함
- 대기 중인 작업:
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백

**발견된 문제점** (Phase 4 E2E 테스트 결과):
- Timeline: 이벤트 타입 분류 부정확 (메타데이터가 "turn" 타입으로 분류)
- Timeline: Summary가 단순 텍스트 자르기만 수행
- Issue Cards: 이벤트 Summary 품질 문제로 핵심 내용 추출 실패
- Issue Cards: Root cause, Fix, Validation 추출이 중간 과정 텍스트를 그대로 포함

### 프로젝트 구조

```
backend/
├── parser/          ✅ 완료 (마크다운 파싱)
├── builders/        ✅ 완료 (이벤트 정규화, Timeline, Issue Cards)
├── core/            ✅ 완료 (모델, 상수, LLM 서비스, 캐시)
├── api/routes/      ⏸️ 미시작 (Phase 6)
└── render/          ⏸️ 미시작 (Phase 6)

tests/
├── fixtures/        ✅ 완료
├── golden/          ⏸️ 부분 완료 (Phase 3.4 완료 후 생성 예정)
├── manual_review/   ✅ 완료 (수동 검증 데이터셋)
├── logs/            ✅ 완료 (자동 로깅)
├── reports/         ✅ 완료 (E2E 테스트 리포트)
└── results/         ✅ 완료 (상세 실행 결과)
```

### 다음 단계 권장 사항

1. 즉시 진행: Phase 3.4 완료
   - 수동 검증 결과 평가 실행
   - 원인 분석 및 개선 방향 결정
   - Type/Summary 로직 수정
   - E2E 재평가

2. Phase 3.4 완료 후: Phase 4 재검증
   - Timeline/Issue Cards 품질 재평가
   - Phase 3.4 개선 효과 검증

3. 이후 진행: Phase 5-8
   - Phase 5: 코드 스니펫 분리 및 저장
   - Phase 6: 백엔드 API 구현
   - Phase 7: 프론트엔드 UI 구현
   - Phase 8: 통합 테스트 및 QA

현재 Phase 3.4의 수동 검증 결과 평가 단계입니다. 다음 작업을 진행할까요?

```plaintext
backend/
├── parser/          ✅ 완료 (마크다운 파싱)
├── builders/        ✅ 완료 (이벤트 정규화, Timeline, Issue Cards)
├── core/            ✅ 완료 (모델, 상수, LLM 서비스, 캐시)
├── api/routes/      ⏸️ 미시작 (Phase 6)
└── render/          ⏸️ 미시작 (Phase 6)

tests/
├── fixtures/        ✅ 완료
├── golden/          ⏸️ 부분 완료 (Phase 3.4 완료 후 생성 예정)
├── manual_review/   ✅ 완료 (수동 검증 데이터셋)
├── logs/            ✅ 완료 (자동 로깅)
├── reports/         ✅ 완료 (E2E 테스트 리포트)
└── results/         ✅ 완료 (상세 실행 결과)
```

---

**User**

코드베이스를 좀더 파악해서 3.4의 더 자세한 상황과 할일을 파악하세요

---

**Cursor**

Phase 3.4의 세부 상황 파악을 위해 관련 파일 확인 중입니다.


Phase 3.4 세부 상황 파악을 위해 추가 파일 확인 중입니다.


Phase 3.4 세부 상황 파악을 위해 추가 확인 중입니다.


Phase 3.4 세부 상황과 할 일 정리 중입니다.


Phase 3.4 세부 상황과 할 일을 정리했습니다.

## Phase 3.4 현재 상황 상세 분석

### 완료된 작업

1. 수동 검증 파일 재작성 (2025-12-23 완료)
   - 파일 위치: `tests/manual_review/all_events_html_review_20251223_212658/manual_review_updated.json`
   - 67개 이벤트 전체 검증 완료
   - 검증 데이터 포함: `correct_type`, `type_accuracy`, `summary_quality`, `summary_completeness`, `notes`

2. 평가 도구 준비 완료
   - `evaluate_manual_review()` 함수 구현 완료 (`backend/builders/evaluation.py`)
   - `create_golden_file_from_manual_review()` 함수 구현 완료

### 대기 중인 작업

1. 수동 검증 결과 평가 실행
   - `evaluate_manual_review()` 함수 실행 필요
   - 평가 결과 분석 및 리포트 생성

2. 원인 분석
   - 타입 분류 부정확 원인 분석
   - Summary 품질 문제 원인 분석

3. 개선 작업
   - Type 추출 로직 수정
   - Summary 로직 수정

### 발견된 문제점 (Phase 4 E2E 테스트 결과 기반)

1. Timeline 타입 분류 문제
   - 메타데이터 Turn이 "turn" 타입으로 분류됨 (실제로는 "status_review"여야 함)
   - LLM 기반 결과와 Timeline 결과 불일치
     - LLM 기반: status_review 25개, plan 21개
     - Timeline 결과: turn 31개, debug 26개 (정규식 기반으로 실행된 것으로 보임)

2. Summary 품질 문제
   - Timeline에서 Summary가 단순 텍스트 자르기만 수행
   - Issue Cards에서 Summary 품질 문제로 핵심 내용 추출 실패

3. Issue Cards 문제
   - Root cause, Fix, Validation 추출이 중간 과정 텍스트를 그대로 포함

### 다음 단계 계획

다음 단계를 진행할까요?

1. 수동 검증 결과 평가 실행
   - `evaluate_manual_review()` 함수로 정확도 계산
   - 혼동 행렬 분석
   - 처리 방법별 정확도 비교 (regex vs llm)

2. 평가 결과 분석 및 원인 파악
   - 타입 분류 오류 패턴 분석
   - Summary 품질 문제 패턴 분석

3. 개선 방향 결정
   - Type 추출 로직 개선 방안
   - Summary 로직 개선 방안

수동 검증 결과 평가부터 진행할까요?

---

**User**

그전에, 
먼저 AGENTS.md와 커서룰을 통해 프로젝트의 기본 실행 규칙을 숙지하세요

---

**Cursor**

AGENTS.md와 커서룰을 확인해 프로젝트의 기본 실행 규칙을 파악 중입니다.


나머지 커서룰 파일 확인 중입니다.


프로젝트 기본 실행 규칙을 파악했습니다. Phase 3.4 작업 계획을 수립합니다.

## 프로젝트 기본 실행 규칙 요약

### 핵심 원칙 (AGENTS.md)
1. Phase별 진행: 한 번에 여러 Phase 진행 금지, 각 Phase 완료 후 피드백 대기
2. 설명 우선: 작업 전 설명 → 사용자 확인 → 실행 → 결과 해석
3. Phase 완료 시 필수: TODOs.md 업데이트 → Git commit (`feat: Phase X 완료 - [제목]`)
4. PowerShell 표준: 세미콜론(`;`) 사용, `cd` 금지, 프로젝트 루트에서 실행
5. E2E 테스트 우선: 실제 데이터만 사용, Mock 금지, 자동 보고 필수

### 기술 규칙 (커서룰)
- LLM 서비스: 타임아웃 120초, 재시도 3회, SHA-256 캐싱, Fallback 필수
- 테스트 전략: Phase 2-5는 모듈 직접 호출, Phase 6+는 실제 서버 실행
- API 계약 동기화: 백엔드-프론트엔드 상수/Enum 일치 필수
- 이벤트 정규화: 1:1 Turn-Event 매핑, 우선순위 기반 단일 이벤트 생성

---

## Phase 3.4 작업 계획

### 현재 상황
- 수동 검증 완료: `tests/manual_review/all_events_html_review_20251223_212658/manual_review_updated.json` (67개 이벤트 전체 검증)
- 평가 함수 준비: `evaluate_manual_review()` 구현 완료
- E2E 테스트 결과: `tests/results/event_normalizer_e2e_llm_20251222_224027.json` 존재

### 작업 단계

1. 수동 검증 결과 평가 실행
   - `evaluate_manual_review()` 함수 실행
   - 타입 분류 정확도, 혼동 행렬, 처리 방법별 정확도 계산
   - Summary 품질 점수 분석

2. 평가 결과 분석 및 원인 파악
   - 타입 분류 오류 패턴 분석 (혼동 행렬 기반)
   - Summary 품질 문제 패턴 분석
   - LLM vs Regex 처리 방법 비교

3. 개선 방향 결정 (사용자와 협의)
   - Type 추출 로직 개선 방안
   - Summary 로직 개선 방안

4. 개선 작업 실행
   - Type 추출 로직 수정
   - Summary 로직 수정

5. E2E 재평가
   - 수정된 로직으로 E2E 테스트 재실행
   - 결과 비교 및 품질 개선 확인

6. Phase 완료 작업
   - TODOs.md 업데이트
   - Git commit 실행

이 계획으로 진행할까요?

---

**User**

수동 검증 결과에 대한 평가는 다음을 고려하여야 합니다.
- 현재 방식은 휴리스틱 기반임. 이를 이용한 판단에 한계가 있음
- manual_review_updated.json에서 notes 내용을 충실히 파악하는 것도 중요하니, 당신이 하나씩 내용을 확인해서 이를 바탕으로 문제 원인 및 개선 방안을 도출하는 것이 추가로 필요합니다.

따라서 이것을 계획에 포함하세요

계획세우고 하나씩 진행합시다

---

**Cursor**

수동 검증 결과의 notes를 하나씩 확인해 문제 원인과 개선 방안을 도출하도록 계획에 반영합니다. 먼저 `manual_review_updated.json` 구조를 확인합니다.


notes 필드 내용을 하나씩 확인해 문제 원인과 개선 방안을 도출하도록 계획에 반영합니다.


---

**User**

@TODOs.md 에 상기 내용을 반영하세요
향후 @TODOs.md 를 바탕으로 프로젝트 진행합니다.

---

**Cursor**

TODOs.md에 계획 내용을 반영 중입니다.


```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 1단계: 정량적 평가 실행
  - [ ] `evaluate_manual_review()` 함수 실행
  - [ ] 타입 분류 정확도 계산
  - [ ] 혼동 행렬 생성 및 분석
  - [ ] 처리 방법별 정확도 비교 (LLM vs Regex)
  - [ ] Summary 품질 점수 통계 분석
  - [ ] 평가 결과 리포트 생성 및 저장 (`tests/reports/manual_review_evaluation_YYYYMMDD_HHMMSS.json`)

- [ ] 2단계: 정성적 분석 - Notes 내용 확인
  - [ ] **⚠️ 중요**: 휴리스틱 기반 평가의 한계를 보완하기 위해 notes 내용을 하나씩 확인
  - [ ] `manual_review_updated.json`의 모든 샘플(67개) 순회
  - [ ] 각 샘플의 `notes` 필드 내용 확인
  - [ ] `correct_type`과 `current_event.type`이 다른 경우 notes 확인
  - [ ] `summary_quality` 또는 `summary_completeness`가 3점 이하인 경우 notes 확인
  - [ ] `type_accuracy`가 3점 이하인 경우 notes 확인
  - [ ] notes 내용을 바탕으로 문제 패턴 분류:
    - [ ] 타입 분류 오류 패턴 (예: "status_review로 분류되었지만 실제로는 plan")
    - [ ] Summary 품질 문제 패턴 (예: "요약이 너무 길다", "핵심 내용 누락")
    - [ ] LLM 프롬프트 문제 (예: "LLM이 잘못 이해함")
    - [ ] 정규식 패턴 문제 (예: "패턴이 너무 엄격함")
    - [ ] 맥락 부족 문제 (예: "이전 Turn의 맥락이 없어서 어려움")
    - [ ] 타입 정의 부족 문제 (예: "새로운 type 정의 필요")
  - [ ] Notes 분석 결과 리포트 생성 및 저장 (`tests/reports/manual_review_notes_analysis_YYYYMMDD_HHMMSS.json`)

- [ ] 3단계: 문제 원인 분석 및 개선 방안 도출
  - [ ] Notes 분석 결과를 바탕으로 문제 원인 도출:
    - [ ] 타입 분류 오류 원인 (LLM 프롬프트, 정규식 패턴, 우선순위 로직, 맥락 부족 등)
    - [ ] Summary 품질 문제 원인 (요약 길이, 핵심 내용 추출 실패, 중간 과정 텍스트 포함 등)
  - [ ] 개선 방안 도출:
    - [ ] Type 추출 로직 개선 방안
    - [ ] Summary 로직 개선 방안
    - [ ] LLM 프롬프트 개선 방안 (필요 시)
    - [ ] 정규식 패턴 개선 방안 (필요 시)
    - [ ] 맥락 처리 개선 방안 (이전 Turn 정보 활용)
    - [ ] 타입 정의 확장 방안 (필요 시)
  - [ ] 개선 방안 우선순위화
  - [ ] 개선 계획 문서 생성 (`tests/reports/improvement_plan_YYYYMMDD_HHMMSS.md`)

- [ ] 4단계: 개선 방안 검토 및 승인
  - [ ] 사용자와 개선 방안 검토
  - [ ] 우선순위 조정 (필요 시)
  - [ ] 개선 작업 범위 결정

- [ ] 5단계: 개선 작업 실행
  - [ ] Type 추출 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [ ] 메타데이터 Turn 처리 로직 개선 (메타데이터는 별도 타입으로 분류 또는 제외)
    - [ ] LLM 프롬프트 개선 (타입 분류 정확도 향상)
    - [ ] 정규식 패턴 개선 (타입 분류 정확도 향상)
    - [ ] 타입 분류 우선순위 로직 개선
    - [ ] 맥락 처리 로직 개선 (이전 Turn 정보 활용)
  - [ ] Summary 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [ ] LLM Summary 생성 프롬프트 개선 (핵심 내용만 추출)
    - [ ] 정규식 기반 Summary 생성 로직 개선 (의미 있는 요약 생성)
    - [ ] 텍스트 자르기 로직 개선 (문장/문단 단위로 의미 있는 위치에서 자르기)
    - [ ] 중간 과정 텍스트 필터링 로직 추가
    - [ ] 맥락 기반 Summary 생성 로직 개선 (이전 Turn 정보 활용)

- [ ] 6단계: E2E 재평가
  - [ ] 개선된 이벤트 정규화 로직으로 E2E 테스트 재실행 (`tests/test_event_normalizer_e2e.py`)
  - [ ] 타입 분류 정확도 재측정
  - [ ] Summary 품질 재평가
  - [ ] Timeline/Issue Cards 품질 재검증 (Phase 4 E2E 테스트 재실행)
  - [ ] 개선 전후 비교 분석
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
  - Phase 4 E2E 테스트 결과 분석 완료 (Timeline/Issue Cards 품질 문제 발견)
  - ✅ 수동 검증 파일 재작성 완료 (2025-12-23)
    - ✅ HTML 형식으로 모든 이벤트 추출 (67개 이벤트)
    - ✅ 사용자 수동 검증 완료 (텍스트 파일 기록)
    - ✅ 텍스트 파일 파싱 스크립트 작성 및 실행 완료
    - ✅ manual_review_updated.json 생성 완료 (67개 이벤트 검증 데이터 포함)
  - 이벤트 정규화 품질 개선 작업 진행 예정
    - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
    - [ ] 원인 분석 (with 사용자)
    - [ ] Type 추출 로직 수정
    - [ ] Summary 로직 수정
    - [ ] E2E 재평가
    - [ ] 결과 피드백

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

TODOs.md의 진행 상황 추적 섹션도 업데이트 중입니다.


```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 1단계: 정량적 평가 실행
  - [ ] `evaluate_manual_review()` 함수 실행
  - [ ] 타입 분류 정확도 계산
  - [ ] 혼동 행렬 생성 및 분석
  - [ ] 처리 방법별 정확도 비교 (LLM vs Regex)
  - [ ] Summary 품질 점수 통계 분석
  - [ ] 평가 결과 리포트 생성 및 저장 (`tests/reports/manual_review_evaluation_YYYYMMDD_HHMMSS.json`)

- [ ] 2단계: 정성적 분석 - Notes 내용 확인
  - [ ] **⚠️ 중요**: 휴리스틱 기반 평가의 한계를 보완하기 위해 notes 내용을 하나씩 확인
  - [ ] `manual_review_updated.json`의 모든 샘플(67개) 순회
  - [ ] 각 샘플의 `notes` 필드 내용 확인
  - [ ] `correct_type`과 `current_event.type`이 다른 경우 notes 확인
  - [ ] `summary_quality` 또는 `summary_completeness`가 3점 이하인 경우 notes 확인
  - [ ] `type_accuracy`가 3점 이하인 경우 notes 확인
  - [ ] notes 내용을 바탕으로 문제 패턴 분류:
    - [ ] 타입 분류 오류 패턴 (예: "status_review로 분류되었지만 실제로는 plan")
    - [ ] Summary 품질 문제 패턴 (예: "요약이 너무 길다", "핵심 내용 누락")
    - [ ] LLM 프롬프트 문제 (예: "LLM이 잘못 이해함")
    - [ ] 정규식 패턴 문제 (예: "패턴이 너무 엄격함")
    - [ ] 맥락 부족 문제 (예: "이전 Turn의 맥락이 없어서 어려움")
    - [ ] 타입 정의 부족 문제 (예: "새로운 type 정의 필요")
  - [ ] Notes 분석 결과 리포트 생성 및 저장 (`tests/reports/manual_review_notes_analysis_YYYYMMDD_HHMMSS.json`)

- [ ] 3단계: 문제 원인 분석 및 개선 방안 도출
  - [ ] Notes 분석 결과를 바탕으로 문제 원인 도출:
    - [ ] 타입 분류 오류 원인 (LLM 프롬프트, 정규식 패턴, 우선순위 로직, 맥락 부족 등)
    - [ ] Summary 품질 문제 원인 (요약 길이, 핵심 내용 추출 실패, 중간 과정 텍스트 포함 등)
  - [ ] 개선 방안 도출:
    - [ ] Type 추출 로직 개선 방안
    - [ ] Summary 로직 개선 방안
    - [ ] LLM 프롬프트 개선 방안 (필요 시)
    - [ ] 정규식 패턴 개선 방안 (필요 시)
    - [ ] 맥락 처리 개선 방안 (이전 Turn 정보 활용)
    - [ ] 타입 정의 확장 방안 (필요 시)
  - [ ] 개선 방안 우선순위화
  - [ ] 개선 계획 문서 생성 (`tests/reports/improvement_plan_YYYYMMDD_HHMMSS.md`)

- [ ] 4단계: 개선 방안 검토 및 승인
  - [ ] 사용자와 개선 방안 검토
  - [ ] 우선순위 조정 (필요 시)
  - [ ] 개선 작업 범위 결정

- [ ] 5단계: 개선 작업 실행
  - [ ] Type 추출 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [ ] 메타데이터 Turn 처리 로직 개선 (메타데이터는 별도 타입으로 분류 또는 제외)
    - [ ] LLM 프롬프트 개선 (타입 분류 정확도 향상)
    - [ ] 정규식 패턴 개선 (타입 분류 정확도 향상)
    - [ ] 타입 분류 우선순위 로직 개선
    - [ ] 맥락 처리 로직 개선 (이전 Turn 정보 활용)
  - [ ] Summary 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [ ] LLM Summary 생성 프롬프트 개선 (핵심 내용만 추출)
    - [ ] 정규식 기반 Summary 생성 로직 개선 (의미 있는 요약 생성)
    - [ ] 텍스트 자르기 로직 개선 (문장/문단 단위로 의미 있는 위치에서 자르기)
    - [ ] 중간 과정 텍스트 필터링 로직 추가
    - [ ] 맥락 기반 Summary 생성 로직 개선 (이전 Turn 정보 활용)

- [ ] 6단계: E2E 재평가
  - [ ] 개선된 이벤트 정규화 로직으로 E2E 테스트 재실행 (`tests/test_event_normalizer_e2e.py`)
  - [ ] 타입 분류 정확도 재측정
  - [ ] Summary 품질 재평가
  - [ ] Timeline/Issue Cards 품질 재검증 (Phase 4 E2E 테스트 재실행)
  - [ ] 개선 전후 비교 분석
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
  - Phase 4 E2E 테스트 결과 분석 완료 (Timeline/Issue Cards 품질 문제 발견)
  - ✅ 수동 검증 파일 재작성 완료 (2025-12-23)
    - ✅ HTML 형식으로 모든 이벤트 추출 (67개 이벤트)
    - ✅ 사용자 수동 검증 완료 (텍스트 파일 기록)
    - ✅ 텍스트 파일 파싱 스크립트 작성 및 실행 완료
    - ✅ manual_review_updated.json 생성 완료 (67개 이벤트 검증 데이터 포함)
  - 이벤트 정규화 품질 개선 작업 진행 중
    - [ ] 1단계: 정량적 평가 실행 (`evaluate_manual_review()` 실행)
    - [ ] 2단계: 정성적 분석 - Notes 내용 확인 (67개 샘플 순회, notes 필드 하나씩 확인)
    - [ ] 3단계: 문제 원인 분석 및 개선 방안 도출
    - [ ] 4단계: 개선 방안 검토 및 승인 (with 사용자)
    - [ ] 5단계: 개선 작업 실행 (Type 추출 로직, Summary 로직 수정)
    - [ ] 6단계: E2E 재평가 (개선 전후 비교)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

TODOs.md에 계획 내용을 반영했습니다.

## 업데이트 내용

### Phase 3.4 섹션 개선
1. **7단계 작업 프로세스로 구체화**
   - 1단계: 정량적 평가 실행
   - 2단계: 정성적 분석 - Notes 내용 확인 (중요)
   - 3단계: 문제 원인 분석 및 개선 방안 도출
   - 4단계: 개선 방안 검토 및 승인
   - 5단계: 개선 작업 실행
   - 6단계: E2E 재평가
   - 7단계: Phase 완료 작업

2. **2단계 정성적 분석 상세화**
   - 67개 샘플 순회
   - 각 샘플의 `notes` 필드 확인
   - 문제 패턴 분류 (타입 분류 오류, Summary 품질 문제, LLM 프롬프트 문제, 정규식 패턴 문제, 맥락 부족 문제, 타입 정의 부족 문제)
   - Notes 분석 결과 리포트 생성

3. **3단계 문제 원인 분석 확장**
   - 맥락 처리 개선 방안 추가
   - 타입 정의 확장 방안 추가

4. **진행 상황 추적 섹션 업데이트**
   - 7단계 작업 프로세스 반영

이제 TODOs.md를 기준으로 Phase 3.4를 진행할 수 있습니다. 1단계(정량적 평가 실행)부터 시작할까요?

---

**User**

자 단계적으로 진행

---

**Cursor**

1단계(정량적 평가 실행)부터 진행합니다. 필요한 파일을 확인하고 평가 스크립트를 작성합니다.


1단계 정량적 평가 실행 스크립트 작성 중입니다.


```python
"""
수동 검증 결과 정량적 평가 스크립트

Phase 3.4 1단계: 정량적 평가 실행
- evaluate_manual_review() 함수 실행
- 타입 분류 정확도 계산
- 혼동 행렬 생성 및 분석
- 처리 방법별 정확도 비교 (LLM vs Regex)
- Summary 품질 점수 통계 분석
- 평가 결과 리포트 생성 및 저장
"""

import argparse
import json
from pathlib import Path
from datetime import datetime
from backend.builders.evaluation import evaluate_manual_review
from backend.core.models import Event, Turn


def load_events_and_turns_from_results(results_file: Path):
    """
    E2E 테스트 결과 파일에서 Event와 Turn 리스트 로드
    
    Args:
        results_file: E2E 테스트 결과 파일 경로
    
    Returns:
        (events, turns) 튜플
    """
    with open(results_file, "r", encoding="utf-8") as f:
        results_data = json.load(f)
    
    # Event 리스트 복원
    events_dict = {e["turn_ref"]: Event(**e) for e in results_data.get("events", [])}
    events_list = list(events_dict.values())
    
    # Turn 리스트 복원 (turns 필드가 있으면 사용, 없으면 빈 리스트)
    turns_list = []
    if "turns" in results_data:
        turns_dict = {
            t["turn_index"]: Turn(**t) 
            for t in results_data.get("turns", []) 
            if "turn_index" in t
        }
        turns_list = list(turns_dict.values())
    
    return events_list, turns_list


def main():
    parser = argparse.ArgumentParser(
        description="수동 검증 결과 정량적 평가 실행"
    )
    parser.add_argument(
        "--review-file",
        type=str,
        required=True,
        help="수동 검증 결과 파일 경로 (manual_review_updated.json)"
    )
    parser.add_argument(
        "--results-file",
        type=str,
        default=None,
        help="E2E 테스트 결과 파일 경로 (event_normalizer_e2e_llm_*.json, 선택적)"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="출력 리포트 파일 경로 (기본값: tests/reports/manual_review_evaluation_YYYYMMDD_HHMMSS.json)"
    )
    
    args = parser.parse_args()
    
    review_file = Path(args.review_file)
    results_file = Path(args.results_file) if args.results_file else None
    
    # 파일 존재 확인
    if not review_file.exists():
        print(f"[ERROR] Review file not found: {review_file}")
        return 1
    
    # E2E 테스트 결과 파일이 있으면 events와 turns 로드
    events = None
    turns = None
    if results_file and results_file.exists():
        print(f"[INFO] Loading events and turns from: {results_file}")
        events, turns = load_events_and_turns_from_results(results_file)
        print(f"[INFO] Loaded {len(events)} events, {len(turns)} turns")
    else:
        print(f"[INFO] Results file not provided or not found, evaluating without events/turns")
    
    # 정량적 평가 실행
    print(f"\n[INFO] Evaluating manual review: {review_file}")
    evaluation = evaluate_manual_review(review_file, events=events, turns=turns)
    
    # 평가 결과 출력
    print("\n" + "=" * 70)
    print("Manual Review Evaluation Report (Quantitative)")
    print("=" * 70)
    
    # 메타데이터
    metadata = evaluation.get("metadata", {})
    print(f"\n[Metadata]")
    print(f"  Total samples: {metadata.get('total_samples', 0)}")
    print(f"  Evaluated samples: {metadata.get('evaluated_samples', 0)}")
    
    # 타입 분류 정확도
    type_classification = evaluation.get("type_classification", {})
    type_accuracy = type_classification.get("accuracy", 0.0)
    type_correct = type_classification.get("correct", 0)
    type_total = type_classification.get("total", 0)
    
    print(f"\n[Type Classification Accuracy]")
    print(f"  Accuracy: {type_accuracy:.2%} ({type_correct}/{type_total})")
    
    # 혼동 행렬
    confusion_matrix = type_classification.get("confusion_matrix", {})
    if confusion_matrix:
        print(f"\n[Confusion Matrix]")
        print(f"  Format: predicted_type -> actual_type: count")
        for predicted, actuals in sorted(confusion_matrix.items()):
            for actual, count in sorted(actuals.items()):
                if predicted != actual:  # 오류만 표시
                    print(f"    {predicted} -> {actual}: {count}")
    
    # Summary 품질
    summary_quality = evaluation.get("summary_quality", {})
    avg_quality = summary_quality.get("average_quality")
    avg_completeness = summary_quality.get("average_completeness")
    quality_count = summary_quality.get("samples_count", 0)
    
    print(f"\n[Summary Quality]")
    if avg_quality is not None:
        print(f"  Average quality: {avg_quality:.2f} / 5.0 ({quality_count} samples)")
    if avg_completeness is not None:
        print(f"  Average completeness: {avg_completeness:.2f} / 5.0 ({quality_count} samples)")
    
    # Type accuracy scores
    type_accuracy_scores = evaluation.get("type_accuracy_scores", {})
    avg_type_accuracy = type_accuracy_scores.get("average")
    accuracy_count = type_accuracy_scores.get("samples_count", 0)
    
    if avg_type_accuracy is not None:
        print(f"\n[Type Accuracy Scores (Manual)]")
        print(f"  Average: {avg_type_accuracy:.2f} / 5.0 ({accuracy_count} samples)")
    
    # 처리 방법별 정확도
    method_comparison = evaluation.get("method_comparison", {})
    if method_comparison:
        print(f"\n[Method Comparison]")
        for method, stats in sorted(method_comparison.items()):
            acc = stats.get("accuracy", 0.0)
            correct = stats.get("correct", 0)
            total = stats.get("total", 0)
            print(f"  {method}: {acc:.2%} ({correct}/{total})")
    
    print("\n" + "=" * 70)
    
    # 리포트 파일 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if args.output_file:
        output_file = Path(args.output_file)
    else:
        reports_dir = Path(__file__).parent.parent / "tests" / "reports"
        reports_dir.mkdir(exist_ok=True)
        output_file = reports_dir / f"manual_review_evaluation_{timestamp}.json"
    
    # 평가 결과에 메타데이터 추가
    evaluation_report = {
        "evaluation_metadata": {
            "timestamp": timestamp,
            "review_file": str(review_file),
            "results_file": str(results_file) if results_file else None,
        },
        **evaluation
    }
    
    output_file.write_text(
        json.dumps(evaluation_report, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    
    print(f"\n[SUCCESS] Evaluation report saved to: {output_file}")
    
    return 0


if __name__ == "__main__":
    exit(main())

```

1단계 정량적 평가 완료. 결과 요약:

- 타입 분류 정확도: 62.69% (42/67)
- Summary 품질: 평균 3.95/5.0 (66개 샘플)
- Summary 완전성: 평균 4.03/5.0 (66개 샘플)
- Type accuracy scores: 평균 3.45/5.0 (67개 샘플)

주요 혼동 패턴:
- `status_review` → `debug`: 10개
- `plan` → `debug`: 4개
- `turn` → `debug`: 3개
- `status_review` → `artifact`: 2개
- `plan` → `artifact`: 2개

2단계(정성적 분석 - Notes 내용 확인)로 진행합니다. `manual_review_updated.json`의 모든 샘플을 순회하며 notes를 분석하는 스크립트를 작성합니다.


```python
"""
수동 검증 Notes 정성적 분석 스크립트

Phase 3.4 2단계: 정성적 분석 - Notes 내용 확인
- manual_review_updated.json의 모든 샘플(67개) 순회
- 각 샘플의 notes 필드 내용 확인
- 문제 패턴 분류
- Notes 분석 결과 리포트 생성 및 저장
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Any


def analyze_notes(review_file: Path) -> Dict[str, Any]:
    """
    Notes 내용을 분석하여 문제 패턴 분류
    
    Args:
        review_file: 수동 검증 결과 파일 경로
    
    Returns:
        분석 결과 딕셔너리
    """
    # 1. 수동 검증 결과 로드
    with open(review_file, "r", encoding="utf-8") as f:
        review_data = json.load(f)
    
    samples = review_data.get("samples", [])
    if len(samples) == 0:
        return {"error": "No samples found in review file"}
    
    # 2. 분석 결과 저장
    analysis_result = {
        "metadata": {
            "review_file": str(review_file),
            "total_samples": len(samples),
            "samples_with_notes": 0,
            "samples_with_type_mismatch": 0,
            "samples_with_low_quality": 0,
        },
        "notes_by_category": {
            "type_classification_errors": [],
            "summary_quality_issues": [],
            "llm_prompt_issues": [],
            "regex_pattern_issues": [],
            "context_lack_issues": [],
            "type_definition_issues": [],
            "other_issues": [],
        },
        "problem_patterns": {
            "type_mismatches": defaultdict(list),  # predicted -> actual: [samples]
            "low_quality_samples": [],  # summary_quality <= 3 or summary_completeness <= 3
            "low_accuracy_samples": [],  # type_accuracy <= 3
        },
        "detailed_analysis": []
    }
    
    # 3. 각 샘플 분석
    for sample in samples:
        event_id = sample.get("event_id", "UNKNOWN")
        turn_index = sample.get("turn_index", -1)
        current_event = sample.get("current_event", {})
        manual_review = sample.get("manual_review", {})
        
        current_type = current_event.get("type")
        correct_type = manual_review.get("correct_type")
        notes = manual_review.get("notes", "").strip()
        summary_quality = manual_review.get("summary_quality")
        summary_completeness = manual_review.get("summary_completeness")
        type_accuracy = manual_review.get("type_accuracy")
        
        # Notes가 있는 샘플
        if notes:
            analysis_result["metadata"]["samples_with_notes"] += 1
        
        # 타입 불일치 샘플
        type_mismatch = False
        if correct_type is not None and current_type != correct_type:
            type_mismatch = True
            analysis_result["metadata"]["samples_with_type_mismatch"] += 1
            analysis_result["problem_patterns"]["type_mismatches"][f"{current_type} -> {correct_type}"].append({
                "event_id": event_id,
                "turn_index": turn_index,
                "notes": notes
            })
        
        # 낮은 품질 샘플
        low_quality = False
        if (summary_quality is not None and summary_quality <= 3) or \
           (summary_completeness is not None and summary_completeness <= 3):
            low_quality = True
            analysis_result["metadata"]["samples_with_low_quality"] += 1
            analysis_result["problem_patterns"]["low_quality_samples"].append({
                "event_id": event_id,
                "turn_index": turn_index,
                "summary_quality": summary_quality,
                "summary_completeness": summary_completeness,
                "notes": notes
            })
        
        # 낮은 정확도 샘플
        if type_accuracy is not None and type_accuracy <= 3:
            analysis_result["problem_patterns"]["low_accuracy_samples"].append({
                "event_id": event_id,
                "turn_index": turn_index,
                "type_accuracy": type_accuracy,
                "notes": notes
            })
        
        # Notes 내용 분석 및 분류
        if notes:
            notes_lower = notes.lower()
            
            # 타입 분류 오류
            if any(keyword in notes_lower for keyword in ["타입 문제", "타입", "분류", "type"]):
                if "새로운 type 정의 필요" in notes or "type 정의" in notes:
                    analysis_result["notes_by_category"]["type_definition_issues"].append({
                        "event_id": event_id,
                        "turn_index": turn_index,
                        "current_type": current_type,
                        "correct_type": correct_type,
                        "notes": notes
                    })
                else:
                    analysis_result["notes_by_category"]["type_classification_errors"].append({
                        "event_id": event_id,
                        "turn_index": turn_index,
                        "current_type": current_type,
                        "correct_type": correct_type,
                        "notes": notes
                    })
            
            # Summary 품질 문제
            elif any(keyword in notes_lower for keyword in ["요약 문제", "요약", "summary"]):
                analysis_result["notes_by_category"]["summary_quality_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "summary_quality": summary_quality,
                    "summary_completeness": summary_completeness,
                    "notes": notes
                })
            
            # LLM 프롬프트 문제
            elif any(keyword in notes_lower for keyword in ["llm", "프롬프트", "prompt", "이해"]):
                analysis_result["notes_by_category"]["llm_prompt_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })
            
            # 정규식 패턴 문제
            elif any(keyword in notes_lower for keyword in ["정규식", "패턴", "regex", "pattern"]):
                analysis_result["notes_by_category"]["regex_pattern_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })
            
            # 맥락 부족 문제
            elif any(keyword in notes_lower for keyword in ["맥락", "이전 turn", "이전 turn의", "context", "어려운"]):
                analysis_result["notes_by_category"]["context_lack_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })
            
            # 기타
            else:
                analysis_result["notes_by_category"]["other_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })
        
        # 상세 분석 항목 추가
        detailed_item = {
            "event_id": event_id,
            "turn_index": turn_index,
            "current_type": current_type,
            "correct_type": correct_type,
            "type_mismatch": type_mismatch,
            "summary_quality": summary_quality,
            "summary_completeness": summary_completeness,
            "type_accuracy": type_accuracy,
            "notes": notes,
            "has_notes": bool(notes),
            "is_problematic": type_mismatch or low_quality or (type_accuracy is not None and type_accuracy <= 3)
        }
        analysis_result["detailed_analysis"].append(detailed_item)
    
    # 4. 통계 계산
    analysis_result["statistics"] = {
        "total_samples": len(samples),
        "samples_with_notes": analysis_result["metadata"]["samples_with_notes"],
        "samples_with_type_mismatch": analysis_result["metadata"]["samples_with_type_mismatch"],
        "samples_with_low_quality": analysis_result["metadata"]["samples_with_low_quality"],
        "samples_with_low_accuracy": len(analysis_result["problem_patterns"]["low_accuracy_samples"]),
        "notes_category_counts": {
            "type_classification_errors": len(analysis_result["notes_by_category"]["type_classification_errors"]),
            "summary_quality_issues": len(analysis_result["notes_by_category"]["summary_quality_issues"]),
            "llm_prompt_issues": len(analysis_result["notes_by_category"]["llm_prompt_issues"]),
            "regex_pattern_issues": len(analysis_result["notes_by_category"]["regex_pattern_issues"]),
            "context_lack_issues": len(analysis_result["notes_by_category"]["context_lack_issues"]),
            "type_definition_issues": len(analysis_result["notes_by_category"]["type_definition_issues"]),
            "other_issues": len(analysis_result["notes_by_category"]["other_issues"]),
        },
        "type_mismatch_counts": {
            mismatch: len(samples) 
            for mismatch, samples in analysis_result["problem_patterns"]["type_mismatches"].items()
        }
    }
    
    return analysis_result


def print_analysis_summary(analysis_result: Dict[str, Any]):
    """분석 결과 요약 출력"""
    print("\n" + "=" * 70)
    print("Manual Review Notes Analysis Report (Qualitative)")
    print("=" * 70)
    
    metadata = analysis_result.get("metadata", {})
    stats = analysis_result.get("statistics", {})
    
    print(f"\n[Metadata]")
    print(f"  Total samples: {metadata.get('total_samples', 0)}")
    print(f"  Samples with notes: {stats.get('samples_with_notes', 0)}")
    print(f"  Samples with type mismatch: {stats.get('samples_with_type_mismatch', 0)}")
    print(f"  Samples with low quality: {stats.get('samples_with_low_quality', 0)}")
    print(f"  Samples with low accuracy: {stats.get('samples_with_low_accuracy', 0)}")
    
    print(f"\n[Notes Category Counts]")
    category_counts = stats.get("notes_category_counts", {})
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"  {category}: {count}")
    
    print(f"\n[Type Mismatch Patterns]")
    mismatch_counts = stats.get("type_mismatch_counts", {})
    for mismatch, count in sorted(mismatch_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {mismatch}: {count}")
    
    # 주요 문제 샘플 출력
    notes_by_category = analysis_result.get("notes_by_category", {})
    
    # 타입 분류 오류 샘플 (상위 5개)
    type_errors = notes_by_category.get("type_classification_errors", [])
    if type_errors:
        print(f"\n[Type Classification Errors - Sample (Top 5)]")
        for item in type_errors[:5]:
            print(f"  EVT-{item['turn_index']:03d}: {item['current_type']} -> {item['correct_type']}")
            print(f"    Notes: {item['notes'][:100]}...")
    
    # Summary 품질 문제 샘플 (상위 5개)
    summary_issues = notes_by_category.get("summary_quality_issues", [])
    if summary_issues:
        print(f"\n[Summary Quality Issues - Sample (Top 5)]")
        for item in summary_issues[:5]:
            print(f"  EVT-{item['turn_index']:03d}: quality={item.get('summary_quality')}, completeness={item.get('summary_completeness')}")
            print(f"    Notes: {item['notes'][:100]}...")
    
    # 맥락 부족 문제 샘플
    context_issues = notes_by_category.get("context_lack_issues", [])
    if context_issues:
        print(f"\n[Context Lack Issues - Sample (Top 5)]")
        for item in context_issues[:5]:
            print(f"  EVT-{item['turn_index']:03d}")
            print(f"    Notes: {item['notes'][:100]}...")
    
    # 타입 정의 부족 문제 샘플
    type_def_issues = notes_by_category.get("type_definition_issues", [])
    if type_def_issues:
        print(f"\n[Type Definition Issues - Sample]")
        for item in type_def_issues:
            print(f"  EVT-{item['turn_index']:03d}: {item['current_type']} -> {item['correct_type']}")
            print(f"    Notes: {item['notes'][:100]}...")
    
    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="수동 검증 Notes 정성적 분석"
    )
    parser.add_argument(
        "--review-file",
        type=str,
        required=True,
        help="수동 검증 결과 파일 경로 (manual_review_updated.json)"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="출력 리포트 파일 경로 (기본값: tests/reports/manual_review_notes_analysis_YYYYMMDD_HHMMSS.json)"
    )
    
    args = parser.parse_argument()
    
    review_file = Path(args.review_file)
    
    # 파일 존재 확인
    if not review_file.exists():
        print(f"[ERROR] Review file not found: {review_file}")
        return 1
    
    # Notes 분석 실행
    print(f"[INFO] Analyzing notes from: {review_file}")
    analysis_result = analyze_notes(review_file)
    
    # 분석 결과 출력
    print_analysis_summary(analysis_result)
    
    # 리포트 파일 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if args.output_file:
        output_file = Path(args.output_file)
    else:
        reports_dir = Path(__file__).parent.parent / "tests" / "reports"
        reports_dir.mkdir(exist_ok=True)
        output_file = reports_dir / f"manual_review_notes_analysis_{timestamp}.json"
    
    # 분석 결과에 메타데이터 추가
    analysis_report = {
        "analysis_metadata": {
            "timestamp": timestamp,
            "review_file": str(review_file),
        },
        **analysis_result
    }
    
    output_file.write_text(
        json.dumps(analysis_report, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    
    print(f"\n[SUCCESS] Analysis report saved to: {output_file}")
    
    return 0


if __name__ == "__main__":
    import argparse
    exit(main())

```

스크립트 오타 수정 중입니다.


```python
"""
수동 검증 Notes 정성적 분석 스크립트

Phase 3.4 2단계: 정성적 분석 - Notes 내용 확인
- manual_review_updated.json의 모든 샘플(67개) 순회
- 각 샘플의 notes 필드 내용 확인
- 문제 패턴 분류
- Notes 분석 결과 리포트 생성 및 저장
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Any


def analyze_notes(review_file: Path) -> Dict[str, Any]:
    """
    Notes 내용을 분석하여 문제 패턴 분류
    
    Args:
        review_file: 수동 검증 결과 파일 경로
    
    Returns:
        분석 결과 딕셔너리
    """
    # 1. 수동 검증 결과 로드
    with open(review_file, "r", encoding="utf-8") as f:
        review_data = json.load(f)
    
    samples = review_data.get("samples", [])
    if len(samples) == 0:
        return {"error": "No samples found in review file"}
    
    # 2. 분석 결과 저장
    analysis_result = {
        "metadata": {
            "review_file": str(review_file),
            "total_samples": len(samples),
            "samples_with_notes": 0,
            "samples_with_type_mismatch": 0,
            "samples_with_low_quality": 0,
        },
        "notes_by_category": {
            "type_classification_errors": [],
            "summary_quality_issues": [],
            "llm_prompt_issues": [],
            "regex_pattern_issues": [],
            "context_lack_issues": [],
            "type_definition_issues": [],
            "other_issues": [],
        },
        "problem_patterns": {
            "type_mismatches": defaultdict(list),  # predicted -> actual: [samples]
            "low_quality_samples": [],  # summary_quality <= 3 or summary_completeness <= 3
            "low_accuracy_samples": [],  # type_accuracy <= 3
        },
        "detailed_analysis": []
    }
    
    # 3. 각 샘플 분석
    for sample in samples:
        event_id = sample.get("event_id", "UNKNOWN")
        turn_index = sample.get("turn_index", -1)
        current_event = sample.get("current_event", {})
        manual_review = sample.get("manual_review", {})
        
        current_type = current_event.get("type")
        correct_type = manual_review.get("correct_type")
        notes = manual_review.get("notes", "").strip()
        summary_quality = manual_review.get("summary_quality")
        summary_completeness = manual_review.get("summary_completeness")
        type_accuracy = manual_review.get("type_accuracy")
        
        # Notes가 있는 샘플
        if notes:
            analysis_result["metadata"]["samples_with_notes"] += 1
        
        # 타입 불일치 샘플
        type_mismatch = False
        if correct_type is not None and current_type != correct_type:
            type_mismatch = True
            analysis_result["metadata"]["samples_with_type_mismatch"] += 1
            analysis_result["problem_patterns"]["type_mismatches"][f"{current_type} -> {correct_type}"].append({
                "event_id": event_id,
                "turn_index": turn_index,
                "notes": notes
            })
        
        # 낮은 품질 샘플
        low_quality = False
        if (summary_quality is not None and summary_quality <= 3) or \
           (summary_completeness is not None and summary_completeness <= 3):
            low_quality = True
            analysis_result["metadata"]["samples_with_low_quality"] += 1
            analysis_result["problem_patterns"]["low_quality_samples"].append({
                "event_id": event_id,
                "turn_index": turn_index,
                "summary_quality": summary_quality,
                "summary_completeness": summary_completeness,
                "notes": notes
            })
        
        # 낮은 정확도 샘플
        if type_accuracy is not None and type_accuracy <= 3:
            analysis_result["problem_patterns"]["low_accuracy_samples"].append({
                "event_id": event_id,
                "turn_index": turn_index,
                "type_accuracy": type_accuracy,
                "notes": notes
            })
        
        # Notes 내용 분석 및 분류
        if notes:
            notes_lower = notes.lower()
            
            # 타입 분류 오류
            if any(keyword in notes_lower for keyword in ["타입 문제", "타입", "분류", "type"]):
                if "새로운 type 정의 필요" in notes or "type 정의" in notes:
                    analysis_result["notes_by_category"]["type_definition_issues"].append({
                        "event_id": event_id,
                        "turn_index": turn_index,
                        "current_type": current_type,
                        "correct_type": correct_type,
                        "notes": notes
                    })
                else:
                    analysis_result["notes_by_category"]["type_classification_errors"].append({
                        "event_id": event_id,
                        "turn_index": turn_index,
                        "current_type": current_type,
                        "correct_type": correct_type,
                        "notes": notes
                    })
            
            # Summary 품질 문제
            elif any(keyword in notes_lower for keyword in ["요약 문제", "요약", "summary"]):
                analysis_result["notes_by_category"]["summary_quality_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "summary_quality": summary_quality,
                    "summary_completeness": summary_completeness,
                    "notes": notes
                })
            
            # LLM 프롬프트 문제
            elif any(keyword in notes_lower for keyword in ["llm", "프롬프트", "prompt", "이해"]):
                analysis_result["notes_by_category"]["llm_prompt_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })
            
            # 정규식 패턴 문제
            elif any(keyword in notes_lower for keyword in ["정규식", "패턴", "regex", "pattern"]):
                analysis_result["notes_by_category"]["regex_pattern_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })
            
            # 맥락 부족 문제
            elif any(keyword in notes_lower for keyword in ["맥락", "이전 turn", "이전 turn의", "context", "어려운"]):
                analysis_result["notes_by_category"]["context_lack_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })
            
            # 기타
            else:
                analysis_result["notes_by_category"]["other_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })
        
        # 상세 분석 항목 추가
        detailed_item = {
            "event_id": event_id,
            "turn_index": turn_index,
            "current_type": current_type,
            "correct_type": correct_type,
            "type_mismatch": type_mismatch,
            "summary_quality": summary_quality,
            "summary_completeness": summary_completeness,
            "type_accuracy": type_accuracy,
            "notes": notes,
            "has_notes": bool(notes),
            "is_problematic": type_mismatch or low_quality or (type_accuracy is not None and type_accuracy <= 3)
        }
        analysis_result["detailed_analysis"].append(detailed_item)
    
    # 4. 통계 계산
    analysis_result["statistics"] = {
        "total_samples": len(samples),
        "samples_with_notes": analysis_result["metadata"]["samples_with_notes"],
        "samples_with_type_mismatch": analysis_result["metadata"]["samples_with_type_mismatch"],
        "samples_with_low_quality": analysis_result["metadata"]["samples_with_low_quality"],
        "samples_with_low_accuracy": len(analysis_result["problem_patterns"]["low_accuracy_samples"]),
        "notes_category_counts": {
            "type_classification_errors": len(analysis_result["notes_by_category"]["type_classification_errors"]),
            "summary_quality_issues": len(analysis_result["notes_by_category"]["summary_quality_issues"]),
            "llm_prompt_issues": len(analysis_result["notes_by_category"]["llm_prompt_issues"]),
            "regex_pattern_issues": len(analysis_result["notes_by_category"]["regex_pattern_issues"]),
            "context_lack_issues": len(analysis_result["notes_by_category"]["context_lack_issues"]),
            "type_definition_issues": len(analysis_result["notes_by_category"]["type_definition_issues"]),
            "other_issues": len(analysis_result["notes_by_category"]["other_issues"]),
        },
        "type_mismatch_counts": {
            mismatch: len(samples) 
            for mismatch, samples in analysis_result["problem_patterns"]["type_mismatches"].items()
        }
    }
    
    return analysis_result


def print_analysis_summary(analysis_result: Dict[str, Any]):
    """분석 결과 요약 출력"""
    print("\n" + "=" * 70)
    print("Manual Review Notes Analysis Report (Qualitative)")
    print("=" * 70)
    
    metadata = analysis_result.get("metadata", {})
    stats = analysis_result.get("statistics", {})
    
    print(f"\n[Metadata]")
    print(f"  Total samples: {metadata.get('total_samples', 0)}")
    print(f"  Samples with notes: {stats.get('samples_with_notes', 0)}")
    print(f"  Samples with type mismatch: {stats.get('samples_with_type_mismatch', 0)}")
    print(f"  Samples with low quality: {stats.get('samples_with_low_quality', 0)}")
    print(f"  Samples with low accuracy: {stats.get('samples_with_low_accuracy', 0)}")
    
    print(f"\n[Notes Category Counts]")
    category_counts = stats.get("notes_category_counts", {})
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"  {category}: {count}")
    
    print(f"\n[Type Mismatch Patterns]")
    mismatch_counts = stats.get("type_mismatch_counts", {})
    for mismatch, count in sorted(mismatch_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {mismatch}: {count}")
    
    # 주요 문제 샘플 출력
    notes_by_category = analysis_result.get("notes_by_category", {})
    
    # 타입 분류 오류 샘플 (상위 5개)
    type_errors = notes_by_category.get("type_classification_errors", [])
    if type_errors:
        print(f"\n[Type Classification Errors - Sample (Top 5)]")
        for item in type_errors[:5]:
            print(f"  EVT-{item['turn_index']:03d}: {item['current_type']} -> {item['correct_type']}")
            print(f"    Notes: {item['notes'][:100]}...")
    
    # Summary 품질 문제 샘플 (상위 5개)
    summary_issues = notes_by_category.get("summary_quality_issues", [])
    if summary_issues:
        print(f"\n[Summary Quality Issues - Sample (Top 5)]")
        for item in summary_issues[:5]:
            print(f"  EVT-{item['turn_index']:03d}: quality={item.get('summary_quality')}, completeness={item.get('summary_completeness')}")
            print(f"    Notes: {item['notes'][:100]}...")
    
    # 맥락 부족 문제 샘플
    context_issues = notes_by_category.get("context_lack_issues", [])
    if context_issues:
        print(f"\n[Context Lack Issues - Sample (Top 5)]")
        for item in context_issues[:5]:
            print(f"  EVT-{item['turn_index']:03d}")
            print(f"    Notes: {item['notes'][:100]}...")
    
    # 타입 정의 부족 문제 샘플
    type_def_issues = notes_by_category.get("type_definition_issues", [])
    if type_def_issues:
        print(f"\n[Type Definition Issues - Sample]")
        for item in type_def_issues:
            print(f"  EVT-{item['turn_index']:03d}: {item['current_type']} -> {item['correct_type']}")
            print(f"    Notes: {item['notes'][:100]}...")
    
    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="수동 검증 Notes 정성적 분석"
    )
    parser.add_argument(
        "--review-file",
        type=str,
        required=True,
        help="수동 검증 결과 파일 경로 (manual_review_updated.json)"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="출력 리포트 파일 경로 (기본값: tests/reports/manual_review_notes_analysis_YYYYMMDD_HHMMSS.json)"
    )
    
    args = parser.parse_args()
    
    review_file = Path(args.review_file)
    
    # 파일 존재 확인
    if not review_file.exists():
        print(f"[ERROR] Review file not found: {review_file}")
        return 1
    
    # Notes 분석 실행
    print(f"[INFO] Analyzing notes from: {review_file}")
    analysis_result = analyze_notes(review_file)
    
    # 분석 결과 출력
    print_analysis_summary(analysis_result)
    
    # 리포트 파일 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if args.output_file:
        output_file = Path(args.output_file)
    else:
        reports_dir = Path(__file__).parent.parent / "tests" / "reports"
        reports_dir.mkdir(exist_ok=True)
        output_file = reports_dir / f"manual_review_notes_analysis_{timestamp}.json"
    
    # 분석 결과에 메타데이터 추가
    analysis_report = {
        "analysis_metadata": {
            "timestamp": timestamp,
            "review_file": str(review_file),
        },
        **analysis_result
    }
    
    output_file.write_text(
        json.dumps(analysis_report, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    
    print(f"\n[SUCCESS] Analysis report saved to: {output_file}")
    
    return 0


if __name__ == "__main__":
    import argparse
    exit(main())


```

2단계 정성적 분석 완료. 리포트 파일을 확인해 상세 내용을 파악합니다.


2단계 정성적 분석 완료. 주요 발견:

- Notes가 있는 샘플: 34개
- 타입 불일치: 25개
- 낮은 품질: 30개
- 낮은 정확도: 27개

Notes 카테고리:
- 타입 분류 오류: 25개
- Summary 품질 문제: 4개
- 타입 정의 부족: 3개

주요 문제 패턴:
1. `status_review` → `debug` (10개): 상황 리뷰가 debug 맥락 안에서 이루어지는 경우
2. `plan` → `debug` (4개): 계획이 debug 과정에 포함되는 경우
3. `plan`/`status_review` → `artifact` (4개): 분석을 위해 스크립트를 만드는 경우

3단계: 문제 원인 분석 및 개선 방안 도출로 진행합니다. 분석 리포트를 작성합니다.


```python
"""
문제 원인 분석 및 개선 방안 도출 스크립트

Phase 3.4 3단계: 문제 원인 분석 및 개선 방안 도출
- 정량적 평가 결과와 정성적 분석 결과를 종합
- 타입 분류 오류 및 Summary 품질 문제의 원인 도출
- 개선 방안 제시 및 우선순위화
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any


def analyze_root_causes(
    evaluation_file: Path,
    notes_analysis_file: Path
) -> Dict[str, Any]:
    """
    정량적 평가와 정성적 분석 결과를 종합하여 원인 분석 및 개선 방안 도출
    
    Args:
        evaluation_file: 정량적 평가 결과 파일
        notes_analysis_file: 정성적 분석 결과 파일
    
    Returns:
        원인 분석 및 개선 방안 딕셔너리
    """
    # 1. 정량적 평가 결과 로드
    with open(evaluation_file, "r", encoding="utf-8") as f:
        evaluation = json.load(f)
    
    # 2. 정성적 분석 결과 로드
    with open(notes_analysis_file, "r", encoding="utf-8") as f:
        notes_analysis = json.load(f)
    
    # 3. 원인 분석
    root_cause_analysis = {
        "type_classification_issues": {
            "primary_causes": [],
            "secondary_causes": [],
            "improvement_plans": []
        },
        "summary_quality_issues": {
            "primary_causes": [],
            "secondary_causes": [],
            "improvement_plans": []
        },
        "overall_recommendations": []
    }
    
    # 4. 타입 분류 문제 원인 분석
    confusion_matrix = evaluation.get("type_classification", {}).get("confusion_matrix", {})
    type_accuracy = evaluation.get("type_classification", {}).get("accuracy", 0.0)
    
    # 주요 혼동 패턴 분석
    major_confusions = []
    for predicted, actuals in confusion_matrix.items():
        for actual, count in actuals.items():
            if predicted != actual and count >= 2:  # 2개 이상인 경우만
                major_confusions.append({
                    "predicted": predicted,
                    "actual": actual,
                    "count": count
                })
    
    major_confusions.sort(key=lambda x: x["count"], reverse=True)
    
    # Notes 분석 결과에서 타입 분류 오류 패턴 추출
    type_errors = notes_analysis.get("notes_by_category", {}).get("type_classification_errors", [])
    
    # 원인 1: 맥락 부족 문제 (가장 많은 오류)
    status_review_to_debug = [e for e in type_errors if e["current_type"] == "status_review" and e["correct_type"] == "debug"]
    if status_review_to_debug:
        root_cause_analysis["type_classification_issues"]["primary_causes"].append({
            "cause": "맥락 부족 문제",
            "description": "status_review가 debug 맥락 안에서 이루어지는 경우를 구분하지 못함",
            "evidence": {
                "count": len(status_review_to_debug),
                "examples": [e["notes"][:200] for e in status_review_to_debug[:3]]
            },
            "improvement_plan": {
                "priority": "HIGH",
                "actions": [
                    "LLM 프롬프트에 이전 Turn의 맥락 정보 제공",
                    "debug 맥락 감지 로직 추가 (슬라이딩 윈도우로 최근 3-5 Turn 확인)",
                    "타입 분류 시 맥락 점수 가중치 적용"
                ]
            }
        })
    
    # 원인 2: 타입 정의 부족
    type_def_issues = notes_analysis.get("notes_by_category", {}).get("type_definition_issues", [])
    if type_def_issues:
        root_cause_analysis["type_classification_issues"]["primary_causes"].append({
            "cause": "타입 정의 부족",
            "description": "사용자 확인 요청 등 새로운 타입이 필요함",
            "evidence": {
                "count": len(type_def_issues),
                "examples": [e["notes"][:200] for e in type_def_issues]
            },
            "improvement_plan": {
                "priority": "MEDIUM",
                "actions": [
                    "새로운 타입 정의 검토 (예: 'request_to_user', 'confirmation_needed')",
                    "기존 타입 정의 명확화 (status_review vs debug vs plan 구분 기준)",
                    "타입 정의 문서화 및 LLM 프롬프트에 반영"
                ]
            }
        })
    
    # 원인 3: artifact 타입 분류 실패
    plan_to_artifact = [e for e in type_errors if e["current_type"] == "plan" and e["correct_type"] == "artifact"]
    status_review_to_artifact = [e for e in type_errors if e["current_type"] == "status_review" and e["correct_type"] == "artifact"]
    if plan_to_artifact or status_review_to_artifact:
        root_cause_analysis["type_classification_issues"]["secondary_causes"].append({
            "cause": "Artifact 타입 분류 실패",
            "description": "스크립트 생성 등 artifact 작업을 plan이나 status_review로 분류",
            "evidence": {
                "count": len(plan_to_artifact) + len(status_review_to_artifact),
                "examples": [e["notes"][:200] for e in (plan_to_artifact + status_review_to_artifact)[:3]]
            },
            "improvement_plan": {
                "priority": "MEDIUM",
                "actions": [
                    "파일 생성/수정 키워드 감지 로직 강화",
                    "LLM 프롬프트에 artifact 타입 정의 명확화",
                    "path_candidates가 있으면 artifact 타입 우선 고려"
                ]
            }
        })
    
    # 원인 4: plan vs debug 구분 실패
    plan_to_debug = [e for e in type_errors if e["current_type"] == "plan" and e["correct_type"] == "debug"]
    if plan_to_debug:
        root_cause_analysis["type_classification_issues"]["secondary_causes"].append({
            "cause": "Plan vs Debug 구분 실패",
            "description": "debug 맥락 안에서의 계획을 plan으로 분류",
            "evidence": {
                "count": len(plan_to_debug),
                "examples": [e["notes"][:200] for e in plan_to_debug[:3]]
            },
            "improvement_plan": {
                "priority": "MEDIUM",
                "actions": [
                    "맥락 기반 타입 분류 로직 추가",
                    "debug 맥락 감지 시 plan 타입 점수 감소",
                    "LLM 프롬프트에 plan vs debug 구분 기준 명확화"
                ]
            }
        })
    
    # 5. Summary 품질 문제 원인 분석
    summary_issues = notes_analysis.get("notes_by_category", {}).get("summary_quality_issues", [])
    avg_summary_quality = evaluation.get("summary_quality", {}).get("average_quality", 0.0)
    
    if summary_issues or avg_summary_quality < 4.0:
        root_cause_analysis["summary_quality_issues"]["primary_causes"].append({
            "cause": "요약이 Turn의 핵심 내용을 잘 반영하지 못함",
            "description": "요약이 단순 텍스트 자르기만 수행하거나 중요한 정보를 누락",
            "evidence": {
                "average_quality": avg_summary_quality,
                "samples_count": len(summary_issues),
                "examples": [e["notes"][:200] for e in summary_issues[:3]]
            },
            "improvement_plan": {
                "priority": "HIGH",
                "actions": [
                    "LLM 프롬프트에 요약 품질 기준 명확화 (핵심 내용 포함, 구체적 정보 포함)",
                    "요약 생성 시 문장 단위로 자르지 않고 의미 단위로 자르기",
                    "요약 길이 제한을 늘려서 더 많은 정보 포함 (현재 150자 → 200자)"
                ]
            }
        })
    
    # 6. 종합 개선 방안
    root_cause_analysis["overall_recommendations"] = [
        {
            "priority": "HIGH",
            "title": "맥락 기반 타입 분류 개선",
            "description": "이전 Turn의 맥락 정보를 활용하여 타입 분류 정확도 향상",
            "estimated_impact": "타입 분류 정확도 62.69% → 75%+",
            "implementation_steps": [
                "슬라이딩 윈도우로 최근 3-5 Turn의 타입 정보 수집",
                "LLM 프롬프트에 맥락 정보 포함",
                "맥락 점수 가중치 적용"
            ]
        },
        {
            "priority": "HIGH",
            "title": "Summary 품질 개선",
            "description": "LLM 프롬프트 개선 및 요약 생성 로직 개선",
            "estimated_impact": "Summary 품질 3.95 → 4.5+",
            "implementation_steps": [
                "LLM 프롬프트에 요약 품질 기준 명확화",
                "요약 길이 제한 확대 (150자 → 200자)",
                "의미 단위로 요약 생성"
            ]
        },
        {
            "priority": "MEDIUM",
            "title": "타입 정의 명확화",
            "description": "기존 타입 정의 명확화 및 새로운 타입 검토",
            "estimated_impact": "타입 분류 정확도 추가 5-10% 향상",
            "implementation_steps": [
                "타입 정의 문서화",
                "LLM 프롬프트에 타입 정의 명확히 반영",
                "새로운 타입 필요성 검토 (request_to_user 등)"
            ]
        },
        {
            "priority": "MEDIUM",
            "title": "Artifact 타입 분류 강화",
            "description": "파일 생성/수정 작업을 artifact 타입으로 정확히 분류",
            "estimated_impact": "Artifact 타입 분류 정확도 향상",
            "implementation_steps": [
                "파일 생성/수정 키워드 감지 로직 강화",
                "path_candidates가 있으면 artifact 타입 우선 고려",
                "LLM 프롬프트에 artifact 타입 정의 명확화"
            ]
        }
    ]
    
    return root_cause_analysis


def print_root_cause_analysis(analysis: Dict[str, Any]):
    """원인 분석 결과 출력"""
    print("\n" + "=" * 70)
    print("Root Cause Analysis & Improvement Plan")
    print("=" * 70)
    
    # 타입 분류 문제
    type_issues = analysis.get("type_classification_issues", {})
    primary_causes = type_issues.get("primary_causes", [])
    secondary_causes = type_issues.get("secondary_causes", [])
    
    print(f"\n[Type Classification Issues]")
    print(f"\n  Primary Causes ({len(primary_causes)}):")
    for i, cause in enumerate(primary_causes, 1):
        print(f"    {i}. {cause['cause']}")
        print(f"       Description: {cause['description']}")
        print(f"       Evidence: {cause['evidence']['count']} cases")
        print(f"       Priority: {cause['improvement_plan']['priority']}")
        print(f"       Actions:")
        for action in cause['improvement_plan']['actions']:
            print(f"         - {action}")
    
    if secondary_causes:
        print(f"\n  Secondary Causes ({len(secondary_causes)}):")
        for i, cause in enumerate(secondary_causes, 1):
            print(f"    {i}. {cause['cause']}")
            print(f"       Description: {cause['description']}")
            print(f"       Evidence: {cause['evidence']['count']} cases")
            print(f"       Priority: {cause['improvement_plan']['priority']}")
    
    # Summary 품질 문제
    summary_issues = analysis.get("summary_quality_issues", {})
    summary_primary = summary_issues.get("primary_causes", [])
    
    if summary_primary:
        print(f"\n[Summary Quality Issues]")
        for i, cause in enumerate(summary_primary, 1):
            print(f"    {i}. {cause['cause']}")
            print(f"       Description: {cause['description']}")
            print(f"       Evidence: avg_quality={cause['evidence'].get('average_quality', 0):.2f}, samples={cause['evidence'].get('samples_count', 0)}")
            print(f"       Priority: {cause['improvement_plan']['priority']}")
            print(f"       Actions:")
            for action in cause['improvement_plan']['actions']:
                print(f"         - {action}")
    
    # 종합 개선 방안
    recommendations = analysis.get("overall_recommendations", [])
    print(f"\n[Overall Recommendations]")
    for i, rec in enumerate(recommendations, 1):
        print(f"    {i}. [{rec['priority']}] {rec['title']}")
        print(f"       Description: {rec['description']}")
        print(f"       Estimated Impact: {rec['estimated_impact']}")
        print(f"       Implementation Steps:")
        for step in rec['implementation_steps']:
            print(f"         - {step}")
    
    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="문제 원인 분석 및 개선 방안 도출"
    )
    parser.add_argument(
        "--evaluation-file",
        type=str,
        required=True,
        help="정량적 평가 결과 파일 경로"
    )
    parser.add_argument(
        "--notes-analysis-file",
        type=str,
        required=True,
        help="정성적 분석 결과 파일 경로"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="출력 리포트 파일 경로"
    )
    
    args = parser.parse_args()
    
    evaluation_file = Path(args.evaluation_file)
    notes_analysis_file = Path(args.notes_analysis_file)
    
    # 파일 존재 확인
    if not evaluation_file.exists():
        print(f"[ERROR] Evaluation file not found: {evaluation_file}")
        return 1
    
    if not notes_analysis_file.exists():
        print(f"[ERROR] Notes analysis file not found: {notes_analysis_file}")
        return 1
    
    # 원인 분석 실행
    print(f"[INFO] Analyzing root causes...")
    analysis = analyze_root_causes(evaluation_file, notes_analysis_file)
    
    # 분석 결과 출력
    print_root_cause_analysis(analysis)
    
    # 리포트 파일 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if args.output_file:
        output_file = Path(args.output_file)
    else:
        reports_dir = Path(__file__).parent.parent / "tests" / "reports"
        reports_dir.mkdir(exist_ok=True)
        output_file = reports_dir / f"root_cause_analysis_{timestamp}.json"
    
    analysis_report = {
        "analysis_metadata": {
            "timestamp": timestamp,
            "evaluation_file": str(evaluation_file),
            "notes_analysis_file": str(notes_analysis_file),
        },
        **analysis
    }
    
    output_file.write_text(
        json.dumps(analysis_report, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    
    print(f"\n[SUCCESS] Root cause analysis report saved to: {output_file}")
    
    return 0


if __name__ == "__main__":
    import argparse
    exit(main())

```

---

**User**

지금까지 진행하고 있는 원인 분석은, 정성적이라고 하지만, 결국 스크립트에 의한 휴리스틱에 의하고 있습니다.
당신이 직접 notes의 내용을 읽고 주요 이슈 및 개선원인을 찾는 작업도 같이 병행해주세요

---

**Cursor**

스크립트 기반 휴리스틱에만 의존하지 않고, notes를 직접 읽어 주요 이슈와 개선 원인을 분석합니다. 타입 불일치와 낮은 품질 샘플의 notes를 중심으로 확인합니다.


notes를 직접 읽어 주요 이슈와 개선 원인을 분석 중입니다. 타입 불일치와 낮은 품질 샘플의 notes를 중심으로 확인합니다.


notes를 직접 읽어 주요 이슈와 개선 원인을 정리 중입니다. 분석 리포트를 작성합니다.


```markdown
# 수동 검증 Notes 직접 분석 리포트

**분석 일시**: 2025-12-24  
**분석 대상**: `tests/manual_review/all_events_html_review_20251223_212658/manual_review_updated.json`  
**총 샘플 수**: 67개  
**Notes가 있는 샘플**: 34개

---

## 1. 주요 문제 패턴 (Notes 직접 분석 결과)

### 1.1 맥락 부족 문제 (가장 빈번한 문제)

**발견 빈도**: 매우 높음 (10개 이상 샘플)

**주요 사례**:
- **EVT-010**: "이전 turn의 사용자의 계획에 따라 Cursor가 실행하는 단계"
- **EVT-013**: "이전 Turn의 맥락이 없어서 어려운 것으로 보임. 이전 Turn에서 커서가, `피드백 기본 생성 로직 추가` 여부를 문의했기에, 이 문장은 '기본 생성 로직 추가'를 진행하라는 지시이자 plan임"
- **EVT-024**: "상황을 리뷰하는 것이기는 하나, 전체적인 맥락이 debug를 하는 과정에서 원인을 분석하면서 상황이 리뷰되고 있어서, debug가 더 정확한듯"
- **EVT-025, 026, 027**: "역시 debug의 맥락속에서 사용자가 수정지시하고 있으므로 debug가 가장 적합"
- **EVT-031**: "이전 turn의 맥락이 없어서 잘못 파악되었으며, 커서가 DB 조회를 쉽게 하기 위한 사용자 정보를 주고 있음"
- **EVT-1634**: "앞의 사용자 turn의 맥락이 파악이 안되었으나, 그에 대한 단순한 답변임"
- **EVT-1825**: "앞 turn의 커서 대화의 맥락이 파악 안된 상태. 계획 그대로 진행하라는 의미임"

**핵심 원인**:
1. **이전 Turn 정보 부재**: LLM이 현재 Turn만 보고 판단하여 맥락을 놓침
2. **Debug 맥락 감지 실패**: 여러 Turn에 걸친 debug 과정을 하나의 Turn으로만 판단
3. **대화 흐름 파악 실패**: 사용자-커서 간 대화의 연속성을 이해하지 못함

**개선 방안**:
- **슬라이딩 윈도우 적용**: 최근 3-5 Turn의 타입 정보를 LLM 프롬프트에 포함
- **맥락 점수 가중치**: 이전 Turn에 debug가 있으면 현재 Turn도 debug 가능성 높음
- **대화 흐름 추적**: User-Cursor 대화의 연속성을 고려한 타입 분류

---

### 1.2 타입 정의 부족 문제

**발견 빈도**: 중간 (3-4개 샘플)

**주요 사례**:
- **EVT-010**: "실행을 표현하는 type형이 없음. 문제가 있는 부분을 debug한 것이기도 하지만, 사용자가 계획한 내용대로 코드를 수정하고 있기 때문에, artifact에 가깝기도 함"
- **EVT-017, 018, 021**: "사용자가 확인해야 할 사항을 제시하는 것으로, 일단 plan으로 표시했으나, 사실 새로운 type 정의 필요 (예를 들면, request to user)"

**핵심 원인**:
1. **실행 단계 타입 부재**: "계획 → 실행" 사이의 단계를 표현할 타입이 없음
2. **사용자 확인 요청 타입 부재**: "사용자가 확인해야 할 사항"을 표현할 타입이 없음
3. **기존 타입으로 무리하게 분류**: 부적절한 타입으로 분류하여 정확도 저하

**개선 방안**:
- **새로운 타입 검토**: 
  - `execution`: 계획을 실행하는 단계 (plan과 artifact 사이)
  - `request_to_user`: 사용자 확인/입력 요청
- **타입 정의 명확화**: 기존 타입의 경계를 명확히 정의
- **하이브리드 타입 고려**: 하나의 Turn이 여러 타입 특성을 가질 수 있음

---

### 1.3 Artifact 타입 분류 실패

**발견 빈도**: 중간 (3-4개 샘플)

**주요 사례**:
- **EVT-028, 030, 032**: "분석을 위해 자체 스크립트를 만들고 있으므로 artifact로 분류되어야 함"
- **EVT-1564**: "실제 코드를 수정하면서, 보완을 하고 있습니다. artifact가 적당합니다."

**핵심 원인**:
1. **스크립트 생성 감지 실패**: "스크립트 작성", "스크립트 생성" 키워드 감지 미흡
2. **코드 수정 감지 실패**: 코드 수정 작업을 plan이나 status_review로 분류
3. **파일 경로 기반 분류 한계**: path_candidates가 없으면 artifact로 분류하지 않음

**개선 방안**:
- **키워드 감지 강화**: "스크립트 작성", "코드 수정", "파일 생성" 등 키워드 추가
- **LLM 프롬프트 개선**: artifact 타입 정의에 "스크립트 생성", "코드 수정" 포함
- **path_candidates 우선 고려**: path_candidates가 있으면 artifact 타입 점수 증가

---

### 1.4 Summary 품질 문제

**발견 빈도**: 중간 (4-5개 샘플)

**주요 사례**:
- **EVT-010**: "로직 추가등의 코드 수정을 위해 관련 파일을 확인한 것임. 정확하게는 `관련 파일을 확인해서, 로직 추가 및 임계값 변경 진행중`"
- **EVT-012**: "다음이 더 정확 `TODOs.md 업데이트와 Git 커밋 완료후, 다음 단계(피드백 기본 생성 로직 추가) 진행 여부 문의`"
- **EVT-013**: "이전 Turn의 맥락이 없어서 어려운 것으로 보임"
- **EVT-014**: "다음이 더 정확. '기본 생성 로직 추가 완료 후, git 커밋 진행합니다`"
- **EVT-031**: "이전 turn의 맥락이 없어서 잘못 파악되었으며"
- **EVT-035, 039**: "@는 첨부 자료 attach 의미하며, 실행중인 서버 이름을 제공하여 커서가 터미널 로그 정보에 접속하게 함"

**핵심 원인**:
1. **맥락 부족**: 이전 Turn 정보 없이 요약 생성
2. **특수 기호 의미 파악 실패**: "@" 기호의 의미를 이해하지 못함
3. **핵심 동작 누락**: "진행중", "완료 후" 등 중요한 상태 정보 누락
4. **문장 단위 자르기**: 의미 단위가 아닌 단순 텍스트 자르기

**개선 방안**:
- **맥락 정보 포함**: 이전 Turn의 핵심 내용을 요약에 반영
- **특수 기호 처리**: "@", "#" 등 특수 기호의 의미를 LLM에 설명
- **상태 정보 강조**: "진행중", "완료", "요청" 등 상태 정보 포함
- **의미 단위 요약**: 문장 단위가 아닌 의미 단위로 요약 생성

---

### 1.5 Plan vs Debug 구분 실패

**발견 빈도**: 높음 (4-5개 샘플)

**주요 사례**:
- **EVT-025, 027**: "이런 경우가 아주 어려운데, 사용자가 수정 지시를 한 내용이니, plan으로 볼수 있지만, 역시 debug의 맥락속에서 사용자가 수정지시하고 있으므로 debug가 가장 적합"
- **EVT-036**: "커서가 자신의 작업 계획을 설명하고 있으나, debug 과정에 포함됨"
- **EVT-037**: "사용자가 지시하므로 plan에 가까우나, debug에 포함됨"
- **EVT-043, 044**: "사용자가 지시하는 plan이기는 하나, debug 과정"

**핵심 원인**:
1. **맥락 기반 판단 부재**: 단일 Turn만 보고 판단하여 debug 맥락을 놓침
2. **Plan과 Debug 경계 모호**: 사용자 지시가 plan인지 debug 과정의 일부인지 구분 어려움
3. **우선순위 로직 부재**: 여러 타입 특성을 가질 때 우선순위 결정 로직 없음

**개선 방안**:
- **맥락 기반 우선순위**: 이전 Turn에 debug가 있으면 현재 Turn도 debug 우선 고려
- **Plan vs Debug 구분 기준 명확화**: 
  - Plan: 새로운 작업 시작, 독립적인 계획
  - Debug: 문제 해결 과정의 일부, 기존 작업의 연속
- **하이브리드 타입 처리**: 하나의 Turn이 여러 타입 특성을 가질 때 맥락 기반으로 우선순위 결정

---

## 2. 종합 원인 분석

### 2.1 근본 원인

1. **맥락 정보 부재** (가장 중요)
   - LLM이 현재 Turn만 보고 판단
   - 이전 Turn의 타입, 내용, 맥락 정보 미제공
   - 대화 흐름 파악 불가

2. **타입 정의 불완전**
   - 실행 단계, 사용자 확인 요청 등 표현할 타입 부재
   - 기존 타입의 경계가 모호함
   - 하이브리드 타입 처리 로직 없음

3. **LLM 프롬프트 한계**
   - 타입 정의가 명확하지 않음
   - 맥락 정보 제공 안 함
   - 특수 기호 의미 설명 없음

4. **Summary 생성 로직 한계**
   - 단순 텍스트 자르기
   - 맥락 정보 미반영
   - 상태 정보 누락

### 2.2 개선 우선순위

**HIGH (즉시 개선 필요)**:
1. **맥락 기반 타입 분류**: 슬라이딩 윈도우로 이전 Turn 정보 제공
2. **Summary 품질 개선**: 맥락 정보 포함, 의미 단위 요약

**MEDIUM (단기 개선)**:
3. **타입 정의 명확화**: 기존 타입 경계 명확화, 새로운 타입 검토
4. **Artifact 타입 분류 강화**: 키워드 감지, path_candidates 우선 고려
5. **Plan vs Debug 구분 개선**: 맥락 기반 우선순위 로직

**LOW (장기 개선)**:
6. **하이브리드 타입 처리**: 하나의 Turn이 여러 타입 특성을 가질 때 처리
7. **특수 기호 처리**: "@", "#" 등 특수 기호 의미 파악

---

## 3. 구체적 개선 방안

### 3.1 맥락 기반 타입 분류 구현

**구현 방법**:
```python
# 슬라이딩 윈도우로 최근 3-5 Turn 정보 수집
recent_turns = turns[max(0, turn_index-4):turn_index+1]
context_info = {
    "recent_types": [t.type for t in recent_turns],
    "recent_summaries": [t.summary[:100] for t in recent_turns],
    "is_debug_context": any(t.type == "debug" for t in recent_turns[:-1])
}

# LLM 프롬프트에 맥락 정보 포함
prompt = f"""
이전 Turn 맥락:
- 최근 타입: {context_info['recent_types']}
- Debug 맥락 여부: {context_info['is_debug_context']}
- 최근 요약: {context_info['recent_summaries']}

현재 Turn: {turn.body}
"""
```

**예상 효과**: 타입 분류 정확도 62.69% → 75%+

---

### 3.2 Summary 품질 개선

**구현 방법**:
1. **맥락 정보 포함**: 이전 Turn의 핵심 내용을 요약에 반영
2. **의미 단위 요약**: 문장 단위가 아닌 의미 단위로 자르기
3. **상태 정보 강조**: "진행중", "완료", "요청" 등 상태 정보 포함
4. **특수 기호 처리**: "@"는 "첨부 자료", "#"는 "파일/항목 참조"로 설명

**LLM 프롬프트 개선**:
```
요약 생성 시 다음을 포함하세요:
1. 핵심 동작 (무엇을 하는가)
2. 상태 정보 (진행중/완료/요청 등)
3. 중요한 세부사항 (파일명, 수치, 변경사항 등)
4. 이전 Turn과의 연관성 (있는 경우)

특수 기호 의미:
- @: 첨부 자료 또는 참조 대상
- #: 파일명, 항목 번호 등
```

**예상 효과**: Summary 품질 3.95 → 4.5+

---

### 3.3 타입 정의 명확화

**기존 타입 경계 명확화**:
- **status_review**: 독립적인 상태 점검 (맥락과 무관)
- **debug**: 문제 해결 과정 (이전 Turn에 debug가 있으면 우선 고려)
- **plan**: 새로운 작업 시작 (독립적인 계획)
- **artifact**: 파일 생성/수정/실행 (스크립트 생성 포함)

**새로운 타입 검토**:
- **execution**: plan을 실행하는 단계 (선택적, plan과 artifact 사이)
- **request_to_user**: 사용자 확인/입력 요청 (선택적)

---

## 4. 다음 단계

1. **맥락 기반 타입 분류 구현** (최우선)
2. **Summary 품질 개선** (최우선)
3. **타입 정의 명확화 및 LLM 프롬프트 개선**
4. **Artifact 타입 분류 강화**
5. **E2E 재평가 및 개선 효과 검증**

```

Notes 직접 분석 완료. 주요 발견:

- 맥락 부족 문제(가장 빈번): "debug의 맥락속에서", "이전 turn의 맥락이 없어서" 등이 반복됨
- 타입 정의 부족: "실행을 표현하는 type형이 없음", "새로운 type 정의 필요 (request to user)"
- Artifact 타입 분류 실패: "분석을 위해 자체 스크립트를 만들고 있으므로 artifact로 분류되어야 함"
- Summary 품질 문제: "이전 Turn의 맥락이 없어서", "@는 첨부 자료 attach 의미" 등
- Plan vs Debug 구분 실패: "debug의 맥락속에서 사용자가 수정지시하고 있으므로 debug가 가장 적합"

분석 리포트를 `tests/reports/manual_review_direct_analysis.md`에 저장했습니다.

3단계 원인 분석 스크립트를 실행해 정량적 평가와 정성적 분석 결과를 종합하겠습니다.


3단계 원인 분석 완료. 직접 분석과 스크립트 기반 분석을 종합해 최종 리포트를 작성합니다.


```markdown
# Phase 3.4 종합 분석 리포트

**분석 일시**: 2025-12-24  
**분석 방법**: 정량적 평가 + 정성적 분석 (스크립트 기반 + 직접 분석)

---

## 1. 정량적 평가 결과 요약

### 1.1 타입 분류 정확도
- **전체 정확도**: 62.69% (42/67)
- **LLM 기반**: 62.69% (42/67)
- **목표 정확도**: 85%+

### 1.2 Summary 품질
- **평균 품질**: 3.95 / 5.0 (66개 샘플)
- **평균 완전성**: 4.03 / 5.0 (66개 샘플)
- **목표 품질**: 4.5+ / 5.0

### 1.3 주요 혼동 패턴
1. `status_review` → `debug`: 10개 (가장 많은 오류)
2. `plan` → `debug`: 4개
3. `turn` → `debug`: 3개
4. `plan` → `artifact`: 2개
5. `status_review` → `artifact`: 2개

---

## 2. 정성적 분석 결과 (Notes 직접 분석)

### 2.1 맥락 부족 문제 (가장 빈번)

**발견 빈도**: 매우 높음 (10개 이상 샘플)

**주요 사례**:
- **EVT-010**: "이전 turn의 사용자의 계획에 따라 Cursor가 실행하는 단계"
- **EVT-013**: "이전 Turn의 맥락이 없어서 어려운 것으로 보임. 이전 Turn에서 커서가, `피드백 기본 생성 로직 추가` 여부를 문의했기에, 이 문장은 '기본 생성 로직 추가'를 진행하라는 지시이자 plan임"
- **EVT-024**: "상황을 리뷰하는 것이기는 하나, 전체적인 맥락이 debug를 하는 과정에서 원인을 분석하면서 상황이 리뷰되고 있어서, debug가 더 정확한듯"
- **EVT-025, 026, 027**: "역시 debug의 맥락속에서 사용자가 수정지시하고 있으므로 debug가 가장 적합"
- **EVT-031**: "이전 turn의 맥락이 없어서 잘못 파악되었으며, 커서가 DB 조회를 쉽게 하기 위한 사용자 정보를 주고 있음"

**핵심 원인**:
1. **이전 Turn 정보 부재**: LLM이 현재 Turn만 보고 판단
2. **Debug 맥락 감지 실패**: 여러 Turn에 걸친 debug 과정을 하나의 Turn으로만 판단
3. **대화 흐름 파악 실패**: 사용자-커서 간 대화의 연속성을 이해하지 못함

### 2.2 타입 정의 부족 문제

**발견 빈도**: 중간 (3-4개 샘플)

**주요 사례**:
- **EVT-010**: "실행을 표현하는 type형이 없음. 문제가 있는 부분을 debug한 것이기도 하지만, 사용자가 계획한 내용대로 코드를 수정하고 있기 때문에, artifact에 가깝기도 함"
- **EVT-017, 018, 021**: "사용자가 확인해야 할 사항을 제시하는 것으로, 일단 plan으로 표시했으나, 사실 새로운 type 정의 필요 (예를 들면, request to user)"

**핵심 원인**:
1. **실행 단계 타입 부재**: "계획 → 실행" 사이의 단계를 표현할 타입이 없음
2. **사용자 확인 요청 타입 부재**: "사용자가 확인해야 할 사항"을 표현할 타입이 없음

### 2.3 Artifact 타입 분류 실패

**발견 빈도**: 중간 (3-4개 샘플)

**주요 사례**:
- **EVT-028, 030, 032**: "분석을 위해 자체 스크립트를 만들고 있으므로 artifact로 분류되어야 함"

**핵심 원인**:
1. **스크립트 생성 감지 실패**: "스크립트 작성", "스크립트 생성" 키워드 감지 미흡
2. **파일 경로 기반 분류 한계**: path_candidates가 없으면 artifact로 분류하지 않음

### 2.4 Summary 품질 문제

**발견 빈도**: 중간 (4-5개 샘플)

**주요 사례**:
- **EVT-010**: "로직 추가등의 코드 수정을 위해 관련 파일을 확인한 것임. 정확하게는 `관련 파일을 확인해서, 로직 추가 및 임계값 변경 진행중`"
- **EVT-012**: "다음이 더 정확 `TODOs.md 업데이트와 Git 커밋 완료후, 다음 단계(피드백 기본 생성 로직 추가) 진행 여부 문의`"
- **EVT-013**: "이전 Turn의 맥락이 없어서 어려운 것으로 보임"
- **EVT-035, 039**: "@는 첨부 자료 attach 의미하며, 실행중인 서버 이름을 제공하여 커서가 터미널 로그 정보에 접속하게 함"

**핵심 원인**:
1. **맥락 부족**: 이전 Turn 정보 없이 요약 생성
2. **특수 기호 의미 파악 실패**: "@" 기호의 의미를 이해하지 못함
3. **핵심 동작 누락**: "진행중", "완료 후" 등 중요한 상태 정보 누락

---

## 3. 종합 원인 분석

### 3.1 근본 원인 (우선순위 순)

#### 1. 맥락 정보 부재 (최우선)
- **문제**: LLM이 현재 Turn만 보고 판단하여 이전 Turn의 맥락을 놓침
- **영향**: 타입 분류 정확도 62.69%의 주요 원인
- **증거**: 10개 이상 샘플에서 "debug의 맥락속에서", "이전 turn의 맥락이 없어서" 반복

#### 2. Summary 생성 로직 한계
- **문제**: 단순 텍스트 자르기, 맥락 정보 미반영, 상태 정보 누락
- **영향**: Summary 품질 3.95 / 5.0
- **증거**: "이전 Turn의 맥락이 없어서", "다음이 더 정확" 등 반복

#### 3. 타입 정의 불완전
- **문제**: 실행 단계, 사용자 확인 요청 등 표현할 타입 부재
- **영향**: 부적절한 타입으로 분류하여 정확도 저하
- **증거**: "실행을 표현하는 type형이 없음", "새로운 type 정의 필요"

#### 4. LLM 프롬프트 한계
- **문제**: 타입 정의가 명확하지 않음, 맥락 정보 제공 안 함, 특수 기호 의미 설명 없음
- **영향**: LLM이 올바르게 판단하지 못함

---

## 4. 개선 방안 (우선순위별)

### 4.1 HIGH 우선순위 (즉시 개선)

#### 1. 맥락 기반 타입 분류 구현
**목표**: 타입 분류 정확도 62.69% → 75%+

**구현 방법**:
- 슬라이딩 윈도우로 최근 3-5 Turn의 타입 정보 수집
- LLM 프롬프트에 맥락 정보 포함:
  - 최근 Turn들의 타입
  - Debug 맥락 여부 (이전 Turn에 debug가 있는지)
  - 최근 요약 요약
- 맥락 점수 가중치 적용:
  - 이전 Turn에 debug가 있으면 현재 Turn도 debug 가능성 높음
  - 이전 Turn에 plan이 있고 현재 Turn이 실행 단계면 artifact 가능성 높음

**예상 효과**: 
- `status_review` → `debug` 오류 10개 → 2-3개로 감소
- `plan` → `debug` 오류 4개 → 1-2개로 감소
- 전체 정확도 62.69% → 75%+

#### 2. Summary 품질 개선
**목표**: Summary 품질 3.95 → 4.5+

**구현 방법**:
- 맥락 정보 포함: 이전 Turn의 핵심 내용을 요약에 반영
- 의미 단위 요약: 문장 단위가 아닌 의미 단위로 자르기
- 상태 정보 강조: "진행중", "완료", "요청" 등 상태 정보 포함
- 특수 기호 처리: "@"는 "첨부 자료", "#"는 "파일/항목 참조"로 설명
- 요약 길이 제한 확대: 150자 → 200자

**LLM 프롬프트 개선**:
```
요약 생성 시 다음을 포함하세요:
1. 핵심 동작 (무엇을 하는가)
2. 상태 정보 (진행중/완료/요청 등)
3. 중요한 세부사항 (파일명, 수치, 변경사항 등)
4. 이전 Turn과의 연관성 (있는 경우)

특수 기호 의미:
- @: 첨부 자료 또는 참조 대상
- #: 파일명, 항목 번호 등
```

**예상 효과**: Summary 품질 3.95 → 4.5+

### 4.2 MEDIUM 우선순위 (단기 개선)

#### 3. 타입 정의 명확화
**목표**: 타입 분류 정확도 추가 5-10% 향상

**구현 방법**:
- 기존 타입 경계 명확화:
  - **status_review**: 독립적인 상태 점검 (맥락과 무관)
  - **debug**: 문제 해결 과정 (이전 Turn에 debug가 있으면 우선 고려)
  - **plan**: 새로운 작업 시작 (독립적인 계획)
  - **artifact**: 파일 생성/수정/실행 (스크립트 생성 포함)
- 새로운 타입 검토:
  - **execution**: plan을 실행하는 단계 (선택적)
  - **request_to_user**: 사용자 확인/입력 요청 (선택적)
- LLM 프롬프트에 타입 정의 명확히 반영

#### 4. Artifact 타입 분류 강화
**목표**: Artifact 타입 분류 정확도 향상

**구현 방법**:
- 키워드 감지 강화: "스크립트 작성", "코드 수정", "파일 생성" 등 키워드 추가
- path_candidates 우선 고려: path_candidates가 있으면 artifact 타입 점수 증가
- LLM 프롬프트에 artifact 타입 정의 명확화: "스크립트 생성", "코드 수정" 포함

#### 5. Plan vs Debug 구분 개선
**목표**: Plan과 Debug 구분 정확도 향상

**구현 방법**:
- 맥락 기반 우선순위: 이전 Turn에 debug가 있으면 현재 Turn도 debug 우선 고려
- Plan vs Debug 구분 기준 명확화:
  - Plan: 새로운 작업 시작, 독립적인 계획
  - Debug: 문제 해결 과정의 일부, 기존 작업의 연속

---

## 5. 구현 계획

### Phase 1: 맥락 기반 타입 분류 구현 (1-2일)
1. 슬라이딩 윈도우 로직 구현
2. LLM 프롬프트에 맥락 정보 추가
3. 맥락 점수 가중치 로직 구현
4. E2E 테스트 및 검증

### Phase 2: Summary 품질 개선 (1일)
1. LLM 프롬프트 개선 (맥락 정보, 특수 기호 설명)
2. 요약 길이 제한 확대 (150자 → 200자)
3. 의미 단위 요약 로직 구현
4. E2E 테스트 및 검증

### Phase 3: 타입 정의 명확화 (1일)
1. 기존 타입 경계 명확화 문서 작성
2. LLM 프롬프트에 타입 정의 반영
3. 새로운 타입 필요성 검토
4. E2E 테스트 및 검증

### Phase 4: Artifact 타입 분류 강화 (0.5일)
1. 키워드 감지 로직 강화
2. path_candidates 우선 고려 로직 구현
3. LLM 프롬프트 개선
4. E2E 테스트 및 검증

---

## 6. 예상 개선 효과

### 6.1 타입 분류 정확도
- **현재**: 62.69%
- **목표**: 85%+
- **예상 개선**: 
  - 맥락 기반 분류: +12% (62.69% → 74.69%)
  - 타입 정의 명확화: +5% (74.69% → 79.69%)
  - Artifact 분류 강화: +3% (79.69% → 82.69%)
  - Plan vs Debug 구분: +2% (82.69% → 84.69%)

### 6.2 Summary 품질
- **현재**: 3.95 / 5.0
- **목표**: 4.5+ / 5.0
- **예상 개선**: 
  - 맥락 정보 포함: +0.3 (3.95 → 4.25)
  - 의미 단위 요약: +0.2 (4.25 → 4.45)
  - 특수 기호 처리: +0.1 (4.45 → 4.55)

---

## 7. 다음 단계

1. **사용자 검토 및 승인**: 개선 방안 검토 및 우선순위 조정
2. **Phase 1 구현**: 맥락 기반 타입 분류 구현
3. **Phase 2 구현**: Summary 품질 개선
4. **E2E 재평가**: 수정된 로직으로 E2E 테스트 재실행
5. **결과 피드백**: 개선 전후 비교 및 추가 개선 사항 도출

```

Phase 3.4 분석 완료.

## 완료된 작업

### 1단계: 정량적 평가 실행
- 타입 분류 정확도: 62.69% (42/67)
- Summary 품질: 3.95 / 5.0
- 혼동 행렬 생성 및 분석 완료
- 리포트 저장: `tests/reports/manual_review_evaluation_20251224_182554.json`

### 2단계: 정성적 분석 - Notes 직접 확인
- 67개 샘플 중 34개 notes 확인
- 주요 문제 패턴 5가지 식별:
  1. 맥락 부족 문제 (가장 빈번, 10개 이상)
  2. 타입 정의 부족 (3-4개)
  3. Artifact 타입 분류 실패 (3-4개)
  4. Summary 품질 문제 (4-5개)
  5. Plan vs Debug 구분 실패 (4-5개)
- 직접 분석 리포트 저장: `tests/reports/manual_review_direct_analysis.md`

### 3단계: 문제 원인 분석 및 개선 방안 도출
- 정량적/정성적 분석 종합
- 근본 원인 4가지 식별
- 개선 방안 우선순위화 (HIGH/MEDIUM)
- 종합 분석 리포트 저장: `tests/reports/phase_3_4_comprehensive_analysis.md`

## 주요 발견 사항

### 가장 중요한 문제: 맥락 부족
- 증거: "debug의 맥락속에서", "이전 turn의 맥락이 없어서" 등이 반복
- 영향: 타입 분류 정확도 62.69%의 주요 원인
- 해결: 슬라이딩 윈도우로 이전 Turn 정보 제공

### 개선 우선순위
1. HIGH: 맥락 기반 타입 분류 구현 (정확도 62.69% → 75%+)
2. HIGH: Summary 품질 개선 (3.95 → 4.5+)
3. MEDIUM: 타입 정의 명확화 (추가 5-10% 향상)
4. MEDIUM: Artifact 타입 분류 강화

## 생성된 리포트 파일

1. `tests/reports/manual_review_evaluation_20251224_182554.json` - 정량적 평가 결과
2. `tests/reports/manual_review_notes_analysis_20251224_182712.json` - 정성적 분석 결과 (스크립트 기반)
3. `tests/reports/manual_review_direct_analysis.md` - Notes 직접 분석 리포트
4. `tests/reports/root_cause_analysis_20251224_183215.json` - 원인 분석 결과 (스크립트 기반)
5. `tests/reports/phase_3_4_comprehensive_analysis.md` - 종합 분석 리포트

## 다음 단계

4단계: 개선 방안 검토 및 승인
- 종합 분석 리포트 검토
- 우선순위 조정 (필요 시)
- 구현 계획 승인

진행할까요?

---

**User**

개선 우선순위
HIGH: 맥락 기반 타입 분류 구현 (정확도 62.69% → 75%+)
HIGH: Summary 품질 개선 (3.95 → 4.5+)
MEDIUM: 타입 정의 명확화 (추가 5-10% 향상)
MEDIUM: Artifact 타입 분류 강화

이에 대한 구체적인 개선 방안을 설명하세요
특히 맥락 기반 타입 분류가 매우 중요하니, 상세히 설명

---

**Cursor**

개선 방안을 구체화하기 위해 현재 구현 상태를 확인 중입니다.


현재 구현 상태를 확인했습니다. 개선 방안을 구체적으로 설명합니다.

## 개선 방안 상세 설명

### 1. HIGH: 맥락 기반 타입 분류 구현

#### 현재 문제점
- `classify_and_summarize_with_llm()` 함수가 현재 Turn만 받아 처리
- LLM 프롬프트에 이전 Turn 정보가 없음
- 결과: "debug의 맥락속에서" 상황을 파악하지 못함

#### 개선 방안

**1.1 슬라이딩 윈도우로 맥락 정보 수집**

```python
# backend/builders/event_normalizer.py 수정

def _collect_context_info(
    turns: List[Turn], 
    current_turn_index: int, 
    window_size: int = 5
) -> Dict[str, any]:
    """
    현재 Turn의 맥락 정보 수집 (슬라이딩 윈도우)
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        window_size: 윈도우 크기 (기본값: 5, 최근 5개 Turn 확인)
    
    Returns:
        맥락 정보 딕셔너리
    """
    # 최근 window_size개 Turn 수집 (현재 Turn 제외)
    start_index = max(0, current_turn_index - window_size)
    recent_turns = turns[start_index:current_turn_index]
    
    # 이전 Turn들의 타입 정보 (이미 생성된 Event가 있으면 사용)
    recent_types = []
    recent_summaries = []
    
    for turn in recent_turns:
        # 이미 생성된 Event가 있으면 타입 사용, 없으면 추정
        # (병렬 처리 시에는 아직 생성되지 않았을 수 있음)
        recent_types.append("unknown")  # 일단 unknown, 나중에 업데이트
        recent_summaries.append(turn.body[:100])  # 처음 100자만
    
    # Debug 맥락 감지 (이전 Turn에 debug 관련 키워드가 있는지)
    is_debug_context = False
    for turn in recent_turns:
        text_lower = turn.body.lower()
        if any(keyword in text_lower for keyword in [
            "원인", "에러", "문제", "해결", "분석", "확인", "디버그"
        ]):
            is_debug_context = True
            break
    
    # Plan 맥락 감지 (이전 Turn에 plan 관련 키워드가 있는지)
    is_plan_context = False
    for turn in recent_turns:
        text_lower = turn.body.lower()
        if any(keyword in text_lower for keyword in [
            "계획", "진행", "작업", "단계"
        ]):
            is_plan_context = True
            break
    
    return {
        "recent_turn_count": len(recent_turns),
        "recent_summaries": recent_summaries,
        "is_debug_context": is_debug_context,
        "is_plan_context": is_plan_context,
        "window_start_index": start_index,
        "window_end_index": current_turn_index - 1
    }
```

**1.2 LLM 프롬프트에 맥락 정보 포함**

```python
# backend/core/llm_service.py 수정

def classify_and_summarize_with_llm(
    turn: Turn, 
    context_info: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (맥락 정보 포함)
    
    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)
            - recent_summaries: 최근 Turn들의 요약
            - is_debug_context: Debug 맥락 여부
            - is_plan_context: Plan 맥락 여부
    
    Returns:
        {
            "event_type": EventType,
            "summary": str
        }
    """
    # ... (기존 캐시 로직) ...
    
    # 맥락 정보를 포함한 프롬프트 생성
    context_prompt = ""
    if context_info:
        context_prompt = f"""
## 이전 Turn 맥락 정보

최근 {context_info.get('recent_turn_count', 0)}개 Turn의 요약:
"""
        for i, summary in enumerate(context_info.get('recent_summaries', []), 1):
            context_prompt += f"- Turn {i}: {summary}\n"
        
        if context_info.get('is_debug_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 debug 과정이 진행 중입니다. 현재 Turn도 debug 맥락 안에서 이루어질 가능성이 높습니다.\n"
        
        if context_info.get('is_plan_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 계획 수립이 진행 중입니다.\n"
    
    system_prompt = f"""다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

{context_prompt}

## 이벤트 타입 선택지 및 구분 기준

**중요**: 맥락 정보를 반드시 고려하세요!

- **status_review**: 독립적인 상태 점검 (맥락과 무관한 상태 확인)
  - 예: "프로젝트 현황을 파악합니다", "진행 상황을 확인합니다"
  - ⚠️ 주의: debug 맥락 안에서의 상태 확인은 debug 타입이 더 적합할 수 있음

- **plan**: 새로운 작업 시작 (독립적인 계획 수립)
  - 예: "다음 작업을 계획합니다", "단계별 계획을 수립합니다"
  - ⚠️ 주의: debug 맥락 안에서의 계획은 debug 타입이 더 적합할 수 있음

- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - 예: "스크립트를 작성합니다", "파일을 수정합니다", "코드를 변경합니다"
  - 키워드: "스크립트", "작성", "생성", "수정", "변경"

- **debug**: 문제 해결 과정 (에러, 원인, 해결, 검증)
  - 예: "원인을 분석합니다", "문제를 해결합니다", "에러를 확인합니다"
  - ⚠️ 중요: 이전 Turn에 debug 맥락이 있으면 현재 Turn도 debug 가능성 높음
  - ⚠️ 중요: debug 맥락 안에서의 상태 확인, 계획, 코드 수정도 debug 타입 고려

- **completion**: 완료 (작업 완료, 성공)
  - 예: "작업이 완료되었습니다", "성공적으로 완료했습니다"

- **next_step**: 다음 단계 (다음 작업, 진행)
  - 예: "다음 단계로 진행합니다", "다음 작업을 시작합니다"

- **turn**: 일반 대화 (기본값, 위 타입에 해당하지 않을 때)

## 타입 분류 우선순위

1. **맥락 우선**: 이전 Turn의 맥락을 먼저 고려
   - 이전 Turn에 debug가 있으면 → 현재 Turn도 debug 가능성 높음
   - 이전 Turn에 plan이 있고 현재 Turn이 실행 단계면 → artifact 가능성 높음

2. **키워드 기반**: 현재 Turn의 키워드로 타입 판단

3. **기본값**: 위 조건에 해당하지 않으면 turn

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약, 핵심 동작과 상태 정보 포함]"""
    
    # ... (LLM 호출 로직) ...
```

**1.3 맥락 점수 가중치 적용**

```python
# backend/builders/event_normalizer.py 수정

def create_event_with_llm(
    turn: Turn, 
    session_meta: Optional[SessionMeta] = None,
    turns: Optional[List[Turn]] = None,  # 전체 Turn 리스트 추가
    existing_events: Optional[Dict[int, Event]] = None  # 이미 생성된 Event들
) -> Event:
    """
    LLM 기반 이벤트 생성 (맥락 정보 포함)
    
    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터
        turns: 전체 Turn 리스트 (맥락 정보 수집용)
        existing_events: 이미 생성된 Event들 (turn_index -> Event 매핑)
    
    Returns:
        Event 객체
    """
    from backend.core.llm_service import classify_and_summarize_with_llm
    
    # 맥락 정보 수집
    context_info = None
    if turns is not None:
        context_info = _collect_context_info_with_events(
            turns, 
            turn.turn_index, 
            existing_events or {}
        )
    
    # LLM으로 타입 분류 및 요약 생성 (맥락 정보 포함)
    llm_result = classify_and_summarize_with_llm(turn, context_info=context_info)
    
    # ... (나머지 로직) ...


def _collect_context_info_with_events(
    turns: List[Turn],
    current_turn_index: int,
    existing_events: Dict[int, Event],
    window_size: int = 5
) -> Dict[str, any]:
    """
    이미 생성된 Event 정보를 활용하여 맥락 정보 수집
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        existing_events: 이미 생성된 Event들 (turn_index -> Event 매핑)
        window_size: 윈도우 크기
    
    Returns:
        맥락 정보 딕셔너리
    """
    start_index = max(0, current_turn_index - window_size)
    recent_turns = turns[start_index:current_turn_index]
    
    recent_types = []
    recent_summaries = []
    is_debug_context = False
    is_plan_context = False
    
    for turn in recent_turns:
        # 이미 생성된 Event가 있으면 타입 사용
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            recent_types.append(event.type.value)
            recent_summaries.append(event.summary[:100])
            
            # Debug/Plan 맥락 감지
            if event.type == EventType.DEBUG:
                is_debug_context = True
            elif event.type == EventType.PLAN:
                is_plan_context = True
        else:
            # 아직 생성되지 않았으면 Turn 본문으로 추정
            recent_types.append("unknown")
            recent_summaries.append(turn.body[:100])
            
            # 키워드 기반 맥락 감지
            text_lower = turn.body.lower()
            if any(keyword in text_lower for keyword in [
                "원인", "에러", "문제", "해결", "분석", "확인", "디버그"
            ]):
                is_debug_context = True
            elif any(keyword in text_lower for keyword in [
                "계획", "진행", "작업", "단계"
            ]):
                is_plan_context = True
    
    return {
        "recent_turn_count": len(recent_turns),
        "recent_types": recent_types,
        "recent_summaries": recent_summaries,
        "is_debug_context": is_debug_context,
        "is_plan_context": is_plan_context,
        "window_start_index": start_index,
        "window_end_index": current_turn_index - 1
    }
```

**1.4 병렬 처리 시 순차적 맥락 정보 업데이트**

병렬 처리 시 이전 Turn의 Event가 아직 생성되지 않았을 수 있습니다. 두 가지 접근:

- 접근 1: 순차 처리로 전환 (맥락 정보 정확도 최대화)
- 접근 2: 하이브리드 (1차: 맥락 없이 병렬 처리 → 2차: 맥락 정보로 재분류)

```python
# 접근 2: 하이브리드 방식 (권장)

def _normalize_turns_to_events_parallel_with_context(
    turns: List[Turn], 
    session_meta: Optional[SessionMeta] = None
) -> List[Event]:
    """
    LLM 기반 이벤트 생성 (병렬 처리 + 맥락 정보)
    
    전략:
    1. 1차: 맥락 정보 없이 병렬 처리 (빠른 초기 분류)
    2. 2차: 맥락 정보를 활용하여 재분류 (정확도 향상)
    """
    # 1차: 맥락 정보 없이 병렬 처리
    events_dict = {}
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_turn = {
            executor.submit(create_event_with_llm, turn, session_meta, None, None): turn
            for turn in turns
        }
        
        for future in as_completed(future_to_turn):
            turn = future_to_turn[future]
            try:
                event = future.result()
                events_dict[turn.turn_index] = event
            except Exception as e:
                event = create_single_event_with_priority(turn, session_meta)
                events_dict[turn.turn_index] = event
    
    # 2차: 맥락 정보를 활용하여 재분류 (순차 처리)
    # 맥락 정보가 필요한 Turn만 재분류 (debug 맥락이 있는 경우)
    refined_events = []
    for i, turn in enumerate(turns):
        event = events_dict[turn.turn_index]
        
        # 맥락 정보 수집
        context_info = _collect_context_info_with_events(
            turns, 
            turn.turn_index, 
            events_dict
        )
        
        # Debug 맥락이 있고 현재 타입이 status_review나 plan이면 재분류 고려
        if context_info.get('is_debug_context') and event.type in [EventType.STATUS_REVIEW, EventType.PLAN]:
            # LLM으로 재분류 (맥락 정보 포함)
            llm_result = classify_and_summarize_with_llm(turn, context_info=context_info)
            if llm_result["event_type"] == EventType.DEBUG:
                # 타입 변경
                event.type = EventType.DEBUG
                event.summary = llm_result["summary"]
        
        refined_events.append(event)
    
    return refined_events
```

**예상 효과**:
- `status_review` → `debug` 오류: 10개 → 2-3개로 감소
- `plan` → `debug` 오류: 4개 → 1-2개로 감소
- 전체 정확도: 62.69% → 75%+

---

### 2. HIGH: Summary 품질 개선

#### 현재 문제점
- 요약이 단순 텍스트 자르기만 수행
- 이전 Turn 맥락 미반영
- 특수 기호("@") 의미 파악 실패
- 상태 정보("진행중", "완료") 누락

#### 개선 방안

**2.1 LLM 프롬프트 개선**

```python
# backend/core/llm_service.py 수정

system_prompt = f"""다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

{context_prompt}

## 요약 생성 규칙

**핵심 원칙**:
1. **핵심 동작 포함**: 무엇을 하는가 (동작 중심)
2. **상태 정보 포함**: 진행중/완료/요청 등 상태 명시
3. **중요 세부사항 포함**: 파일명, 수치, 변경사항 등
4. **이전 Turn과의 연관성**: 이전 Turn과 연관이 있으면 언급

**특수 기호 의미**:
- **@**: 첨부 자료 또는 참조 대상 (예: @TODOs.md → "TODOs.md 파일을 참조")
- **#**: 파일명, 항목 번호 등 (예: # Phase 6 → "Phase 6")
- **`**: 코드나 파일명 (예: `main.py` → "main.py 파일")

**요약 예시**:
- ❌ 나쁜 예: "프로젝트 현황을 파악합니다."
- ✅ 좋은 예: "TODOs.md 파일을 참조하여 프로젝트의 현재 진행 상황과 남은 작업들을 파악합니다."

- ❌ 나쁜 예: "변경사항을 확인합니다."
- ✅ 좋은 예: "기본 피드백 생성 로직 추가 완료 후, Git 커밋 진행합니다."

- ❌ 나쁜 예: "서버를 확인합니다."
- ✅ 좋은 예: "@Cursor (cd backend; npm run dev) 터미널 로그에 접속하여 백엔드 서버 상태를 확인합니다."

**요약 길이**: 150-200자 (의미 있는 단위로 자르기, 문장 중간 자르기 금지)

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약, 핵심 동작과 상태 정보 포함]"""
```

**2.2 요약 길이 제한 확대**

```python
# backend/core/llm_service.py 수정

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[...],
    max_tokens=200,  # 150 → 200으로 증가 (요약 품질 향상)
    temperature=0.3,
)
```

**2.3 의미 단위 요약 생성**

```python
# backend/builders/event_normalizer.py의 summarize_turn() 함수는 유지
# LLM이 요약을 생성하므로, LLM 프롬프트 개선으로 해결
```

**예상 효과**: Summary 품질 3.95 → 4.5+

---

### 3. MEDIUM: 타입 정의 명확화

#### 개선 방안

**3.1 기존 타입 경계 명확화**

```python
# LLM 프롬프트에 타입 정의 명확히 반영

system_prompt = f"""...

## 이벤트 타입 선택지 및 구분 기준

**중요**: 맥락 정보를 반드시 고려하세요!

### status_review vs debug 구분
- **status_review**: 독립적인 상태 점검 (맥락과 무관)
  - 예: "프로젝트 현황을 파악합니다" (새로운 작업 시작)
  - ⚠️ 주의: debug 맥락 안에서의 상태 확인은 **debug** 타입이 더 적합
  
- **debug**: 문제 해결 과정의 일부 (맥락 중요)
  - 예: "원인을 분석합니다" (이전 Turn에 문제가 있었음)
  - ⚠️ 중요: 이전 Turn에 debug 맥락이 있으면 현재 Turn도 debug 가능성 높음

### plan vs debug 구분
- **plan**: 새로운 작업 시작 (독립적인 계획)
  - 예: "다음 작업을 계획합니다" (새로운 작업)
  - ⚠️ 주의: debug 맥락 안에서의 계획은 **debug** 타입이 더 적합
  
- **debug**: 문제 해결 과정의 일부 (기존 작업의 연속)
  - 예: "문제 해결을 위해 계획을 수정합니다" (이전 Turn에 문제가 있었음)

### artifact 타입 정의
- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - 키워드: "스크립트 작성", "코드 수정", "파일 생성", "파일 수정"
  - 예: "분석을 위해 스크립트를 작성합니다" → artifact
  - 예: "코드를 수정합니다" → artifact
  - ⚠️ 중요: path_candidates가 있으면 artifact 타입 우선 고려

..."""
```

**3.2 새로운 타입 검토 (선택적)**

현재는 기존 타입으로 처리하고, 필요 시 추가 검토:

```python
# 새로운 타입 추가 시 (선택적)
class EventType(str, Enum):
    STATUS_REVIEW = "status_review"
    PLAN = "plan"
    ARTIFACT = "artifact"
    DEBUG = "debug"
    COMPLETION = "completion"
    NEXT_STEP = "next_step"
    # EXECUTION = "execution"  # 선택적: plan을 실행하는 단계
    # REQUEST_TO_USER = "request_to_user"  # 선택적: 사용자 확인 요청
    TURN = "turn"
```

**예상 효과**: 타입 분류 정확도 추가 5-10% 향상

---

### 4. MEDIUM: Artifact 타입 분류 강화

#### 개선 방안

**4.1 키워드 감지 로직 강화**

```python
# backend/builders/event_normalizer.py 수정

def is_artifact_turn(turn: Turn) -> bool:
    """
    Artifact Turn인지 판단 (키워드 기반)
    
    Args:
        turn: Turn 객체
    
    Returns:
        Artifact Turn 여부
    """
    text_lower = turn.body.lower()
    
    # 파일 경로가 있으면 artifact 우선 고려
    if turn.path_candidates:
        return True
    
    # 키워드 기반 감지
    artifact_keywords = [
        "스크립트 작성", "스크립트 생성", "스크립트를 만들",
        "코드 수정", "코드를 수정", "코드 변경",
        "파일 생성", "파일을 생성", "파일 작성",
        "파일 수정", "파일을 수정", "파일 변경",
        "작성 중", "생성 중", "수정 중"
    ]
    
    return any(keyword in text_lower for keyword in artifact_keywords)
```

**4.2 LLM 프롬프트에 artifact 타입 정의 명확화**

```python
# LLM 프롬프트에 artifact 타입 정의 추가

system_prompt = f"""...

- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - 키워드: "스크립트 작성", "스크립트 생성", "코드 수정", "파일 생성", "파일 수정"
  - 예: "분석을 위해 스크립트를 작성합니다" → artifact
  - 예: "코드를 수정합니다" → artifact
  - ⚠️ 중요: path_candidates가 있으면 artifact 타입 우선 고려
  - ⚠️ 중요: "스크립트", "작성", "생성", "수정" 키워드가 있으면 artifact 가능성 높음

..."""
```

**4.3 path_candidates 우선 고려 로직**

```python
# backend/builders/event_normalizer.py 수정

def create_event_with_llm(...):
    # LLM으로 타입 분류
    llm_result = classify_and_summarize_with_llm(turn, context_info=context_info)
    event_type = llm_result["event_type"]
    
    # path_candidates가 있으면 artifact 타입 우선 고려
    if turn.path_candidates and event_type not in [EventType.ARTIFACT, EventType.DEBUG]:
        # LLM이 artifact로 분류하지 않았지만 path_candidates가 있으면 재검토
        if is_artifact_turn(turn):
            event_type = EventType.ARTIFACT
            # Summary도 artifact에 맞게 수정
            summary = f"{llm_result['summary']} (파일: {', '.join(turn.path_candidates[:3])})"
        else:
            summary = llm_result["summary"]
    else:
        summary = llm_result["summary"]
    
    # ... (나머지 로직) ...
```

**예상 효과**: Artifact 타입 분류 정확도 향상

---

## 구현 순서

1. 맥락 기반 타입 분류 구현 (최우선)
   - 슬라이딩 윈도우 로직 구현
   - LLM 프롬프트에 맥락 정보 추가
   - 하이브리드 방식 적용 (병렬 + 순차 재분류)

2. Summary 품질 개선
   - LLM 프롬프트 개선 (맥락 정보, 특수 기호 설명)
   - 요약 길이 제한 확대 (150 → 200자)

3. 타입 정의 명확화
   - LLM 프롬프트에 타입 정의 명확히 반영

4. Artifact 타입 분류 강화
   - 키워드 감지 로직 강화
   - path_candidates 우선 고려 로직 구현

이 순서로 진행할까요?

```python
# backend/builders/event_normalizer.py 수정

def _collect_context_info(
    turns: List[Turn], 
    current_turn_index: int, 
    window_size: int = 5
) -> Dict[str, any]:
    """
    현재 Turn의 맥락 정보 수집 (슬라이딩 윈도우)
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        window_size: 윈도우 크기 (기본값: 5, 최근 5개 Turn 확인)
    
    Returns:
        맥락 정보 딕셔너리
    """
    # 최근 window_size개 Turn 수집 (현재 Turn 제외)
    start_index = max(0, current_turn_index - window_size)
    recent_turns = turns[start_index:current_turn_index]
    
    # 이전 Turn들의 타입 정보 (이미 생성된 Event가 있으면 사용)
    recent_types = []
    recent_summaries = []
    
    for turn in recent_turns:
        # 이미 생성된 Event가 있으면 타입 사용, 없으면 추정
        # (병렬 처리 시에는 아직 생성되지 않았을 수 있음)
        recent_types.append("unknown")  # 일단 unknown, 나중에 업데이트
        recent_summaries.append(turn.body[:100])  # 처음 100자만
    
    # Debug 맥락 감지 (이전 Turn에 debug 관련 키워드가 있는지)
    is_debug_context = False
    for turn in recent_turns:
        text_lower = turn.body.lower()
        if any(keyword in text_lower for keyword in [
            "원인", "에러", "문제", "해결", "분석", "확인", "디버그"
        ]):
            is_debug_context = True
            break
    
    # Plan 맥락 감지 (이전 Turn에 plan 관련 키워드가 있는지)
    is_plan_context = False
    for turn in recent_turns:
        text_lower = turn.body.lower()
        if any(keyword in text_lower for keyword in [
            "계획", "진행", "작업", "단계"
        ]):
            is_plan_context = True
            break
    
    return {
        "recent_turn_count": len(recent_turns),
        "recent_summaries": recent_summaries,
        "is_debug_context": is_debug_context,
        "is_plan_context": is_plan_context,
        "window_start_index": start_index,
        "window_end_index": current_turn_index - 1
    }
```

```python
# backend/core/llm_service.py 수정

def classify_and_summarize_with_llm(
    turn: Turn, 
    context_info: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (맥락 정보 포함)
    
    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)
            - recent_summaries: 최근 Turn들의 요약
            - is_debug_context: Debug 맥락 여부
            - is_plan_context: Plan 맥락 여부
    
    Returns:
        {
            "event_type": EventType,
            "summary": str
        }
    """
    # ... (기존 캐시 로직) ...
    
    # 맥락 정보를 포함한 프롬프트 생성
    context_prompt = ""
    if context_info:
        context_prompt = f"""
## 이전 Turn 맥락 정보

최근 {context_info.get('recent_turn_count', 0)}개 Turn의 요약:
"""
        for i, summary in enumerate(context_info.get('recent_summaries', []), 1):
            context_prompt += f"- Turn {i}: {summary}\n"
        
        if context_info.get('is_debug_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 debug 과정이 진행 중입니다. 현재 Turn도 debug 맥락 안에서 이루어질 가능성이 높습니다.\n"
        
        if context_info.get('is_plan_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 계획 수립이 진행 중입니다.\n"
    
    system_prompt = f"""다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

{context_prompt}

## 이벤트 타입 선택지 및 구분 기준

**중요**: 맥락 정보를 반드시 고려하세요!

- **status_review**: 독립적인 상태 점검 (맥락과 무관한 상태 확인)
  - 예: "프로젝트 현황을 파악합니다", "진행 상황을 확인합니다"
  - ⚠️ 주의: debug 맥락 안에서의 상태 확인은 debug 타입이 더 적합할 수 있음

- **plan**: 새로운 작업 시작 (독립적인 계획 수립)
  - 예: "다음 작업을 계획합니다", "단계별 계획을 수립합니다"
  - ⚠️ 주의: debug 맥락 안에서의 계획은 debug 타입이 더 적합할 수 있음

- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - 예: "스크립트를 작성합니다", "파일을 수정합니다", "코드를 변경합니다"
  - 키워드: "스크립트", "작성", "생성", "수정", "변경"

- **debug**: 문제 해결 과정 (에러, 원인, 해결, 검증)
  - 예: "원인을 분석합니다", "문제를 해결합니다", "에러를 확인합니다"
  - ⚠️ 중요: 이전 Turn에 debug 맥락이 있으면 현재 Turn도 debug 가능성 높음
  - ⚠️ 중요: debug 맥락 안에서의 상태 확인, 계획, 코드 수정도 debug 타입 고려

- **completion**: 완료 (작업 완료, 성공)
  - 예: "작업이 완료되었습니다", "성공적으로 완료했습니다"

- **next_step**: 다음 단계 (다음 작업, 진행)
  - 예: "다음 단계로 진행합니다", "다음 작업을 시작합니다"

- **turn**: 일반 대화 (기본값, 위 타입에 해당하지 않을 때)

## 타입 분류 우선순위

1. **맥락 우선**: 이전 Turn의 맥락을 먼저 고려
   - 이전 Turn에 debug가 있으면 → 현재 Turn도 debug 가능성 높음
   - 이전 Turn에 plan이 있고 현재 Turn이 실행 단계면 → artifact 가능성 높음

2. **키워드 기반**: 현재 Turn의 키워드로 타입 판단

3. **기본값**: 위 조건에 해당하지 않으면 turn

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약, 핵심 동작과 상태 정보 포함]"""
    
    # ... (LLM 호출 로직) ...
```

```python
# backend/builders/event_normalizer.py 수정

def create_event_with_llm(
    turn: Turn, 
    session_meta: Optional[SessionMeta] = None,
    turns: Optional[List[Turn]] = None,  # 전체 Turn 리스트 추가
    existing_events: Optional[Dict[int, Event]] = None  # 이미 생성된 Event들
) -> Event:
    """
    LLM 기반 이벤트 생성 (맥락 정보 포함)
    
    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터
        turns: 전체 Turn 리스트 (맥락 정보 수집용)
        existing_events: 이미 생성된 Event들 (turn_index -> Event 매핑)
    
    Returns:
        Event 객체
    """
    from backend.core.llm_service import classify_and_summarize_with_llm
    
    # 맥락 정보 수집
    context_info = None
    if turns is not None:
        context_info = _collect_context_info_with_events(
            turns, 
            turn.turn_index, 
            existing_events or {}
        )
    
    # LLM으로 타입 분류 및 요약 생성 (맥락 정보 포함)
    llm_result = classify_and_summarize_with_llm(turn, context_info=context_info)
    
    # ... (나머지 로직) ...


def _collect_context_info_with_events(
    turns: List[Turn],
    current_turn_index: int,
    existing_events: Dict[int, Event],
    window_size: int = 5
) -> Dict[str, any]:
    """
    이미 생성된 Event 정보를 활용하여 맥락 정보 수집
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        existing_events: 이미 생성된 Event들 (turn_index -> Event 매핑)
        window_size: 윈도우 크기
    
    Returns:
        맥락 정보 딕셔너리
    """
    start_index = max(0, current_turn_index - window_size)
    recent_turns = turns[start_index:current_turn_index]
    
    recent_types = []
    recent_summaries = []
    is_debug_context = False
    is_plan_context = False
    
    for turn in recent_turns:
        # 이미 생성된 Event가 있으면 타입 사용
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            recent_types.append(event.type.value)
            recent_summaries.append(event.summary[:100])
            
            # Debug/Plan 맥락 감지
            if event.type == EventType.DEBUG:
                is_debug_context = True
            elif event.type == EventType.PLAN:
                is_plan_context = True
        else:
            # 아직 생성되지 않았으면 Turn 본문으로 추정
            recent_types.append("unknown")
            recent_summaries.append(turn.body[:100])
            
            # 키워드 기반 맥락 감지
            text_lower = turn.body.lower()
            if any(keyword in text_lower for keyword in [
                "원인", "에러", "문제", "해결", "분석", "확인", "디버그"
            ]):
                is_debug_context = True
            elif any(keyword in text_lower for keyword in [
                "계획", "진행", "작업", "단계"
            ]):
                is_plan_context = True
    
    return {
        "recent_turn_count": len(recent_turns),
        "recent_types": recent_types,
        "recent_summaries": recent_summaries,
        "is_debug_context": is_debug_context,
        "is_plan_context": is_plan_context,
        "window_start_index": start_index,
        "window_end_index": current_turn_index - 1
    }
```

```python
# 접근 2: 하이브리드 방식 (권장)

def _normalize_turns_to_events_parallel_with_context(
    turns: List[Turn], 
    session_meta: Optional[SessionMeta] = None
) -> List[Event]:
    """
    LLM 기반 이벤트 생성 (병렬 처리 + 맥락 정보)
    
    전략:
    1. 1차: 맥락 정보 없이 병렬 처리 (빠른 초기 분류)
    2. 2차: 맥락 정보를 활용하여 재분류 (정확도 향상)
    """
    # 1차: 맥락 정보 없이 병렬 처리
    events_dict = {}
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_turn = {
            executor.submit(create_event_with_llm, turn, session_meta, None, None): turn
            for turn in turns
        }
        
        for future in as_completed(future_to_turn):
            turn = future_to_turn[future]
            try:
                event = future.result()
                events_dict[turn.turn_index] = event
            except Exception as e:
                event = create_single_event_with_priority(turn, session_meta)
                events_dict[turn.turn_index] = event
    
    # 2차: 맥락 정보를 활용하여 재분류 (순차 처리)
    # 맥락 정보가 필요한 Turn만 재분류 (debug 맥락이 있는 경우)
    refined_events = []
    for i, turn in enumerate(turns):
        event = events_dict[turn.turn_index]
        
        # 맥락 정보 수집
        context_info = _collect_context_info_with_events(
            turns, 
            turn.turn_index, 
            events_dict
        )
        
        # Debug 맥락이 있고 현재 타입이 status_review나 plan이면 재분류 고려
        if context_info.get('is_debug_context') and event.type in [EventType.STATUS_REVIEW, EventType.PLAN]:
            # LLM으로 재분류 (맥락 정보 포함)
            llm_result = classify_and_summarize_with_llm(turn, context_info=context_info)
            if llm_result["event_type"] == EventType.DEBUG:
                # 타입 변경
                event.type = EventType.DEBUG
                event.summary = llm_result["summary"]
        
        refined_events.append(event)
    
    return refined_events
```

```python
# backend/core/llm_service.py 수정

system_prompt = f"""다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

{context_prompt}

## 요약 생성 규칙

**핵심 원칙**:
1. **핵심 동작 포함**: 무엇을 하는가 (동작 중심)
2. **상태 정보 포함**: 진행중/완료/요청 등 상태 명시
3. **중요 세부사항 포함**: 파일명, 수치, 변경사항 등
4. **이전 Turn과의 연관성**: 이전 Turn과 연관이 있으면 언급

**특수 기호 의미**:
- **@**: 첨부 자료 또는 참조 대상 (예: @TODOs.md → "TODOs.md 파일을 참조")
- **#**: 파일명, 항목 번호 등 (예: # Phase 6 → "Phase 6")
- **`**: 코드나 파일명 (예: `main.py` → "main.py 파일")

**요약 예시**:
- ❌ 나쁜 예: "프로젝트 현황을 파악합니다."
- ✅ 좋은 예: "TODOs.md 파일을 참조하여 프로젝트의 현재 진행 상황과 남은 작업들을 파악합니다."

- ❌ 나쁜 예: "변경사항을 확인합니다."
- ✅ 좋은 예: "기본 피드백 생성 로직 추가 완료 후, Git 커밋 진행합니다."

- ❌ 나쁜 예: "서버를 확인합니다."
- ✅ 좋은 예: "@Cursor (cd backend; npm run dev) 터미널 로그에 접속하여 백엔드 서버 상태를 확인합니다."

**요약 길이**: 150-200자 (의미 있는 단위로 자르기, 문장 중간 자르기 금지)

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약, 핵심 동작과 상태 정보 포함]"""
```

```python
# backend/core/llm_service.py 수정

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[...],
    max_tokens=200,  # 150 → 200으로 증가 (요약 품질 향상)
    temperature=0.3,
)
```

```python
# backend/builders/event_normalizer.py의 summarize_turn() 함수는 유지
# LLM이 요약을 생성하므로, LLM 프롬프트 개선으로 해결
```

```python
# LLM 프롬프트에 타입 정의 명확히 반영

system_prompt = f"""...

## 이벤트 타입 선택지 및 구분 기준

**중요**: 맥락 정보를 반드시 고려하세요!

### status_review vs debug 구분
- **status_review**: 독립적인 상태 점검 (맥락과 무관)
  - 예: "프로젝트 현황을 파악합니다" (새로운 작업 시작)
  - ⚠️ 주의: debug 맥락 안에서의 상태 확인은 **debug** 타입이 더 적합
  
- **debug**: 문제 해결 과정의 일부 (맥락 중요)
  - 예: "원인을 분석합니다" (이전 Turn에 문제가 있었음)
  - ⚠️ 중요: 이전 Turn에 debug 맥락이 있으면 현재 Turn도 debug 가능성 높음

### plan vs debug 구분
- **plan**: 새로운 작업 시작 (독립적인 계획)
  - 예: "다음 작업을 계획합니다" (새로운 작업)
  - ⚠️ 주의: debug 맥락 안에서의 계획은 **debug** 타입이 더 적합
  
- **debug**: 문제 해결 과정의 일부 (기존 작업의 연속)
  - 예: "문제 해결을 위해 계획을 수정합니다" (이전 Turn에 문제가 있었음)

### artifact 타입 정의
- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - 키워드: "스크립트 작성", "코드 수정", "파일 생성", "파일 수정"
  - 예: "분석을 위해 스크립트를 작성합니다" → artifact
  - 예: "코드를 수정합니다" → artifact
  - ⚠️ 중요: path_candidates가 있으면 artifact 타입 우선 고려

..."""
```

```python
# 새로운 타입 추가 시 (선택적)
class EventType(str, Enum):
    STATUS_REVIEW = "status_review"
    PLAN = "plan"
    ARTIFACT = "artifact"
    DEBUG = "debug"
    COMPLETION = "completion"
    NEXT_STEP = "next_step"
    # EXECUTION = "execution"  # 선택적: plan을 실행하는 단계
    # REQUEST_TO_USER = "request_to_user"  # 선택적: 사용자 확인 요청
    TURN = "turn"
```

```python
# backend/builders/event_normalizer.py 수정

def is_artifact_turn(turn: Turn) -> bool:
    """
    Artifact Turn인지 판단 (키워드 기반)
    
    Args:
        turn: Turn 객체
    
    Returns:
        Artifact Turn 여부
    """
    text_lower = turn.body.lower()
    
    # 파일 경로가 있으면 artifact 우선 고려
    if turn.path_candidates:
        return True
    
    # 키워드 기반 감지
    artifact_keywords = [
        "스크립트 작성", "스크립트 생성", "스크립트를 만들",
        "코드 수정", "코드를 수정", "코드 변경",
        "파일 생성", "파일을 생성", "파일 작성",
        "파일 수정", "파일을 수정", "파일 변경",
        "작성 중", "생성 중", "수정 중"
    ]
    
    return any(keyword in text_lower for keyword in artifact_keywords)
```

```python
# LLM 프롬프트에 artifact 타입 정의 추가

system_prompt = f"""...

- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - 키워드: "스크립트 작성", "스크립트 생성", "코드 수정", "파일 생성", "파일 수정"
  - 예: "분석을 위해 스크립트를 작성합니다" → artifact
  - 예: "코드를 수정합니다" → artifact
  - ⚠️ 중요: path_candidates가 있으면 artifact 타입 우선 고려
  - ⚠️ 중요: "스크립트", "작성", "생성", "수정" 키워드가 있으면 artifact 가능성 높음

..."""
```

```python
# backend/builders/event_normalizer.py 수정

def create_event_with_llm(...):
    # LLM으로 타입 분류
    llm_result = classify_and_summarize_with_llm(turn, context_info=context_info)
    event_type = llm_result["event_type"]
    
    # path_candidates가 있으면 artifact 타입 우선 고려
    if turn.path_candidates and event_type not in [EventType.ARTIFACT, EventType.DEBUG]:
        # LLM이 artifact로 분류하지 않았지만 path_candidates가 있으면 재검토
        if is_artifact_turn(turn):
            event_type = EventType.ARTIFACT
            # Summary도 artifact에 맞게 수정
            summary = f"{llm_result['summary']} (파일: {', '.join(turn.path_candidates[:3])})"
        else:
            summary = llm_result["summary"]
    else:
        summary = llm_result["summary"]
    
    # ... (나머지 로직) ...
```

---

**User**

Phase 2의 마크다운 파싱부터  artifact 타입 분류 및 처리 관련해서 다음 질문에 답변
- 현재 입력 대화 마크다운 파싱할때, 대화 부분하고 artifact 부분이 구분되어 추출되는 것이 맞나?
- Phase3의 이벤트 분석의 입력 파일은 대화부분에 대한 파싱 결과만 들어가나?
- 그러면 원본 대화 마크다운에서 artifact  부분은 어디에 사용되지?
- 이 artifact 부분은 거기에 맞는 대화 부분과 set를 이루고 있었을텐데 (원본 마크다운기준) 이것을 이용하는 것이 맞지 않나?

세심하게 검토해보세요

---

**Cursor**

Phase 2 파싱과 Phase 3 이벤트 정규화에서 artifact 처리 방식을 확인 중입니다.


원본 마크다운 구조와 현재 파싱/이벤트 정규화에서 artifact 처리 방식을 확인 중입니다.


원본 마크다운 구조와 현재 구현을 확인 중입니다.


원본 마크다운 구조와 현재 구현을 확인했습니다. 질문에 답변합니다.

## 질문에 대한 답변

### 1. 현재 입력 대화 마크다운 파싱할 때, 대화 부분과 artifact 부분이 구분되어 추출되는 것이 맞나?

**답변: 맞습니다. 구분되어 추출됩니다.**

```77:109:backend/parser/turns.py
def parse_turn(block: str, turn_index: int) -> Turn:
    """
    Turn 블록 파싱
    
    Args:
        block: Turn 블록 텍스트
        turn_index: Turn 인덱스
    
    Returns:
        Turn 객체
    """
    # Speaker 추출
    speaker_match = SPEAKER_RE.search(block) or SPEAKER_FALLBACK_RE.search(block)
    speaker = speaker_match.group(1) if speaker_match else "Unknown"
    
    # 코드 블록 제거한 body 추출
    body = re.sub(r"```.*?```", "", block, flags=re.DOTALL)
    body = re.sub(r"^\s*\*\*(User|Cursor)\*\*\s*:?\s*", "", body, flags=re.MULTILINE)
    body = body.strip()
    
    # 코드 블록 추출
    code_blocks = extract_code_blocks(block, turn_index)
    
    # 파일 경로 후보 추출
    path_candidates = extract_path_candidates(block)
    
    return Turn(
        turn_index=turn_index,
        speaker=speaker,
        body=body,
        code_blocks=code_blocks,
        path_candidates=path_candidates,
    )
```

- `body`: 코드 블록을 제거한 대화 텍스트
- `code_blocks`: 코드 펜스에서 추출된 코드 블록 리스트
- `path_candidates`: 정규식으로 추출된 파일 경로 리스트

같은 Turn 블록 안에서 함께 추출되지만, 필드는 구분되어 저장됩니다.

---

### 2. Phase 3의 이벤트 분석의 입력 파일은 대화 부분에 대한 파싱 결과만 들어가나?

**답변: 문제입니다. LLM은 `turn.body`만 보고 타입 분류합니다.**

```71:159:backend/core/llm_service.py
def classify_and_summarize_with_llm(turn: Turn) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (개선 버전)
    
    Args:
        turn: Turn 객체
    
    Returns:
        {
            "event_type": EventType,
            "summary": str
        }
    """
    # ... (캐시 로직) ...
    
    # LLM 호출 (재시도 로직 포함)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.
                ...
                """,
            },
            {
                "role": "user",
                "content": turn.body[:2000],  # ⚠️ body만 전달!
            },
        ],
        ...
    )
```

- `turn.body`만 LLM에 전달됨
- `turn.code_blocks`와 `turn.path_candidates`는 LLM 프롬프트에 포함되지 않음
- 결과: LLM이 artifact 정보를 모르고 타입 분류함

---

### 3. 원본 대화 마크다운에서 artifact 부분은 어디에 사용되지?

**답변: 타입 분류에는 사용되지 않고, 나중에 Event의 artifacts 배열에만 추가됩니다.**

```86:125:backend/builders/event_normalizer.py
def create_event_with_llm(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    LLM 기반 이벤트 생성 (gpt-4.1-mini)
    
    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)
    
    Returns:
        Event 객체 (processing_method="llm")
    """
    from backend.core.llm_service import classify_and_summarize_with_llm
    
    # LLM으로 타입 분류 및 요약 생성
    llm_result = classify_and_summarize_with_llm(turn)  # ⚠️ body만 사용
    event_type = llm_result["event_type"]
    summary = llm_result["summary"]
    
    # Artifact 연결 (파일 경로가 있으면)
    artifacts = []
    if turn.path_candidates:
        artifacts = [{"path": path, "action": "mention"} for path in turn.path_candidates]
    
    # Snippet 참조 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]
    
    return Event(
        ...
        type=event_type,  # ⚠️ LLM이 body만 보고 분류한 타입
        summary=summary,  # ⚠️ LLM이 body만 보고 생성한 요약
        artifacts=artifacts,  # ✅ path_candidates는 나중에 추가됨
        snippet_refs=snippet_refs,  # ✅ code_blocks는 나중에 추가됨
        ...
    )
```

문제점:
- 타입 분류 시: `turn.body`만 사용 → artifact 정보 미반영
- Artifact 연결 시: `turn.path_candidates`와 `turn.code_blocks`는 나중에 추가됨
- 결과: "스크립트를 작성합니다" + 코드 블록이 있어도 LLM은 body만 보고 plan이나 status_review로 분류할 수 있음

---

### 4. 이 artifact 부분은 거기에 맞는 대화 부분과 set를 이루고 있었을 텐데, 이것을 이용하는 것이 맞지 않나?

**답변: 맞습니다. 이것이 artifact 타입 분류 실패의 주요 원인입니다.**

원본 마크다운 구조 예시:
```markdown
---

**Cursor**

분석을 위해 자체 스크립트를 작성합니다.

```python
# 스크립트 코드
import os
...
```

---

**User**

확인했습니다.

---
```

현재 처리:
- Turn 블록에서 추출:
  - `body`: "분석을 위해 자체 스크립트를 작성합니다."
  - `code_blocks`: [CodeBlock(lang="python", code="...")]
  - `path_candidates`: [] (코드 블록만 있고 파일 경로는 없음)
- LLM 타입 분류:
  - `turn.body`만 전달 → "분석을 위해 자체 스크립트를 작성합니다."
  - LLM은 코드 블록 정보를 모름 → plan이나 status_review로 분류 가능
- 올바른 분류:
  - 코드 블록이 있으면 → artifact 타입이어야 함

---

## 핵심 문제 요약

### 현재 구조의 문제점

1. Phase 2 파싱: 올바름
   - Turn 블록에서 body, code_blocks, path_candidates를 모두 추출
   - 같은 Turn 블록 안의 정보를 보존

2. Phase 3 이벤트 정규화: 문제
   - LLM이 `turn.body`만 보고 타입 분류
   - `turn.code_blocks`와 `turn.path_candidates` 정보 미활용
   - 결과: artifact 타입 분류 실패

3. Artifact 연결: 나중에 처리
   - 타입 분류 후 `artifacts` 배열에 추가
   - 타입 분류에는 영향을 주지 않음

---

## 개선 방안

### LLM 프롬프트에 Artifact 정보 포함

```python
# backend/core/llm_service.py 수정

def classify_and_summarize_with_llm(
    turn: Turn, 
    context_info: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (Artifact 정보 포함)
    
    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)
    
    Returns:
        {
            "event_type": EventType,
            "summary": str
        }
    """
    # ... (캐시 로직) ...
    
    # Artifact 정보 수집
    artifact_info = ""
    if turn.code_blocks:
        artifact_info += f"\n## 코드 블록 정보\n"
        artifact_info += f"- 코드 블록 개수: {len(turn.code_blocks)}\n"
        for i, block in enumerate(turn.code_blocks[:3], 1):  # 최대 3개만
            artifact_info += f"- 코드 블록 {i}: 언어={block.lang}, 길이={len(block.code)}자\n"
    
    if turn.path_candidates:
        artifact_info += f"\n## 파일 경로 정보\n"
        artifact_info += f"- 파일 경로: {', '.join(turn.path_candidates[:5])}\n"  # 최대 5개만
    
    # 맥락 정보 (기존)
    context_prompt = ""
    if context_info:
        # ... (기존 맥락 정보) ...
    
    system_prompt = f"""다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

{context_prompt}

{artifact_info}

## 이벤트 타입 선택지 및 구분 기준

**⚠️ 중요: Artifact 정보를 반드시 고려하세요!**

- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - **코드 블록이 있으면**: artifact 타입 가능성 매우 높음
  - **파일 경로가 있으면**: artifact 타입 가능성 높음
  - 키워드: "스크립트 작성", "코드 수정", "파일 생성", "파일 수정"
  - 예: "분석을 위해 스크립트를 작성합니다" + 코드 블록 → **artifact**
  - 예: "코드를 수정합니다" + 코드 블록 → **artifact**

- **status_review**: 독립적인 상태 점검 (맥락과 무관)
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

- **plan**: 새로운 작업 시작 (독립적인 계획)
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

- **debug**: 문제 해결 과정 (에러, 원인, 해결, 검증)
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

...

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약, 핵심 동작과 상태 정보 포함]"""
    
    user_content = turn.body[:2000]
    if artifact_info:
        user_content += f"\n\n{artifact_info}"  # Artifact 정보도 포함
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_content,
            },
        ],
        max_tokens=200,
        temperature=0.3,
    )
    
    # ... (응답 파싱) ...
```

### 캐시 키 생성 시 Artifact 정보 포함

```python
# backend/core/llm_service.py 수정

def classify_and_summarize_with_llm(...):
    # 캐시 키 생성 시 Artifact 정보도 포함
    text_content = turn.body[:2000]
    
    # Artifact 정보를 캐시 키에 포함
    artifact_hash = ""
    if turn.code_blocks:
        artifact_hash += f"_code_{len(turn.code_blocks)}"
    if turn.path_candidates:
        artifact_hash += f"_path_{len(turn.path_candidates)}"
    
    text_hash = _generate_text_hash(text_content + artifact_hash, max_length=2000)
    cache_key = f"llm_{text_hash}"
    
    # ... (나머지 로직) ...
```

---

## 결론

- Phase 2 파싱: 올바름 (대화와 artifact를 구분하여 추출)
- Phase 3 이벤트 정규화: 문제 (LLM이 body만 보고 분류)
- 해결: LLM 프롬프트에 artifact 정보(code_blocks, path_candidates) 포함

이 개선으로 artifact 타입 분류 정확도가 향상될 것으로 예상됩니다.

```python
def parse_turn(block: str, turn_index: int) -> Turn:
    """
    Turn 블록 파싱
    
    Args:
        block: Turn 블록 텍스트
        turn_index: Turn 인덱스
    
    Returns:
        Turn 객체
    """
    # Speaker 추출
    speaker_match = SPEAKER_RE.search(block) or SPEAKER_FALLBACK_RE.search(block)
    speaker = speaker_match.group(1) if speaker_match else "Unknown"
    
    # 코드 블록 제거한 body 추출
    body = re.sub(r"```.*?```", "", block, flags=re.DOTALL)
    body = re.sub(r"^\s*\*\*(User|Cursor)\*\*\s*:?\s*", "", body, flags=re.MULTILINE)
    body = body.strip()
    
    # 코드 블록 추출
    code_blocks = extract_code_blocks(block, turn_index)
    
    # 파일 경로 후보 추출
    path_candidates = extract_path_candidates(block)
    
    return Turn(
        turn_index=turn_index,
        speaker=speaker,
        body=body,
        code_blocks=code_blocks,
        path_candidates=path_candidates,
    )
```

```plaintext
def classify_and_summarize_with_llm(turn: Turn) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (개선 버전)
    
    Args:
        turn: Turn 객체
    
    Returns:
        {
            "event_type": EventType,
            "summary": str
        }
    """
    # ... (캐시 로직) ...
    
    # LLM 호출 (재시도 로직 포함)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.
                ...
                """,
            },
            {
                "role": "user",
                "content": turn.body[:2000],  # ⚠️ body만 전달!
            },
        ],
        ...
    )
```

```python
def classify_and_summarize_with_llm(turn: Turn) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (개선 버전)
    
    Args:
        turn: Turn 객체
    
    Returns:
        {
            "event_type": EventType,
            "summary": str
        }
    """
    # ... (캐시 로직) ...
    
    # LLM 호출 (재시도 로직 포함)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.
                ...
                """,
            },
            {
                "role": "user",
                "content": turn.body[:2000],  # ⚠️ body만 전달!
            },
        ],
        ...
    )
```

```python
def create_event_with_llm(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    LLM 기반 이벤트 생성 (gpt-4.1-mini)
    
    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)
    
    Returns:
        Event 객체 (processing_method="llm")
    """
    from backend.core.llm_service import classify_and_summarize_with_llm
    
    # LLM으로 타입 분류 및 요약 생성
    llm_result = classify_and_summarize_with_llm(turn)  # ⚠️ body만 사용
    event_type = llm_result["event_type"]
    summary = llm_result["summary"]
    
    # Artifact 연결 (파일 경로가 있으면)
    artifacts = []
    if turn.path_candidates:
        artifacts = [{"path": path, "action": "mention"} for path in turn.path_candidates]
    
    # Snippet 참조 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]
    
    return Event(
        ...
        type=event_type,  # ⚠️ LLM이 body만 보고 분류한 타입
        summary=summary,  # ⚠️ LLM이 body만 보고 생성한 요약
        artifacts=artifacts,  # ✅ path_candidates는 나중에 추가됨
        snippet_refs=snippet_refs,  # ✅ code_blocks는 나중에 추가됨
        ...
    )
```

```python
def create_event_with_llm(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    LLM 기반 이벤트 생성 (gpt-4.1-mini)
    
    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)
    
    Returns:
        Event 객체 (processing_method="llm")
    """
    from backend.core.llm_service import classify_and_summarize_with_llm
    
    # LLM으로 타입 분류 및 요약 생성
    llm_result = classify_and_summarize_with_llm(turn)  # ⚠️ body만 사용
    event_type = llm_result["event_type"]
    summary = llm_result["summary"]
    
    # Artifact 연결 (파일 경로가 있으면)
    artifacts = []
    if turn.path_candidates:
        artifacts = [{"path": path, "action": "mention"} for path in turn.path_candidates]
    
    # Snippet 참조 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]
    
    return Event(
        ...
        type=event_type,  # ⚠️ LLM이 body만 보고 분류한 타입
        summary=summary,  # ⚠️ LLM이 body만 보고 생성한 요약
        artifacts=artifacts,  # ✅ path_candidates는 나중에 추가됨
        snippet_refs=snippet_refs,  # ✅ code_blocks는 나중에 추가됨
        ...
    )
```

```python
---

**Cursor**

분석을 위해 자체 스크립트를 작성합니다.
thon
# 스크립트 코드
import os
...---

**User**

확인했습니다.

---
```

```markdown
---

**Cursor**

분석을 위해 자체 스크립트를 작성합니다.
thon
# 스크립트 코드
import os
...---

**User**

확인했습니다.

---
```

```markdown
# backend/core/llm_service.py 수정

def classify_and_summarize_with_llm(
    turn: Turn, 
    context_info: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (Artifact 정보 포함)
    
    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)
    
    Returns:
        {
            "event_type": EventType,
            "summary": str
        }
    """
    # ... (캐시 로직) ...
    
    # Artifact 정보 수집
    artifact_info = ""
    if turn.code_blocks:
        artifact_info += f"\n## 코드 블록 정보\n"
        artifact_info += f"- 코드 블록 개수: {len(turn.code_blocks)}\n"
        for i, block in enumerate(turn.code_blocks[:3], 1):  # 최대 3개만
            artifact_info += f"- 코드 블록 {i}: 언어={block.lang}, 길이={len(block.code)}자\n"
    
    if turn.path_candidates:
        artifact_info += f"\n## 파일 경로 정보\n"
        artifact_info += f"- 파일 경로: {', '.join(turn.path_candidates[:5])}\n"  # 최대 5개만
    
    # 맥락 정보 (기존)
    context_prompt = ""
    if context_info:
        # ... (기존 맥락 정보) ...
    
    system_prompt = f"""다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

{context_prompt}

{artifact_info}

## 이벤트 타입 선택지 및 구분 기준

**⚠️ 중요: Artifact 정보를 반드시 고려하세요!**

- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - **코드 블록이 있으면**: artifact 타입 가능성 매우 높음
  - **파일 경로가 있으면**: artifact 타입 가능성 높음
  - 키워드: "스크립트 작성", "코드 수정", "파일 생성", "파일 수정"
  - 예: "분석을 위해 스크립트를 작성합니다" + 코드 블록 → **artifact**
  - 예: "코드를 수정합니다" + 코드 블록 → **artifact**

- **status_review**: 독립적인 상태 점검 (맥락과 무관)
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

- **plan**: 새로운 작업 시작 (독립적인 계획)
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

- **debug**: 문제 해결 과정 (에러, 원인, 해결, 검증)
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

...

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약, 핵심 동작과 상태 정보 포함]"""
    
    user_content = turn.body[:2000]
    if artifact_info:
        user_content += f"\n\n{artifact_info}"  # Artifact 정보도 포함
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_content,
            },
        ],
        max_tokens=200,
        temperature=0.3,
    )
    
    # ... (응답 파싱) ...
```

```python
# backend/core/llm_service.py 수정

def classify_and_summarize_with_llm(
    turn: Turn, 
    context_info: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (Artifact 정보 포함)
    
    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)
    
    Returns:
        {
            "event_type": EventType,
            "summary": str
        }
    """
    # ... (캐시 로직) ...
    
    # Artifact 정보 수집
    artifact_info = ""
    if turn.code_blocks:
        artifact_info += f"\n## 코드 블록 정보\n"
        artifact_info += f"- 코드 블록 개수: {len(turn.code_blocks)}\n"
        for i, block in enumerate(turn.code_blocks[:3], 1):  # 최대 3개만
            artifact_info += f"- 코드 블록 {i}: 언어={block.lang}, 길이={len(block.code)}자\n"
    
    if turn.path_candidates:
        artifact_info += f"\n## 파일 경로 정보\n"
        artifact_info += f"- 파일 경로: {', '.join(turn.path_candidates[:5])}\n"  # 최대 5개만
    
    # 맥락 정보 (기존)
    context_prompt = ""
    if context_info:
        # ... (기존 맥락 정보) ...
    
    system_prompt = f"""다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

{context_prompt}

{artifact_info}

## 이벤트 타입 선택지 및 구분 기준

**⚠️ 중요: Artifact 정보를 반드시 고려하세요!**

- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - **코드 블록이 있으면**: artifact 타입 가능성 매우 높음
  - **파일 경로가 있으면**: artifact 타입 가능성 높음
  - 키워드: "스크립트 작성", "코드 수정", "파일 생성", "파일 수정"
  - 예: "분석을 위해 스크립트를 작성합니다" + 코드 블록 → **artifact**
  - 예: "코드를 수정합니다" + 코드 블록 → **artifact**

- **status_review**: 독립적인 상태 점검 (맥락과 무관)
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

- **plan**: 새로운 작업 시작 (독립적인 계획)
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

- **debug**: 문제 해결 과정 (에러, 원인, 해결, 검증)
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

...

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약, 핵심 동작과 상태 정보 포함]"""
    
    user_content = turn.body[:2000]
    if artifact_info:
        user_content += f"\n\n{artifact_info}"  # Artifact 정보도 포함
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_content,
            },
        ],
        max_tokens=200,
        temperature=0.3,
    )
    
    # ... (응답 파싱) ...
```

```plaintext
# backend/core/llm_service.py 수정

def classify_and_summarize_with_llm(...):
    # 캐시 키 생성 시 Artifact 정보도 포함
    text_content = turn.body[:2000]
    
    # Artifact 정보를 캐시 키에 포함
    artifact_hash = ""
    if turn.code_blocks:
        artifact_hash += f"_code_{len(turn.code_blocks)}"
    if turn.path_candidates:
        artifact_hash += f"_path_{len(turn.path_candidates)}"
    
    text_hash = _generate_text_hash(text_content + artifact_hash, max_length=2000)
    cache_key = f"llm_{text_hash}"
    
    # ... (나머지 로직) ...
```

```python
# backend/core/llm_service.py 수정

def classify_and_summarize_with_llm(...):
    # 캐시 키 생성 시 Artifact 정보도 포함
    text_content = turn.body[:2000]
    
    # Artifact 정보를 캐시 키에 포함
    artifact_hash = ""
    if turn.code_blocks:
        artifact_hash += f"_code_{len(turn.code_blocks)}"
    if turn.path_candidates:
        artifact_hash += f"_path_{len(turn.path_candidates)}"
    
    text_hash = _generate_text_hash(text_content + artifact_hash, max_length=2000)
    cache_key = f"llm_{text_hash}"
    
    # ... (나머지 로직) ...
```

```python
# backend/core/llm_service.py 수정

def classify_and_summarize_with_llm(...):
    # 캐시 키 생성 시 Artifact 정보도 포함
    text_content = turn.body[:2000]
    
    # Artifact 정보를 캐시 키에 포함
    artifact_hash = ""
    if turn.code_blocks:
        artifact_hash += f"_code_{len(turn.code_blocks)}"
    if turn.path_candidates:
        artifact_hash += f"_path_{len(turn.path_candidates)}"
    
    text_hash = _generate_text_hash(text_content + artifact_hash, max_length=2000)
    cache_key = f"llm_{text_hash}"
    
    # ... (나머지 로직) ...
```

---

**User**

Phase 2 파싱의 결과는 어디에 저장되어 있나요?

---

**Cursor**

Phase 2 파싱 결과 저장 위치 확인 중.


API 엔드포인트에서 파싱 결과 저장 방식을 확인 중.


저장된 파싱 결과 파일 하나를 확인 중.


## Phase 2 파싱 결과 저장 위치

### 1. 메모리 (일시적)
`parse_markdown()` 함수는 딕셔너리를 반환합니다:

```14:60:backend/parser/__init__.py
def parse_markdown(text: str, source_doc: str = "input.md") -> Dict:
    """
    마크다운 파일 전체 파싱
    
    Returns:
        {
            "session_meta": SessionMeta,
            "turns": List[Turn],
            "code_blocks": List[CodeBlock],
            "artifacts": List[str]
        }
    """
    # ... 파싱 로직 ...
    
    return {
        "session_meta": session_meta,
        "turns": turns,
        "code_blocks": all_code_blocks,
        "artifacts": list(set(all_paths)),
    }
```

- 함수 호출 시 메모리에만 존재
- 파일이나 데이터베이스에 자동 저장되지 않음

---

### 2. E2E 테스트 실행 시 파일 저장
E2E 테스트 실행 시 `tests/results/` 디렉토리에 JSON 파일로 저장됩니다:

```107:129:tests/test_parser_e2e.py
    # 상세 실행 결과 저장 (필수)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"parser_e2e_{timestamp}.json"

    detailed_results = {
        "session_meta": session_meta.model_dump(),
        "turns": [turn.model_dump() for turn in result["turns"]],
        "code_blocks": [block.model_dump() for block in result["code_blocks"]],
        "artifacts": result["artifacts"],
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "parser_e2e",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\n[RESULTS] Detailed results saved to: {results_file}")
```

저장 위치:
- 경로: `tests/results/parser_e2e_{timestamp}.json`
- 예시: `tests/results/parser_e2e_20251222_210334.json`

저장 내용:
- `session_meta`: 세션 메타데이터
- `turns`: 모든 Turn 객체 (body, code_blocks, path_candidates 포함)
- `code_blocks`: 모든 코드 블록
- `artifacts`: 모든 파일 경로 후보
- `test_metadata`: 테스트 메타데이터

---

### 3. Phase 3에서의 사용
Phase 3 이벤트 정규화에서는 파싱 결과를 직접 사용합니다:

```240:255:tests/test_event_normalizer_e2e.py
    # 2. 파싱 실행 (Phase 2 결과)
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 3. 이벤트 정규화 실행 (정규식 기반)
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )
```

- `parse_result["turns"]`: Phase 3 입력으로 사용
- `parse_result["session_meta"]`: 세션 메타데이터로 사용
- 파일에서 로드하지 않고, 메모리에서 직접 전달

---

### 4. API 엔드포인트 (미구현)
현재 API 엔드포인트는 구현되지 않았습니다:

```68:79:backend/main.py
# 라우터 등록
# Phase 6에서 실제 라우터 구현 예정
# 현재는 구조만 준비

# TODO: Phase 6에서 구현 예정
# from backend.api.routes import parse, timeline, issues, snippets, export
#
# app.include_router(parse.router)
# app.include_router(timeline.router)
# app.include_router(issues.router)
# app.include_router(snippets.router)
# app.include_router(export.router)
```

- Phase 6에서 `POST /api/parse` 엔드포인트 구현 예정
- 현재는 테스트에서만 사용

---

## 요약

| 저장 위치 | 상태 | 설명 |
|---|---|---|
| 메모리 | 항상 | `parse_markdown()` 반환값 (일시적) |
| 파일 저장 | 테스트 시 | `tests/results/parser_e2e_{timestamp}.json` |
| 데이터베이스 | 없음 | 현재 구현되지 않음 |
| API 엔드포인트 | 미구현 | Phase 6에서 구현 예정 |

---

## 실제 저장된 파일 예시

`tests/results/parser_e2e_20251222_210334.json` 파일 구조:

```json
{
  "session_meta": {
    "session_id": "cursor_export_unknown_1094",
    "exported_at": null,
    "cursor_version": null,
    "phase": 6,
    "subphase": 7,
    "source_doc": "..."
  },
  "turns": [
    {
      "turn_index": 0,
      "speaker": "Unknown",
      "body": "...",
      "code_blocks": [],
      "path_candidates": []
    },
    {
      "turn_index": 1,
      "speaker": "User",
      "body": "@TODOs.md 를 바탕으로...",
      "code_blocks": [],
      "path_candidates": ["TODOs.md"]
    },
    ...
  ],
  "code_blocks": [...],
  "artifacts": [...],
  "test_metadata": {...}
}
```

---

## 결론

- Phase 2 파싱 결과는 메모리에만 존재하며, 자동으로 파일에 저장되지 않습니다.
- E2E 테스트 실행 시에만 `tests/results/` 디렉토리에 JSON 파일로 저장됩니다.
- Phase 3에서는 파싱 결과를 메모리에서 직접 사용합니다.
- API 엔드포인트는 Phase 6에서 구현 예정입니다.

파싱 결과를 영구 저장하려면:
1. E2E 테스트 실행 후 `tests/results/` 디렉토리의 JSON 파일 사용
2. 또는 Phase 6에서 API 엔드포인트 구현 시 데이터베이스 저장 기능 추가

```python
def parse_markdown(text: str, source_doc: str = "input.md") -> Dict:
    """
    마크다운 파일 전체 파싱
    
    Returns:
        {
            "session_meta": SessionMeta,
            "turns": List[Turn],
            "code_blocks": List[CodeBlock],
            "artifacts": List[str]
        }
    """
    # ... 파싱 로직 ...
    
    return {
        "session_meta": session_meta,
        "turns": turns,
        "code_blocks": all_code_blocks,
        "artifacts": list(set(all_paths)),
    }
```

```python
    # 상세 실행 결과 저장 (필수)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"parser_e2e_{timestamp}.json"

    detailed_results = {
        "session_meta": session_meta.model_dump(),
        "turns": [turn.model_dump() for turn in result["turns"]],
        "code_blocks": [block.model_dump() for block in result["code_blocks"]],
        "artifacts": result["artifacts"],
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "parser_e2e",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\n[RESULTS] Detailed results saved to: {results_file}")
```

```python
    # 2. 파싱 실행 (Phase 2 결과)
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 3. 이벤트 정규화 실행 (정규식 기반)
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )
```

```python
# 라우터 등록
# Phase 6에서 실제 라우터 구현 예정
# 현재는 구조만 준비

# TODO: Phase 6에서 구현 예정
# from backend.api.routes import parse, timeline, issues, snippets, export
#
# app.include_router(parse.router)
# app.include_router(timeline.router)
# app.include_router(issues.router)
# app.include_router(snippets.router)
# app.include_router(export.router)
```

```json
{
  "session_meta": {
    "session_id": "cursor_export_unknown_1094",
    "exported_at": null,
    "cursor_version": null,
    "phase": 6,
    "subphase": 7,
    "source_doc": "..."
  },
  "turns": [
    {
      "turn_index": 0,
      "speaker": "Unknown",
      "body": "...",
      "code_blocks": [],
      "path_candidates": []
    },
    {
      "turn_index": 1,
      "speaker": "User",
      "body": "@TODOs.md 를 바탕으로...",
      "code_blocks": [],
      "path_candidates": ["TODOs.md"]
    },
    ...
  ],
  "code_blocks": [...],
  "artifacts": [...],
  "test_metadata": {...}
}
```

---

**User**

알겠습니다. 
그럼 위에서 제시한 개선 계획 (Phase2의 파싱 결과 artifact 반영도 포함)을 실행해주세요
단계별로 실행

---

**Cursor**

단계별로 진행합니다. 먼저 현재 코드 상태를 확인합니다.


1단계: LLM 서비스에 Artifact 정보 포함


```python
"""
LLM 서비스 모듈

gpt-4.1-mini를 사용하여 이벤트 타입 분류 및 요약 생성
"""

import logging
import threading
import time
import os
from typing import Dict
from dotenv import load_dotenv

# .env 파일 자동 로드
load_dotenv()

from backend.core.models import Turn, EventType
from backend.core.cache import (
    get_cached_result,
    save_cached_result,
    CACHE_DIR,
    _generate_text_hash,
    get_cache_stats as get_cache_dir_stats
)
from backend.builders.event_normalizer import summarize_turn

# 로거 설정
logger = logging.getLogger(__name__)

# 실행 중 캐시 통계 추적 (thread-safe)
_cache_stats = {"hits": 0, "misses": 0, "saves": 0}
_cache_stats_lock = threading.Lock()

# LLM 설정 상수
LLM_TIMEOUT = 120  # OpenAI API 타임아웃 (초)
LLM_MAX_RETRIES = 3  # 최대 재시도 횟수


def get_cache_stats() -> dict:
    """
    현재 캐시 통계 반환 (개선 버전: 디렉토리 통계 포함)

    Returns:
        캐시 통계 딕셔너리 (hits, misses, saves, hit_rate, cache_directory, total_files 등)
    """
    with _cache_stats_lock:
        stats = _cache_stats.copy()

        # 디렉토리 통계 추가
        dir_stats = get_cache_dir_stats()
        stats.update(dir_stats)

        # 히트율 계산
        total_requests = stats["hits"] + stats["misses"]
        if total_requests > 0:
            stats["hit_rate"] = stats["hits"] / total_requests
        else:
            stats["hit_rate"] = 0.0

        return stats


def reset_cache_stats() -> None:
    """캐시 통계 초기화"""
    with _cache_stats_lock:
        _cache_stats["hits"] = 0
        _cache_stats["misses"] = 0
        _cache_stats["saves"] = 0


def classify_and_summarize_with_llm(
    turn: Turn, 
    context_info: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (개선 버전: Artifact 정보 및 맥락 포함)

    개선 사항:
    1. 결정적 해시 함수 사용 (SHA-256)
    2. 텍스트 해시 검증으로 충돌 감지
    3. Fallback 시에도 캐시 저장
    4. 캐시 메타데이터 추가
    5. Artifact 정보(code_blocks, path_candidates) 포함
    6. 맥락 정보(context_info) 포함

    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)
            - recent_turn_count: 최근 Turn 개수
            - recent_summaries: 최근 Turn 요약 리스트
            - is_debug_context: debug 맥락 여부
            - is_plan_context: plan 맥락 여부

    Returns:
        {
            "event_type": EventType,
            "summary": str
        }

    비용 분석:
    - 입력: $0.40 per 1M tokens
    - 출력: $1.60 per 1M tokens
    - 평균 500자 텍스트 → 약 125 tokens
    - 평균 응답 (타입 + 요약) → 약 30 tokens
    - 비용: (125 * 0.40 + 30 * 1.60) / 1M = $0.000098 per Turn
    - 캐싱 적용 시: 70-80% 절감 → $0.0000196-0.0000294 per Turn
    """
    # 1. Artifact 정보 수집
    artifact_info = ""
    if turn.code_blocks:
        artifact_info += f"\n## 코드 블록 정보\n"
        artifact_info += f"- 코드 블록 개수: {len(turn.code_blocks)}\n"
        for i, block in enumerate(turn.code_blocks[:3], 1):  # 최대 3개만
            artifact_info += f"- 코드 블록 {i}: 언어={block.lang}, 길이={len(block.code)}자\n"
    
    if turn.path_candidates:
        artifact_info += f"\n## 파일 경로 정보\n"
        artifact_info += f"- 파일 경로: {', '.join(turn.path_candidates[:5])}\n"  # 최대 5개만
    
    # 2. 맥락 정보 수집
    context_prompt = ""
    if context_info:
        context_prompt = f"""
## 이전 Turn 맥락 정보

최근 {context_info.get('recent_turn_count', 0)}개 Turn의 요약:
"""
        for i, summary in enumerate(context_info.get('recent_summaries', []), 1):
            context_prompt += f"- Turn {i}: {summary}\n"
        
        if context_info.get('is_debug_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 debug 과정이 진행 중입니다. 현재 Turn도 debug 맥락 안에서 이루어질 가능성이 높습니다.\n"
        
        if context_info.get('is_plan_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 계획 수립이 진행 중입니다.\n"
    
    # 3. 결정적 캐시 키 생성 (SHA-256 사용, Artifact 정보 포함)
    text_content = turn.body[:2000]  # 충분한 길이로 확장
    
    # Artifact 정보를 캐시 키에 포함
    artifact_hash = ""
    if turn.code_blocks:
        artifact_hash += f"_code_{len(turn.code_blocks)}"
    if turn.path_candidates:
        artifact_hash += f"_path_{len(turn.path_candidates)}"
    
    # 맥락 정보도 캐시 키에 포함 (있는 경우)
    context_hash = ""
    if context_info:
        context_hash = f"_ctx_{hash(str(context_info.get('recent_summaries', []))[:100]) % 10000}"
    
    text_hash = _generate_text_hash(text_content + artifact_hash + context_hash, max_length=2000)
    cache_key = f"llm_{text_hash}"
    cache_file = CACHE_DIR / f"{cache_key}.json"

    logger.debug(
        f"[CACHE] Turn {turn.turn_index}: cache_key={cache_key}, "
        f"text_hash={text_hash}, file_exists={cache_file.exists()}"
    )

    # 2. 캐시 확인 (텍스트 해시 검증 포함)
    cached = get_cached_result(cache_key, text_hash=text_hash)
    if cached:
        with _cache_stats_lock:
            _cache_stats["hits"] += 1
        logger.info(f"[CACHE HIT] Turn {turn.turn_index}: cache_key={cache_key}")
        return {
            "event_type": EventType(cached["event_type"]),
            "summary": cached["summary"],
        }

    # 3. 캐시 미스
    with _cache_stats_lock:
        _cache_stats["misses"] += 1
    logger.info(f"[CACHE MISS] Turn {turn.turn_index}: cache_key={cache_key}, calling LLM")

    # LLM 호출 (재시도 로직 포함)
    from openai import OpenAI

    # API 키 가져오기
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key, timeout=LLM_TIMEOUT)

    # 재시도 로직 (지수 백오프)
    last_error = None
    for attempt in range(LLM_MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",  # 사용자 지시대로 정확히 사용
                messages=[
                    {
                        "role": "system",
                        "content": """다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

이벤트 타입 선택지:
- status_review: 상태 리뷰 (현황 점검, 상태 확인)
- plan: 계획 수립 (작업 계획, 단계별 계획)
- artifact: 파일/경로 관련 (파일 생성/수정/언급)
- debug: 디버깅 (에러, 원인, 해결, 검증)
- completion: 완료 (작업 완료, 성공)
- next_step: 다음 단계 (다음 작업, 진행)
- turn: 일반 대화 (기본값)

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약]""",
                    },
                    {
                        "role": "user",
                        "content": turn.body[:2000],  # 토큰 절감
                    },
                ],
                max_tokens=150,  # 타입 + 요약
                temperature=0.3,  # 일관성 유지
            )

            result_text = response.choices[0].message.content.strip()

            # 응답 파싱
            event_type_str = None
            summary = None

            for line in result_text.split("\n"):
                if line.startswith("TYPE:"):
                    event_type_str = line.replace("TYPE:", "").strip().lower()
                elif line.startswith("SUMMARY:"):
                    summary = line.replace("SUMMARY:", "").strip()

            # 타입 검증
            try:
                event_type = EventType(event_type_str) if event_type_str else EventType.TURN
            except ValueError:
                event_type = EventType.TURN

            # 요약이 없으면 기본 요약 (정규식 기반)
            if not summary:
                summary = summarize_turn(turn)

            result = {
                "event_type": event_type.value,
                "summary": summary,
            }

            # 5. 캐시 저장 (텍스트 해시 포함)
            save_cached_result(
                cache_key,
                result,
                text_hash=text_hash,
                turn_index=turn.turn_index
            )
            with _cache_stats_lock:
                _cache_stats["saves"] += 1
            logger.info(f"[CACHE SAVE] Turn {turn.turn_index}: cache_key={cache_key}")

            return {
                "event_type": event_type,
                "summary": summary,
            }

        # 모든 예외 처리 (타임아웃, Rate limit, 일시적 오류 등)
        except Exception as e:
            last_error = e
            error_type = type(e).__name__

            # 마지막 시도가 아니면 재시도
            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt  # 지수 백오프: 1초, 2초, 4초
                logger.warning(
                    f"[WARNING] LLM call attempt {attempt + 1}/{LLM_MAX_RETRIES} failed for Turn {turn.turn_index}: "
                    f"{error_type}: {str(e)[:100]}, retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                # 모든 재시도 실패 시 에러 로그 및 fallback
                logger.error(
                    f"[ERROR] LLM call failed after {LLM_MAX_RETRIES} attempts for Turn {turn.turn_index}: "
                    f"{error_type}: {str(e)[:200]}"
                )
                # 6. 모든 재시도 실패 시 Fallback (캐시 저장 포함)
                logger.info(
                    f"[FALLBACK] Using regex-based event generation for Turn {turn.turn_index}"
                )

                summary = summarize_turn(turn)
                result = {
                    "event_type": EventType.TURN.value,
                    "summary": summary,
                }

                # ✅ Fallback 결과도 캐시 저장 (중요!)
                save_cached_result(
                    cache_key,
                    result,
                    text_hash=text_hash,
                    turn_index=turn.turn_index
                )
                with _cache_stats_lock:
                    _cache_stats["saves"] += 1
                logger.info(
                    f"[CACHE SAVE] Turn {turn.turn_index}: cache_key={cache_key} (fallback)"
                )

                return {
                    "event_type": EventType.TURN,
                    "summary": summary,
                }

    # 모든 재시도 실패 시 마지막 오류를 다시 발생시킴 (fallback 후에는 도달하지 않음)
    raise last_error

```

프롬프트에 Artifact 정보와 맥락 정보를 포함하도록 수정 중.


```python
"""
LLM 서비스 모듈

gpt-4.1-mini를 사용하여 이벤트 타입 분류 및 요약 생성
"""

import logging
import threading
import time
import os
from typing import Dict, Optional
from dotenv import load_dotenv

# .env 파일 자동 로드
load_dotenv()

from backend.core.models import Turn, EventType
from backend.core.cache import (
    get_cached_result,
    save_cached_result,
    CACHE_DIR,
    _generate_text_hash,
    get_cache_stats as get_cache_dir_stats
)
from backend.builders.event_normalizer import summarize_turn

# 로거 설정
logger = logging.getLogger(__name__)

# 실행 중 캐시 통계 추적 (thread-safe)
_cache_stats = {"hits": 0, "misses": 0, "saves": 0}
_cache_stats_lock = threading.Lock()

# LLM 설정 상수
LLM_TIMEOUT = 120  # OpenAI API 타임아웃 (초)
LLM_MAX_RETRIES = 3  # 최대 재시도 횟수


def get_cache_stats() -> dict:
    """
    현재 캐시 통계 반환 (개선 버전: 디렉토리 통계 포함)

    Returns:
        캐시 통계 딕셔너리 (hits, misses, saves, hit_rate, cache_directory, total_files 등)
    """
    with _cache_stats_lock:
        stats = _cache_stats.copy()

        # 디렉토리 통계 추가
        dir_stats = get_cache_dir_stats()
        stats.update(dir_stats)

        # 히트율 계산
        total_requests = stats["hits"] + stats["misses"]
        if total_requests > 0:
            stats["hit_rate"] = stats["hits"] / total_requests
        else:
            stats["hit_rate"] = 0.0

        return stats


def reset_cache_stats() -> None:
    """캐시 통계 초기화"""
    with _cache_stats_lock:
        _cache_stats["hits"] = 0
        _cache_stats["misses"] = 0
        _cache_stats["saves"] = 0


def classify_and_summarize_with_llm(
    turn: Turn, 
    context_info: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (개선 버전: Artifact 정보 및 맥락 포함)

    개선 사항:
    1. 결정적 해시 함수 사용 (SHA-256)
    2. 텍스트 해시 검증으로 충돌 감지
    3. Fallback 시에도 캐시 저장
    4. 캐시 메타데이터 추가
    5. Artifact 정보(code_blocks, path_candidates) 포함
    6. 맥락 정보(context_info) 포함

    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)
            - recent_turn_count: 최근 Turn 개수
            - recent_summaries: 최근 Turn 요약 리스트
            - is_debug_context: debug 맥락 여부
            - is_plan_context: plan 맥락 여부

    Returns:
        {
            "event_type": EventType,
            "summary": str
        }

    비용 분석:
    - 입력: $0.40 per 1M tokens
    - 출력: $1.60 per 1M tokens
    - 평균 500자 텍스트 → 약 125 tokens
    - 평균 응답 (타입 + 요약) → 약 30 tokens
    - 비용: (125 * 0.40 + 30 * 1.60) / 1M = $0.000098 per Turn
    - 캐싱 적용 시: 70-80% 절감 → $0.0000196-0.0000294 per Turn
    """
    # 1. Artifact 정보 수집
    artifact_info = ""
    if turn.code_blocks:
        artifact_info += f"\n## 코드 블록 정보\n"
        artifact_info += f"- 코드 블록 개수: {len(turn.code_blocks)}\n"
        for i, block in enumerate(turn.code_blocks[:3], 1):  # 최대 3개만
            artifact_info += f"- 코드 블록 {i}: 언어={block.lang}, 길이={len(block.code)}자\n"
    
    if turn.path_candidates:
        artifact_info += f"\n## 파일 경로 정보\n"
        artifact_info += f"- 파일 경로: {', '.join(turn.path_candidates[:5])}\n"  # 최대 5개만
    
    # 2. 맥락 정보 수집
    context_prompt = ""
    if context_info:
        context_prompt = f"""
## 이전 Turn 맥락 정보

최근 {context_info.get('recent_turn_count', 0)}개 Turn의 요약:
"""
        for i, summary in enumerate(context_info.get('recent_summaries', []), 1):
            context_prompt += f"- Turn {i}: {summary}\n"
        
        if context_info.get('is_debug_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 debug 과정이 진행 중입니다. 현재 Turn도 debug 맥락 안에서 이루어질 가능성이 높습니다.\n"
        
        if context_info.get('is_plan_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 계획 수립이 진행 중입니다.\n"
    
    # 3. 결정적 캐시 키 생성 (SHA-256 사용, Artifact 정보 포함)
    text_content = turn.body[:2000]  # 충분한 길이로 확장
    
    # Artifact 정보를 캐시 키에 포함
    artifact_hash = ""
    if turn.code_blocks:
        artifact_hash += f"_code_{len(turn.code_blocks)}"
    if turn.path_candidates:
        artifact_hash += f"_path_{len(turn.path_candidates)}"
    
    # 맥락 정보도 캐시 키에 포함 (있는 경우)
    context_hash = ""
    if context_info:
        context_hash = f"_ctx_{hash(str(context_info.get('recent_summaries', []))[:100]) % 10000}"
    
    text_hash = _generate_text_hash(text_content + artifact_hash + context_hash, max_length=2000)
    cache_key = f"llm_{text_hash}"
    cache_file = CACHE_DIR / f"{cache_key}.json"

    logger.debug(
        f"[CACHE] Turn {turn.turn_index}: cache_key={cache_key}, "
        f"text_hash={text_hash}, file_exists={cache_file.exists()}"
    )

    # 2. 캐시 확인 (텍스트 해시 검증 포함)
    cached = get_cached_result(cache_key, text_hash=text_hash)
    if cached:
        with _cache_stats_lock:
            _cache_stats["hits"] += 1
        logger.info(f"[CACHE HIT] Turn {turn.turn_index}: cache_key={cache_key}")
        return {
            "event_type": EventType(cached["event_type"]),
            "summary": cached["summary"],
        }

    # 3. 캐시 미스
    with _cache_stats_lock:
        _cache_stats["misses"] += 1
    logger.info(f"[CACHE MISS] Turn {turn.turn_index}: cache_key={cache_key}, calling LLM")

    # LLM 호출 (재시도 로직 포함)
    from openai import OpenAI

    # API 키 가져오기
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key, timeout=LLM_TIMEOUT)

    # 재시도 로직 (지수 백오프)
    last_error = None
    for attempt in range(LLM_MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",  # 사용자 지시대로 정확히 사용
                messages=[
                    {
                        "role": "system",
                        "content": """다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

이벤트 타입 선택지:
- status_review: 상태 리뷰 (현황 점검, 상태 확인)
- plan: 계획 수립 (작업 계획, 단계별 계획)
- artifact: 파일/경로 관련 (파일 생성/수정/언급)
- debug: 디버깅 (에러, 원인, 해결, 검증)
- completion: 완료 (작업 완료, 성공)
- next_step: 다음 단계 (다음 작업, 진행)
- turn: 일반 대화 (기본값)

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약]""",
                    },
                    {
                        "role": "user",
                        "content": turn.body[:2000],  # 토큰 절감
                    },
                ],
                max_tokens=150,  # 타입 + 요약
                temperature=0.3,  # 일관성 유지
            )

            result_text = response.choices[0].message.content.strip()

            # 응답 파싱
            event_type_str = None
            summary = None

            for line in result_text.split("\n"):
                if line.startswith("TYPE:"):
                    event_type_str = line.replace("TYPE:", "").strip().lower()
                elif line.startswith("SUMMARY:"):
                    summary = line.replace("SUMMARY:", "").strip()

            # 타입 검증
            try:
                event_type = EventType(event_type_str) if event_type_str else EventType.TURN
            except ValueError:
                event_type = EventType.TURN

            # 요약이 없으면 기본 요약 (정규식 기반)
            if not summary:
                summary = summarize_turn(turn)

            result = {
                "event_type": event_type.value,
                "summary": summary,
            }

            # 5. 캐시 저장 (텍스트 해시 포함)
            save_cached_result(
                cache_key,
                result,
                text_hash=text_hash,
                turn_index=turn.turn_index
            )
            with _cache_stats_lock:
                _cache_stats["saves"] += 1
            logger.info(f"[CACHE SAVE] Turn {turn.turn_index}: cache_key={cache_key}")

            return {
                "event_type": event_type,
                "summary": summary,
            }

        # 모든 예외 처리 (타임아웃, Rate limit, 일시적 오류 등)
        except Exception as e:
            last_error = e
            error_type = type(e).__name__

            # 마지막 시도가 아니면 재시도
            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt  # 지수 백오프: 1초, 2초, 4초
                logger.warning(
                    f"[WARNING] LLM call attempt {attempt + 1}/{LLM_MAX_RETRIES} failed for Turn {turn.turn_index}: "
                    f"{error_type}: {str(e)[:100]}, retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                # 모든 재시도 실패 시 에러 로그 및 fallback
                logger.error(
                    f"[ERROR] LLM call failed after {LLM_MAX_RETRIES} attempts for Turn {turn.turn_index}: "
                    f"{error_type}: {str(e)[:200]}"
                )
                # 6. 모든 재시도 실패 시 Fallback (캐시 저장 포함)
                logger.info(
                    f"[FALLBACK] Using regex-based event generation for Turn {turn.turn_index}"
                )

                summary = summarize_turn(turn)
                result = {
                    "event_type": EventType.TURN.value,
                    "summary": summary,
                }

                # ✅ Fallback 결과도 캐시 저장 (중요!)
                save_cached_result(
                    cache_key,
                    result,
                    text_hash=text_hash,
                    turn_index=turn.turn_index
                )
                with _cache_stats_lock:
                    _cache_stats["saves"] += 1
                logger.info(
                    f"[CACHE SAVE] Turn {turn.turn_index}: cache_key={cache_key} (fallback)"
                )

                return {
                    "event_type": EventType.TURN,
                    "summary": summary,
                }

    # 모든 재시도 실패 시 마지막 오류를 다시 발생시킴 (fallback 후에는 도달하지 않음)
    raise last_error

```

```python
"""
LLM 서비스 모듈

gpt-4.1-mini를 사용하여 이벤트 타입 분류 및 요약 생성
"""

import logging
import threading
import time
import os
from typing import Dict, Optional
from dotenv import load_dotenv

# .env 파일 자동 로드
load_dotenv()

from backend.core.models import Turn, EventType
from backend.core.cache import (
    get_cached_result,
    save_cached_result,
    CACHE_DIR,
    _generate_text_hash,
    get_cache_stats as get_cache_dir_stats
)
from backend.builders.event_normalizer import summarize_turn

# 로거 설정
logger = logging.getLogger(__name__)

# 실행 중 캐시 통계 추적 (thread-safe)
_cache_stats = {"hits": 0, "misses": 0, "saves": 0}
_cache_stats_lock = threading.Lock()

# LLM 설정 상수
LLM_TIMEOUT = 120  # OpenAI API 타임아웃 (초)
LLM_MAX_RETRIES = 3  # 최대 재시도 횟수


def get_cache_stats() -> dict:
    """
    현재 캐시 통계 반환 (개선 버전: 디렉토리 통계 포함)

    Returns:
        캐시 통계 딕셔너리 (hits, misses, saves, hit_rate, cache_directory, total_files 등)
    """
    with _cache_stats_lock:
        stats = _cache_stats.copy()

        # 디렉토리 통계 추가
        dir_stats = get_cache_dir_stats()
        stats.update(dir_stats)

        # 히트율 계산
        total_requests = stats["hits"] + stats["misses"]
        if total_requests > 0:
            stats["hit_rate"] = stats["hits"] / total_requests
        else:
            stats["hit_rate"] = 0.0

        return stats


def reset_cache_stats() -> None:
    """캐시 통계 초기화"""
    with _cache_stats_lock:
        _cache_stats["hits"] = 0
        _cache_stats["misses"] = 0
        _cache_stats["saves"] = 0


def classify_and_summarize_with_llm(
    turn: Turn, 
    context_info: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (개선 버전: Artifact 정보 및 맥락 포함)

    개선 사항:
    1. 결정적 해시 함수 사용 (SHA-256)
    2. 텍스트 해시 검증으로 충돌 감지
    3. Fallback 시에도 캐시 저장
    4. 캐시 메타데이터 추가
    5. Artifact 정보(code_blocks, path_candidates) 포함
    6. 맥락 정보(context_info) 포함

    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)
            - recent_turn_count: 최근 Turn 개수
            - recent_summaries: 최근 Turn 요약 리스트
            - is_debug_context: debug 맥락 여부
            - is_plan_context: plan 맥락 여부

    Returns:
        {
            "event_type": EventType,
            "summary": str
        }

    비용 분석:
    - 입력: $0.40 per 1M tokens
    - 출력: $1.60 per 1M tokens
    - 평균 500자 텍스트 → 약 125 tokens
    - 평균 응답 (타입 + 요약) → 약 30 tokens
    - 비용: (125 * 0.40 + 30 * 1.60) / 1M = $0.000098 per Turn
    - 캐싱 적용 시: 70-80% 절감 → $0.0000196-0.0000294 per Turn
    """
    # 1. Artifact 정보 수집
    artifact_info = ""
    if turn.code_blocks:
        artifact_info += f"\n## 코드 블록 정보\n"
        artifact_info += f"- 코드 블록 개수: {len(turn.code_blocks)}\n"
        for i, block in enumerate(turn.code_blocks[:3], 1):  # 최대 3개만
            artifact_info += f"- 코드 블록 {i}: 언어={block.lang}, 길이={len(block.code)}자\n"
    
    if turn.path_candidates:
        artifact_info += f"\n## 파일 경로 정보\n"
        artifact_info += f"- 파일 경로: {', '.join(turn.path_candidates[:5])}\n"  # 최대 5개만
    
    # 2. 맥락 정보 수집
    context_prompt = ""
    if context_info:
        context_prompt = f"""
## 이전 Turn 맥락 정보

최근 {context_info.get('recent_turn_count', 0)}개 Turn의 요약:
"""
        for i, summary in enumerate(context_info.get('recent_summaries', []), 1):
            context_prompt += f"- Turn {i}: {summary}\n"
        
        if context_info.get('is_debug_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 debug 과정이 진행 중입니다. 현재 Turn도 debug 맥락 안에서 이루어질 가능성이 높습니다.\n"
        
        if context_info.get('is_plan_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 계획 수립이 진행 중입니다.\n"
    
    # 3. 결정적 캐시 키 생성 (SHA-256 사용, Artifact 정보 포함)
    text_content = turn.body[:2000]  # 충분한 길이로 확장
    
    # Artifact 정보를 캐시 키에 포함
    artifact_hash = ""
    if turn.code_blocks:
        artifact_hash += f"_code_{len(turn.code_blocks)}"
    if turn.path_candidates:
        artifact_hash += f"_path_{len(turn.path_candidates)}"
    
    # 맥락 정보도 캐시 키에 포함 (있는 경우)
    context_hash = ""
    if context_info:
        context_hash = f"_ctx_{hash(str(context_info.get('recent_summaries', []))[:100]) % 10000}"
    
    text_hash = _generate_text_hash(text_content + artifact_hash + context_hash, max_length=2000)
    cache_key = f"llm_{text_hash}"
    cache_file = CACHE_DIR / f"{cache_key}.json"

    logger.debug(
        f"[CACHE] Turn {turn.turn_index}: cache_key={cache_key}, "
        f"text_hash={text_hash}, file_exists={cache_file.exists()}"
    )

    # 2. 캐시 확인 (텍스트 해시 검증 포함)
    cached = get_cached_result(cache_key, text_hash=text_hash)
    if cached:
        with _cache_stats_lock:
            _cache_stats["hits"] += 1
        logger.info(f"[CACHE HIT] Turn {turn.turn_index}: cache_key={cache_key}")
        return {
            "event_type": EventType(cached["event_type"]),
            "summary": cached["summary"],
        }

    # 3. 캐시 미스
    with _cache_stats_lock:
        _cache_stats["misses"] += 1
    logger.info(f"[CACHE MISS] Turn {turn.turn_index}: cache_key={cache_key}, calling LLM")

    # LLM 호출 (재시도 로직 포함)
    from openai import OpenAI

    # API 키 가져오기
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key, timeout=LLM_TIMEOUT)

    # 재시도 로직 (지수 백오프)
    last_error = None
    for attempt in range(LLM_MAX_RETRIES):
        try:
            # System 프롬프트 생성 (Artifact 정보 및 맥락 포함)
            system_prompt = f"""다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

{context_prompt}

{artifact_info}

## 이벤트 타입 선택지 및 구분 기준

**⚠️ 중요**: 맥락 정보와 Artifact 정보를 반드시 고려하세요!

- **status_review**: 독립적인 상태 점검 (맥락과 무관한 상태 확인)
  - 예: "프로젝트 현황을 파악합니다", "진행 상황을 확인합니다"
  - ⚠️ 주의: debug 맥락 안에서의 상태 확인은 debug 타입이 더 적합할 수 있음
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

- **plan**: 새로운 작업 시작 (독립적인 계획 수립)
  - 예: "다음 작업을 계획합니다", "단계별 계획을 수립합니다"
  - ⚠️ 주의: debug 맥락 안에서의 계획은 debug 타입이 더 적합할 수 있음
  - ⚠️ 주의: 코드 블록이 있으면 artifact 타입이 더 적합할 수 있음

- **artifact**: 파일 생성/수정/실행 (스크립트 생성, 코드 수정 포함)
  - **코드 블록이 있으면**: artifact 타입 가능성 매우 높음
  - **파일 경로가 있으면**: artifact 타입 가능성 높음
  - 예: "스크립트를 작성합니다" + 코드 블록 → **artifact**
  - 예: "코드를 수정합니다" + 코드 블록 → **artifact**
  - 키워드: "스크립트 작성", "코드 수정", "파일 생성", "파일 수정"

- **debug**: 문제 해결 과정 (에러, 원인, 해결, 검증)
  - 예: "원인을 분석합니다", "문제를 해결합니다", "에러를 확인합니다"
  - ⚠️ 중요: 이전 Turn에 debug 맥락이 있으면 현재 Turn도 debug 가능성 높음
  - ⚠️ 중요: debug 맥락 안에서의 상태 확인, 계획, 코드 수정도 debug 타입 고려

- **completion**: 완료 (작업 완료, 성공)
  - 예: "작업이 완료되었습니다", "성공적으로 완료했습니다"

- **next_step**: 다음 단계 (다음 작업, 진행)
  - 예: "다음 단계로 진행합니다", "다음 작업을 시작합니다"

- **turn**: 일반 대화 (기본값, 위 타입에 해당하지 않을 때)

## 타입 분류 우선순위

1. **Artifact 우선**: 코드 블록이나 파일 경로가 있으면 artifact 타입 우선 고려
2. **맥락 우선**: 이전 Turn의 맥락을 먼저 고려
   - 이전 Turn에 debug가 있으면 → 현재 Turn도 debug 가능성 높음
   - 이전 Turn에 plan이 있고 현재 Turn이 실행 단계면 → artifact 가능성 높음
3. **키워드 기반**: 현재 Turn의 키워드로 타입 판단
4. **기본값**: 위 조건에 해당하지 않으면 turn

## 요약 생성 규칙

**핵심 원칙**:
1. **핵심 동작 포함**: 무엇을 하는가 (동작 중심)
2. **상태 정보 포함**: 진행중/완료/요청 등 상태 명시
3. **중요 세부사항 포함**: 파일명, 수치, 변경사항 등
4. **이전 Turn과의 연관성**: 이전 Turn과 연관이 있으면 언급

**특수 기호 의미**:
- **@**: 첨부 자료 또는 참조 대상 (예: @TODOs.md → "TODOs.md 파일을 참조")
- **#**: 파일명, 항목 번호 등 (예: # Phase 6 → "Phase 6")
- **`**: 코드나 파일명 (예: `main.py` → "main.py 파일")

**요약 예시**:
- ❌ 나쁜 예: "프로젝트 현황을 파악합니다."
- ✅ 좋은 예: "TODOs.md 파일을 참조하여 프로젝트의 현재 진행 상황과 남은 작업들을 파악합니다."

- ❌ 나쁜 예: "변경사항을 확인합니다."
- ✅ 좋은 예: "기본 피드백 생성 로직 추가 완료 후, Git 커밋 진행합니다."

**요약 길이**: 150-200자 (의미 있는 단위로 자르기, 문장 중간 자르기 금지)

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약, 핵심 동작과 상태 정보 포함]"""

            # User 프롬프트 생성 (Artifact 정보 포함)
            user_content = turn.body[:2000]
            if artifact_info:
                user_content += f"\n\n{artifact_info}"

            response = client.chat.completions.create(
                model="gpt-4.1-mini",  # 사용자 지시대로 정확히 사용
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_content,
                    },
                ],
                max_tokens=200,  # 150 → 200으로 증가 (요약 품질 개선)
                temperature=0.3,  # 일관성 유지
            )

            result_text = response.choices[0].message.content.strip()

            # 응답 파싱
            event_type_str = None
            summary = None

            for line in result_text.split("\n"):
                if line.startswith("TYPE:"):
                    event_type_str = line.replace("TYPE:", "").strip().lower()
                elif line.startswith("SUMMARY:"):
                    summary = line.replace("SUMMARY:", "").strip()

            # 타입 검증
            try:
                event_type = EventType(event_type_str) if event_type_str else EventType.TURN
            except ValueError:
                event_type = EventType.TURN

            # 요약이 없으면 기본 요약 (정규식 기반)
            if not summary:
                summary = summarize_turn(turn)

            result = {
                "event_type": event_type.value,
                "summary": summary,
            }

            # 5. 캐시 저장 (텍스트 해시 포함)
            save_cached_result(
                cache_key,
                result,
                text_hash=text_hash,
                turn_index=turn.turn_index
            )
            with _cache_stats_lock:
                _cache_stats["saves"] += 1
            logger.info(f"[CACHE SAVE] Turn {turn.turn_index}: cache_key={cache_key}")

            return {
                "event_type": event_type,
                "summary": summary,
            }

        # 모든 예외 처리 (타임아웃, Rate limit, 일시적 오류 등)
        except Exception as e:
            last_error = e
            error_type = type(e).__name__

            # 마지막 시도가 아니면 재시도
            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt  # 지수 백오프: 1초, 2초, 4초
                logger.warning(
                    f"[WARNING] LLM call attempt {attempt + 1}/{LLM_MAX_RETRIES} failed for Turn {turn.turn_index}: "
                    f"{error_type}: {str(e)[:100]}, retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                # 모든 재시도 실패 시 에러 로그 및 fallback
                logger.error(
                    f"[ERROR] LLM call failed after {LLM_MAX_RETRIES} attempts for Turn {turn.turn_index}: "
                    f"{error_type}: {str(e)[:200]}"
                )
                # 6. 모든 재시도 실패 시 Fallback (캐시 저장 포함)
                logger.info(
                    f"[FALLBACK] Using regex-based event generation for Turn {turn.turn_index}"
                )

                summary = summarize_turn(turn)
                result = {
                    "event_type": EventType.TURN.value,
                    "summary": summary,
                }

                # ✅ Fallback 결과도 캐시 저장 (중요!)
                save_cached_result(
                    cache_key,
                    result,
                    text_hash=text_hash,
                    turn_index=turn.turn_index
                )
                with _cache_stats_lock:
                    _cache_stats["saves"] += 1
                logger.info(
                    f"[CACHE SAVE] Turn {turn.turn_index}: cache_key={cache_key} (fallback)"
                )

                return {
                    "event_type": EventType.TURN,
                    "summary": summary,
                }

    # 모든 재시도 실패 시 마지막 오류를 다시 발생시킴 (fallback 후에는 도달하지 않음)
    raise last_error

```

2단계: 맥락 정보 수집 함수 구현 중.


```python
"""
이벤트 정규화 모듈

파싱된 Turn 데이터를 이벤트로 정규화합니다.
"""

import re
from typing import List, Optional, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from backend.core.models import Turn, Event, EventType, SessionMeta
from backend.core.constants import DEBUG_TRIGGERS


def normalize_turns_to_events(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None, use_llm: bool = False
) -> List[Event]:
    """
    Turn 리스트를 Event 리스트로 변환 (우선순위 기반 단일 이벤트, LLM 옵션)

    LLM 사용 시 병렬 처리 (max_workers=5)

    Args:
        turns: 파싱된 Turn 리스트
        session_meta: 세션 메타데이터 (Phase/Subphase 연결용, 선택)
        use_llm: LLM 사용 여부 (기본값: False, True 시 일괄 적용, 병렬 처리)

    Returns:
        정규화된 Event 리스트
    """
    if use_llm:
        # 병렬 처리 (ThreadPoolExecutor)
        events = _normalize_turns_to_events_parallel(turns, session_meta)
    else:
        # 순차 처리 (기존 로직)
        events = []
        for turn in turns:
            event = create_single_event_with_priority(turn, session_meta)
            events.append(event)

    # 시퀀스 번호 부여
    for i, event in enumerate(events):
        event.seq = i + 1

    return events


def _normalize_turns_to_events_parallel(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None
) -> List[Event]:
    """
    LLM 기반 이벤트 생성 (병렬 처리)

    Args:
        turns: Turn 리스트
        session_meta: 세션 메타데이터

    Returns:
        Event 리스트 (turn_index 순서 유지)
    """
    events_dict = {}  # turn_index -> Event 매핑

    with ThreadPoolExecutor(max_workers=5) as executor:
        # 각 Turn을 병렬로 처리
        future_to_turn = {
            executor.submit(create_event_with_llm, turn, session_meta): turn
            for turn in turns
        }

        # 완료된 작업부터 처리 (순서 보장을 위해 turn_index 저장)
        for future in as_completed(future_to_turn):
            turn = future_to_turn[future]
            try:
                event = future.result()
                events_dict[turn.turn_index] = event
            except Exception as e:
                # 에러 발생 시 기본 이벤트 생성 (fallback)
                # 로깅은 선택적 (필요시 추가)
                event = create_single_event_with_priority(turn, session_meta)
                events_dict[turn.turn_index] = event

    # turn_index 순서로 정렬
    events = [events_dict[turn.turn_index] for turn in turns]
    return events


def create_event_with_llm(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    LLM 기반 이벤트 생성 (gpt-4.1-mini)

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체 (processing_method="llm")
    """
    from backend.core.llm_service import classify_and_summarize_with_llm

    # LLM으로 타입 분류 및 요약 생성
    llm_result = classify_and_summarize_with_llm(turn)
    event_type = llm_result["event_type"]
    summary = llm_result["summary"]

    # Artifact 연결 (파일 경로가 있으면)
    artifacts = []
    if turn.path_candidates:
        artifacts = [{"path": path, "action": "mention"} for path in turn.path_candidates]

    # Snippet 참조 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summary,
        artifacts=artifacts,
        snippet_refs=snippet_refs,
        processing_method="llm",
    )


def create_single_event_with_priority(
    turn: Turn, session_meta: Optional[SessionMeta] = None
) -> Event:
    """
    우선순위 기반 단일 이벤트 생성

    우선순위 (높은 순서):
    1. DEBUG: 에러/원인/해결 관련 (가장 구체적)
    2. ARTIFACT: 파일 경로 존재
    3. COMPLETION: 완료 키워드
    4. PLAN: 계획 수립
    5. STATUS_REVIEW: 상태 리뷰
    6. NEXT_STEP: 다음 단계
    7. TURN: 기본

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체
    """
    # 1순위: DEBUG (디버그 트리거 + Cursor 발화)
    if is_debug_turn(turn):
        return create_debug_event(turn, session_meta)

    # 2순위: ARTIFACT (파일 경로 존재)
    if turn.path_candidates:
        return create_artifact_event(turn, session_meta)

    # 3순위: 특수 타입 (엄격한 정규식)
    event_type = classify_event_type_strict(turn)
    if event_type != EventType.TURN:
        return create_message_event(turn, event_type, session_meta)

    # 4순위: 기본 TURN
    return create_message_event(turn, EventType.TURN, session_meta)


def is_debug_turn(turn: Turn) -> bool:
    """
    디버그 Turn인지 판단

    Args:
        turn: Turn 객체

    Returns:
        디버그 Turn 여부
    """
    if turn.speaker != "Cursor":
        return False

    text = turn.body.lower()
    return any(trigger.search(text) for trigger in DEBUG_TRIGGERS.values())


def create_debug_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    DebugEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        DebugEvent 객체
    """
    # 스니펫 참조 생성 (Phase 5에서 실제 ID로 대체될 예정)
    # 현재는 turn_index와 block_index를 조합하여 임시 ID 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.DEBUG,
        summary=summarize_turn(turn),
        artifacts=[],  # 후속 단계에서 연결
        snippet_refs=snippet_refs,
        processing_method="regex",
    )


def create_artifact_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    ArtifactEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        ArtifactEvent 객체
    """
    # Artifact 정보 구성
    artifacts = [
        {"path": path, "action": "mention"}  # Phase 3에서는 mention만, Phase 4에서 확장
        for path in turn.path_candidates
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.ARTIFACT,
        summary=summarize_turn(turn),
        artifacts=artifacts,
        snippet_refs=[],
        processing_method="regex",
    )


def create_message_event(
    turn: Turn,
    event_type: Optional[EventType] = None,
    session_meta: Optional[SessionMeta] = None,
) -> Event:
    """
    MessageEvent 생성 (일반 Turn 이벤트)

    Args:
        turn: Turn 객체
        event_type: 이벤트 타입 (None이면 자동 분류)
        session_meta: 세션 메타데이터 (선택)

    Returns:
        MessageEvent 객체
    """
    # 이벤트 타입 결정 (기본은 TURN, 특정 키워드로 분류 가능)
    if event_type is None:
        event_type = classify_event_type_strict(turn)

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summarize_turn(turn),
        artifacts=[],
        snippet_refs=[],
        processing_method="regex",
    )


def classify_event_type_strict(turn: Turn) -> EventType:
    """
    엄격한 조건으로 이벤트 타입 분류 (정규식 기반)

    일반 단어 매칭을 피하기 위해 더 구체적인 패턴 사용

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    text = turn.body.lower()

    # COMPLETION: 완료 키워드 (더 구체적)
    if re.search(r"(?i)\b(완료되었|완료됨|완료했습니다|성공적으로 완료|작업 완료)\b", text):
        return EventType.COMPLETION

    # PLAN: 계획 수립 (더 구체적)
    if re.search(r"(?i)\b(계획을|계획은|계획하|작업 계획|단계별 계획|진행 계획)\b", text):
        return EventType.PLAN

    # STATUS_REVIEW: 상태 리뷰 (더 구체적)
    if re.search(r"(?i)\b(현황을 리뷰|상태를 확인|진행 상황을 점검|현황 점검|상태 리뷰)\b", text):
        return EventType.STATUS_REVIEW

    # NEXT_STEP: 다음 단계 (더 구체적)
    if re.search(r"(?i)\b(다음 단계는|다음 작업은|다음으로 진행|다음 단계로)\b", text):
        return EventType.NEXT_STEP

    # 기본값: TURN
    return EventType.TURN


def classify_event_type(turn: Turn) -> EventType:
    """
    Turn의 이벤트 타입 분류 (기존 함수, 호환성 유지)

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    # 엄격한 분류 함수 사용
    return classify_event_type_strict(turn)


def summarize_turn(turn: Turn) -> str:
    """
    Turn을 요약 (정규식 기반 개선 버전)

    Args:
        turn: Turn 객체

    Returns:
        요약 텍스트
    """
    body = turn.body.strip()

    # 1. 줄바꿈 정리 (연속된 \n을 최대 2개로 제한)
    body = re.sub(r"\n{3,}", "\n\n", body)

    # 2. 200자 이하면 그대로 반환
    if len(body) <= 200:
        return body

    # 3. 의미 있는 위치에서 자르기 (우선순위 순)

    # 옵션 A: 마지막 완전한 문장까지만 (마침표/물음표/느낌표 기준)
    # 250자까지 확인하여 여유있게 검색
    sentences = re.split(r"([.!?。！？]\s+)", body[:250])
    if len(sentences) > 1:
        # 마지막 불완전 문장 제외
        summary = "".join(sentences[:-2])
        if 100 <= len(summary) <= 200:
            return summary.rstrip() + "..."

    # 옵션 B: 마지막 줄바꿈 기준 (문단 단위)
    last_newline = body[:200].rfind("\n\n")
    if last_newline > 100:  # 너무 앞에서 자르지 않도록
        return body[:last_newline].rstrip() + "..."

    # 옵션 C: 마지막 공백 기준 (단어 중간 자르기 방지)
    last_space = body[:200].rfind(" ")
    if last_space > 150:
        return body[:last_space] + "..."

    # 최후: 200자 자르기
    return body[:200] + "..."

```

```python
"""
이벤트 정규화 모듈

파싱된 Turn 데이터를 이벤트로 정규화합니다.
"""

import re
from typing import List, Optional, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from backend.core.models import Turn, Event, EventType, SessionMeta
from backend.core.constants import DEBUG_TRIGGERS


def normalize_turns_to_events(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None, use_llm: bool = False
) -> List[Event]:
    """
    Turn 리스트를 Event 리스트로 변환 (우선순위 기반 단일 이벤트, LLM 옵션)

    LLM 사용 시 병렬 처리 (max_workers=5)

    Args:
        turns: 파싱된 Turn 리스트
        session_meta: 세션 메타데이터 (Phase/Subphase 연결용, 선택)
        use_llm: LLM 사용 여부 (기본값: False, True 시 일괄 적용, 병렬 처리)

    Returns:
        정규화된 Event 리스트
    """
    if use_llm:
        # 병렬 처리 (ThreadPoolExecutor)
        events = _normalize_turns_to_events_parallel(turns, session_meta)
    else:
        # 순차 처리 (기존 로직)
        events = []
        for turn in turns:
            event = create_single_event_with_priority(turn, session_meta)
            events.append(event)

    # 시퀀스 번호 부여
    for i, event in enumerate(events):
        event.seq = i + 1

    return events


def _normalize_turns_to_events_parallel(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None
) -> List[Event]:
    """
    LLM 기반 이벤트 생성 (병렬 처리)

    Args:
        turns: Turn 리스트
        session_meta: 세션 메타데이터

    Returns:
        Event 리스트 (turn_index 순서 유지)
    """
    events_dict = {}  # turn_index -> Event 매핑

    with ThreadPoolExecutor(max_workers=5) as executor:
        # 각 Turn을 병렬로 처리
        future_to_turn = {
            executor.submit(create_event_with_llm, turn, session_meta): turn
            for turn in turns
        }

        # 완료된 작업부터 처리 (순서 보장을 위해 turn_index 저장)
        for future in as_completed(future_to_turn):
            turn = future_to_turn[future]
            try:
                event = future.result()
                events_dict[turn.turn_index] = event
            except Exception as e:
                # 에러 발생 시 기본 이벤트 생성 (fallback)
                # 로깅은 선택적 (필요시 추가)
                event = create_single_event_with_priority(turn, session_meta)
                events_dict[turn.turn_index] = event

    # turn_index 순서로 정렬
    events = [events_dict[turn.turn_index] for turn in turns]
    return events


def create_event_with_llm(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    LLM 기반 이벤트 생성 (gpt-4.1-mini)

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체 (processing_method="llm")
    """
    from backend.core.llm_service import classify_and_summarize_with_llm

    # LLM으로 타입 분류 및 요약 생성
    llm_result = classify_and_summarize_with_llm(turn)
    event_type = llm_result["event_type"]
    summary = llm_result["summary"]

    # Artifact 연결 (파일 경로가 있으면)
    artifacts = []
    if turn.path_candidates:
        artifacts = [{"path": path, "action": "mention"} for path in turn.path_candidates]

    # Snippet 참조 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summary,
        artifacts=artifacts,
        snippet_refs=snippet_refs,
        processing_method="llm",
    )


def create_single_event_with_priority(
    turn: Turn, session_meta: Optional[SessionMeta] = None
) -> Event:
    """
    우선순위 기반 단일 이벤트 생성

    우선순위 (높은 순서):
    1. DEBUG: 에러/원인/해결 관련 (가장 구체적)
    2. ARTIFACT: 파일 경로 존재
    3. COMPLETION: 완료 키워드
    4. PLAN: 계획 수립
    5. STATUS_REVIEW: 상태 리뷰
    6. NEXT_STEP: 다음 단계
    7. TURN: 기본

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체
    """
    # 1순위: DEBUG (디버그 트리거 + Cursor 발화)
    if is_debug_turn(turn):
        return create_debug_event(turn, session_meta)

    # 2순위: ARTIFACT (파일 경로 존재)
    if turn.path_candidates:
        return create_artifact_event(turn, session_meta)

    # 3순위: 특수 타입 (엄격한 정규식)
    event_type = classify_event_type_strict(turn)
    if event_type != EventType.TURN:
        return create_message_event(turn, event_type, session_meta)

    # 4순위: 기본 TURN
    return create_message_event(turn, EventType.TURN, session_meta)


def is_debug_turn(turn: Turn) -> bool:
    """
    디버그 Turn인지 판단

    Args:
        turn: Turn 객체

    Returns:
        디버그 Turn 여부
    """
    if turn.speaker != "Cursor":
        return False

    text = turn.body.lower()
    return any(trigger.search(text) for trigger in DEBUG_TRIGGERS.values())


def create_debug_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    DebugEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        DebugEvent 객체
    """
    # 스니펫 참조 생성 (Phase 5에서 실제 ID로 대체될 예정)
    # 현재는 turn_index와 block_index를 조합하여 임시 ID 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.DEBUG,
        summary=summarize_turn(turn),
        artifacts=[],  # 후속 단계에서 연결
        snippet_refs=snippet_refs,
        processing_method="regex",
    )


def create_artifact_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    ArtifactEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        ArtifactEvent 객체
    """
    # Artifact 정보 구성
    artifacts = [
        {"path": path, "action": "mention"}  # Phase 3에서는 mention만, Phase 4에서 확장
        for path in turn.path_candidates
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.ARTIFACT,
        summary=summarize_turn(turn),
        artifacts=artifacts,
        snippet_refs=[],
        processing_method="regex",
    )


def create_message_event(
    turn: Turn,
    event_type: Optional[EventType] = None,
    session_meta: Optional[SessionMeta] = None,
) -> Event:
    """
    MessageEvent 생성 (일반 Turn 이벤트)

    Args:
        turn: Turn 객체
        event_type: 이벤트 타입 (None이면 자동 분류)
        session_meta: 세션 메타데이터 (선택)

    Returns:
        MessageEvent 객체
    """
    # 이벤트 타입 결정 (기본은 TURN, 특정 키워드로 분류 가능)
    if event_type is None:
        event_type = classify_event_type_strict(turn)

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summarize_turn(turn),
        artifacts=[],
        snippet_refs=[],
        processing_method="regex",
    )


def classify_event_type_strict(turn: Turn) -> EventType:
    """
    엄격한 조건으로 이벤트 타입 분류 (정규식 기반)

    일반 단어 매칭을 피하기 위해 더 구체적인 패턴 사용

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    text = turn.body.lower()

    # COMPLETION: 완료 키워드 (더 구체적)
    if re.search(r"(?i)\b(완료되었|완료됨|완료했습니다|성공적으로 완료|작업 완료)\b", text):
        return EventType.COMPLETION

    # PLAN: 계획 수립 (더 구체적)
    if re.search(r"(?i)\b(계획을|계획은|계획하|작업 계획|단계별 계획|진행 계획)\b", text):
        return EventType.PLAN

    # STATUS_REVIEW: 상태 리뷰 (더 구체적)
    if re.search(r"(?i)\b(현황을 리뷰|상태를 확인|진행 상황을 점검|현황 점검|상태 리뷰)\b", text):
        return EventType.STATUS_REVIEW

    # NEXT_STEP: 다음 단계 (더 구체적)
    if re.search(r"(?i)\b(다음 단계는|다음 작업은|다음으로 진행|다음 단계로)\b", text):
        return EventType.NEXT_STEP

    # 기본값: TURN
    return EventType.TURN


def classify_event_type(turn: Turn) -> EventType:
    """
    Turn의 이벤트 타입 분류 (기존 함수, 호환성 유지)

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    # 엄격한 분류 함수 사용
    return classify_event_type_strict(turn)


def _collect_context_info(
    turns: List[Turn], 
    current_turn_index: int, 
    window_size: int = 5
) -> Dict[str, Any]:
    """
    현재 Turn의 맥락 정보 수집 (슬라이딩 윈도우)
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        window_size: 맥락 윈도우 크기 (기본값: 5)
    
    Returns:
        맥락 정보 딕셔너리
    """
    context_info = {
        "recent_turn_count": 0,
        "recent_summaries": [],
        "is_debug_context": False,
        "is_plan_context": False,
    }
    
    # 이전 Turn들 수집 (최근 window_size개)
    start_idx = max(0, current_turn_index - window_size)
    recent_turns = turns[start_idx:current_turn_index]
    
    if not recent_turns:
        return context_info
    
    context_info["recent_turn_count"] = len(recent_turns)
    
    # 최근 Turn들의 요약 생성 (간단한 요약)
    for turn in recent_turns:
        summary = summarize_turn(turn)
        context_info["recent_summaries"].append(summary[:100])  # 최대 100자
    
    # 맥락 타입 판단 (최근 Turn들에서 debug/plan 패턴 확인)
    debug_count = 0
    plan_count = 0
    
    for turn in recent_turns:
        text_lower = turn.body.lower()
        
        # Debug 패턴 확인
        if any(trigger.search(text_lower) for trigger in DEBUG_TRIGGERS.values()):
            debug_count += 1
        
        # Plan 패턴 확인
        if re.search(r"(?i)\b(계획을|계획은|계획하|작업 계획|단계별 계획)\b", text_lower):
            plan_count += 1
    
    # 맥락 판단 (최근 Turn 중 절반 이상이 해당 타입이면 맥락으로 판단)
    threshold = len(recent_turns) / 2
    context_info["is_debug_context"] = debug_count >= threshold
    context_info["is_plan_context"] = plan_count >= threshold
    
    return context_info


def _collect_context_info_with_events(
    turns: List[Turn],
    current_turn_index: int,
    existing_events: Dict[int, Event],
    window_size: int = 5
) -> Dict[str, Any]:
    """
    이미 생성된 Event를 활용하여 맥락 정보 수집 (더 정확)
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        existing_events: 이미 생성된 Event 딕셔너리 (turn_index -> Event)
        window_size: 맥락 윈도우 크기 (기본값: 5)
    
    Returns:
        맥락 정보 딕셔너리
    """
    context_info = {
        "recent_turn_count": 0,
        "recent_summaries": [],
        "is_debug_context": False,
        "is_plan_context": False,
    }
    
    # 이전 Turn들 수집 (최근 window_size개)
    start_idx = max(0, current_turn_index - window_size)
    recent_turns = turns[start_idx:current_turn_index]
    
    if not recent_turns:
        return context_info
    
    context_info["recent_turn_count"] = len(recent_turns)
    
    # 이미 생성된 Event의 summary 사용 (더 정확)
    for turn in recent_turns:
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            context_info["recent_summaries"].append(event.summary[:100])
        else:
            # Event가 없으면 간단한 요약 생성
            summary = summarize_turn(turn)
            context_info["recent_summaries"].append(summary[:100])
    
    # 맥락 타입 판단 (이미 생성된 Event의 타입 사용)
    debug_count = 0
    plan_count = 0
    
    for turn in recent_turns:
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            if event.type == EventType.DEBUG:
                debug_count += 1
            elif event.type == EventType.PLAN:
                plan_count += 1
    
    # 맥락 판단
    threshold = len(recent_turns) / 2
    context_info["is_debug_context"] = debug_count >= threshold
    context_info["is_plan_context"] = plan_count >= threshold
    
    return context_info


def summarize_turn(turn: Turn) -> str:
    """
    Turn을 요약 (정규식 기반 개선 버전)

    Args:
        turn: Turn 객체

    Returns:
        요약 텍스트
    """
    body = turn.body.strip()

    # 1. 줄바꿈 정리 (연속된 \n을 최대 2개로 제한)
    body = re.sub(r"\n{3,}", "\n\n", body)

    # 2. 200자 이하면 그대로 반환
    if len(body) <= 200:
        return body

    # 3. 의미 있는 위치에서 자르기 (우선순위 순)

    # 옵션 A: 마지막 완전한 문장까지만 (마침표/물음표/느낌표 기준)
    # 250자까지 확인하여 여유있게 검색
    sentences = re.split(r"([.!?。！？]\s+)", body[:250])
    if len(sentences) > 1:
        # 마지막 불완전 문장 제외
        summary = "".join(sentences[:-2])
        if 100 <= len(summary) <= 200:
            return summary.rstrip() + "..."

    # 옵션 B: 마지막 줄바꿈 기준 (문단 단위)
    last_newline = body[:200].rfind("\n\n")
    if last_newline > 100:  # 너무 앞에서 자르지 않도록
        return body[:last_newline].rstrip() + "..."

    # 옵션 C: 마지막 공백 기준 (단어 중간 자르기 방지)
    last_space = body[:200].rfind(" ")
    if last_space > 150:
        return body[:last_space] + "..."

    # 최후: 200자 자르기
    return body[:200] + "..."

```

3단계: 이벤트 정규화 함수에 맥락 정보 전달 및 하이브리드 병렬 처리 구현 중.


```python
"""
이벤트 정규화 모듈

파싱된 Turn 데이터를 이벤트로 정규화합니다.
"""

import re
from typing import List, Optional, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from backend.core.models import Turn, Event, EventType, SessionMeta
from backend.core.constants import DEBUG_TRIGGERS


def normalize_turns_to_events(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None, use_llm: bool = False
) -> List[Event]:
    """
    Turn 리스트를 Event 리스트로 변환 (우선순위 기반 단일 이벤트, LLM 옵션)

    LLM 사용 시 병렬 처리 (max_workers=5)

    Args:
        turns: 파싱된 Turn 리스트
        session_meta: 세션 메타데이터 (Phase/Subphase 연결용, 선택)
        use_llm: LLM 사용 여부 (기본값: False, True 시 일괄 적용, 병렬 처리)

    Returns:
        정규화된 Event 리스트
    """
    if use_llm:
        # 병렬 처리 (ThreadPoolExecutor)
        events = _normalize_turns_to_events_parallel(turns, session_meta)
    else:
        # 순차 처리 (기존 로직)
        events = []
        for turn in turns:
            event = create_single_event_with_priority(turn, session_meta)
            events.append(event)

    # 시퀀스 번호 부여
    for i, event in enumerate(events):
        event.seq = i + 1

    return events


def _normalize_turns_to_events_parallel(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None
) -> List[Event]:
    """
    LLM 기반 이벤트 생성 (병렬 처리)

    Args:
        turns: Turn 리스트
        session_meta: 세션 메타데이터

    Returns:
        Event 리스트 (turn_index 순서 유지)
    """
    events_dict = {}  # turn_index -> Event 매핑

    with ThreadPoolExecutor(max_workers=5) as executor:
        # 각 Turn을 병렬로 처리
        future_to_turn = {
            executor.submit(create_event_with_llm, turn, session_meta): turn
            for turn in turns
        }

        # 완료된 작업부터 처리 (순서 보장을 위해 turn_index 저장)
        for future in as_completed(future_to_turn):
            turn = future_to_turn[future]
            try:
                event = future.result()
                events_dict[turn.turn_index] = event
            except Exception as e:
                # 에러 발생 시 기본 이벤트 생성 (fallback)
                # 로깅은 선택적 (필요시 추가)
                event = create_single_event_with_priority(turn, session_meta)
                events_dict[turn.turn_index] = event

    # turn_index 순서로 정렬
    events = [events_dict[turn.turn_index] for turn in turns]
    return events


def create_event_with_llm(
    turn: Turn, 
    session_meta: Optional[SessionMeta] = None,
    turns: Optional[List[Turn]] = None,  # 전체 Turn 리스트 추가
    existing_events: Optional[Dict[int, Event]] = None  # 이미 생성된 Event들
) -> Event:
    """
    LLM 기반 이벤트 생성 (gpt-4.1-mini, 맥락 정보 포함)

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)
        turns: 전체 Turn 리스트 (맥락 정보 수집용, 선택)
        existing_events: 이미 생성된 Event 딕셔너리 (맥락 정보 수집용, 선택)

    Returns:
        Event 객체 (processing_method="llm")
    """
    from backend.core.llm_service import classify_and_summarize_with_llm

    # 맥락 정보 수집
    context_info = None
    if turns is not None:
        if existing_events is not None:
            # 이미 생성된 Event를 활용한 맥락 정보 (더 정확)
            context_info = _collect_context_info_with_events(
                turns, 
                turn.turn_index, 
                existing_events
            )
        else:
            # 기본 맥락 정보
            context_info = _collect_context_info(
                turns, 
                turn.turn_index
            )

    # LLM으로 타입 분류 및 요약 생성 (맥락 정보 포함)
    llm_result = classify_and_summarize_with_llm(turn, context_info=context_info)
    event_type = llm_result["event_type"]
    summary = llm_result["summary"]

    # path_candidates가 있으면 artifact 타입 우선 고려
    if turn.path_candidates and event_type not in [EventType.ARTIFACT, EventType.DEBUG]:
        # 코드 블록이 있거나 artifact 키워드가 있으면 artifact 타입으로 변경
        if turn.code_blocks or is_artifact_turn(turn):
            event_type = EventType.ARTIFACT
            if turn.path_candidates:
                summary = f"{llm_result['summary']} (파일: {', '.join(turn.path_candidates[:3])})"
        else:
            summary = llm_result["summary"]
    else:
        summary = llm_result["summary"]

    # Artifact 연결 (파일 경로가 있으면)
    artifacts = []
    if turn.path_candidates:
        artifacts = [{"path": path, "action": "mention"} for path in turn.path_candidates]

    # Snippet 참조 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summary,
        artifacts=artifacts,
        snippet_refs=snippet_refs,
        processing_method="llm",
    )


def is_artifact_turn(turn: Turn) -> bool:
    """
    Artifact Turn인지 판단 (키워드 기반)
    
    Args:
        turn: Turn 객체
    
    Returns:
        Artifact Turn 여부
    """
    text_lower = turn.body.lower()
    
    # 파일 경로가 있으면 artifact
    if turn.path_candidates:
        return True
    
    # 코드 블록이 있으면 artifact 가능성 높음
    if turn.code_blocks:
        return True
    
    # Artifact 키워드 확인
    artifact_keywords = [
        "스크립트 작성", "스크립트 생성", "스크립트를 만들",
        "코드 수정", "코드를 수정", "코드 변경",
        "파일 생성", "파일을 생성", "파일 작성",
        "파일 수정", "파일을 수정", "파일 변경",
        "작성 중", "생성 중", "수정 중"
    ]
    
    return any(keyword in text_lower for keyword in artifact_keywords)


def create_single_event_with_priority(
    turn: Turn, session_meta: Optional[SessionMeta] = None
) -> Event:
    """
    우선순위 기반 단일 이벤트 생성

    우선순위 (높은 순서):
    1. DEBUG: 에러/원인/해결 관련 (가장 구체적)
    2. ARTIFACT: 파일 경로 존재
    3. COMPLETION: 완료 키워드
    4. PLAN: 계획 수립
    5. STATUS_REVIEW: 상태 리뷰
    6. NEXT_STEP: 다음 단계
    7. TURN: 기본

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체
    """
    # 1순위: DEBUG (디버그 트리거 + Cursor 발화)
    if is_debug_turn(turn):
        return create_debug_event(turn, session_meta)

    # 2순위: ARTIFACT (파일 경로 존재)
    if turn.path_candidates:
        return create_artifact_event(turn, session_meta)

    # 3순위: 특수 타입 (엄격한 정규식)
    event_type = classify_event_type_strict(turn)
    if event_type != EventType.TURN:
        return create_message_event(turn, event_type, session_meta)

    # 4순위: 기본 TURN
    return create_message_event(turn, EventType.TURN, session_meta)


def is_debug_turn(turn: Turn) -> bool:
    """
    디버그 Turn인지 판단

    Args:
        turn: Turn 객체

    Returns:
        디버그 Turn 여부
    """
    if turn.speaker != "Cursor":
        return False

    text = turn.body.lower()
    return any(trigger.search(text) for trigger in DEBUG_TRIGGERS.values())


def create_debug_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    DebugEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        DebugEvent 객체
    """
    # 스니펫 참조 생성 (Phase 5에서 실제 ID로 대체될 예정)
    # 현재는 turn_index와 block_index를 조합하여 임시 ID 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.DEBUG,
        summary=summarize_turn(turn),
        artifacts=[],  # 후속 단계에서 연결
        snippet_refs=snippet_refs,
        processing_method="regex",
    )


def create_artifact_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    ArtifactEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        ArtifactEvent 객체
    """
    # Artifact 정보 구성
    artifacts = [
        {"path": path, "action": "mention"}  # Phase 3에서는 mention만, Phase 4에서 확장
        for path in turn.path_candidates
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.ARTIFACT,
        summary=summarize_turn(turn),
        artifacts=artifacts,
        snippet_refs=[],
        processing_method="regex",
    )


def create_message_event(
    turn: Turn,
    event_type: Optional[EventType] = None,
    session_meta: Optional[SessionMeta] = None,
) -> Event:
    """
    MessageEvent 생성 (일반 Turn 이벤트)

    Args:
        turn: Turn 객체
        event_type: 이벤트 타입 (None이면 자동 분류)
        session_meta: 세션 메타데이터 (선택)

    Returns:
        MessageEvent 객체
    """
    # 이벤트 타입 결정 (기본은 TURN, 특정 키워드로 분류 가능)
    if event_type is None:
        event_type = classify_event_type_strict(turn)

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summarize_turn(turn),
        artifacts=[],
        snippet_refs=[],
        processing_method="regex",
    )


def classify_event_type_strict(turn: Turn) -> EventType:
    """
    엄격한 조건으로 이벤트 타입 분류 (정규식 기반)

    일반 단어 매칭을 피하기 위해 더 구체적인 패턴 사용

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    text = turn.body.lower()

    # COMPLETION: 완료 키워드 (더 구체적)
    if re.search(r"(?i)\b(완료되었|완료됨|완료했습니다|성공적으로 완료|작업 완료)\b", text):
        return EventType.COMPLETION

    # PLAN: 계획 수립 (더 구체적)
    if re.search(r"(?i)\b(계획을|계획은|계획하|작업 계획|단계별 계획|진행 계획)\b", text):
        return EventType.PLAN

    # STATUS_REVIEW: 상태 리뷰 (더 구체적)
    if re.search(r"(?i)\b(현황을 리뷰|상태를 확인|진행 상황을 점검|현황 점검|상태 리뷰)\b", text):
        return EventType.STATUS_REVIEW

    # NEXT_STEP: 다음 단계 (더 구체적)
    if re.search(r"(?i)\b(다음 단계는|다음 작업은|다음으로 진행|다음 단계로)\b", text):
        return EventType.NEXT_STEP

    # 기본값: TURN
    return EventType.TURN


def classify_event_type(turn: Turn) -> EventType:
    """
    Turn의 이벤트 타입 분류 (기존 함수, 호환성 유지)

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    # 엄격한 분류 함수 사용
    return classify_event_type_strict(turn)


def _collect_context_info(
    turns: List[Turn], 
    current_turn_index: int, 
    window_size: int = 5
) -> Dict[str, Any]:
    """
    현재 Turn의 맥락 정보 수집 (슬라이딩 윈도우)
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        window_size: 맥락 윈도우 크기 (기본값: 5)
    
    Returns:
        맥락 정보 딕셔너리
    """
    context_info = {
        "recent_turn_count": 0,
        "recent_summaries": [],
        "is_debug_context": False,
        "is_plan_context": False,
    }
    
    # 이전 Turn들 수집 (최근 window_size개)
    start_idx = max(0, current_turn_index - window_size)
    recent_turns = turns[start_idx:current_turn_index]
    
    if not recent_turns:
        return context_info
    
    context_info["recent_turn_count"] = len(recent_turns)
    
    # 최근 Turn들의 요약 생성 (간단한 요약)
    for turn in recent_turns:
        summary = summarize_turn(turn)
        context_info["recent_summaries"].append(summary[:100])  # 최대 100자
    
    # 맥락 타입 판단 (최근 Turn들에서 debug/plan 패턴 확인)
    debug_count = 0
    plan_count = 0
    
    for turn in recent_turns:
        text_lower = turn.body.lower()
        
        # Debug 패턴 확인
        if any(trigger.search(text_lower) for trigger in DEBUG_TRIGGERS.values()):
            debug_count += 1
        
        # Plan 패턴 확인
        if re.search(r"(?i)\b(계획을|계획은|계획하|작업 계획|단계별 계획)\b", text_lower):
            plan_count += 1
    
    # 맥락 판단 (최근 Turn 중 절반 이상이 해당 타입이면 맥락으로 판단)
    threshold = len(recent_turns) / 2
    context_info["is_debug_context"] = debug_count >= threshold
    context_info["is_plan_context"] = plan_count >= threshold
    
    return context_info


def _collect_context_info_with_events(
    turns: List[Turn],
    current_turn_index: int,
    existing_events: Dict[int, Event],
    window_size: int = 5
) -> Dict[str, Any]:
    """
    이미 생성된 Event를 활용하여 맥락 정보 수집 (더 정확)
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        existing_events: 이미 생성된 Event 딕셔너리 (turn_index -> Event)
        window_size: 맥락 윈도우 크기 (기본값: 5)
    
    Returns:
        맥락 정보 딕셔너리
    """
    context_info = {
        "recent_turn_count": 0,
        "recent_summaries": [],
        "is_debug_context": False,
        "is_plan_context": False,
    }
    
    # 이전 Turn들 수집 (최근 window_size개)
    start_idx = max(0, current_turn_index - window_size)
    recent_turns = turns[start_idx:current_turn_index]
    
    if not recent_turns:
        return context_info
    
    context_info["recent_turn_count"] = len(recent_turns)
    
    # 이미 생성된 Event의 summary 사용 (더 정확)
    for turn in recent_turns:
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            context_info["recent_summaries"].append(event.summary[:100])
        else:
            # Event가 없으면 간단한 요약 생성
            summary = summarize_turn(turn)
            context_info["recent_summaries"].append(summary[:100])
    
    # 맥락 타입 판단 (이미 생성된 Event의 타입 사용)
    debug_count = 0
    plan_count = 0
    
    for turn in recent_turns:
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            if event.type == EventType.DEBUG:
                debug_count += 1
            elif event.type == EventType.PLAN:
                plan_count += 1
    
    # 맥락 판단
    threshold = len(recent_turns) / 2
    context_info["is_debug_context"] = debug_count >= threshold
    context_info["is_plan_context"] = plan_count >= threshold
    
    return context_info


def summarize_turn(turn: Turn) -> str:
    """
    Turn을 요약 (정규식 기반 개선 버전)

    Args:
        turn: Turn 객체

    Returns:
        요약 텍스트
    """
    body = turn.body.strip()

    # 1. 줄바꿈 정리 (연속된 \n을 최대 2개로 제한)
    body = re.sub(r"\n{3,}", "\n\n", body)

    # 2. 200자 이하면 그대로 반환
    if len(body) <= 200:
        return body

    # 3. 의미 있는 위치에서 자르기 (우선순위 순)

    # 옵션 A: 마지막 완전한 문장까지만 (마침표/물음표/느낌표 기준)
    # 250자까지 확인하여 여유있게 검색
    sentences = re.split(r"([.!?。！？]\s+)", body[:250])
    if len(sentences) > 1:
        # 마지막 불완전 문장 제외
        summary = "".join(sentences[:-2])
        if 100 <= len(summary) <= 200:
            return summary.rstrip() + "..."

    # 옵션 B: 마지막 줄바꿈 기준 (문단 단위)
    last_newline = body[:200].rfind("\n\n")
    if last_newline > 100:  # 너무 앞에서 자르지 않도록
        return body[:last_newline].rstrip() + "..."

    # 옵션 C: 마지막 공백 기준 (단어 중간 자르기 방지)
    last_space = body[:200].rfind(" ")
    if last_space > 150:
        return body[:last_space] + "..."

    # 최후: 200자 자르기
    return body[:200] + "..."

```

```python
"""
이벤트 정규화 모듈

파싱된 Turn 데이터를 이벤트로 정규화합니다.
"""

import re
from typing import List, Optional, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from backend.core.models import Turn, Event, EventType, SessionMeta
from backend.core.constants import DEBUG_TRIGGERS


def normalize_turns_to_events(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None, use_llm: bool = False
) -> List[Event]:
    """
    Turn 리스트를 Event 리스트로 변환 (우선순위 기반 단일 이벤트, LLM 옵션)

    LLM 사용 시 병렬 처리 (max_workers=5)

    Args:
        turns: 파싱된 Turn 리스트
        session_meta: 세션 메타데이터 (Phase/Subphase 연결용, 선택)
        use_llm: LLM 사용 여부 (기본값: False, True 시 일괄 적용, 병렬 처리)

    Returns:
        정규화된 Event 리스트
    """
    if use_llm:
        # 병렬 처리 (ThreadPoolExecutor)
        events = _normalize_turns_to_events_parallel(turns, session_meta)
    else:
        # 순차 처리 (기존 로직)
        events = []
        for turn in turns:
            event = create_single_event_with_priority(turn, session_meta)
            events.append(event)

    # 시퀀스 번호 부여
    for i, event in enumerate(events):
        event.seq = i + 1

    return events


def _normalize_turns_to_events_parallel(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None
) -> List[Event]:
    """
    LLM 기반 이벤트 생성 (병렬 처리, 하이브리드 방식)

    하이브리드 방식:
    1. 1차: 병렬로 모든 Turn 처리 (맥락 없이)
    2. 2차: 순차적으로 맥락 정보를 활용하여 재분류 (필요시)

    Args:
        turns: Turn 리스트
        session_meta: 세션 메타데이터

    Returns:
        Event 리스트 (turn_index 순서 유지)
    """
    events_dict = {}  # turn_index -> Event 매핑

    # 1차: 병렬로 모든 Turn 처리 (맥락 없이, 빠른 처리)
    with ThreadPoolExecutor(max_workers=5) as executor:
        # 각 Turn을 병렬로 처리
        future_to_turn = {
            executor.submit(create_event_with_llm, turn, session_meta, turns, None): turn
            for turn in turns
        }

        # 완료된 작업부터 처리 (순서 보장을 위해 turn_index 저장)
        for future in as_completed(future_to_turn):
            turn = future_to_turn[future]
            try:
                event = future.result()
                events_dict[turn.turn_index] = event
            except Exception as e:
                # 에러 발생 시 기본 이벤트 생성 (fallback)
                # 로깅은 선택적 (필요시 추가)
                event = create_single_event_with_priority(turn, session_meta)
                events_dict[turn.turn_index] = event

    # 2차: 맥락 정보를 활용하여 재분류 (순차 처리)
    # 현재는 1차 결과를 그대로 사용 (향후 개선 가능)
    # 맥락 정보가 중요한 경우에만 재분류하도록 최적화 가능

    # turn_index 순서로 정렬
    events = [events_dict[turn.turn_index] for turn in turns]
    return events


def create_event_with_llm(
    turn: Turn, 
    session_meta: Optional[SessionMeta] = None,
    turns: Optional[List[Turn]] = None,  # 전체 Turn 리스트 추가
    existing_events: Optional[Dict[int, Event]] = None  # 이미 생성된 Event들
) -> Event:
    """
    LLM 기반 이벤트 생성 (gpt-4.1-mini, 맥락 정보 포함)

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)
        turns: 전체 Turn 리스트 (맥락 정보 수집용, 선택)
        existing_events: 이미 생성된 Event 딕셔너리 (맥락 정보 수집용, 선택)

    Returns:
        Event 객체 (processing_method="llm")
    """
    from backend.core.llm_service import classify_and_summarize_with_llm

    # 맥락 정보 수집
    context_info = None
    if turns is not None:
        if existing_events is not None:
            # 이미 생성된 Event를 활용한 맥락 정보 (더 정확)
            context_info = _collect_context_info_with_events(
                turns, 
                turn.turn_index, 
                existing_events
            )
        else:
            # 기본 맥락 정보
            context_info = _collect_context_info(
                turns, 
                turn.turn_index
            )

    # LLM으로 타입 분류 및 요약 생성 (맥락 정보 포함)
    llm_result = classify_and_summarize_with_llm(turn, context_info=context_info)
    event_type = llm_result["event_type"]
    summary = llm_result["summary"]

    # path_candidates가 있으면 artifact 타입 우선 고려
    if turn.path_candidates and event_type not in [EventType.ARTIFACT, EventType.DEBUG]:
        # 코드 블록이 있거나 artifact 키워드가 있으면 artifact 타입으로 변경
        if turn.code_blocks or is_artifact_turn(turn):
            event_type = EventType.ARTIFACT
            if turn.path_candidates:
                summary = f"{llm_result['summary']} (파일: {', '.join(turn.path_candidates[:3])})"
        else:
            summary = llm_result["summary"]
    else:
        summary = llm_result["summary"]

    # Artifact 연결 (파일 경로가 있으면)
    artifacts = []
    if turn.path_candidates:
        artifacts = [{"path": path, "action": "mention"} for path in turn.path_candidates]

    # Snippet 참조 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summary,
        artifacts=artifacts,
        snippet_refs=snippet_refs,
        processing_method="llm",
    )


def is_artifact_turn(turn: Turn) -> bool:
    """
    Artifact Turn인지 판단 (키워드 기반)
    
    Args:
        turn: Turn 객체
    
    Returns:
        Artifact Turn 여부
    """
    text_lower = turn.body.lower()
    
    # 파일 경로가 있으면 artifact
    if turn.path_candidates:
        return True
    
    # 코드 블록이 있으면 artifact 가능성 높음
    if turn.code_blocks:
        return True
    
    # Artifact 키워드 확인
    artifact_keywords = [
        "스크립트 작성", "스크립트 생성", "스크립트를 만들",
        "코드 수정", "코드를 수정", "코드 변경",
        "파일 생성", "파일을 생성", "파일 작성",
        "파일 수정", "파일을 수정", "파일 변경",
        "작성 중", "생성 중", "수정 중"
    ]
    
    return any(keyword in text_lower for keyword in artifact_keywords)


def create_single_event_with_priority(
    turn: Turn, session_meta: Optional[SessionMeta] = None
) -> Event:
    """
    우선순위 기반 단일 이벤트 생성

    우선순위 (높은 순서):
    1. DEBUG: 에러/원인/해결 관련 (가장 구체적)
    2. ARTIFACT: 파일 경로 존재
    3. COMPLETION: 완료 키워드
    4. PLAN: 계획 수립
    5. STATUS_REVIEW: 상태 리뷰
    6. NEXT_STEP: 다음 단계
    7. TURN: 기본

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체
    """
    # 1순위: DEBUG (디버그 트리거 + Cursor 발화)
    if is_debug_turn(turn):
        return create_debug_event(turn, session_meta)

    # 2순위: ARTIFACT (파일 경로 존재)
    if turn.path_candidates:
        return create_artifact_event(turn, session_meta)

    # 3순위: 특수 타입 (엄격한 정규식)
    event_type = classify_event_type_strict(turn)
    if event_type != EventType.TURN:
        return create_message_event(turn, event_type, session_meta)

    # 4순위: 기본 TURN
    return create_message_event(turn, EventType.TURN, session_meta)


def is_debug_turn(turn: Turn) -> bool:
    """
    디버그 Turn인지 판단

    Args:
        turn: Turn 객체

    Returns:
        디버그 Turn 여부
    """
    if turn.speaker != "Cursor":
        return False

    text = turn.body.lower()
    return any(trigger.search(text) for trigger in DEBUG_TRIGGERS.values())


def create_debug_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    DebugEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        DebugEvent 객체
    """
    # 스니펫 참조 생성 (Phase 5에서 실제 ID로 대체될 예정)
    # 현재는 turn_index와 block_index를 조합하여 임시 ID 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.DEBUG,
        summary=summarize_turn(turn),
        artifacts=[],  # 후속 단계에서 연결
        snippet_refs=snippet_refs,
        processing_method="regex",
    )


def create_artifact_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    ArtifactEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        ArtifactEvent 객체
    """
    # Artifact 정보 구성
    artifacts = [
        {"path": path, "action": "mention"}  # Phase 3에서는 mention만, Phase 4에서 확장
        for path in turn.path_candidates
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.ARTIFACT,
        summary=summarize_turn(turn),
        artifacts=artifacts,
        snippet_refs=[],
        processing_method="regex",
    )


def create_message_event(
    turn: Turn,
    event_type: Optional[EventType] = None,
    session_meta: Optional[SessionMeta] = None,
) -> Event:
    """
    MessageEvent 생성 (일반 Turn 이벤트)

    Args:
        turn: Turn 객체
        event_type: 이벤트 타입 (None이면 자동 분류)
        session_meta: 세션 메타데이터 (선택)

    Returns:
        MessageEvent 객체
    """
    # 이벤트 타입 결정 (기본은 TURN, 특정 키워드로 분류 가능)
    if event_type is None:
        event_type = classify_event_type_strict(turn)

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summarize_turn(turn),
        artifacts=[],
        snippet_refs=[],
        processing_method="regex",
    )


def classify_event_type_strict(turn: Turn) -> EventType:
    """
    엄격한 조건으로 이벤트 타입 분류 (정규식 기반)

    일반 단어 매칭을 피하기 위해 더 구체적인 패턴 사용

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    text = turn.body.lower()

    # COMPLETION: 완료 키워드 (더 구체적)
    if re.search(r"(?i)\b(완료되었|완료됨|완료했습니다|성공적으로 완료|작업 완료)\b", text):
        return EventType.COMPLETION

    # PLAN: 계획 수립 (더 구체적)
    if re.search(r"(?i)\b(계획을|계획은|계획하|작업 계획|단계별 계획|진행 계획)\b", text):
        return EventType.PLAN

    # STATUS_REVIEW: 상태 리뷰 (더 구체적)
    if re.search(r"(?i)\b(현황을 리뷰|상태를 확인|진행 상황을 점검|현황 점검|상태 리뷰)\b", text):
        return EventType.STATUS_REVIEW

    # NEXT_STEP: 다음 단계 (더 구체적)
    if re.search(r"(?i)\b(다음 단계는|다음 작업은|다음으로 진행|다음 단계로)\b", text):
        return EventType.NEXT_STEP

    # 기본값: TURN
    return EventType.TURN


def classify_event_type(turn: Turn) -> EventType:
    """
    Turn의 이벤트 타입 분류 (기존 함수, 호환성 유지)

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    # 엄격한 분류 함수 사용
    return classify_event_type_strict(turn)


def _collect_context_info(
    turns: List[Turn], 
    current_turn_index: int, 
    window_size: int = 5
) -> Dict[str, Any]:
    """
    현재 Turn의 맥락 정보 수집 (슬라이딩 윈도우)
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        window_size: 맥락 윈도우 크기 (기본값: 5)
    
    Returns:
        맥락 정보 딕셔너리
    """
    context_info = {
        "recent_turn_count": 0,
        "recent_summaries": [],
        "is_debug_context": False,
        "is_plan_context": False,
    }
    
    # 이전 Turn들 수집 (최근 window_size개)
    start_idx = max(0, current_turn_index - window_size)
    recent_turns = turns[start_idx:current_turn_index]
    
    if not recent_turns:
        return context_info
    
    context_info["recent_turn_count"] = len(recent_turns)
    
    # 최근 Turn들의 요약 생성 (간단한 요약)
    for turn in recent_turns:
        summary = summarize_turn(turn)
        context_info["recent_summaries"].append(summary[:100])  # 최대 100자
    
    # 맥락 타입 판단 (최근 Turn들에서 debug/plan 패턴 확인)
    debug_count = 0
    plan_count = 0
    
    for turn in recent_turns:
        text_lower = turn.body.lower()
        
        # Debug 패턴 확인
        if any(trigger.search(text_lower) for trigger in DEBUG_TRIGGERS.values()):
            debug_count += 1
        
        # Plan 패턴 확인
        if re.search(r"(?i)\b(계획을|계획은|계획하|작업 계획|단계별 계획)\b", text_lower):
            plan_count += 1
    
    # 맥락 판단 (최근 Turn 중 절반 이상이 해당 타입이면 맥락으로 판단)
    threshold = len(recent_turns) / 2
    context_info["is_debug_context"] = debug_count >= threshold
    context_info["is_plan_context"] = plan_count >= threshold
    
    return context_info


def _collect_context_info_with_events(
    turns: List[Turn],
    current_turn_index: int,
    existing_events: Dict[int, Event],
    window_size: int = 5
) -> Dict[str, Any]:
    """
    이미 생성된 Event를 활용하여 맥락 정보 수집 (더 정확)
    
    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        existing_events: 이미 생성된 Event 딕셔너리 (turn_index -> Event)
        window_size: 맥락 윈도우 크기 (기본값: 5)
    
    Returns:
        맥락 정보 딕셔너리
    """
    context_info = {
        "recent_turn_count": 0,
        "recent_summaries": [],
        "is_debug_context": False,
        "is_plan_context": False,
    }
    
    # 이전 Turn들 수집 (최근 window_size개)
    start_idx = max(0, current_turn_index - window_size)
    recent_turns = turns[start_idx:current_turn_index]
    
    if not recent_turns:
        return context_info
    
    context_info["recent_turn_count"] = len(recent_turns)
    
    # 이미 생성된 Event의 summary 사용 (더 정확)
    for turn in recent_turns:
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            context_info["recent_summaries"].append(event.summary[:100])
        else:
            # Event가 없으면 간단한 요약 생성
            summary = summarize_turn(turn)
            context_info["recent_summaries"].append(summary[:100])
    
    # 맥락 타입 판단 (이미 생성된 Event의 타입 사용)
    debug_count = 0
    plan_count = 0
    
    for turn in recent_turns:
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            if event.type == EventType.DEBUG:
                debug_count += 1
            elif event.type == EventType.PLAN:
                plan_count += 1
    
    # 맥락 판단
    threshold = len(recent_turns) / 2
    context_info["is_debug_context"] = debug_count >= threshold
    context_info["is_plan_context"] = plan_count >= threshold
    
    return context_info


def summarize_turn(turn: Turn) -> str:
    """
    Turn을 요약 (정규식 기반 개선 버전)

    Args:
        turn: Turn 객체

    Returns:
        요약 텍스트
    """
    body = turn.body.strip()

    # 1. 줄바꿈 정리 (연속된 \n을 최대 2개로 제한)
    body = re.sub(r"\n{3,}", "\n\n", body)

    # 2. 200자 이하면 그대로 반환
    if len(body) <= 200:
        return body

    # 3. 의미 있는 위치에서 자르기 (우선순위 순)

    # 옵션 A: 마지막 완전한 문장까지만 (마침표/물음표/느낌표 기준)
    # 250자까지 확인하여 여유있게 검색
    sentences = re.split(r"([.!?。！？]\s+)", body[:250])
    if len(sentences) > 1:
        # 마지막 불완전 문장 제외
        summary = "".join(sentences[:-2])
        if 100 <= len(summary) <= 200:
            return summary.rstrip() + "..."

    # 옵션 B: 마지막 줄바꿈 기준 (문단 단위)
    last_newline = body[:200].rfind("\n\n")
    if last_newline > 100:  # 너무 앞에서 자르지 않도록
        return body[:last_newline].rstrip() + "..."

    # 옵션 C: 마지막 공백 기준 (단어 중간 자르기 방지)
    last_space = body[:200].rfind(" ")
    if last_space > 150:
        return body[:last_space] + "..."

    # 최후: 200자 자르기
    return body[:200] + "..."

```

4단계: E2E 테스트 실행 및 결과 검증 중.


테스트가 완료되었습니다. 결과 확인 중입니다.


PowerShell 따옴표 문제로 스크립트 파일로 실행 중.


```python
"""
개선 후 Artifact 타입 분류 결과 확인
"""
import json
from pathlib import Path

results_file = Path("tests/results/event_normalizer_e2e_llm_20251225_183334.json")
data = json.load(open(results_file, "r", encoding="utf-8"))

artifacts = [e for e in data["events"] if e["type"] == "artifact"]
print(f"Artifact 이벤트: {len(artifacts)}개")
print(f"\n전체 이벤트 타입 분포:")
type_dist = {}
for e in data["events"]:
    type_dist[e["type"]] = type_dist.get(e["type"], 0) + 1
for t, count in sorted(type_dist.items()):
    print(f"  {t}: {count}개")

print("\nArtifact 이벤트 샘플 5개:")
for e in artifacts[:5]:
    print(f"  Turn {e['turn_ref']}: {e['summary'][:100]}...")
    if e.get("artifacts"):
        print(f"    - 파일: {[a['path'] for a in e['artifacts']]}")

```

개선 작업이 완료되었습니다. 결과 요약:

## 개선 작업 완료 요약

### 완료된 작업

#### 1단계: LLM 서비스에 Artifact 정보 포함
- `classify_and_summarize_with_llm()` 함수 수정
- `code_blocks`와 `path_candidates` 정보를 프롬프트에 포함
- Artifact 정보를 고려한 타입 분류 지침 추가

#### 2단계: 캐시 키 생성 시 Artifact 정보 포함
- 캐시 키 생성 시 `code_blocks`와 `path_candidates` 정보 포함
- 맥락 정보도 캐시 키에 포함 (있는 경우)

#### 3단계: 맥락 정보 수집 함수 구현
- `_collect_context_info()` 함수 추가 (기본 맥락 정보)
- `_collect_context_info_with_events()` 함수 추가 (Event 기반 맥락 정보)

#### 4단계: 이벤트 정규화 함수 수정
- `create_event_with_llm()` 함수에 맥락 정보 전달
- `is_artifact_turn()` 함수 추가 (Artifact 타입 판단 강화)
- `path_candidates`가 있으면 artifact 타입 우선 고려

#### 5단계: E2E 테스트 실행 및 검증
- 테스트 성공적으로 완료
- Artifact 타입 분류: 32개 (개선됨)
- 요약 품질: 파일명 포함된 상세 요약 생성

---

## 테스트 결과

### 이벤트 타입 분포
```
artifact: 32개 (47.8%)
debug: 18개 (26.9%)
turn: 8개 (11.9%)
next_step: 4개 (6.0%)
plan: 3개 (4.5%)
status_review: 2개 (3.0%)
```

### 개선 사항 확인
1. Artifact 타입 분류 개선: 파일 경로가 있는 Turn이 artifact로 분류됨
2. 요약 품질 개선: 파일명과 상세 정보가 포함된 요약 생성
3. 맥락 정보 활용: 이전 Turn의 맥락을 고려한 타입 분류

---

## 다음 단계

1. 수동 검증 데이터셋 검토: `tests/manual_review/manual_review_dataset_20251225_183334.json`
2. 정확도 평가: 수동 검증 후 `evaluate_manual_review()` 실행
3. Golden 파일 생성: 정확도가 충분하면 Golden 파일 생성

개선 작업이 완료되었습니다. 수동 검증을 진행하시겠습니까?

```plaintext
artifact: 32개 (47.8%)
debug: 18개 (26.9%)
turn: 8개 (11.9%)
next_step: 4개 (6.0%)
plan: 3개 (4.5%)
status_review: 2개 (3.0%)
```

---

**User**

수동 검증할 데이터 셋을 이전과 같이 html로 읽고 사용자 피드백을 받을 수 있도록 해주세요
스크립트 파일이 있으니, 확인하세요
그리고 피드백 받은 내용 포함해서 저장할때, 문제가 있었습니다.
스크립트를 확인해서 저장에 문제없게 하세됴

---

**Cursor**

기존 스크립트 확인 중. HTML 생성 및 피드백 저장 로직 점검 중.


기존 스크립트 확인 중. HTML 생성 및 피드백 저장 로직 점검 중.


최신 테스트 결과로 HTML 생성 스크립트 실행 및 저장 로직 개선 중.


HTML 생성 완료. 저장 로직 개선 중: `exportToJSON()` 함수 수정 및 저장 형식 검증.


```python
        // JSON으로 내보내기
        function exportToJSON() {
            const updatedData = JSON.parse(JSON.stringify(eventData));

            updatedData.samples.forEach((sample, index) => {
                const turnIndex = sample.turn_index;
                const correctTypeEl = document.getElementById(`correct_type_${turnIndex}`);
                const typeAccuracyEl = document.getElementById(`type_accuracy_${turnIndex}`);
                const summaryQualityEl = document.getElementById(`summary_quality_${turnIndex}`);
                const summaryCompletenessEl = document.getElementById(`summary_completeness_${turnIndex}`);
                const notesEl = document.getElementById(`notes_${turnIndex}`);

                // 값 가져오기 (null 체크)
                const correctType = correctTypeEl ? correctTypeEl.value : '';
                const typeAccuracy = typeAccuracyEl ? typeAccuracyEl.value : '';
                const summaryQuality = summaryQualityEl ? summaryQualityEl.value : '';
                const summaryCompleteness = summaryCompletenessEl ? summaryCompletenessEl.value : '';
                const notes = notesEl ? notesEl.value : '';

                // manual_review 업데이트 (빈 문자열은 null로 처리)
                sample.manual_review.correct_type = correctType && correctType.trim() !== '' ? correctType : null;
                sample.manual_review.type_accuracy = typeAccuracy && typeAccuracy.trim() !== '' ? parseInt(typeAccuracy) : null;
                sample.manual_review.summary_quality = summaryQuality && summaryQuality.trim() !== '' ? parseInt(summaryQuality) : null;
                sample.manual_review.summary_completeness = summaryCompleteness && summaryCompleteness.trim() !== '' ? parseInt(summaryCompleteness) : null;
                sample.manual_review.notes = notes ? notes.trim() : '';
            });

            // 타임스탬프 포함 파일명 생성
            const now = new Date();
            const timestamp = now.getFullYear().toString() +
                String(now.getMonth() + 1).padStart(2, '0') +
                String(now.getDate()).padStart(2, '0') + '_' +
                String(now.getHours()).padStart(2, '0') +
                String(now.getMinutes()).padStart(2, '0') +
                String(now.getSeconds()).padStart(2, '0');
            const filename = `manual_review_updated_${timestamp}.json`;

            // JSON 문자열 생성 (UTF-8 BOM 없이)
            const jsonStr = JSON.stringify(updatedData, null, 2);
            const blob = new Blob(['\\ufeff' + jsonStr], { type: 'application/json;charset=utf-8;' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            // 검증 완료 수 계산
            const reviewedCount = updatedData.samples.filter(s => s.manual_review.correct_type !== null).length;
            alert(`JSON 파일이 다운로드되었습니다!\\n파일명: ${filename}\\n검증 완료: ${reviewedCount}/${updatedData.samples.length}개`);
        }
```

저장 로직 개선 중: `exportToJSON()` 함수 수정 및 저장 형식 검증.


```python
"""
이벤트 정규화 결과 평가 도구

Phase 3.3: 결과 평가 방법 구축
- 정성적 평가 도구 (수동 검증 데이터셋 생성 및 평가)
- Golden 파일 관리 도구 (회귀 테스트용)
"""

import json
import random
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from collections import Counter, defaultdict

from backend.core.models import Event, EventType, Turn


def create_manual_review_dataset(
    events: List[Event],
    turns: List[Turn],
    output_file: Optional[Path] = None,
    sample_size: int = 30,
    min_per_type: int = 3,
) -> Dict[str, Any]:
    """
    수동 검증용 데이터셋 생성

    다양한 타입을 균등하게 샘플링하여 수동 검증용 JSON 파일 생성

    Args:
        events: 평가할 Event 리스트
        turns: 원본 Turn 리스트 (Event와 매칭용)
        output_file: 출력 파일 경로 (None이면 자동 생성)
        sample_size: 샘플 크기 (기본값: 30)
        min_per_type: 타입별 최소 샘플 수 (기본값: 3)

    Returns:
        생성된 데이터셋 딕셔너리
    """
    # 1. 타입별 이벤트 그룹화
    events_by_type: Dict[EventType, List[Event]] = defaultdict(list)
    for event in events:
        events_by_type[event.type].append(event)

    # 2. 타입별 샘플링 (최소 개수 보장)
    sampled_events: List[Event] = []
    sampled_indices: set = set()

    # 각 타입에서 최소 개수만큼 샘플링
    for event_type, type_events in events_by_type.items():
        if len(type_events) > 0:
            min_samples = min(min_per_type, len(type_events))
            samples = random.sample(type_events, min_samples)
            sampled_events.extend(samples)
            sampled_indices.update(e.turn_ref for e in samples)

    # 3. 나머지 샘플을 랜덤하게 추가 (총 sample_size까지)
    remaining_events = [e for e in events if e.turn_ref not in sampled_indices]
    if len(sampled_events) < sample_size and len(remaining_events) > 0:
        additional_needed = sample_size - len(sampled_events)
        additional_samples = random.sample(
            remaining_events, min(additional_needed, len(remaining_events))
        )
        sampled_events.extend(additional_samples)

    # 4. turn_ref 기준으로 정렬
    sampled_events.sort(key=lambda e: e.turn_ref)

    # 5. Turn 정보 매칭
    turns_dict = {turn.turn_index: turn for turn in turns}

    # 6. 데이터셋 구성
    dataset = {
        "metadata": {
            "total_events": len(events),
            "total_turns": len(turns),
            "sample_size": len(sampled_events),
            "event_type_distribution": {
                event_type.value: len(type_events)
                for event_type, type_events in events_by_type.items()
            },
            "sampled_type_distribution": {
                event_type.value: sum(1 for e in sampled_events if e.type == event_type)
                for event_type in EventType
            },
        },
        "guidelines": {
            "event_type_definition": {
                "status_review": "상태 리뷰 (현황 점검, 상태 확인)",
                "plan": "계획 수립 (작업 계획, 단계별 계획)",
                "artifact": "파일/경로 관련 (파일 생성/수정/언급)",
                "debug": "디버깅 (에러, 원인, 해결, 검증)",
                "completion": "완료 (작업 완료, 성공)",
                "next_step": "다음 단계 (다음 작업, 진행)",
                "turn": "일반 대화 (기본값)",
            },
            "evaluation_criteria": {
                "event_type_accuracy": "이벤트 타입이 Turn의 내용과 일치하는가?",
                "summary_quality": "요약이 Turn의 핵심 내용을 잘 반영하는가? (1-5점)",
                "summary_completeness": "요약이 중요한 정보를 누락하지 않는가? (1-5점)",
            },
        },
        "samples": [],
    }

    # 7. 샘플 데이터 구성
    for event in sampled_events:
        turn = turns_dict.get(event.turn_ref)
        if turn is None:
            continue

        sample = {
            "event_id": f"EVT-{event.turn_ref:03d}",
            "turn_index": event.turn_ref,
            "turn_speaker": turn.speaker,
            "turn_body": turn.body[:500],  # 처음 500자만 (전체는 너무 길 수 있음)
            "current_event": {
                "type": event.type.value,
                "summary": event.summary,
                "processing_method": event.processing_method,
                "artifacts_count": len(event.artifacts),
                "snippets_count": len(event.snippet_refs),
            },
            "manual_review": {
                "correct_type": None,  # 수동 입력: 올바른 타입
                "correct_summary": None,  # 수동 입력: 올바른 요약 (선택적)
                "type_accuracy": None,  # 수동 입력: 타입 정확도 (1-5점)
                "summary_quality": None,  # 수동 입력: 요약 품질 (1-5점)
                "summary_completeness": None,  # 수동 입력: 요약 완전성 (1-5점)
                "notes": "",  # 수동 입력: 추가 메모
            },
        }
        dataset["samples"].append(sample)

    # 8. 파일 저장
    if output_file is None:
        output_file = Path("tests/manual_review") / "manual_review_dataset.json"

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    return dataset


def evaluate_manual_review(
    review_file: Path, events: Optional[List[Event]] = None, turns: Optional[List[Turn]] = None
) -> Dict[str, Any]:
    """
    수동 검증 결과 평가

    수동 검증 결과를 로드하여 정확도 계산 및 분석

    Args:
        review_file: 수동 검증 결과 파일 경로
        events: 원본 Event 리스트 (선택적, 비교용)
        turns: 원본 Turn 리스트 (선택적, 비교용)

    Returns:
        평가 결과 딕셔너리
    """
    # 1. 수동 검증 결과 로드
    with open(review_file, "r", encoding="utf-8") as f:
        review_data = json.load(f)

    samples = review_data.get("samples", [])
    if len(samples) == 0:
        return {"error": "No samples found in review file"}

    # 2. 타입 분류 정확도 계산
    type_correct = 0
    type_total = 0
    type_confusion: Dict[Tuple[str, str], int] = defaultdict(int)  # (predicted, actual)

    # 3. Summary 품질 점수 계산
    summary_quality_scores: List[int] = []
    summary_completeness_scores: List[int] = []
    type_accuracy_scores: List[int] = []

    # 4. 처리 방법별 통계
    method_stats: Dict[str, Dict[str, int]] = defaultdict(lambda: {"correct": 0, "total": 0})

    for sample in samples:
        current = sample.get("current_event", {})
        review = sample.get("manual_review", {})

        current_type = current.get("type")
        correct_type = review.get("correct_type")
        processing_method = current.get("processing_method", "unknown")

        # 타입 정확도
        if correct_type is not None:
            type_total += 1
            if current_type == correct_type:
                type_correct += 1
            type_confusion[(current_type, correct_type)] += 1

            method_stats[processing_method]["total"] += 1
            if current_type == correct_type:
                method_stats[processing_method]["correct"] += 1

        # Summary 품질 점수
        if review.get("summary_quality") is not None:
            summary_quality_scores.append(review["summary_quality"])

        if review.get("summary_completeness") is not None:
            summary_completeness_scores.append(review["summary_completeness"])

        if review.get("type_accuracy") is not None:
            type_accuracy_scores.append(review["type_accuracy"])

    # 5. 정확도 계산
    type_accuracy = type_correct / type_total if type_total > 0 else 0.0

    # 6. 처리 방법별 정확도
    method_accuracy = {}
    for method, stats in method_stats.items():
        if stats["total"] > 0:
            method_accuracy[method] = {
                "accuracy": stats["correct"] / stats["total"],
                "correct": stats["correct"],
                "total": stats["total"],
            }

    # 7. 혼동 행렬 생성
    confusion_matrix = {}
    for (predicted, actual), count in type_confusion.items():
        if predicted not in confusion_matrix:
            confusion_matrix[predicted] = {}
        confusion_matrix[predicted][actual] = count

    # 8. 평균 점수 계산
    avg_summary_quality = (
        sum(summary_quality_scores) / len(summary_quality_scores)
        if summary_quality_scores
        else None
    )
    avg_summary_completeness = (
        sum(summary_completeness_scores) / len(summary_completeness_scores)
        if summary_completeness_scores
        else None
    )
    avg_type_accuracy = (
        sum(type_accuracy_scores) / len(type_accuracy_scores) if type_accuracy_scores else None
    )

    # 9. 결과 구성
    evaluation_result = {
        "metadata": {
            "review_file": str(review_file),
            "total_samples": len(samples),
            "evaluated_samples": type_total,
        },
        "type_classification": {
            "accuracy": type_accuracy,
            "correct": type_correct,
            "total": type_total,
            "confusion_matrix": confusion_matrix,
        },
        "summary_quality": {
            "average_quality": avg_summary_quality,
            "average_completeness": avg_summary_completeness,
            "samples_count": len(summary_quality_scores),
        },
        "type_accuracy_scores": {
            "average": avg_type_accuracy,
            "samples_count": len(type_accuracy_scores),
        },
        "method_comparison": method_accuracy,
    }

    return evaluation_result


def create_golden_file_from_manual_review(
    review_file: Path,
    results_file: Path,
    output_file: Optional[Path] = None,
    min_accuracy: float = 0.85,
    apply_corrections: bool = True,
) -> Dict[str, Any]:
    """
    수동 검증 결과를 기반으로 Golden 파일 생성

    수동 검증 데이터셋 파일과 E2E 테스트 결과 파일을 사용하여
    검증된 결과를 Golden 파일로 저장합니다.

    Args:
        review_file: 수동 검증 결과 파일 경로 (manual_review_dataset_*.json)
        results_file: E2E 테스트 결과 파일 경로 (event_normalizer_e2e_llm_*.json)
        output_file: 출력 Golden 파일 경로 (None이면 자동 생성)
        min_accuracy: 최소 정확도 요구사항 (기본값: 0.85)
        apply_corrections: 수동 검증에서 correct_type이 있으면 적용할지 여부

    Returns:
        생성 결과 딕셔너리
    """
    import json

    # 1. 수동 검증 결과 로드
    with open(review_file, "r", encoding="utf-8") as f:
        review_data = json.load(f)

    # 2. E2E 테스트 결과 로드
    with open(results_file, "r", encoding="utf-8") as f:
        results_data = json.load(f)

    # 3. Event 리스트 복원
    from backend.core.models import Event, EventType, Turn, SessionMeta

    events_dict = {e["turn_ref"]: Event(**e) for e in results_data.get("events", [])}
    turns_dict = {
        t["turn_index"]: Turn(**t) for t in results_data.get("turns", []) if "turn_index" in t
    }

    # SessionMeta 복원
    session_meta_dict = results_data.get("session_meta", {})
    session_meta = SessionMeta(**session_meta_dict) if session_meta_dict else None

    # 4. 수동 검증 결과 평가
    events_list = list(events_dict.values())
    turns_list = list(turns_dict.values())

    evaluation = evaluate_manual_review(review_file, events_list, turns_list)

    # 5. 정확도 확인
    type_accuracy = evaluation.get("type_classification", {}).get("accuracy", 0.0)

    if type_accuracy < min_accuracy:
        return {
            "created": False,
            "reason": f"정확도가 너무 낮음: {type_accuracy:.2%} < {min_accuracy:.2%}",
            "evaluation": evaluation,
            "min_accuracy_required": min_accuracy,
        }

    # 6. 수동 검증 결과를 반영하여 "올바른" 이벤트 생성 (선택적)
    corrected_events = []

    if apply_corrections:
        # turn_ref → correct_type 매핑
        corrections = {}
        for sample in review_data.get("samples", []):
            turn_ref = sample.get("turn_index")
            correct_type_str = sample.get("manual_review", {}).get("correct_type")
            if turn_ref is not None and correct_type_str is not None:
                try:
                    corrections[turn_ref] = EventType(correct_type_str)
                except ValueError:
                    # 잘못된 타입은 무시
                    pass

        # 이벤트 수정 (correct_type이 있으면 적용)
        for event in events_list:
            if event.turn_ref in corrections:
                # 수동 검증 결과 반영
                corrected_event = event.model_copy()
                corrected_event.type = corrections[event.turn_ref]
                corrected_events.append(corrected_event)
            else:
                corrected_events.append(event)
    else:
        corrected_events = events_list

    # 7. Golden 파일 생성 (수정된 이벤트 사용)
    if output_file is None:
        output_file = Path("tests/golden") / "event_normalizer_golden.json"

    golden_data = create_golden_file(
        events=corrected_events,
        turns=turns_list,
        session_meta=session_meta,
        output_file=output_file,
        description=f"수동 검증 기반 Golden 파일 (정확도: {type_accuracy:.2%}, corrections_applied: {apply_corrections})",
    )

    return {
        "created": True,
        "file_path": str(output_file),
        "type_accuracy": type_accuracy,
        "evaluation": evaluation,
        "corrections_applied": apply_corrections,
        "corrected_count": (
            len([e for e in corrected_events if e.turn_ref in corrections])
            if apply_corrections
            else 0
        ),
    }


def create_golden_file(
    events: List[Event],
    turns: List[Turn],
    session_meta: Any,
    output_file: Optional[Path] = None,
    description: str = "",
) -> Dict[str, Any]:
    """
    Golden 파일 생성 (회귀 테스트용)

    개선 사이클 완료 후 현재 결과를 Golden 파일로 저장

    Args:
        events: Event 리스트
        turns: Turn 리스트
        session_meta: SessionMeta 객체
        output_file: 출력 파일 경로 (None이면 자동 생성)
        description: Golden 파일 설명

    Returns:
        생성된 Golden 파일 딕셔너리
    """
    from datetime import datetime

    golden_data = {
        "metadata": {
            "created_at": datetime.now().isoformat(),
            "description": description,
            "session_id": session_meta.session_id if session_meta else "unknown",
            "total_events": len(events),
            "total_turns": len(turns),
        },
        "event_type_distribution": {
            event_type.value: sum(1 for e in events if e.type == event_type)
            for event_type in EventType
        },
        "processing_method_distribution": {
            method: sum(1 for e in events if e.processing_method == method)
            for method in ["regex", "llm"]
        },
        "events": [event.dict() for event in events],
        "turns": [turn.dict() for turn in turns],
    }

    if output_file is None:
        output_file = Path("tests/golden") / "event_normalizer_golden.json"

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(golden_data, f, ensure_ascii=False, indent=2)

    return golden_data


def compare_with_golden(
    current_events: List[Event], golden_file: Path, similarity_threshold: float = 0.95
) -> Dict[str, Any]:
    """
    Golden 파일과 현재 결과 비교 (회귀 감지)

    Args:
        current_events: 현재 Event 리스트
        golden_file: Golden 파일 경로
        similarity_threshold: 유사도 임계값 (기본값: 0.95, 95% 미만 시 회귀)

    Returns:
        비교 결과 딕셔너리
    """
    # 1. Golden 파일 로드
    with open(golden_file, "r", encoding="utf-8") as f:
        golden_data = json.load(f)

    golden_events = golden_data.get("events", [])
    golden_metadata = golden_data.get("metadata", {})

    # 2. 이벤트 수 비교
    current_count = len(current_events)
    golden_count = len(golden_events)
    count_match = current_count == golden_count

    # 3. 타입 분포 비교
    current_type_dist = Counter(e.type.value for e in current_events)
    golden_type_dist = Counter(e.get("type") for e in golden_events if isinstance(e, dict))

    type_dist_similarity = _calculate_distribution_similarity(current_type_dist, golden_type_dist)

    # 4. 타입 일치 비교 (turn_ref 기준)
    type_matches = 0
    type_total = 0

    golden_events_dict = {e.get("turn_ref"): e for e in golden_events if isinstance(e, dict)}

    for event in current_events:
        golden_event = golden_events_dict.get(event.turn_ref)
        if golden_event:
            type_total += 1
            if event.type.value == golden_event.get("type"):
                type_matches += 1

    type_accuracy = type_matches / type_total if type_total > 0 else 0.0

    # 5. 회귀 감지
    is_regression = (
        not count_match
        or type_dist_similarity < similarity_threshold
        or type_accuracy < similarity_threshold
    )

    # 6. 결과 구성
    comparison_result = {
        "golden_file": str(golden_file),
        "golden_metadata": golden_metadata,
        "comparison": {
            "event_count": {"current": current_count, "golden": golden_count, "match": count_match},
            "type_distribution": {
                "current": dict(current_type_dist),
                "golden": dict(golden_type_dist),
                "similarity": type_dist_similarity,
            },
            "type_accuracy": {
                "accuracy": type_accuracy,
                "matches": type_matches,
                "total": type_total,
            },
        },
        "regression_detected": is_regression,
        "regression_reasons": [],
    }

    if not count_match:
        comparison_result["regression_reasons"].append(
            f"Event count mismatch: current={current_count}, golden={golden_count}"
        )

    if type_dist_similarity < similarity_threshold:
        comparison_result["regression_reasons"].append(
            f"Type distribution similarity too low: {type_dist_similarity:.2%} < {similarity_threshold:.2%}"
        )

    if type_accuracy < similarity_threshold:
        comparison_result["regression_reasons"].append(
            f"Type accuracy too low: {type_accuracy:.2%} < {similarity_threshold:.2%}"
        )

    return comparison_result


def _calculate_distribution_similarity(dist1: Counter, dist2: Counter) -> float:
    """
    두 분포의 유사도 계산 (Jaccard 유사도 기반)

    Args:
        dist1: 첫 번째 분포 (Counter)
        dist2: 두 번째 분포 (Counter)

    Returns:
        유사도 (0.0 ~ 1.0)
    """
    all_keys = set(dist1.keys()) | set(dist2.keys())
    if len(all_keys) == 0:
        return 1.0

    total_diff = 0
    total_sum = 0

    for key in all_keys:
        val1 = dist1.get(key, 0)
        val2 = dist2.get(key, 0)
        total_sum += max(val1, val2)
        total_diff += abs(val1 - val2)

    if total_sum == 0:
        return 1.0

    similarity = 1.0 - (total_diff / total_sum)
    return max(0.0, min(1.0, similarity))


def create_all_events_html_review_dataset(
    events: List[Event],
    turns: List[Turn],
    output_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    모든 이벤트를 포함한 HTML 형식 수동 검증 데이터셋 생성

    HTML 파일에서 타입 수정 후 JavaScript로 JSON 파일 생성

    Args:
        events: 평가할 Event 리스트 (모두 포함)
        turns: 원본 Turn 리스트
        output_dir: 출력 디렉토리 (None이면 자동 생성)

    Returns:
        생성된 데이터셋 딕셔너리
    """
    from datetime import datetime

    if output_dir is None:
        output_dir = Path("tests/manual_review")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = output_dir / f"all_events_html_review_{timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Turn 정보 매칭
    turns_dict = {turn.turn_index: turn for turn in turns}

    # 이벤트를 turn_ref 기준으로 정렬
    sorted_events = sorted(events, key=lambda e: e.turn_ref)

    # 데이터셋 구성 (JSON용)
    dataset = {
        "metadata": {
            "total_events": len(events),
            "total_turns": len(turns),
            "created_at": timestamp,
        },
        "guidelines": {
            "event_type_definition": {
                "status_review": "상태 리뷰 (현황 점검, 상태 확인)",
                "plan": "계획 수립 (작업 계획, 단계별 계획)",
                "artifact": "파일/경로 관련 (파일 생성/수정/언급)",
                "debug": "디버깅 (에러, 원인, 해결, 검증)",
                "completion": "완료 (작업 완료, 성공)",
                "next_step": "다음 단계 (다음 작업, 진행)",
                "turn": "일반 대화 (기본값)",
            }
        },
        "samples": [],
    }

    # 샘플 데이터 구성
    for event in sorted_events:
        turn = turns_dict.get(event.turn_ref)
        if turn is None:
            continue

        sample = {
            "event_id": f"EVT-{event.turn_ref:03d}",
            "turn_index": event.turn_ref,
            "turn_speaker": turn.speaker,
            "turn_body": turn.body,
            "turn_body_length": len(turn.body),
            "current_event": {
                "type": event.type.value,
                "summary": event.summary,
                "processing_method": event.processing_method,
                "artifacts_count": len(event.artifacts),
                "snippets_count": len(event.snippet_refs),
                "artifacts": event.artifacts,
                "snippet_refs": event.snippet_refs,
            },
            "manual_review": {
                "correct_type": None,
                "type_accuracy": None,
                "summary_quality": None,
                "summary_completeness": None,
                "notes": "",
            },
        }
        dataset["samples"].append(sample)

    # JSON 파일 저장 (초기 데이터)
    json_file = output_dir / "manual_review_data.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    # HTML 파일 생성
    html_file = output_dir / "manual_review.html"
    html_content = generate_html_review_page(dataset)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[INFO] HTML manual review dataset created:")
    print(f"  HTML file: {html_file}")
    print(f"  JSON file: {json_file}")
    print(f"  Total events: {len(dataset['samples'])}")
    print(f"\n[INFO] 사용 방법:")
    print(f"  1. {html_file} 파일을 브라우저에서 열기")
    print(f"  2. 각 이벤트의 correct_type 선택 및 notes 입력")
    print(f"  3. 'Export to JSON' 버튼 클릭하여 수정 결과 저장")

    return dataset


def generate_html_review_page(dataset: Dict[str, Any]) -> str:
    """HTML 리뷰 페이지 생성"""

    event_types = ["status_review", "plan", "artifact", "debug", "completion", "next_step", "turn"]

    # HTML 템플릿
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>이벤트 정규화 수동 검증 - 모든 이벤트</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .header .stats {{
            color: #666;
            font-size: 14px;
        }}
        .controls {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .btn {{
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
        }}
        .btn-primary {{
            background: #007bff;
            color: white;
        }}
        .btn-primary:hover {{
            background: #0056b3;
        }}
        .btn-success {{
            background: #28a745;
            color: white;
        }}
        .btn-success:hover {{
            background: #218838;
        }}
        .event-card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .event-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 2px solid #eee;
        }}
        .event-id {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }}
        .event-type-badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }}
        .type-status_review {{ background: #e3f2fd; color: #1976d2; }}
        .type-plan {{ background: #f3e5f5; color: #7b1fa2; }}
        .type-artifact {{ background: #fff3e0; color: #e65100; }}
        .type-debug {{ background: #ffebee; color: #c62828; }}
        .type-completion {{ background: #e8f5e9; color: #2e7d32; }}
        .type-next_step {{ background: #e0f2f1; color: #00695c; }}
        .type-turn {{ background: #f5f5f5; color: #616161; }}
        .review-section {{
            margin-top: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 4px;
        }}
        .form-group {{
            margin-bottom: 15px;
        }}
        .form-group label {{
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
            color: #333;
        }}
        .form-group select, .form-group input {{
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }}
        .form-group textarea {{
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            min-height: 80px;
            resize: vertical;
        }}
        .turn-body {{
            background: #f9f9f9;
            padding: 15px;
            border-radius: 4px;
            white-space: pre-wrap;
            word-wrap: break-word;
            max-height: 400px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.5;
        }}
        .summary-box {{
            background: #fff;
            padding: 15px;
            border-left: 4px solid #007bff;
            margin: 15px 0;
            border-radius: 4px;
        }}
        .summary-box h4 {{
            margin-bottom: 10px;
            color: #007bff;
        }}
        .toggle-btn {{
            background: #6c757d;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            margin-top: 10px;
        }}
        .toggle-btn:hover {{
            background: #5a6268;
        }}
        .collapsed {{
            display: none;
        }}
        .progress-bar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: #e0e0e0;
            z-index: 1000;
        }}
        .progress-fill {{
            height: 100%;
            background: #007bff;
            transition: width 0.3s;
        }}
    </style>
</head>
<body>
    <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%"></div>
    </div>

    <div class="container">
        <div class="header">
            <h1>이벤트 정규화 수동 검증</h1>
            <div class="stats">
                총 이벤트: {dataset['metadata']['total_events']}개 |
                검증 완료: <span id="reviewedCount">0</span>개 |
                진행률: <span id="progressPercent">0</span>%
            </div>
        </div>

        <div class="controls">
            <button class="btn btn-primary" onclick="scrollToNextUnreviewed()">다음 미검증 항목으로</button>
            <button class="btn btn-primary" onclick="scrollToPrevUnreviewed()">이전 미검증 항목으로</button>
            <button class="btn btn-success" onclick="exportToJSON()">Export to JSON</button>
            <button class="btn btn-primary" onclick="saveProgress()">진행 상황 저장 (로컬)</button>
        </div>

        <div id="eventList">
"""

    # 각 이벤트 카드 생성
    for i, sample in enumerate(dataset["samples"]):
        event_id = sample["event_id"]
        turn_index = sample["turn_index"]
        turn_speaker = sample["turn_speaker"]
        turn_body = sample["turn_body"]
        turn_body_length = sample["turn_body_length"]
        current_type = sample["current_event"]["type"]
        summary = sample["current_event"]["summary"]
        processing_method = sample["current_event"]["processing_method"]

        # HTML 이스케이프 처리
        import html as html_module

        escaped_turn_body = html_module.escape(turn_body)
        escaped_summary = html_module.escape(summary)

        # 긴 텍스트는 접기/펼치기
        is_long_text = turn_body_length > 2000
        display_text = turn_body[:2000] if is_long_text else turn_body
        escaped_display_text = html_module.escape(display_text)
        escaped_remaining_text = html_module.escape(turn_body[2000:]) if is_long_text else ""

        html += f"""
            <div class="event-card" id="event-{turn_index}" data-reviewed="false">
                <div class="event-header">
                    <div>
                        <span class="event-id">{event_id}</span>
                        <span style="margin-left: 10px; color: #666;">Turn {turn_index} | {turn_speaker}</span>
                    </div>
                    <span class="event-type-badge type-{current_type}">{current_type}</span>
                </div>

                <div class="summary-box">
                    <h4>현재 이벤트 Summary</h4>
                    <div>{escaped_summary}</div>
                    <div style="margin-top: 10px; font-size: 12px; color: #666;">
                        처리 방법: {processing_method} |
                        Artifacts: {sample['current_event']['artifacts_count']}개 |
                        Snippets: {sample['current_event']['snippets_count']}개
                    </div>
                </div>

                <div class="form-group">
                    <label>원본 Turn 텍스트 (총 {turn_body_length}자)</label>
                    <div class="turn-body" id="turn-body-{turn_index}">
                        {escaped_display_text}
"""

        if is_long_text:
            html += f"""
                        <div class="collapsed" id="turn-body-full-{turn_index}">
                            {escaped_remaining_text}
                        </div>
                        <button class="toggle-btn" onclick="toggleText({turn_index})">전체 텍스트 보기/접기</button>
"""

        html += f"""
                    </div>
                </div>

                <div class="review-section">
                    <h3 style="margin-bottom: 15px;">수동 검증</h3>

                    <div class="form-group">
                        <label for="correct_type_{turn_index}">올바른 타입 (correct_type) *</label>
                        <select id="correct_type_{turn_index}" onchange="markAsReviewed({turn_index})">
                            <option value="">선택하세요</option>
"""

        for event_type in event_types:
            selected = "selected" if event_type == current_type else ""
            html += f'                            <option value="{event_type}" {selected}>{event_type}</option>\n'

        html += f"""
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="type_accuracy_{turn_index}">타입 정확도 (1-5점)</label>
                        <input type="number" id="type_accuracy_{turn_index}" min="1" max="5" placeholder="1-5">
                    </div>

                    <div class="form-group">
                        <label for="summary_quality_{turn_index}">요약 품질 (1-5점)</label>
                        <input type="number" id="summary_quality_{turn_index}" min="1" max="5" placeholder="1-5">
                    </div>

                    <div class="form-group">
                        <label for="summary_completeness_{turn_index}">요약 완전성 (1-5점)</label>
                        <input type="number" id="summary_completeness_{turn_index}" min="1" max="5" placeholder="1-5">
                    </div>

                    <div class="form-group">
                        <label for="notes_{turn_index}">메모 (notes)</label>
                        <textarea id="notes_{turn_index}" placeholder="추가 메모를 입력하세요..."></textarea>
                    </div>
                </div>
            </div>
"""

    # JavaScript 코드
    html += (
        """
        </div>
    </div>

    <script>
        const eventData = """
        + json.dumps(dataset, ensure_ascii=False)
        + """;

        // 텍스트 접기/펼치기
        function toggleText(turnIndex) {
            const fullText = document.getElementById(`turn-body-full-${turnIndex}`);
            const btn = event.target;
            if (fullText.classList.contains('collapsed')) {
                fullText.classList.remove('collapsed');
                btn.textContent = '텍스트 접기';
            } else {
                fullText.classList.add('collapsed');
                btn.textContent = '전체 텍스트 보기';
            }
        }

        // 검증 완료 표시
        function markAsReviewed(turnIndex) {
            const card = document.getElementById(`event-${turnIndex}`);
            const correctType = document.getElementById(`correct_type_${turnIndex}`).value;
            if (correctType) {
                card.setAttribute('data-reviewed', 'true');
                card.style.borderLeft = '4px solid #28a745';
            } else {
                card.setAttribute('data-reviewed', 'false');
                card.style.borderLeft = 'none';
            }
            updateProgress();
        }

        // 진행률 업데이트
        function updateProgress() {
            const total = eventData.samples.length;
            const reviewed = document.querySelectorAll('[data-reviewed="true"]').length;
            const percent = Math.round((reviewed / total) * 100);

            document.getElementById('reviewedCount').textContent = reviewed;
            document.getElementById('progressPercent').textContent = percent;
            document.getElementById('progressFill').style.width = percent + '%';
        }

        // 다음 미검증 항목으로 스크롤
        function scrollToNextUnreviewed() {
            const unreviewed = document.querySelector('[data-reviewed="false"]');
            if (unreviewed) {
                unreviewed.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } else {
                alert('모든 항목을 검증했습니다!');
            }
        }

        // 이전 미검증 항목으로 스크롤
        function scrollToPrevUnreviewed() {
            const allCards = Array.from(document.querySelectorAll('.event-card'));
            const currentIndex = allCards.findIndex(card => {
                const rect = card.getBoundingClientRect();
                return rect.top > 0 && rect.top < window.innerHeight;
            });

            for (let i = currentIndex - 1; i >= 0; i--) {
                if (allCards[i].getAttribute('data-reviewed') === 'false') {
                    allCards[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
                    return;
                }
            }
            alert('이전 미검증 항목이 없습니다.');
        }

        // JSON으로 내보내기
        function exportToJSON() {
            const updatedData = JSON.parse(JSON.stringify(eventData));

            updatedData.samples.forEach((sample, index) => {
                const turnIndex = sample.turn_index;
                const correctTypeEl = document.getElementById(`correct_type_${turnIndex}`);
                const typeAccuracyEl = document.getElementById(`type_accuracy_${turnIndex}`);
                const summaryQualityEl = document.getElementById(`summary_quality_${turnIndex}`);
                const summaryCompletenessEl = document.getElementById(`summary_completeness_${turnIndex}`);
                const notesEl = document.getElementById(`notes_${turnIndex}`);

                // 값 가져오기 (null 체크)
                const correctType = correctTypeEl ? correctTypeEl.value : '';
                const typeAccuracy = typeAccuracyEl ? typeAccuracyEl.value : '';
                const summaryQuality = summaryQualityEl ? summaryQualityEl.value : '';
                const summaryCompleteness = summaryCompletenessEl ? summaryCompletenessEl.value : '';
                const notes = notesEl ? notesEl.value : '';

                // manual_review 업데이트 (빈 문자열은 null로 처리, 숫자는 유효성 검사)
                sample.manual_review.correct_type = correctType && correctType.trim() !== '' ? correctType : null;
                
                // 숫자 필드는 빈 문자열이 아니고 유효한 숫자인 경우만 저장
                if (typeAccuracy && typeAccuracy.trim() !== '') {
                    const acc = parseInt(typeAccuracy);
                    sample.manual_review.type_accuracy = (!isNaN(acc) && acc >= 1 && acc <= 5) ? acc : null;
                } else {
                    sample.manual_review.type_accuracy = null;
                }
                
                if (summaryQuality && summaryQuality.trim() !== '') {
                    const qual = parseInt(summaryQuality);
                    sample.manual_review.summary_quality = (!isNaN(qual) && qual >= 1 && qual <= 5) ? qual : null;
                } else {
                    sample.manual_review.summary_quality = null;
                }
                
                if (summaryCompleteness && summaryCompleteness.trim() !== '') {
                    const comp = parseInt(summaryCompleteness);
                    sample.manual_review.summary_completeness = (!isNaN(comp) && comp >= 1 && comp <= 5) ? comp : null;
                } else {
                    sample.manual_review.summary_completeness = null;
                }
                
                sample.manual_review.notes = notes ? notes.trim() : '';
            });

            // 타임스탬프 포함 파일명 생성
            const now = new Date();
            const timestamp = now.getFullYear().toString() +
                String(now.getMonth() + 1).padStart(2, '0') +
                String(now.getDate()).padStart(2, '0') + '_' +
                String(now.getHours()).padStart(2, '0') +
                String(now.getMinutes()).padStart(2, '0') +
                String(now.getSeconds()).padStart(2, '0');
            const filename = `manual_review_updated_${timestamp}.json`;

            // JSON 문자열 생성 (UTF-8 인코딩)
            const jsonStr = JSON.stringify(updatedData, null, 2);
            const blob = new Blob([jsonStr], { type: 'application/json;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            // 검증 완료 수 계산
            const reviewedCount = updatedData.samples.filter(s => s.manual_review.correct_type !== null).length;
            alert(`JSON 파일이 다운로드되었습니다!\\n파일명: ${filename}\\n검증 완료: ${reviewedCount}/${updatedData.samples.length}개`);
        }

        // 진행 상황 저장 (로컬 스토리지)
        function saveProgress() {{
            const progress = {{}};
            eventData.samples.forEach(sample => {{
                const turnIndex = sample.turn_index;
                progress[turnIndex] = {{
                    correct_type: document.getElementById(`correct_type_${{turnIndex}}`).value,
                    type_accuracy: document.getElementById(`type_accuracy_${{turnIndex}}`).value,
                    summary_quality: document.getElementById(`summary_quality_${{turnIndex}}`).value,
                    summary_completeness: document.getElementById(`summary_completeness_${{turnIndex}}`).value,
                    notes: document.getElementById(`notes_${{turnIndex}}`).value
                }};
            }});
            localStorage.setItem('reviewProgress', JSON.stringify(progress));
            alert('진행 상황이 저장되었습니다! (브라우저 로컬 스토리지)');
        }}

        // 진행 상황 복원
        function loadProgress() {{
            const saved = localStorage.getItem('reviewProgress');
            if (saved) {{
                const progress = JSON.parse(saved);
                Object.keys(progress).forEach(turnIndex => {{
                    const p = progress[turnIndex];
                    if (p.correct_type) document.getElementById(`correct_type_${{turnIndex}}`).value = p.correct_type;
                    if (p.type_accuracy) document.getElementById(`type_accuracy_${{turnIndex}}`).value = p.type_accuracy;
                    if (p.summary_quality) document.getElementById(`summary_quality_${{turnIndex}}`).value = p.summary_quality;
                    if (p.summary_completeness) document.getElementById(`summary_completeness_${{turnIndex}}`).value = p.summary_completeness;
                    if (p.notes) document.getElementById(`notes_${{turnIndex}}`).value = p.notes;
                    markAsReviewed(parseInt(turnIndex));
                }});
                alert('저장된 진행 상황을 복원했습니다!');
            }}
        }}

        // 페이지 로드 시 진행 상황 복원
        window.addEventListener('load', () => {{
            if (confirm('저장된 진행 상황을 복원하시겠습니까?')) {{
                loadProgress();
            }}
            updateProgress();
        }});
    </script>
</body>
</html>
"""
    )

    return html

```

개선된 HTML 생성 스크립트 재실행 중.


생성된 HTML 파일 확인 및 저장 안내 메시지 추가 중.


```python
    print(f"[INFO] HTML manual review dataset created:")
    print(f"  HTML file: {html_file}")
    print(f"  JSON file: {json_file}")
    print(f"  Total events: {len(dataset['samples'])}")
    print(f"\n[INFO] 사용 방법:")
    print(f"  1. {html_file} 파일을 브라우저에서 열기")
    print(f"  2. 각 이벤트의 correct_type 선택 및 notes 입력")
    print(f"  3. 'Export to JSON' 버튼 클릭하여 수정 결과 다운로드")
    print(f"  4. 다운로드한 JSON 파일을 다음 위치에 저장:")
    print(f"     {output_dir / 'manual_review_updated.json'}")
    print(f"\n[INFO] 저장 시 주의사항:")
    print(f"  - 다운로드한 파일명은 'manual_review_updated_YYYYMMDD_HHMMSS.json' 형식입니다")
    print(f"  - 파일을 '{output_dir / 'manual_review_updated.json'}'로 복사하거나 이름을 변경하세요")
    print(f"  - 또는 다운로드한 파일을 그대로 사용해도 됩니다 (타임스탬프 포함)")
```

생성된 HTML 파일의 `exportToJSON()` 함수 확인 중.


```python
"""
이벤트 정규화 결과 평가 도구

Phase 3.3: 결과 평가 방법 구축
- 정성적 평가 도구 (수동 검증 데이터셋 생성 및 평가)
- Golden 파일 관리 도구 (회귀 테스트용)
"""

import json
import random
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from collections import Counter, defaultdict

from backend.core.models import Event, EventType, Turn


def create_manual_review_dataset(
    events: List[Event],
    turns: List[Turn],
    output_file: Optional[Path] = None,
    sample_size: int = 30,
    min_per_type: int = 3,
) -> Dict[str, Any]:
    """
    수동 검증용 데이터셋 생성

    다양한 타입을 균등하게 샘플링하여 수동 검증용 JSON 파일 생성

    Args:
        events: 평가할 Event 리스트
        turns: 원본 Turn 리스트 (Event와 매칭용)
        output_file: 출력 파일 경로 (None이면 자동 생성)
        sample_size: 샘플 크기 (기본값: 30)
        min_per_type: 타입별 최소 샘플 수 (기본값: 3)

    Returns:
        생성된 데이터셋 딕셔너리
    """
    # 1. 타입별 이벤트 그룹화
    events_by_type: Dict[EventType, List[Event]] = defaultdict(list)
    for event in events:
        events_by_type[event.type].append(event)

    # 2. 타입별 샘플링 (최소 개수 보장)
    sampled_events: List[Event] = []
    sampled_indices: set = set()

    # 각 타입에서 최소 개수만큼 샘플링
    for event_type, type_events in events_by_type.items():
        if len(type_events) > 0:
            min_samples = min(min_per_type, len(type_events))
            samples = random.sample(type_events, min_samples)
            sampled_events.extend(samples)
            sampled_indices.update(e.turn_ref for e in samples)

    # 3. 나머지 샘플을 랜덤하게 추가 (총 sample_size까지)
    remaining_events = [e for e in events if e.turn_ref not in sampled_indices]
    if len(sampled_events) < sample_size and len(remaining_events) > 0:
        additional_needed = sample_size - len(sampled_events)
        additional_samples = random.sample(
            remaining_events, min(additional_needed, len(remaining_events))
        )
        sampled_events.extend(additional_samples)

    # 4. turn_ref 기준으로 정렬
    sampled_events.sort(key=lambda e: e.turn_ref)

    # 5. Turn 정보 매칭
    turns_dict = {turn.turn_index: turn for turn in turns}

    # 6. 데이터셋 구성
    dataset = {
        "metadata": {
            "total_events": len(events),
            "total_turns": len(turns),
            "sample_size": len(sampled_events),
            "event_type_distribution": {
                event_type.value: len(type_events)
                for event_type, type_events in events_by_type.items()
            },
            "sampled_type_distribution": {
                event_type.value: sum(1 for e in sampled_events if e.type == event_type)
                for event_type in EventType
            },
        },
        "guidelines": {
            "event_type_definition": {
                "status_review": "상태 리뷰 (현황 점검, 상태 확인)",
                "plan": "계획 수립 (작업 계획, 단계별 계획)",
                "artifact": "파일/경로 관련 (파일 생성/수정/언급)",
                "debug": "디버깅 (에러, 원인, 해결, 검증)",
                "completion": "완료 (작업 완료, 성공)",
                "next_step": "다음 단계 (다음 작업, 진행)",
                "turn": "일반 대화 (기본값)",
            },
            "evaluation_criteria": {
                "event_type_accuracy": "이벤트 타입이 Turn의 내용과 일치하는가?",
                "summary_quality": "요약이 Turn의 핵심 내용을 잘 반영하는가? (1-5점)",
                "summary_completeness": "요약이 중요한 정보를 누락하지 않는가? (1-5점)",
            },
        },
        "samples": [],
    }

    # 7. 샘플 데이터 구성
    for event in sampled_events:
        turn = turns_dict.get(event.turn_ref)
        if turn is None:
            continue

        sample = {
            "event_id": f"EVT-{event.turn_ref:03d}",
            "turn_index": event.turn_ref,
            "turn_speaker": turn.speaker,
            "turn_body": turn.body[:500],  # 처음 500자만 (전체는 너무 길 수 있음)
            "current_event": {
                "type": event.type.value,
                "summary": event.summary,
                "processing_method": event.processing_method,
                "artifacts_count": len(event.artifacts),
                "snippets_count": len(event.snippet_refs),
            },
            "manual_review": {
                "correct_type": None,  # 수동 입력: 올바른 타입
                "correct_summary": None,  # 수동 입력: 올바른 요약 (선택적)
                "type_accuracy": None,  # 수동 입력: 타입 정확도 (1-5점)
                "summary_quality": None,  # 수동 입력: 요약 품질 (1-5점)
                "summary_completeness": None,  # 수동 입력: 요약 완전성 (1-5점)
                "notes": "",  # 수동 입력: 추가 메모
            },
        }
        dataset["samples"].append(sample)

    # 8. 파일 저장
    if output_file is None:
        output_file = Path("tests/manual_review") / "manual_review_dataset.json"

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    return dataset


def evaluate_manual_review(
    review_file: Path, events: Optional[List[Event]] = None, turns: Optional[List[Turn]] = None
) -> Dict[str, Any]:
    """
    수동 검증 결과 평가

    수동 검증 결과를 로드하여 정확도 계산 및 분석

    Args:
        review_file: 수동 검증 결과 파일 경로
        events: 원본 Event 리스트 (선택적, 비교용)
        turns: 원본 Turn 리스트 (선택적, 비교용)

    Returns:
        평가 결과 딕셔너리
    """
    # 1. 수동 검증 결과 로드
    with open(review_file, "r", encoding="utf-8") as f:
        review_data = json.load(f)

    samples = review_data.get("samples", [])
    if len(samples) == 0:
        return {"error": "No samples found in review file"}

    # 2. 타입 분류 정확도 계산
    type_correct = 0
    type_total = 0
    type_confusion: Dict[Tuple[str, str], int] = defaultdict(int)  # (predicted, actual)

    # 3. Summary 품질 점수 계산
    summary_quality_scores: List[int] = []
    summary_completeness_scores: List[int] = []
    type_accuracy_scores: List[int] = []

    # 4. 처리 방법별 통계
    method_stats: Dict[str, Dict[str, int]] = defaultdict(lambda: {"correct": 0, "total": 0})

    for sample in samples:
        current = sample.get("current_event", {})
        review = sample.get("manual_review", {})

        current_type = current.get("type")
        correct_type = review.get("correct_type")
        processing_method = current.get("processing_method", "unknown")

        # 타입 정확도
        if correct_type is not None:
            type_total += 1
            if current_type == correct_type:
                type_correct += 1
            type_confusion[(current_type, correct_type)] += 1

            method_stats[processing_method]["total"] += 1
            if current_type == correct_type:
                method_stats[processing_method]["correct"] += 1

        # Summary 품질 점수
        if review.get("summary_quality") is not None:
            summary_quality_scores.append(review["summary_quality"])

        if review.get("summary_completeness") is not None:
            summary_completeness_scores.append(review["summary_completeness"])

        if review.get("type_accuracy") is not None:
            type_accuracy_scores.append(review["type_accuracy"])

    # 5. 정확도 계산
    type_accuracy = type_correct / type_total if type_total > 0 else 0.0

    # 6. 처리 방법별 정확도
    method_accuracy = {}
    for method, stats in method_stats.items():
        if stats["total"] > 0:
            method_accuracy[method] = {
                "accuracy": stats["correct"] / stats["total"],
                "correct": stats["correct"],
                "total": stats["total"],
            }

    # 7. 혼동 행렬 생성
    confusion_matrix = {}
    for (predicted, actual), count in type_confusion.items():
        if predicted not in confusion_matrix:
            confusion_matrix[predicted] = {}
        confusion_matrix[predicted][actual] = count

    # 8. 평균 점수 계산
    avg_summary_quality = (
        sum(summary_quality_scores) / len(summary_quality_scores)
        if summary_quality_scores
        else None
    )
    avg_summary_completeness = (
        sum(summary_completeness_scores) / len(summary_completeness_scores)
        if summary_completeness_scores
        else None
    )
    avg_type_accuracy = (
        sum(type_accuracy_scores) / len(type_accuracy_scores) if type_accuracy_scores else None
    )

    # 9. 결과 구성
    evaluation_result = {
        "metadata": {
            "review_file": str(review_file),
            "total_samples": len(samples),
            "evaluated_samples": type_total,
        },
        "type_classification": {
            "accuracy": type_accuracy,
            "correct": type_correct,
            "total": type_total,
            "confusion_matrix": confusion_matrix,
        },
        "summary_quality": {
            "average_quality": avg_summary_quality,
            "average_completeness": avg_summary_completeness,
            "samples_count": len(summary_quality_scores),
        },
        "type_accuracy_scores": {
            "average": avg_type_accuracy,
            "samples_count": len(type_accuracy_scores),
        },
        "method_comparison": method_accuracy,
    }

    return evaluation_result


def create_golden_file_from_manual_review(
    review_file: Path,
    results_file: Path,
    output_file: Optional[Path] = None,
    min_accuracy: float = 0.85,
    apply_corrections: bool = True,
) -> Dict[str, Any]:
    """
    수동 검증 결과를 기반으로 Golden 파일 생성

    수동 검증 데이터셋 파일과 E2E 테스트 결과 파일을 사용하여
    검증된 결과를 Golden 파일로 저장합니다.

    Args:
        review_file: 수동 검증 결과 파일 경로 (manual_review_dataset_*.json)
        results_file: E2E 테스트 결과 파일 경로 (event_normalizer_e2e_llm_*.json)
        output_file: 출력 Golden 파일 경로 (None이면 자동 생성)
        min_accuracy: 최소 정확도 요구사항 (기본값: 0.85)
        apply_corrections: 수동 검증에서 correct_type이 있으면 적용할지 여부

    Returns:
        생성 결과 딕셔너리
    """
    import json

    # 1. 수동 검증 결과 로드
    with open(review_file, "r", encoding="utf-8") as f:
        review_data = json.load(f)

    # 2. E2E 테스트 결과 로드
    with open(results_file, "r", encoding="utf-8") as f:
        results_data = json.load(f)

    # 3. Event 리스트 복원
    from backend.core.models import Event, EventType, Turn, SessionMeta

    events_dict = {e["turn_ref"]: Event(**e) for e in results_data.get("events", [])}
    turns_dict = {
        t["turn_index"]: Turn(**t) for t in results_data.get("turns", []) if "turn_index" in t
    }

    # SessionMeta 복원
    session_meta_dict = results_data.get("session_meta", {})
    session_meta = SessionMeta(**session_meta_dict) if session_meta_dict else None

    # 4. 수동 검증 결과 평가
    events_list = list(events_dict.values())
    turns_list = list(turns_dict.values())

    evaluation = evaluate_manual_review(review_file, events_list, turns_list)

    # 5. 정확도 확인
    type_accuracy = evaluation.get("type_classification", {}).get("accuracy", 0.0)

    if type_accuracy < min_accuracy:
        return {
            "created": False,
            "reason": f"정확도가 너무 낮음: {type_accuracy:.2%} < {min_accuracy:.2%}",
            "evaluation": evaluation,
            "min_accuracy_required": min_accuracy,
        }

    # 6. 수동 검증 결과를 반영하여 "올바른" 이벤트 생성 (선택적)
    corrected_events = []

    if apply_corrections:
        # turn_ref → correct_type 매핑
        corrections = {}
        for sample in review_data.get("samples", []):
            turn_ref = sample.get("turn_index")
            correct_type_str = sample.get("manual_review", {}).get("correct_type")
            if turn_ref is not None and correct_type_str is not None:
                try:
                    corrections[turn_ref] = EventType(correct_type_str)
                except ValueError:
                    # 잘못된 타입은 무시
                    pass

        # 이벤트 수정 (correct_type이 있으면 적용)
        for event in events_list:
            if event.turn_ref in corrections:
                # 수동 검증 결과 반영
                corrected_event = event.model_copy()
                corrected_event.type = corrections[event.turn_ref]
                corrected_events.append(corrected_event)
            else:
                corrected_events.append(event)
    else:
        corrected_events = events_list

    # 7. Golden 파일 생성 (수정된 이벤트 사용)
    if output_file is None:
        output_file = Path("tests/golden") / "event_normalizer_golden.json"

    golden_data = create_golden_file(
        events=corrected_events,
        turns=turns_list,
        session_meta=session_meta,
        output_file=output_file,
        description=f"수동 검증 기반 Golden 파일 (정확도: {type_accuracy:.2%}, corrections_applied: {apply_corrections})",
    )

    return {
        "created": True,
        "file_path": str(output_file),
        "type_accuracy": type_accuracy,
        "evaluation": evaluation,
        "corrections_applied": apply_corrections,
        "corrected_count": (
            len([e for e in corrected_events if e.turn_ref in corrections])
            if apply_corrections
            else 0
        ),
    }


def create_golden_file(
    events: List[Event],
    turns: List[Turn],
    session_meta: Any,
    output_file: Optional[Path] = None,
    description: str = "",
) -> Dict[str, Any]:
    """
    Golden 파일 생성 (회귀 테스트용)

    개선 사이클 완료 후 현재 결과를 Golden 파일로 저장

    Args:
        events: Event 리스트
        turns: Turn 리스트
        session_meta: SessionMeta 객체
        output_file: 출력 파일 경로 (None이면 자동 생성)
        description: Golden 파일 설명

    Returns:
        생성된 Golden 파일 딕셔너리
    """
    from datetime import datetime

    golden_data = {
        "metadata": {
            "created_at": datetime.now().isoformat(),
            "description": description,
            "session_id": session_meta.session_id if session_meta else "unknown",
            "total_events": len(events),
            "total_turns": len(turns),
        },
        "event_type_distribution": {
            event_type.value: sum(1 for e in events if e.type == event_type)
            for event_type in EventType
        },
        "processing_method_distribution": {
            method: sum(1 for e in events if e.processing_method == method)
            for method in ["regex", "llm"]
        },
        "events": [event.dict() for event in events],
        "turns": [turn.dict() for turn in turns],
    }

    if output_file is None:
        output_file = Path("tests/golden") / "event_normalizer_golden.json"

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(golden_data, f, ensure_ascii=False, indent=2)

    return golden_data


def compare_with_golden(
    current_events: List[Event], golden_file: Path, similarity_threshold: float = 0.95
) -> Dict[str, Any]:
    """
    Golden 파일과 현재 결과 비교 (회귀 감지)

    Args:
        current_events: 현재 Event 리스트
        golden_file: Golden 파일 경로
        similarity_threshold: 유사도 임계값 (기본값: 0.95, 95% 미만 시 회귀)

    Returns:
        비교 결과 딕셔너리
    """
    # 1. Golden 파일 로드
    with open(golden_file, "r", encoding="utf-8") as f:
        golden_data = json.load(f)

    golden_events = golden_data.get("events", [])
    golden_metadata = golden_data.get("metadata", {})

    # 2. 이벤트 수 비교
    current_count = len(current_events)
    golden_count = len(golden_events)
    count_match = current_count == golden_count

    # 3. 타입 분포 비교
    current_type_dist = Counter(e.type.value for e in current_events)
    golden_type_dist = Counter(e.get("type") for e in golden_events if isinstance(e, dict))

    type_dist_similarity = _calculate_distribution_similarity(current_type_dist, golden_type_dist)

    # 4. 타입 일치 비교 (turn_ref 기준)
    type_matches = 0
    type_total = 0

    golden_events_dict = {e.get("turn_ref"): e for e in golden_events if isinstance(e, dict)}

    for event in current_events:
        golden_event = golden_events_dict.get(event.turn_ref)
        if golden_event:
            type_total += 1
            if event.type.value == golden_event.get("type"):
                type_matches += 1

    type_accuracy = type_matches / type_total if type_total > 0 else 0.0

    # 5. 회귀 감지
    is_regression = (
        not count_match
        or type_dist_similarity < similarity_threshold
        or type_accuracy < similarity_threshold
    )

    # 6. 결과 구성
    comparison_result = {
        "golden_file": str(golden_file),
        "golden_metadata": golden_metadata,
        "comparison": {
            "event_count": {"current": current_count, "golden": golden_count, "match": count_match},
            "type_distribution": {
                "current": dict(current_type_dist),
                "golden": dict(golden_type_dist),
                "similarity": type_dist_similarity,
            },
            "type_accuracy": {
                "accuracy": type_accuracy,
                "matches": type_matches,
                "total": type_total,
            },
        },
        "regression_detected": is_regression,
        "regression_reasons": [],
    }

    if not count_match:
        comparison_result["regression_reasons"].append(
            f"Event count mismatch: current={current_count}, golden={golden_count}"
        )

    if type_dist_similarity < similarity_threshold:
        comparison_result["regression_reasons"].append(
            f"Type distribution similarity too low: {type_dist_similarity:.2%} < {similarity_threshold:.2%}"
        )

    if type_accuracy < similarity_threshold:
        comparison_result["regression_reasons"].append(
            f"Type accuracy too low: {type_accuracy:.2%} < {similarity_threshold:.2%}"
        )

    return comparison_result


def _calculate_distribution_similarity(dist1: Counter, dist2: Counter) -> float:
    """
    두 분포의 유사도 계산 (Jaccard 유사도 기반)

    Args:
        dist1: 첫 번째 분포 (Counter)
        dist2: 두 번째 분포 (Counter)

    Returns:
        유사도 (0.0 ~ 1.0)
    """
    all_keys = set(dist1.keys()) | set(dist2.keys())
    if len(all_keys) == 0:
        return 1.0

    total_diff = 0
    total_sum = 0

    for key in all_keys:
        val1 = dist1.get(key, 0)
        val2 = dist2.get(key, 0)
        total_sum += max(val1, val2)
        total_diff += abs(val1 - val2)

    if total_sum == 0:
        return 1.0

    similarity = 1.0 - (total_diff / total_sum)
    return max(0.0, min(1.0, similarity))


def create_all_events_html_review_dataset(
    events: List[Event],
    turns: List[Turn],
    output_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    모든 이벤트를 포함한 HTML 형식 수동 검증 데이터셋 생성

    HTML 파일에서 타입 수정 후 JavaScript로 JSON 파일 생성

    Args:
        events: 평가할 Event 리스트 (모두 포함)
        turns: 원본 Turn 리스트
        output_dir: 출력 디렉토리 (None이면 자동 생성)

    Returns:
        생성된 데이터셋 딕셔너리
    """
    from datetime import datetime

    if output_dir is None:
        output_dir = Path("tests/manual_review")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = output_dir / f"all_events_html_review_{timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Turn 정보 매칭
    turns_dict = {turn.turn_index: turn for turn in turns}

    # 이벤트를 turn_ref 기준으로 정렬
    sorted_events = sorted(events, key=lambda e: e.turn_ref)

    # 데이터셋 구성 (JSON용)
    dataset = {
        "metadata": {
            "total_events": len(events),
            "total_turns": len(turns),
            "created_at": timestamp,
        },
        "guidelines": {
            "event_type_definition": {
                "status_review": "상태 리뷰 (현황 점검, 상태 확인)",
                "plan": "계획 수립 (작업 계획, 단계별 계획)",
                "artifact": "파일/경로 관련 (파일 생성/수정/언급)",
                "debug": "디버깅 (에러, 원인, 해결, 검증)",
                "completion": "완료 (작업 완료, 성공)",
                "next_step": "다음 단계 (다음 작업, 진행)",
                "turn": "일반 대화 (기본값)",
            }
        },
        "samples": [],
    }

    # 샘플 데이터 구성
    for event in sorted_events:
        turn = turns_dict.get(event.turn_ref)
        if turn is None:
            continue

        sample = {
            "event_id": f"EVT-{event.turn_ref:03d}",
            "turn_index": event.turn_ref,
            "turn_speaker": turn.speaker,
            "turn_body": turn.body,
            "turn_body_length": len(turn.body),
            "current_event": {
                "type": event.type.value,
                "summary": event.summary,
                "processing_method": event.processing_method,
                "artifacts_count": len(event.artifacts),
                "snippets_count": len(event.snippet_refs),
                "artifacts": event.artifacts,
                "snippet_refs": event.snippet_refs,
            },
            "manual_review": {
                "correct_type": None,
                "type_accuracy": None,
                "summary_quality": None,
                "summary_completeness": None,
                "notes": "",
            },
        }
        dataset["samples"].append(sample)

    # JSON 파일 저장 (초기 데이터)
    json_file = output_dir / "manual_review_data.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    # HTML 파일 생성
    html_file = output_dir / "manual_review.html"
    html_content = generate_html_review_page(dataset)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[INFO] HTML manual review dataset created:")
    print(f"  HTML file: {html_file}")
    print(f"  JSON file: {json_file}")
    print(f"  Total events: {len(dataset['samples'])}")
    print(f"\n[INFO] 사용 방법:")
    print(f"  1. {html_file} 파일을 브라우저에서 열기")
    print(f"  2. 각 이벤트의 correct_type 선택 및 notes 입력")
    print(f"  3. 'Export to JSON' 버튼 클릭하여 수정 결과 다운로드")
    print(f"  4. 다운로드한 JSON 파일을 다음 위치에 저장:")
    print(f"     {output_dir / 'manual_review_updated.json'}")
    print(f"\n[INFO] 저장 시 주의사항:")
    print(f"  - 다운로드한 파일명은 'manual_review_updated_YYYYMMDD_HHMMSS.json' 형식입니다")
    print(f"  - 파일을 '{output_dir / 'manual_review_updated.json'}'로 복사하거나 이름을 변경하세요")
    print(f"  - 또는 다운로드한 파일을 그대로 사용해도 됩니다 (타임스탬프 포함)")

    return dataset


def generate_html_review_page(dataset: Dict[str, Any]) -> str:
    """HTML 리뷰 페이지 생성"""

    event_types = ["status_review", "plan", "artifact", "debug", "completion", "next_step", "turn"]

    # HTML 템플릿
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>이벤트 정규화 수동 검증 - 모든 이벤트</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .header .stats {{
            color: #666;
            font-size: 14px;
        }}
        .controls {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .btn {{
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
        }}
        .btn-primary {{
            background: #007bff;
            color: white;
        }}
        .btn-primary:hover {{
            background: #0056b3;
        }}
        .btn-success {{
            background: #28a745;
            color: white;
        }}
        .btn-success:hover {{
            background: #218838;
        }}
        .event-card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .event-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 2px solid #eee;
        }}
        .event-id {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }}
        .event-type-badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }}
        .type-status_review {{ background: #e3f2fd; color: #1976d2; }}
        .type-plan {{ background: #f3e5f5; color: #7b1fa2; }}
        .type-artifact {{ background: #fff3e0; color: #e65100; }}
        .type-debug {{ background: #ffebee; color: #c62828; }}
        .type-completion {{ background: #e8f5e9; color: #2e7d32; }}
        .type-next_step {{ background: #e0f2f1; color: #00695c; }}
        .type-turn {{ background: #f5f5f5; color: #616161; }}
        .review-section {{
            margin-top: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 4px;
        }}
        .form-group {{
            margin-bottom: 15px;
        }}
        .form-group label {{
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
            color: #333;
        }}
        .form-group select, .form-group input {{
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }}
        .form-group textarea {{
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            min-height: 80px;
            resize: vertical;
        }}
        .turn-body {{
            background: #f9f9f9;
            padding: 15px;
            border-radius: 4px;
            white-space: pre-wrap;
            word-wrap: break-word;
            max-height: 400px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.5;
        }}
        .summary-box {{
            background: #fff;
            padding: 15px;
            border-left: 4px solid #007bff;
            margin: 15px 0;
            border-radius: 4px;
        }}
        .summary-box h4 {{
            margin-bottom: 10px;
            color: #007bff;
        }}
        .toggle-btn {{
            background: #6c757d;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            margin-top: 10px;
        }}
        .toggle-btn:hover {{
            background: #5a6268;
        }}
        .collapsed {{
            display: none;
        }}
        .progress-bar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: #e0e0e0;
            z-index: 1000;
        }}
        .progress-fill {{
            height: 100%;
            background: #007bff;
            transition: width 0.3s;
        }}
    </style>
</head>
<body>
    <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%"></div>
    </div>

    <div class="container">
        <div class="header">
            <h1>이벤트 정규화 수동 검증</h1>
            <div class="stats">
                총 이벤트: {dataset['metadata']['total_events']}개 |
                검증 완료: <span id="reviewedCount">0</span>개 |
                진행률: <span id="progressPercent">0</span>%
            </div>
        </div>

        <div class="controls">
            <button class="btn btn-primary" onclick="scrollToNextUnreviewed()">다음 미검증 항목으로</button>
            <button class="btn btn-primary" onclick="scrollToPrevUnreviewed()">이전 미검증 항목으로</button>
            <button class="btn btn-success" onclick="exportToJSON()">Export to JSON</button>
            <button class="btn btn-primary" onclick="saveProgress()">진행 상황 저장 (로컬)</button>
        </div>

        <div id="eventList">
"""

    # 각 이벤트 카드 생성
    for i, sample in enumerate(dataset["samples"]):
        event_id = sample["event_id"]
        turn_index = sample["turn_index"]
        turn_speaker = sample["turn_speaker"]
        turn_body = sample["turn_body"]
        turn_body_length = sample["turn_body_length"]
        current_type = sample["current_event"]["type"]
        summary = sample["current_event"]["summary"]
        processing_method = sample["current_event"]["processing_method"]

        # HTML 이스케이프 처리
        import html as html_module

        escaped_turn_body = html_module.escape(turn_body)
        escaped_summary = html_module.escape(summary)

        # 긴 텍스트는 접기/펼치기
        is_long_text = turn_body_length > 2000
        display_text = turn_body[:2000] if is_long_text else turn_body
        escaped_display_text = html_module.escape(display_text)
        escaped_remaining_text = html_module.escape(turn_body[2000:]) if is_long_text else ""

        html += f"""
            <div class="event-card" id="event-{turn_index}" data-reviewed="false">
                <div class="event-header">
                    <div>
                        <span class="event-id">{event_id}</span>
                        <span style="margin-left: 10px; color: #666;">Turn {turn_index} | {turn_speaker}</span>
                    </div>
                    <span class="event-type-badge type-{current_type}">{current_type}</span>
                </div>

                <div class="summary-box">
                    <h4>현재 이벤트 Summary</h4>
                    <div>{escaped_summary}</div>
                    <div style="margin-top: 10px; font-size: 12px; color: #666;">
                        처리 방법: {processing_method} |
                        Artifacts: {sample['current_event']['artifacts_count']}개 |
                        Snippets: {sample['current_event']['snippets_count']}개
                    </div>
                </div>

                <div class="form-group">
                    <label>원본 Turn 텍스트 (총 {turn_body_length}자)</label>
                    <div class="turn-body" id="turn-body-{turn_index}">
                        {escaped_display_text}
"""

        if is_long_text:
            html += f"""
                        <div class="collapsed" id="turn-body-full-{turn_index}">
                            {escaped_remaining_text}
                        </div>
                        <button class="toggle-btn" onclick="toggleText({turn_index})">전체 텍스트 보기/접기</button>
"""

        html += f"""
                    </div>
                </div>

                <div class="review-section">
                    <h3 style="margin-bottom: 15px;">수동 검증</h3>

                    <div class="form-group">
                        <label for="correct_type_{turn_index}">올바른 타입 (correct_type) *</label>
                        <select id="correct_type_{turn_index}" onchange="markAsReviewed({turn_index})">
                            <option value="">선택하세요</option>
"""

        for event_type in event_types:
            selected = "selected" if event_type == current_type else ""
            html += f'                            <option value="{event_type}" {selected}>{event_type}</option>\n'

        html += f"""
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="type_accuracy_{turn_index}">타입 정확도 (1-5점)</label>
                        <input type="number" id="type_accuracy_{turn_index}" min="1" max="5" placeholder="1-5">
                    </div>

                    <div class="form-group">
                        <label for="summary_quality_{turn_index}">요약 품질 (1-5점)</label>
                        <input type="number" id="summary_quality_{turn_index}" min="1" max="5" placeholder="1-5">
                    </div>

                    <div class="form-group">
                        <label for="summary_completeness_{turn_index}">요약 완전성 (1-5점)</label>
                        <input type="number" id="summary_completeness_{turn_index}" min="1" max="5" placeholder="1-5">
                    </div>

                    <div class="form-group">
                        <label for="notes_{turn_index}">메모 (notes)</label>
                        <textarea id="notes_{turn_index}" placeholder="추가 메모를 입력하세요..."></textarea>
                    </div>
                </div>
            </div>
"""

    # JavaScript 코드
    html += (
        """
        </div>
    </div>

    <script>
        const eventData = """
        + json.dumps(dataset, ensure_ascii=False)
        + """;

        // 텍스트 접기/펼치기
        function toggleText(turnIndex) {
            const fullText = document.getElementById(`turn-body-full-${turnIndex}`);
            const btn = event.target;
            if (fullText.classList.contains('collapsed')) {
                fullText.classList.remove('collapsed');
                btn.textContent = '텍스트 접기';
            } else {
                fullText.classList.add('collapsed');
                btn.textContent = '전체 텍스트 보기';
            }
        }

        // 검증 완료 표시
        function markAsReviewed(turnIndex) {
            const card = document.getElementById(`event-${turnIndex}`);
            const correctType = document.getElementById(`correct_type_${turnIndex}`).value;
            if (correctType) {
                card.setAttribute('data-reviewed', 'true');
                card.style.borderLeft = '4px solid #28a745';
            } else {
                card.setAttribute('data-reviewed', 'false');
                card.style.borderLeft = 'none';
            }
            updateProgress();
        }

        // 진행률 업데이트
        function updateProgress() {
            const total = eventData.samples.length;
            const reviewed = document.querySelectorAll('[data-reviewed="true"]').length;
            const percent = Math.round((reviewed / total) * 100);

            document.getElementById('reviewedCount').textContent = reviewed;
            document.getElementById('progressPercent').textContent = percent;
            document.getElementById('progressFill').style.width = percent + '%';
        }

        // 다음 미검증 항목으로 스크롤
        function scrollToNextUnreviewed() {
            const unreviewed = document.querySelector('[data-reviewed="false"]');
            if (unreviewed) {
                unreviewed.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } else {
                alert('모든 항목을 검증했습니다!');
            }
        }

        // 이전 미검증 항목으로 스크롤
        function scrollToPrevUnreviewed() {
            const allCards = Array.from(document.querySelectorAll('.event-card'));
            const currentIndex = allCards.findIndex(card => {
                const rect = card.getBoundingClientRect();
                return rect.top > 0 && rect.top < window.innerHeight;
            });

            for (let i = currentIndex - 1; i >= 0; i--) {
                if (allCards[i].getAttribute('data-reviewed') === 'false') {
                    allCards[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
                    return;
                }
            }
            alert('이전 미검증 항목이 없습니다.');
        }

        // JSON으로 내보내기
        function exportToJSON() {
            const updatedData = JSON.parse(JSON.stringify(eventData));

            updatedData.samples.forEach((sample, index) => {
                const turnIndex = sample.turn_index;
                const correctTypeEl = document.getElementById(`correct_type_${turnIndex}`);
                const typeAccuracyEl = document.getElementById(`type_accuracy_${turnIndex}`);
                const summaryQualityEl = document.getElementById(`summary_quality_${turnIndex}`);
                const summaryCompletenessEl = document.getElementById(`summary_completeness_${turnIndex}`);
                const notesEl = document.getElementById(`notes_${turnIndex}`);

                // 값 가져오기 (null 체크)
                const correctType = correctTypeEl ? correctTypeEl.value : '';
                const typeAccuracy = typeAccuracyEl ? typeAccuracyEl.value : '';
                const summaryQuality = summaryQualityEl ? summaryQualityEl.value : '';
                const summaryCompleteness = summaryCompletenessEl ? summaryCompletenessEl.value : '';
                const notes = notesEl ? notesEl.value : '';

                // manual_review 업데이트 (빈 문자열은 null로 처리, 숫자는 유효성 검사)
                sample.manual_review.correct_type = correctType && correctType.trim() !== '' ? correctType : null;
                
                // 숫자 필드는 빈 문자열이 아니고 유효한 숫자인 경우만 저장
                if (typeAccuracy && typeAccuracy.trim() !== '') {
                    const acc = parseInt(typeAccuracy);
                    sample.manual_review.type_accuracy = (!isNaN(acc) && acc >= 1 && acc <= 5) ? acc : null;
                } else {
                    sample.manual_review.type_accuracy = null;
                }
                
                if (summaryQuality && summaryQuality.trim() !== '') {
                    const qual = parseInt(summaryQuality);
                    sample.manual_review.summary_quality = (!isNaN(qual) && qual >= 1 && qual <= 5) ? qual : null;
                } else {
                    sample.manual_review.summary_quality = null;
                }
                
                if (summaryCompleteness && summaryCompleteness.trim() !== '') {
                    const comp = parseInt(summaryCompleteness);
                    sample.manual_review.summary_completeness = (!isNaN(comp) && comp >= 1 && comp <= 5) ? comp : null;
                } else {
                    sample.manual_review.summary_completeness = null;
                }
                
                sample.manual_review.notes = notes ? notes.trim() : '';
            });

            // 타임스탬프 포함 파일명 생성
            const now = new Date();
            const timestamp = now.getFullYear().toString() +
                String(now.getMonth() + 1).padStart(2, '0') +
                String(now.getDate()).padStart(2, '0') + '_' +
                String(now.getHours()).padStart(2, '0') +
                String(now.getMinutes()).padStart(2, '0') +
                String(now.getSeconds()).padStart(2, '0');
            const filename = `manual_review_updated_${timestamp}.json`;

            // JSON 문자열 생성 (UTF-8 인코딩)
            const jsonStr = JSON.stringify(updatedData, null, 2);
            const blob = new Blob([jsonStr], { type: 'application/json;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            // 검증 완료 수 계산
            const reviewedCount = updatedData.samples.filter(s => s.manual_review.correct_type !== null).length;
            alert(`JSON 파일이 다운로드되었습니다!\\n파일명: ${filename}\\n검증 완료: ${reviewedCount}/${updatedData.samples.length}개`);
        }

        // 진행 상황 저장 (로컬 스토리지)
        function saveProgress() {{
            const progress = {{}};
            eventData.samples.forEach(sample => {{
                const turnIndex = sample.turn_index;
                progress[turnIndex] = {{
                    correct_type: document.getElementById(`correct_type_${{turnIndex}}`).value,
                    type_accuracy: document.getElementById(`type_accuracy_${{turnIndex}}`).value,
                    summary_quality: document.getElementById(`summary_quality_${{turnIndex}}`).value,
                    summary_completeness: document.getElementById(`summary_completeness_${{turnIndex}}`).value,
                    notes: document.getElementById(`notes_${{turnIndex}}`).value
                }};
            }});
            localStorage.setItem('reviewProgress', JSON.stringify(progress));
            alert('진행 상황이 저장되었습니다! (브라우저 로컬 스토리지)');
        }}

        // 진행 상황 복원
        function loadProgress() {{
            const saved = localStorage.getItem('reviewProgress');
            if (saved) {{
                const progress = JSON.parse(saved);
                Object.keys(progress).forEach(turnIndex => {{
                    const p = progress[turnIndex];
                    if (p.correct_type) document.getElementById(`correct_type_${{turnIndex}}`).value = p.correct_type;
                    if (p.type_accuracy) document.getElementById(`type_accuracy_${{turnIndex}}`).value = p.type_accuracy;
                    if (p.summary_quality) document.getElementById(`summary_quality_${{turnIndex}}`).value = p.summary_quality;
                    if (p.summary_completeness) document.getElementById(`summary_completeness_${{turnIndex}}`).value = p.summary_completeness;
                    if (p.notes) document.getElementById(`notes_${{turnIndex}}`).value = p.notes;
                    markAsReviewed(parseInt(turnIndex));
                }});
                alert('저장된 진행 상황을 복원했습니다!');
            }}
        }}

        // 페이지 로드 시 진행 상황 복원
        window.addEventListener('load', () => {{
            if (confirm('저장된 진행 상황을 복원하시겠습니까?')) {{
                loadProgress();
            }}
            updateProgress();
        }});
    </script>
</body>
</html>
"""
    )

    return html

```

개선된 HTML 재생성 및 요약 작성 중.


---

**User**

잠깐만요.
create_all_events 파일의 내용에 대해서 설명해주세요

지금 왜 여러번 실행하고 있는지도 설명하세요
상세히 설명


---

**Cursor**

`create_all_events_html_review.py` 파일 내용과 여러 번 실행한 이유 확인 중.


`create_all_events_html_review.py` 파일 내용과 여러 번 실행한 이유를 설명합니다.

## `create_all_events_html_review.py` 파일 설명

### 1. 파일의 목적

이 스크립트는 수동 검증용 HTML 인터페이스를 생성합니다. 모든 이벤트를 HTML로 보여주고, 사용자가 브라우저에서 피드백을 입력할 수 있게 합니다.

### 2. 스크립트의 동작 과정

```python
# 1단계: 입력 파일 로드
input_file = project_root / "docs" / "cursor_phase_6_3.md"
text = input_file.read_text(encoding="utf-8")

# 2단계: 마크다운 파싱 (Phase 2)
parse_result = parse_markdown(text, source_doc=str(input_file))
# 결과: Turn 리스트 생성

# 3단계: 이벤트 정규화 (Phase 3, LLM 기반)
events = normalize_turns_to_events(
    parse_result["turns"], 
    session_meta=session_meta, 
    use_llm=True
)
# 결과: Event 리스트 생성 (67개)

# 4단계: HTML 수동 검증 데이터셋 생성
dataset = create_all_events_html_review_dataset(
    events=events, 
    turns=parse_result["turns"], 
    output_dir=None  # 자동 생성
)
```

### 3. `create_all_events_html_review_dataset()` 함수의 역할

이 함수는 다음을 수행합니다:

#### 3.1 출력 디렉토리 생성
```python
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = output_dir / f"all_events_html_review_{timestamp}"
# 예: tests/manual_review/all_events_html_review_20251225_204608/
```

#### 3.2 데이터셋 구조 생성
각 이벤트를 샘플로 변환:
- `event_id`: "EVT-000", "EVT-001" 등
- `turn_index`: Turn 인덱스
- `turn_speaker`: "User" 또는 "Cursor"
- `turn_body`: 원본 Turn 텍스트
- `current_event`: 현재 이벤트 정보 (타입, 요약, 처리 방법 등)
- `manual_review`: 수동 검증 필드 (초기값은 None 또는 빈 문자열)

#### 3.3 두 가지 파일 생성

1. `manual_review_data.json`: 초기 데이터 (JSON 형식)
   - 모든 이벤트 정보 포함
   - `manual_review` 필드는 빈 상태

2. `manual_review.html`: HTML 인터페이스
   - 브라우저에서 열어 사용
   - 각 이벤트 카드에 입력 폼 제공
   - "Export to JSON" 버튼으로 수정 결과 다운로드

### 4. HTML 파일의 주요 기능

#### 4.1 이벤트 카드 표시
- 각 이벤트를 카드로 표시
- 현재 이벤트 타입, 요약, Turn 텍스트 표시
- 긴 텍스트는 접기/펼치기 지원

#### 4.2 수동 검증 입력 폼
각 이벤트마다 다음 입력 필드 제공:
- `correct_type`: 올바른 타입 선택 (드롭다운)
- `type_accuracy`: 타입 정확도 (1-5점)
- `summary_quality`: 요약 품질 (1-5점)
- `summary_completeness`: 요약 완전성 (1-5점)
- `notes`: 추가 메모 (텍스트 영역)

#### 4.3 `exportToJSON()` 함수 (개선됨)

이전 문제점:
- 빈 값 처리 미흡
- 파일명이 고정되어 덮어쓰기 위험
- 숫자 유효성 검사 부족

개선 사항:
```javascript
// 1. null 체크 강화
const correctTypeEl = document.getElementById(`correct_type_${turnIndex}`);
const correctType = correctTypeEl ? correctTypeEl.value : '';

// 2. 빈 문자열을 null로 변환
sample.manual_review.correct_type = correctType && correctType.trim() !== '' ? correctType : null;

// 3. 숫자 유효성 검사 (1-5 범위)
if (typeAccuracy && typeAccuracy.trim() !== '') {
    const acc = parseInt(typeAccuracy);
    sample.manual_review.type_accuracy = (!isNaN(acc) && acc >= 1 && acc <= 5) ? acc : null;
}

// 4. 타임스탬프 포함 파일명 생성
const timestamp = now.getFullYear().toString() + ...;
const filename = `manual_review_updated_${timestamp}.json`;

// 5. 검증 완료 수 표시
const reviewedCount = updatedData.samples.filter(s => s.manual_review.correct_type !== null).length;
```

### 5. 왜 여러 번 실행했는가?

#### 첫 번째 실행 (20251225_204043)
- 사용자 요청에 따라 HTML 생성 스크립트 실행
- 초기 HTML 파일 생성

#### 두 번째 실행 (20251225_204608)
- `exportToJSON()` 함수 개선 후 재생성
- 개선 사항:
  - null 체크 강화
  - 빈 값 처리 개선
  - 숫자 유효성 검사 추가
  - 타임스탬프 포함 파일명

#### 세 번째 실행 (시도했으나 사용자가 중단)
- 안내 메시지 개선 후 재생성 시도
- 사용자가 중단

### 6. 실행이 필요한 경우

다음 경우에만 재실행:
1. 코드 수정 후: `backend/builders/evaluation.py`의 `generate_html_review_page()` 또는 `exportToJSON()` 수정
2. 새로운 테스트 결과 반영: 최신 이벤트 정규화 결과로 HTML 생성
3. HTML 구조 변경: UI/UX 개선 시

### 7. 현재 상태

- 최신 HTML 파일: `tests/manual_review/all_events_html_review_20251225_204608/manual_review.html`
- 개선된 `exportToJSON()` 함수 포함
- 저장 로직 개선 완료

### 8. 사용 방법

1. HTML 파일 열기: `tests/manual_review/all_events_html_review_20251225_204608/manual_review.html`을 브라우저에서 열기
2. 검증 입력: 각 이벤트의 `correct_type`, 점수, `notes` 입력
3. JSON 다운로드: "Export to JSON" 버튼 클릭
4. 파일 저장: 다운로드한 파일을 `manual_review_updated.json`으로 저장하거나 타임스탬프 포함 파일명 그대로 사용

## 요약

- 스크립트는 최신 이벤트 정규화 결과로 HTML 인터페이스를 생성합니다.
- 여러 번 실행한 이유는 `exportToJSON()` 함수 개선 후 개선 사항을 반영하기 위함입니다.
- 현재는 최신 버전이 생성되어 있으며, 추가 수정이 없으면 재실행할 필요가 없습니다.

```python
# 1단계: 입력 파일 로드
input_file = project_root / "docs" / "cursor_phase_6_3.md"
text = input_file.read_text(encoding="utf-8")

# 2단계: 마크다운 파싱 (Phase 2)
parse_result = parse_markdown(text, source_doc=str(input_file))
# 결과: Turn 리스트 생성

# 3단계: 이벤트 정규화 (Phase 3, LLM 기반)
events = normalize_turns_to_events(
    parse_result["turns"], 
    session_meta=session_meta, 
    use_llm=True
)
# 결과: Event 리스트 생성 (67개)

# 4단계: HTML 수동 검증 데이터셋 생성
dataset = create_all_events_html_review_dataset(
    events=events, 
    turns=parse_result["turns"], 
    output_dir=None  # 자동 생성
)
```

```python
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = output_dir / f"all_events_html_review_{timestamp}"
# 예: tests/manual_review/all_events_html_review_20251225_204608/
```

```javascript
// 1. null 체크 강화
const correctTypeEl = document.getElementById(`correct_type_${turnIndex}`);
const correctType = correctTypeEl ? correctTypeEl.value : '';

// 2. 빈 문자열을 null로 변환
sample.manual_review.correct_type = correctType && correctType.trim() !== '' ? correctType : null;

// 3. 숫자 유효성 검사 (1-5 범위)
if (typeAccuracy && typeAccuracy.trim() !== '') {
    const acc = parseInt(typeAccuracy);
    sample.manual_review.type_accuracy = (!isNaN(acc) && acc >= 1 && acc <= 5) ? acc : null;
}

// 4. 타임스탬프 포함 파일명 생성
const timestamp = now.getFullYear().toString() + ...;
const filename = `manual_review_updated_${timestamp}.json`;

// 5. 검증 완료 수 표시
const reviewedCount = updatedData.samples.filter(s => s.manual_review.correct_type !== null).length;
```

---

**User**

그렇다면 문제가 있습니다.
create_all_events_html_review.py 파일을 다음과 같이 수정합시다
- 1~3단계: 여기서 이벤트 정규화까지 진행. 그런데 llm이 사용되므로, 이걸 계속 실행하면 비용 문제 발생. 따라서 이 파일은 여기까지만 실행
- 4단계 이후: 이건 이벤트 정규화를 바탕으로 UI를 만드는 것 뿐입니다. 그런데 이걸 수정후 재실행하기 위해 1~3단계를 다시 재실행한다구요? 그러면 llm 비용은 어떻게 감당하나요?

이 파일의 문제점을 당신이 다시 검토하세요
무엇이 문제이고 어떻게 개선할지 다시 설명하세요


---

**Cursor**

문제점 확인 중. 코드를 검토해 개선 방안을 제시하겠습니다.


문제점과 개선 방안을 정리합니다.

## 문제점 분석

### 현재 `create_all_events_html_review.py`의 문제

1. 매번 실행 시 불필요한 LLM 호출
   - 1~3단계: 마크다운 파싱 → 이벤트 정규화 (LLM 사용, 비용 발생)
   - 4단계: HTML 생성 (비용 없음)
   - HTML UI 수정 후 재생성 시에도 1~3단계를 다시 실행해 비용이 발생

2. 비효율적인 워크플로우
   ```
   HTML 수정 → 스크립트 재실행 → LLM 호출 (불필요) → HTML 생성
   ```

3. 기존 결과 미활용
   - `tests/results/event_normalizer_e2e_llm_*.json`에 이미 이벤트 정규화 결과가 저장되어 있음
   - 이 파일을 재사용하지 않고 매번 새로 생성

## 개선 방안

### 방안 1: 두 개의 스크립트로 분리 (권장)

#### 스크립트 1: `create_events_for_review.py` (1~3단계만, 최초 1회 실행)
```python
"""
이벤트 정규화 결과 생성 스크립트 (LLM 사용, 비용 발생)

최초 1회만 실행하여 이벤트 정규화 결과를 저장합니다.
이후 HTML 생성은 create_html_review.py를 사용하세요.

사용법:
    poetry run python scripts/create_events_for_review.py
"""
# 1~3단계: 마크다운 파싱 → 이벤트 정규화
# 결과를 tests/results/event_normalizer_e2e_llm_YYYYMMDD_HHMMSS.json에 저장
```

#### 스크립트 2: `create_html_review.py` (4단계만, 무료, 반복 실행 가능)
```python
"""
HTML 수동 검증 데이터셋 생성 스크립트 (비용 없음)

저장된 이벤트 정규화 결과를 읽어서 HTML만 생성합니다.
HTML UI 수정 후 재생성 시 이 스크립트만 실행하세요.

사용법:
    # 최신 결과 파일 자동 사용
    poetry run python scripts/create_html_review.py
    
    # 특정 결과 파일 지정
    poetry run python scripts/create_html_review.py --results-file tests/results/event_normalizer_e2e_llm_20251225_183334.json
"""
# 4단계: 저장된 이벤트 정규화 결과 읽기 → HTML 생성
```

### 방안 2: 기존 스크립트에 옵션 추가

```python
"""
모든 이벤트 HTML 수동 검증 데이터셋 생성 스크립트

사용법:
    # 전체 실행 (1~4단계, LLM 사용, 비용 발생)
    poetry run python scripts/create_all_events_html_review.py --full
    
    # HTML만 생성 (4단계만, 비용 없음, 최신 결과 파일 자동 사용)
    poetry run python scripts/create_all_events_html_review.py --html-only
    
    # 특정 결과 파일 지정
    poetry run python scripts/create_html_review.py --html-only --results-file tests/results/event_normalizer_e2e_llm_20251225_183334.json
"""
```

## 권장 개선 사항

### 1. 스크립트 분리 (방안 1 권장)

이유:
- 책임 분리: 이벤트 생성 vs HTML 생성
- 비용 관리: HTML 재생성 시 LLM 호출 방지
- 재사용성: 다른 스크립트에서도 이벤트 결과 재사용 가능

### 2. 결과 파일 자동 감지

```python
def find_latest_results_file() -> Optional[Path]:
    """가장 최근의 이벤트 정규화 결과 파일 찾기"""
    results_dir = Path("tests/results")
    pattern = "event_normalizer_e2e_llm_*.json"
    files = sorted(results_dir.glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None
```

### 3. 결과 파일 구조 확인

`tests/results/event_normalizer_e2e_llm_*.json` 파일 구조:
```json
{
  "session_meta": {...},
  "turns_count": 67,
  "events": [...],  // Event 객체 리스트
  "event_type_distribution": {...},
  "test_metadata": {...}
}
```

이 구조에서 `events`와 `session_meta`를 읽어서 HTML 생성에 사용 가능합니다.

## 구체적인 개선 코드

### 개선된 `create_html_review.py` (새 스크립트)

```python
"""
HTML 수동 검증 데이터셋 생성 스크립트 (비용 없음)

저장된 이벤트 정규화 결과를 읽어서 HTML만 생성합니다.

사용법:
    # 최신 결과 파일 자동 사용
    poetry run python scripts/create_html_review.py
    
    # 특정 결과 파일 지정
    poetry run python scripts/create_html_review.py --results-file tests/results/event_normalizer_e2e_llm_20251225_183334.json
"""

import sys
import json
import argparse
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
load_dotenv()

from backend.core.models import Event, Turn, SessionMeta
from backend.builders.evaluation import create_all_events_html_review_dataset


def find_latest_results_file() -> Path:
    """가장 최근의 이벤트 정규화 결과 파일 찾기"""
    results_dir = project_root / "tests" / "results"
    pattern = "event_normalizer_e2e_llm_*.json"
    files = sorted(
        results_dir.glob(pattern), 
        key=lambda p: p.stat().st_mtime, 
        reverse=True
    )
    if not files:
        raise FileNotFoundError(
            f"이벤트 정규화 결과 파일을 찾을 수 없습니다: {results_dir / pattern}"
        )
    return files[0]


def load_events_from_results_file(results_file: Path):
    """결과 파일에서 Event와 Turn 리스트 로드"""
    print(f"[INFO] 결과 파일 로드 중: {results_file}")
    
    with open(results_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Event 리스트 복원
    events = [Event(**e) for e in data.get("events", [])]
    
    # Turn 리스트 복원 (results 파일에 turns가 있으면 사용, 없으면 파싱 필요)
    turns = []
    if "turns" in data and data["turns"]:
        turns = [Turn(**t) for t in data["turns"]]
    else:
        # Turn 정보가 없으면 파싱 실행 (비용 없음, LLM 사용 안 함)
        print("[INFO] Turn 정보가 없어 파싱 실행 중...")
        from backend.parser import parse_markdown
        input_file = project_root / "docs" / "cursor_phase_6_3.md"
        text = input_file.read_text(encoding="utf-8")
        parse_result = parse_markdown(text, source_doc=str(input_file))
        turns = parse_result["turns"]
    
    # SessionMeta 복원
    session_meta_dict = data.get("session_meta", {})
    session_meta = SessionMeta(**session_meta_dict) if session_meta_dict else None
    
    print(f"[INFO] 로드 완료: {len(events)}개 이벤트, {len(turns)}개 Turn")
    return events, turns, session_meta


def main():
    parser = argparse.ArgumentParser(
        description="저장된 이벤트 정규화 결과를 읽어서 HTML 수동 검증 데이터셋 생성"
    )
    parser.add_argument(
        "--results-file",
        type=str,
        default=None,
        help="이벤트 정규화 결과 파일 경로 (지정하지 않으면 최신 파일 자동 사용)"
    )
    
    args = parser.parse_args()
    
    # 결과 파일 경로 결정
    if args.results_file:
        results_file = Path(args.results_file)
        if not results_file.exists():
            print(f"[ERROR] 결과 파일을 찾을 수 없습니다: {results_file}")
            return 1
    else:
        try:
            results_file = find_latest_results_file()
            print(f"[INFO] 최신 결과 파일 자동 선택: {results_file.name}")
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            print("[INFO] 먼저 이벤트 정규화를 실행하세요:")
            print("  poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v")
            return 1
    
    # 이벤트 및 Turn 로드
    try:
        events, turns, session_meta = load_events_from_results_file(results_file)
    except Exception as e:
        print(f"[ERROR] 결과 파일 로드 실패: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    # HTML 수동 검증 데이터셋 생성 (비용 없음)
    print("[INFO] HTML 수동 검증 데이터셋 생성 중...")
    dataset = create_all_events_html_review_dataset(
        events=events, 
        turns=turns, 
        output_dir=None  # 자동 생성
    )
    
    print("\n[SUCCESS] HTML manual review dataset created successfully!")
    print(f"  Total events: {len(dataset['samples'])}")
    print(f"\n[INFO] 사용된 결과 파일: {results_file.name}")
    print(f"[INFO] HTML UI 수정 후 이 스크립트를 다시 실행하면 비용 없이 재생성됩니다!")
    
    return 0


if __name__ == "__main__":
    exit(main())
```

### 개선된 `create_all_events_html_review.py` (기존 스크립트, 옵션 추가)

```python
"""
모든 이벤트 HTML 수동 검증 데이터셋 생성 스크립트

사용법:
    # 전체 실행 (1~4단계, LLM 사용, 비용 발생) - 최초 1회만
    poetry run python scripts/create_all_events_html_review.py --full
    
    # HTML만 생성 (4단계만, 비용 없음) - HTML UI 수정 후 재생성 시
    poetry run python scripts/create_all_events_html_review.py --html-only
"""

import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
load_dotenv()

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.evaluation import create_all_events_html_review_dataset


def main():
    parser = argparse.ArgumentParser(
        description="모든 이벤트 HTML 수동 검증 데이터셋 생성"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="전체 실행 (1~4단계, LLM 사용, 비용 발생)"
    )
    parser.add_argument(
        "--html-only",
        action="store_true",
        help="HTML만 생성 (4단계만, 비용 없음, 최신 결과 파일 사용)"
    )
    
    args = parser.parse_args()
    
    # 옵션이 없으면 기본값은 --html-only (비용 절감)
    if not args.full and not args.html_only:
        args.html_only = True
        print("[INFO] 기본값으로 --html-only 모드 실행 (비용 없음)")
        print("[INFO] 전체 실행을 원하면 --full 옵션을 사용하세요")
    
    if args.html_only:
        # HTML만 생성 (비용 없음)
        # create_html_review.py의 로직 사용
        from scripts.create_html_review import find_latest_results_file, load_events_from_results_file
        
        try:
            results_file = find_latest_results_file()
            print(f"[INFO] 최신 결과 파일 사용: {results_file.name}")
            events, turns, session_meta = load_events_from_results_file(results_file)
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            print("[INFO] 먼저 전체 실행을 하거나 E2E 테스트를 실행하세요:")
            print("  poetry run python scripts/create_all_events_html_review.py --full")
            return 1
        
        # HTML 생성
        dataset = create_all_events_html_review_dataset(
            events=events, 
            turns=turns, 
            output_dir=None
        )
        
        print("\n[SUCCESS] HTML manual review dataset created successfully!")
        print(f"  Total events: {len(dataset['samples'])}")
        return 0
    
    elif args.full:
        # 전체 실행 (1~4단계, LLM 사용, 비용 발생)
        # 기존 로직
        input_file = project_root / "docs" / "cursor_phase_6_3.md"
        
        if not input_file.exists():
            print(f"[ERROR] Input file not found: {input_file}")
            return 1
        
        print(f"[INFO] Loading input file: {input_file}")
        text = input_file.read_text(encoding="utf-8")
        
        print("[INFO] Parsing markdown file...")
        parse_result = parse_markdown(text, source_doc=str(input_file))
        print(f"[INFO] Parsed: {len(parse_result['turns'])} turns")
        
        print("[INFO] Normalizing turns to events (LLM-based)...")
        print("[WARNING] LLM 호출로 인한 비용이 발생합니다!")
        session_meta = parse_result["session_meta"]
        events = normalize_turns_to_events(
            parse_result["turns"], session_meta=session_meta, use_llm=True
        )
        print(f"[INFO] Normalized: {len(events)} events")
        
        print("[INFO] Creating HTML manual review dataset...")
        dataset = create_all_events_html_review_dataset(
            events=events, turns=parse_result["turns"], output_dir=None
        )
        
        print("\n[SUCCESS] HTML manual review dataset created successfully!")
        print(f"  Total events: {len(dataset['samples'])}")
        print(f"\n[INFO] 다음부터는 --html-only 옵션으로 비용 없이 재생성할 수 있습니다!")
        return 0


if __name__ == "__main__":
    exit(main())
```

## 요약

### 문제점
1. HTML 재생성 시마다 불필요한 LLM 호출 발생
2. 기존 결과 파일(`tests/results/event_normalizer_e2e_llm_*.json`) 미활용
3. 비용 관리 어려움

### 개선 방안
1. 스크립트 분리: `create_html_review.py` (HTML만 생성, 비용 없음)
2. 옵션 추가: `--html-only` 모드로 HTML만 재생성
3. 자동 감지: 최신 결과 파일 자동 선택

### 권장 워크플로우
```
1. 최초 1회: create_all_events_html_review.py --full 실행 (LLM 사용)
2. HTML UI 수정 후: create_html_review.py 실행 (비용 없음, 반복 가능)
```

이렇게 하면 HTML UI 수정 후 재생성 시 비용 없이 반복 실행할 수 있습니다.

```plaintext
   HTML 수정 → 스크립트 재실행 → LLM 호출 (불필요) → HTML 생성
```

```python
"""
이벤트 정규화 결과 생성 스크립트 (LLM 사용, 비용 발생)

최초 1회만 실행하여 이벤트 정규화 결과를 저장합니다.
이후 HTML 생성은 create_html_review.py를 사용하세요.

사용법:
    poetry run python scripts/create_events_for_review.py
"""
# 1~3단계: 마크다운 파싱 → 이벤트 정규화
# 결과를 tests/results/event_normalizer_e2e_llm_YYYYMMDD_HHMMSS.json에 저장
```

```python
"""
HTML 수동 검증 데이터셋 생성 스크립트 (비용 없음)

저장된 이벤트 정규화 결과를 읽어서 HTML만 생성합니다.
HTML UI 수정 후 재생성 시 이 스크립트만 실행하세요.

사용법:
    # 최신 결과 파일 자동 사용
    poetry run python scripts/create_html_review.py
    
    # 특정 결과 파일 지정
    poetry run python scripts/create_html_review.py --results-file tests/results/event_normalizer_e2e_llm_20251225_183334.json
"""
# 4단계: 저장된 이벤트 정규화 결과 읽기 → HTML 생성
```

```python
"""
모든 이벤트 HTML 수동 검증 데이터셋 생성 스크립트

사용법:
    # 전체 실행 (1~4단계, LLM 사용, 비용 발생)
    poetry run python scripts/create_all_events_html_review.py --full
    
    # HTML만 생성 (4단계만, 비용 없음, 최신 결과 파일 자동 사용)
    poetry run python scripts/create_all_events_html_review.py --html-only
    
    # 특정 결과 파일 지정
    poetry run python scripts/create_html_review.py --html-only --results-file tests/results/event_normalizer_e2e_llm_20251225_183334.json
"""
```

```python
def find_latest_results_file() -> Optional[Path]:
    """가장 최근의 이벤트 정규화 결과 파일 찾기"""
    results_dir = Path("tests/results")
    pattern = "event_normalizer_e2e_llm_*.json"
    files = sorted(results_dir.glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None
```

```json
{
  "session_meta": {...},
  "turns_count": 67,
  "events": [...],  // Event 객체 리스트
  "event_type_distribution": {...},
  "test_metadata": {...}
}
```

```python
"""
HTML 수동 검증 데이터셋 생성 스크립트 (비용 없음)

저장된 이벤트 정규화 결과를 읽어서 HTML만 생성합니다.

사용법:
    # 최신 결과 파일 자동 사용
    poetry run python scripts/create_html_review.py
    
    # 특정 결과 파일 지정
    poetry run python scripts/create_html_review.py --results-file tests/results/event_normalizer_e2e_llm_20251225_183334.json
"""

import sys
import json
import argparse
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
load_dotenv()

from backend.core.models import Event, Turn, SessionMeta
from backend.builders.evaluation import create_all_events_html_review_dataset


def find_latest_results_file() -> Path:
    """가장 최근의 이벤트 정규화 결과 파일 찾기"""
    results_dir = project_root / "tests" / "results"
    pattern = "event_normalizer_e2e_llm_*.json"
    files = sorted(
        results_dir.glob(pattern), 
        key=lambda p: p.stat().st_mtime, 
        reverse=True
    )
    if not files:
        raise FileNotFoundError(
            f"이벤트 정규화 결과 파일을 찾을 수 없습니다: {results_dir / pattern}"
        )
    return files[0]


def load_events_from_results_file(results_file: Path):
    """결과 파일에서 Event와 Turn 리스트 로드"""
    print(f"[INFO] 결과 파일 로드 중: {results_file}")
    
    with open(results_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Event 리스트 복원
    events = [Event(**e) for e in data.get("events", [])]
    
    # Turn 리스트 복원 (results 파일에 turns가 있으면 사용, 없으면 파싱 필요)
    turns = []
    if "turns" in data and data["turns"]:
        turns = [Turn(**t) for t in data["turns"]]
    else:
        # Turn 정보가 없으면 파싱 실행 (비용 없음, LLM 사용 안 함)
        print("[INFO] Turn 정보가 없어 파싱 실행 중...")
        from backend.parser import parse_markdown
        input_file = project_root / "docs" / "cursor_phase_6_3.md"
        text = input_file.read_text(encoding="utf-8")
        parse_result = parse_markdown(text, source_doc=str(input_file))
        turns = parse_result["turns"]
    
    # SessionMeta 복원
    session_meta_dict = data.get("session_meta", {})
    session_meta = SessionMeta(**session_meta_dict) if session_meta_dict else None
    
    print(f"[INFO] 로드 완료: {len(events)}개 이벤트, {len(turns)}개 Turn")
    return events, turns, session_meta


def main():
    parser = argparse.ArgumentParser(
        description="저장된 이벤트 정규화 결과를 읽어서 HTML 수동 검증 데이터셋 생성"
    )
    parser.add_argument(
        "--results-file",
        type=str,
        default=None,
        help="이벤트 정규화 결과 파일 경로 (지정하지 않으면 최신 파일 자동 사용)"
    )
    
    args = parser.parse_args()
    
    # 결과 파일 경로 결정
    if args.results_file:
        results_file = Path(args.results_file)
        if not results_file.exists():
            print(f"[ERROR] 결과 파일을 찾을 수 없습니다: {results_file}")
            return 1
    else:
        try:
            results_file = find_latest_results_file()
            print(f"[INFO] 최신 결과 파일 자동 선택: {results_file.name}")
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            print("[INFO] 먼저 이벤트 정규화를 실행하세요:")
            print("  poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v")
            return 1
    
    # 이벤트 및 Turn 로드
    try:
        events, turns, session_meta = load_events_from_results_file(results_file)
    except Exception as e:
        print(f"[ERROR] 결과 파일 로드 실패: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    # HTML 수동 검증 데이터셋 생성 (비용 없음)
    print("[INFO] HTML 수동 검증 데이터셋 생성 중...")
    dataset = create_all_events_html_review_dataset(
        events=events, 
        turns=turns, 
        output_dir=None  # 자동 생성
    )
    
    print("\n[SUCCESS] HTML manual review dataset created successfully!")
    print(f"  Total events: {len(dataset['samples'])}")
    print(f"\n[INFO] 사용된 결과 파일: {results_file.name}")
    print(f"[INFO] HTML UI 수정 후 이 스크립트를 다시 실행하면 비용 없이 재생성됩니다!")
    
    return 0


if __name__ == "__main__":
    exit(main())
```

```python
"""
모든 이벤트 HTML 수동 검증 데이터셋 생성 스크립트

사용법:
    # 전체 실행 (1~4단계, LLM 사용, 비용 발생) - 최초 1회만
    poetry run python scripts/create_all_events_html_review.py --full
    
    # HTML만 생성 (4단계만, 비용 없음) - HTML UI 수정 후 재생성 시
    poetry run python scripts/create_all_events_html_review.py --html-only
"""

import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
load_dotenv()

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.evaluation import create_all_events_html_review_dataset


def main():
    parser = argparse.ArgumentParser(
        description="모든 이벤트 HTML 수동 검증 데이터셋 생성"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="전체 실행 (1~4단계, LLM 사용, 비용 발생)"
    )
    parser.add_argument(
        "--html-only",
        action="store_true",
        help="HTML만 생성 (4단계만, 비용 없음, 최신 결과 파일 사용)"
    )
    
    args = parser.parse_args()
    
    # 옵션이 없으면 기본값은 --html-only (비용 절감)
    if not args.full and not args.html_only:
        args.html_only = True
        print("[INFO] 기본값으로 --html-only 모드 실행 (비용 없음)")
        print("[INFO] 전체 실행을 원하면 --full 옵션을 사용하세요")
    
    if args.html_only:
        # HTML만 생성 (비용 없음)
        # create_html_review.py의 로직 사용
        from scripts.create_html_review import find_latest_results_file, load_events_from_results_file
        
        try:
            results_file = find_latest_results_file()
            print(f"[INFO] 최신 결과 파일 사용: {results_file.name}")
            events, turns, session_meta = load_events_from_results_file(results_file)
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            print("[INFO] 먼저 전체 실행을 하거나 E2E 테스트를 실행하세요:")
            print("  poetry run python scripts/create_all_events_html_review.py --full")
            return 1
        
        # HTML 생성
        dataset = create_all_events_html_review_dataset(
            events=events, 
            turns=turns, 
            output_dir=None
        )
        
        print("\n[SUCCESS] HTML manual review dataset created successfully!")
        print(f"  Total events: {len(dataset['samples'])}")
        return 0
    
    elif args.full:
        # 전체 실행 (1~4단계, LLM 사용, 비용 발생)
        # 기존 로직
        input_file = project_root / "docs" / "cursor_phase_6_3.md"
        
        if not input_file.exists():
            print(f"[ERROR] Input file not found: {input_file}")
            return 1
        
        print(f"[INFO] Loading input file: {input_file}")
        text = input_file.read_text(encoding="utf-8")
        
        print("[INFO] Parsing markdown file...")
        parse_result = parse_markdown(text, source_doc=str(input_file))
        print(f"[INFO] Parsed: {len(parse_result['turns'])} turns")
        
        print("[INFO] Normalizing turns to events (LLM-based)...")
        print("[WARNING] LLM 호출로 인한 비용이 발생합니다!")
        session_meta = parse_result["session_meta"]
        events = normalize_turns_to_events(
            parse_result["turns"], session_meta=session_meta, use_llm=True
        )
        print(f"[INFO] Normalized: {len(events)} events")
        
        print("[INFO] Creating HTML manual review dataset...")
        dataset = create_all_events_html_review_dataset(
            events=events, turns=parse_result["turns"], output_dir=None
        )
        
        print("\n[SUCCESS] HTML manual review dataset created successfully!")
        print(f"  Total events: {len(dataset['samples'])}")
        print(f"\n[INFO] 다음부터는 --html-only 옵션으로 비용 없이 재생성할 수 있습니다!")
        return 0


if __name__ == "__main__":
    exit(main())
```

```plaintext
1. 최초 1회: create_all_events_html_review.py --full 실행 (LLM 사용)
2. HTML UI 수정 후: create_html_review.py 실행 (비용 없음, 반복 가능)
```

---

**User**

방안1로 진행하세요

---

**Cursor**

방안 1로 진행: 두 개의 스크립트로 분리합니다. 먼저 결과 파일 구조를 확인합니다.


방안 1로 진행: 두 개의 스크립트로 분리합니다.


```python
"""
HTML 수동 검증 데이터셋 생성 스크립트 (비용 없음)

저장된 이벤트 정규화 결과를 읽어서 HTML만 생성합니다.
HTML UI 수정 후 재생성 시 이 스크립트만 실행하세요.

사용법:
    # 최신 결과 파일 자동 사용
    poetry run python scripts/create_html_review.py
    
    # 특정 결과 파일 지정
    poetry run python scripts/create_html_review.py --results-file tests/results/event_normalizer_e2e_llm_20251225_183334.json
"""

import sys
import json
import argparse
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# .env 파일 자동 로드
load_dotenv()

from backend.core.models import Event, Turn, SessionMeta
from backend.builders.evaluation import create_all_events_html_review_dataset


def find_latest_results_file() -> Path:
    """가장 최근의 이벤트 정규화 결과 파일 찾기"""
    results_dir = project_root / "tests" / "results"
    pattern = "event_normalizer_e2e_llm_*.json"
    files = sorted(
        results_dir.glob(pattern), 
        key=lambda p: p.stat().st_mtime, 
        reverse=True
    )
    if not files:
        raise FileNotFoundError(
            f"이벤트 정규화 결과 파일을 찾을 수 없습니다: {results_dir / pattern}\n"
            f"먼저 이벤트 정규화를 실행하세요:\n"
            f"  poetry run python scripts/create_events_for_review.py"
        )
    return files[0]


def load_events_from_results_file(results_file: Path):
    """결과 파일에서 Event와 Turn 리스트 로드"""
    print(f"[INFO] 결과 파일 로드 중: {results_file}")
    
    with open(results_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Event 리스트 복원
    events = [Event(**e) for e in data.get("events", [])]
    print(f"[INFO] {len(events)}개 이벤트 로드 완료")
    
    # Turn 리스트 복원 (results 파일에 turns가 있으면 사용, 없으면 파싱 필요)
    turns = []
    if "turns" in data and data["turns"]:
        turns = [Turn(**t) for t in data["turns"]]
        print(f"[INFO] {len(turns)}개 Turn 로드 완료 (결과 파일에서)")
    else:
        # Turn 정보가 없으면 파싱 실행 (비용 없음, LLM 사용 안 함)
        print("[INFO] Turn 정보가 없어 파싱 실행 중... (LLM 사용 안 함, 비용 없음)")
        from backend.parser import parse_markdown
        input_file = project_root / "docs" / "cursor_phase_6_3.md"
        if not input_file.exists():
            raise FileNotFoundError(
                f"입력 파일을 찾을 수 없습니다: {input_file}\n"
                f"Turn 정보를 복원할 수 없습니다."
            )
        text = input_file.read_text(encoding="utf-8")
        parse_result = parse_markdown(text, source_doc=str(input_file))
        turns = parse_result["turns"]
        print(f"[INFO] {len(turns)}개 Turn 파싱 완료")
    
    # SessionMeta 복원
    session_meta_dict = data.get("session_meta", {})
    session_meta = SessionMeta(**session_meta_dict) if session_meta_dict else None
    
    return events, turns, session_meta


def main():
    parser = argparse.ArgumentParser(
        description="저장된 이벤트 정규화 결과를 읽어서 HTML 수동 검증 데이터셋 생성 (비용 없음)"
    )
    parser.add_argument(
        "--results-file",
        type=str,
        default=None,
        help="이벤트 정규화 결과 파일 경로 (지정하지 않으면 최신 파일 자동 사용)"
    )
    
    args = parser.parse_args()
    
    # 결과 파일 경로 결정
    if args.results_file:
        results_file = Path(args.results_file)
        if not results_file.is_absolute():
            results_file = project_root / results_file
        if not results_file.exists():
            print(f"[ERROR] 결과 파일을 찾을 수 없습니다: {results_file}")
            return 1
    else:
        try:
            results_file = find_latest_results_file()
            print(f"[INFO] 최신 결과 파일 자동 선택: {results_file.name}")
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            return 1
    
    # 이벤트 및 Turn 로드
    try:
        events, turns, session_meta = load_events_from_results_file(results_file)
    except Exception as e:
        print(f"[ERROR] 결과 파일 로드 실패: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    # HTML 수동 검증 데이터셋 생성 (비용 없음)
    print("[INFO] HTML 수동 검증 데이터셋 생성 중...")
    dataset = create_all_events_html_review_dataset(
        events=events, 
        turns=turns, 
        output_dir=None  # 자동 생성
    )
    
    print("\n[SUCCESS] HTML manual review dataset created successfully!")
    print(f"  Total events: {len(dataset['samples'])}")
    print(f"\n[INFO] 사용된 결과 파일: {results_file.name}")
    print(f"[INFO] HTML UI 수정 후 이 스크립트를 다시 실행하면 비용 없이 재생성됩니다!")
    print(f"\n[INFO] 사용 방법:")
    print(f"  1. 생성된 HTML 파일을 브라우저에서 열기")
    print(f"  2. 각 이벤트의 correct_type 선택 및 notes 입력")
    print(f"  3. 'Export to JSON' 버튼 클릭하여 수정 결과 다운로드")
    
    return 0


if __name__ == "__main__":
    exit(main())

```

```python
"""
이벤트 정규화 결과 생성 스크립트 (LLM 사용, 비용 발생)

최초 1회만 실행하여 이벤트 정규화 결과를 저장합니다.
이후 HTML 생성은 create_html_review.py를 사용하세요.

사용법:
    poetry run python scripts/create_events_for_review.py
"""

import sys
import json
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# .env 파일 자동 로드
load_dotenv()

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.core.llm_service import reset_cache_stats, get_cache_stats


def main():
    """이벤트 정규화 결과 생성 (1~3단계만)"""
    
    # 입력 파일 경로
    input_file = project_root / "docs" / "cursor_phase_6_3.md"
    
    if not input_file.exists():
        print(f"[ERROR] Input file not found: {input_file}")
        return 1
    
    print(f"[INFO] Loading input file: {input_file}")
    text = input_file.read_text(encoding="utf-8")
    
    # 1단계: 파싱 실행
    print("[INFO] Step 1: Parsing markdown file...")
    parse_result = parse_markdown(text, source_doc=str(input_file))
    print(f"[INFO] Parsed: {len(parse_result['turns'])} turns")
    
    # 2-3단계: 이벤트 정규화 실행 (LLM 기반)
    print("[INFO] Step 2-3: Normalizing turns to events (LLM-based)...")
    print("[WARNING] LLM 호출로 인한 비용이 발생합니다!")
    
    # 캐시 통계 초기화
    reset_cache_stats()
    
    session_meta = parse_result["session_meta"]
    start_time = time.time()
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=True
    )
    elapsed_time = time.time() - start_time
    
    # 실행 중 캐시 통계 수집
    runtime_cache_stats = get_cache_stats()
    
    print(f"[INFO] Normalized: {len(events)} events")
    print(f"[INFO] Elapsed time: {elapsed_time:.2f} seconds")
    print(f"[INFO] Cache hit rate: {runtime_cache_stats.get('hit_rate', 0):.2%}")
    
    # 결과 저장
    results_dir = project_root / "tests" / "results"
    results_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = results_dir / f"event_normalizer_e2e_llm_{timestamp}.json"
    
    # 이벤트 타입 분포 계산
    from collections import Counter
    event_type_distribution = Counter(e.type.value for e in events)
    
    # 결과 저장
    detailed_results = {
        "session_meta": parse_result["session_meta"].model_dump(),
        "turns_count": len(parse_result["turns"]),
        "turns": [turn.model_dump() for turn in parse_result["turns"]],  # Turn 정보도 저장
        "events": [event.model_dump() for event in events],
        "event_type_distribution": dict(event_type_distribution),
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(input_file),
            "test_name": "create_events_for_review",
            "processing_method": "llm",
            "elapsed_time_seconds": round(elapsed_time, 2),
            "cache_statistics": runtime_cache_stats,
        },
    }
    
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(detailed_results, f, ensure_ascii=False, indent=2)
    
    print(f"\n[SUCCESS] 이벤트 정규화 결과가 저장되었습니다!")
    print(f"  Results file: {results_file}")
    print(f"  Total events: {len(events)}")
    print(f"  Event type distribution:")
    for event_type, count in sorted(event_type_distribution.items()):
        print(f"    {event_type}: {count}개")
    
    print(f"\n[INFO] 다음 단계:")
    print(f"  HTML 수동 검증 데이터셋을 생성하려면 다음 명령어를 실행하세요:")
    print(f"    poetry run python scripts/create_html_review.py")
    print(f"  또는 특정 결과 파일을 지정하려면:")
    print(f"    poetry run python scripts/create_html_review.py --results-file {results_file.name}")
    
    return 0


if __name__ == "__main__":
    exit(main())

```

기존 스크립트에 deprecated 표시 추가 중.


```python
"""
모든 이벤트 HTML 수동 검증 데이터셋 생성 스크립트

⚠️ DEPRECATED: 이 스크립트는 더 이상 권장되지 않습니다.

새로운 워크플로우 (비용 절감):
1. 최초 1회: poetry run python scripts/create_events_for_review.py
   - 이벤트 정규화 결과 생성 (LLM 사용, 비용 발생)
   
2. HTML 생성/재생성: poetry run python scripts/create_html_review.py
   - 저장된 결과를 읽어서 HTML만 생성 (비용 없음, 반복 실행 가능)

이 스크립트는 하위 호환성을 위해 유지되지만, 
HTML UI 수정 후 재생성 시 불필요한 LLM 호출이 발생하므로 
새로운 스크립트 사용을 권장합니다.

사용법 (하위 호환):
    poetry run python scripts/create_all_events_html_review.py
"""

import sys
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# .env 파일 자동 로드
load_dotenv()

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.evaluation import create_all_events_html_review_dataset


def main():
    """모든 이벤트 HTML 수동 검증 데이터셋 생성"""

    # 입력 파일 경로
    input_file = project_root / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        print(f"[ERROR] Input file not found: {input_file}")
        return 1

    print(f"[INFO] Loading input file: {input_file}")
    text = input_file.read_text(encoding="utf-8")

    # 파싱 실행
    print("[INFO] Parsing markdown file...")
    parse_result = parse_markdown(text, source_doc=str(input_file))
    print(f"[INFO] Parsed: {len(parse_result['turns'])} turns")

    # 이벤트 정규화 실행 (LLM 기반)
    print("[INFO] Normalizing turns to events (LLM-based)...")
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=True
    )
    print(f"[INFO] Normalized: {len(events)} events")

    # HTML 수동 검증 데이터셋 생성
    print("[INFO] Creating HTML manual review dataset...")
    dataset = create_all_events_html_review_dataset(
        events=events, turns=parse_result["turns"], output_dir=None  # 자동 생성
    )

    print("\n[SUCCESS] HTML manual review dataset created successfully!")
    print(f"  Total events: {len(dataset['samples'])}")

    return 0


if __name__ == "__main__":
    exit(main())

```

```python
"""
모든 이벤트 HTML 수동 검증 데이터셋 생성 스크립트

⚠️ DEPRECATED: 이 스크립트는 더 이상 권장되지 않습니다.

새로운 워크플로우 (비용 절감):
1. 최초 1회: poetry run python scripts/create_events_for_review.py
   - 이벤트 정규화 결과 생성 (LLM 사용, 비용 발생)
   
2. HTML 생성/재생성: poetry run python scripts/create_html_review.py
   - 저장된 결과를 읽어서 HTML만 생성 (비용 없음, 반복 실행 가능)

이 스크립트는 하위 호환성을 위해 유지되지만, 
HTML UI 수정 후 재생성 시 불필요한 LLM 호출이 발생하므로 
새로운 스크립트 사용을 권장합니다.

사용법 (하위 호환):
    poetry run python scripts/create_all_events_html_review.py
"""

import sys
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# .env 파일 자동 로드
load_dotenv()

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.evaluation import create_all_events_html_review_dataset


def main():
    """모든 이벤트 HTML 수동 검증 데이터셋 생성 (DEPRECATED)"""
    
    print("[WARNING] 이 스크립트는 deprecated되었습니다.")
    print("[INFO] 새로운 워크플로우를 사용하세요:")
    print("  1. poetry run python scripts/create_events_for_review.py  (최초 1회)")
    print("  2. poetry run python scripts/create_html_review.py  (HTML 생성/재생성)")
    print()
    
    # 입력 파일 경로
    input_file = project_root / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        print(f"[ERROR] Input file not found: {input_file}")
        return 1

    print(f"[INFO] Loading input file: {input_file}")
    text = input_file.read_text(encoding="utf-8")

    # 파싱 실행
    print("[INFO] Parsing markdown file...")
    parse_result = parse_markdown(text, source_doc=str(input_file))
    print(f"[INFO] Parsed: {len(parse_result['turns'])} turns")

    # 이벤트 정규화 실행 (LLM 기반)
    print("[INFO] Normalizing turns to events (LLM-based)...")
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=True
    )
    print(f"[INFO] Normalized: {len(events)} events")

    # HTML 수동 검증 데이터셋 생성
    print("[INFO] Creating HTML manual review dataset...")
    dataset = create_all_events_html_review_dataset(
        events=events, turns=parse_result["turns"], output_dir=None  # 자동 생성
    )

    print("\n[SUCCESS] HTML manual review dataset created successfully!")
    print(f"  Total events: {len(dataset['samples'])}")

    return 0


if __name__ == "__main__":
    exit(main())

```

생성된 스크립트 테스트 중.


---

**User**

create_events_for_review.py 이거는 다시 왜 실행하나요?
이미 이벤트 생성 파일이 만들어졌고, 여기에 내용이 다 있는거 아닌가요?

---

**Cursor**

맞습니다. 이미 `tests/results/event_normalizer_e2e_llm_*.json` 파일들이 있고, 이벤트 정규화 결과가 저장되어 있습니다. 확인 중입니다.


맞습니다. 이미 `tests/results/`에 이벤트 정규화 결과 파일들이 있습니다.

## 현재 상황

1. 이미 결과 파일 존재: `event_normalizer_e2e_llm_20251225_183334.json` 등
2. E2E 테스트 실행 시 자동 생성: `test_event_normalizer_e2e_with_llm` 테스트가 결과 파일을 생성
3. 대부분의 경우: `create_html_review.py`만 실행하면 됨

## `create_events_for_review.py`가 필요한 경우

다음 경우에만 필요합니다:
1. E2E 테스트를 실행하지 않고 직접 이벤트 정규화 결과만 생성하고 싶을 때
2. 새로운 입력 파일이 있거나 이벤트 정규화 로직이 변경되어 재생성이 필요할 때
3. E2E 테스트 결과 파일이 없을 때

## 권장 워크플로우 수정

### 일반적인 경우 (대부분)
```bash
# HTML 생성/재생성 (비용 없음, 반복 실행 가능)
poetry run python scripts/create_html_review.py
```

### 이벤트 정규화 결과가 없거나 재생성이 필요한 경우
```bash
# 옵션 1: E2E 테스트 실행 (권장)
poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v

# 옵션 2: 직접 이벤트 정규화 결과 생성
poetry run python scripts/create_events_for_review.py
```

## 스크립트 설명 수정 제안

`create_events_for_review.py`의 설명을 다음과 같이 수정하는 것이 좋습니다:

```python
"""
이벤트 정규화 결과 생성 스크립트 (LLM 사용, 비용 발생)

⚠️ 주의: 대부분의 경우 이 스크립트를 실행할 필요가 없습니다.

일반적인 워크플로우:
1. E2E 테스트 실행 (이벤트 정규화 결과 자동 생성):
   poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v

2. HTML 생성/재생성 (비용 없음):
   poetry run python scripts/create_html_review.py

이 스크립트는 다음 경우에만 사용하세요:
- E2E 테스트를 실행하지 않고 직접 이벤트 정규화 결과만 생성하고 싶을 때
- 새로운 입력 파일이 있거나 이벤트 정규화 로직이 변경되어 재생성이 필요할 때

사용법:
    poetry run python scripts/create_events_for_review.py
"""
```

요약: 대부분의 경우 `create_html_review.py`만 사용하면 되고, `create_events_for_review.py`는 선택적입니다. 스크립트 설명을 위와 같이 수정할까요?

```shellscript
# HTML 생성/재생성 (비용 없음, 반복 실행 가능)
poetry run python scripts/create_html_review.py
```

```shellscript
# 옵션 1: E2E 테스트 실행 (권장)
poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v

# 옵션 2: 직접 이벤트 정규화 결과 생성
poetry run python scripts/create_events_for_review.py
```

```python
"""
이벤트 정규화 결과 생성 스크립트 (LLM 사용, 비용 발생)

⚠️ 주의: 대부분의 경우 이 스크립트를 실행할 필요가 없습니다.

일반적인 워크플로우:
1. E2E 테스트 실행 (이벤트 정규화 결과 자동 생성):
   poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v

2. HTML 생성/재생성 (비용 없음):
   poetry run python scripts/create_html_review.py

이 스크립트는 다음 경우에만 사용하세요:
- E2E 테스트를 실행하지 않고 직접 이벤트 정규화 결과만 생성하고 싶을 때
- 새로운 입력 파일이 있거나 이벤트 정규화 로직이 변경되어 재생성이 필요할 때

사용법:
    poetry run python scripts/create_events_for_review.py
"""
```

---

**User**

네 그렇게 하세요

---

**Cursor**

스크립트 설명을 수정 중입니다.


```python
"""
이벤트 정규화 결과 생성 스크립트 (LLM 사용, 비용 발생)

⚠️ 주의: 대부분의 경우 이 스크립트를 실행할 필요가 없습니다.

일반적인 워크플로우:
1. E2E 테스트 실행 (이벤트 정규화 결과 자동 생성):
   poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v

2. HTML 생성/재생성 (비용 없음):
   poetry run python scripts/create_html_review.py

이 스크립트는 다음 경우에만 사용하세요:
- E2E 테스트를 실행하지 않고 직접 이벤트 정규화 결과만 생성하고 싶을 때
- 새로운 입력 파일이 있거나 이벤트 정규화 로직이 변경되어 재생성이 필요할 때

사용법:
    poetry run python scripts/create_events_for_review.py
"""

import sys
import json
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# .env 파일 자동 로드
load_dotenv()

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.core.llm_service import reset_cache_stats, get_cache_stats


def main():
    """이벤트 정규화 결과 생성 (1~3단계만)"""

    # 입력 파일 경로
    input_file = project_root / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        print(f"[ERROR] Input file not found: {input_file}")
        return 1

    print(f"[INFO] Loading input file: {input_file}")
    text = input_file.read_text(encoding="utf-8")

    # 1단계: 파싱 실행
    print("[INFO] Step 1: Parsing markdown file...")
    parse_result = parse_markdown(text, source_doc=str(input_file))
    print(f"[INFO] Parsed: {len(parse_result['turns'])} turns")

    # 2-3단계: 이벤트 정규화 실행 (LLM 기반)
    print("[INFO] Step 2-3: Normalizing turns to events (LLM-based)...")
    print("[WARNING] LLM 호출로 인한 비용이 발생합니다!")

    # 캐시 통계 초기화
    reset_cache_stats()

    session_meta = parse_result["session_meta"]
    start_time = time.time()
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=True
    )
    elapsed_time = time.time() - start_time

    # 실행 중 캐시 통계 수집
    runtime_cache_stats = get_cache_stats()

    print(f"[INFO] Normalized: {len(events)} events")
    print(f"[INFO] Elapsed time: {elapsed_time:.2f} seconds")
    print(f"[INFO] Cache hit rate: {runtime_cache_stats.get('hit_rate', 0):.2%}")

    # 결과 저장
    results_dir = project_root / "tests" / "results"
    results_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = results_dir / f"event_normalizer_e2e_llm_{timestamp}.json"

    # 이벤트 타입 분포 계산
    from collections import Counter
    event_type_distribution = Counter(e.type.value for e in events)

    # 결과 저장
    detailed_results = {
        "session_meta": parse_result["session_meta"].model_dump(),
        "turns_count": len(parse_result["turns"]),
        "turns": [turn.model_dump() for turn in parse_result["turns"]],  # Turn 정보도 저장
        "events": [event.model_dump() for event in events],
        "event_type_distribution": dict(event_type_distribution),
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(input_file),
            "test_name": "create_events_for_review",
            "processing_method": "llm",
            "elapsed_time_seconds": round(elapsed_time, 2),
            "cache_statistics": runtime_cache_stats,
        },
    }

    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(detailed_results, f, ensure_ascii=False, indent=2)

    print(f"\n[SUCCESS] 이벤트 정규화 결과가 저장되었습니다!")
    print(f"  Results file: {results_file}")
    print(f"  Total events: {len(events)}")
    print(f"  Event type distribution:")
    for event_type, count in sorted(event_type_distribution.items()):
        print(f"    {event_type}: {count}개")

    print(f"\n[INFO] 다음 단계:")
    print(f"  HTML 수동 검증 데이터셋을 생성하려면 다음 명령어를 실행하세요:")
    print(f"    poetry run python scripts/create_html_review.py")
    print(f"  또는 특정 결과 파일을 지정하려면:")
    print(f"    poetry run python scripts/create_html_review.py --results-file {results_file.name}")

    return 0


if __name__ == "__main__":
    exit(main())


```

```python
"""
이벤트 정규화 결과 생성 스크립트 (LLM 사용, 비용 발생)

⚠️ 주의: 대부분의 경우 이 스크립트를 실행할 필요가 없습니다.

일반적인 워크플로우:
1. E2E 테스트 실행 (이벤트 정규화 결과 자동 생성):
   poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v

2. HTML 생성/재생성 (비용 없음):
   poetry run python scripts/create_html_review.py

이 스크립트는 다음 경우에만 사용하세요:
- E2E 테스트를 실행하지 않고 직접 이벤트 정규화 결과만 생성하고 싶을 때
- 새로운 입력 파일이 있거나 이벤트 정규화 로직이 변경되어 재생성이 필요할 때

사용법:
    poetry run python scripts/create_events_for_review.py
"""

import sys
import json
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# .env 파일 자동 로드
load_dotenv()

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.core.llm_service import reset_cache_stats, get_cache_stats


def main():
    """이벤트 정규화 결과 생성 (1~3단계만)"""

    # 입력 파일 경로
    input_file = project_root / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        print(f"[ERROR] Input file not found: {input_file}")
        return 1

    print(f"[INFO] Loading input file: {input_file}")
    text = input_file.read_text(encoding="utf-8")

    # 1단계: 파싱 실행
    print("[INFO] Step 1: Parsing markdown file...")
    parse_result = parse_markdown(text, source_doc=str(input_file))
    print(f"[INFO] Parsed: {len(parse_result['turns'])} turns")

    # 2-3단계: 이벤트 정규화 실행 (LLM 기반)
    print("[INFO] Step 2-3: Normalizing turns to events (LLM-based)...")
    print("[WARNING] LLM 호출로 인한 비용이 발생합니다!")

    # 캐시 통계 초기화
    reset_cache_stats()

    session_meta = parse_result["session_meta"]
    start_time = time.time()
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=True
    )
    elapsed_time = time.time() - start_time

    # 실행 중 캐시 통계 수집
    runtime_cache_stats = get_cache_stats()

    print(f"[INFO] Normalized: {len(events)} events")
    print(f"[INFO] Elapsed time: {elapsed_time:.2f} seconds")
    print(f"[INFO] Cache hit rate: {runtime_cache_stats.get('hit_rate', 0):.2%}")

    # 결과 저장
    results_dir = project_root / "tests" / "results"
    results_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = results_dir / f"event_normalizer_e2e_llm_{timestamp}.json"

    # 이벤트 타입 분포 계산
    from collections import Counter
    event_type_distribution = Counter(e.type.value for e in events)

    # 결과 저장
    detailed_results = {
        "session_meta": parse_result["session_meta"].model_dump(),
        "turns_count": len(parse_result["turns"]),
        "turns": [turn.model_dump() for turn in parse_result["turns"]],  # Turn 정보도 저장
        "events": [event.model_dump() for event in events],
        "event_type_distribution": dict(event_type_distribution),
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(input_file),
            "test_name": "create_events_for_review",
            "processing_method": "llm",
            "elapsed_time_seconds": round(elapsed_time, 2),
            "cache_statistics": runtime_cache_stats,
        },
    }

    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(detailed_results, f, ensure_ascii=False, indent=2)

    print(f"\n[SUCCESS] 이벤트 정규화 결과가 저장되었습니다!")
    print(f"  Results file: {results_file}")
    print(f"  Total events: {len(events)}")
    print(f"  Event type distribution:")
    for event_type, count in sorted(event_type_distribution.items()):
        print(f"    {event_type}: {count}개")

    print(f"\n[INFO] 다음 단계:")
    print(f"  HTML 수동 검증 데이터셋을 생성하려면 다음 명령어를 실행하세요:")
    print(f"    poetry run python scripts/create_html_review.py")
    print(f"  (최신 결과 파일을 자동으로 사용합니다)")
    print(f"  또는 특정 결과 파일을 지정하려면:")
    print(f"    poetry run python scripts/create_html_review.py --results-file {results_file.name}")

    return 0


if __name__ == "__main__":
    exit(main())


```

`create_html_review.py` 설명도 더 명확하게 업데이트 중입니다.


```python
"""
HTML 수동 검증 데이터셋 생성 스크립트 (비용 없음)

저장된 이벤트 정규화 결과를 읽어서 HTML만 생성합니다.
HTML UI 수정 후 재생성 시 이 스크립트만 실행하세요.

⚠️ 중요: 이 스크립트는 LLM을 호출하지 않으므로 비용이 발생하지 않습니다.
반복 실행이 가능하며, HTML UI 수정 후 재생성 시 사용하세요.

사용법:
    # 최신 결과 파일 자동 사용 (권장)
    poetry run python scripts/create_html_review.py
    
    # 특정 결과 파일 지정
    poetry run python scripts/create_html_review.py --results-file tests/results/event_normalizer_e2e_llm_20251225_183334.json

참고:
    - 이벤트 정규화 결과 파일은 E2E 테스트 실행 시 자동 생성됩니다:
      poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v
    - 결과 파일이 없으면 에러 메시지가 표시됩니다.
"""

import sys
import json
import argparse
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# .env 파일 자동 로드
load_dotenv()

from backend.core.models import Event, Turn, SessionMeta
from backend.builders.evaluation import create_all_events_html_review_dataset


def find_latest_results_file() -> Path:
    """가장 최근의 이벤트 정규화 결과 파일 찾기"""
    results_dir = project_root / "tests" / "results"
    pattern = "event_normalizer_e2e_llm_*.json"
    files = sorted(
        results_dir.glob(pattern),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )
    if not files:
        raise FileNotFoundError(
            f"이벤트 정규화 결과 파일을 찾을 수 없습니다: {results_dir / pattern}\n"
            f"먼저 이벤트 정규화를 실행하세요:\n"
            f"  poetry run python scripts/create_events_for_review.py"
        )
    return files[0]


def load_events_from_results_file(results_file: Path):
    """결과 파일에서 Event와 Turn 리스트 로드"""
    print(f"[INFO] 결과 파일 로드 중: {results_file}")

    with open(results_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Event 리스트 복원
    events = [Event(**e) for e in data.get("events", [])]
    print(f"[INFO] {len(events)}개 이벤트 로드 완료")

    # Turn 리스트 복원 (results 파일에 turns가 있으면 사용, 없으면 파싱 필요)
    turns = []
    if "turns" in data and data["turns"]:
        turns = [Turn(**t) for t in data["turns"]]
        print(f"[INFO] {len(turns)}개 Turn 로드 완료 (결과 파일에서)")
    else:
        # Turn 정보가 없으면 파싱 실행 (비용 없음, LLM 사용 안 함)
        print("[INFO] Turn 정보가 없어 파싱 실행 중... (LLM 사용 안 함, 비용 없음)")
        from backend.parser import parse_markdown
        input_file = project_root / "docs" / "cursor_phase_6_3.md"
        if not input_file.exists():
            raise FileNotFoundError(
                f"입력 파일을 찾을 수 없습니다: {input_file}\n"
                f"Turn 정보를 복원할 수 없습니다."
            )
        text = input_file.read_text(encoding="utf-8")
        parse_result = parse_markdown(text, source_doc=str(input_file))
        turns = parse_result["turns"]
        print(f"[INFO] {len(turns)}개 Turn 파싱 완료")

    # SessionMeta 복원
    session_meta_dict = data.get("session_meta", {})
    session_meta = SessionMeta(**session_meta_dict) if session_meta_dict else None

    return events, turns, session_meta


def main():
    parser = argparse.ArgumentParser(
        description="저장된 이벤트 정규화 결과를 읽어서 HTML 수동 검증 데이터셋 생성 (비용 없음)"
    )
    parser.add_argument(
        "--results-file",
        type=str,
        default=None,
        help="이벤트 정규화 결과 파일 경로 (지정하지 않으면 최신 파일 자동 사용)"
    )

    args = parser.parse_args()

    # 결과 파일 경로 결정
    if args.results_file:
        results_file = Path(args.results_file)
        if not results_file.is_absolute():
            results_file = project_root / results_file
        if not results_file.exists():
            print(f"[ERROR] 결과 파일을 찾을 수 없습니다: {results_file}")
            return 1
    else:
        try:
            results_file = find_latest_results_file()
            print(f"[INFO] 최신 결과 파일 자동 선택: {results_file.name}")
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            return 1

    # 이벤트 및 Turn 로드
    try:
        events, turns, session_meta = load_events_from_results_file(results_file)
    except Exception as e:
        print(f"[ERROR] 결과 파일 로드 실패: {e}")
        import traceback
        traceback.print_exc()
        return 1

    # HTML 수동 검증 데이터셋 생성 (비용 없음)
    print("[INFO] HTML 수동 검증 데이터셋 생성 중...")
    dataset = create_all_events_html_review_dataset(
        events=events,
        turns=turns,
        output_dir=None  # 자동 생성
    )

    print("\n[SUCCESS] HTML manual review dataset created successfully!")
    print(f"  Total events: {len(dataset['samples'])}")
    print(f"\n[INFO] 사용된 결과 파일: {results_file.name}")
    print(f"[INFO] HTML UI 수정 후 이 스크립트를 다시 실행하면 비용 없이 재생성됩니다!")
    print(f"\n[INFO] 사용 방법:")
    print(f"  1. 생성된 HTML 파일을 브라우저에서 열기")
    print(f"  2. 각 이벤트의 correct_type 선택 및 notes 입력")
    print(f"  3. 'Export to JSON' 버튼 클릭하여 수정 결과 다운로드")

    return 0


if __name__ == "__main__":
    exit(main())


```

스크립트 설명을 수정했습니다.

## 완료된 작업

### 1. `create_html_review.py` (HTML 생성, 비용 없음)
- 저장된 이벤트 정규화 결과를 읽어서 HTML만 생성
- LLM 호출 없음 (비용 없음)
- 반복 실행 가능
- 최신 결과 파일 자동 사용

### 2. `create_events_for_review.py` (이벤트 정규화, LLM 사용)
- 설명 업데이트: 대부분의 경우 불필요함을 명시
- E2E 테스트가 결과 파일을 자동 생성함을 안내
- 특수한 경우에만 사용하도록 안내

### 3. `create_all_events_html_review.py` (기존 스크립트)
- DEPRECATED 표시 추가
- 새로운 워크플로우 안내 추가

## 권장 워크플로우

### 일반적인 경우 (대부분)
```bash
# 1. E2E 테스트 실행 (이벤트 정규화 결과 자동 생성)
poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v

# 2. HTML 생성/재생성 (비용 없음, 반복 실행 가능)
poetry run python scripts/create_html_review.py
```

### 특수한 경우
```bash
# E2E 테스트를 실행하지 않고 직접 이벤트 정규화 결과만 생성하고 싶을 때
poetry run python scripts/create_events_for_review.py
```

이제 HTML UI 수정 후 재생성 시 비용 없이 반복 실행할 수 있습니다.

```shellscript
# 1. E2E 테스트 실행 (이벤트 정규화 결과 자동 생성)
poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v

# 2. HTML 생성/재생성 (비용 없음, 반복 실행 가능)
poetry run python scripts/create_html_review.py
```

```shellscript
# E2E 테스트를 실행하지 않고 직접 이벤트 정규화 결과만 생성하고 싶을 때
poetry run python scripts/create_events_for_review.py
```

---

**User**

지금 복잡한 상황이니 이렇게 한번 정리하고 실행
- create_all_events_html_review.py는 아예 삭제해서 혼선을 방지
- 현재 상태 @TODOs.md 에서 진행상황 헷갈리지 않게 업데이트하고 git commit도 실시
- 그리고 나서 다시 html 파일 생성 진행

---

**Cursor**

단계별로 진행합니다.


TODOs.md 업데이트 중.


```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 1단계: 정량적 평가 실행
  - [ ] `evaluate_manual_review()` 함수 실행
  - [ ] 타입 분류 정확도 계산
  - [ ] 혼동 행렬 생성 및 분석
  - [ ] 처리 방법별 정확도 비교 (LLM vs Regex)
  - [ ] Summary 품질 점수 통계 분석
  - [ ] 평가 결과 리포트 생성 및 저장 (`tests/reports/manual_review_evaluation_YYYYMMDD_HHMMSS.json`)

- [ ] 2단계: 정성적 분석 - Notes 내용 확인
  - [ ] **⚠️ 중요**: 휴리스틱 기반 평가의 한계를 보완하기 위해 notes 내용을 하나씩 확인
  - [ ] `manual_review_updated.json`의 모든 샘플(67개) 순회
  - [ ] 각 샘플의 `notes` 필드 내용 확인
  - [ ] `correct_type`과 `current_event.type`이 다른 경우 notes 확인
  - [ ] `summary_quality` 또는 `summary_completeness`가 3점 이하인 경우 notes 확인
  - [ ] `type_accuracy`가 3점 이하인 경우 notes 확인
  - [ ] notes 내용을 바탕으로 문제 패턴 분류:
    - [ ] 타입 분류 오류 패턴 (예: "status_review로 분류되었지만 실제로는 plan")
    - [ ] Summary 품질 문제 패턴 (예: "요약이 너무 길다", "핵심 내용 누락")
    - [ ] LLM 프롬프트 문제 (예: "LLM이 잘못 이해함")
    - [ ] 정규식 패턴 문제 (예: "패턴이 너무 엄격함")
    - [ ] 맥락 부족 문제 (예: "이전 Turn의 맥락이 없어서 어려움")
    - [ ] 타입 정의 부족 문제 (예: "새로운 type 정의 필요")
  - [ ] Notes 분석 결과 리포트 생성 및 저장 (`tests/reports/manual_review_notes_analysis_YYYYMMDD_HHMMSS.json`)

- [ ] 3단계: 문제 원인 분석 및 개선 방안 도출
  - [ ] Notes 분석 결과를 바탕으로 문제 원인 도출:
    - [ ] 타입 분류 오류 원인 (LLM 프롬프트, 정규식 패턴, 우선순위 로직, 맥락 부족 등)
    - [ ] Summary 품질 문제 원인 (요약 길이, 핵심 내용 추출 실패, 중간 과정 텍스트 포함 등)
  - [ ] 개선 방안 도출:
    - [ ] Type 추출 로직 개선 방안
    - [ ] Summary 로직 개선 방안
    - [ ] LLM 프롬프트 개선 방안 (필요 시)
    - [ ] 정규식 패턴 개선 방안 (필요 시)
    - [ ] 맥락 처리 개선 방안 (이전 Turn 정보 활용)
    - [ ] 타입 정의 확장 방안 (필요 시)
  - [ ] 개선 방안 우선순위화
  - [ ] 개선 계획 문서 생성 (`tests/reports/improvement_plan_YYYYMMDD_HHMMSS.md`)

- [ ] 4단계: 개선 방안 검토 및 승인
  - [ ] 사용자와 개선 방안 검토
  - [ ] 우선순위 조정 (필요 시)
  - [ ] 개선 작업 범위 결정

- [ ] 5단계: 개선 작업 실행
  - [ ] Type 추출 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [ ] 메타데이터 Turn 처리 로직 개선 (메타데이터는 별도 타입으로 분류 또는 제외)
    - [ ] LLM 프롬프트 개선 (타입 분류 정확도 향상)
    - [ ] 정규식 패턴 개선 (타입 분류 정확도 향상)
    - [ ] 타입 분류 우선순위 로직 개선
    - [ ] 맥락 처리 로직 개선 (이전 Turn 정보 활용)
  - [ ] Summary 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [ ] LLM Summary 생성 프롬프트 개선 (핵심 내용만 추출)
    - [ ] 정규식 기반 Summary 생성 로직 개선 (의미 있는 요약 생성)
    - [ ] 텍스트 자르기 로직 개선 (문장/문단 단위로 의미 있는 위치에서 자르기)
    - [ ] 중간 과정 텍스트 필터링 로직 추가
    - [ ] 맥락 기반 Summary 생성 로직 개선 (이전 Turn 정보 활용)

- [ ] 6단계: E2E 재평가
  - [ ] 개선된 이벤트 정규화 로직으로 E2E 테스트 재실행 (`tests/test_event_normalizer_e2e.py`)
  - [ ] 타입 분류 정확도 재측정
  - [ ] Summary 품질 재평가
  - [ ] Timeline/Issue Cards 품질 재검증 (Phase 4 E2E 테스트 재실행)
  - [ ] 개선 전후 비교 분석
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
  - Phase 4 E2E 테스트 결과 분석 완료 (Timeline/Issue Cards 품질 문제 발견)
  - ✅ 수동 검증 파일 재작성 완료 (2025-12-23)
    - ✅ HTML 형식으로 모든 이벤트 추출 (67개 이벤트)
    - ✅ 사용자 수동 검증 완료 (텍스트 파일 기록)
    - ✅ 텍스트 파일 파싱 스크립트 작성 및 실행 완료
    - ✅ manual_review_updated.json 생성 완료 (67개 이벤트 검증 데이터 포함)
  - 이벤트 정규화 품질 개선 작업 진행 중
    - [ ] 1단계: 정량적 평가 실행 (`evaluate_manual_review()` 실행)
    - [ ] 2단계: 정성적 분석 - Notes 내용 확인 (67개 샘플 순회, notes 필드 하나씩 확인)
    - [ ] 3단계: 문제 원인 분석 및 개선 방안 도출
    - [ ] 4단계: 개선 방안 검토 및 승인 (with 사용자)
    - [ ] 5단계: 개선 작업 실행 (Type 추출 로직, Summary 로직 수정)
    - [ ] 6단계: E2E 재평가 (개선 전후 비교)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

```markdown
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [x] 맥락 정보 수집 함수 구현 (_collect_context_info)
      - [x] 이벤트 정규화 함수에 맥락 정보 전달
      - [x] E2E 테스트 실행 및 결과 검증
    - [ ] 6단계: E2E 재평가 (개선 전후 비교)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)
```

TODOs.md의 진행 상황 섹션 업데이트 중.


```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 1단계: 정량적 평가 실행
  - [ ] `evaluate_manual_review()` 함수 실행
  - [ ] 타입 분류 정확도 계산
  - [ ] 혼동 행렬 생성 및 분석
  - [ ] 처리 방법별 정확도 비교 (LLM vs Regex)
  - [ ] Summary 품질 점수 통계 분석
  - [ ] 평가 결과 리포트 생성 및 저장 (`tests/reports/manual_review_evaluation_YYYYMMDD_HHMMSS.json`)

- [ ] 2단계: 정성적 분석 - Notes 내용 확인
  - [ ] **⚠️ 중요**: 휴리스틱 기반 평가의 한계를 보완하기 위해 notes 내용을 하나씩 확인
  - [ ] `manual_review_updated.json`의 모든 샘플(67개) 순회
  - [ ] 각 샘플의 `notes` 필드 내용 확인
  - [ ] `correct_type`과 `current_event.type`이 다른 경우 notes 확인
  - [ ] `summary_quality` 또는 `summary_completeness`가 3점 이하인 경우 notes 확인
  - [ ] `type_accuracy`가 3점 이하인 경우 notes 확인
  - [ ] notes 내용을 바탕으로 문제 패턴 분류:
    - [ ] 타입 분류 오류 패턴 (예: "status_review로 분류되었지만 실제로는 plan")
    - [ ] Summary 품질 문제 패턴 (예: "요약이 너무 길다", "핵심 내용 누락")
    - [ ] LLM 프롬프트 문제 (예: "LLM이 잘못 이해함")
    - [ ] 정규식 패턴 문제 (예: "패턴이 너무 엄격함")
    - [ ] 맥락 부족 문제 (예: "이전 Turn의 맥락이 없어서 어려움")
    - [ ] 타입 정의 부족 문제 (예: "새로운 type 정의 필요")
  - [ ] Notes 분석 결과 리포트 생성 및 저장 (`tests/reports/manual_review_notes_analysis_YYYYMMDD_HHMMSS.json`)

- [ ] 3단계: 문제 원인 분석 및 개선 방안 도출
  - [ ] Notes 분석 결과를 바탕으로 문제 원인 도출:
    - [ ] 타입 분류 오류 원인 (LLM 프롬프트, 정규식 패턴, 우선순위 로직, 맥락 부족 등)
    - [ ] Summary 품질 문제 원인 (요약 길이, 핵심 내용 추출 실패, 중간 과정 텍스트 포함 등)
  - [ ] 개선 방안 도출:
    - [ ] Type 추출 로직 개선 방안
    - [ ] Summary 로직 개선 방안
    - [ ] LLM 프롬프트 개선 방안 (필요 시)
    - [ ] 정규식 패턴 개선 방안 (필요 시)
    - [ ] 맥락 처리 개선 방안 (이전 Turn 정보 활용)
    - [ ] 타입 정의 확장 방안 (필요 시)
  - [ ] 개선 방안 우선순위화
  - [ ] 개선 계획 문서 생성 (`tests/reports/improvement_plan_YYYYMMDD_HHMMSS.md`)

- [ ] 4단계: 개선 방안 검토 및 승인
  - [ ] 사용자와 개선 방안 검토
  - [ ] 우선순위 조정 (필요 시)
  - [ ] 개선 작업 범위 결정

- [ ] 5단계: 개선 작업 실행
  - [ ] Type 추출 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [ ] 메타데이터 Turn 처리 로직 개선 (메타데이터는 별도 타입으로 분류 또는 제외)
    - [ ] LLM 프롬프트 개선 (타입 분류 정확도 향상)
    - [ ] 정규식 패턴 개선 (타입 분류 정확도 향상)
    - [ ] 타입 분류 우선순위 로직 개선
    - [ ] 맥락 처리 로직 개선 (이전 Turn 정보 활용)
  - [ ] Summary 로직 수정 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
    - [ ] LLM Summary 생성 프롬프트 개선 (핵심 내용만 추출)
    - [ ] 정규식 기반 Summary 생성 로직 개선 (의미 있는 요약 생성)
    - [ ] 텍스트 자르기 로직 개선 (문장/문단 단위로 의미 있는 위치에서 자르기)
    - [ ] 중간 과정 텍스트 필터링 로직 추가
    - [ ] 맥락 기반 Summary 생성 로직 개선 (이전 Turn 정보 활용)

- [ ] 6단계: E2E 재평가
  - [ ] 개선된 이벤트 정규화 로직으로 E2E 테스트 재실행 (`tests/test_event_normalizer_e2e.py`)
  - [ ] 타입 분류 정확도 재측정
  - [ ] Summary 품질 재평가
  - [ ] Timeline/Issue Cards 품질 재검증 (Phase 4 E2E 테스트 재실행)
  - [ ] 개선 전후 비교 분석
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [x] 맥락 정보 수집 함수 구현 (_collect_context_info)
      - [x] 이벤트 정규화 함수에 맥락 정보 전달
      - [x] E2E 테스트 실행 및 결과 검증
    - [ ] 6단계: E2E 재평가 (개선 전후 비교)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

---

**User**

상황 파악이 미흡합니다.
우리는 Phase3의 1,2,3 단계를 진행하고, 문제가 발생해서, 이를 반영한 수정을 진행한 것입니다. 그러니 6단계까지 진행된 것입니다.
그결과를 다시 확인하려고 하고 있는 것입니다.
그게 문제가 있으면 다시 3단계로 가서 3->4->5>6으로 진행해야 겠지요
이해 했나요?


---

**Cursor**

상황 파악 중입니다. 현재 상태 확인 중입니다.


상황 정리:

- 1–3단계: 정량적 평가, 정성적 분석, 문제 원인 분석 및 개선 방안 도출 → 완료
- 4단계: 개선 방안 검토 및 승인 → 완료
- 5단계: 개선 작업 실행 (Artifact 정보 포함, 맥락 정보 추가 등) → 완료
- 6단계: E2E 재평가 → 실행 완료(결과 확인 필요)
- 현재: 6단계 결과를 HTML로 확인하려는 단계

최신 E2E 테스트 결과 파일 확인 중.


상황 정리:

- 1–3단계: 완료
- 4단계: 완료
- 5단계: 완료
- 6단계: E2E 재평가 실행 완료 (결과 확인 필요)
- 현재: 6단계 결과를 HTML로 확인하는 단계

최신 결과 파일: `event_normalizer_e2e_llm_20251225_183334.json` (개선 작업 후 실행)

다음 단계:
1. 최신 결과 파일로 HTML 생성
2. 결과 확인
3. 문제가 있으면 3단계로 돌아가서 3→4→5→6 재진행

TODOs.md 업데이트 제안:

```markdown
- [x] 5단계: 개선 작업 실행 (Type 추출 로직, Summary 로직 수정) - 완료
  - [x] LLM 서비스에 Artifact 정보 포함 (code_blocks, path_candidates)
  - [x] 캐시 키 생성 시 Artifact 정보 포함
  - [x] 맥락 정보 수집 함수 구현 (_collect_context_info)
  - [x] 이벤트 정규화 함수에 맥락 정보 전달
  - [x] E2E 테스트 실행 및 결과 검증
- [x] 6단계: E2E 재평가 (개선 전후 비교) - 완료
  - [x] 개선된 이벤트 정규화 로직으로 E2E 테스트 재실행 완료
  - [x] 결과 파일 생성: `tests/results/event_normalizer_e2e_llm_20251225_183334.json`
  - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토
  - [ ] 개선 전후 비교 분석 (진행 중)
- [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)
```

이대로 진행할까요?

```markdown
- [x] 5단계: 개선 작업 실행 (Type 추출 로직, Summary 로직 수정) - 완료
  - [x] LLM 서비스에 Artifact 정보 포함 (code_blocks, path_candidates)
  - [x] 캐시 키 생성 시 Artifact 정보 포함
  - [x] 맥락 정보 수집 함수 구현 (_collect_context_info)
  - [x] 이벤트 정규화 함수에 맥락 정보 전달
  - [x] E2E 테스트 실행 및 결과 검증
- [x] 6단계: E2E 재평가 (개선 전후 비교) - 완료
  - [x] 개선된 이벤트 정규화 로직으로 E2E 테스트 재실행 완료
  - [x] 결과 파일 생성: `tests/results/event_normalizer_e2e_llm_20251225_183334.json`
  - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토
  - [ ] 개선 전후 비교 분석 (진행 중)
- [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)
```

---

**User**

네 이렇게 진행

---

**Cursor**

TODOs.md 업데이트부터 진행합니다.


```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 1단계: 정량적 평가 실행
  - [ ] `evaluate_manual_review()` 함수 실행
  - [ ] 타입 분류 정확도 계산
  - [ ] 혼동 행렬 생성 및 분석
  - [ ] 처리 방법별 정확도 비교 (LLM vs Regex)
  - [ ] Summary 품질 점수 통계 분석
  - [ ] 평가 결과 리포트 생성 및 저장 (`tests/reports/manual_review_evaluation_YYYYMMDD_HHMMSS.json`)

- [ ] 2단계: 정성적 분석 - Notes 내용 확인
  - [ ] **⚠️ 중요**: 휴리스틱 기반 평가의 한계를 보완하기 위해 notes 내용을 하나씩 확인
  - [ ] `manual_review_updated.json`의 모든 샘플(67개) 순회
  - [ ] 각 샘플의 `notes` 필드 내용 확인
  - [ ] `correct_type`과 `current_event.type`이 다른 경우 notes 확인
  - [ ] `summary_quality` 또는 `summary_completeness`가 3점 이하인 경우 notes 확인
  - [ ] `type_accuracy`가 3점 이하인 경우 notes 확인
  - [ ] notes 내용을 바탕으로 문제 패턴 분류:
    - [ ] 타입 분류 오류 패턴 (예: "status_review로 분류되었지만 실제로는 plan")
    - [ ] Summary 품질 문제 패턴 (예: "요약이 너무 길다", "핵심 내용 누락")
    - [ ] LLM 프롬프트 문제 (예: "LLM이 잘못 이해함")
    - [ ] 정규식 패턴 문제 (예: "패턴이 너무 엄격함")
    - [ ] 맥락 부족 문제 (예: "이전 Turn의 맥락이 없어서 어려움")
    - [ ] 타입 정의 부족 문제 (예: "새로운 type 정의 필요")
  - [ ] Notes 분석 결과 리포트 생성 및 저장 (`tests/reports/manual_review_notes_analysis_YYYYMMDD_HHMMSS.json`)

- [ ] 3단계: 문제 원인 분석 및 개선 방안 도출
  - [ ] Notes 분석 결과를 바탕으로 문제 원인 도출:
    - [ ] 타입 분류 오류 원인 (LLM 프롬프트, 정규식 패턴, 우선순위 로직, 맥락 부족 등)
    - [ ] Summary 품질 문제 원인 (요약 길이, 핵심 내용 추출 실패, 중간 과정 텍스트 포함 등)
  - [ ] 개선 방안 도출:
    - [ ] Type 추출 로직 개선 방안
    - [ ] Summary 로직 개선 방안
    - [ ] LLM 프롬프트 개선 방안 (필요 시)
    - [ ] 정규식 패턴 개선 방안 (필요 시)
    - [ ] 맥락 처리 개선 방안 (이전 Turn 정보 활용)
    - [ ] 타입 정의 확장 방안 (필요 시)
  - [ ] 개선 방안 우선순위화
  - [ ] 개선 계획 문서 생성 (`tests/reports/improvement_plan_YYYYMMDD_HHMMSS.md`)

- [ ] 4단계: 개선 방안 검토 및 승인
  - [ ] 사용자와 개선 방안 검토
  - [ ] 우선순위 조정 (필요 시)
  - [ ] 개선 작업 범위 결정

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
  - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
  - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [x] 맥락 정보 수집 함수 구현 (_collect_context_info)
      - [x] 이벤트 정규화 함수에 맥락 정보 전달
      - [x] E2E 테스트 실행 및 결과 검증
    - [ ] 6단계: E2E 재평가 (개선 전후 비교)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 1단계: 정량적 평가 실행
  - [ ] `evaluate_manual_review()` 함수 실행
  - [ ] 타입 분류 정확도 계산
  - [ ] 혼동 행렬 생성 및 분석
  - [ ] 처리 방법별 정확도 비교 (LLM vs Regex)
  - [ ] Summary 품질 점수 통계 분석
  - [ ] 평가 결과 리포트 생성 및 저장 (`tests/reports/manual_review_evaluation_YYYYMMDD_HHMMSS.json`)

- [ ] 2단계: 정성적 분석 - Notes 내용 확인
  - [ ] **⚠️ 중요**: 휴리스틱 기반 평가의 한계를 보완하기 위해 notes 내용을 하나씩 확인
  - [ ] `manual_review_updated.json`의 모든 샘플(67개) 순회
  - [ ] 각 샘플의 `notes` 필드 내용 확인
  - [ ] `correct_type`과 `current_event.type`이 다른 경우 notes 확인
  - [ ] `summary_quality` 또는 `summary_completeness`가 3점 이하인 경우 notes 확인
  - [ ] `type_accuracy`가 3점 이하인 경우 notes 확인
  - [ ] notes 내용을 바탕으로 문제 패턴 분류:
    - [ ] 타입 분류 오류 패턴 (예: "status_review로 분류되었지만 실제로는 plan")
    - [ ] Summary 품질 문제 패턴 (예: "요약이 너무 길다", "핵심 내용 누락")
    - [ ] LLM 프롬프트 문제 (예: "LLM이 잘못 이해함")
    - [ ] 정규식 패턴 문제 (예: "패턴이 너무 엄격함")
    - [ ] 맥락 부족 문제 (예: "이전 Turn의 맥락이 없어서 어려움")
    - [ ] 타입 정의 부족 문제 (예: "새로운 type 정의 필요")
  - [ ] Notes 분석 결과 리포트 생성 및 저장 (`tests/reports/manual_review_notes_analysis_YYYYMMDD_HHMMSS.json`)

- [ ] 3단계: 문제 원인 분석 및 개선 방안 도출
  - [ ] Notes 분석 결과를 바탕으로 문제 원인 도출:
    - [ ] 타입 분류 오류 원인 (LLM 프롬프트, 정규식 패턴, 우선순위 로직, 맥락 부족 등)
    - [ ] Summary 품질 문제 원인 (요약 길이, 핵심 내용 추출 실패, 중간 과정 텍스트 포함 등)
  - [ ] 개선 방안 도출:
    - [ ] Type 추출 로직 개선 방안
    - [ ] Summary 로직 개선 방안
    - [ ] LLM 프롬프트 개선 방안 (필요 시)
    - [ ] 정규식 패턴 개선 방안 (필요 시)
    - [ ] 맥락 처리 개선 방안 (이전 Turn 정보 활용)
    - [ ] 타입 정의 확장 방안 (필요 시)
  - [ ] 개선 방안 우선순위화
  - [ ] 개선 계획 문서 생성 (`tests/reports/improvement_plan_YYYYMMDD_HHMMSS.md`)

- [ ] 4단계: 개선 방안 검토 및 승인
  - [ ] 사용자와 개선 방안 검토
  - [ ] 우선순위 조정 (필요 시)
  - [ ] 개선 작업 범위 결정

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
  - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
  - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
      - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

---

**User**

TODOs.md가 왜 1,2,3,4 단계도 완료 처리 안되었나요?

---

**Cursor**

TODOs.md에서 1-4단계도 완료 처리하겠습니다.


```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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
  - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
  - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
      - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

---

**User**

그리고 6단계에서 결과 확인시 문제 있으면 3단계로 다시 돌아간다고 명시하세요


---

**Cursor**

6단계에 '결과 확인에서 문제 발견 시 3단계로 복귀'를 명시하도록 수정 중입니다.


```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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
  - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
    - [ ] ⚠️ **중요**: 결과 확인 시 문제가 발견되면 **3단계(문제 원인 분석 및 개선 방안 도출)**로 돌아가서 재분석 및 개선 작업 진행
  - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
      - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

TODOs.md의 6단계에 "결과 확인 시 문제 발견 시 3단계로 복귀"를 명시했습니다.

**수정 내용**:
- 6단계의 "결과 확인" 항목에 다음을 추가:
  - ⚠️ **중요**: 결과 확인 시 문제가 발견되면 **3단계(문제 원인 분석 및 개선 방안 도출)**로 돌아가서 재분석 및 개선 작업 진행

이제 6단계에서 문제가 발견되면 3단계로 돌아가 재분석 및 개선을 진행하는 워크플로우가 명확히 문서화되었습니다.

다음 단계로 진행할까요? (예: HTML 수동 검증 데이터셋 생성)

---

**User**

네 다음 단계 진행

---

**Cursor**

HTML 수동 검증 데이터셋 생성 중입니다. 최신 E2E 재평가 결과를 사용합니다.


HTML 수동 검증 데이터셋 생성 완료.

생성된 파일:
- HTML 파일: `tests\manual_review\all_events_html_review_20251225_211525\manual_review.html`
- JSON 데이터: `tests\manual_review\all_events_html_review_20251225_211525\manual_review_data.json`
- 총 67개 이벤트

다음 단계:
1. HTML 파일을 브라우저에서 열기
2. 각 이벤트의 `correct_type` 입력 및 `notes` 입력
3. 'Export to JSON' 버튼 클릭하여 다운로드
4. 다운로드한 JSON 파일을 다음 위치에 저장:
   - `tests\manual_review\all_events_html_review_20251225_211525\manual_review_updated.json`
   - 또는 다운로드한 파일명 그대로 사용 (타임스탬프 포함)

TODOs.md 업데이트 중입니다.


```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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
    - [ ] 사용자 수동 검증 대기 중 (HTML에서 correct_type 및 notes 입력 후 JSON 다운로드)
    - [ ] ⚠️ **중요**: 결과 확인 시 문제가 발견되면 **3단계(문제 원인 분석 및 개선 방안 도출)**로 돌아가서 재분석 및 개선 작업 진행
  - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
  - [ ] 비교 리포트 생성 (`tests/reports/improvement_comparison_YYYYMMDD_HHMMSS.json`)

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
      - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

HTML 수동 검증 데이터셋 생성 완료.

**생성된 파일**:
- **HTML 파일**: `tests\manual_review\all_events_html_review_20251225_211525\manual_review.html`
- **JSON 데이터**: `tests\manual_review\all_events_html_review_20251225_211525\manual_review_data.json`
- **총 67개 이벤트**

**다음 단계**:
1. HTML 파일을 브라우저에서 열기
2. 각 이벤트의 `correct_type` 입력 및 `notes` 입력
3. 'Export to JSON' 버튼 클릭하여 다운로드
4. 다운로드한 JSON 파일을 다음 위치에 저장:
   - `tests\manual_review\all_events_html_review_20251225_211525\manual_review_updated.json`
   - 또는 다운로드한 파일명 그대로 사용 (타임스탬프 포함)

**중요 사항**:
- 결과 확인 시 문제가 발견되면 **3단계(문제 원인 분석 및 개선 방안 도출)**로 돌아가서 재분석 및 개선 작업을 진행합니다.

수동 검증 완료 후 알려주시면, 다음 단계(개선 전후 비교 분석)로 진행하겠습니다.

---

**User**

네 수동검증 완료했습니다.

전체적으로 다음과 같은 평가를 내리고 싶습니다.
이를 바탕으로 어떻게 할지 같이 논의합시다. 당신의 의견을 설명하세요
- artifact라는 타입은 무의미할 것 같습니다. 타입이 어떤 activity를 하고 있는지를 설명해주어야 하는데 artifact 만으로는 설명이 안되니까요
- artifact가 나오는 상황은 크게 2가지가 있습니다. 그리고, 추가로 한가지는 artifact로 잘못 인식되지만 artifact가 되어서는 안됩니다.
- artifact 상황 2가지: 사용자의 지시에 따라서 코드 파일을 작성할 경우가 artifact가 됩니다. 하지만 이 경우는 code generation이 맞습니다. 그리고 코드에 문제가 있어 수정하는 경우가 artifact로 인식됩니다. 하지만 이경우는 debug로 타입이 되어야 합니다. 따라서 이 경우 artifact가 아닌, 각각 code generation과 debug로 합시다
- artifact가 되면 안되는 경우: TODOs.md는 프로젝트 전체의 계획으로 사용되는 내용입니다. 하지만 이것을 읽거나 내용 확인하고, 수정하는 것은 모두 artifact로 보는 것은 의미가 없습니다. 따라서 읽고 내용 확인은 status_review가 타당합니다. 그리고 이를 수정하는 것은, 사용자 지시에 대한 수행이 완료될때, 이를 TODOs.md에 반영하고 git commit하는 것이므로, 이것은 completion이 타당합니다.
- 이 프로젝트의 목적: 이 프로젝트의 목적은, 사용자-커서간의 대화를 바탕으로 어떤 작업이 이루어졌는지, 그 제목과 실제 내용을 파악하는 것입니다. 따라서, 일반적인 flow는 다음과 같습니다.
- 프로젝트 flow: status_review (프로젝트의 현 상황 파악) -> plan (이를 바탕으로 사용자가 지시하고, 지시한 내용을 수행하는 절차 수립) -> code generation (실제 작업의 핵심인 코드 생성) -> plan (사용자가 보통 코드를 실행한 결과의 확인을 요청) -> status_review(코드의 실행 결과를 리뷰) -> debug1 (문제가 발생시, 그 원인을 파악) -> debug2 (원인을 파악하여 개선 계획 수립) -> debug3 (개선 계획대로 코드 수정하고 결과 파악) -> 문제 있으면 다시 debug1~3의 과정을 거침 -> status_review (문제 해결 완료되면 현재 어떤 단계인지 확인) -> completion (문제 없으면, 진행 상황 TODOs.md에 업데이트하고 git commit 실시) -> next_step (사용자가 다음 단계를 계속 진행할거면 다음 step 으로 지시, 아니면 여기서 완료로 completion으로 끝나면 됨)

전체 그림이 잘 그려지는지요? 당신의 언어로 다시 설명해보세요
전체 프로젝트의 흐름과
그 상황에서 우리의 e2e 결과를 어떻게 이해하면 될까요?

---

**Cursor**

현재 코드베이스의 EventType 정의와 사용 현황을 확인 중입니다.


사용자 제안을 바탕으로 전체 타입 체계와 프로젝트 흐름을 정리 중입니다.


## 전체 그림 재정리

### 1. 프로젝트의 핵심 목적
사용자-커서 대화에서 수행된 작업과 그 내용을 파악하는 것. 따라서 이벤트 타입은 "무엇을 하는지"를 명확히 표현해야 합니다.

### 2. 현재 `artifact` 타입의 문제점
- `artifact`는 "파일이 있다"는 상태만 나타내고, "무엇을 하는지"를 설명하지 않습니다.
- 예: "TODOs.md를 읽는다"와 "TODOs.md를 수정한다"는 다른 활동이지만, 현재는 둘 다 `artifact`로 분류됩니다.

### 3. 제안된 타입 체계 재구성

#### 제거: `artifact` 타입
#### 추가: `code_generation` 타입
- 사용자 지시에 따라 새 코드 파일을 작성하는 경우
- 예: "새로운 컴포넌트를 생성합니다" + 코드 블록

#### 기존 타입 재활용:
- `debug`: 코드에 문제가 있어 수정하는 경우 (기존 `artifact` 중 일부)
- `status_review`: TODOs.md나 기타 파일을 읽고 내용을 확인하는 경우 (기존 `artifact` 중 일부)
- `completion`: TODOs.md 수정/반영 및 git commit (기존 `artifact` 중 일부)

### 4. 프로젝트 Flow (사용자 제안)

```
1. status_review
   ↓ (프로젝트 현황 파악)
2. plan
   ↓ (사용자 지시 + 수행 절차 수립)
3. code_generation
   ↓ (실제 코드 생성)
4. plan
   ↓ (코드 실행 결과 확인 요청)
5. status_review
   ↓ (실행 결과 리뷰)
6. debug1 (문제 발생 시)
   ↓ (원인 파악)
7. debug2
   ↓ (개선 계획 수립)
8. debug3
   ↓ (코드 수정 및 결과 파악)
   ↓ (문제 있으면 6-8 반복)
9. status_review
   ↓ (문제 해결 완료 확인)
10. completion
    ↓ (TODOs.md 업데이트 + git commit)
11. next_step
    ↓ (다음 단계 지시 또는 완료)
```

### 5. E2E 결과 재해석

현재 E2E 결과에서 `artifact`로 분류된 이벤트들을 재분류하면:

#### Case 1: TODOs.md 읽기/확인 (seq 2, 3, 4, 5 등)
- 현재: `artifact`
- 재분류: `status_review`
- 이유: 프로젝트 현황을 파악하는 활동

#### Case 2: 코드 파일 작성 (코드 블록이 있는 경우)
- 현재: `artifact`
- 재분류: `code_generation`
- 이유: 사용자 지시에 따른 새 코드 생성

#### Case 3: 코드 수정 (문제 해결 맥락)
- 현재: `artifact` 또는 `debug`
- 재분류: `debug`
- 이유: 문제 해결을 위한 코드 수정

#### Case 4: TODOs.md 수정/반영
- 현재: `artifact`
- 재분류: `completion`
- 이유: 작업 완료 후 진행 상황 반영

### 6. 제안하는 개선 방안

#### Option A: 점진적 개선 (권장)
1. `code_generation` 타입 추가
2. `artifact` 타입 제거
3. 기존 `artifact` 이벤트를 맥락에 따라 재분류:
   - 파일 읽기/확인 → `status_review`
   - 코드 작성 → `code_generation`
   - 코드 수정 (문제 해결) → `debug`
   - 파일 수정/반영 → `completion`

#### Option B: 전체 재분류
- 수동 검증 결과를 바탕으로 모든 이벤트 재분류
- 새로운 타입 체계로 Golden 파일 재생성

### 7. 구현 시 고려사항

#### LLM 프롬프트 수정 필요:
- `artifact` 타입 제거
- `code_generation` 타입 추가 및 정의
- 파일 읽기 vs 파일 수정 구분 로직 강화

#### 분류 로직 개선:
- 파일 경로만으로는 타입 결정 불가
- 맥락 정보 활용 필수:
  - 이전 Turn에 `plan`이 있고 코드 블록이 있으면 → `code_generation`
  - 이전 Turn에 `debug`가 있고 코드 블록이 있으면 → `debug`
  - 파일 경로만 있고 읽기 키워드가 있으면 → `status_review`
  - 완료 키워드 + TODOs.md 수정 → `completion`

### 8. 다음 단계 제안

1. 수동 검증 결과 분석: 현재 `artifact`로 분류된 이벤트들을 새로운 타입 체계로 재분류
2. 타입 체계 업데이트: `EventType` Enum 수정 (`code_generation` 추가, `artifact` 제거)
3. 분류 로직 개선: 맥락 기반 분류 로직 강화
4. LLM 프롬프트 수정: 새로운 타입 체계 반영
5. 재평가: 새로운 타입 체계로 E2E 테스트 재실행

이 방향으로 진행할까요? 수동 검증 결과를 먼저 분석해 새로운 타입 체계로 재분류하는 것부터 시작하는 것을 권장합니다.

```plaintext
1. status_review
   ↓ (프로젝트 현황 파악)
2. plan
   ↓ (사용자 지시 + 수행 절차 수립)
3. code_generation
   ↓ (실제 코드 생성)
4. plan
   ↓ (코드 실행 결과 확인 요청)
5. status_review
   ↓ (실행 결과 리뷰)
6. debug1 (문제 발생 시)
   ↓ (원인 파악)
7. debug2
   ↓ (개선 계획 수립)
8. debug3
   ↓ (코드 수정 및 결과 파악)
   ↓ (문제 있으면 6-8 반복)
9. status_review
   ↓ (문제 해결 완료 확인)
10. completion
    ↓ (TODOs.md 업데이트 + git commit)
11. next_step
    ↓ (다음 단계 지시 또는 완료)
```

---

**User**

대신 타입별로 artifact가 링크되는지 아닌지, 그 정보는 있어야 합니다.
그걸 표현하는 별도의 방법은 필요하겠네요. 그러면 나중에 event의 흐름은 있는 상태에서 중간중간에 어떤 타입의 이벤트는, 별도 artifact를 연결해서 나중에 확인 가능하게
그걸 감안해서, 위의 내용을 다시 정리해보세요

---

**Cursor**

타입과 artifact 정보를 분리해 정리합니다. 현재 모델 구조를 확인 중입니다.


타입과 artifact 정보를 분리해 정리했습니다.

## 개선된 타입 체계 정리

### 1. 핵심 원칙

**타입 = "무엇을 하는지" (Activity)**
- 각 타입은 수행되는 활동을 명확히 표현
- 예: `code_generation` (코드 생성), `debug` (문제 해결), `status_review` (상태 확인)

**Artifact 정보 = "어떤 파일/코드가 관련되었는지" (Metadata)**
- `Event.artifacts` 필드에 별도로 저장
- 타입과 독립적으로 관리
- 나중에 Timeline에서 특정 이벤트의 상세 내용 확인 가능

### 2. 새로운 EventType 체계

```python
class EventType(str, Enum):
    STATUS_REVIEW = "status_review"  # 상태 확인/리뷰
    PLAN = "plan"                    # 계획 수립
    CODE_GENERATION = "code_generation"  # 코드 생성 (새로 추가)
    DEBUG = "debug"                  # 문제 해결
    COMPLETION = "completion"        # 완료
    NEXT_STEP = "next_step"         # 다음 단계
    TURN = "turn"                    # 일반 대화 (fallback)
    
    # 제거: ARTIFACT = "artifact"
```

### 3. 타입별 Artifact 연결 가능성

| 타입 | Artifact 연결 가능 | 예시 |
|------|-------------------|------|
| `status_review` | ✅ 가능 | TODOs.md 읽기, 파일 내용 확인 |
| `plan` | ⚠️ 드물게 | 계획 문서 참조 시 |
| `code_generation` | ✅ 필수 | 생성된 파일 경로, 코드 블록 |
| `debug` | ✅ 필수 | 수정된 파일 경로, 수정된 코드 |
| `completion` | ✅ 가능 | 업데이트된 파일 경로 (TODOs.md 등) |
| `next_step` | ❌ 드물게 | - |
| `turn` | ⚠️ 드물게 | - |

### 4. 프로젝트 Flow (개선된 버전)

```
1. status_review
   ↓ (프로젝트 현황 파악)
   [artifacts: ["TODOs.md"]]
   
2. plan
   ↓ (사용자 지시 + 수행 절차 수립)
   
3. code_generation
   ↓ (실제 코드 생성)
   [artifacts: ["frontend/components/NewComponent.tsx"], 
    snippet_refs: ["turn_5_block_0"]]
   
4. plan
   ↓ (코드 실행 결과 확인 요청)
   
5. status_review
   ↓ (실행 결과 리뷰)
   [artifacts: ["output.log"]]
   
6. debug1 (문제 발생 시)
   ↓ (원인 파악)
   [artifacts: ["error.log"]]
   
7. debug2
   ↓ (개선 계획 수립)
   
8. debug3
   ↓ (코드 수정 및 결과 파악)
   [artifacts: ["frontend/components/NewComponent.tsx"],
    snippet_refs: ["turn_8_block_0"]]
   ↓ (문제 있으면 6-8 반복)
   
9. status_review
   ↓ (문제 해결 완료 확인)
   
10. completion
    ↓ (TODOs.md 업데이트 + git commit)
    [artifacts: ["TODOs.md"]]
    
11. next_step
    ↓ (다음 단계 지시 또는 완료)
```

### 5. E2E 결과 재해석 (개선된 관점)

현재 `artifact` 타입으로 분류된 이벤트들을 재분류:

#### Case 1: TODOs.md 읽기/확인
```json
{
  "type": "status_review",  // 변경: artifact → status_review
  "summary": "TODOs.md 파일을 참조하여 프로젝트의 현재 진행 상황을 파악합니다.",
  "artifacts": [{"path": "TODOs.md", "action": "read"}]  // 유지
}
```

#### Case 2: 코드 파일 작성
```json
{
  "type": "code_generation",  // 변경: artifact → code_generation
  "summary": "새로운 컴포넌트를 생성합니다.",
  "artifacts": [{"path": "frontend/components/NewComponent.tsx", "action": "create"}],
  "snippet_refs": ["turn_10_block_0"]  // 코드 블록 참조
}
```

#### Case 3: 코드 수정 (문제 해결)
```json
{
  "type": "debug",  // 변경: artifact → debug
  "summary": "에러를 수정하기 위해 코드를 변경합니다.",
  "artifacts": [{"path": "backend/api/routes.py", "action": "modify"}],
  "snippet_refs": ["turn_15_block_0"]
}
```

#### Case 4: TODOs.md 수정/반영
```json
{
  "type": "completion",  // 변경: artifact → completion
  "summary": "작업 완료 후 TODOs.md에 진행 상황을 반영합니다.",
  "artifacts": [{"path": "TODOs.md", "action": "update"}]
}
```

### 6. Artifact Action 타입 확장

현재 `action: "mention"`만 있는데, 더 구체적인 액션 타입 추가:

```python
# Artifact Action 타입 (제안)
class ArtifactAction(str, Enum):
    READ = "read"        # 읽기/확인
    CREATE = "create"    # 생성
    MODIFY = "modify"    # 수정
    EXECUTE = "execute"  # 실행
    MENTION = "mention"  # 단순 언급 (기본값)
```

### 7. Timeline에서의 활용

나중에 Timeline을 볼 때:
- `code_generation` 타입 이벤트 클릭 → `artifacts`에서 생성된 파일 확인 → `snippet_refs`에서 실제 코드 확인
- `debug` 타입 이벤트 클릭 → `artifacts`에서 수정된 파일 확인 → `snippet_refs`에서 수정된 코드 확인
- `status_review` 타입 이벤트 클릭 → `artifacts`에서 확인한 파일 목록 확인

### 8. 구현 계획

#### Step 1: EventType Enum 수정
- `ARTIFACT` 제거
- `CODE_GENERATION` 추가

#### Step 2: Artifact Action 타입 추가 (선택)
- `ArtifactAction` Enum 추가
- 기존 `"mention"`을 더 구체적인 액션으로 확장

#### Step 3: 분류 로직 개선
- 파일 경로만으로 타입 결정하지 않음
- 맥락 기반 분류:
  - 코드 블록 + 이전 Turn에 `plan` → `code_generation`
  - 코드 블록 + 이전 Turn에 `debug` → `debug`
  - 파일 경로만 + 읽기 키워드 → `status_review`
  - 완료 키워드 + TODOs.md → `completion`

#### Step 4: LLM 프롬프트 수정
- `artifact` 타입 제거
- `code_generation` 타입 추가 및 정의
- Artifact 정보는 타입 분류에 참고하되, 타입 자체는 활동 중심으로 결정

#### Step 5: 수동 검증 결과 재분류
- 기존 `artifact` 타입 이벤트들을 새로운 타입 체계로 재분류
- Artifact 정보는 그대로 유지

### 9. 장점

1. 타입의 의미가 명확해짐: "무엇을 하는지"를 직접 표현
2. Artifact 정보 유지: 파일/코드 참조 가능
3. Timeline에서 상세 확인 가능: 타입별로 관련 artifact 확인
4. 확장성: 새로운 타입 추가 시 artifact 연결 방식 일관성 유지

이 방향으로 진행할까요? 수동 검증 결과를 먼저 분석해 새로운 타입 체계로 재분류하는 것부터 시작하는 것을 권장합니다.

```python
class EventType(str, Enum):
    STATUS_REVIEW = "status_review"  # 상태 확인/리뷰
    PLAN = "plan"                    # 계획 수립
    CODE_GENERATION = "code_generation"  # 코드 생성 (새로 추가)
    DEBUG = "debug"                  # 문제 해결
    COMPLETION = "completion"        # 완료
    NEXT_STEP = "next_step"         # 다음 단계
    TURN = "turn"                    # 일반 대화 (fallback)
    
    # 제거: ARTIFACT = "artifact"
```

```plaintext
1. status_review
   ↓ (프로젝트 현황 파악)
   [artifacts: ["TODOs.md"]]
   
2. plan
   ↓ (사용자 지시 + 수행 절차 수립)
   
3. code_generation
   ↓ (실제 코드 생성)
   [artifacts: ["frontend/components/NewComponent.tsx"], 
    snippet_refs: ["turn_5_block_0"]]
   
4. plan
   ↓ (코드 실행 결과 확인 요청)
   
5. status_review
   ↓ (실행 결과 리뷰)
   [artifacts: ["output.log"]]
   
6. debug1 (문제 발생 시)
   ↓ (원인 파악)
   [artifacts: ["error.log"]]
   
7. debug2
   ↓ (개선 계획 수립)
   
8. debug3
   ↓ (코드 수정 및 결과 파악)
   [artifacts: ["frontend/components/NewComponent.tsx"],
    snippet_refs: ["turn_8_block_0"]]
   ↓ (문제 있으면 6-8 반복)
   
9. status_review
   ↓ (문제 해결 완료 확인)
   
10. completion
    ↓ (TODOs.md 업데이트 + git commit)
    [artifacts: ["TODOs.md"]]
    
11. next_step
    ↓ (다음 단계 지시 또는 완료)
```

```json
{
  "type": "status_review",  // 변경: artifact → status_review
  "summary": "TODOs.md 파일을 참조하여 프로젝트의 현재 진행 상황을 파악합니다.",
  "artifacts": [{"path": "TODOs.md", "action": "read"}]  // 유지
}
```

```json
{
  "type": "code_generation",  // 변경: artifact → code_generation
  "summary": "새로운 컴포넌트를 생성합니다.",
  "artifacts": [{"path": "frontend/components/NewComponent.tsx", "action": "create"}],
  "snippet_refs": ["turn_10_block_0"]  // 코드 블록 참조
}
```

```json
{
  "type": "debug",  // 변경: artifact → debug
  "summary": "에러를 수정하기 위해 코드를 변경합니다.",
  "artifacts": [{"path": "backend/api/routes.py", "action": "modify"}],
  "snippet_refs": ["turn_15_block_0"]
}
```

```json
{
  "type": "completion",  // 변경: artifact → completion
  "summary": "작업 완료 후 TODOs.md에 진행 상황을 반영합니다.",
  "artifacts": [{"path": "TODOs.md", "action": "update"}]
}
```

```python
# Artifact Action 타입 (제안)
class ArtifactAction(str, Enum):
    READ = "read"        # 읽기/확인
    CREATE = "create"    # 생성
    MODIFY = "modify"    # 수정
    EXECUTE = "execute"  # 실행
    MENTION = "mention"  # 단순 언급 (기본값)
```

---

**User**

자 일단은 이렇게 합시다. 
- 위의 내용을 별도의 상세한 마크다운 파일로 정리해서, 다시 참고할 수 있도록 합니다.
- @TODOs.md 에서는 현재 상황을 정리하고, 특히 위의 마크다운 파일을 참고하도록 명시적으로 표현합니다.
- 이것을 실제 실행은 새로운 세션에서 하고, 오늘은 이것으로 정리해서 @TODOs.md 업데이트 및 깃 커밋후 마무리
- 새로운 세션은 TODOs.md를 확인하여, 어디서부터 시작해서, 어떤 파일을 참고하여 컨텍스트 파악하면서 start할지를 분명히 알 수 있도록 진행

---

**Cursor**

타입 체계 개선 계획을 상세 마크다운으로 정리하고, TODOs.md를 업데이트한 뒤 커밋합니다.


```markdown
# Phase 3.4: 이벤트 타입 체계 개선 계획

> **작성일**: 2025-12-25  
> **상태**: 계획 수립 완료, 구현 대기  
> **참고**: Phase 3.4 E2E 재평가 결과 검토 후 수립된 개선 계획

---

## 1. 개선 배경

### 1.1 현재 문제점

**`artifact` 타입의 근본적 문제**:
- `artifact` 타입은 "무엇을 하는지"를 설명하지 못함
- 단순히 "파일이 있다"는 상태만 나타냄
- 실제 활동(activity)을 표현하지 못함

**예시 문제**:
- "TODOs.md를 읽는다"와 "TODOs.md를 수정한다"는 다른 활동이지만, 현재는 둘 다 `artifact`로 분류됨
- 코드 파일 작성과 코드 수정(문제 해결)이 구분되지 않음

### 1.2 프로젝트의 핵심 목적

**사용자-커서 간 대화를 바탕으로 어떤 작업이 이루어졌는지 파악**

따라서 이벤트 타입은 **"무엇을 하는지"**를 명확히 표현해야 함

---

## 2. 개선된 타입 체계

### 2.1 핵심 원칙

**타입 = "무엇을 하는지" (Activity)**
- 각 타입은 수행되는 활동을 명확히 표현
- 예: `code_generation` (코드 생성), `debug` (문제 해결), `status_review` (상태 확인)

**Artifact 정보 = "어떤 파일/코드가 관련되었는지" (Metadata)**
- `Event.artifacts` 필드에 별도로 저장
- 타입과 독립적으로 관리
- 나중에 Timeline에서 특정 이벤트의 상세 내용 확인 가능

### 2.2 새로운 EventType Enum

```python
class EventType(str, Enum):
    STATUS_REVIEW = "status_review"      # 상태 확인/리뷰
    PLAN = "plan"                        # 계획 수립
    CODE_GENERATION = "code_generation"  # 코드 생성 (새로 추가)
    DEBUG = "debug"                      # 문제 해결
    COMPLETION = "completion"            # 완료
    NEXT_STEP = "next_step"             # 다음 단계
    TURN = "turn"                        # 일반 대화 (fallback)
    
    # 제거: ARTIFACT = "artifact"
```

### 2.3 타입별 Artifact 연결 가능성

| 타입 | Artifact 연결 가능 | 예시 |
|------|-------------------|------|
| `status_review` | ✅ 가능 | TODOs.md 읽기, 파일 내용 확인 |
| `plan` | ⚠️ 드물게 | 계획 문서 참조 시 |
| `code_generation` | ✅ 필수 | 생성된 파일 경로, 코드 블록 |
| `debug` | ✅ 필수 | 수정된 파일 경로, 수정된 코드 |
| `completion` | ✅ 가능 | 업데이트된 파일 경로 (TODOs.md 등) |
| `next_step` | ❌ 드물게 | - |
| `turn` | ⚠️ 드물게 | - |

---

## 3. 프로젝트 Flow (개선된 버전)

```
1. status_review
   ↓ (프로젝트 현황 파악)
   [artifacts: ["TODOs.md"]]
   
2. plan
   ↓ (사용자 지시 + 수행 절차 수립)
   
3. code_generation
   ↓ (실제 코드 생성)
   [artifacts: ["frontend/components/NewComponent.tsx"], 
    snippet_refs: ["turn_5_block_0"]]
   
4. plan
   ↓ (코드 실행 결과 확인 요청)
   
5. status_review
   ↓ (실행 결과 리뷰)
   [artifacts: ["output.log"]]
   
6. debug1 (문제 발생 시)
   ↓ (원인 파악)
   [artifacts: ["error.log"]]
   
7. debug2
   ↓ (개선 계획 수립)
   
8. debug3
   ↓ (코드 수정 및 결과 파악)
   [artifacts: ["frontend/components/NewComponent.tsx"],
    snippet_refs: ["turn_8_block_0"]]
   ↓ (문제 있으면 6-8 반복)
   
9. status_review
   ↓ (문제 해결 완료 확인)
   
10. completion
    ↓ (TODOs.md 업데이트 + git commit)
    [artifacts: ["TODOs.md"]]
    
11. next_step
    ↓ (다음 단계 지시 또는 완료)
```

---

## 4. E2E 결과 재해석 (개선된 관점)

### 4.1 Case 1: TODOs.md 읽기/확인

**현재 분류**: `artifact`  
**개선 후**: `status_review`

```json
{
  "type": "status_review",
  "summary": "TODOs.md 파일을 참조하여 프로젝트의 현재 진행 상황을 파악합니다.",
  "artifacts": [{"path": "TODOs.md", "action": "read"}]
}
```

### 4.2 Case 2: 코드 파일 작성

**현재 분류**: `artifact`  
**개선 후**: `code_generation`

```json
{
  "type": "code_generation",
  "summary": "새로운 컴포넌트를 생성합니다.",
  "artifacts": [{"path": "frontend/components/NewComponent.tsx", "action": "create"}],
  "snippet_refs": ["turn_10_block_0"]
}
```

### 4.3 Case 3: 코드 수정 (문제 해결)

**현재 분류**: `artifact` 또는 `debug`  
**개선 후**: `debug`

```json
{
  "type": "debug",
  "summary": "에러를 수정하기 위해 코드를 변경합니다.",
  "artifacts": [{"path": "backend/api/routes.py", "action": "modify"}],
  "snippet_refs": ["turn_15_block_0"]
}
```

### 4.4 Case 4: TODOs.md 수정/반영

**현재 분류**: `artifact`  
**개선 후**: `completion`

```json
{
  "type": "completion",
  "summary": "작업 완료 후 TODOs.md에 진행 상황을 반영합니다.",
  "artifacts": [{"path": "TODOs.md", "action": "update"}]
}
```

---

## 5. Artifact Action 타입 확장 (선택적)

현재 `action: "mention"`만 있는데, 더 구체적인 액션 타입 추가 가능:

```python
# Artifact Action 타입 (제안)
class ArtifactAction(str, Enum):
    READ = "read"        # 읽기/확인
    CREATE = "create"    # 생성
    MODIFY = "modify"    # 수정
    EXECUTE = "execute"  # 실행
    MENTION = "mention"  # 단순 언급 (기본값)
```

---

## 6. Timeline에서의 활용

나중에 Timeline을 볼 때:
- `code_generation` 타입 이벤트 클릭 → `artifacts`에서 생성된 파일 확인 → `snippet_refs`에서 실제 코드 확인
- `debug` 타입 이벤트 클릭 → `artifacts`에서 수정된 파일 확인 → `snippet_refs`에서 수정된 코드 확인
- `status_review` 타입 이벤트 클릭 → `artifacts`에서 확인한 파일 목록 확인

---

## 7. 구현 계획

### Step 1: EventType Enum 수정
- [ ] `backend/core/models.py`에서 `ARTIFACT` 제거
- [ ] `CODE_GENERATION` 추가
- [ ] 관련 상수 파일 업데이트 (`backend/core/constants.py`)

### Step 2: Artifact Action 타입 추가 (선택적)
- [ ] `ArtifactAction` Enum 추가 (선택적, 나중에 확장 가능)
- [ ] 기존 `"mention"`을 더 구체적인 액션으로 확장

### Step 3: 분류 로직 개선
- [ ] 파일 경로만으로 타입 결정하지 않음
- [ ] 맥락 기반 분류:
  - 코드 블록 + 이전 Turn에 `plan` → `code_generation`
  - 코드 블록 + 이전 Turn에 `debug` → `debug`
  - 파일 경로만 + 읽기 키워드 → `status_review`
  - 완료 키워드 + TODOs.md → `completion`

### Step 4: LLM 프롬프트 수정
- [ ] `artifact` 타입 제거
- [ ] `code_generation` 타입 추가 및 정의
- [ ] Artifact 정보는 타입 분류에 참고하되, 타입 자체는 활동 중심으로 결정

### Step 5: 수동 검증 결과 재분류
- [ ] 기존 `artifact` 타입 이벤트들을 새로운 타입 체계로 재분류
- [ ] Artifact 정보는 그대로 유지

### Step 6: E2E 테스트 재실행
- [ ] 새로운 타입 체계로 E2E 테스트 실행
- [ ] 결과 분석 및 검증

---

## 8. 장점

1. **타입의 의미가 명확해짐**: "무엇을 하는지"를 직접 표현
2. **Artifact 정보 유지**: 파일/코드 참조 가능
3. **Timeline에서 상세 확인 가능**: 타입별로 관련 artifact 확인
4. **확장성**: 새로운 타입 추가 시 artifact 연결 방식 일관성 유지

---

## 9. 참고 파일

- 현재 EventType 정의: `backend/core/models.py`
- 이벤트 정규화 로직: `backend/builders/event_normalizer.py`
- LLM 서비스: `backend/core/llm_service.py`
- 최신 E2E 결과: `tests/results/event_normalizer_e2e_llm_20251225_183334.json`
- 수동 검증 결과: `tests/manual_review/all_events_html_review_20251225_211525/manual_review_updated.json` (생성 예정)

---

## 10. 다음 세션 시작 가이드

1. **TODOs.md 확인**: Phase 3.4의 현재 진행 상황 파악
2. **이 문서 읽기**: 타입 체계 개선 계획 전체 이해
3. **최신 E2E 결과 확인**: `tests/results/event_normalizer_e2e_llm_20251225_183334.json`
4. **수동 검증 결과 확인**: `tests/manual_review/all_events_html_review_20251225_211525/manual_review_updated.json` (사용자 검증 완료 후)
5. **구현 시작**: Step 1부터 순차적으로 진행

---

**작성자**: AI Assistant  
**검토자**: 사용자  
**승인일**: 2025-12-25

```

```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 7단계: Phase 완료 작업
  - [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
  - [ ] Git commit 실행 (`feat: Phase 3.4 완료 - 이벤트 정규화 품질 개선`)
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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
      - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 7단계: 타입 체계 개선 구현 (다음 세션 시작)
  - [ ] **⚠️ 시작 전 필수**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 문서 읽기
  - [ ] Step 1: EventType Enum 수정 (`backend/core/models.py`)
  - [ ] Step 2: Artifact Action 타입 추가 (선택적)
  - [ ] Step 3: 분류 로직 개선 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
  - [ ] Step 4: LLM 프롬프트 수정 (`backend/core/llm_service.py`)
  - [ ] Step 5: 수동 검증 결과 재분류 (기존 `artifact` 타입 이벤트 재분류)
  - [ ] Step 6: E2E 테스트 재실행 및 검증

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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**현재 Phase**: Phase 3.4 진행 중 (이벤트 정규화 품질 개선)

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
      - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 7단계: 타입 체계 개선 구현 (다음 세션 시작)
  - [ ] **⚠️ 시작 전 필수**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 문서 읽기
  - [ ] Step 1: EventType Enum 수정 (`backend/core/models.py`)
  - [ ] Step 2: Artifact Action 타입 추가 (선택적)
  - [ ] Step 3: 분류 로직 개선 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
  - [ ] Step 4: LLM 프롬프트 수정 (`backend/core/llm_service.py`)
  - [ ] Step 5: 수동 검증 결과 재분류 (기존 `artifact` 타입 이벤트 재분류)
  - [ ] Step 6: E2E 테스트 재실행 및 검증

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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**마지막 업데이트**: 2025-12-23

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
- Phase 3.4: 이벤트 정규화 품질 개선 - 진행 중 (2025-12-23 시작)
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
      - [ ] 결과 확인: HTML 수동 검증 데이터셋 생성 및 검토 (진행 중)
      - [ ] 개선 전후 비교 분석 (HTML 검토 후 진행)
    - [ ] 7단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

```markdown
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

### Phase 3.4: 이벤트 정규화 품질 개선

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

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

- [ ] 7단계: 타입 체계 개선 구현 (다음 세션 시작)
  - [ ] **⚠️ 시작 전 필수**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 문서 읽기
  - [ ] Step 1: EventType Enum 수정 (`backend/core/models.py`)
  - [ ] Step 2: Artifact Action 타입 추가 (선택적)
  - [ ] Step 3: 분류 로직 개선 (`backend/builders/event_normalizer.py`, `backend/core/llm_service.py`)
  - [ ] Step 4: LLM 프롬프트 수정 (`backend/core/llm_service.py`)
  - [ ] Step 5: 수동 검증 결과 재분류 (기존 `artifact` 타입 이벤트 재분류)
  - [ ] Step 6: E2E 테스트 재실행 및 검증

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

### Phase 3 이벤트 정규화 품질 재평가 (Phase 4 완료 후)

**목표**: Phase 4의 Timeline/Issue Cards 생성 결과를 반영하여 Phase 3의 이벤트 정규화 품질을 재평가

- [ ] Timeline/Issue Cards 품질 분석
  - [ ] Timeline 이벤트의 적절성 검증 (이벤트 타입 분류가 Timeline 생성에 적합한지)
  - [ ] Issue Cards 탐지 정확도 검증 (DebugEvent 기반 이슈 탐지가 효과적인지)
  - [ ] 이벤트 Summary 품질이 Timeline/Issue Cards에 미치는 영향 분석
- [ ] 이벤트 정규화 품질 재평가
  - [ ] Phase 4 결과를 바탕으로 이벤트 정규화 품질 재검토
  - [ ] Timeline/Issue Cards 품질이 낮은 경우 이벤트 정규화 로직 개선 필요 여부 판단
  - [ ] 개선이 필요한 경우 Phase 3 이벤트 정규화 로직 수정
- [ ] Golden 파일 생성 (재평가 완료 후)
  - [ ] 재평가 결과가 양호한 경우 Golden 파일 생성
  - [ ] 수동 검증 데이터셋과 Phase 4 결과를 종합하여 최종 Golden 파일 작성
  - [ ] 회귀 테스트 기준으로 설정

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

**마지막 업데이트**: 2025-12-23

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
    - [ ] 7단계: 타입 체계 개선 구현 (다음 세션 시작)
      - [ ] **⚠️ 시작 전 필수**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 문서 읽기
      - [ ] Step 1-6 순차 진행 (상세 내용은 위 문서 참조)
    - [ ] 8단계: Phase 완료 작업 (TODOs.md 업데이트, Git commit)

**다음 단계**:
- Phase 3.4 진행 (이벤트 정규화 품질 개선)
  - ✅ 수동 검증 파일 재작성 (완료)
  - [ ] 수동 검증 결과 평가 (`evaluate_manual_review()` 실행)
  - [ ] 원인 분석 (with 사용자)
  - [ ] Type 추출 로직 수정
  - [ ] Summary 로직 수정
  - [ ] E2E 재평가
  - [ ] 결과 피드백
- Phase 3.4 완료 후 Phase 4 재진행 (Timeline 및 Issue Cards 생성 품질 재검증)


```

작업 완료.

## 완료된 작업

### 1. 타입 체계 개선 계획 문서 작성
- 파일: `docs/phase3_4_type_system_improvement.md`
- 내용:
  - 개선 배경 및 문제점
  - 새로운 타입 체계 설계
  - 프로젝트 Flow (개선된 버전)
  - E2E 결과 재해석 예시
  - 구현 계획 (Step 1-6)
  - 다음 세션 시작 가이드

### 2. TODOs.md 업데이트
- Phase 3.4의 6단계 완료 상태 반영
- 타입 체계 개선 계획 수립 완료 표시
- 7단계를 "타입 체계 개선 구현"으로 변경
- 8단계를 "Phase 완료 작업"으로 추가
- 다음 세션 시작 가이드 명시:
  - 시작 전 필수: `docs/phase3_4_type_system_improvement.md` 문서 읽기
  - Step 1-6 순차 진행

### 3. Git 커밋 완료
- 커밋 메시지: `docs: Phase 3.4 타입 체계 개선 계획 수립 및 TODOs.md 업데이트`
- 변경 파일:
  - `docs/phase3_4_type_system_improvement.md` (신규 생성)
  - `TODOs.md` (업데이트)

## 다음 세션 시작 가이드

1. TODOs.md 확인: Phase 3.4의 현재 진행 상황 파악
2. 개선 계획 문서 읽기: `docs/phase3_4_type_system_improvement.md` 전체 읽기
3. 최신 E2E 결과 확인: `tests/results/event_normalizer_e2e_llm_20251225_183334.json`
4. 구현 시작: Step 1부터 순차적으로 진행
   - Step 1: EventType Enum 수정
   - Step 2: Artifact Action 타입 추가 (선택적)
   - Step 3: 분류 로직 개선
   - Step 4: LLM 프롬프트 수정
   - Step 5: 수동 검증 결과 재분류
   - Step 6: E2E 테스트 재실행 및 검증

모든 내용이 문서화되어 다음 세션에서 바로 시작할 수 있습니다.

