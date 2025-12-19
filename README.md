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
├── backend/          # FastAPI 백엔드
├── frontend/         # Next.js 프론트엔드
├── tests/            # 테스트 파일
├── docs/             # 문서
└── .cursor/rules/    # Cursor Rules
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

## 개발 가이드

프로젝트는 Phase별로 진행됩니다. 자세한 내용은 [TODOs.md](TODOs.md)를 참고하세요.

**현재 Phase**: Phase 1 (프로젝트 초기 설정 및 환경 구성)

