# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (필수)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

**이전 Archive**: `TODOs_archive_20251228.md` (상세 내용 참조)

---

## ⚠️ 중요: LLM 사용 규칙 (프로젝트 전역)

**기본 원칙**: 모든 빌더 함수는 기본적으로 LLM을 사용합니다.

### 핵심 규칙

1. **기본값**: 모든 빌더 함수의 `use_llm` 파라미터 기본값은 `USE_LLM_BY_DEFAULT = True`입니다.
   - `normalize_turns_to_events(..., use_llm=USE_LLM_BY_DEFAULT)`
   - `build_structured_timeline(..., use_llm=USE_LLM_BY_DEFAULT)`
   - `build_issue_cards(..., use_llm=USE_LLM_BY_DEFAULT)`

2. **패턴 기반(REGEX) vs LLM 기반**:
   - **LLM 기반 (기본값)**: 모든 빌더 함수는 기본적으로 LLM을 사용합니다.
   - **패턴 기반 (Fallback)**: LLM 실패 시에만 패턴 기반으로 fallback합니다.
   - **명시적 패턴 기반**: 테스트에서 패턴 기반을 사용하려면 명시적으로 `use_llm=False`를 전달하세요.

3. **테스트 규칙**:
   - `test_*_with_llm()`: LLM 사용 (명시적)
   - `test_*_pattern()` 또는 `test_*_no_llm()`: 패턴 기반 (명시적)
   - 그 외: 기본값 사용 (LLM)

4. **API 규칙** (Phase 6+):
   - 모든 API 엔드포인트도 기본적으로 LLM을 사용합니다.
   - 클라이언트가 명시적으로 `use_llm=false`를 전달하지 않는 한 LLM 사용.

5. **주의사항**:
   - **다음 세션에서 코드를 작성할 때도 이 규칙을 따라야 합니다.**
   - 새로운 빌더 함수를 추가할 때도 `use_llm=True`를 기본값으로 설정하세요.
   - 이 규칙은 `.cursor/rules/llm-default-rule.mdc`에도 문서화되어 있습니다.
   - 상수 정의: `backend/core/constants.py`의 `USE_LLM_BY_DEFAULT = True`

### 다층 방어선

1. **코드 레벨**: 모든 함수의 기본값이 `USE_LLM_BY_DEFAULT = True`
2. **상수 정의**: `backend/core/constants.py`에 명시적 상수 정의
3. **문서화**: 이 문서와 `.cursor/rules/llm-default-rule.mdc`에 규칙 명시
4. **테스트 Fixture**: 테스트 함수 이름에서 자동 감지 (`_with_llm`, `_pattern`, `_no_llm`)
5. **타입 힌트**: 모든 함수에 명확한 타입 힌트와 문서화

---

## 아키텍처 개요

```
마크다운 파일 업로드 → Ingest & Normalize → Session Meta 추출 → Turn 파싱
→ Artifact 추출 → Event 정규화 → Timeline 생성 + Issue Cards 생성 + 코드 스니펫 분리
→ JSON/MD 출력 → 다운로드
```

---

## Phase 1-2: 완료 (2025-12-19)

- ✅ Phase 1: 프로젝트 초기 설정 및 환경 구성 (Poetry, FastAPI, Next.js 설정)
- ✅ Phase 2: 백엔드 파서 구현 (텍스트 정규화, 세션 메타 추출, Turn 파싱, 코드 스니펫/Artifact 추출)
  - 단위 테스트 및 E2E 테스트 완료

---

## Phase 3: 이벤트 추출 및 정규화 (완료)

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**
- Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행
- Phase 4나 Phase 5에서 문제 발견 시 Phase 3으로 돌아가서 개선 후 재검증

**완료된 Sub Phase**:
- ✅ Phase 3.0: 기본 구현 (데이터 모델 정의, 이벤트 정규화 기본 구현)
- ✅ Phase 3.1: 즉시 개선 (이벤트 중복 생성 방지, Summary 품질 개선)
- ✅ Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini, 파일 기반 캐싱)
- ✅ Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선 (224초 → 44.99초, 약 5배 향상)
- ✅ Phase 3.3: 결과 평가 방법 구축
- ✅ Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선
  - EventType.ARTIFACT 제거, EventType.CODE_GENERATION 추가
  - ArtifactAction Enum 추가

