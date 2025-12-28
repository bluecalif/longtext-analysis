# Longtext Analysis

> Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

## 프로젝트 개요

이 프로젝트는 Cursor IDE에서 export된 세션 대화 마크다운 파일을 입력으로 받아:
1. 프로젝트 단계별 진행 작업(Timeline)
2. 디버깅 이슈 히스토리(Issue Cards)
3. 코드 스니펫 분리 저장

을 구조화된 산출물(JSON/Markdown)로 생성합니다.

## 기술 스택

- **백엔드**: Python FastAPI (Poetry)
- **프론트엔드**: Next.js 14+ (App Router, TypeScript)
- **LLM**: OpenAI API (gpt-4.1-mini, 기본값 사용, 배치 처리 최적화)
- **저장**: 로컬 파일 기반 (JSON/MD)
- **배포**: 로컬 개발 환경

## 프로젝트 구조

```
longtext-analysis/
├── backend/                    # FastAPI 백엔드
│   ├── parser/                 # 마크다운 파서 모듈
│   │   ├── normalize.py        # 텍스트 정규화
│   │   ├── meta.py             # 세션 메타데이터 추출
│   │   ├── turns.py            # Turn 블록 파싱
│   │   ├── snippets.py         # 코드 스니펫 추출
│   │   └── artifacts.py        # Artifact 추출
│   ├── builders/               # Timeline/Issue Cards 빌더
│   ├── render/                 # Markdown 렌더러
│   ├── api/routes/             # FastAPI 라우터
│   ├── core/                   # 상수, 유틸리티, 모델
│   └── main.py                 # FastAPI 앱 진입점
├── frontend/                   # Next.js 프론트엔드
├── tests/                      # 테스트 파일
│   ├── fixtures/               # 테스트 입력 데이터
│   ├── golden/                 # 예상 결과 (Golden 파일)
│   ├── logs/                   # E2E 테스트 로그
│   ├── results/                # E2E 테스트 실행 결과
│   └── reports/                # 테스트 리포트
├── docs/                       # 문서
└── .cursor/rules/              # Cursor Rules
```

## 개발 환경 설정

### 필수 요구사항

- Python 3.11 이상
- Poetry 1.8.5 이상 (PEP 621 메타데이터 버전 2.4 지원)
- Node.js 18 이상 (프론트엔드용, Phase 8에서 사용)
- npm 또는 yarn (프론트엔드용)

### 설치 방법

1. Poetry 의존성 설치:
```powershell
poetry install
```

2. 프론트엔드 의존성 설치 (프론트엔드 디렉토리 생성 후):
```powershell
cd frontend
npm install
```

### 환경 변수 설정

`.env` 파일을 프로젝트 루트에 생성하세요:

```env
OPENAI_API_KEY=your-api-key-here
```

**주의**: `.env` 파일은 숨김 파일일 수 있으므로 `Get-ChildItem -Name "*.env*" -Force` 명령으로 확인하세요.

## 실행 방법

### 백엔드 서버 실행

```powershell
poetry run uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 프론트엔드 서버 실행 (Phase 8에서 구현 예정)

```powershell
cd frontend
npm run dev
```

**참고**: 현재 Phase 7 진행 중 (백엔드 API 구현). 프론트엔드는 Phase 8에서 구현됩니다.

## 참고 문서

- [PRD](docs/PRD_longtext.md)
- [TODOs](TODOs.md)
- [AGENTS.md](AGENTS.md)

## 파서 모듈

### 개요

파서는 Cursor IDE에서 export된 마크다운 파일을 구조화된 데이터로 변환합니다.

### 파싱 파이프라인

1. **텍스트 정규화** (`normalize.py`)
   - 줄바꿈 통일 (`\r\n` → `\n`)
   - BOM 제거
   - 공백 정리 (코드 블록 보존)

2. **세션 메타데이터 추출** (`meta.py`)
   - Phase, Subphase 추출
   - Exported at, Cursor version 추출
   - Session ID 생성

3. **Turn 블록 파싱** (`turns.py`)
   - 구분선(`---`) 또는 Speaker 라벨(`**User**`, `**Cursor**`) 기준 분할
   - Speaker 추출 (User/Cursor/Unknown)
   - Body 텍스트 추출 (코드 블록 제외)

4. **코드 스니펫 추출** (`snippets.py`)
   - 코드 펜스(```) 추출
   - 언어 판별
   - `turn_index`와 `block_index`로 고유 식별

