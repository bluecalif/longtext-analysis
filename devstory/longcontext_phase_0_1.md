# Phase 0-1
_Exported on 12/29/2025 at 14:25:42 GMT+9 from Cursor (2.2.44)_

---

**User**

@TODOs.md 를 바탕으로 프로젝트의 현재 상황을 파악하세요

---

**Cursor**

프로젝트 구조를 확인해 현재 상황을 파악 중입니다.


프로젝트 현황 요약:

## 프로젝트 현재 상황 분석

### 완료된 항목

1. 문서 준비
   - `TODOs.md`: 8개 Phase로 구성된 프로젝트 계획
   - `docs/PRD_longtext.md`: 프로젝트 요구사항 정의
   - `docs/instruction_detail.md`, `docs/instruction_moredetail.md`: 상세 지침
   - `docs/cursor_phase_6_3.md`: E2E 테스트용 실제 입력 데이터
   - `AGENTS.md`: AI 에이전트 운영 가이드
   - `cursor-master-sequence.md`: 프로젝트 진행 순서
   - `api-contract-sync.mdc`: API 계약 동기화 규칙

### 미구현 항목 (Phase 1)

현재 Phase 1(프로젝트 초기 설정 및 환경 구성)이 시작 전 상태입니다.

#### 백엔드 설정
- [ ] Poetry 프로젝트 초기화 (`pyproject.toml`, `poetry.lock` 없음)
- [ ] 백엔드 의존성 패키지 설치
- [ ] 백엔드 디렉토리 구조 생성 (`backend/` 디렉토리 없음)

#### 프론트엔드 설정
- [ ] Next.js 프로젝트 초기화 (`frontend/` 디렉토리 없음)
- [ ] 프론트엔드 의존성 패키지 설치
- [ ] 프론트엔드 디렉토리 구조 생성

#### 프로젝트 공통 설정
- [ ] `tests/` 디렉토리 생성
- [ ] `.env` 파일 템플릿 생성
- [ ] `.env.example` 파일 생성
- [ ] `.gitignore` 설정
- [ ] `README.md` 작성
- [ ] Cursor Rules 초기 설정 (`.cursor/rules/` 디렉토리 없음)

### 프로젝트 개요

- 목적: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫 생성
- 기술 스택:
  - 백엔드: Python FastAPI (Poetry)
  - 프론트엔드: Next.js 14+ (App Router, TypeScript)
  - LLM: OpenAI API (옵션)
  - 저장: 로컬 파일 기반 (JSON/MD)

### 현재 상태 요약

```
✅ 문서 준비: 100% 완료
❌ 프로젝트 구조: 0% (Phase 1 시작 전)
❌ 코드 구현: 0% (Phase 2~8 시작 전)
```

### 다음 단계

Phase 1을 시작하면:
1. Poetry 프로젝트 초기화 및 백엔드 구조 생성
2. Next.js 프로젝트 초기화 및 프론트엔드 구조 생성
3. 테스트 디렉토리 및 기본 설정 파일 생성
4. Cursor Rules 설정

Phase 1을 시작할까요?

```plaintext
✅ 문서 준비: 100% 완료
❌ 프로젝트 구조: 0% (Phase 1 시작 전)
❌ 코드 구현: 0% (Phase 2~8 시작 전)
```

---

**User**

AGENTS.md에서 프로젝트의 규칙을 파악하여 준수하도록 하세요

---

**Cursor**

AGENTS.md의 규칙을 확인 중입니다.


AGENTS.md의 규칙을 확인했습니다. 핵심 규칙을 정리하고 현재 상황을 설명합니다.

## AGENTS.md 핵심 규칙 요약

### 1. Phase별 진행 원칙 (최우선)
- 절대 혼자서 전체 작업을 진행하지 않음
- Phase별로 사용자 피드백을 받아 진행
- 작업 전 사용자 확인 필수
- 작업 완료 후 피드백 대기

### 2. 사용자 설명 필수 원칙 (최우선)
- 모든 작업 전에 설명하고, 실행은 사용자 확인 후 진행
- 설명 형식: What(무엇을) → Why(왜) → How(어떻게) → Result & Action(예상 결과 및 대책)
- 실행 후 결과 해석 및 다음 단계 제시

### 3. PowerShell 명령어 표준
- 명령어 연결: 세미콜론(`;`) 사용 (Bash `&&` 금지)
- 모듈 실행: `python -m` 형식 사용
- 서버 실행: 프로젝트 루트에서 실행 (`cd` 사용 금지)
- 이모지 사용 금지: `[OK]`, `[PASS]`, `[FAIL]` 태그 사용
- 한글 파일명/문자열: 스크립트 파일로 작성 후 실행

### 4. 환경변수 파일 관리
- `.env` 파일 확인: `Get-ChildItem -Name "*.env*" -Force` 사용
- 숨김 파일 인식 문제 주의

### 5. Poetry 패키지 관리
- Poetry 1.8.5 이상 필수
- 버전 확인: `poetry --version`

### 6. Git 버전 관리 (필수)
- 작업 시작 전: `git status` → `git pull origin main`
- 작업 완료 후: `git add .` → `git commit -m "타입: 작업 내용"` → `git push origin main`

### 7. 테스트 환경 설정
- E2E 테스트: 실제 서버 실행 필수
- 테스트 후 자동 보고 필수

---

## 현재 프로젝트 상황

### 완료된 항목
- 문서 준비: 100% 완료
  - TODOs.md (8개 Phase 계획)
  - PRD 및 상세 지침 문서
  - AGENTS.md, cursor-master-sequence.md

### 미구현 항목 (Phase 1 시작 전)
- 백엔드: Poetry 프로젝트 미초기화, 디렉토리 구조 없음
- 프론트엔드: Next.js 프로젝트 미초기화, 디렉토리 구조 없음
- 공통 설정: tests/, .env, .gitignore, README.md, .cursor/rules/ 없음

---

## 다음 단계 제안

### Phase 1 시작 준비

작업 범위: 프로젝트 초기 설정 및 환경 구성

1. 백엔드 설정
   - Poetry 프로젝트 초기화 (`pyproject.toml`, `poetry.lock`)
   - 의존성 패키지 설치 (fastapi, uvicorn, pydantic, python-dotenv, openai, regex)
   - 백엔드 디렉토리 구조 생성

2. 프론트엔드 설정
   - Next.js 프로젝트 초기화 (`frontend/` 디렉토리)
   - 의존성 패키지 설치 (next, react, typescript, tailwindcss)
   - 프론트엔드 디렉토리 구조 생성

3. 프로젝트 공통 설정
   - `tests/` 디렉토리 생성
   - `.env.example` 파일 생성
   - `.gitignore` 설정
   - `README.md` 작성
   - Cursor Rules 초기 설정

예상 시간: 약 30-40분  
의존성: 없음 (프로젝트 시작 단계)

---

## 확인 사항

1. Poetry 버전 확인 필요 (1.8.5 이상)
2. Git 저장소 초기화 여부 확인
3. Node.js 설치 여부 확인 (Next.js용)

Phase 1을 시작할까요? 시작 전에 위 확인 사항을 점검하겠습니다.

---

**User**

/gen-proj-rules PRD와 TODOs.md를 바탕으로 커서룰 작성해주세요

--- Cursor Command: gen-proj-rules.md ---
# Generate Project Rules

Create project-specific rules based on user requirements and project context.

## Instructions

### 1. Understand User Request
- Clarify what aspect of the project needs rules (domain, workflow, architecture, style)
- Ask for specific examples or scenarios if needed
- Identify the scope: single feature, domain area, or project-wide standards

### 2. Analyze Project Context
- Review key project files:
  - `README.md` - Project overview and goals
  - `TODOs.md` or similar - Current development plan
  - `package.json` or `pyproject.toml` - Tech stack and dependencies
  - Core source files in main directories (e.g., `src/`, `backend/`, `frontend/`)
- Identify:
  - Technology stack (frameworks, languages, tools)
  - Architecture patterns (MVC, microservices, monorepo, etc.)
  - Existing conventions (naming, file structure, testing)
  - Domain concepts and business logic

### 3. Create Rule Files
- Create `.cursor/rules/` directory if it doesn't exist
- Generate `.mdc` files with descriptive names
- **One file per domain/feature area** (e.g., `api-design.mdc`, `database-schema.mdc`, `frontend-components.mdc`)

### 4. Structure Each Rule File

```markdown
---
alwaysApply: true  # or false for optional rules
description: Brief description of what this rule covers
---

# [Rule Title]

## Overview
Brief explanation of the domain/feature and why these rules exist.

## Domain Knowledge
- Key concepts and terminology
- Business logic patterns
- Data models and relationships
- Common workflows

## Standards & Conventions
- Code structure and organization
- Naming conventions
- File/folder patterns
- Import/export patterns

## Implementation Patterns
- Common code patterns and templates
- Reusable components or utilities
- Error handling approaches
- Testing strategies

## Examples
```[language]
// Concrete code examples demonstrating the rules
```

## Checklist
- [ ] Key validation points
- [ ] Common pitfalls to avoid
- [ ] Required dependencies or setup

## References
- Links to relevant documentation
- Related rule files
```

### 5. Rule Categories

**Domain Knowledge Systematization**
- Business logic and domain models
- Data schemas and relationships
- API contracts and interfaces
- Key algorithms or calculations

**Workflow & Template Automation**
- Feature development workflow (e.g., "Adding a new API endpoint")
- Code generation templates
- Testing patterns (unit, integration, e2e)
- Deployment and release process

**Style & Architecture Standardization**
- Code style and formatting
- Architecture decisions (state management, data flow, etc.)
- Component/module organization
- Performance best practices
- Security guidelines

### 6. File Naming Convention
- Use kebab-case: `feature-name.mdc`
- Be specific: `api-authentication.mdc` not `auth.mdc`
- Group related rules: `backend-api-design.mdc`, `backend-error-handling.mdc`

### 7. Quality Checklist
Before finalizing the rule file:
- [ ] Is the rule actionable and specific?
- [ ] Does it include concrete examples?
- [ ] Is it relevant to the current project tech stack?
- [ ] Does it avoid redundancy with existing rules?
- [ ] Is the language clear and concise?
- [ ] Are there practical code snippets?

### 8. Example Output

For a request like "Create rules for adding new API endpoints", generate:

**File**: `.cursor/rules/backend-api-endpoints.mdc`

```markdown
---
alwaysApply: true
description: Standards for creating new API endpoints in FastAPI backend
---

# Backend API Endpoints

## Overview
Guidelines for implementing RESTful API endpoints in the FastAPI backend...

[Continue with full structure...]
```

## Notes
- Keep rules focused and scoped to specific areas
- Update existing rule files rather than creating duplicates
- Reference related rules using relative paths
- Include real code from the project as examples when possible
- Make rules prescriptive but flexible for edge cases

--- End Command ---

---

**Cursor**

PRD와 TODOs.md를 검토해 프로젝트 컨텍스트를 파악한 뒤, Cursor Rules를 작성합니다.


PRD와 TODOs.md를 검토했습니다. 프로젝트 컨텍스트를 바탕으로 Cursor Rules를 작성합니다.


프로젝트 특성에 맞는 Cursor Rules 파일을 생성 중입니다.


```markdown
---
alwaysApply: true
description: FastAPI 백엔드 API 설계 및 구현 규칙
---

# Backend API Design

## Overview
FastAPI 기반 백엔드 API 설계 규칙. RESTful 원칙을 따르며, Pydantic 모델을 통한 타입 안정성과 API 계약 동기화를 보장합니다.

## Domain Knowledge

### 핵심 엔드포인트
- `POST /api/parse` - 마크다운 파일 업로드 및 파싱
- `POST /api/timeline` - Timeline 생성
- `POST /api/issues` - Issue Cards 생성
- `GET /api/snippets/{snippet_id}` - 스니펫 조회
- `POST /api/snippets/export` - 스니펫 ZIP 다운로드
- `POST /api/export/timeline` - Timeline JSON/MD 다운로드
- `POST /api/export/issues` - Issues JSON/MD 다운로드
- `POST /api/export/all` - 전체 산출물 ZIP 다운로드

### 데이터 모델 계층
1. **Parser Layer**: `Turn`, `CodeBlock`, `Artifact` (파싱 결과)
2. **Event Layer**: `MessageEvent`, `ArtifactEvent`, `DebugEvent` (정규화된 이벤트)
3. **Output Layer**: `TimelineEvent`, `IssueCard`, `Snippet` (최종 산출물)

## Standards & Conventions

### 1. 파일 구조
```
backend/
├── api/
│   └── routes/
│       ├── parse.py
│       ├── timeline.py
│       ├── issues.py
│       ├── snippets.py
│       └── export.py
├── parser/          # 파싱 모듈
├── builders/        # Timeline/Issue Cards 빌더
├── render/          # Markdown 렌더러
├── core/
│   ├── models.py    # Pydantic 모델
│   └── constants.py # 상수 정의
└── main.py
```

### 2. Pydantic 모델 정의 규칙

**원칙**: 모든 API 요청/응답은 Pydantic 모델로 정의

```python
# backend/core/models.py
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class EventType(str, Enum):
    STATUS_REVIEW = "status_review"
    PLAN = "plan"
    ARTIFACT = "artifact"
    DEBUG = "debug"
    COMPLETION = "completion"
    NEXT_STEP = "next_step"
    TURN = "turn"

class SessionMeta(BaseModel):
    session_id: str
    exported_at: Optional[str] = None
    cursor_version: Optional[str] = None
    phase: Optional[int] = None
    subphase: Optional[int] = None
    source_doc: str

class TimelineEvent(BaseModel):
    seq: int
    session_id: str
    phase: Optional[int] = None
    subphase: Optional[int] = None
    type: EventType
    summary: str
    artifacts: List[dict] = []
    snippet_refs: List[str] = []

class IssueCard(BaseModel):
    issue_id: str
    scope: dict
    title: str
    symptoms: List[str]
    root_cause: Optional[dict] = None
    evidence: List[dict] = []
    fix: List[dict] = []
    validation: List[str] = []
    related_artifacts: List[dict] = []
    snippet_refs: List[str] = []
```

### 3. API 라우터 구현 패턴

```python
# backend/api/routes/parse.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.core.models import SessionMeta, Turn
from backend.parser import parse_markdown

router = APIRouter(prefix="/api/parse", tags=["parse"])

@router.post("", response_model=dict)
async def parse_file(file: UploadFile = File(...)):
    """
    마크다운 파일을 업로드하고 파싱합니다.
    
    Returns:
        {
            "session_meta": SessionMeta,
            "turns": List[Turn],
            "events": List[Event]
        }
    """
    if not file.filename.endswith('.md'):
        raise HTTPException(status_code=400, detail="Only .md files are supported")
    
    content = await file.read()
    text = content.decode('utf-8')
    
    # 파싱 실행
    result = parse_markdown(text)
    
    return {
        "session_meta": result.session_meta,
        "turns": result.turns,
        "events": result.events
    }
```

### 4. 에러 처리 규칙

```python
from fastapi import HTTPException
from fastapi.responses import JSONResponse

# 커스텀 예외 클래스
class ParseError(Exception):
    pass

# 예외 핸들러
@app.exception_handler(ParseError)
async def parse_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": f"Parse error: {str(exc)}"}
    )

# 사용 예시
try:
    result = parse_markdown(text)
except ParseError as e:
    raise HTTPException(status_code=400, detail=str(e))
