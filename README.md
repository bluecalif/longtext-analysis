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
- **LLM**: OpenAI API (옵션, 요약/라벨링 보조)
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
- Poetry 1.8.5 이상
- Node.js 18 이상
- npm 또는 yarn

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

`.env.example` 파일을 참고하여 `.env` 파일을 생성하세요.

## 실행 방법

### 백엔드 서버 실행

```powershell
poetry run uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 프론트엔드 서버 실행

```powershell
cd frontend
npm run dev
```

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

## 개발 가이드

프로젝트는 Phase별로 진행됩니다. 자세한 내용은 [TODOs.md](TODOs.md)를 참고하세요.

**현재 Phase**: Phase 2 완료, Phase 3 준비 중