**상세 내용**: `TODOs_archive_20251228.md` 참조

---

## Phase 4: Timeline 및 Issue Cards 생성 (완료)

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**완료된 Sub Phase**:
- ✅ 기본 구현: Timeline 빌더, Issue Cards 빌더 구현
- ✅ Phase 4.5: Timeline 구조화 개선 (TimelineSection 모델, LLM 기반 작업 항목 추출)
- ✅ Phase 4.6: Issue Card 품질 개선 (LLM 기반 추출 함수 구현, 품질 점수: 94/100)
- ✅ Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토
  - `extract_issue_with_llm()` 통합 함수 사용으로 전환
  - Fix 항목: 20개 → 1개 (95% 감소), 품질 대폭 향상

**상세 내용**: `TODOs_archive_20251228.md` 참조

---

## Phase 5: 코드 스니펫 분리 및 저장 (완료)

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

**완료된 작업**:
- ✅ Snippet 모델 정의
- ✅ 스니펫 관리 모듈 구현 (ID 생성, 해시, 언어 판별, 변환, 중복 제거, 링킹)
- ✅ 스니펫 저장 모듈 구현 (snippets.json 생성)
- ✅ 단위 테스트 및 E2E 테스트 완료
  - 92개 코드 블록 → 81개 스니펫 (11개 중복 제거)
  - 19개 이벤트 링킹, 1개 Issue Card 링킹

**상세 내용**: `TODOs_archive_20251228.md` 참조

---

## Phase 6: LLM 호출 최적화 (완료)

**목표**: LLM 호출 횟수를 최적화하여 비용을 절감하면서 데이터 품질을 유지 또는 향상

**완료된 Sub Phase**:
- ✅ Phase 6.1: 이벤트 추출 최적화 (배치 처리)
  - 배치 처리 LLM 함수 구현 (`classify_and_summarize_batch_with_llm()`)
  - 67번 호출 → 13-14번 호출 (약 80% 감소)
- ✅ Phase 6.2: 타임라인 구조화 최적화 (검증 로직 개선)
  - LLM 결과 활용률: 0% → 100%
  - 검증 실패율: 100% → 0%

**상세 내용**: `TODOs_archive_20251228.md` 참조

---

## Phase 7: 백엔드 API 구현 (완료)

**목표**: FastAPI 기반 백엔드 API 엔드포인트 구현. 프론트엔드에서 사용할 수 있도록 RESTful API 제공.

**완료된 Sub Phase**:
- ✅ Phase 7.1: API 요청/응답 스키마 검토 및 추가
- ✅ Phase 7.2: Parse API 구현 (`POST /api/parse`)
- ✅ Phase 7.3: Timeline API 구현 (`POST /api/timeline`)
- ✅ Phase 7.4: Issues API 구현 (`POST /api/issues`)
- ✅ Phase 7.5: Snippets API 구현 (`GET /api/snippets/{snippet_id}`, `POST /api/snippets/process`)
- ✅ Phase 7.6: Markdown 렌더러 구현 (`render_timeline_md`, `render_issues_md`)
- ✅ Phase 7.7: Export API 구현 (`POST /api/export/timeline`, `/api/export/issues`, `/api/export/all`)
- ✅ Phase 7.8: FastAPI 앱 라우터 등록
- ✅ Phase 7.9: API E2E 테스트 작성 및 검증 (6개 테스트 모두 통과)
- ✅ Phase 7.10: Phase 완료 작업 (서버 관리 개선, TODOs.md 업데이트)
- ✅ Phase 7.11: Pipeline Cache 통일 (프로젝트 전반 캐시 일관성 확보)
  - 파일 내용 해시 기반 캐싱
  - Phase 2-7 전반에 pipeline_cache 적용

**주요 API 엔드포인트**:
- `POST /api/parse` - 파일 업로드 및 파싱
- `POST /api/timeline` - Timeline 생성
- `POST /api/issues` - Issue Cards 생성
- `GET /api/snippets/{snippet_id}` - 스니펫 조회
- `POST /api/snippets/process` - 스니펫 처리
- `POST /api/export/timeline` - Timeline 다운로드 (JSON/MD)
- `POST /api/export/issues` - Issues 다운로드 (JSON/MD)
- `POST /api/export/all` - 전체 산출물 다운로드 (ZIP)