```

### 5. 파일 업로드 처리

```python
from fastapi import UploadFile, File
import aiofiles

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # 파일 크기 제한 (예: 10MB)
    MAX_SIZE = 10 * 1024 * 1024
    
    content = await file.read()
    if len(content) > MAX_SIZE:
        raise HTTPException(status_code=413, detail="File too large")
    
    # UTF-8 디코딩
    try:
        text = content.decode('utf-8')
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Invalid UTF-8 encoding")
    
    return {"filename": file.filename, "size": len(content)}
```

## Implementation Patterns

### Pattern 1: 의존성 주입 (Dependency Injection)

```python
# backend/core/dependencies.py
from fastapi import Depends

def get_llm_service():
    from backend.core.llm_service import LLMService
    return LLMService()

# 사용
@router.post("/timeline")
async def create_timeline(
    events: List[Event],
    llm_service: LLMService = Depends(get_llm_service)
):
    # LLM 서비스 사용
    pass
```

### Pattern 2: 캐싱 전략

```python
# backend/core/cache.py
from functools import lru_cache
import hashlib
import json

def cache_key(*args, **kwargs):
    """캐시 키 생성"""
    data = json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True)
    return hashlib.sha256(data.encode()).hexdigest()

# 파일 기반 캐시 (LLM 호출 결과)
def get_cached_result(key: str):
    cache_file = f"cache/{key}.json"
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_cached_result(key: str, result: dict):
    os.makedirs("cache", exist_ok=True)
    cache_file = f"cache/{key}.json"
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
```

### Pattern 3: 백그라운드 작업 처리

```python
# 백그라운드 작업은 FastAPI BackgroundTasks 사용
from fastapi import BackgroundTasks

@router.post("/parse")
async def parse_file(
    file: UploadFile,
    background_tasks: BackgroundTasks
):
    result = parse_markdown(text)
    
    # 백그라운드에서 스니펫 저장
    background_tasks.add_task(save_snippets, result.snippets)
    
    return result
```

## Examples

### 완전한 API 엔드포인트 예시

```python
# backend/api/routes/timeline.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from backend.core.models import TimelineEvent, SessionMeta
from backend.builders.timeline_builder import build_timeline

router = APIRouter(prefix="/api/timeline", tags=["timeline"])

@router.post("", response_model=dict)
async def create_timeline(
    session_id: str,
    events: List[dict],
    session_meta: SessionMeta
):
    """
    이벤트 리스트로부터 Timeline을 생성합니다.
    
    Args:
        session_id: 세션 ID
        events: 정규화된 이벤트 리스트
        session_meta: 세션 메타데이터
    
    Returns:
        {
            "session_meta": SessionMeta,
            "timeline": List[TimelineEvent]
        }
    """
    try:
        timeline = build_timeline(
            session_id=session_id,
            events=events,
            session_meta=session_meta
        )
        
        return {
            "session_meta": session_meta,
            "timeline": timeline
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to build timeline: {str(e)}"
        )
```

## Checklist

### 새 API 엔드포인트 추가 시
- [ ] Pydantic 모델로 요청/응답 스키마 정의
- [ ] `response_model` 파라미터 지정
- [ ] 에러 처리 (HTTPException 사용)
- [ ] API 문서 (docstring 작성)
- [ ] 프론트엔드 타입 정의와 동기화 확인 (api-contract-sync.mdc 참조)

### 파일 업로드 처리 시
- [ ] 파일 크기 제한 검증
- [ ] 인코딩 검증 (UTF-8)
- [ ] 파일 확장자 검증
- [ ] 에러 메시지 명확성

### 캐싱 적용 시
- [ ] 캐시 키 생성 규칙 명확화
- [ ] 파일 기반 캐시 사용 (LLM 호출 결과)
- [ ] 캐시 무효화 전략 수립

## References
- API Contract Sync: `.cursor/rules/api-contract-sync.mdc`
- Parser Rules: `.cursor/rules/parser-rules.mdc`
- Constants: `backend/core/constants.py`
- Models: `backend/core/models.py`

```

```markdown
---
alwaysApply: true
description: 마크다운 파서 구현 규칙 및 정규식 패턴
---

# Parser Rules

## Overview
Cursor IDE export 마크다운 파일을 구조화된 데이터로 파싱하는 규칙. 포맷 변화에 견딜 수 있도록 규칙 기반 + fallback 전략을 사용합니다.

## Domain Knowledge

### 파싱 파이프라인
1. **Normalize** - 텍스트 정규화 (줄바꿈, BOM, 공백)
2. **Meta Extraction** - 세션 메타 추출 (phase, subphase, exported_at, cursor_version)
3. **Turn Parsing** - Turn 블록 분할 및 파싱
4. **Snippet Extraction** - 코드 블록 추출
5. **Artifact Extraction** - 파일/경로 후보 추출

### 입력 포맷 가정
- 문서 상단: 메타 텍스트 (Phase/Exported at/Cursor version 등) - 없을 수도 있음
- Turn 블록: `---` 구분선 또는 `**User**`/`**Cursor**` 라벨 기준
- 코드 블록: ```lang ... ``` 펜스 (lang 누락 가능)
- 파일/경로: 자연어 문장 중간에 등장

## Standards & Conventions

### 1. 파일 구조
```
backend/parser/
├── normalize.py    # 텍스트 정규화
├── meta.py         # 세션 메타 추출
├── turns.py        # Turn 분할/파싱
├── snippets.py     # 코드 블록 추출
└── artifacts.py    # 파일/경로 추출
```

### 2. Normalize 규칙

```python
# backend/parser/normalize.py
import re

def normalize_text(text: str, preserve_code_blocks: bool = True) -> str:
    """
    텍스트 정규화
    
    Args:
        text: 원본 텍스트
        preserve_code_blocks: 코드 블록 내부 보존 여부
    
    Returns:
        정규화된 텍스트
    """
    # 1. 줄바꿈 통일
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # 2. BOM 제거
    text = text.lstrip('\ufeff')
    
    if preserve_code_blocks:
        # 코드 블록 분리
        code_blocks = []
        pattern = r'```([a-zA-Z0-9_+-]+)?\n(.*?)```'
        
        def replace_code(match):
            idx = len(code_blocks)
            code_blocks.append(match.group(0))
            return f'__CODE_BLOCK_{idx}__'
        
        text = re.sub(pattern, replace_code, text, flags=re.DOTALL)
    
    # 3. 트레일링 공백 제거
    text = re.sub(r'[ \t]+$', '', text, flags=re.MULTILINE)
    
    # 4. 너무 긴 공백 축소 (3개 이상 → 2개)
    text = re.sub(r' {3,}', '  ', text)
    
    if preserve_code_blocks:
        # 코드 블록 복원
        for idx, code in enumerate(code_blocks):
            text = text.replace(f'__CODE_BLOCK_{idx}__', code)
    
    return text
```

### 3. Session Meta 추출 규칙

```python
# backend/parser/meta.py
import re
from typing import Optional
from backend.core.models import SessionMeta

# 정규식 패턴
EXPORTED_AT_RE = re.compile(
    r'(?i)Exported\s+(\d{4}-\d{2}-\d{2}[^,\n]*?(?:KST|UTC|GMT|[+\-]\d{2}:\d{2})?)',
    re.MULTILINE
)

CURSOR_VERSION_RE = re.compile(
    r'(?i)\bCursor\s+(\d+\.\d+\.\d+)\b',
    re.MULTILINE
)

PHASE_RE = re.compile(
    r'(?i)\bPhase\s+(\d+)\b',
    re.MULTILINE
)

SUBPHASE_RE = re.compile(
    r'(?i)\bSub\s*Phase\s+(\d+)\b',
    re.MULTILINE
)

def extract_session_meta(text: str, source_doc: str) -> SessionMeta:
    """
    상단 2000~4000 chars 범위에서 best-effort로 메타 추출
    
    Args:
        text: 원본 텍스트
        source_doc: 소스 문서 경로
    
    Returns:
        SessionMeta 객체
    """
    # 상단 범위 추출
    header_text = text[:4000]
    
    # exported_at 추출
    exported_at_match = EXPORTED_AT_RE.search(header_text)
    exported_at = exported_at_match.group(1) if exported_at_match else None
    
    # cursor_version 추출
    version_match = CURSOR_VERSION_RE.search(header_text)
    cursor_version = version_match.group(1) if version_match else None
    
    # phase 추출
    phase_match = PHASE_RE.search(header_text)
    phase = int(phase_match.group(1)) if phase_match else None
    
    # subphase 추출
    subphase_match = SUBPHASE_RE.search(header_text)
    subphase = int(subphase_match.group(1)) if subphase_match else None
    
    # session_id 생성
    if exported_at:
        # 문자열 정규화: 공백 → _, : 제거
        session_id_base = exported_at.replace(' ', '_').replace(':', '')
        session_id = f"cursor_export_{session_id_base}"
    else:
        session_id = f"cursor_export_unknown_{hash(text) % 10000}"
    
    return SessionMeta(
        session_id=session_id,
        exported_at=exported_at,
        cursor_version=cursor_version,
        phase=phase,
        subphase=subphase,
        source_doc=source_doc
    )
```

### 4. Turn 분할 규칙

```python
# backend/parser/turns.py
import re
from typing import List
from backend.core.models import Turn

# 구분선 패턴
TURN_SPLIT_RE = re.compile(r'^\s*---\s*$', re.MULTILINE)

# Speaker 라벨 패턴
SPEAKER_RE = re.compile(
    r'^\s*\*\*(User|Cursor)\*\*\s*:?\s*$',
    re.MULTILINE
)

# Fallback: 굵게 누락된 경우
SPEAKER_FALLBACK_RE = re.compile(
    r'^\s*(User|Cursor)\s*:?\s*$',
    re.MULTILINE
)

def split_to_turns(text: str) -> List[str]:
    """
    구분선 기준으로 Turn 블록 분할
    
    Args:
        text: 정규화된 텍스트
    
    Returns:
        Turn 블록 리스트
    """
    # 1차: 구분선 기준 분할
    blocks = TURN_SPLIT_RE.split(text)
    blocks = [b.strip() for b in blocks if b.strip()]
    
    # 구분선이 없거나 너무 적으면 fallback
    if len(blocks) < 2:
        return fallback_split_by_speaker(text)
    
    return blocks

def fallback_split_by_speaker(text: str) -> List[str]:
    """
    Speaker 라벨 기준으로 분할 (fallback)
    """
    turns = []
    current_turn = []
    current_speaker = None
    
    for line in text.split('\n'):
        speaker_match = SPEAKER_RE.match(line) or SPEAKER_FALLBACK_RE.match(line)
        
        if speaker_match:
            # 새 Turn 시작
            if current_turn:
                turns.append('\n'.join(current_turn))
            current_speaker = speaker_match.group(1)
            current_turn = [line]
        else:
            current_turn.append(line)
    
    if current_turn:
        turns.append('\n'.join(current_turn))
    
    return turns

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
    body = re.sub(r'```.*?```', '', block, flags=re.DOTALL)
    body = re.sub(r'^\s*\*\*(User|Cursor)\*\*\s*:?\s*', '', body, flags=re.MULTILINE)
    body = body.strip()
    
    # 코드 블록 추출 (별도 함수로)
    from backend.parser.snippets import extract_code_blocks
    code_blocks = extract_code_blocks(block)
    
    # 파일 경로 후보 추출 (별도 함수로)
    from backend.parser.artifacts import extract_path_candidates
    path_candidates = extract_path_candidates(block)
    
    return Turn(
        turn_index=turn_index,
        speaker=speaker,
        body=body,
        code_blocks=code_blocks,
        path_candidates=path_candidates
    )
```

### 5. 코드 블록 추출 규칙

```python
# backend/parser/snippets.py
import re
from typing import List, Optional
from backend.core.models import CodeBlock

CODE_FENCE_RE = re.compile(
    r'```([a-zA-Z0-9_+-]+)?\n(.*?)```',
    re.DOTALL
)

def extract_code_blocks(text: str) -> List[CodeBlock]:
    """
    코드 펜스 추출
    
    Args:
        text: 텍스트
    
    Returns:
        CodeBlock 리스트
    """
    blocks = []
    matches = CODE_FENCE_RE.finditer(text)
    
    for idx, match in enumerate(matches):
        lang = (match.group(1) or "").lower()
        code = match.group(2)
        
        blocks.append(CodeBlock(
            block_index=idx,
            lang=lang,
            code=code
        ))
    
    return blocks
```

### 6. 파일/경로 추출 규칙

```python
# backend/parser/artifacts.py
import re
from typing import List

# 파일 경로 패턴 (보수적)
PATH_RE = re.compile(
    r'(?:(?:[\w.-]+[/\\])+[\w.-]+\.(?:md|mdc|py|ts|tsx|sql|json)|'
    r'TODOs\.md|[\w.-]+\.(?:md|mdc|py|ts|tsx|sql|json))',
    re.IGNORECASE
)

def extract_path_candidates(text: str) -> List[str]:
    """
    파일/경로 후보 추출
    
    Args:
        text: 텍스트
    
    Returns:
        경로 후보 리스트 (중복 제거)
    """
    matches = PATH_RE.findall(text)
    # 중복 제거 및 정규화
    candidates = list(set(matches))
    return candidates
```

## Implementation Patterns

### Pattern 1: Parse Health Check

```python
def check_parse_health(turns: List[Turn]) -> dict:
    """
    파싱 품질 검사
    
    Returns:
        {
            "unknown_ratio": float,
            "warnings": List[str]
        }
    """
    total = len(turns)
    unknown_count = sum(1 for t in turns if t.speaker == "Unknown")
    unknown_ratio = unknown_count / total if total > 0 else 0.0
    
    warnings = []
    if unknown_ratio > 0.2:
        warnings.append(
            f"High Unknown speaker ratio: {unknown_ratio:.1%}. "
            "Format detection may have failed."
        )
    
    return {
        "unknown_ratio": unknown_ratio,
        "warnings": warnings
    }
```

### Pattern 2: Fallback 파서 체인

```python
def parse_with_fallback(text: str) -> dict:
    """
    규칙 기반 파싱 → Fallback 파서 체인
    """
    # 1차: 규칙 기반 파싱
    try:
        result = parse_markdown(text)
        health = check_parse_health(result.turns)
        
        if health["unknown_ratio"] < 0.2:
            return result
    except Exception as e:
        pass
    
    # 2차: Fallback 파서
    result = fallback_parse(text)
    return result
```

## Examples

### 완전한 파서 예시

```python
# backend/parser/__init__.py
from backend.parser.normalize import normalize_text
from backend.parser.meta import extract_session_meta
from backend.parser.turns import split_to_turns, parse_turn

def parse_markdown(text: str, source_doc: str = "input.md") -> dict:
    """
    마크다운 파일 전체 파싱
    
    Returns:
        {
            "session_meta": SessionMeta,
            "turns": List[Turn],
            "code_blocks": List[CodeBlock],
            "artifacts": List[Artifact]
        }
    """
    # 1. 정규화
    normalized = normalize_text(text)
    
    # 2. 메타 추출
    session_meta = extract_session_meta(normalized, source_doc)
    
    # 3. Turn 분할
    turn_blocks = split_to_turns(normalized)
    
    # 4. Turn 파싱
    turns = []
    for idx, block in enumerate(turn_blocks):
        turn = parse_turn(block, idx)
        turns.append(turn)
    
    # 5. 코드 블록 수집
    from backend.parser.snippets import extract_code_blocks
    all_code_blocks = []
    for turn in turns:
        all_code_blocks.extend(turn.code_blocks)
    
    # 6. Artifact 수집
    from backend.parser.artifacts import extract_path_candidates
    all_paths = []
    for turn in turns:
        all_paths.extend(turn.path_candidates)
    
    return {
        "session_meta": session_meta,
        "turns": turns,
        "code_blocks": all_code_blocks,
        "artifacts": list(set(all_paths))
    }