5. **Artifact 추출** (`artifacts.py`)
   - 파일/경로 후보 추출
   - 파일 타입 분류 (md, py, ts, sql 등)

### 파싱 예시

```python
from backend.parser import parse_markdown

# 마크다운 파일 파싱
result = parse_markdown(text, source_doc="input.md")

# 결과 구조
{
    "session_meta": SessionMeta(
        session_id="cursor_export_2025-12-14_223636_KST",
        phase=6,
        subphase=7,
        ...
    ),
    "turns": [
        Turn(
            turn_index=0,
            speaker="User",
            body="...",
            code_blocks=[...],
            path_candidates=[...]
        ),
        ...
    ],
    "code_blocks": [...],  # 모든 Turn의 코드 블록 통합
    "artifacts": [...]     # 파일 경로 후보
}
```

### 테스트

```powershell
# 단위 테스트
poetry run pytest tests/test_parser.py -v

# E2E 테스트
poetry run pytest tests/test_parser_e2e.py -v
```

E2E 테스트는 자동으로 다음을 저장합니다:
- 로그 파일: `tests/logs/`
- 실행 결과: `tests/results/`
- 리포트: `tests/reports/`

## 이벤트 정규화 모듈

### 개요

이벤트 정규화 모듈은 파싱된 Turn 데이터를 이벤트로 변환하여 Timeline과 Issue Cards 생성을 위한 기반을 제공합니다.

### 이벤트 타입

- `status_review`: 상태 리뷰 이벤트
- `plan`: 계획 수립 이벤트
- `code_generation`: 코드 생성 이벤트
- `debug`: 디버깅 이벤트 (에러, 원인, 해결 등)
- `completion`: 완료 이벤트
- `next_step`: 다음 단계 이벤트
- `turn`: 일반 Turn 이벤트 (기본값)

**참고**: Phase 3.4에서 타입 체계 개선 완료 (`code_generation` 추가, `artifact` 제거)

### 이벤트 정규화 파이프라인

1. **Turn → Event 변환** (`event_normalizer.py`)
   - Turn 리스트를 Event 리스트로 변환 (1:1 매핑)
   - LLM 기반 타입 분류 및 요약 생성 (기본값)
   - 배치 처리로 최적화 (67개 Turn → 13-14개 배치)
   - 패턴 기반 fallback 지원

2. **이벤트 타입 분류**
   - LLM 기반 분류 (gpt-4.1-mini 사용, 기본값)
   - 키워드 기반 fallback (status_review, plan, completion 등)
   - Debug 트리거 패턴 매칭 (error, root_cause, fix, validation)
   - Code Generation 탐지 (코드 생성 활동)

### 사용 예시

```python
from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events

# 파싱 실행
result = parse_markdown(text, source_doc="input.md")

# 이벤트 정규화
events = normalize_turns_to_events(result["turns"])

# 결과 구조
[
    Event(
        type=EventType.DEBUG,
        turn_ref=5,
        summary="There was an error...",
        artifacts=[],
        snippet_refs=["turn_5_block_0"]
    ),
    Event(
        type=EventType.ARTIFACT,
        turn_ref=10,
        summary="Created new file...",
        artifacts=[{"path": "backend/main.py", "action": "mention"}],
        snippet_refs=[]
    ),
    ...
]
```

### 테스트

```powershell
# 단위 테스트
poetry run pytest tests/test_event_normalizer.py -v

# E2E 테스트
poetry run pytest tests/test_event_normalizer_e2e.py -v
```