**상세 내용**: `TODOs_archive_20251228.md` 참조

---

## Phase 8: 프론트엔드 UI 구현

**목표**: Next.js 14+ 기반 프론트엔드 UI 구현. 백엔드 API와의 contract 동기화를 보장하며, 입력 패널, 결과 미리보기, Export 패널을 포함한 전체 기능을 구현합니다.

**⚠️ 중요: Phase별 진행 원칙 (AGENTS.md 준수)**
- 각 Sub Phase (8.1, 8.2, ...) 단위로만 작업 진행
- Sub Phase 완료 후 사용자 피드백 요청
- 작업 전 사용자 확인 필수
- Phase 8 완료 시 필수 작업: 테스트 실행 검증 → TODOs.md 업데이트 → Git commit

**⚠️ 중요: Sub Phase별 브라우저 확인 규칙**
- 각 Sub Phase 완료 후 가능한 단계부터 브라우저에서 사용자가 확인할 수 있도록 구성
- 백엔드 서버와 프론트엔드 서버를 실행하여 실제 동작 확인
- 각 Sub Phase별로 "브라우저 확인" 섹션에 확인 방법 명시
- 서버 실행 방법:
  - 백엔드: `poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000` (프로젝트 루트에서)
  - 프론트엔드: `npm --prefix frontend run dev` (프로젝트 루트에서)

### Phase 8.1: 타입 정의 및 API Contract 동기화

**목표**: 백엔드 Pydantic 모델과 완전히 일치하는 TypeScript 타입 정의

**⚠️ 중요: API Contract 동기화 원칙**
- 모든 타입은 백엔드 모델과 1:1 매핑
- Enum 값은 문자열 리터럴로 정확히 일치
- Query 파라미터 이름은 snake_case 유지 (`use_llm`)
- 필드명, 타입, Optional 여부 모두 일치

**구현 계획**:
- [x] `frontend/types/api.ts` 생성
  - [x] `EventType` enum 정의 (백엔드 `EventType`와 동일한 값)
  - [x] `ArtifactAction` enum 정의
  - [x] `ExportFormat` enum 정의
  - [x] `IssueStatus` enum 정의
  - [x] `SessionMeta` interface 정의
  - [x] `CodeBlock` interface 정의
  - [x] `Turn` interface 정의
  - [x] `Event` interface 정의
  - [x] `TimelineEvent` interface 정의
  - [x] `TimelineSection` interface 정의
  - [x] `IssueCard` interface 정의
  - [x] `Snippet` interface 정의
  - [x] API Request/Response 타입 정의:
    - [x] `ParseResponse`
    - [x] `TimelineRequest`, `TimelineResponse`
    - [x] `IssuesRequest`, `IssuesResponse`
    - [x] `SnippetResponse`
    - [x] `SnippetsProcessRequest`, `SnippetsProcessResponse`
    - [x] `ExportTimelineRequest`, `ExportIssuesRequest`, `ExportAllRequest`

**검증 방법**:
- 백엔드 `backend/core/models.py`와 필드명, 타입, Optional 여부 일치 확인
- Enum 값 문자열 리터럴 정확히 일치 확인
- TypeScript 컴파일 오류 없음 확인 (`npm --prefix frontend run build` 또는 `npx tsc --noEmit`)

**브라우저 확인**:
- 이 단계에서는 브라우저 확인 불가 (타입 정의만 수행)
- TypeScript 컴파일 확인으로 대체

### Phase 8.2: API 클라이언트 구현

**목표**: 타입 안전한 API 클라이언트 구현

**구현 계획**:
- [x] `frontend/lib/api.ts` 생성
  - [x] API 기본 URL 설정 (`NEXT_PUBLIC_API_URL` 환경 변수)
  - [x] fetch 기반 클라이언트 구현
  - [x] 에러 처리 (HTTPException → ApiError 변환)
  - [x] API 함수 구현:
    - [x] `parseFile(file: File, use_llm?: boolean): Promise<ParseResponse>`
      - Query 파라미터: `use_llm` (snake_case, bool)
      - FormData로 파일 업로드
    - [x] `createTimeline(request: TimelineRequest, use_llm?: boolean): Promise<TimelineResponse>`
      - Query 파라미터: `use_llm` (snake_case, bool)
    - [x] `createIssues(request: IssuesRequest, use_llm?: boolean): Promise<IssuesResponse>`
      - Query 파라미터: `use_llm` (snake_case, bool)
    - [x] `processSnippets(request: SnippetsProcessRequest): Promise<SnippetsProcessResponse>`
    - [x] `getSnippet(snippetId: string): Promise<SnippetResponse>`
    - [x] `exportTimeline(request: ExportTimelineRequest): Promise<Blob>`
    - [x] `exportIssues(request: ExportIssuesRequest): Promise<Blob>`
    - [x] `exportAll(request: ExportAllRequest): Promise<Blob>`