```

## Checklist

### 파서 구현 시
- [ ] 정규식 패턴이 포맷 변형에 견디는지 확인
- [ ] Fallback 파서 구현
- [ ] Parse Health Check 구현
- [ ] 코드 블록 내부 보존 로직 확인
- [ ] 한글 파일명/경로 처리 확인

### 테스트 케이스 준비
- [ ] 정상 케이스 (구분선 + speaker + 코드펜스)
- [ ] 구분선 없음 (speaker 라벨만)
- [ ] Speaker 라벨 변형
- [ ] 코드펜스 lang 누락
- [ ] 파일 경로가 괄호/백틱 안에 존재

## References
- 상세 지침: `docs/instruction_detail.md`
- 구체화 지침: `docs/instruction_moredetail.md`
- 테스트: `tests/test_parser.py`

```

```markdown
---
alwaysApply: true
description: 이벤트 정규화 및 Timeline/Issue Cards 빌더 규칙
---

# Event Normalization & Builders

## Overview
파싱된 Turn 데이터를 이벤트로 정규화하고, Timeline과 Issue Cards를 생성하는 규칙. 링킹(연결) 로직을 통해 재사용 가능한 작업 지식을 구성합니다.

## Domain Knowledge

### 이벤트 타입 (MVP 고정)
- `status_review` - 상태 리뷰
- `plan` - 계획 수립
- `artifact` - 파일 생성/수정/실행
- `debug` - 디버깅 이벤트
- `completion` - 완료 요약
- `next_step` - 다음 단계
- `turn` - 일반 Turn (fallback)

### Issue Card 구조
- **symptom** (주로 User 발화) - 증상
- **root_cause** (주로 Cursor 발화) - 원인 (confirmed/hypothesis)
- **fix** - 조치 방법
- **validation** - 검증 방법
- **related_artifacts** - 관련 파일
- **snippet_refs** - 관련 코드 스니펫

### 링킹 원칙
- **근접성 우선**: 슬라이딩 윈도우(최근 6~10 turns) 내에서 연결
- **키워드 트리거**: error, 원인, 해결, 조치, 검증 등
- **산출물 연결**: 파일 경로/코드 블록이 있으면 ArtifactEvent로 변환 후 연결

## Standards & Conventions

### 1. 파일 구조
```
backend/builders/
├── event_normalizer.py  # Turn → Event 변환
├── timeline_builder.py  # Timeline 생성
└── issues_builder.py    # Issue Cards 생성
```

### 2. 이벤트 정규화 규칙

```python
# backend/builders/event_normalizer.py
from typing import List
from backend.core.models import Turn, Event, EventType

# Debug 트리거 패턴
DEBUG_TRIGGERS = {
    "error": re.compile(
        r'(?i)\b(error|exception|stack trace|violates check constraint|constraint)\b'
    ),
    "root_cause": re.compile(
        r'(?i)\b(원인|Root cause|because|due to)\b'
    ),
    "fix": re.compile(
        r'(?i)\b(해결|조치|수정|patch|fix|ALTER TABLE|UPDATE|script)\b'
    ),
    "validation": re.compile(
        r'(?i)\b(검증|확인|테스트|scenario|check)\b'
    )
}

def normalize_turns_to_events(turns: List[Turn]) -> List[Event]:
    """
    Turn 리스트를 Event 리스트로 변환
    
    Args:
        turns: 파싱된 Turn 리스트
    
    Returns:
        정규화된 Event 리스트
    """
    events = []
    
    for turn in turns:
        # 1. ArtifactEvent 체크 (파일 경로가 있으면)
        if turn.path_candidates:
            events.append(create_artifact_event(turn))
        
        # 2. DebugEvent 체크 (디버그 트리거가 있으면)
        if is_debug_turn(turn):
            events.append(create_debug_event(turn))
        
        # 3. 일반 MessageEvent
        events.append(create_message_event(turn))
    
    return events

def is_debug_turn(turn: Turn) -> bool:
    """디버그 Turn인지 판단"""
    if turn.speaker != "Cursor":
        return False
    
    text = turn.body.lower()
    return any(
        trigger.search(text) 
        for trigger in DEBUG_TRIGGERS.values()
    )

def create_debug_event(turn: Turn) -> Event:
    """DebugEvent 생성"""
    return Event(
        type=EventType.DEBUG,
        turn_ref=turn.turn_index,
        summary=summarize_turn(turn),
        artifacts=[],  # 후속 단계에서 연결
        snippet_refs=[block.block_index for block in turn.code_blocks]
    )
```

### 3. Timeline 빌더 규칙

```python
# backend/builders/timeline_builder.py
from typing import List
from backend.core.models import Event, TimelineEvent, SessionMeta

def build_timeline(
    session_id: str,
    events: List[Event],
    session_meta: SessionMeta
) -> List[TimelineEvent]:
    """
    이벤트 리스트로부터 Timeline 생성
    
    Args:
        session_id: 세션 ID
        events: 정규화된 이벤트 리스트
        session_meta: 세션 메타데이터
    
    Returns:
        TimelineEvent 리스트
    """
    timeline = []
    
    for seq, event in enumerate(events, start=1):
        timeline_event = TimelineEvent(
            seq=seq,
            session_id=session_id,
            phase=session_meta.phase,
            subphase=session_meta.subphase,
            type=event.type,
            summary=event.summary,
            artifacts=event.artifacts,
            snippet_refs=event.snippet_refs
        )
        timeline.append(timeline_event)
    
    return timeline
```

### 4. Issue Cards 빌더 규칙

```python
# backend/builders/issues_builder.py
from typing import List, Optional
from backend.core.models import Event, IssueCard, Turn

# 슬라이딩 윈도우 크기
WINDOW_SIZE = 10

def build_issue_cards(
    turns: List[Turn],
    events: List[Event]
) -> List[IssueCard]:
    """
    Turn과 Event로부터 Issue Cards 생성
    
    Args:
        turns: Turn 리스트
        events: Event 리스트
    
    Returns:
        IssueCard 리스트
    """
    issue_cards = []
    
    # 1. Seed 탐지 (User symptom)
    seeds = find_symptom_seeds(turns)
    
    for seed_idx, seed_turn in seeds:
        # 2. 슬라이딩 윈도우 내에서 연결 후보 탐색
        window_turns = turns[seed_idx:seed_idx + WINDOW_SIZE]
        window_events = [
            e for e in events 
            if seed_idx <= e.turn_ref < seed_idx + WINDOW_SIZE
        ]
        
        # 3. Issue Card 구성
        issue_card = build_issue_card_from_window(
            seed_turn=seed_turn,
            window_turns=window_turns,
            window_events=window_events,
            seed_idx=seed_idx
        )
        
        if issue_card:
            issue_cards.append(issue_card)
    
    return issue_cards

def find_symptom_seeds(turns: List[Turn]) -> List[tuple]:
    """
    User Turn에서 symptom 후보 탐지
    
    Returns:
        [(turn_index, Turn), ...]
    """
    seeds = []
    symptom_pattern = re.compile(
        r'(?i)\b(없|안 보|에러|문제|왜|%\s*증가|%\s*감소)\b'
    )
    
    for idx, turn in enumerate(turns):
        if turn.speaker == "User" and symptom_pattern.search(turn.body):
            seeds.append((idx, turn))
    
    return seeds

def build_issue_card_from_window(
    seed_turn: Turn,
    window_turns: List[Turn],
    window_events: List[Event],
    seed_idx: int
) -> Optional[IssueCard]:
    """
    슬라이딩 윈도우 내에서 Issue Card 구성
    """
    # Symptom 추출
    symptoms = [seed_turn.body]
    
    # Root cause 추출 (Cursor turns에서)
    root_cause = None
    for turn in window_turns:
        if turn.speaker == "Cursor":
            if DEBUG_TRIGGERS["root_cause"].search(turn.body):
                root_cause = {
                    "status": "confirmed",  # 또는 "hypothesis"
                    "text": extract_root_cause_text(turn.body)
                }
                break
    
    # Fix 추출
    fixes = []
    for event in window_events:
        if event.type == EventType.DEBUG and event.snippet_refs:
            fixes.append({
                "summary": event.summary,
                "snippet_refs": event.snippet_refs
            })
    
    # Validation 추출
    validations = []
    for turn in window_turns:
        if DEBUG_TRIGGERS["validation"].search(turn.body):
            validations.append(extract_validation_text(turn.body))
    
    # Root cause 또는 Fix 중 하나라도 있어야 카드 생성
    if not root_cause and not fixes:
        return None
    
    # Issue ID 생성
    issue_id = f"ISS-{seed_idx:03d}-{hash(seed_turn.body) % 10000}"
    
    return IssueCard(
        issue_id=issue_id,
        scope={
            "session_id": "current",  # 실제로는 session_id 전달
            "phase": None,
            "subphase": None
        },
        title=generate_issue_title(seed_turn, root_cause),
        symptoms=symptoms,
        root_cause=root_cause,
        evidence=[],
        fix=fixes,
        validation=validations,
        related_artifacts=[],
        snippet_refs=[]
    )
```

## Implementation Patterns

### Pattern 1: 점수 기반 링킹

```python
def score_turn_for_issue(
    turn: Turn,
    issue_type: str  # "root_cause", "fix", "validation"
) -> float:
    """
    Turn이 Issue의 특정 부분에 얼마나 적합한지 점수 계산
    """
    score = 0.0
    
    if issue_type == "root_cause":
        if DEBUG_TRIGGERS["error"].search(turn.body):
            score += 5.0
        if DEBUG_TRIGGERS["root_cause"].search(turn.body):
            score += 4.0
    
    elif issue_type == "fix":
        if DEBUG_TRIGGERS["fix"].search(turn.body):
            score += 4.0
        if turn.code_blocks:
            score += 3.0  # 코드가 있으면 fix 가능성 높음
    
    elif issue_type == "validation":
        if DEBUG_TRIGGERS["validation"].search(turn.body):
            score += 3.0
    
    # 거리 패널티
    # (seed에서 멀수록 점수 감소)
    
    return score
```

### Pattern 2: LLM 보조 요약 (옵션)

```python
# backend/core/llm_service.py
from backend.core.cache import get_cached_result, save_cached_result

def summarize_with_llm(text: str, cache_key: str) -> str:
    """
    LLM으로 요약 (캐싱 적용)
    """
    # 캐시 확인
    cached = get_cached_result(cache_key)
    if cached:
        return cached["summary"]
    
    # LLM 호출
    from openai import OpenAI
    client = OpenAI()
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "요약만 제공하세요."},
            {"role": "user", "content": f"다음 텍스트를 1-2문장으로 요약: {text}"}
        ]
    )
    
    summary = response.choices[0].message.content
    
    # 캐시 저장
    save_cached_result(cache_key, {"summary": summary})
    
    return summary
```

## Examples

### 완전한 이벤트 정규화 예시

```python
# backend/builders/event_normalizer.py
def normalize_session(
    session_meta: SessionMeta,
    turns: List[Turn]
) -> dict:
    """
    전체 세션 정규화
    
    Returns:
        {
            "events": List[Event],
            "timeline": List[TimelineEvent],
            "issues": List[IssueCard]
        }
    """
    # 1. Turn → Event 변환
    events = normalize_turns_to_events(turns)
    
    # 2. Timeline 생성
    from backend.builders.timeline_builder import build_timeline
    timeline = build_timeline(
        session_id=session_meta.session_id,
        events=events,
        session_meta=session_meta
    )
    
    # 3. Issue Cards 생성
    from backend.builders.issues_builder import build_issue_cards
    issues = build_issue_cards(turns, events)
    
    return {
        "events": events,
        "timeline": timeline,
        "issues": issues
    }
```

## Checklist

### 이벤트 정규화 구현 시
- [ ] Event 타입 분류 로직 구현
- [ ] Debug 트리거 패턴 정의
- [ ] Artifact 연결 로직 구현
- [ ] Snippet 참조 연결 로직 구현

### Issue Cards 생성 시
- [ ] Symptom seed 탐지 로직
- [ ] 슬라이딩 윈도우 크기 설정
- [ ] Root cause 추출 로직 (confirmed/hypothesis 구분)
- [ ] Fix 추출 로직
- [ ] Validation 추출 로직
- [ ] 카드 완료 조건 확인 (root_cause 또는 fix 중 하나)

### LLM 사용 시
- [ ] 캐싱 로직 구현 (파일 기반)
- [ ] 캐시 키 생성 규칙 명확화
- [ ] 입력 텍스트에 있는 내용만 사용 (새로운 사실 생성 금지)

## References
- 상세 지침: `docs/instruction_detail.md`
- 구체화 지침: `docs/instruction_moredetail.md`
- Parser Rules: `.cursor/rules/parser-rules.mdc`
- Models: `backend/core/models.py`

```

```markdown
---
alwaysApply: true
description: Next.js 프론트엔드 컴포넌트 및 페이지 구현 규칙
---

# Frontend Components

## Overview
Next.js 14+ (App Router) 기반 프론트엔드 구현 규칙. TypeScript, Tailwind CSS를 사용하며, 백엔드 API와의 계약 동기화를 보장합니다.

## Domain Knowledge

### 화면 구성 (MVP)
1. **좌측: 입력 패널**
   - 파일 업로드 (드래그&드롭)
   - Session Meta Preview
   - 파싱 옵션 토글

2. **중앙: 결과 미리보기 탭**
   - Timeline Preview
   - Issues Preview
   - Snippets Preview

3. **우측: Export 패널**
   - 다운로드 버튼들

### 주요 컴포넌트
- `FileUpload` - 파일 업로드
- `SessionMetaPreview` - 세션 메타 표시
- `TimelinePreview` - Timeline 이벤트 리스트
- `IssuesPreview` - Issue Cards 리스트
- `SnippetsPreview` - 코드 스니펫 목록

## Standards & Conventions

### 1. 파일 구조
```
frontend/
├── app/
│   └── page.tsx              # 메인 페이지
├── components/
│   ├── FileUpload.tsx
│   ├── SessionMetaPreview.tsx
│   ├── TimelinePreview.tsx
│   ├── IssuesPreview.tsx
│   └── SnippetsPreview.tsx
├── lib/
│   ├── api.ts                # API 클라이언트
│   └── constants.ts          # 상수 (백엔드와 동기화)
├── types/
│   └── api.ts                # 타입 정의 (백엔드와 동기화)
└── package.json
```

### 2. 타입 정의 규칙

```typescript
// frontend/types/api.ts
// 백엔드 Pydantic 모델과 동일한 구조 유지

export type EventType = 
  | 'status_review'
  | 'plan'
  | 'artifact'
  | 'debug'
  | 'completion'
  | 'next_step'
  | 'turn'

export interface SessionMeta {
  session_id: string
  exported_at?: string
  cursor_version?: string
  phase?: number
  subphase?: number
  source_doc: string
}

export interface TimelineEvent {
  seq: number
  session_id: string
  phase?: number
  subphase?: number
  type: EventType
  summary: string
  artifacts: Array<{
    kind: string
    path: string
    action: string
  }>
  snippet_refs: string[]
}

export interface IssueCard {
  issue_id: string
  scope: {
    session_id: string
    phase?: number
    subphase?: number
  }
  title: string
  symptoms: string[]
  root_cause?: {
    status: 'confirmed' | 'hypothesis'
    text: string
  }
  evidence: Array<{
    type: string
    text_or_ref: string
  }>
  fix: Array<{
    summary: string
    snippet_refs: string[]
  }>
  validation: string[]
  related_artifacts: Array<{
    path: string
    kind: string
  }>
  snippet_refs: string[]
}
```

### 3. API 클라이언트 규칙

```typescript
// frontend/lib/api.ts
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