## Timeline 및 Issue Cards 생성 모듈

### Timeline 생성 (`timeline_builder.py`)

**구조화된 Timeline 생성**:
- Phase/Subphase별 이벤트 그룹화
- 주요 작업 항목 추출 (LLM 기반, 기본값)
- Timeline Section 생성 (제목, 요약, 관련 이벤트, 이슈 연결 정보)

**출력**:
- `List[TimelineSection]` - 구조화된 섹션 리스트
- `List[TimelineEvent]` - 원본 이벤트 리스트 (하위 호환성)

### Issue Card 생성 (`issues_builder.py`)

**통합 컨텍스트 기반 생성** (Phase 4.7 개선):
- DEBUG 이벤트 클러스터링 (논리적 이슈 단위로 그룹화)
- Timeline Section 매칭
- LLM 기반 통합 추출 (`extract_issue_with_llm()`)
  - symptom, root_cause, fix, validation을 한 번에 추출
  - 일관성 있는 체인 생성

**출력**:
- `List[IssueCard]` - Issue Card 리스트 (Timeline Section과 연결)

### 핵심 개선 사항 (Phase 4.7)

**이전 문제점**:
- 각 컴포넌트 개별 추출 → Fix 항목 20개 생성
- 컨텍스트 부족으로 품질 낮음

**개선 후**:
- 통합 컨텍스트 기반 추출 → Fix 항목 1개 (클러스터당)
- TimelineSection + Events + Turns 통합 활용
- 품질 대폭 향상

### 테스트

```powershell
# E2E 테스트 (LLM 기반)
poetry run pytest tests/test_timeline_issues_e2e.py::test_timeline_issues_e2e_with_llm -v

# E2E 테스트 (패턴 기반)
poetry run pytest tests/test_timeline_issues_e2e.py::test_timeline_issues_e2e_pattern -v
```

## 코드 스니펫 관리 모듈 (Phase 5)

### 개요

코드 블록을 별도로 저장하고 Timeline/Issue Cards와 링킹합니다.

### 주요 기능

1. **스니펫 ID 생성**: `SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang}`
2. **중복 제거**: SHA-256 해시 기반
3. **언어 판별**: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash)
4. **링킹**: Event/IssueCard와 snippet_refs로 연결

### 테스트

```powershell
# E2E 테스트
poetry run pytest tests/test_snippet_e2e.py -v
```

**검증 결과**: 92개 코드 블록 → 81개 스니펫 (11개 중복 제거), 19개 이벤트 링킹, 1개 Issue Card 링킹

## LLM 최적화 (Phase 6)

### 이벤트 추출 최적화 (Phase 6.1)

**배치 처리 구현**:
- 개별 Turn 호출 (67번) → 배치 처리 (13-14번, 5개씩 묶음)
- 비용 절감: 약 80% (67번 → 13-14번 호출)
- 병렬 처리 유지 (5개 배치 동시 처리)

### 타임라인 구조화 최적화 (Phase 6.2)

**검증 로직 개선**:
- LLM 결과 검증 실패 문제 해결
- 누락된 이벤트 자동 포함 로직 구현
- LLM 결과 활용률: 0% → 100%

## 개발 가이드

프로젝트는 Phase별로 진행됩니다. 자세한 내용은 [TODOs.md](TODOs.md)를 참고하세요.

**현재 Phase**: Phase 6 완료, Phase 7 진행 준비 (백엔드 API 구현)

### 완료된 주요 Phase
- Phase 1-2: 프로젝트 초기 설정 및 파서 구현
- Phase 3: 이벤트 정규화 및 품질 개선
- Phase 4: Timeline 및 Issue Cards 생성 (구조화 개선 포함)
- Phase 5: 코드 스니펫 분리 및 저장
- Phase 6: LLM 호출 최적화 (배치 처리, 타임라인 구조화 최적화)

### 다음 Phase
- Phase 7: 백엔드 API 구현 (FastAPI 엔드포인트, Markdown 렌더러)