**⚠️ 중요: Query 파라미터 동기화**
- 백엔드: `use_llm: bool = Query(default=USE_LLM_BY_DEFAULT)` (snake_case)
- 프론트엔드: `use_llm?: boolean` (snake_case 유지, camelCase 금지)

**검증 방법**:
- 백엔드 API 엔드포인트와 Query 파라미터 이름 일치 확인
- 타입 안전성 확인 (TypeScript 컴파일 오류 없음)

**브라우저 확인** (⚠️ 필수):
- [x] 테스트 페이지 구현 완료 (`frontend/app/page.tsx` - API 클라이언트 테스트용)
- [x] 백엔드 서버 실행: `poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000`
- [x] 프론트엔드 개발 서버 실행: `npm --prefix frontend run dev`
- [x] 브라우저에서 `http://localhost:3000` 접속
- [x] 브라우저 개발자 도구 콘솔에서 API 클라이언트 함수 직접 호출 테스트
  - `window.api.parseFile(file)` 또는 테스트 페이지에서 파일 업로드
- [x] 네트워크 탭에서 API 요청 확인 (Query 파라미터 `use_llm` snake_case 확인)
  - Request URL: `http://localhost:8000/api/parse?use_llm=true` (snake_case 확인)
- [x] API 응답 타입 일치 확인 (콘솔에서 응답 객체 구조 확인)
  - `result.session_meta`, `result.turns`, `result.events`, `result.content_hash` 확인
- [x] 브라우저 확인 결과 문서화 (성공/실패, 발견된 문제점)
  - ✅ 확인 결과: 양호 (2025-12-28)

**참고**: 상세 브라우저 확인 가이드는 `docs/phase8_2_browser_test.md` 참조

### Phase 8.3: 상수 정의 (필요 시)

**목표**: 백엔드 상수와 동기화

**구현 계획**:
- [x] `frontend/lib/constants.ts` 생성
  - [x] `USE_LLM_BY_DEFAULT = true` (백엔드와 동일)
  - [x] API 클라이언트에서 상수 사용 (`frontend/lib/api.ts`에 import 및 적용)

**검증 방법**:
- 백엔드 `backend/core/constants.py`와 값 일치 확인

**브라우저 확인**:
- 이 단계에서는 브라우저 확인 불가 (상수 정의만 수행)
- 코드 리뷰로 대체

### Phase 8.4: 메인 페이지 레이아웃 구현

**목표**: 3열 레이아웃 구성 (입력 패널 | 미리보기 | Export 패널)

**구현 계획**:
- [ ] `frontend/app/page.tsx` 수정
  - [ ] 상태 관리 (React hooks)
    - [ ] `sessionMeta`, `turns`, `events` 상태
    - [ ] `timelineSections`, `issueCards`, `snippets` 상태
    - [ ] `activeTab` 상태 (timeline | issues | snippets)
    - [ ] `isProcessing` 상태 (로딩 표시)
  - [ ] 3열 레이아웃 구성 (Tailwind CSS Grid)
    - [ ] 좌측: 입력 패널 (고정 너비)
    - [ ] 중앙: 결과 미리보기 (가변 너비)
    - [ ] 우측: Export 패널 (고정 너비)
  - [ ] 파이프라인 실행 로직
    - [ ] 파일 업로드 → 파싱 → Timeline 생성 → Issues 생성 → Snippets 처리 순서