class ApiClient {
  private baseUrl: string

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl
  }

  async parseFile(file: File): Promise<{
    session_meta: SessionMeta
    turns: any[]
    events: any[]
  }> {
    const formData = new FormData()
    formData.append('file', file)

    const response = await fetch(`${this.baseUrl}/api/parse`, {
      method: 'POST',
      body: formData
    })

    if (!response.ok) {
      throw new Error(`Parse failed: ${response.statusText}`)
    }

    return response.json()
  }

  async createTimeline(
    sessionId: string,
    events: any[],
    sessionMeta: SessionMeta
  ): Promise<{
    session_meta: SessionMeta
    timeline: TimelineEvent[]
  }> {
    const response = await fetch(`${this.baseUrl}/api/timeline`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        session_id: sessionId,
        events,
        session_meta: sessionMeta
      })
    })

    if (!response.ok) {
      throw new Error(`Timeline creation failed: ${response.statusText}`)
    }

    return response.json()
  }

  async getSnippet(snippetId: string): Promise<{
    snippet_id: string
    lang: string
    code: string
  }> {
    const response = await fetch(`${this.baseUrl}/api/snippets/${snippetId}`)

    if (!response.ok) {
      throw new Error(`Snippet fetch failed: ${response.statusText}`)
    }

    return response.json()
  }
}

export const api = new ApiClient(API_BASE_URL)
```

### 4. 컴포넌트 구현 규칙

```typescript
// frontend/components/FileUpload.tsx
'use client'

import { useState, useCallback } from 'react'
import { api } from '@/lib/api'

export function FileUpload({
  onParseComplete
}: {
  onParseComplete: (result: any) => void
}) {
  const [isDragging, setIsDragging] = useState(false)
  const [isParsing, setIsParsing] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleFile = useCallback(async (file: File) => {
    if (!file.name.endsWith('.md')) {
      setError('Only .md files are supported')
      return
    }

    setIsParsing(true)
    setError(null)

    try {
      const result = await api.parseFile(file)
      onParseComplete(result)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Parse failed')
    } finally {
      setIsParsing(false)
    }
  }, [onParseComplete])

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(false)

    const file = e.dataTransfer.files[0]
    if (file) {
      handleFile(file)
    }
  }, [handleFile])

  return (
    <div
      onDrop={handleDrop}
      onDragOver={(e) => {
        e.preventDefault()
        setIsDragging(true)
      }}
      onDragLeave={() => setIsDragging(false)}
      className={`border-2 border-dashed p-8 ${
        isDragging ? 'border-blue-500' : 'border-gray-300'
      }`}
    >
      <input
        type="file"
        accept=".md"
        onChange={(e) => {
          const file = e.target.files?.[0]
          if (file) handleFile(file)
        }}
        className="hidden"
        id="file-upload"
      />
      <label
        htmlFor="file-upload"
        className="cursor-pointer block text-center"
      >
        {isParsing ? 'Parsing...' : 'Drop .md file here or click to select'}
      </label>
      {error && <div className="text-red-500 mt-2">{error}</div>}
    </div>
  )
}
```

### 5. 상태 관리 규칙

```typescript
// frontend/app/page.tsx
'use client'

import { useState } from 'react'
import { FileUpload } from '@/components/FileUpload'
import { SessionMetaPreview } from '@/components/SessionMetaPreview'
import { TimelinePreview } from '@/components/TimelinePreview'
import { IssuesPreview } from '@/components/IssuesPreview'
import { SnippetsPreview } from '@/components/SnippetsPreview'
import type { SessionMeta, TimelineEvent, IssueCard } from '@/types/api'

export default function Home() {
  const [sessionMeta, setSessionMeta] = useState<SessionMeta | null>(null)
  const [timeline, setTimeline] = useState<TimelineEvent[]>([])
  const [issues, setIssues] = useState<IssueCard[]>([])
  const [activeTab, setActiveTab] = useState<'timeline' | 'issues' | 'snippets'>('timeline')

  const handleParseComplete = async (result: any) => {
    setSessionMeta(result.session_meta)

    // Timeline 생성
    const timelineResult = await api.createTimeline(
      result.session_meta.session_id,
      result.events,
      result.session_meta
    )
    setTimeline(timelineResult.timeline)

    // Issues 생성
    const issuesResult = await api.createIssues(
      result.session_meta.session_id,
      result.events,
      result.turns
    )
    setIssues(issuesResult.issues)
  }

  return (
    <div className="grid grid-cols-3 gap-4 p-4">
      {/* 좌측: 입력 패널 */}
      <div className="col-span-1">
        <FileUpload onParseComplete={handleParseComplete} />
        {sessionMeta && (
          <SessionMetaPreview sessionMeta={sessionMeta} />
        )}
      </div>

      {/* 중앙: 결과 미리보기 */}
      <div className="col-span-1">
        <div className="tabs">
          <button onClick={() => setActiveTab('timeline')}>Timeline</button>
          <button onClick={() => setActiveTab('issues')}>Issues</button>
          <button onClick={() => setActiveTab('snippets')}>Snippets</button>
        </div>

        {activeTab === 'timeline' && (
          <TimelinePreview timeline={timeline} />
        )}
        {activeTab === 'issues' && (
          <IssuesPreview issues={issues} />
        )}
        {activeTab === 'snippets' && (
          <SnippetsPreview />
        )}
      </div>

      {/* 우측: Export 패널 */}
      <div className="col-span-1">
        <ExportPanel
          sessionMeta={sessionMeta}
          timeline={timeline}
          issues={issues}
        />
      </div>
    </div>
  )
}
```

## Implementation Patterns

### Pattern 1: 에러 처리

```typescript
// frontend/lib/error-handler.ts
export function handleApiError(error: unknown): string {
  if (error instanceof Error) {
    return error.message
  }
  return 'An unexpected error occurred'
}

// 사용
try {
  const result = await api.parseFile(file)
} catch (error) {
  const message = handleApiError(error)
  toast.error(message)
}
```

### Pattern 2: 로딩 상태 관리

```typescript
// 커스텀 훅
function useAsync<T>(
  asyncFn: () => Promise<T>
): {
  data: T | null
  loading: boolean
  error: string | null
} {
  const [data, setData] = useState<T | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    setLoading(true)
    setError(null)
    asyncFn()
      .then(setData)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false))
  }, [asyncFn])

  return { data, loading, error }
}
```

## Examples

### 완전한 컴포넌트 예시

```typescript
// frontend/components/TimelinePreview.tsx
'use client'

import { useState } from 'react'
import type { TimelineEvent } from '@/types/api'
import { api } from '@/lib/api'