**브라우저 확인**:
- [ ] 백엔드 서버 실행: `poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000`
- [ ] 프론트엔드 개발 서버 실행: `npm --prefix frontend run dev`
- [ ] 브라우저에서 `http://localhost:3000` 접속
- [ ] 3열 레이아웃 확인 (좌측 입력 패널 | 중앙 미리보기 | 우측 Export 패널)
- [ ] 레이아웃 반응형 동작 확인 (창 크기 조절)
- [ ] 상태 관리 동작 확인 (개발자 도구 React DevTools 사용)

### Phase 8.5: 입력 패널 컴포넌트 구현

**목표**: 파일 업로드 및 세션 메타 표시

**구현 계획**:
- [ ] `frontend/components/FileUpload.tsx` 생성
  - [ ] 드래그&드롭 기능
  - [ ] 파일 선택 기능
  - [ ] 파일 검증 (.md 확장자, 크기 제한)
  - [ ] 업로드 진행 상태 표시
  - [ ] 에러 메시지 표시
- [ ] `frontend/components/SessionMetaPreview.tsx` 생성
  - [ ] Session Meta 표시 (session_id, phase, subphase, exported_at 등)
  - [ ] Phase/Subphase 수동 입력 기능 (누락 시, 선택적)

**브라우저 확인**:
- [ ] 백엔드 서버 실행: `poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000`
- [ ] 프론트엔드 개발 서버 실행: `npm --prefix frontend run dev`
- [ ] 브라우저에서 `http://localhost:3000` 접속
- [ ] FileUpload 컴포넌트 확인:
  - [ ] 드래그&드롭 영역 표시 확인
  - [ ] 파일 선택 버튼 동작 확인
  - [ ] `.md` 파일 업로드 테스트 (실제 파일 사용: `docs/cursor_phase_6_3.md`)
  - [ ] 업로드 진행 상태 표시 확인
  - [ ] 에러 메시지 표시 확인 (잘못된 파일 형식, 크기 초과 등)
- [ ] SessionMetaPreview 컴포넌트 확인:
  - [ ] 파일 업로드 후 Session Meta 정보 표시 확인
  - [ ] Phase/Subphase 수동 입력 기능 확인 (필요 시)

### Phase 8.6: 결과 미리보기 컴포넌트 구현

**목표**: Timeline, Issues, Snippets 미리보기

**구현 계획**:
- [ ] `frontend/components/TimelinePreview.tsx` 생성
  - [ ] Timeline Section 리스트 표시
  - [ ] 각 Section의 이벤트 표시
  - [ ] 이슈 연결 표시 (has_issues, issue_refs)
  - [ ] 작업 결과 연결 정보 표시 (코드 스니펫, 파일, Artifact)
- [ ] `frontend/components/IssuesPreview.tsx` 생성
  - [ ] Issue Card 리스트 표시
  - [ ] 카드 클릭 시 상세 정보 표시 (증상, 원인, 조치, 검증)
  - [ ] 관련 스니펫 링크 표시
  - [ ] Timeline Section 연결 표시
- [ ] `frontend/components/SnippetsPreview.tsx` 생성
  - [ ] 언어별 필터 (sql/ts/py 등)
  - [ ] 스니펫 목록 표시 (snippet_id, 언어, 코드 일부)
  - [ ] 코드 접기/펼치기 기능
  - [ ] 스니펫 상세 조회 (API 호출)

**브라우저 확인**:
- [ ] 백엔드 서버 실행: `poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000`
- [ ] 프론트엔드 개발 서버 실행: `npm --prefix frontend run dev`
- [ ] 브라우저에서 `http://localhost:3000` 접속
- [ ] 파일 업로드 후 전체 파이프라인 실행 (파싱 → Timeline → Issues → Snippets)
- [ ] TimelinePreview 컴포넌트 확인:
  - [ ] Timeline Section 리스트 표시 확인
  - [ ] 각 Section의 이벤트 표시 확인
  - [ ] 이슈 연결 표시 확인 (has_issues, issue_refs)
  - [ ] 작업 결과 연결 정보 표시 확인 (코드 스니펫, 파일, Artifact)
- [ ] IssuesPreview 컴포넌트 확인:
  - [ ] Issue Card 리스트 표시 확인
  - [ ] 카드 클릭 시 상세 정보 표시 확인 (증상, 원인, 조치, 검증)
  - [ ] 관련 스니펫 링크 표시 확인
  - [ ] Timeline Section 연결 표시 확인
- [ ] SnippetsPreview 컴포넌트 확인:
  - [ ] 언어별 필터 동작 확인
  - [ ] 스니펫 목록 표시 확인
  - [ ] 코드 접기/펼치기 기능 확인
  - [ ] 스니펫 상세 조회 동작 확인 (API 호출)

### Phase 8.7: Export 패널 구현

**목표**: 다운로드 기능 구현

**구현 계획**:
- [ ] Export 패널 컴포넌트 생성 (`frontend/app/page.tsx` 내부 또는 별도 컴포넌트)
  - [ ] Timeline 다운로드 버튼 (JSON/MD 선택)
  - [ ] Issues 다운로드 버튼 (JSON/MD 선택)
  - [ ] 전체 다운로드 버튼 (ZIP)
  - [ ] 다운로드 진행 상태 표시
  - [ ] 파일명 생성 로직 (session_id 기반)

**브라우저 확인**:
- [ ] 백엔드 서버 실행: `poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000`
- [ ] 프론트엔드 개발 서버 실행: `npm --prefix frontend run dev`
- [ ] 브라우저에서 `http://localhost:3000` 접속
- [ ] 파일 업로드 후 전체 파이프라인 실행 완료
- [ ] Export 패널 확인:
  - [ ] Timeline 다운로드 버튼 동작 확인 (JSON/MD 선택)
  - [ ] Issues 다운로드 버튼 동작 확인 (JSON/MD 선택)
  - [ ] 전체 다운로드 버튼 동작 확인 (ZIP)
  - [ ] 다운로드 진행 상태 표시 확인
  - [ ] 다운로드된 파일명 확인 (session_id 기반)
  - [ ] 다운로드된 파일 내용 확인 (JSON/MD/ZIP 형식 검증)

### Phase 8.8: 환경 변수 설정

**목표**: API URL 등 환경 변수 설정

**구현 계획**:
- [ ] `frontend/.env.local` 생성 (또는 `.env.local.example`)
  - [ ] `NEXT_PUBLIC_API_URL=http://localhost:8000` 설정
- [ ] 환경 변수 사용 확인 (`frontend/lib/api.ts`)

**브라우저 확인**:
- [ ] 프론트엔드 개발 서버 재시작: `npm --prefix frontend run dev`
- [ ] 브라우저에서 `http://localhost:3000` 접속
- [ ] 환경 변수 적용 확인 (API 호출이 올바른 URL로 전송되는지 네트워크 탭에서 확인)
- [ ] API 연결 정상 동작 확인

### Phase 8.9: 스타일링 및 UX 개선

**목표**: 기본 스타일링 적용 (기능 우선)

**구현 계획**:
- [ ] Tailwind CSS 기본 스타일 적용
- [ ] 로딩 상태 표시 (스피너 또는 스켈레톤)
- [ ] 에러 메시지 표시 (토스트 또는 인라인)
- [ ] 반응형 디자인 (모바일 대응, 선택적)

**브라우저 확인**:
- [ ] 백엔드 서버 실행: `poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000`
- [ ] 프론트엔드 개발 서버 실행: `npm --prefix frontend run dev`
- [ ] 브라우저에서 `http://localhost:3000` 접속
- [ ] 전체 UI 스타일 확인:
  - [ ] Tailwind CSS 스타일 적용 확인
  - [ ] 로딩 상태 표시 확인 (파일 업로드, API 호출 중)
  - [ ] 에러 메시지 표시 확인 (파일 크기 초과, 잘못된 형식 등)
  - [ ] 반응형 디자인 확인 (창 크기 조절, 모바일 뷰)
- [ ] UX 개선 사항 확인:
  - [ ] 사용자 피드백 명확성 확인
  - [ ] 인터랙션 반응성 확인

### Phase 8.10: 통합 테스트 및 검증

**목표**: 프론트엔드-백엔드 통합 검증

**⚠️ 중요: 테스트 실행 검증 필수**
- ❌ 절대 금지: 테스트 파일만 작성하고 실행하지 않은 채 완료 보고
- ✅ 필수: 수동 테스트 시나리오 실행 및 결과 확인
- ✅ 필수: 완료 보고에 테스트 실행 결과 포함