export function TimelinePreview({ timeline }: { timeline: TimelineEvent[] }) {
  const [expandedSeq, setExpandedSeq] = useState<number | null>(null)
  const [snippetCache, setSnippetCache] = useState<Record<string, string>>({})

  const loadSnippet = async (snippetId: string) => {
    if (snippetCache[snippetId]) {
      return snippetCache[snippetId]
    }

    const snippet = await api.getSnippet(snippetId)
    setSnippetCache((prev) => ({
      ...prev,
      [snippetId]: snippet.code
    }))
    return snippet.code
  }

  return (
    <div className="space-y-2">
      {timeline.map((event) => (
        <div
          key={event.seq}
          className="border p-4 rounded cursor-pointer"
          onClick={() => setExpandedSeq(
            expandedSeq === event.seq ? null : event.seq
          )}
        >
          <div className="flex justify-between">
            <span className="font-bold">#{event.seq}</span>
            <span className="text-sm text-gray-500">{event.type}</span>
          </div>
          <p className="mt-2">{event.summary}</p>

          {expandedSeq === event.seq && (
            <div className="mt-4">
              {event.snippet_refs.length > 0 && (
                <div>
                  <h4>Snippets:</h4>
                  {event.snippet_refs.map((snippetId) => (
                    <div key={snippetId}>
                      <code>{snippetId}</code>
                      {/* 스니펫 로드 및 표시 */}
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>
      ))}
    </div>
  )
}
```

## Checklist

### 컴포넌트 구현 시
- [ ] 타입 정의가 백엔드와 동기화되어 있는지 확인
- [ ] API 클라이언트 에러 처리
- [ ] 로딩 상태 표시
- [ ] 반응형 디자인 (Tailwind CSS)
- [ ] 접근성 고려 (키보드 네비게이션 등)

### API 연동 시
- [ ] 요청/응답 타입이 백엔드와 일치하는지 확인
- [ ] 환경 변수 설정 (NEXT_PUBLIC_API_URL)
- [ ] CORS 설정 확인

## References
- API Contract Sync: `.cursor/rules/api-contract-sync.mdc`
- Backend API Design: `.cursor/rules/backend-api-design.mdc`
- Types: `frontend/types/api.ts`
- Constants: `frontend/lib/constants.ts`

```

```markdown
---
alwaysApply: true
description: 테스트 전략 및 E2E 테스트 규칙
---

# Testing Strategy

## Overview
프로젝트는 E2E 테스트 중심의 테스트 전략을 사용합니다. 실제 서버를 실행하여 프로덕션 플로우와 동일하게 검증합니다.

## Domain Knowledge

### 테스트 원칙
1. **E2E 테스트 우선**: 모든 테스트는 실제 서버 실행 필수
2. **실제 데이터 사용**: Mock 사용 절대 금지
3. **프로덕션 플로우 동일**: 배포 후 문제가 없음을 보장
4. **자동 보고 필수**: 테스트 실행 후 상세 분석 리포트

### 테스트 입력 데이터
- 실제 Cursor export 파일: `docs/cursor_phase_6_3.md`
- 각 Phase별 E2E 테스트에서 동일 파일 사용

### 테스트 단계별 검증
- **정합성 검증**: 구조적 정확성 확인
- **타당성 검증**: 실제 상황에서의 품질 확인
- **결과 분석**: 상세 분석 및 개선점 도출

## Standards & Conventions

### 1. 파일 구조
```
tests/
├── fixtures/
│   └── cursor_phase_6_3.md    # 실제 입력 데이터
├── golden/
│   ├── parser_expected.json
│   ├── timeline_expected.json
│   └── issues_expected.json
├── conftest_e2e.py             # E2E 테스트 fixture
├── test_parser_e2e.py
├── test_event_normalizer_e2e.py
├── test_timeline_issues_e2e.py
├── test_snippet_e2e.py
└── test_api_e2e.py
```

### 2. E2E 테스트 Fixture

```python
# tests/conftest_e2e.py
import pytest
import subprocess
import time
import httpx
from pathlib import Path

@pytest.fixture(scope="session")
def test_server():
    """
    실제 uvicorn 서버 실행 fixture
    """
    # 서버 시작
    process = subprocess.Popen(
        ["poetry", "run", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"],
        cwd=Path(__file__).parent.parent,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # 서버 준비 대기
    max_retries = 30
    for _ in range(max_retries):
        try:
            response = httpx.get("http://localhost:8000/health", timeout=1.0)
            if response.status_code == 200:
                break
        except:
            time.sleep(0.5)
    else:
        process.terminate()
        raise RuntimeError("Server failed to start")
    
    yield process
    
    # 서버 종료
    process.terminate()
    process.wait()

@pytest.fixture
def client(test_server):
    """
    httpx.Client fixture (실제 HTTP 요청)
    """
    return httpx.Client(base_url="http://localhost:8000", timeout=30.0)
```

### 3. E2E 테스트 패턴

```python
# tests/test_parser_e2e.py
import pytest
from pathlib import Path
from backend.parser import parse_markdown

def test_parser_e2e():
    """
    실제 입력 데이터로 전체 파서 파이프라인 테스트
    """
    # 1. 실제 입력 데이터 로드
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
    text = input_file.read_text(encoding='utf-8')
    
    # 2. 파싱 실행
    result = parse_markdown(text, source_doc=str(input_file))
    
    # 3. 정합성 검증
    assert result["session_meta"] is not None
    assert result["session_meta"].session_id is not None
    assert len(result["turns"]) > 0
    
    # Session Meta 추출 정확성
    assert result["session_meta"].phase is not None or result["session_meta"].phase is None
    # (phase가 없을 수도 있으므로 None도 허용)
    
    # Turn 블록 분할 정확성
    user_turns = [t for t in result["turns"] if t.speaker == "User"]
    cursor_turns = [t for t in result["turns"] if t.speaker == "Cursor"]
    unknown_turns = [t for t in result["turns"] if t.speaker == "Unknown"]
    
    assert len(user_turns) > 0, "User turns should exist"
    assert len(cursor_turns) > 0, "Cursor turns should exist"
    
    # Unknown 비율 검증
    unknown_ratio = len(unknown_turns) / len(result["turns"])
    assert unknown_ratio < 0.2, f"Unknown speaker ratio too high: {unknown_ratio:.1%}"
    
    # 코드 스니펫 추출 정확성
    all_code_blocks = []
    for turn in result["turns"]:
        all_code_blocks.extend(turn.code_blocks)
    
    assert len(all_code_blocks) > 0, "Code blocks should be extracted"
    
    # 4. 타당성 검증
    # 파싱 실패율 검증
    assert unknown_ratio < 0.2, "Parse failure rate too high"
    
    # 5. 결과 분석 및 피드백
    print(f"\n[Parser E2E Test Results]")
    print(f"Total turns: {len(result['turns'])}")
    print(f"User turns: {len(user_turns)}")
    print(f"Cursor turns: {len(cursor_turns)}")
    print(f"Unknown turns: {len(unknown_turns)} ({unknown_ratio:.1%})")
    print(f"Code blocks: {len(all_code_blocks)}")
    print(f"Artifacts: {len(result.get('artifacts', []))}")
```

### 4. API E2E 테스트 패턴

```python
# tests/test_api_e2e.py
import pytest
from pathlib import Path
import httpx

def test_parse_endpoint_e2e(client: httpx.Client):
    """
    POST /api/parse 엔드포인트 E2E 테스트
    """
    # 실제 입력 파일
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
    
    with open(input_file, "rb") as f:
        files = {"file": ("cursor_phase_6_3.md", f, "text/markdown")}
        response = client.post("/api/parse", files=files)
    
    assert response.status_code == 200
    
    data = response.json()
    
    # 응답 스키마 검증
    assert "session_meta" in data
    assert "turns" in data
    assert "events" in data
    
    # 파싱 결과 정확성
    assert data["session_meta"]["session_id"] is not None
    assert len(data["turns"]) > 0

def test_timeline_endpoint_e2e(client: httpx.Client):
    """
    POST /api/timeline 엔드포인트 E2E 테스트
    """
    # 1. 먼저 파싱
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
    
    with open(input_file, "rb") as f:
        files = {"file": ("cursor_phase_6_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)
    
    parse_data = parse_response.json()
    
    # 2. Timeline 생성
    timeline_response = client.post(
        "/api/timeline",
        json={
            "session_id": parse_data["session_meta"]["session_id"],
            "events": parse_data["events"],
            "session_meta": parse_data["session_meta"]
        }
    )
    
    assert timeline_response.status_code == 200
    
    timeline_data = timeline_response.json()
    
    # Timeline JSON 구조 검증
    assert "session_meta" in timeline_data
    assert "timeline" in timeline_data
    assert len(timeline_data["timeline"]) > 0
    
    # Artifact/Snippet 연결 확인
    for event in timeline_data["timeline"]:
        assert "seq" in event
        assert "type" in event
        assert "summary" in event
```

### 5. 테스트 후 자동 보고

```python
# tests/test_parser_e2e.py
def test_parser_e2e_with_report():
    """
    테스트 실행 후 상세 보고 포함
    """
    # ... 테스트 실행 ...
    
    # 결과 분석
    report = {
        "test_name": "parser_e2e",
        "input_file": str(input_file),
        "results": {
            "total_turns": len(result["turns"]),
            "user_turns": len(user_turns),
            "cursor_turns": len(cursor_turns),
            "unknown_ratio": unknown_ratio,
            "code_blocks": len(all_code_blocks),
            "artifacts": len(result.get("artifacts", []))
        },
        "warnings": [],
        "errors": []
    }
    
    if unknown_ratio > 0.2:
        report["warnings"].append(
            f"High Unknown speaker ratio: {unknown_ratio:.1%}"
        )
    
    # 리포트 출력
    import json
    print("\n" + "="*50)
    print("E2E Test Report")
    print("="*50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("="*50)
    
    # 리포트 파일 저장
    report_file = Path(__file__).parent / "reports" / "parser_e2e_report.json"
    report_file.parent.mkdir(exist_ok=True)
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )
```

## Implementation Patterns

### Pattern 1: Golden 파일 비교

```python
# tests/test_parser_e2e.py
def test_parser_golden_comparison():
    """
    Golden 파일과 비교하여 회귀 테스트
    """
    # 실제 파싱
    result = parse_markdown(text, source_doc)
    
    # Golden 파일 로드
    golden_file = Path(__file__).parent / "golden" / "parser_expected.json"
    if golden_file.exists():
        expected = json.loads(golden_file.read_text(encoding='utf-8'))
        
        # 비교 (주요 필드만)
        assert result["session_meta"].session_id == expected["session_meta"]["session_id"]
        assert len(result["turns"]) == len(expected["turns"])
    else:
        # Golden 파일 생성 (최초 1회)
        golden_file.parent.mkdir(exist_ok=True)
        golden_file.write_text(
            json.dumps({
                "session_meta": result["session_meta"].dict(),
                "turns_count": len(result["turns"])
            }, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
```

### Pattern 2: 로그 파일 저장

```python
# 테스트 실행 시 로그 파일로 저장
import logging
from pathlib import Path

def setup_test_logging():
    """
    테스트용 로깅 설정
    """
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f"test_{time.strftime('%Y%m%d_%H%M%S')}.log"
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)
```

## Examples

### 완전한 E2E 테스트 예시

```python
# tests/test_api_e2e.py
import pytest
from pathlib import Path
import httpx
import json

@pytest.mark.e2e
def test_full_pipeline_e2e(client: httpx.Client):
    """
    전체 파이프라인 E2E 테스트
    파일 업로드 → 파싱 → Timeline 생성 → Issues 생성 → Export
    """
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
    
    # 1. 파일 업로드 및 파싱
    with open(input_file, "rb") as f:
        files = {"file": ("cursor_phase_6_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)
    
    assert parse_response.status_code == 200
    parse_data = parse_response.json()
    
    # 2. Timeline 생성
    timeline_response = client.post(
        "/api/timeline",
        json={
            "session_id": parse_data["session_meta"]["session_id"],
            "events": parse_data["events"],
            "session_meta": parse_data["session_meta"]
        }
    )
    assert timeline_response.status_code == 200
    timeline_data = timeline_response.json()
    
    # 3. Issues 생성
    issues_response = client.post(
        "/api/issues",
        json={
            "session_id": parse_data["session_meta"]["session_id"],
            "events": parse_data["events"],
            "turns": parse_data["turns"]
        }
    )
    assert issues_response.status_code == 200
    issues_data = issues_response.json()
    
    # 4. Export 테스트
    export_response = client.post(
        "/api/export/all",
        json={
            "session_id": parse_data["session_meta"]["session_id"]
        }
    )
    assert export_response.status_code == 200
    
    # 5. 결과 검증
    assert len(timeline_data["timeline"]) > 0
    assert len(issues_data["issues"]) >= 0  # 이슈가 없을 수도 있음
    
    # 6. 리포트 생성
    report = {
        "test": "full_pipeline_e2e",
        "timeline_events": len(timeline_data["timeline"]),
        "issues": len(issues_data["issues"]),
        "status": "PASS"
    }
    
    print(json.dumps(report, indent=2, ensure_ascii=False))
```

## Checklist

### E2E 테스트 작성 시
- [ ] 실제 서버 실행 fixture 사용 (`test_server`)
- [ ] `httpx.Client` 사용 (TestClient 금지)
- [ ] 실제 입력 데이터 사용 (Mock 금지)
- [ ] 정합성 검증 구현
- [ ] 타당성 검증 구현
- [ ] 결과 분석 및 리포트 생성
- [ ] 로그 파일 저장

### 테스트 실행 후
- [ ] 자동으로 상세 보고 출력
- [ ] 리포트 파일 저장
- [ ] 문제 발견 시 원인 분석 포함
- [ ] 정량적 데이터 제시

## References
- AGENTS.md: 테스트 관련 내용
- E2E 테스트 입력: `docs/cursor_phase_6_3.md`
- Backend API: `.cursor/rules/backend-api-design.mdc`

```

기존 `api-contract-sync.mdc`를 `.cursor/rules/`로 복사 중입니다.


PRD와 TODOs.md를 바탕으로 Cursor Rules를 작성했습니다.

## 생성된 규칙 파일

`.cursor/rules/` 디렉토리에 다음 6개 규칙 파일을 생성했습니다:

### 1. **backend-api-design.mdc**
- FastAPI 백엔드 API 설계 규칙
- Pydantic 모델 정의 규칙
- API 라우터 구현 패턴
- 에러 처리 및 파일 업로드 처리
- 캐싱 전략

### 2. **parser-rules.mdc**
- 마크다운 파서 구현 규칙
- 정규식 패턴 (Meta 추출, Turn 분할, 코드 블록 추출)
- Fallback 파서 전략
- Parse Health Check 로직
- 파일/경로 추출 규칙

### 3. **event-normalization.mdc**
- 이벤트 정규화 규칙
- Timeline 빌더 규칙
- Issue Cards 빌더 규칙
- 링킹(연결) 로직 (슬라이딩 윈도우, 점수 기반)
- LLM 보조 요약 (옵션, 캐싱 포함)

### 4. **frontend-components.mdc**
- Next.js 프론트엔드 컴포넌트 규칙
- TypeScript 타입 정의 규칙 (백엔드와 동기화)
- API 클라이언트 구현 패턴
- 상태 관리 및 에러 처리
- 반응형 디자인 (Tailwind CSS)

### 5. **testing-strategy.mdc**
- E2E 테스트 전략
- 실제 서버 실행 fixture
- 테스트 후 자동 보고
- Golden 파일 비교
- 로그 파일 저장

### 6. **api-contract-sync.mdc** (기존 파일 복사)
- 백엔드-프론트엔드 API 계약 동기화
- 상수 및 Enum 동기화 규칙
- 단일 진실 공급원 원칙

## 규칙 파일 특징

각 규칙 파일은 다음 구조를 포함합니다:
- Overview: 도메인 및 목적 설명
- Domain Knowledge: 핵심 개념 및 용어
- Standards & Conventions: 코딩 표준 및 규칙
- Implementation Patterns: 구현 패턴 및 예시
- Examples: 구체적인 코드 예시
- Checklist: 검증 체크리스트
- References: 관련 문서 및 규칙 파일 참조

## 다음 단계

이제 Phase 1(프로젝트 초기 설정)을 시작할 수 있습니다. Cursor Rules가 준비되어 있어 개발 시 자동으로 적용됩니다.

Phase 1을 시작할까요?

---

**User**

**test세션**: backend-frontend가 별도로 구성된 경우, backend에서 E2E 테스트가 완료되어야 합니다. 
이를 위해 각 단계별 sub 테스트가 정합성있게 빠짐없이 되어 있는지 TODOs.md에 반영. 
**AGNETS.md에서 테스트 관련내용 숙지하고, 확인 및 반영하세요

---

**Cursor**

AGENTS.md의 테스트 관련 내용을 확인하고, TODOs.md의 테스트 계획을 점검해 누락된 부분을 보완하겠습니다.


AGENTS.md의 테스트 규칙을 확인했습니다. TODOs.md의 각 Phase별 E2E 테스트 계획을 점검하고 보완하겠습니다.


AGENTS.md의 테스트 규칙을 반영해 TODOs.md의 각 Phase별 E2E 테스트 계획을 보완 중입니다.


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
- [ ] `tests/test_parser.py` 작성
  - [ ] `test_normalize()` - 정규화 테스트
  - [ ] `test_meta_extraction()` - 메타 추출 테스트
  - [ ] `test_turn_parsing()` - Turn 파싱 테스트
  - [ ] `test_snippet_extraction()` - 스니펫 추출 테스트
  - [ ] `test_artifact_extraction()` - Artifact 추출 테스트
- [ ] `tests/fixtures/*.md` 샘플 마크다운 파일 준비
- [ ] `tests/golden/*.json` 예상 결과 (Golden 파일) 준비

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
- [ ] `tests/test_event_normalizer.py` 작성
  - [ ] `test_turn_to_event_conversion()` - Turn → Event 변환 테스트
  - [ ] `test_event_type_classification()` - 이벤트 타입 분류 테스트
  - [ ] `test_artifact_linking()` - Artifact 연결 테스트
  - [ ] `test_snippet_linking()` - Snippet 참조 연결 테스트
- [ ] LLM 호출 Mock 테스트 작성

### E2E 테스트 (Phase 3 완료 검증)
- [ ] `tests/test_event_normalizer_e2e.py` 작성
  - [ ] 실제 입력 데이터 사용: Phase 2에서 파싱한 `docs/cursor_phase_6_3.md` 결과를 입력으로 사용
  - [ ] 정합성 검증: 이벤트 정규화 결과의 구조적 정확성 확인
    - [ ] Turn → Event 변환 정확성
    - [ ] Event 타입 분류 정확성 (status_review/plan/artifact/debug/completion/next_step/turn)
    - [ ] Phase/Subphase 연결 정확성
    - [ ] Artifact 연결 정확성
    - [ ] Snippet 참조 연결 정확성
  - [ ] 타당성 검증: 실제 상황에서의 이벤트 정규화 품질 확인
    - [ ] 이벤트 타입 분류의 적절성
    - [ ] 연결 관계의 정확성
    - [ ] LLM 요약 품질 (LLM 사용 시)
  - [ ] 결과 분석 및 피드백: 이벤트 정규화 결과를 상세히 분석하여 개선점 도출

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
- [ ] `tests/test_timeline_builder.py` 작성
  - [ ] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트
  - [ ] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트
  - [ ] `test_timeline_artifact_linking()` - Artifact 연결 테스트
- [ ] `tests/test_issues_builder.py` 작성
  - [ ] `test_issue_detection()` - 이슈 탐지 테스트
  - [ ] `test_issue_grouping()` - 이슈 그룹화 테스트
  - [ ] `test_symptom_extraction()` - Symptom 추출 테스트
  - [ ] `test_root_cause_extraction()` - Root cause 추출 테스트
- [ ] Golden 파일 비교 테스트 작성

### E2E 테스트 (Phase 4 완료 검증)
- [ ] `tests/test_timeline_issues_e2e.py` 작성
  - [ ] 실제 입력 데이터 사용: Phase 3에서 정규화한 이벤트를 입력으로 사용
  - [ ] 정합성 검증: Timeline 및 Issue Cards 생성 결과의 구조적 정확성 확인
    - [ ] Timeline 시퀀스 번호 부여 정확성
    - [ ] Timeline Phase/Subphase 그룹화 정확성
    - [ ] Timeline Artifact/Snippet 연결 정확성
    - [ ] Issue Cards 탐지 정확성 (DebugEvent 기반)
    - [ ] Issue Cards 그룹화 정확성
    - [ ] Issue Cards symptom/root_cause/fix/validation 추출 정확성
    - [ ] Issue Cards Artifact/Snippet 연결 정확성
  - [ ] 타당성 검증: 실제 상황에서의 Timeline/Issue Cards 품질 확인
    - [ ] Timeline 요약의 적절성
    - [ ] Issue Cards 탐지의 적절성 (과다/과소 탐지 확인)
    - [ ] Issue Cards 내용의 완전성 (symptom/root_cause/fix/validation)
  - [ ] JSON Schema 검증: 생성된 Timeline/Issue Cards JSON이 스키마를 준수하는지 확인
  - [ ] 결과 분석 및 피드백: Timeline/Issue Cards 생성 결과를 상세히 분석하여 개선점 도출

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
- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트
  - [ ] `test_snippet_linking()` - 링킹 테스트
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트

### E2E 테스트 (Phase 5 완료 검증)
- [ ] `tests/test_snippet_e2e.py` 작성
  - [ ] 실제 입력 데이터 사용: Phase 2에서 추출한 코드 스니펫과 Phase 4에서 생성한 Timeline/Issue Cards를 입력으로 사용
  - [ ] 정합성 검증: 스니펫 분리 및 저장 결과의 구조적 정확성 확인
    - [ ] 스니펫 ID 생성 규칙 준수
    - [ ] 스니펫 중복 제거 정확성
    - [ ] 스니펫 파일 저장 정확성 (파일명 규칙, 내용)
    - [ ] Issue/Timeline과의 링킹 정확성
    - [ ] `snippets.json` 생성 정확성
  - [ ] 타당성 검증: 실제 상황에서의 스니펫 관리 품질 확인
    - [ ] 중복 제거 효과 확인
    - [ ] 링킹의 완전성 확인
    - [ ] 파일 저장의 적절성 확인
  - [ ] 결과 분석 및 피드백: 스니펫 분리 및 저장 결과를 상세히 분석하여 개선점 도출

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

### E2E 테스트 (Phase 6 완료 검증 - 백엔드 서버 단계 최종 검증)
- [ ] `tests/conftest_e2e.py` fixture 작성
  - [ ] `test_server` fixture: 실제 uvicorn 서버 실행
  - [ ] `httpx.Client` fixture: 실제 HTTP 요청 클라이언트
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
  - [ ] **결과 분석 및 피드백**: API E2E 테스트 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 결과 리포트 생성
    - [ ] 발견된 문제점 및 개선 사항 문서화

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
- [ ] `tests/test_parser.py` 작성
  - [ ] `test_normalize()` - 정규화 테스트
  - [ ] `test_meta_extraction()` - 메타 추출 테스트
  - [ ] `test_turn_parsing()` - Turn 파싱 테스트
  - [ ] `test_snippet_extraction()` - 스니펫 추출 테스트
  - [ ] `test_artifact_extraction()` - Artifact 추출 테스트
- [ ] `tests/fixtures/*.md` 샘플 마크다운 파일 준비
- [ ] `tests/golden/*.json` 예상 결과 (Golden 파일) 준비

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
- [ ] `tests/test_event_normalizer.py` 작성
  - [ ] `test_turn_to_event_conversion()` - Turn → Event 변환 테스트
  - [ ] `test_event_type_classification()` - 이벤트 타입 분류 테스트
  - [ ] `test_artifact_linking()` - Artifact 연결 테스트
  - [ ] `test_snippet_linking()` - Snippet 참조 연결 테스트
- [ ] LLM 호출 Mock 테스트 작성

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
- [ ] `tests/test_timeline_builder.py` 작성
  - [ ] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트
  - [ ] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트
  - [ ] `test_timeline_artifact_linking()` - Artifact 연결 테스트
- [ ] `tests/test_issues_builder.py` 작성
  - [ ] `test_issue_detection()` - 이슈 탐지 테스트
  - [ ] `test_issue_grouping()` - 이슈 그룹화 테스트
  - [ ] `test_symptom_extraction()` - Symptom 추출 테스트
  - [ ] `test_root_cause_extraction()` - Root cause 추출 테스트
- [ ] Golden 파일 비교 테스트 작성

### E2E 테스트 (Phase 4 완료 검증)
- [ ] `tests/test_timeline_issues_e2e.py` 작성
  - [ ] 실제 입력 데이터 사용: Phase 3에서 정규화한 이벤트를 입력으로 사용
  - [ ] 정합성 검증: Timeline 및 Issue Cards 생성 결과의 구조적 정확성 확인
    - [ ] Timeline 시퀀스 번호 부여 정확성
    - [ ] Timeline Phase/Subphase 그룹화 정확성
    - [ ] Timeline Artifact/Snippet 연결 정확성
    - [ ] Issue Cards 탐지 정확성 (DebugEvent 기반)
    - [ ] Issue Cards 그룹화 정확성
    - [ ] Issue Cards symptom/root_cause/fix/validation 추출 정확성
    - [ ] Issue Cards Artifact/Snippet 연결 정확성
  - [ ] 타당성 검증: 실제 상황에서의 Timeline/Issue Cards 품질 확인
    - [ ] Timeline 요약의 적절성
    - [ ] Issue Cards 탐지의 적절성 (과다/과소 탐지 확인)
    - [ ] Issue Cards 내용의 완전성 (symptom/root_cause/fix/validation)
  - [ ] JSON Schema 검증: 생성된 Timeline/Issue Cards JSON이 스키마를 준수하는지 확인
  - [ ] 결과 분석 및 피드백: Timeline/Issue Cards 생성 결과를 상세히 분석하여 개선점 도출

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
- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트
  - [ ] `test_snippet_linking()` - 링킹 테스트
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트

### E2E 테스트 (Phase 5 완료 검증)
- [ ] `tests/test_snippet_e2e.py` 작성
  - [ ] 실제 입력 데이터 사용: Phase 2에서 추출한 코드 스니펫과 Phase 4에서 생성한 Timeline/Issue Cards를 입력으로 사용
  - [ ] 정합성 검증: 스니펫 분리 및 저장 결과의 구조적 정확성 확인
    - [ ] 스니펫 ID 생성 규칙 준수
    - [ ] 스니펫 중복 제거 정확성
    - [ ] 스니펫 파일 저장 정확성 (파일명 규칙, 내용)
    - [ ] Issue/Timeline과의 링킹 정확성
    - [ ] `snippets.json` 생성 정확성
  - [ ] 타당성 검증: 실제 상황에서의 스니펫 관리 품질 확인
    - [ ] 중복 제거 효과 확인
    - [ ] 링킹의 완전성 확인
    - [ ] 파일 저장의 적절성 확인
  - [ ] 결과 분석 및 피드백: 스니펫 분리 및 저장 결과를 상세히 분석하여 개선점 도출

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

### E2E 테스트 (Phase 6 완료 검증 - 백엔드 서버 단계 최종 검증)
- [ ] `tests/conftest_e2e.py` fixture 작성
  - [ ] `test_server` fixture: 실제 uvicorn 서버 실행
  - [ ] `httpx.Client` fixture: 실제 HTTP 요청 클라이언트
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
  - [ ] **결과 분석 및 피드백**: API E2E 테스트 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 결과 리포트 생성
    - [ ] 발견된 문제점 및 개선 사항 문서화

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
- [ ] `tests/test_parser.py` 작성
  - [ ] `test_normalize()` - 정규화 테스트
  - [ ] `test_meta_extraction()` - 메타 추출 테스트
  - [ ] `test_turn_parsing()` - Turn 파싱 테스트
  - [ ] `test_snippet_extraction()` - 스니펫 추출 테스트
  - [ ] `test_artifact_extraction()` - Artifact 추출 테스트
- [ ] `tests/fixtures/*.md` 샘플 마크다운 파일 준비
- [ ] `tests/golden/*.json` 예상 결과 (Golden 파일) 준비

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
- [ ] `tests/test_event_normalizer.py` 작성
  - [ ] `test_turn_to_event_conversion()` - Turn → Event 변환 테스트
  - [ ] `test_event_type_classification()` - 이벤트 타입 분류 테스트
  - [ ] `test_artifact_linking()` - Artifact 연결 테스트
  - [ ] `test_snippet_linking()` - Snippet 참조 연결 테스트
- [ ] LLM 호출 Mock 테스트 작성

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
- [ ] `tests/test_timeline_builder.py` 작성
  - [ ] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트
  - [ ] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트
  - [ ] `test_timeline_artifact_linking()` - Artifact 연결 테스트
- [ ] `tests/test_issues_builder.py` 작성
  - [ ] `test_issue_detection()` - 이슈 탐지 테스트
  - [ ] `test_issue_grouping()` - 이슈 그룹화 테스트
  - [ ] `test_symptom_extraction()` - Symptom 추출 테스트
  - [ ] `test_root_cause_extraction()` - Root cause 추출 테스트
- [ ] Golden 파일 비교 테스트 작성

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
- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트
  - [ ] `test_snippet_linking()` - 링킹 테스트
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트

### E2E 테스트 (Phase 5 완료 검증)
- [ ] `tests/test_snippet_e2e.py` 작성
  - [ ] 실제 입력 데이터 사용: Phase 2에서 추출한 코드 스니펫과 Phase 4에서 생성한 Timeline/Issue Cards를 입력으로 사용
  - [ ] 정합성 검증: 스니펫 분리 및 저장 결과의 구조적 정확성 확인
    - [ ] 스니펫 ID 생성 규칙 준수
    - [ ] 스니펫 중복 제거 정확성
    - [ ] 스니펫 파일 저장 정확성 (파일명 규칙, 내용)
    - [ ] Issue/Timeline과의 링킹 정확성
    - [ ] `snippets.json` 생성 정확성
  - [ ] 타당성 검증: 실제 상황에서의 스니펫 관리 품질 확인
    - [ ] 중복 제거 효과 확인
    - [ ] 링킹의 완전성 확인
    - [ ] 파일 저장의 적절성 확인
  - [ ] 결과 분석 및 피드백: 스니펫 분리 및 저장 결과를 상세히 분석하여 개선점 도출

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

### E2E 테스트 (Phase 6 완료 검증 - 백엔드 서버 단계 최종 검증)
- [ ] `tests/conftest_e2e.py` fixture 작성
  - [ ] `test_server` fixture: 실제 uvicorn 서버 실행
  - [ ] `httpx.Client` fixture: 실제 HTTP 요청 클라이언트
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
  - [ ] **결과 분석 및 피드백**: API E2E 테스트 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 결과 리포트 생성
    - [ ] 발견된 문제점 및 개선 사항 문서화

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
- [ ] `tests/test_parser.py` 작성
  - [ ] `test_normalize()` - 정규화 테스트
  - [ ] `test_meta_extraction()` - 메타 추출 테스트
  - [ ] `test_turn_parsing()` - Turn 파싱 테스트
  - [ ] `test_snippet_extraction()` - 스니펫 추출 테스트
  - [ ] `test_artifact_extraction()` - Artifact 추출 테스트
- [ ] `tests/fixtures/*.md` 샘플 마크다운 파일 준비
- [ ] `tests/golden/*.json` 예상 결과 (Golden 파일) 준비

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
- [ ] `tests/test_event_normalizer.py` 작성
  - [ ] `test_turn_to_event_conversion()` - Turn → Event 변환 테스트
  - [ ] `test_event_type_classification()` - 이벤트 타입 분류 테스트
  - [ ] `test_artifact_linking()` - Artifact 연결 테스트
  - [ ] `test_snippet_linking()` - Snippet 참조 연결 테스트
- [ ] LLM 호출 Mock 테스트 작성

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
- [ ] `tests/test_timeline_builder.py` 작성
  - [ ] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트
  - [ ] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트
  - [ ] `test_timeline_artifact_linking()` - Artifact 연결 테스트
- [ ] `tests/test_issues_builder.py` 작성
  - [ ] `test_issue_detection()` - 이슈 탐지 테스트
  - [ ] `test_issue_grouping()` - 이슈 그룹화 테스트
  - [ ] `test_symptom_extraction()` - Symptom 추출 테스트
  - [ ] `test_root_cause_extraction()` - Root cause 추출 테스트
- [ ] Golden 파일 비교 테스트 작성

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
- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트
  - [ ] `test_snippet_linking()` - 링킹 테스트
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

### E2E 테스트 (Phase 6 완료 검증 - 백엔드 서버 단계 최종 검증)
- [ ] `tests/conftest_e2e.py` fixture 작성
  - [ ] `test_server` fixture: 실제 uvicorn 서버 실행
  - [ ] `httpx.Client` fixture: 실제 HTTP 요청 클라이언트
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
  - [ ] **결과 분석 및 피드백**: API E2E 테스트 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 결과 리포트 생성
    - [ ] 발견된 문제점 및 개선 사항 문서화

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
- [ ] `tests/test_parser.py` 작성
  - [ ] `test_normalize()` - 정규화 테스트
  - [ ] `test_meta_extraction()` - 메타 추출 테스트
  - [ ] `test_turn_parsing()` - Turn 파싱 테스트
  - [ ] `test_snippet_extraction()` - 스니펫 추출 테스트
  - [ ] `test_artifact_extraction()` - Artifact 추출 테스트
- [ ] `tests/fixtures/*.md` 샘플 마크다운 파일 준비
- [ ] `tests/golden/*.json` 예상 결과 (Golden 파일) 준비

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
- [ ] `tests/test_event_normalizer.py` 작성
  - [ ] `test_turn_to_event_conversion()` - Turn → Event 변환 테스트
  - [ ] `test_event_type_classification()` - 이벤트 타입 분류 테스트
  - [ ] `test_artifact_linking()` - Artifact 연결 테스트
  - [ ] `test_snippet_linking()` - Snippet 참조 연결 테스트
- [ ] LLM 호출 Mock 테스트 작성

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
- [ ] `tests/test_timeline_builder.py` 작성
  - [ ] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트
  - [ ] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트
  - [ ] `test_timeline_artifact_linking()` - Artifact 연결 테스트
- [ ] `tests/test_issues_builder.py` 작성
  - [ ] `test_issue_detection()` - 이슈 탐지 테스트
  - [ ] `test_issue_grouping()` - 이슈 그룹화 테스트
  - [ ] `test_symptom_extraction()` - Symptom 추출 테스트
  - [ ] `test_root_cause_extraction()` - Root cause 추출 테스트
- [ ] Golden 파일 비교 테스트 작성

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
- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트
  - [ ] `test_snippet_linking()` - 링킹 테스트
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

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
  - [ ] **결과 분석 및 피드백**: API E2E 테스트 결과를 상세히 분석하여 개선점 도출
    - [ ] 테스트 결과 리포트 생성
    - [ ] 발견된 문제점 및 개선 사항 문서화

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
- [ ] `tests/test_parser.py` 작성
  - [ ] `test_normalize()` - 정규화 테스트
  - [ ] `test_meta_extraction()` - 메타 추출 테스트
  - [ ] `test_turn_parsing()` - Turn 파싱 테스트
  - [ ] `test_snippet_extraction()` - 스니펫 추출 테스트
  - [ ] `test_artifact_extraction()` - Artifact 추출 테스트
- [ ] `tests/fixtures/*.md` 샘플 마크다운 파일 준비
- [ ] `tests/golden/*.json` 예상 결과 (Golden 파일) 준비

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
- [ ] `tests/test_event_normalizer.py` 작성
  - [ ] `test_turn_to_event_conversion()` - Turn → Event 변환 테스트
  - [ ] `test_event_type_classification()` - 이벤트 타입 분류 테스트
  - [ ] `test_artifact_linking()` - Artifact 연결 테스트
  - [ ] `test_snippet_linking()` - Snippet 참조 연결 테스트
- [ ] LLM 호출 Mock 테스트 작성

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
- [ ] `tests/test_timeline_builder.py` 작성
  - [ ] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트
  - [ ] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트
  - [ ] `test_timeline_artifact_linking()` - Artifact 연결 테스트
- [ ] `tests/test_issues_builder.py` 작성
  - [ ] `test_issue_detection()` - 이슈 탐지 테스트
  - [ ] `test_issue_grouping()` - 이슈 그룹화 테스트
  - [ ] `test_symptom_extraction()` - Symptom 추출 테스트
  - [ ] `test_root_cause_extraction()` - Root cause 추출 테스트
- [ ] Golden 파일 비교 테스트 작성

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
- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트
  - [ ] `test_snippet_linking()` - 링킹 테스트
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

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
- [ ] `tests/test_event_normalizer.py` 작성
  - [ ] `test_turn_to_event_conversion()` - Turn → Event 변환 테스트
  - [ ] `test_event_type_classification()` - 이벤트 타입 분류 테스트
  - [ ] `test_artifact_linking()` - Artifact 연결 테스트
  - [ ] `test_snippet_linking()` - Snippet 참조 연결 테스트
- [ ] LLM 호출 Mock 테스트 작성

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
- [ ] `tests/test_timeline_builder.py` 작성
  - [ ] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트
  - [ ] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트
  - [ ] `test_timeline_artifact_linking()` - Artifact 연결 테스트
- [ ] `tests/test_issues_builder.py` 작성
  - [ ] `test_issue_detection()` - 이슈 탐지 테스트
  - [ ] `test_issue_grouping()` - 이슈 그룹화 테스트
  - [ ] `test_symptom_extraction()` - Symptom 추출 테스트
  - [ ] `test_root_cause_extraction()` - Root cause 추출 테스트
- [ ] Golden 파일 비교 테스트 작성

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
- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트
  - [ ] `test_snippet_linking()` - 링킹 테스트
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

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
- [ ] `tests/test_timeline_builder.py` 작성
  - [ ] `test_timeline_sequence()` - 시퀀스 번호 부여 테스트
  - [ ] `test_timeline_grouping()` - Phase/Subphase 그룹화 테스트
  - [ ] `test_timeline_artifact_linking()` - Artifact 연결 테스트
- [ ] `tests/test_issues_builder.py` 작성
  - [ ] `test_issue_detection()` - 이슈 탐지 테스트
  - [ ] `test_issue_grouping()` - 이슈 그룹화 테스트
  - [ ] `test_symptom_extraction()` - Symptom 추출 테스트
  - [ ] `test_root_cause_extraction()` - Root cause 추출 테스트
- [ ] Golden 파일 비교 테스트 작성

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
- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트
  - [ ] `test_snippet_linking()` - 링킹 테스트
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

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
- [ ] `tests/test_snippet_manager.py` 작성
  - [ ] `test_snippet_id_generation()` - 스니펫 ID 생성 테스트
  - [ ] `test_snippet_deduplication()` - 중복 제거 테스트
  - [ ] `test_snippet_linking()` - 링킹 테스트
  - [ ] `test_snippet_file_save()` - 파일 저장 테스트

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

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
- [ ] `tests/test_api.py` 작성
  - [ ] `test_parse_endpoint()` - 파싱 API 테스트
  - [ ] `test_timeline_endpoint()` - Timeline API 테스트
  - [ ] `test_issues_endpoint()` - Issues API 테스트
  - [ ] `test_snippets_endpoint()` - Snippets API 테스트
  - [ ] `test_export_endpoint()` - Export API 테스트

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


```

Phase 6 E2E 테스트 섹션에 누락된 항목을 확인하고 보완 중입니다.


Phase 6 E2E 테스트 섹션 확인 중입니다.


AGENTS.md의 테스트 규칙을 반영해 TODOs.md를 업데이트했습니다.

## 업데이트 내용 요약

### 1. 각 Phase별 E2E 테스트에 AGENTS.md 규칙 반영

모든 Phase (2, 3, 4, 5, 6)의 E2E 테스트 섹션에 다음을 추가했습니다:

- 경고 표시: "⚠️ 중요: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지"
- 자동 보고 요구사항:
  - 테스트 실행 후 자동으로 상세 보고 출력 (사용자 질문 없이)
  - 정량적 데이터 제시
  - 문제 발견 시 원인 분석 포함
  - 리포트 파일 저장 (`tests/reports/*_e2e_report.json`)

### 2. Phase 6 (백엔드 API) E2E 테스트 강화

- `conftest_e2e.py` fixture 상세화:
  - 서버 시작 대기 로직 (최대 30회 재시도)
  - 서버 종료 자동화
  - `httpx.Client` fixture (TestClient 사용 금지 명시)
  - 타임아웃 설정 (30초)
- 백엔드 서비스 완전성 검증 추가:
  - 모든 API 엔드포인트 정상 동작 확인
  - API 응답 형식이 프론트엔드에서 사용 가능한지 확인
  - 에러 응답 형식의 일관성 확인
  - CORS 설정 확인
  - 백엔드 E2E 테스트 완료 후에만 Phase 7(프론트엔드) 진행

### 3. 단위 테스트 섹션 보완

모든 Phase의 단위 테스트 섹션에:
- "⚠️ 중요: AGENTS.md 규칙 준수 - 실제 데이터만 사용, Mock 사용 절대 금지" 추가
- 각 테스트에 "(실제 데이터 사용)" 명시
- LLM 테스트는 Mock 대신 캐싱 확인으로 변경

### 4. 테스트 데이터 준비 명시

- `tests/fixtures/cursor_phase_6_3.md` (실제 입력 데이터 복사) 명시
- Golden 파일 비교 테스트 구현 명시

## 주요 개선 사항

1. 정합성: 각 Phase별 sub 테스트가 빠짐없이 정의됨
2. 실제 서버 실행: Phase 6에서 실제 uvicorn 서버 실행 E2E 테스트 필수
3. 자동 보고: 모든 E2E 테스트 후 자동 보고 및 리포트 파일 저장
4. 백엔드 완전성 검증: 프론트엔드 구현 전 백엔드 서비스 완전성 검증 필수

이제 TODOs.md가 AGENTS.md의 테스트 규칙을 반영하여, backend-frontend가 별도로 구성된 경우 backend에서 E2E 테스트가 완료되어야 한다는 요구사항을 충족합니다.

---

**User**

**Sub Phase 완료 조건**: TODOs.md 업데이트 및 깃 커밋 반드시 실시

---

**Cursor**

TODOs.md 업데이트를 Git에 커밋합니다. 먼저 Git 상태를 확인합니다.


Git 저장소가 없습니다. 초기화 후 커밋하겠습니다.


커밋 완료. 원격 저장소 설정을 확인 중입니다.


## Sub Phase 완료: TODOs.md 업데이트 및 Git 커밋 완료

### 완료된 작업

1. **Git 저장소 초기화**
   - `git init` 실행 (최초 1회)

2. **변경사항 커밋**
   - 커밋 메시지: `docs: TODOs.md에 AGENTS.md 테스트 규칙 반영 및 E2E 테스트 계획 보완`
   - 커밋 해시: `69b50ea`
   - 변경된 파일: 15개 파일, 9796줄 추가

3. **커밋된 주요 파일**
   - `TODOs.md` (AGENTS.md 테스트 규칙 반영)
   - `.cursor/rules/*.mdc` (6개 규칙 파일)
   - `AGENTS.md`
   - `docs/*.md` (프로젝트 문서들)

### 현재 상태

- 모든 변경사항이 커밋되었습니다.
- 원격 저장소는 아직 설정되지 않았습니다.

### 다음 단계 (선택사항)

원격 저장소가 있으면 다음 명령으로 푸시하세요:

```powershell
git remote add origin <원격_저장소_URL>
git branch -M main
git push -u origin main
```

Sub Phase 완료 조건을 충족했습니다.

```powershell
git remote add origin <원격_저장소_URL>
git branch -M main
git push -u origin main
```

---

**User**

깃 허브 레포 작성 완료
https://github.com/bluecalif/longtext-analysis.git 

---

**Cursor**

원격 저장소를 설정하고 푸시합니다.


원격 저장소 설정과 푸시가 완료되었습니다. 최종 상태를 확인합니다.


## GitHub 원격 저장소 설정 및 푸시 완료

### 완료된 작업

1. 원격 저장소 추가
   - URL: `https://github.com/bluecalif/longtext-analysis.git`
   - 원격 이름: `origin`

2. 브랜치 설정
   - 로컬 브랜치: `main`
   - 원격 추적: `origin/main`

3. 푸시 완료
   - 커밋 해시: `69b50ea`
   - 커밋 메시지: `docs: TODOs.md에 AGENTS.md 테스트 규칙 반영 및 E2E 테스트 계획 보완`
   - 푸시된 파일: 15개 파일, 9796줄

### 현재 상태

- 로컬 저장소와 원격 저장소 동기화 완료
- Working tree clean (커밋할 변경사항 없음)
- 브랜치 상태: `main` 브랜치가 `origin/main`과 동기화됨

### GitHub 레포지토리 확인

레포지토리: [https://github.com/bluecalif/longtext-analysis.git](https://github.com/bluecalif/longtext-analysis.git)

업로드된 주요 파일:
- `TODOs.md` (AGENTS.md 테스트 규칙 반영)
- `.cursor/rules/*.mdc` (6개 Cursor Rules 파일)
- `AGENTS.md`
- `docs/*.md` (프로젝트 문서들)

Sub Phase 완료 조건을 충족했습니다.

---

**User**

**indent 에러관련 에디팅체커**: indentation 에러가 빈발할 수 있으므로, eslintrc 및 prettierrc를 반드시 사용

---

**Cursor**

프로젝트 구조를 확인하고, indent 에러 방지를 위한 ESLint와 Prettier 설정 파일을 생성합니다.


프로젝트 루트에 ESLint와 Prettier 설정 파일을 생성 중입니다.


```jsonc
{
  "extends": [
    "next/core-web-vitals",
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 2022,
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    },
    "project": "./tsconfig.json"
  },
  "plugins": [
    "@typescript-eslint",
    "react",
    "react-hooks"
  ],
  "rules": {
    "indent": ["error", 2, {
      "SwitchCase": 1,
      "VariableDeclarator": 1,
      "outerIIFEBody": 1,
      "MemberExpression": 1,
      "FunctionDeclaration": {
        "parameters": 1,
        "body": 1
      },
      "FunctionExpression": {
        "parameters": 1,
        "body": 1
      },
      "CallExpression": {
        "arguments": 1
      },
      "ArrayExpression": 1,
      "ObjectExpression": 1,
      "ImportDeclaration": 1,
      "flatTernaryExpressions": false,
      "ignoreComments": false
    }],
    "linebreak-style": ["error", "unix"],
    "quotes": ["error", "single", { "avoidEscape": true }],
    "semi": ["error", "always"],
    "no-unused-vars": "off",
    "@typescript-eslint/no-unused-vars": ["error", {
      "argsIgnorePattern": "^_",
      "varsIgnorePattern": "^_"
    }],
    "@typescript-eslint/explicit-function-return-type": "off",
    "@typescript-eslint/explicit-module-boundary-types": "off",
    "@typescript-eslint/no-explicit-any": "warn",
    "react/react-in-jsx-scope": "off",
    "react/prop-types": "off",
    "react-hooks/rules-of-hooks": "error",
    "react-hooks/exhaustive-deps": "warn"
  },
  "settings": {
    "react": {
      "version": "detect"
    }
  },
  "env": {
    "browser": true,
    "es2022": true,
    "node": true
  },
  "ignorePatterns": [
    "node_modules/",
    ".next/",
    "out/",
    "build/",
    "dist/",
    "*.config.js",
    "*.config.ts"
  ]
}

```

```plaintext
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "arrowParens": "avoid",
  "endOfLine": "lf",
  "bracketSpacing": true,
  "jsxSingleQuote": false,
  "quoteProps": "as-needed",
  "proseWrap": "preserve"
}

```

```plaintext
# Dependencies
node_modules/
.pnp
.pnp.js

# Testing
coverage/
*.log

# Next.js
.next/
out/
build/
dist/

# Production
*.min.js
*.min.css

# Misc
.DS_Store
*.pem

# Debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Local env files
.env
.env*.local

# Vercel
.vercel

# TypeScript
*.tsbuildinfo
next-env.d.ts

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Poetry
poetry.lock

# IDE
.vscode/
.idea/

# OS
Thumbs.db

```

```properties
# EditorConfig is awesome: https://EditorConfig.org

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

# Python files
[*.py]
indent_style = space
indent_size = 4
max_line_length = 100

# TypeScript/JavaScript files
[*.{ts,tsx,js,jsx}]
indent_style = space
indent_size = 2
max_line_length = 100

# JSON files
[*.json]
indent_style = space
indent_size = 2

# YAML files
[*.{yml,yaml}]
indent_style = space
indent_size = 2

# Markdown files
[*.md]
trim_trailing_whitespace = false
max_line_length = off

# Makefile
[Makefile]
indent_style = tab

# Shell scripts
[*.sh]
indent_style = space
indent_size = 2

```

```ini
[flake8]
# Python 코드 스타일 검사 설정

# 최대 줄 길이
max-line-length = 100

# 무시할 에러 코드
# E203: whitespace before ':' (black과 충돌)
# E501: line too long (max-line-length로 처리)
# W503: line break before binary operator (black과 충돌)
ignore = E203, E501, W503

# 제외할 디렉토리/파일
exclude =
    .git,
    __pycache__,
    .venv,
    venv,
    env,
    ENV,
    .env,
    build,
    dist,
    *.egg-info,
    .pytest_cache,
    .mypy_cache,
    .coverage,
    htmlcov,
    node_modules,
    .next,
    frontend

# 허용할 최대 복잡도
max-complexity = 10

# import 순서 검사
import-order-style = google

# 통계 출력
statistics = True

# 에러 수 제한
max-errors = 1000

```

```toml
[tool.poetry]
name = "longtext-analysis"
version = "0.1.0"
description = "Cursor IDE 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션"
authors = ["Your Name <you@example.com>"]
readme = "README.md"
packages = [{include = "backend"}]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.104.1"
uvicorn = {extras = ["standard"], version = "^0.24.0"}
pydantic = "^2.5.0"
python-dotenv = "^1.0.0"
openai = "^1.3.0"
regex = "^2023.10.3"
httpx = "^0.25.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.3"
pytest-asyncio = "^0.21.1"
black = "^23.11.0"
flake8 = "^6.1.0"
isort = "^5.12.0"
mypy = "^1.7.0"
ruff = "^0.1.6"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

# Black 설정 (코드 포맷팅)
[tool.black]
line-length = 100
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | venv
  | _build
  | buck-out
  | build
  | dist
  | node_modules
  | \.next
  | frontend
)/
'''

# isort 설정 (import 정렬)
[tool.isort]
profile = "black"
line_length = 100
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
skip_glob = [
    "*/migrations/*",
    "*/node_modules/*",
    "*/.next/*",
    "*/frontend/*"
]

# mypy 설정 (타입 체크)
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
disallow_incomplete_defs = false
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
ignore_missing_imports = true
exclude = [
    "*/migrations/*",
    "*/node_modules/*",
    "*/.next/*",
    "*/frontend/*"
]

# Ruff 설정 (빠른 린터)
[tool.ruff]
line-length = 100
target-version = "py311"
exclude = [
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    "ENV",
    "build",
    "dist",
    "*.egg-info",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    ".next",
    "frontend"
]

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
]
ignore = [
    "E501",  # line too long (handled by black)
    "B008",  # do not perform function calls in argument defaults
    "C901",  # too complex
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]  # unused imports in __init__.py

```

```jsonc
{
  // Editor 설정
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.organizeImports": "explicit"
  },
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.detectIndentation": false,
  "editor.trimAutoWhitespace": true,
  "files.insertFinalNewline": true,
  "files.trimTrailingWhitespace": true,
  "files.eol": "\n",

  // 파일별 포맷터 설정
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.tabSize": 4,
    "editor.insertSpaces": true
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "editor.tabSize": 2
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "editor.tabSize": 2
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "editor.tabSize": 2
  },
  "[javascriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "editor.tabSize": 2
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "editor.tabSize": 2
  },
  "[jsonc]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
  },
  "[markdown]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "files.trimTrailingWhitespace": false
  },

  // Python 설정
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.mypyEnabled": true,
  "python.linting.lintOnSave": true,
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,

  // ESLint 설정
  "eslint.enable": true,
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact"
  ],
  "eslint.format.enable": true,

  // 파일 제외
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.pytest_cache": true,
    "**/.mypy_cache": true,
    "**/.coverage": true,
    "**/htmlcov": true,
    "**/node_modules": true,
    "**/.next": true,
    "**/dist": true,
    "**/build": true
  },

  // 검색 제외
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/*.code-search": true,
    "**/__pycache__": true,
    "**/.next": true,
    "**/dist": true,
    "**/build": true,
    "**/.venv": true,
    "**/venv": true
  }
}

```

```jsonc
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "ms-python.python",
    "ms-python.black-formatter",
    "ms-python.flake8",
    "ms-python.isort",
    "ms-python.mypy-type-checker",
    "charliermarsh.ruff"
  ]
}

```

`.gitignore` 확인 및 업데이트 후 커밋합니다.


`.gitignore` 파일을 생성합니다.


```ignore
# Environment variables
.env
.env.local
.env*.local
.env.production
.env.development

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
env/
ENV/
.venv/
env.bak/
venv.bak/

# Poetry
# poetry.lock  # 프로젝트 정책에 따라 주석 해제

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/
coverage.xml
*.cover
*.py,cover
.hypothesis/
tests/reports/
tests/logs/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Next.js
.next/
out/
build/
dist/
.vercel

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnp
.pnp.js
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz

# TypeScript
*.tsbuildinfo
next-env.d.ts

# Database
*.db
*.sqlite
*.sqlite3
*.db-journal

# Cache and temp
cache/
temp/
tmp/
*.log
*.tmp

# OS
Thumbs.db
.DS_Store
*.swp
*.swo

# Project specific
snippets/
*.zip
reports/
logs/

# Mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Ruff
.ruff_cache/

# Black
.black

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# Celery
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

```

생성된 설정 파일 확인 중입니다.


## Indent 에러 방지 설정 파일 생성 완료

### 생성된 설정 파일

#### 프론트엔드 (Next.js/TypeScript)
1. `.eslintrc.json` — ESLint 설정
   - Next.js 14+ App Router 지원
   - TypeScript 규칙 포함
   - Indent 에러 검사 강화 (2 spaces)
   - React Hooks 규칙 포함

2. `.prettierrc` — Prettier 포맷팅 설정
   - 2 spaces indent
   - Single quotes
   - 100자 줄 길이
   - LF 줄바꿈

3. `.prettierignore` — Prettier 제외 파일 목록

#### 백엔드 (Python)
4. `pyproject.toml` — Poetry 및 Python 도구 설정
   - Black (코드 포맷팅) - 4 spaces indent
   - isort (import 정렬)
   - mypy (타입 체크)
   - Ruff (빠른 린터)

5. `.flake8` — Flake8 설정
   - 100자 최대 줄 길이
   - Black과 호환되는 ignore 규칙

#### 공통
6. `.editorconfig` — 에디터 공통 설정
   - Python: 4 spaces
   - TypeScript/JavaScript: 2 spaces
   - JSON: 2 spaces
   - UTF-8, LF 줄바꿈

7. `.gitignore` — Git 제외 파일 목록
   - Python 캐시, 가상환경
   - Node.js 모듈
   - 환경 변수 파일
   - 빌드 산출물

8. `.vscode/settings.json` — VSCode 워크스페이스 설정
   - 저장 시 자동 포맷팅
   - 파일별 포맷터 지정
   - ESLint 자동 수정

9. `.vscode/extensions.json` — 권장 확장 프로그램 목록

### 주요 기능

1. Indent 에러 방지
   - ESLint: 2 spaces 강제 (TypeScript/JavaScript)
   - Black: 4 spaces 강제 (Python)
   - EditorConfig: 파일 타입별 indent 규칙

2. 자동 포맷팅
   - 저장 시 자동 포맷팅 (VSCode)
   - Prettier (프론트엔드)
   - Black (백엔드)

3. 일관성 유지
   - 모든 파일 타입에 대한 통일된 규칙
   - 팀원 간 동일한 포맷팅

### Git 커밋 완료

- 커밋 해시: `059606a`
- 커밋 메시지: `chore: ESLint, Prettier, EditorConfig 및 Python 린터 설정 파일 추가`
- 푸시 완료: GitHub 원격 저장소에 반영됨

### 다음 단계

프로젝트 개발 시:
1. VSCode 확장 프로그램 설치 (`.vscode/extensions.json` 참고)
2. 저장 시 자동 포맷팅 적용
3. 커밋 전 수동 검사:
   ```powershell
   # 프론트엔드
   npm run lint
   npm run format
   
   # 백엔드
   poetry run black .
   poetry run flake8 .
   poetry run isort .
   ```

Indent 에러 방지를 위한 설정이 완료되었습니다.

```powershell
   # 프론트엔드
   npm run lint
   npm run format
   
   # 백엔드
   poetry run black .
   poetry run flake8 .
   poetry run isort .
```

---

**User**

**README**: README.md를 작성후 프로젝트 구조가 지속적으로 변경되므로, 이를 반영한 업데이트 필수.
README를 언제 최초로 작성하고, 언제마다 업데이트하면 좋을지 제안하세요

---

**Cursor**

프로젝트 상태를 확인하고 README 작성 및 업데이트 시점을 제안합니다.


프로젝트 상태를 확인했습니다. README 작성 및 업데이트 시점 제안입니다.

## README.md 작성 및 업데이트 시점 제안

### 최초 작성 시점

**Phase 1 완료 직후 (권장)**

이유:
- 프로젝트 기본 구조가 생성된 후 작성 가능
- 실제 디렉토리 구조를 반영 가능
- 개발 환경 설정 완료 후 설치/실행 방법을 정확히 기술 가능

**Phase 1에서 작성할 최소 내용:**
```markdown
# Longtext Analysis

## 프로젝트 개요
- PRD 기반 간단한 설명
- 기술 스택 (FastAPI, Next.js)

## 프로젝트 구조
- 실제 생성된 디렉토리 구조

## 개발 환경 설정
- Poetry 설치 및 설정
- Next.js 설치 및 설정
- 환경 변수 설정

## 실행 방법
- 백엔드 서버 실행
- 프론트엔드 개발 서버 실행

## 참고 문서
- PRD, TODOs.md 링크
```

---

### 업데이트 시점 및 주기

#### 1. Phase 완료 시마다 (필수)

각 Phase 완료 후 다음 내용 업데이트:

**Phase 2 완료 후:**
- 파서 모듈 설명 추가
- 파싱 예시 추가

**Phase 3 완료 후:**
- 이벤트 정규화 설명 추가

**Phase 4 완료 후:**
- Timeline/Issue Cards 생성 설명 추가
- 출력 예시 추가

**Phase 5 완료 후:**
- 스니펫 관리 설명 추가

**Phase 6 완료 후:**
- API 엔드포인트 문서 추가
- API 사용 예시 추가

**Phase 7 완료 후:**
- UI 스크린샷 추가
- 사용자 가이드 추가

**Phase 8 완료 후:**
- 배포 가이드 추가
- 트러블슈팅 섹션 추가

#### 2. 프로젝트 구조 변경 시 (필수)

다음 변경 시 즉시 업데이트:
- 새 디렉토리 추가/삭제
- 주요 파일 위치 변경
- 설정 파일 추가/변경
- 의존성 패키지 추가/변경

#### 3. 정기 업데이트 (권장)

- 주 1회: 진행 상황 반영
- Phase 시작 전: 예정 작업 확인 및 README와 일치 여부 점검

---

### README 업데이트 체크리스트

각 Phase 완료 후 다음 항목 확인:

```markdown
## 업데이트 체크리스트

### 프로젝트 구조
- [ ] 디렉토리 구조가 실제와 일치하는가?
- [ ] 새로 추가된 디렉토리/파일이 반영되었는가?

### 설치 및 실행
- [ ] 설치 명령어가 정확한가?
- [ ] 실행 방법이 최신인가?
- [ ] 환경 변수 설정이 완전한가?

### 기능 설명
- [ ] 새로 구현된 기능이 설명되었는가?
- [ ] API 엔드포인트가 문서화되었는가?
- [ ] 사용 예시가 최신인가?

### 참고 문서
- [ ] 링크가 유효한가?
- [ ] 새 문서가 추가되었는가?
```

---

### README 구조 제안

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

### 권장 워크플로우

1. Phase 1 완료 직후: 최초 README 작성
2. 각 Phase 완료 시: 해당 Phase 내용 추가/업데이트
3. 프로젝트 구조 변경 시: 즉시 구조 섹션 업데이트
4. 주 1회: 전체 내용 검토 및 정리

---

### 자동화 제안 (선택사항)

README 업데이트를 자동화하려면:

1. Phase 완료 시 자동 체크리스트 생성
2. 디렉토리 구조 자동 생성 스크립트
3. API 엔드포인트 자동 문서화 (FastAPI OpenAPI 활용)

---

## 결론

- 최초 작성: Phase 1 완료 직후
- 업데이트 주기:
  - 필수: 각 Phase 완료 시, 프로젝트 구조 변경 시
  - 권장: 주 1회 정기 검토

이렇게 하면 README가 프로젝트 상태를 정확히 반영하고, 새로 참여하는 개발자도 빠르게 이해할 수 있습니다.

Phase 1 완료 후 최초 README 작성을 진행할까요?

```markdown
# Longtext Analysis

## 프로젝트 개요
- PRD 기반 간단한 설명
- 기술 스택 (FastAPI, Next.js)

## 프로젝트 구조
- 실제 생성된 디렉토리 구조

## 개발 환경 설정
- Poetry 설치 및 설정
- Next.js 설치 및 설정
- 환경 변수 설정

## 실행 방법
- 백엔드 서버 실행
- 프론트엔드 개발 서버 실행

## 참고 문서
- PRD, TODOs.md 링크
```

```markdown
## 업데이트 체크리스트

### 프로젝트 구조
- [ ] 디렉토리 구조가 실제와 일치하는가?
- [ ] 새로 추가된 디렉토리/파일이 반영되었는가?

### 설치 및 실행
- [ ] 설치 명령어가 정확한가?
- [ ] 실행 방법이 최신인가?
- [ ] 환경 변수 설정이 완전한가?

### 기능 설명
- [ ] 새로 구현된 기능이 설명되었는가?
- [ ] API 엔드포인트가 문서화되었는가?
- [ ] 사용 예시가 최신인가?

### 참고 문서
- [ ] 링크가 유효한가?
- [ ] 새 문서가 추가되었는가?
```

```markdown
# Longtext Analysis

## 📋 프로젝트 개요
- 목적 및 배경
- 주요 기능

## 🏗️ 프로젝트 구조
```

```plaintext

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

**User**

@TODOs.md README 생성 및 업데이트 반영해주세요

---

**Cursor**

TODOs.md에 README 생성 및 업데이트 관련 내용을 반영 중입니다.


TODOs.md에 README 생성 및 업데이트 관련 내용을 반영 중입니다.


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
- [ ] `README.md` 최초 작성
  - [ ] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [ ] 기술 스택 (FastAPI, Next.js)
  - [ ] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [ ] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [ ] 환경 변수 설정 (`.env.example` 참조)
  - [ ] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [ ] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
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
- [ ] `README.md` 최초 작성
  - [ ] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [ ] 기술 스택 (FastAPI, Next.js)
  - [ ] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [ ] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [ ] 환경 변수 설정 (`.env.example` 참조)
  - [ ] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [ ] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
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

### README 업데이트 (Phase 2 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 파서 모듈 설명 추가
  - [ ] 파싱 예시 추가
  - [ ] 프로젝트 구조 업데이트 (실제 디렉토리 구조 반영)

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
- [ ] `README.md` 최초 작성
  - [ ] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [ ] 기술 스택 (FastAPI, Next.js)
  - [ ] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [ ] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [ ] 환경 변수 설정 (`.env.example` 참조)
  - [ ] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [ ] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
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

### README 업데이트 (Phase 2 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 파서 모듈 설명 추가
  - [ ] 파싱 예시 추가
  - [ ] 프로젝트 구조 업데이트 (실제 디렉토리 구조 반영)

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

### README 업데이트 (Phase 3 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 이벤트 정규화 설명 추가
  - [ ] 이벤트 타입 설명 추가

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
- [ ] `README.md` 최초 작성
  - [ ] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [ ] 기술 스택 (FastAPI, Next.js)
  - [ ] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [ ] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [ ] 환경 변수 설정 (`.env.example` 참조)
  - [ ] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [ ] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
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

### README 업데이트 (Phase 2 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 파서 모듈 설명 추가
  - [ ] 파싱 예시 추가
  - [ ] 프로젝트 구조 업데이트 (실제 디렉토리 구조 반영)

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

### README 업데이트 (Phase 3 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 이벤트 정규화 설명 추가
  - [ ] 이벤트 타입 설명 추가

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
- [ ] `README.md` 최초 작성
  - [ ] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [ ] 기술 스택 (FastAPI, Next.js)
  - [ ] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [ ] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [ ] 환경 변수 설정 (`.env.example` 참조)
  - [ ] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [ ] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
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

### README 업데이트 (Phase 2 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 파서 모듈 설명 추가
  - [ ] 파싱 예시 추가
  - [ ] 프로젝트 구조 업데이트 (실제 디렉토리 구조 반영)

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

### README 업데이트 (Phase 3 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 이벤트 정규화 설명 추가
  - [ ] 이벤트 타입 설명 추가

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
- [ ] `README.md` 최초 작성
  - [ ] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [ ] 기술 스택 (FastAPI, Next.js)
  - [ ] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [ ] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [ ] 환경 변수 설정 (`.env.example` 참조)
  - [ ] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [ ] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
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

### README 업데이트 (Phase 2 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 파서 모듈 설명 추가
  - [ ] 파싱 예시 추가
  - [ ] 프로젝트 구조 업데이트 (실제 디렉토리 구조 반영)

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

### README 업데이트 (Phase 3 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 이벤트 정규화 설명 추가
  - [ ] 이벤트 타입 설명 추가

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
- [ ] `README.md` 최초 작성
  - [ ] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [ ] 기술 스택 (FastAPI, Next.js)
  - [ ] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [ ] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [ ] 환경 변수 설정 (`.env.example` 참조)
  - [ ] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [ ] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
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

### README 업데이트 (Phase 2 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 파서 모듈 설명 추가
  - [ ] 파싱 예시 추가
  - [ ] 프로젝트 구조 업데이트 (실제 디렉토리 구조 반영)

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

### README 업데이트 (Phase 3 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 이벤트 정규화 설명 추가
  - [ ] 이벤트 타입 설명 추가

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
- [ ] `README.md` 최초 작성
  - [ ] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [ ] 기술 스택 (FastAPI, Next.js)
  - [ ] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [ ] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [ ] 환경 변수 설정 (`.env.example` 참조)
  - [ ] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [ ] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
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

### README 업데이트 (Phase 2 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 파서 모듈 설명 추가
  - [ ] 파싱 예시 추가
  - [ ] 프로젝트 구조 업데이트 (실제 디렉토리 구조 반영)

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

### README 업데이트 (Phase 3 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 이벤트 정규화 설명 추가
  - [ ] 이벤트 타입 설명 추가

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


```

```markdown
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
```

README 업데이트 가이드라인 섹션을 추가하기 위해 파일을 다시 확인 중입니다.


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
- [ ] `README.md` 최초 작성
  - [ ] 프로젝트 개요 (PRD 기반 간단한 설명)
  - [ ] 기술 스택 (FastAPI, Next.js)
  - [ ] 프로젝트 구조 (실제 생성된 디렉토리 구조 반영)
  - [ ] 개발 환경 설정 (Poetry, Next.js 설치 방법)
  - [ ] 환경 변수 설정 (`.env.example` 참조)
  - [ ] 실행 방법 (백엔드/프론트엔드 서버 실행)
  - [ ] 참고 문서 링크 (PRD, TODOs.md, AGENTS.md)
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

### README 업데이트 (Phase 2 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 파서 모듈 설명 추가
  - [ ] 파싱 예시 추가
  - [ ] 프로젝트 구조 업데이트 (실제 디렉토리 구조 반영)

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

### README 업데이트 (Phase 3 완료 후)
- [ ] `README.md` 업데이트
  - [ ] 이벤트 정규화 설명 추가
  - [ ] 이벤트 타입 설명 추가

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

**현재 Phase**: Phase 1 (프로젝트 초기 설정 및 환경 구성)

**마지막 업데이트**: 2025-01-XX

**완료된 Phase**:
- 없음

**진행 중인 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성

**다음 단계**:
- Phase 1 완료 후 Phase 2로 진행


```

TODOs.md에 README 생성 및 업데이트 관련 내용을 반영했습니다.

## 업데이트 완료 내용

### 1. Phase 1 - README 최초 작성 상세화
- 프로젝트 개요, 기술 스택, 프로젝트 구조, 개발 환경 설정, 환경 변수 설정, 실행 방법, 참고 문서 링크 포함

### 2. 각 Phase별 README 업데이트 체크리스트 추가
- Phase 2: 파서 모듈 설명, 파싱 예시 추가
- Phase 3: 이벤트 정규화 설명 추가
- Phase 4: Timeline/Issue Cards 생성 설명, 출력 예시 추가
- Phase 5: 스니펫 관리 설명 추가
- Phase 6: API 엔드포인트 문서, API 사용 예시 추가
- Phase 7: UI 스크린샷, 사용자 가이드 추가
- Phase 8: 배포 가이드, 트러블슈팅, 최종 업데이트

### 3. README 업데이트 가이드라인 섹션 추가
- 최초 작성 시점: Phase 1 완료 직후
- 업데이트 시점:
  - 필수: 각 Phase 완료 시, 프로젝트 구조 변경 시
  - 권장: 주 1회 정기 검토, Phase 시작 전 점검
- README 업데이트 체크리스트: 10개 항목
- README 구조 권장 사항: 템플릿 제공

### Git 커밋 완료
- 커밋 해시: `ccfb30d`
- 커밋 메시지: `docs: README 업데이트 가이드라인 섹션 추가`
- 푸시 완료: GitHub 원격 저장소에 반영됨

이제 각 Phase 완료 시 README를 업데이트할 수 있고, 프로젝트 구조 변경 시에도 README를 최신 상태로 유지할 수 있습니다.