**구현 계획**:
- [ ] 수동 테스트 시나리오 실행
  - [ ] 백엔드 서버 실행: `poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000` (프로젝트 루트에서)
  - [ ] 프론트엔드 개발 서버 실행: `npm --prefix frontend run dev` (프로젝트 루트에서)
  - [ ] 브라우저에서 `http://localhost:3000` 접속
  - [ ] 파일 업로드 → 파싱 → Timeline 생성 → Issues 생성 → Snippets 처리 → Export 전체 플로우 테스트
  - [ ] 각 단계별 결과 확인 (콘솔 로그, 네트워크 탭, 브라우저 화면)
  - [ ] 에러 처리 확인 (파일 크기 초과, 잘못된 형식 등)
- [ ] API contract 일치 확인
  - [ ] Query 파라미터 이름 일치 (`use_llm` snake_case) - 네트워크 탭에서 확인
  - [ ] Request/Response 타입 일치 - TypeScript 컴파일 오류 없음 확인
  - [ ] Enum 값 일치 (EventType, ExportFormat 등) - 실제 API 응답과 비교
  - [ ] Optional 필드 일치 - 백엔드 모델과 비교
- [ ] 테스트 결과 문서화
  - [ ] 테스트 실행 명령어 기록
  - [ ] 테스트 통과 상태 기록 (PASS / FAIL)
  - [ ] 발견된 문제점 및 해결 방법 기록

**브라우저 확인** (최종 통합 확인):
- [ ] 백엔드 서버 실행: `poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000`
- [ ] 프론트엔드 개발 서버 실행: `npm --prefix frontend run dev`
- [ ] 브라우저에서 `http://localhost:3000` 접속
- [ ] 전체 플로우 E2E 테스트:
  - [ ] 파일 업로드 (드래그&드롭 또는 파일 선택)
  - [ ] 파싱 완료 확인 (Session Meta 표시)
  - [ ] Timeline 생성 및 표시 확인
  - [ ] Issues 생성 및 표시 확인
  - [ ] Snippets 처리 및 표시 확인
  - [ ] Export 다운로드 동작 확인 (JSON/MD/ZIP)
- [ ] 사용자 피드백 수집:
  - [ ] UI/UX 개선 사항 확인
  - [ ] 버그 또는 문제점 확인
  - [ ] 기능 요청 사항 확인

**검증 체크리스트**:
- [ ] 모든 타입이 백엔드 모델과 1:1 매핑
- [ ] Enum 값이 문자열 리터럴로 정확히 일치
- [ ] Query 파라미터 이름이 snake_case로 일치 (`use_llm`)
- [ ] 필드명, 타입, Optional 여부 모두 일치
- [ ] Request/Response 스키마 일치
- [ ] 파일 업로드 및 파싱 동작
- [ ] Timeline 생성 및 표시
- [ ] Issues 생성 및 표시
- [ ] Snippets 처리 및 표시
- [ ] Export 다운로드 동작

**Phase 8 완료 시 필수 작업**:
1. Phase 8.10 통합 테스트 완료 (수동 테스트 시나리오 실행)
2. API contract 일치 확인 (타입, 필드명, Enum 값, Query 파라미터)
3. TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
4. `git add .` → `git commit -m "feat: Phase 8 완료 - 프론트엔드 UI 구현"` → `git push origin main`
5. 사용자 피드백 요청

---

## Phase 9: 통합 테스트 및 QA (미완료)

- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 8 진행 준비 (프론트엔드 UI 구현)

**마지막 업데이트**: 2025-12-28

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3: 이벤트 추출 및 정규화 (2025-12-20~26)
- Phase 4: Timeline 및 Issue Cards 생성 (2025-12-26~27)
- Phase 5: 코드 스니펫 분리 및 저장 (2025-12-27)
- Phase 6: LLM 호출 최적화 (2025-12-27~28)
- Phase 7: 백엔드 API 구현 (2025-12-28)

**다음 단계**:
- Phase 8.2 (API 클라이언트 구현) 진행 준비

**진행 중인 Phase**:
- Phase 8: 프론트엔드 UI 구현
  - ✅ Phase 8.1: 타입 정의 및 API Contract 동기화 (2025-12-28 완료)

---

## 참고: Archive

- **상세 내용**: `TODOs_archive_20251228.md` (Phase 1-7 상세 내용 포함)
- **이전 Archive**: `TODOs_archive_20251226.md`
