# Phase 5-1
_Exported on 12/29/2025 at 14:34:16 GMT+9 from Cursor (2.2.44)_

---

**User**

@TODOs.md 를 바탕으로 프로젝트의 현황 파악하고 계획 수립

---

**Cursor**

프로젝트 현황 파악을 위해 관련 파일 확인 중.


프로젝트 현황 파악 완료. Phase 5 진행 전, 몇 가지 확인이 필요합니다.


Phase 5 진행, snippets.json만 생성하는 범위로 계획 수립 중.


Phase 5 계획 수립 중.


---

**User**

다음을 설명하세요
1. Phase 5는 llm을 사용안하는거지요?
입력-처리-출력이 어떻게 되는지 설명해주세요.
2. 스니펫이 분리 및 저장되면,이것이 나중에 어떻게 활용되는지 설명해주세요.
제 이해는, timeline이나 section 그리고 이슈등에서 어떤 스니펫인지 내용을 필요로 할때 바로바로 보여줄 수 있어야 함
3. 이것이 파일로 저장이 안되면, 나중에 다시 실행할 때, 계속 다시 뽑아야 하나요? Phase 2,3,4의 생성물은 캐시가 되어 있긴 합니다. 이것들과 다른가요?

설명만 하고 사용자 지시 대기

---

**Cursor**

Phase 5의 세 가지 질문에 대해 확인 중입니다.


세 가지 질문에 대해 설명합니다.

## 1. Phase 5는 LLM을 사용하지 않습니다 (패턴 기반)

**입력-처리-출력 흐름**:

```
입력:
├── Turns (이미 파싱된 결과, Phase 2)
│   └── code_blocks: List[CodeBlock]  # 각 Turn에 포함된 코드 블록들
├── Events (이미 정규화된 결과, Phase 3)
├── IssueCards (이미 생성된 결과, Phase 4)
└── SessionMeta

처리 (패턴 기반, LLM 없음):
├── 1. CodeBlock → Snippet 변환
│   ├── snippet_id 생성: "SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang}"
│   ├── 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
│   └── 해시 생성: SHA-256(normalize(code))
│
├── 2. 중복 제거 (해시 기반)
│   ├── 동일한 해시를 가진 스니펫은 하나만 유지
│   └── 제거된 스니펫의 ID는 aliases에 추가
│
├── 3. 링킹
│   ├── Event.snippet_refs 업데이트 (turn_ref 매칭)
│   ├── IssueCard.snippet_refs 업데이트 (related_events → snippet_refs 수집)
│   └── Snippet.links 업데이트 (event_seq, issue_id)
│
└── 4. snippets.json 생성

출력:
├── snippets: List[Snippet]  # 분리된 스니펫 리스트
├── events: List[Event]  # snippet_refs가 업데이트된 이벤트
├── issue_cards: List[IssueCard]  # snippet_refs가 업데이트된 이슈 카드
└── snippets.json  # 전체 스니펫 데이터 (snippet_id, code, lang, links 등)
```

**LLM 미사용 이유**:
- 코드 추출: 이미 파서에서 완료
- ID 생성: 규칙 기반 (session_id, turn_index, block_index, lang)
- 언어 판별: fence_lang 또는 키워드 휴리스틱
- 중복 제거: 해시 기반 비교
- 링킹: Turn/Event 인덱스 매칭

## 2. 스니펫 활용 방식

스니펫은 ID 참조 방식으로 활용됩니다.

### 현재 구조

```python
# Event 모델
Event.snippet_refs: List[str]  # ["SNP-session-012-00-sql", "SNP-session-013-01-python"]

# IssueCard 모델  
IssueCard.snippet_refs: List[str]  # 이슈와 관련된 모든 스니펫 ID
IssueCard.fix[].snippet_refs: List[str]  # 각 fix 항목에 관련된 스니펫 ID

# TimelineEvent 모델
TimelineEvent.snippet_refs: List[str]  # 타임라인 이벤트와 관련된 스니펫 ID
```

### 활용 시나리오

**시나리오 1: Timeline/Section에서 코드 보기**
```
사용자가 Timeline Event #15 클릭
→ Event.snippet_refs = ["SNP-session-015-00-sql"]
→ snippets.json에서 snippet_id로 조회
→ 코드 내용 표시
```

**시나리오 2: Issue Card에서 Fix 코드 보기**
```
사용자가 Issue Card #3의 Fix 항목 클릭
→ IssueCard.fix[0].snippet_refs = ["SNP-session-020-01-python"]
→ snippets.json에서 snippet_id로 조회
→ 해결 방법 코드 표시
```

**시나리오 3: Phase 6 API (예상)**
```python
# GET /api/snippets/{snippet_id}
{
    "snippet_id": "SNP-session-015-00-sql",
    "lang": "sql",
    "code": "ALTER TABLE users ADD COLUMN ...",
    "source": {"turn_index": 15, "block_index": 0},
    "links": {"event_seq": 15, "issue_id": "ISS-003-1234"}
}
```

**핵심 포인트**:
- Timeline/Section/Issue는 코드를 직접 포함하지 않고 `snippet_refs`만 가짐
- 실제 코드는 `snippets.json`에서 `snippet_id`로 조회
- 필요 시 즉시 조회 가능 (snippets.json은 메모리에 로드 가능)

## 3. 파일 저장과 캐시의 관계

snippets.json은 Phase 2-4 캐시와 유사하게 영구 저장되며, 재실행 시 재추출이 필요하지 않습니다.

### Phase 2-4 캐시 시스템

```python
# backend/core/pipeline_cache.py
PIPELINE_CACHE_DIR = "cache/pipeline/"

# 저장되는 파일들:
- parsed_{file_hash}.json      # Phase 2: 파싱 결과
- events_{file_hash}_llm.json  # Phase 3: 이벤트 정규화 결과
- timeline_sections_{file_hash}_llm.json  # Phase 4: Timeline Section 결과
```

**캐시 동작**:
- 입력 파일 해시 기반 캐시 키 생성
- 파일 변경 감지 시 자동 무효화
- 같은 입력 파일이면 캐시 사용 (재실행 불필요)

### Phase 5 snippets.json 저장 전략

**옵션 1: 파이프라인 캐시에 포함 (권장)**
```python
# backend/core/pipeline_cache.py에 추가
def get_or_create_snippets(
    turns: List[Turn],
    events: List[Event],
    issue_cards: List[IssueCard],
    session_meta: SessionMeta,
    input_file: Path
) -> List[Snippet]:
    """
    스니펫 처리 결과 캐싱
    - 캐시 키: snippets_{file_hash}
    - 입력 파일 변경 시 자동 무효화
    """
```

**옵션 2: 별도 저장 (snippets.json만)**
```
# Phase 6 API에서 사용하는 경우
output/
  ├── snippets.json  # 영구 저장
  ├── timeline.json
  └── issues.json
```

**차이점 비교**:

| 항목 | Phase 2-4 캐시 | Phase 5 snippets.json |
|------|----------------|----------------------|
| 저장 위치 | `cache/pipeline/` | `output/` 또는 `cache/pipeline/` |
| 목적 | 중복 실행 방지 | 스니펫 참조 및 조회 |
| 무효화 | 입력 파일 변경 시 | 입력 파일 변경 시 (캐시 포함 시) |
| 재사용 | 다음 실행 시 재사용 | API 조회 시 사용 |

**추천 방식**:
- Phase 5에서는 파이프라인 캐시에 포함 (`cache/pipeline/snippets_{file_hash}.json`)
- Phase 6 API에서는 `snippets.json`을 output 디렉토리에 별도 저장
- 두 가지 모두 유지:
  - 캐시: 재실행 시 빠른 재사용
  - output: API 및 사용자 다운로드용

**결론**:
- snippets.json은 파일로 저장되므로 재추출이 필요하지 않습니다
- Phase 2-4 캐시와 동일한 방식으로 저장하면 재사용 가능합니다
- Phase 6에서 API 제공 시 별도 output 파일로도 저장할 수 있습니다

---

**요약**:
1. Phase 5는 패턴 기반 (LLM 미사용)
2. 스니펫은 ID 참조 방식으로 활용, snippets.json에서 조회
3. snippets.json은 파일로 저장되며, 캐시와 유사하게 재사용 가능

추가 질문이 있으면 알려주세요.

```plaintext
입력:
├── Turns (이미 파싱된 결과, Phase 2)
│   └── code_blocks: List[CodeBlock]  # 각 Turn에 포함된 코드 블록들
├── Events (이미 정규화된 결과, Phase 3)
├── IssueCards (이미 생성된 결과, Phase 4)
└── SessionMeta

처리 (패턴 기반, LLM 없음):
├── 1. CodeBlock → Snippet 변환
│   ├── snippet_id 생성: "SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang}"
│   ├── 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
│   └── 해시 생성: SHA-256(normalize(code))
│
├── 2. 중복 제거 (해시 기반)
│   ├── 동일한 해시를 가진 스니펫은 하나만 유지
│   └── 제거된 스니펫의 ID는 aliases에 추가
│
├── 3. 링킹
│   ├── Event.snippet_refs 업데이트 (turn_ref 매칭)
│   ├── IssueCard.snippet_refs 업데이트 (related_events → snippet_refs 수집)
│   └── Snippet.links 업데이트 (event_seq, issue_id)
│
└── 4. snippets.json 생성

출력:
├── snippets: List[Snippet]  # 분리된 스니펫 리스트
├── events: List[Event]  # snippet_refs가 업데이트된 이벤트
├── issue_cards: List[IssueCard]  # snippet_refs가 업데이트된 이슈 카드
└── snippets.json  # 전체 스니펫 데이터 (snippet_id, code, lang, links 등)
```

```python
# Event 모델
Event.snippet_refs: List[str]  # ["SNP-session-012-00-sql", "SNP-session-013-01-python"]

# IssueCard 모델  
IssueCard.snippet_refs: List[str]  # 이슈와 관련된 모든 스니펫 ID
IssueCard.fix[].snippet_refs: List[str]  # 각 fix 항목에 관련된 스니펫 ID

# TimelineEvent 모델
TimelineEvent.snippet_refs: List[str]  # 타임라인 이벤트와 관련된 스니펫 ID
```

```plaintext
사용자가 Timeline Event #15 클릭
→ Event.snippet_refs = ["SNP-session-015-00-sql"]
→ snippets.json에서 snippet_id로 조회
→ 코드 내용 표시
```

```plaintext
사용자가 Issue Card #3의 Fix 항목 클릭
→ IssueCard.fix[0].snippet_refs = ["SNP-session-020-01-python"]
→ snippets.json에서 snippet_id로 조회
→ 해결 방법 코드 표시
```

```python
# GET /api/snippets/{snippet_id}
{
    "snippet_id": "SNP-session-015-00-sql",
    "lang": "sql",
    "code": "ALTER TABLE users ADD COLUMN ...",
    "source": {"turn_index": 15, "block_index": 0},
    "links": {"event_seq": 15, "issue_id": "ISS-003-1234"}
}
```

```python
# backend/core/pipeline_cache.py
PIPELINE_CACHE_DIR = "cache/pipeline/"

# 저장되는 파일들:
- parsed_{file_hash}.json      # Phase 2: 파싱 결과
- events_{file_hash}_llm.json  # Phase 3: 이벤트 정규화 결과
- timeline_sections_{file_hash}_llm.json  # Phase 4: Timeline Section 결과
```

```python
# backend/core/pipeline_cache.py에 추가
def get_or_create_snippets(
    turns: List[Turn],
    events: List[Event],
    issue_cards: List[IssueCard],
    session_meta: SessionMeta,
    input_file: Path
) -> List[Snippet]:
    """
    스니펫 처리 결과 캐싱
    - 캐시 키: snippets_{file_hash}
    - 입력 파일 변경 시 자동 무효화
    """
```

```plaintext
# Phase 6 API에서 사용하는 경우
output/
  ├── snippets.json  # 영구 저장
  ├── timeline.json
  └── issues.json
```

---

**User**

자 다음 순서로 진행하세요

1. AGENTS.md와 커서룰을 바탕으로 프로젝트의 규칙을 확인하고, 이를 준수할 것을 스스로 확인
2. 위의 계획을 @TODOs.md 에 업데이트 할 것
3. @TODOs.md 를 바탕으로 단계적으로 진행

---

**Cursor**

AGENTS.md와 커서룰 확인 중. 이후 계획을 TODOs.md에 반영하고 단계별로 진행합니다.


규칙 확인 완료. Phase 5 계획을 TODOs.md에 반영 중.


```markdown
# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (필수)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

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

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**

프로젝트는 Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행합니다.
하지만 Phase 4나 Phase 5에서 문제가 발견되면 **Phase 3으로 돌아가서 이벤트 정규화 로직을 개선**한 후, 다시 Phase 4, 5로 넘어가는 iterative cycle을 돌고 있습니다.

**주의사항**:
- Phase 3, 4, 5의 **기본 순서는 항상 유지**: 3 → 4 → 5
- 개선 작업은 **Phase 3의 서브 Phase (3.1, 3.2, 3.4 등)**로 진행
- Phase 번호는 **절대 섞이지 않음** (3 → 4 → 3.4 → 5 ❌, 3 → 4 → 3.4 → 4 재검증 → 5 ✅)

### Phase 3.0: 기본 구현 (완료)

- ✅ 데이터 모델 정의 (EventType, Event, TimelineEvent, IssueCard)
- ✅ 이벤트 정규화 기본 구현 (규칙 기반 타입 분류)
- ✅ 단위 테스트 및 E2E 테스트 완료
- **발견된 문제점**: 이벤트 중복 생성, Summary 품질, 타입 분류 정확도

### Phase 3.1: 즉시 개선 (정규식 기반) - 완료

- ✅ 이벤트 중복 생성 방지 (117개 → 67개, 1:1 매핑 달성)
- ✅ Summary 품질 개선 (줄바꿈 정리, 의미 있는 위치에서 자르기)
- ✅ 타입 분류 엄격화 (구체적인 패턴 사용)

### Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료

- ✅ LLM 서비스 구현 (gpt-4.1-mini, 파일 기반 캐싱, `.env` 자동 로드)
- ✅ 이벤트 정규화 모듈에 LLM 옵션 추가 (`use_llm` 파라미터)
- ✅ LLM 기반 E2E 테스트 완료 (67개 Turn → 67개 Event, 1:1 매핑 달성)
- ✅ E2E 테스트 결과 분석 완료

**Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선** - 완료
- ✅ 병렬 처리 구현 (224초 → 44.99초, 약 5배 향상)
- ✅ 캐시 시스템 개선 (SHA-256 해시, 원자적 저장, 텍스트 해시 검증)
- ✅ 캐시 성능 검증: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상)

### Phase 3.3: 결과 평가 방법 구축 - 완료

- ✅ 정성적 평가 도구 구현 (`backend/builders/evaluation.py`)
- ✅ Golden 파일 관리 도구 구현
- ✅ 수동 검증 프로세스 실행 완료
- ⏸️ Golden 파일 생성: 보류 (Phase 3.4 완료 후 작성 예정)

### Phase 3.4: 이벤트 정규화 품질 개선 (Iterative Improvement Cycle)

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

**⚠️ 컨텍스트**: Phase 4 완료 후 문제 발견 → Phase 3으로 돌아온 개선 작업

**발견된 문제점**:
- Timeline: 이벤트 타입 분류 부정확, Summary 품질 낮음
- Issue Cards: Summary 품질 문제, Root cause/Fix/Validation 추출 품질 낮음

**완료된 작업**:
- [x] 수동 검증 파일 재작성 및 검증 (HTML 형식, 67개 이벤트)
- [x] 정량적/정성적 분석 완료 (타입 분류 정확도 62.69%, 문제 패턴 분류)
- [x] 문제 원인 분석 및 개선 방안 도출
- [x] 개선 작업 실행 (Type 추출 로직, Summary 로직, LLM 프롬프트 개선)
- [x] **타입 체계 개선 구현 완료** (2025-12-26)
  - [x] EventType.ARTIFACT 제거, EventType.CODE_GENERATION 추가
  - [x] ArtifactAction Enum 추가
  - [x] 분류 로직 개선 (is_code_generation_turn, create_code_generation_event)
  - [x] LLM 프롬프트 수정
  - [x] 평가 도구 업데이트
  - [x] E2E 테스트 재실행 및 검증 완료

**상세 개선 계획**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 참조

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**⚠️ 참고**: E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)**로 돌아가서 개선 작업을 수행한 후 다시 Phase 4 E2E 테스트를 재실행합니다

### 기본 구현 - 완료

- ✅ Timeline 빌더 구현 (`build_timeline()`)
- ✅ Issue Cards 빌더 구현 (`build_issue_cards()`)
  - DebugEvent 기반 이슈 탐지, 슬라이딩 윈도우 그룹화
  - Symptom/Root cause/Fix/Validation 추출 (패턴 기반)
- ✅ 단위 테스트 및 E2E 테스트 완료 (구조적 정합성 검증 완료)

**⚠️ E2E 테스트 상태**:
- 구조적 정합성 검증 완료 (테스트 통과)
- 실제 내용 품질 검증은 미완료 (Phase 4.5, 4.6에서 개선 예정)

### Phase 4.5: Timeline 구조화 개선 (진행 중)

**목표**: Timeline을 단순 나열에서 구조화된 작업 항목별 그룹으로 개선

**발견된 문제점**:
- Timeline이 단순히 Event를 seq 1, 2, 3... 순서로 나열
- 주요 작업 내용이 항목화되지 않음
- 작업 내용 중 이슈 발생 여부 표시 안 됨
- 작업 결과 연결 정보 부족

**개선 목표**:
1. Phase/Subphase별로 주요 작업 항목 추출 및 항목화 (1, 2, 3, 4...)
2. 각 항목의 작업 내용 명확화 (LLM 기반 또는 패턴 기반)
3. 작업 내용 중 이슈 발생 여부 표시 (Issue Card와 연결)
4. 작업 결과 연결 정보 추가 (코드 스니펫, 파일, Git commit 등)

**구현 계획**:
- [x] Timeline 구조화 모델 정의 (`TimelineSection` 모델 추가)
- [x] Timeline 구조화 빌더 구현 (`build_structured_timeline()`)
  - [x] Phase/Subphase별 그룹화 로직
  - [x] 주요 작업 항목 추출 로직 (패턴 기반, LLM 옵션 추가 예정)
  - [x] 이슈 연결 로직
  - [x] 작업 결과 연결 정보 추출 로직
- [x] LLM 기반 작업 항목 추출 (선택적) (2025-12-26 완료)
  - [x] LLM 프롬프트 설계 및 캐싱 로직 적용
  - [x] extract_main_tasks_with_llm() 함수 구현
  - [x] timeline_builder에 use_llm 파라미터 통합
- [x] 테스트 작성 및 E2E 테스트 업데이트 (2025-12-26 완료)
  - [x] 단위 테스트 작성 (test_structured_timeline_pattern_based, test_structured_timeline_llm_based)
  - [x] E2E 테스트 업데이트 (test_timeline_issues_e2e_with_llm에서 build_structured_timeline 사용)
  - [x] E2E 테스트 실행 완료 (7개 sections 생성, 패턴 기반 fallback 사용)

**Timeline 품질 평가 및 수동 검증** (2025-12-26 완료):
- [x] E2E 테스트 결과 분석 (결과 파일: `tests/timeline_issues_e2e_llm_20251226_130658.json`)
  - Timeline Section 개수 및 구조 분석 (7개 섹션, 67개 이벤트)
  - Section 제목/요약 품질 평가 (제목 품질 문제 발견: 모든 제목이 이벤트 타입만 나열)
  - 이슈 연결 정확성 검증 (100% 연결률)
  - 작업 결과 연결 정보 완성도 확인 (85.7% 섹션에 코드 스니펫/파일/Artifact 포함)
- [x] Timeline 품질 평가 리포트 생성 (`tests/reports/timeline_quality_evaluation.json`)
- [x] 수동 검증 및 개선점 도출 (`tests/reports/timeline_quality_analysis.md`)
  - **주요 발견사항**: 제목 품질 문제 (7개 섹션 모두), Artifact 중복 문제 (4개 섹션)
  - **품질 점수**: 45/100
  - **개선 권장사항**: 제목 생성 로직 개선, Artifact 중복 제거

**산출물**: 구조화된 Timeline 모델, Timeline 구조화 빌더, E2E 테스트 완료 및 검증 리포트, Timeline 품질 평가 리포트

### Phase 4.6: Issue Card 품질 개선 (완료)

**목표**: Issue Card의 symptom → root_cause → fix → validation 체인을 LLM 기반으로 개선하여 내용 품질 향상

**발견된 문제점** (개선 전):
- Symptom: 단순히 Turn body 처음 500자 잘라내기
- Root cause: 패턴 매칭으로 텍스트 잘라내기 (중간 과정 텍스트 포함)
- Fix: DebugEvent의 summary만 사용 (구체적이지 않음)
- Validation: 패턴 매칭으로 텍스트 잘라내기 (불완전한 텍스트)

**개선 결과** (2025-12-26):
- Symptom: 평균 길이 82.5자 → 23.5자 (약 3.5배 개선, 핵심만 추출)
- Fix: 2개 → 12개 (6배 증가, 구체적이고 상세한 해결 방법)
- Validation: 명확하고 구체적인 검증 방법 추출
- Root cause: 프롬프트 개선 완료 (중간 과정 텍스트 제거 지시 추가)
- 품질 점수: 94/100
- 디버그 부분을 각 이슈로 나누는 로직 점검 필요

**구현 계획**:
- [x] LLM 기반 추출 함수 구현 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`) (2025-12-26 완료)
  - 각 함수는 캐싱 로직 적용 (SHA-256 해시 기반)
  - Fallback 로직 유지 (LLM 실패 시 패턴 기반)
  - 재시도 로직 적용 (최대 3회, 지수 백오프)
- [x] Issue Builder에 LLM 기반 추출 통합 (`build_issue_cards()` 함수에 `use_llm` 파라미터 추가) (2025-12-26 완료)
- [x] E2E 테스트 업데이트 및 실행 완료 (2025-12-26 완료)
  - LLM 기반 Issue Card 생성 검증 완료
  - 품질 분석 완료 (품질 점수: 94/100)
- [x] Root cause 프롬프트 개선 (중간 과정 텍스트 제거) (2025-12-26 완료)
- [ ] 디버그 이슈 분리 로직 개선 (논리적 이슈 단위로 클러스터링) (선택적, 추후 개선)
- [ ] 단위 테스트 작성 (`tests/test_issues_builder.py`) (선택적, 추후 개선)

### Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토 (진행 중)

**목표**: 
1. 파이프라인 중간 결과를 Fixture와 파일 캐싱으로 관리하여 중복 실행 제거
2. Timeline Section을 Issue Card 생성에 활용
3. Issue Card 생성 로직 전면 재검토 및 개선

**발견된 문제점**:
- 각 테스트가 독립적으로 파싱/이벤트 정규화 재실행 (비효율)
- Timeline Section 생성이 Issue Card 생성 이후에 실행됨
- Timeline Section을 Issue Card에 활용할 수 없음
- Issue Card 품질 문제: LLM이 제대로 적용되지 않은 것으로 보임
  - Root cause에 중간 과정 텍스트 포함
  - Fix summary가 형식적이고 부자연스러움
  - Symptom이 핵심이 아닌 경우 발생
- 각 컴포넌트(symptom, root_cause, fix, validation)가 독립적으로 작동하여 컨텍스트 부족

**⚠️ Phase 4.7 완료 후 발견된 심각한 문제점 (2025-12-26)**:
- **Issue Card 결과가 완전히 엉망**: 사용자 평가 "100점 만점에 -100점"
- **핵심 문제**:
  1. **`extract_issue_with_llm()` 함수가 구현되어 있지만 사용되지 않음**
     - `build_issue_card_from_cluster()` 함수가 각 컴포넌트를 개별적으로 추출
     - 통합 컨텍스트를 활용하지 못함
  2. **Fix 항목이 20개나 생성됨** (각 이벤트마다 하나씩)
     - `extract_fix_with_llm()` 함수가 각 DEBUG 이벤트마다 개별 호출됨
     - 각 fix가 매우 길고 반복적인 템플릿 문구 포함 ("이벤트 요약에 기반하여 구체적인 해결 방법을 추출하고 설명하겠습니다.")
  3. **Symptom이 너무 짧고 구체적이지 않음**
     - "다음 단계" 같은 의미 없는 텍스트만 추출됨
  4. **Title이 잘림**
     - 제목 생성 로직에 문제가 있거나 길이 제한이 너무 짧음
  5. **LLM은 사용되었지만 프롬프트/로직 문제**
     - 캐시 파일 확인 결과 LLM 호출은 정상적으로 이루어짐
     - 하지만 프롬프트가 각 컴포넌트를 개별적으로 요청하여 컨텍스트 부족
     - `extract_issue_with_llm()` 함수가 구현되어 있지만 실제로 호출되지 않음
- **확인된 사항**:
  - LLM 캐시 파일 존재: `cache/issue_*.json` (92개 파일)
  - LLM 호출은 정상적으로 이루어짐 (캐시 히트율 32.84%)
  - 문제는 로직 구조: 통합 컨텍스트를 활용하지 않고 각 컴포넌트를 개별 추출
- **필요한 개선**:
  1. `build_issue_card_from_cluster()` 함수를 `extract_issue_with_llm()` 사용하도록 수정
  2. 각 이벤트마다 개별 fix 추출 대신, 클러스터 전체에 대한 통합 fix 추출
  3. Symptom 추출 프롬프트 개선 (핵심만 추출하도록)
  4. Title 생성 로직 개선 (길이 제한 확대 또는 더 나은 요약)
  5. 통합 컨텍스트(TimelineSection + Events + Turns)를 활용한 일관성 있는 추출

**개선 방향**:
1. **파이프라인 데이터 관리**: 하이브리드 방식 (Fixture + 파일 캐싱)
   - pytest Fixture로 메모리 기반 공유 (빠른 접근)
   - 파일 기반 캐싱으로 영구 저장 (디버깅, 수동 검증)
2. **Issue Card 생성 로직 전면 재검토**:
   - 입력: TimelineSection + 관련 Events + 관련 Turns (통합 컨텍스트)
   - LLM 프롬프트: 구조화된 출력 (현상-원인-개선내용)
   - 출력: 구조화된 IssueCard (Timeline Section과 연결)
3. **이슈 클러스터링**: DEBUG 타입 이벤트 주변 Turn들을 논리적 이슈 단위로 클러스터링

**구현 계획**:

**Phase 4.7.1: 중간 결과 캐싱 모듈 생성**
- [ ] `backend/core/pipeline_cache.py` 생성
  - 파싱 결과 캐싱 (파일 기반)
  - 이벤트 정규화 결과 캐싱 (파일 기반)
  - Timeline Section 결과 캐싱 (파일 기반)
  - 캐시 키 생성 (입력 파일 해시 + use_llm 플래그)
  - 캐시 무효화 전략 (입력 파일 변경 감지)

**Phase 4.7.2: pytest Fixture 추가**
- [ ] `tests/conftest.py`에 Fixture 추가
  - `parsed_data` fixture (세션 스코프)
  - `normalized_events` fixture (세션 스코프, use_llm 파라미터)
  - `timeline_sections` fixture (세션 스코프, use_llm 파라미터)
  - 각 Fixture는 pipeline_cache 모듈 사용

**Phase 4.7.3: Issue Card 생성 로직 개선** - ✅ 완료 (2025-12-27)
- [x] `backend/builders/issues_builder.py` 수정
  - [x] `build_issue_cards()` 함수 시그니처 변경: `timeline_sections` 파라미터 추가
  - [x] DEBUG 이벤트 클러스터링 로직 구현 (논리적 이슈 단위로 그룹화)
  - [x] Timeline Section과 Issue Card 매칭 로직 구현
  - [x] **`build_issue_card_from_cluster()` 함수 수정**:
    - [x] 개별 추출 함수 호출 제거 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`)
    - [x] `extract_issue_with_llm()` 한 번 호출로 통합 (통합 컨텍스트 기반)
    - [x] 모든 필드에 fallback 적용 (일관성):
      - `title`: `generate_issue_title_from_cluster()` 사용
      - `symptom`: 첫 번째 User Turn 사용
      - `root_cause`: 패턴 기반 추출
      - `fix`: 패턴 기반 추출
      - `validation`: 패턴 기반 추출
  - [x] **`build_issue_card_from_window()` 함수 수정**:
    - [x] window를 클러스터로 변환하여 `extract_issue_with_llm()` 사용
    - [x] 개별 추출 함수 호출 제거
    - [x] 모든 필드에 fallback 적용 (동일한 전략)

**Phase 4.7.4: LLM 서비스 리팩토링 및 통합** - ✅ 완료 (2025-12-27)
- [x] `backend/core/constants.py` 수정
  - [x] `LLM_MODEL = "gpt-4.1-mini"` 상수 추가 (커서룰에 맞춰 통일)
- [x] `backend/core/llm_service.py` 수정
  - [x] **공통 LLM 호출 함수 추출**: `_call_llm_with_retry()` 함수 생성
    - 캐시 확인/저장 로직 통합
    - 재시도 로직 (지수 백오프) 통합
    - 예외 처리 및 fallback 통합
  - [x] **모든 함수에서 `LLM_MODEL` 상수 사용**: 하드코딩된 모델명 제거
  - [x] **`extract_issue_with_llm()` 함수 개선**:
    - 반환값에 `title` 필드 추가 (필수)
    - 프롬프트에 title 생성 규칙 추가
    - 반환 구조: `{"title": str, "symptom": str, "root_cause": dict, "fix": dict, "validation": str}`
  - [x] **개별 추출 함수 제거**:
    - `extract_symptom_with_llm()` 제거
    - `extract_root_cause_with_llm()` 제거
    - `extract_fix_with_llm()` 제거
    - `extract_validation_with_llm()` 제거
  - 참고: 모든 LLM 호출 함수에서 `_call_llm_with_retry()` 사용 (향후 리팩토링 가능)

**Phase 4.7.5: IssueCard 모델 확장**
- [ ] `backend/core/models.py` 수정
  - `IssueCard` 모델에 필드 추가:
    - `section_id: Optional[str]` - 연결된 Timeline Section ID
    - `section_title: Optional[str]` - 연결된 Timeline Section 제목
    - `related_events: List[str]` - 관련 Event ID 리스트
    - `related_turns: List[int]` - 관련 Turn 인덱스 리스트
    - `confidence_score: Optional[float]` - 추출 신뢰도 점수

**Phase 4.7.6: 테스트 코드 수정**
- [ ] `tests/test_timeline_issues_e2e.py` 수정
  - Fixture 사용으로 변경 (parsed_data, normalized_events, timeline_sections)
  - 실행 순서 변경: Timeline Section 생성 → Issue Card 생성
  - 새로운 Issue Card 생성 로직 검증

**Phase 4.7.7: 캐시 무효화 전략 구현** - ✅ 완료 (이전 Phase에서 완료됨)
- [x] `backend/core/pipeline_cache.py`에 무효화 로직 추가
  - [x] 입력 파일 변경 감지 (파일 해시 비교) - 각 함수에서 자동 구현됨
  - [x] 자동 무효화 (캐시 키 기반) - 파일 해시 불일치 시 자동 무효화
  - [x] 수동 무효화 옵션 (테스트용) - `invalidate_cache()` 함수 구현됨

**검증 계획**:
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 캐시 동작 확인 (파일 저장/로드)
  - [x] 실행 순서 확인 (Timeline → Issue)
  - [x] 성능 개선 확인 (중복 실행 제거)
  - [x] 하위 호환성 확인 (기존 테스트 통과)
- [x] Issue Card 품질 평가 (2025-12-27 완료)
  - [x] 새로운 로직으로 생성된 Issue Card 품질 분석
    - **핵심 개선 사항 확인**:
      - Fix 항목: 20개 → 1개 (클러스터당, 95% 감소) ✅
      - Title: LLM 생성으로 품질 향상 ✅
      - Symptom: 구체적이고 명확함 ✅
      - Root Cause: 중간 과정 텍스트 제거, 핵심만 포함 ✅
      - Fix: 통합 컨텍스트 기반으로 구체적이고 명확함 ✅
      - Validation: 구체적인 검증 방법 제시 ✅
  - [x] Timeline Section 연결 정확성 검증 (100% 연결률) ✅
  - [x] LLM 적용 여부 확인 (2회 호출, 클러스터당 1회) ✅

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

**⚠️ 중요**: Phase 5는 패턴 기반 처리입니다 (LLM 미사용)
- 스니펫 ID 생성: 규칙 기반 (SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang})
- 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
- 중복 제거: 해시 기반 (SHA-256)
- 링킹: Turn/Event 인덱스 매칭

**입력-처리-출력**:
```
입력: Turns (code_blocks), Events, IssueCards, SessionMeta
처리: CodeBlock → Snippet 변환 → 중복 제거 → 링킹 → snippets.json 생성
출력: snippets.json, 업데이트된 Events/IssueCards (snippet_refs 포함)
```

**구현 계획**:

**Phase 5.1: Snippet 모델 정의**
- [ ] `backend/core/models.py`에 Snippet 모델 추가
  - snippet_id, lang, code, source, links, snippet_hash, aliases 필드

**Phase 5.2: 스니펫 관리 모듈 구현**
- [ ] `backend/builders/snippet_manager.py` 생성
  - [ ] 스니펫 ID 생성 함수 (generate_snippet_id)
  - [ ] 코드 정규화 및 해시 생성 함수 (normalize_code, generate_snippet_hash)
  - [ ] 언어 판별 함수 (detect_language, fence_lang 우선 → 휴리스틱)
  - [ ] CodeBlock → Snippet 변환 함수 (code_blocks_to_snippets)
  - [ ] 중복 제거 로직 (deduplicate_snippets, 해시 기반)
  - [ ] 링킹 로직 (link_snippets_to_events, link_snippets_to_issues)
  - [ ] 통합 처리 함수 (process_snippets)

**Phase 5.3: 스니펫 저장 모듈 구현**
- [ ] `backend/builders/snippet_storage.py` 생성
  - [ ] snippets.json 생성 함수 (generate_snippets_json)

**Phase 5.4: 파이프라인 캐싱 통합 (선택적)**
- [ ] `backend/core/pipeline_cache.py`에 스니펫 캐싱 추가 (선택적)
  - [ ] get_or_create_snippets() 함수 추가

**Phase 5.5: 테스트 작성**
- [ ] `tests/test_snippet_manager.py` 작성 (단위 테스트)
  - [ ] test_generate_snippet_id()
  - [ ] test_normalize_code()
  - [ ] test_generate_snippet_hash()
  - [ ] test_detect_language()
  - [ ] test_code_blocks_to_snippets()
  - [ ] test_deduplicate_snippets()
  - [ ] test_link_snippets_to_events()
  - [ ] test_link_snippets_to_issues()
- [ ] `tests/test_snippet_e2e.py` 작성 (E2E 테스트)
  - [ ] test_snippet_e2e_with_llm() - 전체 파이프라인 통합 테스트
    - 실제 입력 파일 사용 (docs/cursor_phase_6_3.md)
    - 파싱 → 이벤트 정규화 → Timeline → Issue Cards → 스니펫 처리
    - snippets.json 생성 및 검증
    - Event/IssueCard 링킹 검증

**검증 계획**:
- [ ] 단위 테스트 실행 및 통과 확인
- [ ] E2E 테스트 실행 및 검증
  - 스니펫 ID 형식 검증
  - 중복 제거 검증 (해시 기반)
  - Event 링킹 검증 (Event.snippet_refs)
  - Issue Card 링킹 검증 (IssueCard.snippet_refs)
  - snippets.json 구조 검증
- [ ] E2E 테스트 결과 분석 및 리포트 생성

---

## Phase 6-8: 미완료 (간략 요약)

### Phase 6: 백엔드 API 구현
- [ ] FastAPI 엔드포인트 구현 (파싱, Timeline, Issues, Snippets, Export)
- [ ] Markdown 렌더러 구현
- [ ] 테스트 및 E2E 테스트 (실제 서버 실행)

### Phase 7: 프론트엔드 UI 구현
- [ ] Next.js 기반 웹 UI (메인 페이지, 입력 패널, 결과 미리보기, Export 패널)
- [ ] API 클라이언트 및 타입 정의
- [ ] 스타일링 (Tailwind CSS)

### Phase 8: 통합 테스트 및 QA
- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 4.7 완료, Phase 5 진행 예정 (코드 스니펫 분리 및 저장)

**마지막 업데이트**: 2025-12-27

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3.0-3.3: 이벤트 정규화 기본 구현 및 평가 방법 구축 (2025-12-20~23)
- Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선 (2025-12-23~26)
  - 타입 체계 개선 완료 (CODE_GENERATION 추가, ARTIFACT 제거)
- Phase 4: Timeline 및 Issue Cards 생성 기본 구현 (2025-12-26)
  - LLM 기반 E2E 테스트 완료
- Phase 4.5: Timeline 구조화 개선 및 품질 평가 (2025-12-26)
  - Timeline 품질 평가 완료 (품질 점수: 45/100)
- Phase 4.6: Issue Card 품질 개선 (2025-12-26)
  - LLM 기반 추출 함수 구현 완료
  - E2E 테스트 완료 (품질 점수: 94/100, 하지만 실제 품질 문제 발견)
- Phase 4.7.3-4.7.4: Issue Card 생성 로직 개선 및 LLM 서비스 리팩토링 (2025-12-27 완료)
  - `extract_issue_with_llm()` 통합 함수 사용으로 전환
  - 모든 필드에 일관된 fallback 적용
  - LLM 모델 통일 (`gpt-4.1-mini`)
  - 개별 추출 함수 제거 (539줄 삭제)
  - E2E 테스트 완료: Fix 항목 20개 → 1개 (95% 감소), 품질 대폭 향상

**진행 중인 Phase**:
- Phase 4.7.7: 캐시 무효화 전략 구현 (진행 예정)
  - 입력 파일 변경 감지 (파일 해시 비교)
  - 자동 무효화 (캐시 키 기반)
  - 수동 무효화 옵션 (테스트용)

**다음 단계**:
- Phase 4.7 완료 후 Phase 5 진행 예정
  - Phase 4.7 완료 후 사용자 피드백 대기

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.

```

```markdown
**현재 Phase**: Phase 5 진행 중 (코드 스니펫 분리 및 저장)

**마지막 업데이트**: 2025-12-27
```

```markdown
# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (필수)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

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

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**

프로젝트는 Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행합니다.
하지만 Phase 4나 Phase 5에서 문제가 발견되면 **Phase 3으로 돌아가서 이벤트 정규화 로직을 개선**한 후, 다시 Phase 4, 5로 넘어가는 iterative cycle을 돌고 있습니다.

**주의사항**:
- Phase 3, 4, 5의 **기본 순서는 항상 유지**: 3 → 4 → 5
- 개선 작업은 **Phase 3의 서브 Phase (3.1, 3.2, 3.4 등)**로 진행
- Phase 번호는 **절대 섞이지 않음** (3 → 4 → 3.4 → 5 ❌, 3 → 4 → 3.4 → 4 재검증 → 5 ✅)

### Phase 3.0: 기본 구현 (완료)

- ✅ 데이터 모델 정의 (EventType, Event, TimelineEvent, IssueCard)
- ✅ 이벤트 정규화 기본 구현 (규칙 기반 타입 분류)
- ✅ 단위 테스트 및 E2E 테스트 완료
- **발견된 문제점**: 이벤트 중복 생성, Summary 품질, 타입 분류 정확도

### Phase 3.1: 즉시 개선 (정규식 기반) - 완료

- ✅ 이벤트 중복 생성 방지 (117개 → 67개, 1:1 매핑 달성)
- ✅ Summary 품질 개선 (줄바꿈 정리, 의미 있는 위치에서 자르기)
- ✅ 타입 분류 엄격화 (구체적인 패턴 사용)

### Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료

- ✅ LLM 서비스 구현 (gpt-4.1-mini, 파일 기반 캐싱, `.env` 자동 로드)
- ✅ 이벤트 정규화 모듈에 LLM 옵션 추가 (`use_llm` 파라미터)
- ✅ LLM 기반 E2E 테스트 완료 (67개 Turn → 67개 Event, 1:1 매핑 달성)
- ✅ E2E 테스트 결과 분석 완료

**Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선** - 완료
- ✅ 병렬 처리 구현 (224초 → 44.99초, 약 5배 향상)
- ✅ 캐시 시스템 개선 (SHA-256 해시, 원자적 저장, 텍스트 해시 검증)
- ✅ 캐시 성능 검증: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상)

### Phase 3.3: 결과 평가 방법 구축 - 완료

- ✅ 정성적 평가 도구 구현 (`backend/builders/evaluation.py`)
- ✅ Golden 파일 관리 도구 구현
- ✅ 수동 검증 프로세스 실행 완료
- ⏸️ Golden 파일 생성: 보류 (Phase 3.4 완료 후 작성 예정)

### Phase 3.4: 이벤트 정규화 품질 개선 (Iterative Improvement Cycle)

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

**⚠️ 컨텍스트**: Phase 4 완료 후 문제 발견 → Phase 3으로 돌아온 개선 작업

**발견된 문제점**:
- Timeline: 이벤트 타입 분류 부정확, Summary 품질 낮음
- Issue Cards: Summary 품질 문제, Root cause/Fix/Validation 추출 품질 낮음

**완료된 작업**:
- [x] 수동 검증 파일 재작성 및 검증 (HTML 형식, 67개 이벤트)
- [x] 정량적/정성적 분석 완료 (타입 분류 정확도 62.69%, 문제 패턴 분류)
- [x] 문제 원인 분석 및 개선 방안 도출
- [x] 개선 작업 실행 (Type 추출 로직, Summary 로직, LLM 프롬프트 개선)
- [x] **타입 체계 개선 구현 완료** (2025-12-26)
  - [x] EventType.ARTIFACT 제거, EventType.CODE_GENERATION 추가
  - [x] ArtifactAction Enum 추가
  - [x] 분류 로직 개선 (is_code_generation_turn, create_code_generation_event)
  - [x] LLM 프롬프트 수정
  - [x] 평가 도구 업데이트
  - [x] E2E 테스트 재실행 및 검증 완료

**상세 개선 계획**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 참조

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**⚠️ 참고**: E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)**로 돌아가서 개선 작업을 수행한 후 다시 Phase 4 E2E 테스트를 재실행합니다

### 기본 구현 - 완료

- ✅ Timeline 빌더 구현 (`build_timeline()`)
- ✅ Issue Cards 빌더 구현 (`build_issue_cards()`)
  - DebugEvent 기반 이슈 탐지, 슬라이딩 윈도우 그룹화
  - Symptom/Root cause/Fix/Validation 추출 (패턴 기반)
- ✅ 단위 테스트 및 E2E 테스트 완료 (구조적 정합성 검증 완료)

**⚠️ E2E 테스트 상태**:
- 구조적 정합성 검증 완료 (테스트 통과)
- 실제 내용 품질 검증은 미완료 (Phase 4.5, 4.6에서 개선 예정)

### Phase 4.5: Timeline 구조화 개선 (진행 중)

**목표**: Timeline을 단순 나열에서 구조화된 작업 항목별 그룹으로 개선

**발견된 문제점**:
- Timeline이 단순히 Event를 seq 1, 2, 3... 순서로 나열
- 주요 작업 내용이 항목화되지 않음
- 작업 내용 중 이슈 발생 여부 표시 안 됨
- 작업 결과 연결 정보 부족

**개선 목표**:
1. Phase/Subphase별로 주요 작업 항목 추출 및 항목화 (1, 2, 3, 4...)
2. 각 항목의 작업 내용 명확화 (LLM 기반 또는 패턴 기반)
3. 작업 내용 중 이슈 발생 여부 표시 (Issue Card와 연결)
4. 작업 결과 연결 정보 추가 (코드 스니펫, 파일, Git commit 등)

**구현 계획**:
- [x] Timeline 구조화 모델 정의 (`TimelineSection` 모델 추가)
- [x] Timeline 구조화 빌더 구현 (`build_structured_timeline()`)
  - [x] Phase/Subphase별 그룹화 로직
  - [x] 주요 작업 항목 추출 로직 (패턴 기반, LLM 옵션 추가 예정)
  - [x] 이슈 연결 로직
  - [x] 작업 결과 연결 정보 추출 로직
- [x] LLM 기반 작업 항목 추출 (선택적) (2025-12-26 완료)
  - [x] LLM 프롬프트 설계 및 캐싱 로직 적용
  - [x] extract_main_tasks_with_llm() 함수 구현
  - [x] timeline_builder에 use_llm 파라미터 통합
- [x] 테스트 작성 및 E2E 테스트 업데이트 (2025-12-26 완료)
  - [x] 단위 테스트 작성 (test_structured_timeline_pattern_based, test_structured_timeline_llm_based)
  - [x] E2E 테스트 업데이트 (test_timeline_issues_e2e_with_llm에서 build_structured_timeline 사용)
  - [x] E2E 테스트 실행 완료 (7개 sections 생성, 패턴 기반 fallback 사용)

**Timeline 품질 평가 및 수동 검증** (2025-12-26 완료):
- [x] E2E 테스트 결과 분석 (결과 파일: `tests/timeline_issues_e2e_llm_20251226_130658.json`)
  - Timeline Section 개수 및 구조 분석 (7개 섹션, 67개 이벤트)
  - Section 제목/요약 품질 평가 (제목 품질 문제 발견: 모든 제목이 이벤트 타입만 나열)
  - 이슈 연결 정확성 검증 (100% 연결률)
  - 작업 결과 연결 정보 완성도 확인 (85.7% 섹션에 코드 스니펫/파일/Artifact 포함)
- [x] Timeline 품질 평가 리포트 생성 (`tests/reports/timeline_quality_evaluation.json`)
- [x] 수동 검증 및 개선점 도출 (`tests/reports/timeline_quality_analysis.md`)
  - **주요 발견사항**: 제목 품질 문제 (7개 섹션 모두), Artifact 중복 문제 (4개 섹션)
  - **품질 점수**: 45/100
  - **개선 권장사항**: 제목 생성 로직 개선, Artifact 중복 제거

**산출물**: 구조화된 Timeline 모델, Timeline 구조화 빌더, E2E 테스트 완료 및 검증 리포트, Timeline 품질 평가 리포트

### Phase 4.6: Issue Card 품질 개선 (완료)

**목표**: Issue Card의 symptom → root_cause → fix → validation 체인을 LLM 기반으로 개선하여 내용 품질 향상

**발견된 문제점** (개선 전):
- Symptom: 단순히 Turn body 처음 500자 잘라내기
- Root cause: 패턴 매칭으로 텍스트 잘라내기 (중간 과정 텍스트 포함)
- Fix: DebugEvent의 summary만 사용 (구체적이지 않음)
- Validation: 패턴 매칭으로 텍스트 잘라내기 (불완전한 텍스트)

**개선 결과** (2025-12-26):
- Symptom: 평균 길이 82.5자 → 23.5자 (약 3.5배 개선, 핵심만 추출)
- Fix: 2개 → 12개 (6배 증가, 구체적이고 상세한 해결 방법)
- Validation: 명확하고 구체적인 검증 방법 추출
- Root cause: 프롬프트 개선 완료 (중간 과정 텍스트 제거 지시 추가)
- 품질 점수: 94/100
- 디버그 부분을 각 이슈로 나누는 로직 점검 필요

**구현 계획**:
- [x] LLM 기반 추출 함수 구현 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`) (2025-12-26 완료)
  - 각 함수는 캐싱 로직 적용 (SHA-256 해시 기반)
  - Fallback 로직 유지 (LLM 실패 시 패턴 기반)
  - 재시도 로직 적용 (최대 3회, 지수 백오프)
- [x] Issue Builder에 LLM 기반 추출 통합 (`build_issue_cards()` 함수에 `use_llm` 파라미터 추가) (2025-12-26 완료)
- [x] E2E 테스트 업데이트 및 실행 완료 (2025-12-26 완료)
  - LLM 기반 Issue Card 생성 검증 완료
  - 품질 분석 완료 (품질 점수: 94/100)
- [x] Root cause 프롬프트 개선 (중간 과정 텍스트 제거) (2025-12-26 완료)
- [ ] 디버그 이슈 분리 로직 개선 (논리적 이슈 단위로 클러스터링) (선택적, 추후 개선)
- [ ] 단위 테스트 작성 (`tests/test_issues_builder.py`) (선택적, 추후 개선)

### Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토 (진행 중)

**목표**: 
1. 파이프라인 중간 결과를 Fixture와 파일 캐싱으로 관리하여 중복 실행 제거
2. Timeline Section을 Issue Card 생성에 활용
3. Issue Card 생성 로직 전면 재검토 및 개선

**발견된 문제점**:
- 각 테스트가 독립적으로 파싱/이벤트 정규화 재실행 (비효율)
- Timeline Section 생성이 Issue Card 생성 이후에 실행됨
- Timeline Section을 Issue Card에 활용할 수 없음
- Issue Card 품질 문제: LLM이 제대로 적용되지 않은 것으로 보임
  - Root cause에 중간 과정 텍스트 포함
  - Fix summary가 형식적이고 부자연스러움
  - Symptom이 핵심이 아닌 경우 발생
- 각 컴포넌트(symptom, root_cause, fix, validation)가 독립적으로 작동하여 컨텍스트 부족

**⚠️ Phase 4.7 완료 후 발견된 심각한 문제점 (2025-12-26)**:
- **Issue Card 결과가 완전히 엉망**: 사용자 평가 "100점 만점에 -100점"
- **핵심 문제**:
  1. **`extract_issue_with_llm()` 함수가 구현되어 있지만 사용되지 않음**
     - `build_issue_card_from_cluster()` 함수가 각 컴포넌트를 개별적으로 추출
     - 통합 컨텍스트를 활용하지 못함
  2. **Fix 항목이 20개나 생성됨** (각 이벤트마다 하나씩)
     - `extract_fix_with_llm()` 함수가 각 DEBUG 이벤트마다 개별 호출됨
     - 각 fix가 매우 길고 반복적인 템플릿 문구 포함 ("이벤트 요약에 기반하여 구체적인 해결 방법을 추출하고 설명하겠습니다.")
  3. **Symptom이 너무 짧고 구체적이지 않음**
     - "다음 단계" 같은 의미 없는 텍스트만 추출됨
  4. **Title이 잘림**
     - 제목 생성 로직에 문제가 있거나 길이 제한이 너무 짧음
  5. **LLM은 사용되었지만 프롬프트/로직 문제**
     - 캐시 파일 확인 결과 LLM 호출은 정상적으로 이루어짐
     - 하지만 프롬프트가 각 컴포넌트를 개별적으로 요청하여 컨텍스트 부족
     - `extract_issue_with_llm()` 함수가 구현되어 있지만 실제로 호출되지 않음
- **확인된 사항**:
  - LLM 캐시 파일 존재: `cache/issue_*.json` (92개 파일)
  - LLM 호출은 정상적으로 이루어짐 (캐시 히트율 32.84%)
  - 문제는 로직 구조: 통합 컨텍스트를 활용하지 않고 각 컴포넌트를 개별 추출
- **필요한 개선**:
  1. `build_issue_card_from_cluster()` 함수를 `extract_issue_with_llm()` 사용하도록 수정
  2. 각 이벤트마다 개별 fix 추출 대신, 클러스터 전체에 대한 통합 fix 추출
  3. Symptom 추출 프롬프트 개선 (핵심만 추출하도록)
  4. Title 생성 로직 개선 (길이 제한 확대 또는 더 나은 요약)
  5. 통합 컨텍스트(TimelineSection + Events + Turns)를 활용한 일관성 있는 추출

**개선 방향**:
1. **파이프라인 데이터 관리**: 하이브리드 방식 (Fixture + 파일 캐싱)
   - pytest Fixture로 메모리 기반 공유 (빠른 접근)
   - 파일 기반 캐싱으로 영구 저장 (디버깅, 수동 검증)
2. **Issue Card 생성 로직 전면 재검토**:
   - 입력: TimelineSection + 관련 Events + 관련 Turns (통합 컨텍스트)
   - LLM 프롬프트: 구조화된 출력 (현상-원인-개선내용)
   - 출력: 구조화된 IssueCard (Timeline Section과 연결)
3. **이슈 클러스터링**: DEBUG 타입 이벤트 주변 Turn들을 논리적 이슈 단위로 클러스터링

**구현 계획**:

**Phase 4.7.1: 중간 결과 캐싱 모듈 생성**
- [ ] `backend/core/pipeline_cache.py` 생성
  - 파싱 결과 캐싱 (파일 기반)
  - 이벤트 정규화 결과 캐싱 (파일 기반)
  - Timeline Section 결과 캐싱 (파일 기반)
  - 캐시 키 생성 (입력 파일 해시 + use_llm 플래그)
  - 캐시 무효화 전략 (입력 파일 변경 감지)

**Phase 4.7.2: pytest Fixture 추가**
- [ ] `tests/conftest.py`에 Fixture 추가
  - `parsed_data` fixture (세션 스코프)
  - `normalized_events` fixture (세션 스코프, use_llm 파라미터)
  - `timeline_sections` fixture (세션 스코프, use_llm 파라미터)
  - 각 Fixture는 pipeline_cache 모듈 사용

**Phase 4.7.3: Issue Card 생성 로직 개선** - ✅ 완료 (2025-12-27)
- [x] `backend/builders/issues_builder.py` 수정
  - [x] `build_issue_cards()` 함수 시그니처 변경: `timeline_sections` 파라미터 추가
  - [x] DEBUG 이벤트 클러스터링 로직 구현 (논리적 이슈 단위로 그룹화)
  - [x] Timeline Section과 Issue Card 매칭 로직 구현
  - [x] **`build_issue_card_from_cluster()` 함수 수정**:
    - [x] 개별 추출 함수 호출 제거 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`)
    - [x] `extract_issue_with_llm()` 한 번 호출로 통합 (통합 컨텍스트 기반)
    - [x] 모든 필드에 fallback 적용 (일관성):
      - `title`: `generate_issue_title_from_cluster()` 사용
      - `symptom`: 첫 번째 User Turn 사용
      - `root_cause`: 패턴 기반 추출
      - `fix`: 패턴 기반 추출
      - `validation`: 패턴 기반 추출
  - [x] **`build_issue_card_from_window()` 함수 수정**:
    - [x] window를 클러스터로 변환하여 `extract_issue_with_llm()` 사용
    - [x] 개별 추출 함수 호출 제거
    - [x] 모든 필드에 fallback 적용 (동일한 전략)

**Phase 4.7.4: LLM 서비스 리팩토링 및 통합** - ✅ 완료 (2025-12-27)
- [x] `backend/core/constants.py` 수정
  - [x] `LLM_MODEL = "gpt-4.1-mini"` 상수 추가 (커서룰에 맞춰 통일)
- [x] `backend/core/llm_service.py` 수정
  - [x] **공통 LLM 호출 함수 추출**: `_call_llm_with_retry()` 함수 생성
    - 캐시 확인/저장 로직 통합
    - 재시도 로직 (지수 백오프) 통합
    - 예외 처리 및 fallback 통합
  - [x] **모든 함수에서 `LLM_MODEL` 상수 사용**: 하드코딩된 모델명 제거
  - [x] **`extract_issue_with_llm()` 함수 개선**:
    - 반환값에 `title` 필드 추가 (필수)
    - 프롬프트에 title 생성 규칙 추가
    - 반환 구조: `{"title": str, "symptom": str, "root_cause": dict, "fix": dict, "validation": str}`
  - [x] **개별 추출 함수 제거**:
    - `extract_symptom_with_llm()` 제거
    - `extract_root_cause_with_llm()` 제거
    - `extract_fix_with_llm()` 제거
    - `extract_validation_with_llm()` 제거
  - 참고: 모든 LLM 호출 함수에서 `_call_llm_with_retry()` 사용 (향후 리팩토링 가능)

**Phase 4.7.5: IssueCard 모델 확장**
- [ ] `backend/core/models.py` 수정
  - `IssueCard` 모델에 필드 추가:
    - `section_id: Optional[str]` - 연결된 Timeline Section ID
    - `section_title: Optional[str]` - 연결된 Timeline Section 제목
    - `related_events: List[str]` - 관련 Event ID 리스트
    - `related_turns: List[int]` - 관련 Turn 인덱스 리스트
    - `confidence_score: Optional[float]` - 추출 신뢰도 점수

**Phase 4.7.6: 테스트 코드 수정**
- [ ] `tests/test_timeline_issues_e2e.py` 수정
  - Fixture 사용으로 변경 (parsed_data, normalized_events, timeline_sections)
  - 실행 순서 변경: Timeline Section 생성 → Issue Card 생성
  - 새로운 Issue Card 생성 로직 검증

**Phase 4.7.7: 캐시 무효화 전략 구현** - ✅ 완료 (이전 Phase에서 완료됨)
- [x] `backend/core/pipeline_cache.py`에 무효화 로직 추가
  - [x] 입력 파일 변경 감지 (파일 해시 비교) - 각 함수에서 자동 구현됨
  - [x] 자동 무효화 (캐시 키 기반) - 파일 해시 불일치 시 자동 무효화
  - [x] 수동 무효화 옵션 (테스트용) - `invalidate_cache()` 함수 구현됨

**검증 계획**:
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 캐시 동작 확인 (파일 저장/로드)
  - [x] 실행 순서 확인 (Timeline → Issue)
  - [x] 성능 개선 확인 (중복 실행 제거)
  - [x] 하위 호환성 확인 (기존 테스트 통과)
- [x] Issue Card 품질 평가 (2025-12-27 완료)
  - [x] 새로운 로직으로 생성된 Issue Card 품질 분석
    - **핵심 개선 사항 확인**:
      - Fix 항목: 20개 → 1개 (클러스터당, 95% 감소) ✅
      - Title: LLM 생성으로 품질 향상 ✅
      - Symptom: 구체적이고 명확함 ✅
      - Root Cause: 중간 과정 텍스트 제거, 핵심만 포함 ✅
      - Fix: 통합 컨텍스트 기반으로 구체적이고 명확함 ✅
      - Validation: 구체적인 검증 방법 제시 ✅
  - [x] Timeline Section 연결 정확성 검증 (100% 연결률) ✅
  - [x] LLM 적용 여부 확인 (2회 호출, 클러스터당 1회) ✅

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

**⚠️ 중요**: Phase 5는 패턴 기반 처리입니다 (LLM 미사용)
- 스니펫 ID 생성: 규칙 기반 (SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang})
- 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
- 중복 제거: 해시 기반 (SHA-256)
- 링킹: Turn/Event 인덱스 매칭

**입력-처리-출력**:
```
입력: Turns (code_blocks), Events, IssueCards, SessionMeta
처리: CodeBlock → Snippet 변환 → 중복 제거 → 링킹 → snippets.json 생성
출력: snippets.json, 업데이트된 Events/IssueCards (snippet_refs 포함)
```

**구현 계획**:

**Phase 5.1: Snippet 모델 정의**
- [ ] `backend/core/models.py`에 Snippet 모델 추가
  - snippet_id, lang, code, source, links, snippet_hash, aliases 필드

**Phase 5.2: 스니펫 관리 모듈 구현**
- [ ] `backend/builders/snippet_manager.py` 생성
  - [ ] 스니펫 ID 생성 함수 (generate_snippet_id)
  - [ ] 코드 정규화 및 해시 생성 함수 (normalize_code, generate_snippet_hash)
  - [ ] 언어 판별 함수 (detect_language, fence_lang 우선 → 휴리스틱)
  - [ ] CodeBlock → Snippet 변환 함수 (code_blocks_to_snippets)
  - [ ] 중복 제거 로직 (deduplicate_snippets, 해시 기반)
  - [ ] 링킹 로직 (link_snippets_to_events, link_snippets_to_issues)
  - [ ] 통합 처리 함수 (process_snippets)

**Phase 5.3: 스니펫 저장 모듈 구현**
- [ ] `backend/builders/snippet_storage.py` 생성
  - [ ] snippets.json 생성 함수 (generate_snippets_json)

**Phase 5.4: 파이프라인 캐싱 통합 (선택적)**
- [ ] `backend/core/pipeline_cache.py`에 스니펫 캐싱 추가 (선택적)
  - [ ] get_or_create_snippets() 함수 추가

**Phase 5.5: 테스트 작성**
- [ ] `tests/test_snippet_manager.py` 작성 (단위 테스트)
  - [ ] test_generate_snippet_id()
  - [ ] test_normalize_code()
  - [ ] test_generate_snippet_hash()
  - [ ] test_detect_language()
  - [ ] test_code_blocks_to_snippets()
  - [ ] test_deduplicate_snippets()
  - [ ] test_link_snippets_to_events()
  - [ ] test_link_snippets_to_issues()
- [ ] `tests/test_snippet_e2e.py` 작성 (E2E 테스트)
  - [ ] test_snippet_e2e_with_llm() - 전체 파이프라인 통합 테스트
    - 실제 입력 파일 사용 (docs/cursor_phase_6_3.md)
    - 파싱 → 이벤트 정규화 → Timeline → Issue Cards → 스니펫 처리
    - snippets.json 생성 및 검증
    - Event/IssueCard 링킹 검증

**검증 계획**:
- [ ] 단위 테스트 실행 및 통과 확인
- [ ] E2E 테스트 실행 및 검증
  - 스니펫 ID 형식 검증
  - 중복 제거 검증 (해시 기반)
  - Event 링킹 검증 (Event.snippet_refs)
  - Issue Card 링킹 검증 (IssueCard.snippet_refs)
  - snippets.json 구조 검증
- [ ] E2E 테스트 결과 분석 및 리포트 생성

---

## Phase 6-8: 미완료 (간략 요약)

### Phase 6: 백엔드 API 구현
- [ ] FastAPI 엔드포인트 구현 (파싱, Timeline, Issues, Snippets, Export)
- [ ] Markdown 렌더러 구현
- [ ] 테스트 및 E2E 테스트 (실제 서버 실행)

### Phase 7: 프론트엔드 UI 구현
- [ ] Next.js 기반 웹 UI (메인 페이지, 입력 패널, 결과 미리보기, Export 패널)
- [ ] API 클라이언트 및 타입 정의
- [ ] 스타일링 (Tailwind CSS)

### Phase 8: 통합 테스트 및 QA
- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 4.7 완료, Phase 5 진행 예정 (코드 스니펫 분리 및 저장)

**마지막 업데이트**: 2025-12-27

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3.0-3.3: 이벤트 정규화 기본 구현 및 평가 방법 구축 (2025-12-20~23)
- Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선 (2025-12-23~26)
  - 타입 체계 개선 완료 (CODE_GENERATION 추가, ARTIFACT 제거)
- Phase 4: Timeline 및 Issue Cards 생성 기본 구현 (2025-12-26)
  - LLM 기반 E2E 테스트 완료
- Phase 4.5: Timeline 구조화 개선 및 품질 평가 (2025-12-26)
  - Timeline 품질 평가 완료 (품질 점수: 45/100)
- Phase 4.6: Issue Card 품질 개선 (2025-12-26)
  - LLM 기반 추출 함수 구현 완료
  - E2E 테스트 완료 (품질 점수: 94/100, 하지만 실제 품질 문제 발견)
- Phase 4.7.3-4.7.4: Issue Card 생성 로직 개선 및 LLM 서비스 리팩토링 (2025-12-27 완료)
  - `extract_issue_with_llm()` 통합 함수 사용으로 전환
  - 모든 필드에 일관된 fallback 적용
  - LLM 모델 통일 (`gpt-4.1-mini`)
  - 개별 추출 함수 제거 (539줄 삭제)
  - E2E 테스트 완료: Fix 항목 20개 → 1개 (95% 감소), 품질 대폭 향상

**진행 중인 Phase**:
- Phase 5: 코드 스니펫 분리 및 저장 (진행 중)
  - Phase 5.1: Snippet 모델 정의
  - Phase 5.2: 스니펫 관리 모듈 구현
  - Phase 5.3: 스니펫 저장 모듈 구현
  - Phase 5.4: 파이프라인 캐싱 통합 (선택적)
  - Phase 5.5: 테스트 작성

**다음 단계**:
- Phase 5 완료 후 Phase 6 진행 예정 (백엔드 API 구현)

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.

```

```markdown
**진행 중인 Phase**:
- Phase 5: 코드 스니펫 분리 및 저장 (진행 중)
  - Phase 5.1: Snippet 모델 정의
  - Phase 5.2: 스니펫 관리 모듈 구현
  - Phase 5.3: 스니펫 저장 모듈 구현
  - Phase 5.4: 파이프라인 캐싱 통합 (선택적)
  - Phase 5.5: 테스트 작성

**다음 단계**:
- Phase 5 완료 후 Phase 6 진행 예정 (백엔드 API 구현)
```

TODOs.md 업데이트 완료. Phase 5 작업 시작. 규칙 준수 확인 후 단계별 진행.


TODOs.md 업데이트 완료. Phase 5.1 시작. 규칙 준수 확인 완료.

Phase 5.1: Snippet 모델 정의
- 파일: `backend/core/models.py`
- 작업: Snippet 모델 추가 (PRD 및 instruction_detail.md 참조)

진행 내용:
1. Snippet 모델 필드 정의
   - `snippet_id`: 스니펫 ID
   - `lang`: 언어
   - `code`: 코드 내용
   - `source`: 출처 정보
   - `links`: 링크 정보
   - `snippet_hash`: 중복 제거용 해시
   - `aliases`: 중복 제거 시 원본 ID 목록

2. 기존 CodeBlock 모델과의 관계 확인

현재 models.py를 확인하고 Snippet 모델을 추가하겠습니다.


Snippet 모델 추가 중.


```python
"""
데이터 모델 정의

이 모듈은 파서, 빌더, API에서 사용하는 Pydantic 모델을 정의합니다.
"""

from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class SessionMeta(BaseModel):
    """세션 메타데이터"""

    session_id: str
    exported_at: Optional[str] = None
    cursor_version: Optional[str] = None
    phase: Optional[int] = None
    subphase: Optional[int] = None
    source_doc: str


class CodeBlock(BaseModel):
    """코드 블록"""

    turn_index: int  # 어느 Turn에서 추출되었는지
    block_index: int  # Turn 내에서의 인덱스
    lang: str  # 언어 (빈 문자열 가능)
    code: str  # 코드 내용


class Turn(BaseModel):
    """Turn 블록 (User/Cursor 대화 단위)"""

    turn_index: int
    speaker: str  # "User", "Cursor", "Unknown"
    body: str  # 본문 텍스트 (코드 블록 제외)
    code_blocks: List[CodeBlock] = []  # 코드 블록 리스트
    path_candidates: List[str] = []  # 파일/경로 후보 리스트


class EventType(str, Enum):
    """이벤트 타입 Enum

    각 타입은 수행되는 활동(activity)을 명확히 표현합니다.
    Artifact 정보(파일 경로, 코드 블록 등)는 Event.artifacts 필드에 별도로 저장됩니다.
    """

    STATUS_REVIEW = "status_review"  # 상태 확인/리뷰
    PLAN = "plan"  # 계획 수립
    CODE_GENERATION = "code_generation"  # 코드 생성 (새로 추가)
    DEBUG = "debug"  # 문제 해결
    COMPLETION = "completion"  # 완료
    NEXT_STEP = "next_step"  # 다음 단계
    TURN = "turn"  # 일반 대화 (fallback)


class ArtifactAction(str, Enum):
    """Artifact Action 타입 Enum

    파일이나 코드 블록에 대해 수행된 작업의 종류를 나타냅니다.
    """

    READ = "read"  # 읽기/확인
    CREATE = "create"  # 생성
    MODIFY = "modify"  # 수정
    EXECUTE = "execute"  # 실행
    MENTION = "mention"  # 단순 언급 (기본값)


class Event(BaseModel):
    """이벤트 기본 모델 (정규화된 Turn)"""

    seq: int = 0  # 시퀀스 번호 (normalize_turns_to_events에서 부여)
    session_id: str = ""  # 세션 ID
    turn_ref: int  # 원본 Turn 인덱스
    phase: Optional[int] = None  # Phase 번호
    subphase: Optional[int] = None  # Subphase 번호
    type: EventType  # 이벤트 타입
    summary: str  # 요약
    artifacts: List[dict] = []  # 연결된 Artifact (파일 경로, 액션 등)
    snippet_refs: List[str] = []  # 연결된 스니펫 ID (Phase 5에서 생성될 ID)
    processing_method: str = "regex"  # "regex" 또는 "llm" (결과 파일에 기록)


class TimelineEvent(BaseModel):
    """Timeline 이벤트 모델"""

    seq: int  # 시퀀스 번호
    session_id: str  # 세션 ID
    phase: Optional[int] = None  # Phase 번호
    subphase: Optional[int] = None  # Subphase 번호
    type: EventType  # 이벤트 타입
    summary: str  # 요약
    artifacts: List[dict] = []  # 연결된 Artifact (파일 경로, 액션 등)
    snippet_refs: List[str] = []  # 연결된 스니펫 ID


class TimelineSection(BaseModel):
    """Timeline 섹션 모델 (주요 작업 항목)

    Phase/Subphase별로 주요 작업을 항목화하여 구조화된 Timeline을 생성합니다.
    각 섹션은 하나의 주요 작업 항목을 나타내며, 관련 Event들을 그룹화합니다.
    """

    section_id: str  # 섹션 ID (예: "6.7-main-task-1")
    title: str  # 작업 항목 제목
    summary: str  # 작업 내용 요약
    phase: Optional[int] = None  # Phase 번호
    subphase: Optional[int] = None  # Subphase 번호
    events: List[int] = []  # 관련 Event seq 리스트
    has_issues: bool = False  # 이슈 발생 여부
    issue_refs: List[str] = []  # 관련 Issue Card ID 리스트
    detailed_results: dict = {}  # 작업 결과 연결 정보
    # detailed_results 구조 예시:
    # {
    #   "code_snippets": ["snippet_id_1", "snippet_id_2"],  # 관련 코드 스니펫
    #   "files": ["path/to/file1.py", "path/to/file2.ts"],  # 관련 파일
    #   "artifacts": [{"path": "...", "action": "create"}],  # Artifact 정보
    #   "git_commit": "abc123def456",  # Git commit 해시 (선택적)
    # }


class IssueCard(BaseModel):
    """Issue Card 모델"""

    issue_id: str  # 이슈 ID (예: "ISS-003-1234")
    scope: dict  # 범위 (session_id, phase, subphase)
    title: str  # 이슈 제목
    symptoms: List[str] = []  # 증상 (주로 User 발화)
    root_cause: Optional[dict] = None  # 원인 (status: "confirmed" | "hypothesis", text: str)
    evidence: List[dict] = []  # 증거
    fix: List[dict] = []  # 조치 방법 (summary, snippet_refs)
    validation: List[str] = []  # 검증 방법
    related_artifacts: List[dict] = []  # 관련 파일
    snippet_refs: List[str] = []  # 관련 코드 스니펫 ID
    # Phase 4.7 추가 필드
    section_id: Optional[str] = None  # 연결된 Timeline Section ID
    section_title: Optional[str] = None  # 연결된 Timeline Section 제목
    related_events: List[int] = []  # 관련 Event seq 리스트
    related_turns: List[int] = []  # 관련 Turn 인덱스 리스트
    confidence_score: Optional[float] = None  # 추출 신뢰도 점수 (0.0 ~ 1.0)


class Snippet(BaseModel):
    """코드 스니펫 모델 (Phase 5)

    코드 블록을 별도로 저장하고 Timeline/Issue Cards와 링킹하기 위한 모델입니다.
    """

    snippet_id: str  # 스니펫 ID (예: "SNP-session-012-00-sql")
    lang: str  # 언어 (예: "sql", "python", "typescript")
    code: str  # 코드 내용
    source: dict  # 출처 정보 {turn_index: int, block_index: int}
    links: dict = {}  # 링크 정보 {issue_id?: str, event_seq?: int, paths?: List[str]}
    snippet_hash: str  # 중복 제거용 해시 (SHA-256)
    aliases: List[str] = []  # 중복 제거 시 원본 ID 목록 (선택적)

```

Phase 5.1 완료. Snippet 모델 추가 완료. TODOs.md 업데이트 후 다음 단계로 진행합니다.


```markdown
# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (필수)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

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

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**

프로젝트는 Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행합니다.
하지만 Phase 4나 Phase 5에서 문제가 발견되면 **Phase 3으로 돌아가서 이벤트 정규화 로직을 개선**한 후, 다시 Phase 4, 5로 넘어가는 iterative cycle을 돌고 있습니다.

**주의사항**:
- Phase 3, 4, 5의 **기본 순서는 항상 유지**: 3 → 4 → 5
- 개선 작업은 **Phase 3의 서브 Phase (3.1, 3.2, 3.4 등)**로 진행
- Phase 번호는 **절대 섞이지 않음** (3 → 4 → 3.4 → 5 ❌, 3 → 4 → 3.4 → 4 재검증 → 5 ✅)

### Phase 3.0: 기본 구현 (완료)

- ✅ 데이터 모델 정의 (EventType, Event, TimelineEvent, IssueCard)
- ✅ 이벤트 정규화 기본 구현 (규칙 기반 타입 분류)
- ✅ 단위 테스트 및 E2E 테스트 완료
- **발견된 문제점**: 이벤트 중복 생성, Summary 품질, 타입 분류 정확도

### Phase 3.1: 즉시 개선 (정규식 기반) - 완료

- ✅ 이벤트 중복 생성 방지 (117개 → 67개, 1:1 매핑 달성)
- ✅ Summary 품질 개선 (줄바꿈 정리, 의미 있는 위치에서 자르기)
- ✅ 타입 분류 엄격화 (구체적인 패턴 사용)

### Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료

- ✅ LLM 서비스 구현 (gpt-4.1-mini, 파일 기반 캐싱, `.env` 자동 로드)
- ✅ 이벤트 정규화 모듈에 LLM 옵션 추가 (`use_llm` 파라미터)
- ✅ LLM 기반 E2E 테스트 완료 (67개 Turn → 67개 Event, 1:1 매핑 달성)
- ✅ E2E 테스트 결과 분석 완료

**Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선** - 완료
- ✅ 병렬 처리 구현 (224초 → 44.99초, 약 5배 향상)
- ✅ 캐시 시스템 개선 (SHA-256 해시, 원자적 저장, 텍스트 해시 검증)
- ✅ 캐시 성능 검증: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상)

### Phase 3.3: 결과 평가 방법 구축 - 완료

- ✅ 정성적 평가 도구 구현 (`backend/builders/evaluation.py`)
- ✅ Golden 파일 관리 도구 구현
- ✅ 수동 검증 프로세스 실행 완료
- ⏸️ Golden 파일 생성: 보류 (Phase 3.4 완료 후 작성 예정)

### Phase 3.4: 이벤트 정규화 품질 개선 (Iterative Improvement Cycle)

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

**⚠️ 컨텍스트**: Phase 4 완료 후 문제 발견 → Phase 3으로 돌아온 개선 작업

**발견된 문제점**:
- Timeline: 이벤트 타입 분류 부정확, Summary 품질 낮음
- Issue Cards: Summary 품질 문제, Root cause/Fix/Validation 추출 품질 낮음

**완료된 작업**:
- [x] 수동 검증 파일 재작성 및 검증 (HTML 형식, 67개 이벤트)
- [x] 정량적/정성적 분석 완료 (타입 분류 정확도 62.69%, 문제 패턴 분류)
- [x] 문제 원인 분석 및 개선 방안 도출
- [x] 개선 작업 실행 (Type 추출 로직, Summary 로직, LLM 프롬프트 개선)
- [x] **타입 체계 개선 구현 완료** (2025-12-26)
  - [x] EventType.ARTIFACT 제거, EventType.CODE_GENERATION 추가
  - [x] ArtifactAction Enum 추가
  - [x] 분류 로직 개선 (is_code_generation_turn, create_code_generation_event)
  - [x] LLM 프롬프트 수정
  - [x] 평가 도구 업데이트
  - [x] E2E 테스트 재실행 및 검증 완료

**상세 개선 계획**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 참조

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**⚠️ 참고**: E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)**로 돌아가서 개선 작업을 수행한 후 다시 Phase 4 E2E 테스트를 재실행합니다

### 기본 구현 - 완료

- ✅ Timeline 빌더 구현 (`build_timeline()`)
- ✅ Issue Cards 빌더 구현 (`build_issue_cards()`)
  - DebugEvent 기반 이슈 탐지, 슬라이딩 윈도우 그룹화
  - Symptom/Root cause/Fix/Validation 추출 (패턴 기반)
- ✅ 단위 테스트 및 E2E 테스트 완료 (구조적 정합성 검증 완료)

**⚠️ E2E 테스트 상태**:
- 구조적 정합성 검증 완료 (테스트 통과)
- 실제 내용 품질 검증은 미완료 (Phase 4.5, 4.6에서 개선 예정)

### Phase 4.5: Timeline 구조화 개선 (진행 중)

**목표**: Timeline을 단순 나열에서 구조화된 작업 항목별 그룹으로 개선

**발견된 문제점**:
- Timeline이 단순히 Event를 seq 1, 2, 3... 순서로 나열
- 주요 작업 내용이 항목화되지 않음
- 작업 내용 중 이슈 발생 여부 표시 안 됨
- 작업 결과 연결 정보 부족

**개선 목표**:
1. Phase/Subphase별로 주요 작업 항목 추출 및 항목화 (1, 2, 3, 4...)
2. 각 항목의 작업 내용 명확화 (LLM 기반 또는 패턴 기반)
3. 작업 내용 중 이슈 발생 여부 표시 (Issue Card와 연결)
4. 작업 결과 연결 정보 추가 (코드 스니펫, 파일, Git commit 등)

**구현 계획**:
- [x] Timeline 구조화 모델 정의 (`TimelineSection` 모델 추가)
- [x] Timeline 구조화 빌더 구현 (`build_structured_timeline()`)
  - [x] Phase/Subphase별 그룹화 로직
  - [x] 주요 작업 항목 추출 로직 (패턴 기반, LLM 옵션 추가 예정)
  - [x] 이슈 연결 로직
  - [x] 작업 결과 연결 정보 추출 로직
- [x] LLM 기반 작업 항목 추출 (선택적) (2025-12-26 완료)
  - [x] LLM 프롬프트 설계 및 캐싱 로직 적용
  - [x] extract_main_tasks_with_llm() 함수 구현
  - [x] timeline_builder에 use_llm 파라미터 통합
- [x] 테스트 작성 및 E2E 테스트 업데이트 (2025-12-26 완료)
  - [x] 단위 테스트 작성 (test_structured_timeline_pattern_based, test_structured_timeline_llm_based)
  - [x] E2E 테스트 업데이트 (test_timeline_issues_e2e_with_llm에서 build_structured_timeline 사용)
  - [x] E2E 테스트 실행 완료 (7개 sections 생성, 패턴 기반 fallback 사용)

**Timeline 품질 평가 및 수동 검증** (2025-12-26 완료):
- [x] E2E 테스트 결과 분석 (결과 파일: `tests/timeline_issues_e2e_llm_20251226_130658.json`)
  - Timeline Section 개수 및 구조 분석 (7개 섹션, 67개 이벤트)
  - Section 제목/요약 품질 평가 (제목 품질 문제 발견: 모든 제목이 이벤트 타입만 나열)
  - 이슈 연결 정확성 검증 (100% 연결률)
  - 작업 결과 연결 정보 완성도 확인 (85.7% 섹션에 코드 스니펫/파일/Artifact 포함)
- [x] Timeline 품질 평가 리포트 생성 (`tests/reports/timeline_quality_evaluation.json`)
- [x] 수동 검증 및 개선점 도출 (`tests/reports/timeline_quality_analysis.md`)
  - **주요 발견사항**: 제목 품질 문제 (7개 섹션 모두), Artifact 중복 문제 (4개 섹션)
  - **품질 점수**: 45/100
  - **개선 권장사항**: 제목 생성 로직 개선, Artifact 중복 제거

**산출물**: 구조화된 Timeline 모델, Timeline 구조화 빌더, E2E 테스트 완료 및 검증 리포트, Timeline 품질 평가 리포트

### Phase 4.6: Issue Card 품질 개선 (완료)

**목표**: Issue Card의 symptom → root_cause → fix → validation 체인을 LLM 기반으로 개선하여 내용 품질 향상

**발견된 문제점** (개선 전):
- Symptom: 단순히 Turn body 처음 500자 잘라내기
- Root cause: 패턴 매칭으로 텍스트 잘라내기 (중간 과정 텍스트 포함)
- Fix: DebugEvent의 summary만 사용 (구체적이지 않음)
- Validation: 패턴 매칭으로 텍스트 잘라내기 (불완전한 텍스트)

**개선 결과** (2025-12-26):
- Symptom: 평균 길이 82.5자 → 23.5자 (약 3.5배 개선, 핵심만 추출)
- Fix: 2개 → 12개 (6배 증가, 구체적이고 상세한 해결 방법)
- Validation: 명확하고 구체적인 검증 방법 추출
- Root cause: 프롬프트 개선 완료 (중간 과정 텍스트 제거 지시 추가)
- 품질 점수: 94/100
- 디버그 부분을 각 이슈로 나누는 로직 점검 필요

**구현 계획**:
- [x] LLM 기반 추출 함수 구현 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`) (2025-12-26 완료)
  - 각 함수는 캐싱 로직 적용 (SHA-256 해시 기반)
  - Fallback 로직 유지 (LLM 실패 시 패턴 기반)
  - 재시도 로직 적용 (최대 3회, 지수 백오프)
- [x] Issue Builder에 LLM 기반 추출 통합 (`build_issue_cards()` 함수에 `use_llm` 파라미터 추가) (2025-12-26 완료)
- [x] E2E 테스트 업데이트 및 실행 완료 (2025-12-26 완료)
  - LLM 기반 Issue Card 생성 검증 완료
  - 품질 분석 완료 (품질 점수: 94/100)
- [x] Root cause 프롬프트 개선 (중간 과정 텍스트 제거) (2025-12-26 완료)
- [ ] 디버그 이슈 분리 로직 개선 (논리적 이슈 단위로 클러스터링) (선택적, 추후 개선)
- [ ] 단위 테스트 작성 (`tests/test_issues_builder.py`) (선택적, 추후 개선)

### Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토 (진행 중)

**목표**: 
1. 파이프라인 중간 결과를 Fixture와 파일 캐싱으로 관리하여 중복 실행 제거
2. Timeline Section을 Issue Card 생성에 활용
3. Issue Card 생성 로직 전면 재검토 및 개선

**발견된 문제점**:
- 각 테스트가 독립적으로 파싱/이벤트 정규화 재실행 (비효율)
- Timeline Section 생성이 Issue Card 생성 이후에 실행됨
- Timeline Section을 Issue Card에 활용할 수 없음
- Issue Card 품질 문제: LLM이 제대로 적용되지 않은 것으로 보임
  - Root cause에 중간 과정 텍스트 포함
  - Fix summary가 형식적이고 부자연스러움
  - Symptom이 핵심이 아닌 경우 발생
- 각 컴포넌트(symptom, root_cause, fix, validation)가 독립적으로 작동하여 컨텍스트 부족

**⚠️ Phase 4.7 완료 후 발견된 심각한 문제점 (2025-12-26)**:
- **Issue Card 결과가 완전히 엉망**: 사용자 평가 "100점 만점에 -100점"
- **핵심 문제**:
  1. **`extract_issue_with_llm()` 함수가 구현되어 있지만 사용되지 않음**
     - `build_issue_card_from_cluster()` 함수가 각 컴포넌트를 개별적으로 추출
     - 통합 컨텍스트를 활용하지 못함
  2. **Fix 항목이 20개나 생성됨** (각 이벤트마다 하나씩)
     - `extract_fix_with_llm()` 함수가 각 DEBUG 이벤트마다 개별 호출됨
     - 각 fix가 매우 길고 반복적인 템플릿 문구 포함 ("이벤트 요약에 기반하여 구체적인 해결 방법을 추출하고 설명하겠습니다.")
  3. **Symptom이 너무 짧고 구체적이지 않음**
     - "다음 단계" 같은 의미 없는 텍스트만 추출됨
  4. **Title이 잘림**
     - 제목 생성 로직에 문제가 있거나 길이 제한이 너무 짧음
  5. **LLM은 사용되었지만 프롬프트/로직 문제**
     - 캐시 파일 확인 결과 LLM 호출은 정상적으로 이루어짐
     - 하지만 프롬프트가 각 컴포넌트를 개별적으로 요청하여 컨텍스트 부족
     - `extract_issue_with_llm()` 함수가 구현되어 있지만 실제로 호출되지 않음
- **확인된 사항**:
  - LLM 캐시 파일 존재: `cache/issue_*.json` (92개 파일)
  - LLM 호출은 정상적으로 이루어짐 (캐시 히트율 32.84%)
  - 문제는 로직 구조: 통합 컨텍스트를 활용하지 않고 각 컴포넌트를 개별 추출
- **필요한 개선**:
  1. `build_issue_card_from_cluster()` 함수를 `extract_issue_with_llm()` 사용하도록 수정
  2. 각 이벤트마다 개별 fix 추출 대신, 클러스터 전체에 대한 통합 fix 추출
  3. Symptom 추출 프롬프트 개선 (핵심만 추출하도록)
  4. Title 생성 로직 개선 (길이 제한 확대 또는 더 나은 요약)
  5. 통합 컨텍스트(TimelineSection + Events + Turns)를 활용한 일관성 있는 추출

**개선 방향**:
1. **파이프라인 데이터 관리**: 하이브리드 방식 (Fixture + 파일 캐싱)
   - pytest Fixture로 메모리 기반 공유 (빠른 접근)
   - 파일 기반 캐싱으로 영구 저장 (디버깅, 수동 검증)
2. **Issue Card 생성 로직 전면 재검토**:
   - 입력: TimelineSection + 관련 Events + 관련 Turns (통합 컨텍스트)
   - LLM 프롬프트: 구조화된 출력 (현상-원인-개선내용)
   - 출력: 구조화된 IssueCard (Timeline Section과 연결)
3. **이슈 클러스터링**: DEBUG 타입 이벤트 주변 Turn들을 논리적 이슈 단위로 클러스터링

**구현 계획**:

**Phase 4.7.1: 중간 결과 캐싱 모듈 생성**
- [ ] `backend/core/pipeline_cache.py` 생성
  - 파싱 결과 캐싱 (파일 기반)
  - 이벤트 정규화 결과 캐싱 (파일 기반)
  - Timeline Section 결과 캐싱 (파일 기반)
  - 캐시 키 생성 (입력 파일 해시 + use_llm 플래그)
  - 캐시 무효화 전략 (입력 파일 변경 감지)

**Phase 4.7.2: pytest Fixture 추가**
- [ ] `tests/conftest.py`에 Fixture 추가
  - `parsed_data` fixture (세션 스코프)
  - `normalized_events` fixture (세션 스코프, use_llm 파라미터)
  - `timeline_sections` fixture (세션 스코프, use_llm 파라미터)
  - 각 Fixture는 pipeline_cache 모듈 사용

**Phase 4.7.3: Issue Card 생성 로직 개선** - ✅ 완료 (2025-12-27)
- [x] `backend/builders/issues_builder.py` 수정
  - [x] `build_issue_cards()` 함수 시그니처 변경: `timeline_sections` 파라미터 추가
  - [x] DEBUG 이벤트 클러스터링 로직 구현 (논리적 이슈 단위로 그룹화)
  - [x] Timeline Section과 Issue Card 매칭 로직 구현
  - [x] **`build_issue_card_from_cluster()` 함수 수정**:
    - [x] 개별 추출 함수 호출 제거 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`)
    - [x] `extract_issue_with_llm()` 한 번 호출로 통합 (통합 컨텍스트 기반)
    - [x] 모든 필드에 fallback 적용 (일관성):
      - `title`: `generate_issue_title_from_cluster()` 사용
      - `symptom`: 첫 번째 User Turn 사용
      - `root_cause`: 패턴 기반 추출
      - `fix`: 패턴 기반 추출
      - `validation`: 패턴 기반 추출
  - [x] **`build_issue_card_from_window()` 함수 수정**:
    - [x] window를 클러스터로 변환하여 `extract_issue_with_llm()` 사용
    - [x] 개별 추출 함수 호출 제거
    - [x] 모든 필드에 fallback 적용 (동일한 전략)

**Phase 4.7.4: LLM 서비스 리팩토링 및 통합** - ✅ 완료 (2025-12-27)
- [x] `backend/core/constants.py` 수정
  - [x] `LLM_MODEL = "gpt-4.1-mini"` 상수 추가 (커서룰에 맞춰 통일)
- [x] `backend/core/llm_service.py` 수정
  - [x] **공통 LLM 호출 함수 추출**: `_call_llm_with_retry()` 함수 생성
    - 캐시 확인/저장 로직 통합
    - 재시도 로직 (지수 백오프) 통합
    - 예외 처리 및 fallback 통합
  - [x] **모든 함수에서 `LLM_MODEL` 상수 사용**: 하드코딩된 모델명 제거
  - [x] **`extract_issue_with_llm()` 함수 개선**:
    - 반환값에 `title` 필드 추가 (필수)
    - 프롬프트에 title 생성 규칙 추가
    - 반환 구조: `{"title": str, "symptom": str, "root_cause": dict, "fix": dict, "validation": str}`
  - [x] **개별 추출 함수 제거**:
    - `extract_symptom_with_llm()` 제거
    - `extract_root_cause_with_llm()` 제거
    - `extract_fix_with_llm()` 제거
    - `extract_validation_with_llm()` 제거
  - 참고: 모든 LLM 호출 함수에서 `_call_llm_with_retry()` 사용 (향후 리팩토링 가능)

**Phase 4.7.5: IssueCard 모델 확장**
- [ ] `backend/core/models.py` 수정
  - `IssueCard` 모델에 필드 추가:
    - `section_id: Optional[str]` - 연결된 Timeline Section ID
    - `section_title: Optional[str]` - 연결된 Timeline Section 제목
    - `related_events: List[str]` - 관련 Event ID 리스트
    - `related_turns: List[int]` - 관련 Turn 인덱스 리스트
    - `confidence_score: Optional[float]` - 추출 신뢰도 점수

**Phase 4.7.6: 테스트 코드 수정**
- [ ] `tests/test_timeline_issues_e2e.py` 수정
  - Fixture 사용으로 변경 (parsed_data, normalized_events, timeline_sections)
  - 실행 순서 변경: Timeline Section 생성 → Issue Card 생성
  - 새로운 Issue Card 생성 로직 검증

**Phase 4.7.7: 캐시 무효화 전략 구현** - ✅ 완료 (이전 Phase에서 완료됨)
- [x] `backend/core/pipeline_cache.py`에 무효화 로직 추가
  - [x] 입력 파일 변경 감지 (파일 해시 비교) - 각 함수에서 자동 구현됨
  - [x] 자동 무효화 (캐시 키 기반) - 파일 해시 불일치 시 자동 무효화
  - [x] 수동 무효화 옵션 (테스트용) - `invalidate_cache()` 함수 구현됨

**검증 계획**:
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 캐시 동작 확인 (파일 저장/로드)
  - [x] 실행 순서 확인 (Timeline → Issue)
  - [x] 성능 개선 확인 (중복 실행 제거)
  - [x] 하위 호환성 확인 (기존 테스트 통과)
- [x] Issue Card 품질 평가 (2025-12-27 완료)
  - [x] 새로운 로직으로 생성된 Issue Card 품질 분석
    - **핵심 개선 사항 확인**:
      - Fix 항목: 20개 → 1개 (클러스터당, 95% 감소) ✅
      - Title: LLM 생성으로 품질 향상 ✅
      - Symptom: 구체적이고 명확함 ✅
      - Root Cause: 중간 과정 텍스트 제거, 핵심만 포함 ✅
      - Fix: 통합 컨텍스트 기반으로 구체적이고 명확함 ✅
      - Validation: 구체적인 검증 방법 제시 ✅
  - [x] Timeline Section 연결 정확성 검증 (100% 연결률) ✅
  - [x] LLM 적용 여부 확인 (2회 호출, 클러스터당 1회) ✅

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

**⚠️ 중요**: Phase 5는 패턴 기반 처리입니다 (LLM 미사용)
- 스니펫 ID 생성: 규칙 기반 (SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang})
- 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
- 중복 제거: 해시 기반 (SHA-256)
- 링킹: Turn/Event 인덱스 매칭

**입력-처리-출력**:
```
입력: Turns (code_blocks), Events, IssueCards, SessionMeta
처리: CodeBlock → Snippet 변환 → 중복 제거 → 링킹 → snippets.json 생성
출력: snippets.json, 업데이트된 Events/IssueCards (snippet_refs 포함)
```

**구현 계획**:

**Phase 5.1: Snippet 모델 정의** - ✅ 완료
- [x] `backend/core/models.py`에 Snippet 모델 추가
  - [x] snippet_id, lang, code, source, links, snippet_hash, aliases 필드

**Phase 5.2: 스니펫 관리 모듈 구현**
- [ ] `backend/builders/snippet_manager.py` 생성
  - [ ] 스니펫 ID 생성 함수 (generate_snippet_id)
  - [ ] 코드 정규화 및 해시 생성 함수 (normalize_code, generate_snippet_hash)
  - [ ] 언어 판별 함수 (detect_language, fence_lang 우선 → 휴리스틱)
  - [ ] CodeBlock → Snippet 변환 함수 (code_blocks_to_snippets)
  - [ ] 중복 제거 로직 (deduplicate_snippets, 해시 기반)
  - [ ] 링킹 로직 (link_snippets_to_events, link_snippets_to_issues)
  - [ ] 통합 처리 함수 (process_snippets)

**Phase 5.3: 스니펫 저장 모듈 구현**
- [ ] `backend/builders/snippet_storage.py` 생성
  - [ ] snippets.json 생성 함수 (generate_snippets_json)

**Phase 5.4: 파이프라인 캐싱 통합 (선택적)**
- [ ] `backend/core/pipeline_cache.py`에 스니펫 캐싱 추가 (선택적)
  - [ ] get_or_create_snippets() 함수 추가

**Phase 5.5: 테스트 작성**
- [ ] `tests/test_snippet_manager.py` 작성 (단위 테스트)
  - [ ] test_generate_snippet_id()
  - [ ] test_normalize_code()
  - [ ] test_generate_snippet_hash()
  - [ ] test_detect_language()
  - [ ] test_code_blocks_to_snippets()
  - [ ] test_deduplicate_snippets()
  - [ ] test_link_snippets_to_events()
  - [ ] test_link_snippets_to_issues()
- [ ] `tests/test_snippet_e2e.py` 작성 (E2E 테스트)
  - [ ] test_snippet_e2e_with_llm() - 전체 파이프라인 통합 테스트
    - 실제 입력 파일 사용 (docs/cursor_phase_6_3.md)
    - 파싱 → 이벤트 정규화 → Timeline → Issue Cards → 스니펫 처리
    - snippets.json 생성 및 검증
    - Event/IssueCard 링킹 검증

**검증 계획**:
- [ ] 단위 테스트 실행 및 통과 확인
- [ ] E2E 테스트 실행 및 검증
  - 스니펫 ID 형식 검증
  - 중복 제거 검증 (해시 기반)
  - Event 링킹 검증 (Event.snippet_refs)
  - Issue Card 링킹 검증 (IssueCard.snippet_refs)
  - snippets.json 구조 검증
- [ ] E2E 테스트 결과 분석 및 리포트 생성

---

## Phase 6-8: 미완료 (간략 요약)

### Phase 6: 백엔드 API 구현
- [ ] FastAPI 엔드포인트 구현 (파싱, Timeline, Issues, Snippets, Export)
- [ ] Markdown 렌더러 구현
- [ ] 테스트 및 E2E 테스트 (실제 서버 실행)

### Phase 7: 프론트엔드 UI 구현
- [ ] Next.js 기반 웹 UI (메인 페이지, 입력 패널, 결과 미리보기, Export 패널)
- [ ] API 클라이언트 및 타입 정의
- [ ] 스타일링 (Tailwind CSS)

### Phase 8: 통합 테스트 및 QA
- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 4.7 완료, Phase 5 진행 예정 (코드 스니펫 분리 및 저장)

**마지막 업데이트**: 2025-12-27

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3.0-3.3: 이벤트 정규화 기본 구현 및 평가 방법 구축 (2025-12-20~23)
- Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선 (2025-12-23~26)
  - 타입 체계 개선 완료 (CODE_GENERATION 추가, ARTIFACT 제거)
- Phase 4: Timeline 및 Issue Cards 생성 기본 구현 (2025-12-26)
  - LLM 기반 E2E 테스트 완료
- Phase 4.5: Timeline 구조화 개선 및 품질 평가 (2025-12-26)
  - Timeline 품질 평가 완료 (품질 점수: 45/100)
- Phase 4.6: Issue Card 품질 개선 (2025-12-26)
  - LLM 기반 추출 함수 구현 완료
  - E2E 테스트 완료 (품질 점수: 94/100, 하지만 실제 품질 문제 발견)
- Phase 4.7.3-4.7.4: Issue Card 생성 로직 개선 및 LLM 서비스 리팩토링 (2025-12-27 완료)
  - `extract_issue_with_llm()` 통합 함수 사용으로 전환
  - 모든 필드에 일관된 fallback 적용
  - LLM 모델 통일 (`gpt-4.1-mini`)
  - 개별 추출 함수 제거 (539줄 삭제)
  - E2E 테스트 완료: Fix 항목 20개 → 1개 (95% 감소), 품질 대폭 향상

**진행 중인 Phase**:
- Phase 5: 코드 스니펫 분리 및 저장 (진행 중)
  - Phase 5.1: Snippet 모델 정의
  - Phase 5.2: 스니펫 관리 모듈 구현
  - Phase 5.3: 스니펫 저장 모듈 구현
  - Phase 5.4: 파이프라인 캐싱 통합 (선택적)
  - Phase 5.5: 테스트 작성

**다음 단계**:
- Phase 5 완료 후 Phase 6 진행 예정 (백엔드 API 구현)

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.

```

Phase 5.2: 스니펫 관리 모듈 구현 시작.

작업 내용:
1. 스니펫 ID 생성 함수
2. 코드 정규화 및 해시 생성
3. 언어 판별 (fence_lang 우선 → 휴리스틱)
4. CodeBlock → Snippet 변환
5. 중복 제거 (해시 기반)
6. Event/Issue Card 링킹
7. 통합 처리 함수

`snippet_manager.py` 파일을 생성합니다.


```python
"""
스니펫 관리 모듈 (Phase 5)

코드 블록을 Snippet으로 변환하고, 중복 제거 및 링킹을 수행합니다.
"""

import re
import hashlib
from typing import List, Tuple, Dict, Optional
from collections import defaultdict

from backend.core.models import (
    CodeBlock,
    Snippet,
    Event,
    IssueCard,
    Turn,
    SessionMeta,
)


def generate_snippet_id(
    session_id: str, turn_index: int, block_index: int, lang: str
) -> str:
    """
    스니펫 ID 생성

    형식: SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang}

    Args:
        session_id: 세션 ID
        turn_index: Turn 인덱스
        block_index: 블록 인덱스
        lang: 언어 (비어있으면 "text" 사용)

    Returns:
        스니펫 ID 문자열

    예시:
        SNP-cursor_export_2025-12-14_223636_KST-012-00-sql
    """
    # lang이 비어있으면 "text" 사용
    lang_normalized = lang.strip().lower() if lang else "text"
    if not lang_normalized:
        lang_normalized = "text"

    snippet_id = f"SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang_normalized}"
    return snippet_id


def normalize_code(code: str) -> str:
    """
    코드 정규화 (공백 정규화, 줄바꿈 통일)

    Args:
        code: 원본 코드

    Returns:
        정규화된 코드
    """
    # 줄바꿈 통일 (CRLF → LF)
    normalized = code.replace("\r\n", "\n").replace("\r", "\n")

    # 트레일링 공백 제거 (각 줄 끝)
    lines = normalized.split("\n")
    lines = [line.rstrip() for line in lines]

    # 빈 줄 제거 (선택적, 하지만 중복 제거를 위해서는 공백 정규화만 수행)
    # 완전히 빈 줄은 유지하고 공백만 제거

    return "\n".join(lines)


def generate_snippet_hash(code: str) -> str:
    """
    코드 해시 생성 (SHA-256, 정규화된 코드 사용)

    Args:
        code: 코드 내용

    Returns:
        64자리 해시 문자열 (SHA-256)
    """
    normalized_code = normalize_code(code)
    hash_obj = hashlib.sha256(normalized_code.encode("utf-8"))
    return hash_obj.hexdigest()


def detect_language(code: str, fence_lang: str = "") -> str:
    """
    언어 판별 (fence_lang 우선 → 휴리스틱)

    Args:
        code: 코드 내용
        fence_lang: 코드 펜스에서 추출한 언어 (우선 사용)

    Returns:
        언어 문자열 (예: "sql", "python", "typescript", "bash", "text")

    휴리스틱 규칙:
    - SQL: ALTER TABLE|SELECT|UPDATE|INSERT|DELETE|CREATE TABLE
    - TypeScript: import ... from|export|const|interface|type
    - Python: def |import |from fastapi|from typing
    - Bash: npm |yarn |pnpm|#!/bin/bash|#!/bin/sh
    - 실패 시 "text"
    """
    # fence_lang이 있으면 우선 사용
    if fence_lang:
        lang_normalized = fence_lang.strip().lower()
        if lang_normalized:
            return lang_normalized

    # 휴리스틱: 코드 내용으로 판별
    code_lower = code.lower()
    code_start = code.strip()[:200]  # 처음 200자만 확인

    # SQL 패턴
    sql_pattern = re.compile(
        r"\b(ALTER\s+TABLE|SELECT|UPDATE|INSERT\s+INTO|DELETE\s+FROM|CREATE\s+TABLE|DROP\s+TABLE)\b",
        re.IGNORECASE,
    )
    if sql_pattern.search(code_start):
        return "sql"

    # TypeScript 패턴
    ts_pattern = re.compile(
        r"(import\s+.*\s+from|export\s+(const|interface|type|default)|const\s+\w+\s*[:=]|interface\s+\w+|type\s+\w+\s*=)",
        re.IGNORECASE,
    )
    if ts_pattern.search(code_start):
        return "typescript"

    # Python 패턴
    python_pattern = re.compile(
        r"(def\s+\w+|import\s+\w+|from\s+\w+\s+import|from\s+fastapi|from\s+typing)",
        re.IGNORECASE,
    )
    if python_pattern.search(code_start):
        return "python"

    # Bash 패턴
    bash_pattern = re.compile(
        r"(npm\s+|yarn\s+|pnpm\s+|#!/bin/bash|#!/bin/sh|#!/usr/bin/env\s+bash)",
        re.IGNORECASE,
    )
    if bash_pattern.search(code_start):
        return "bash"

    # 판별 실패 시 "text"
    return "text"


def code_blocks_to_snippets(
    code_blocks: List[CodeBlock], session_id: str, session_meta: SessionMeta
) -> List[Snippet]:
    """
    CodeBlock 리스트를 Snippet 리스트로 변환

    Args:
        code_blocks: CodeBlock 리스트
        session_id: 세션 ID
        session_meta: 세션 메타데이터 (언어 판별에 사용 가능)

    Returns:
        Snippet 리스트
    """
    snippets = []

    for code_block in code_blocks:
        # 언어 판별 (fence_lang 우선 → 휴리스틱)
        lang = detect_language(code_block.code, fence_lang=code_block.lang)

        # 스니펫 ID 생성
        snippet_id = generate_snippet_id(
            session_id=session_id,
            turn_index=code_block.turn_index,
            block_index=code_block.block_index,
            lang=lang,
        )

        # 해시 생성
        snippet_hash = generate_snippet_hash(code_block.code)

        # Snippet 생성
        snippet = Snippet(
            snippet_id=snippet_id,
            lang=lang,
            code=code_block.code,
            source={
                "turn_index": code_block.turn_index,
                "block_index": code_block.block_index,
            },
            links={},
            snippet_hash=snippet_hash,
            aliases=[],
        )

        snippets.append(snippet)

    return snippets


def deduplicate_snippets(snippets: List[Snippet]) -> List[Snippet]:
    """
    중복 스니펫 제거 (해시 기반)

    동일한 해시를 가진 스니펫은 하나만 유지하고,
    제거된 스니펫의 ID는 aliases에 추가합니다.

    Args:
        snippets: Snippet 리스트

    Returns:
        중복 제거된 Snippet 리스트
    """
    if not snippets:
        return []

    # 해시별로 그룹화
    hash_groups: Dict[str, List[Snippet]] = defaultdict(list)
    for snippet in snippets:
        hash_groups[snippet.snippet_hash].append(snippet)

    deduplicated = []

    for snippet_hash, group in hash_groups.items():
        if len(group) == 1:
            # 중복 없음
            deduplicated.append(group[0])
        else:
            # 중복 있음: 첫 번째를 대표로 사용
            representative = group[0]

            # 나머지의 ID를 aliases에 추가
            aliases = [s.snippet_id for s in group[1:]]
            representative.aliases = aliases

            # 나머지의 links 정보를 병합 (선택적)
            # 대표 snippet의 links에 모든 정보 병합
            for other in group[1:]:
                # links 병합 (issue_id, event_seq, paths)
                if other.links:
                    if not representative.links:
                        representative.links = {}
                    # issue_id 병합
                    if "issue_id" in other.links and "issue_id" not in representative.links:
                        representative.links["issue_id"] = other.links["issue_id"]
                    # event_seq 병합 (리스트로)
                    if "event_seq" in other.links:
                        if "event_seq" not in representative.links:
                            representative.links["event_seq"] = []
                        if isinstance(representative.links["event_seq"], list):
                            representative.links["event_seq"].append(other.links["event_seq"])
                    # paths 병합
                    if "paths" in other.links:
                        if "paths" not in representative.links:
                            representative.links["paths"] = []
                        if isinstance(representative.links["paths"], list):
                            representative.links["paths"].extend(other.links["paths"])

            deduplicated.append(representative)

    return deduplicated


def link_snippets_to_events(
    snippets: List[Snippet], events: List[Event]
) -> Tuple[List[Snippet], List[Event]]:
    """
    스니펫과 이벤트 간 링킹

    Event의 turn_ref와 Snippet의 source.turn_index를 매칭하여 연결합니다.

    Args:
        snippets: Snippet 리스트
        events: Event 리스트

    Returns:
        (업데이트된 Snippet 리스트, 업데이트된 Event 리스트) 튜플
    """
    # 스니펫 인덱스 생성 (turn_index, block_index) → snippet_id 매핑
    snippet_map: Dict[Tuple[int, int], Snippet] = {}
    for snippet in snippets:
        turn_idx = snippet.source["turn_index"]
        block_idx = snippet.source["block_index"]
        snippet_map[(turn_idx, block_idx)] = snippet

    # Event별로 snippet_refs 업데이트
    updated_events = []
    for event in events:
        event_snippet_refs = []

        # turn_ref와 일치하는 스니펫 찾기
        turn_idx = event.turn_ref
        for block_idx in range(100):  # 최대 100개 블록 가정 (충분)
            key = (turn_idx, block_idx)
            if key in snippet_map:
                snippet = snippet_map[key]
                event_snippet_refs.append(snippet.snippet_id)

                # Snippet의 links에 event_seq 추가
                if "event_seq" not in snippet.links:
                    snippet.links["event_seq"] = []
                if not isinstance(snippet.links["event_seq"], list):
                    snippet.links["event_seq"] = [snippet.links["event_seq"]]
                if event.seq not in snippet.links["event_seq"]:
                    snippet.links["event_seq"].append(event.seq)

        # Event의 snippet_refs 업데이트 (기존 refs 유지, 새 refs 추가)
        existing_refs = set(event.snippet_refs)
        new_refs = set(event_snippet_refs)
        event.snippet_refs = list(existing_refs | new_refs)

        updated_events.append(event)

    return snippets, updated_events


def link_snippets_to_issues(
    snippets: List[Snippet],
    issue_cards: List[IssueCard],
    events: List[Event],
) -> Tuple[List[Snippet], List[IssueCard]]:
    """
    스니펫과 Issue Card 간 링킹

    IssueCard의 related_events를 통해 연결된 이벤트를 찾고,
    해당 이벤트의 snippet_refs를 수집하여 IssueCard.snippet_refs를 업데이트합니다.

    Args:
        snippets: Snippet 리스트
        issue_cards: IssueCard 리스트
        events: Event 리스트 (이벤트 조회용)

    Returns:
        (업데이트된 Snippet 리스트, 업데이트된 IssueCard 리스트) 튜플
    """
    # Event 인덱스 생성 (seq → Event 매핑)
    event_map: Dict[int, Event] = {event.seq: event for event in events}

    # Snippet 인덱스 생성 (snippet_id → Snippet 매핑)
    snippet_map: Dict[str, Snippet] = {s.snippet_id: s for s in snippets}

    updated_issue_cards = []

    for issue_card in issue_cards:
        # related_events를 통해 snippet_refs 수집
        issue_snippet_refs = set()

        for event_seq in issue_card.related_events:
            if event_seq in event_map:
                event = event_map[event_seq]
                issue_snippet_refs.update(event.snippet_refs)

        # IssueCard의 snippet_refs 업데이트 (기존 refs 유지, 새 refs 추가)
        existing_refs = set(issue_card.snippet_refs)
        issue_card.snippet_refs = list(existing_refs | issue_snippet_refs)

        # Snippet의 links에 issue_id 추가
        for snippet_id in issue_card.snippet_refs:
            if snippet_id in snippet_map:
                snippet = snippet_map[snippet_id]
                if "issue_id" not in snippet.links:
                    snippet.links["issue_id"] = issue_card.issue_id

        updated_issue_cards.append(issue_card)

    return snippets, updated_issue_cards


def process_snippets(
    turns: List[Turn],
    events: List[Event],
    issue_cards: List[IssueCard],
    session_meta: SessionMeta,
) -> Tuple[List[Snippet], List[Event], List[IssueCard]]:
    """
    전체 스니펫 처리 파이프라인

    Args:
        turns: Turn 리스트
        events: Event 리스트
        issue_cards: IssueCard 리스트
        session_meta: 세션 메타데이터

    Returns:
        (snippets, updated_events, updated_issue_cards) 튜플
    """
    # 1. 모든 Turn의 code_blocks 수집
    all_code_blocks = []
    for turn in turns:
        all_code_blocks.extend(turn.code_blocks)

    # 2. CodeBlock → Snippet 변환
    snippets = code_blocks_to_snippets(
        code_blocks=all_code_blocks,
        session_id=session_meta.session_id,
        session_meta=session_meta,
    )

    # 3. 중복 제거
    snippets = deduplicate_snippets(snippets)

    # 4. Event 링킹
    snippets, events = link_snippets_to_events(snippets, events)

    # 5. Issue Card 링킹
    snippets, issue_cards = link_snippets_to_issues(snippets, issue_cards, events)

    return snippets, events, issue_cards
```

Phase 5.2 완료. `snippet_manager.py` 모듈 구현 완료. Phase 5.3로 진행: 스니펫 저장 모듈 구현.

`snippet_storage.py` 생성 중.


```python
"""
스니펫 저장 모듈 (Phase 5)

snippets.json 파일을 생성합니다.
"""

from pathlib import Path
from typing import List, Optional, Dict, Any
import json

from backend.core.models import Snippet, SessionMeta


def generate_snippets_json(
    snippets: List[Snippet],
    session_meta: SessionMeta,
    output_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    snippets.json 생성 (dict 반환)

    형식:
    {
        "session_meta": {
            "session_id": "...",
            "exported_at": "...",
            "cursor_version": "...",
            "phase": ...,
            "subphase": ...,
            "source_doc": "..."
        },
        "snippets": [
            {
                "snippet_id": "...",
                "lang": "...",
                "code": "...",
                "source": {"turn_index": ..., "block_index": ...},
                "links": {"issue_id": "...", "event_seq": [...], "paths": [...]},
                "snippet_hash": "...",
                "aliases": [...]
            }
        ]
    }

    Args:
        snippets: Snippet 리스트
        session_meta: 세션 메타데이터
        output_dir: 출력 디렉토리 (선택적, None이면 파일 저장 안 함)

    Returns:
        snippets.json 딕셔너리
    """
    # session_meta를 딕셔너리로 변환
    session_meta_dict = session_meta.model_dump()

    # snippets를 딕셔너리 리스트로 변환
    snippets_list = [snippet.model_dump() for snippet in snippets]

    # snippets.json 구조 생성
    snippets_json = {
        "session_meta": session_meta_dict,
        "snippets": snippets_list,
    }

    # 파일 저장 (output_dir이 제공된 경우)
    if output_dir is not None:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        snippets_file = output_dir / "snippets.json"
        with open(snippets_file, "w", encoding="utf-8") as f:
            json.dump(snippets_json, f, ensure_ascii=False, indent=2)

    return snippets_json
```

```markdown
# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (필수)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

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

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**

프로젝트는 Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행합니다.
하지만 Phase 4나 Phase 5에서 문제가 발견되면 **Phase 3으로 돌아가서 이벤트 정규화 로직을 개선**한 후, 다시 Phase 4, 5로 넘어가는 iterative cycle을 돌고 있습니다.

**주의사항**:
- Phase 3, 4, 5의 **기본 순서는 항상 유지**: 3 → 4 → 5
- 개선 작업은 **Phase 3의 서브 Phase (3.1, 3.2, 3.4 등)**로 진행
- Phase 번호는 **절대 섞이지 않음** (3 → 4 → 3.4 → 5 ❌, 3 → 4 → 3.4 → 4 재검증 → 5 ✅)

### Phase 3.0: 기본 구현 (완료)

- ✅ 데이터 모델 정의 (EventType, Event, TimelineEvent, IssueCard)
- ✅ 이벤트 정규화 기본 구현 (규칙 기반 타입 분류)
- ✅ 단위 테스트 및 E2E 테스트 완료
- **발견된 문제점**: 이벤트 중복 생성, Summary 품질, 타입 분류 정확도

### Phase 3.1: 즉시 개선 (정규식 기반) - 완료

- ✅ 이벤트 중복 생성 방지 (117개 → 67개, 1:1 매핑 달성)
- ✅ Summary 품질 개선 (줄바꿈 정리, 의미 있는 위치에서 자르기)
- ✅ 타입 분류 엄격화 (구체적인 패턴 사용)

### Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료

- ✅ LLM 서비스 구현 (gpt-4.1-mini, 파일 기반 캐싱, `.env` 자동 로드)
- ✅ 이벤트 정규화 모듈에 LLM 옵션 추가 (`use_llm` 파라미터)
- ✅ LLM 기반 E2E 테스트 완료 (67개 Turn → 67개 Event, 1:1 매핑 달성)
- ✅ E2E 테스트 결과 분석 완료

**Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선** - 완료
- ✅ 병렬 처리 구현 (224초 → 44.99초, 약 5배 향상)
- ✅ 캐시 시스템 개선 (SHA-256 해시, 원자적 저장, 텍스트 해시 검증)
- ✅ 캐시 성능 검증: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상)

### Phase 3.3: 결과 평가 방법 구축 - 완료

- ✅ 정성적 평가 도구 구현 (`backend/builders/evaluation.py`)
- ✅ Golden 파일 관리 도구 구현
- ✅ 수동 검증 프로세스 실행 완료
- ⏸️ Golden 파일 생성: 보류 (Phase 3.4 완료 후 작성 예정)

### Phase 3.4: 이벤트 정규화 품질 개선 (Iterative Improvement Cycle)

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

**⚠️ 컨텍스트**: Phase 4 완료 후 문제 발견 → Phase 3으로 돌아온 개선 작업

**발견된 문제점**:
- Timeline: 이벤트 타입 분류 부정확, Summary 품질 낮음
- Issue Cards: Summary 품질 문제, Root cause/Fix/Validation 추출 품질 낮음

**완료된 작업**:
- [x] 수동 검증 파일 재작성 및 검증 (HTML 형식, 67개 이벤트)
- [x] 정량적/정성적 분석 완료 (타입 분류 정확도 62.69%, 문제 패턴 분류)
- [x] 문제 원인 분석 및 개선 방안 도출
- [x] 개선 작업 실행 (Type 추출 로직, Summary 로직, LLM 프롬프트 개선)
- [x] **타입 체계 개선 구현 완료** (2025-12-26)
  - [x] EventType.ARTIFACT 제거, EventType.CODE_GENERATION 추가
  - [x] ArtifactAction Enum 추가
  - [x] 분류 로직 개선 (is_code_generation_turn, create_code_generation_event)
  - [x] LLM 프롬프트 수정
  - [x] 평가 도구 업데이트
  - [x] E2E 테스트 재실행 및 검증 완료

**상세 개선 계획**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 참조

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**⚠️ 참고**: E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)**로 돌아가서 개선 작업을 수행한 후 다시 Phase 4 E2E 테스트를 재실행합니다

### 기본 구현 - 완료

- ✅ Timeline 빌더 구현 (`build_timeline()`)
- ✅ Issue Cards 빌더 구현 (`build_issue_cards()`)
  - DebugEvent 기반 이슈 탐지, 슬라이딩 윈도우 그룹화
  - Symptom/Root cause/Fix/Validation 추출 (패턴 기반)
- ✅ 단위 테스트 및 E2E 테스트 완료 (구조적 정합성 검증 완료)

**⚠️ E2E 테스트 상태**:
- 구조적 정합성 검증 완료 (테스트 통과)
- 실제 내용 품질 검증은 미완료 (Phase 4.5, 4.6에서 개선 예정)

### Phase 4.5: Timeline 구조화 개선 (진행 중)

**목표**: Timeline을 단순 나열에서 구조화된 작업 항목별 그룹으로 개선

**발견된 문제점**:
- Timeline이 단순히 Event를 seq 1, 2, 3... 순서로 나열
- 주요 작업 내용이 항목화되지 않음
- 작업 내용 중 이슈 발생 여부 표시 안 됨
- 작업 결과 연결 정보 부족

**개선 목표**:
1. Phase/Subphase별로 주요 작업 항목 추출 및 항목화 (1, 2, 3, 4...)
2. 각 항목의 작업 내용 명확화 (LLM 기반 또는 패턴 기반)
3. 작업 내용 중 이슈 발생 여부 표시 (Issue Card와 연결)
4. 작업 결과 연결 정보 추가 (코드 스니펫, 파일, Git commit 등)

**구현 계획**:
- [x] Timeline 구조화 모델 정의 (`TimelineSection` 모델 추가)
- [x] Timeline 구조화 빌더 구현 (`build_structured_timeline()`)
  - [x] Phase/Subphase별 그룹화 로직
  - [x] 주요 작업 항목 추출 로직 (패턴 기반, LLM 옵션 추가 예정)
  - [x] 이슈 연결 로직
  - [x] 작업 결과 연결 정보 추출 로직
- [x] LLM 기반 작업 항목 추출 (선택적) (2025-12-26 완료)
  - [x] LLM 프롬프트 설계 및 캐싱 로직 적용
  - [x] extract_main_tasks_with_llm() 함수 구현
  - [x] timeline_builder에 use_llm 파라미터 통합
- [x] 테스트 작성 및 E2E 테스트 업데이트 (2025-12-26 완료)
  - [x] 단위 테스트 작성 (test_structured_timeline_pattern_based, test_structured_timeline_llm_based)
  - [x] E2E 테스트 업데이트 (test_timeline_issues_e2e_with_llm에서 build_structured_timeline 사용)
  - [x] E2E 테스트 실행 완료 (7개 sections 생성, 패턴 기반 fallback 사용)

**Timeline 품질 평가 및 수동 검증** (2025-12-26 완료):
- [x] E2E 테스트 결과 분석 (결과 파일: `tests/timeline_issues_e2e_llm_20251226_130658.json`)
  - Timeline Section 개수 및 구조 분석 (7개 섹션, 67개 이벤트)
  - Section 제목/요약 품질 평가 (제목 품질 문제 발견: 모든 제목이 이벤트 타입만 나열)
  - 이슈 연결 정확성 검증 (100% 연결률)
  - 작업 결과 연결 정보 완성도 확인 (85.7% 섹션에 코드 스니펫/파일/Artifact 포함)
- [x] Timeline 품질 평가 리포트 생성 (`tests/reports/timeline_quality_evaluation.json`)
- [x] 수동 검증 및 개선점 도출 (`tests/reports/timeline_quality_analysis.md`)
  - **주요 발견사항**: 제목 품질 문제 (7개 섹션 모두), Artifact 중복 문제 (4개 섹션)
  - **품질 점수**: 45/100
  - **개선 권장사항**: 제목 생성 로직 개선, Artifact 중복 제거

**산출물**: 구조화된 Timeline 모델, Timeline 구조화 빌더, E2E 테스트 완료 및 검증 리포트, Timeline 품질 평가 리포트

### Phase 4.6: Issue Card 품질 개선 (완료)

**목표**: Issue Card의 symptom → root_cause → fix → validation 체인을 LLM 기반으로 개선하여 내용 품질 향상

**발견된 문제점** (개선 전):
- Symptom: 단순히 Turn body 처음 500자 잘라내기
- Root cause: 패턴 매칭으로 텍스트 잘라내기 (중간 과정 텍스트 포함)
- Fix: DebugEvent의 summary만 사용 (구체적이지 않음)
- Validation: 패턴 매칭으로 텍스트 잘라내기 (불완전한 텍스트)

**개선 결과** (2025-12-26):
- Symptom: 평균 길이 82.5자 → 23.5자 (약 3.5배 개선, 핵심만 추출)
- Fix: 2개 → 12개 (6배 증가, 구체적이고 상세한 해결 방법)
- Validation: 명확하고 구체적인 검증 방법 추출
- Root cause: 프롬프트 개선 완료 (중간 과정 텍스트 제거 지시 추가)
- 품질 점수: 94/100
- 디버그 부분을 각 이슈로 나누는 로직 점검 필요

**구현 계획**:
- [x] LLM 기반 추출 함수 구현 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`) (2025-12-26 완료)
  - 각 함수는 캐싱 로직 적용 (SHA-256 해시 기반)
  - Fallback 로직 유지 (LLM 실패 시 패턴 기반)
  - 재시도 로직 적용 (최대 3회, 지수 백오프)
- [x] Issue Builder에 LLM 기반 추출 통합 (`build_issue_cards()` 함수에 `use_llm` 파라미터 추가) (2025-12-26 완료)
- [x] E2E 테스트 업데이트 및 실행 완료 (2025-12-26 완료)
  - LLM 기반 Issue Card 생성 검증 완료
  - 품질 분석 완료 (품질 점수: 94/100)
- [x] Root cause 프롬프트 개선 (중간 과정 텍스트 제거) (2025-12-26 완료)
- [ ] 디버그 이슈 분리 로직 개선 (논리적 이슈 단위로 클러스터링) (선택적, 추후 개선)
- [ ] 단위 테스트 작성 (`tests/test_issues_builder.py`) (선택적, 추후 개선)

### Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토 (진행 중)

**목표**: 
1. 파이프라인 중간 결과를 Fixture와 파일 캐싱으로 관리하여 중복 실행 제거
2. Timeline Section을 Issue Card 생성에 활용
3. Issue Card 생성 로직 전면 재검토 및 개선

**발견된 문제점**:
- 각 테스트가 독립적으로 파싱/이벤트 정규화 재실행 (비효율)
- Timeline Section 생성이 Issue Card 생성 이후에 실행됨
- Timeline Section을 Issue Card에 활용할 수 없음
- Issue Card 품질 문제: LLM이 제대로 적용되지 않은 것으로 보임
  - Root cause에 중간 과정 텍스트 포함
  - Fix summary가 형식적이고 부자연스러움
  - Symptom이 핵심이 아닌 경우 발생
- 각 컴포넌트(symptom, root_cause, fix, validation)가 독립적으로 작동하여 컨텍스트 부족

**⚠️ Phase 4.7 완료 후 발견된 심각한 문제점 (2025-12-26)**:
- **Issue Card 결과가 완전히 엉망**: 사용자 평가 "100점 만점에 -100점"
- **핵심 문제**:
  1. **`extract_issue_with_llm()` 함수가 구현되어 있지만 사용되지 않음**
     - `build_issue_card_from_cluster()` 함수가 각 컴포넌트를 개별적으로 추출
     - 통합 컨텍스트를 활용하지 못함
  2. **Fix 항목이 20개나 생성됨** (각 이벤트마다 하나씩)
     - `extract_fix_with_llm()` 함수가 각 DEBUG 이벤트마다 개별 호출됨
     - 각 fix가 매우 길고 반복적인 템플릿 문구 포함 ("이벤트 요약에 기반하여 구체적인 해결 방법을 추출하고 설명하겠습니다.")
  3. **Symptom이 너무 짧고 구체적이지 않음**
     - "다음 단계" 같은 의미 없는 텍스트만 추출됨
  4. **Title이 잘림**
     - 제목 생성 로직에 문제가 있거나 길이 제한이 너무 짧음
  5. **LLM은 사용되었지만 프롬프트/로직 문제**
     - 캐시 파일 확인 결과 LLM 호출은 정상적으로 이루어짐
     - 하지만 프롬프트가 각 컴포넌트를 개별적으로 요청하여 컨텍스트 부족
     - `extract_issue_with_llm()` 함수가 구현되어 있지만 실제로 호출되지 않음
- **확인된 사항**:
  - LLM 캐시 파일 존재: `cache/issue_*.json` (92개 파일)
  - LLM 호출은 정상적으로 이루어짐 (캐시 히트율 32.84%)
  - 문제는 로직 구조: 통합 컨텍스트를 활용하지 않고 각 컴포넌트를 개별 추출
- **필요한 개선**:
  1. `build_issue_card_from_cluster()` 함수를 `extract_issue_with_llm()` 사용하도록 수정
  2. 각 이벤트마다 개별 fix 추출 대신, 클러스터 전체에 대한 통합 fix 추출
  3. Symptom 추출 프롬프트 개선 (핵심만 추출하도록)
  4. Title 생성 로직 개선 (길이 제한 확대 또는 더 나은 요약)
  5. 통합 컨텍스트(TimelineSection + Events + Turns)를 활용한 일관성 있는 추출

**개선 방향**:
1. **파이프라인 데이터 관리**: 하이브리드 방식 (Fixture + 파일 캐싱)
   - pytest Fixture로 메모리 기반 공유 (빠른 접근)
   - 파일 기반 캐싱으로 영구 저장 (디버깅, 수동 검증)
2. **Issue Card 생성 로직 전면 재검토**:
   - 입력: TimelineSection + 관련 Events + 관련 Turns (통합 컨텍스트)
   - LLM 프롬프트: 구조화된 출력 (현상-원인-개선내용)
   - 출력: 구조화된 IssueCard (Timeline Section과 연결)
3. **이슈 클러스터링**: DEBUG 타입 이벤트 주변 Turn들을 논리적 이슈 단위로 클러스터링

**구현 계획**:

**Phase 4.7.1: 중간 결과 캐싱 모듈 생성**
- [ ] `backend/core/pipeline_cache.py` 생성
  - 파싱 결과 캐싱 (파일 기반)
  - 이벤트 정규화 결과 캐싱 (파일 기반)
  - Timeline Section 결과 캐싱 (파일 기반)
  - 캐시 키 생성 (입력 파일 해시 + use_llm 플래그)
  - 캐시 무효화 전략 (입력 파일 변경 감지)

**Phase 4.7.2: pytest Fixture 추가**
- [ ] `tests/conftest.py`에 Fixture 추가
  - `parsed_data` fixture (세션 스코프)
  - `normalized_events` fixture (세션 스코프, use_llm 파라미터)
  - `timeline_sections` fixture (세션 스코프, use_llm 파라미터)
  - 각 Fixture는 pipeline_cache 모듈 사용

**Phase 4.7.3: Issue Card 생성 로직 개선** - ✅ 완료 (2025-12-27)
- [x] `backend/builders/issues_builder.py` 수정
  - [x] `build_issue_cards()` 함수 시그니처 변경: `timeline_sections` 파라미터 추가
  - [x] DEBUG 이벤트 클러스터링 로직 구현 (논리적 이슈 단위로 그룹화)
  - [x] Timeline Section과 Issue Card 매칭 로직 구현
  - [x] **`build_issue_card_from_cluster()` 함수 수정**:
    - [x] 개별 추출 함수 호출 제거 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`)
    - [x] `extract_issue_with_llm()` 한 번 호출로 통합 (통합 컨텍스트 기반)
    - [x] 모든 필드에 fallback 적용 (일관성):
      - `title`: `generate_issue_title_from_cluster()` 사용
      - `symptom`: 첫 번째 User Turn 사용
      - `root_cause`: 패턴 기반 추출
      - `fix`: 패턴 기반 추출
      - `validation`: 패턴 기반 추출
  - [x] **`build_issue_card_from_window()` 함수 수정**:
    - [x] window를 클러스터로 변환하여 `extract_issue_with_llm()` 사용
    - [x] 개별 추출 함수 호출 제거
    - [x] 모든 필드에 fallback 적용 (동일한 전략)

**Phase 4.7.4: LLM 서비스 리팩토링 및 통합** - ✅ 완료 (2025-12-27)
- [x] `backend/core/constants.py` 수정
  - [x] `LLM_MODEL = "gpt-4.1-mini"` 상수 추가 (커서룰에 맞춰 통일)
- [x] `backend/core/llm_service.py` 수정
  - [x] **공통 LLM 호출 함수 추출**: `_call_llm_with_retry()` 함수 생성
    - 캐시 확인/저장 로직 통합
    - 재시도 로직 (지수 백오프) 통합
    - 예외 처리 및 fallback 통합
  - [x] **모든 함수에서 `LLM_MODEL` 상수 사용**: 하드코딩된 모델명 제거
  - [x] **`extract_issue_with_llm()` 함수 개선**:
    - 반환값에 `title` 필드 추가 (필수)
    - 프롬프트에 title 생성 규칙 추가
    - 반환 구조: `{"title": str, "symptom": str, "root_cause": dict, "fix": dict, "validation": str}`
  - [x] **개별 추출 함수 제거**:
    - `extract_symptom_with_llm()` 제거
    - `extract_root_cause_with_llm()` 제거
    - `extract_fix_with_llm()` 제거
    - `extract_validation_with_llm()` 제거
  - 참고: 모든 LLM 호출 함수에서 `_call_llm_with_retry()` 사용 (향후 리팩토링 가능)

**Phase 4.7.5: IssueCard 모델 확장**
- [ ] `backend/core/models.py` 수정
  - `IssueCard` 모델에 필드 추가:
    - `section_id: Optional[str]` - 연결된 Timeline Section ID
    - `section_title: Optional[str]` - 연결된 Timeline Section 제목
    - `related_events: List[str]` - 관련 Event ID 리스트
    - `related_turns: List[int]` - 관련 Turn 인덱스 리스트
    - `confidence_score: Optional[float]` - 추출 신뢰도 점수

**Phase 4.7.6: 테스트 코드 수정**
- [ ] `tests/test_timeline_issues_e2e.py` 수정
  - Fixture 사용으로 변경 (parsed_data, normalized_events, timeline_sections)
  - 실행 순서 변경: Timeline Section 생성 → Issue Card 생성
  - 새로운 Issue Card 생성 로직 검증

**Phase 4.7.7: 캐시 무효화 전략 구현** - ✅ 완료 (이전 Phase에서 완료됨)
- [x] `backend/core/pipeline_cache.py`에 무효화 로직 추가
  - [x] 입력 파일 변경 감지 (파일 해시 비교) - 각 함수에서 자동 구현됨
  - [x] 자동 무효화 (캐시 키 기반) - 파일 해시 불일치 시 자동 무효화
  - [x] 수동 무효화 옵션 (테스트용) - `invalidate_cache()` 함수 구현됨

**검증 계획**:
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 캐시 동작 확인 (파일 저장/로드)
  - [x] 실행 순서 확인 (Timeline → Issue)
  - [x] 성능 개선 확인 (중복 실행 제거)
  - [x] 하위 호환성 확인 (기존 테스트 통과)
- [x] Issue Card 품질 평가 (2025-12-27 완료)
  - [x] 새로운 로직으로 생성된 Issue Card 품질 분석
    - **핵심 개선 사항 확인**:
      - Fix 항목: 20개 → 1개 (클러스터당, 95% 감소) ✅
      - Title: LLM 생성으로 품질 향상 ✅
      - Symptom: 구체적이고 명확함 ✅
      - Root Cause: 중간 과정 텍스트 제거, 핵심만 포함 ✅
      - Fix: 통합 컨텍스트 기반으로 구체적이고 명확함 ✅
      - Validation: 구체적인 검증 방법 제시 ✅
  - [x] Timeline Section 연결 정확성 검증 (100% 연결률) ✅
  - [x] LLM 적용 여부 확인 (2회 호출, 클러스터당 1회) ✅

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

**⚠️ 중요**: Phase 5는 패턴 기반 처리입니다 (LLM 미사용)
- 스니펫 ID 생성: 규칙 기반 (SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang})
- 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
- 중복 제거: 해시 기반 (SHA-256)
- 링킹: Turn/Event 인덱스 매칭

**입력-처리-출력**:
```
입력: Turns (code_blocks), Events, IssueCards, SessionMeta
처리: CodeBlock → Snippet 변환 → 중복 제거 → 링킹 → snippets.json 생성
출력: snippets.json, 업데이트된 Events/IssueCards (snippet_refs 포함)
```

**구현 계획**:

**Phase 5.1: Snippet 모델 정의** - ✅ 완료
- [x] `backend/core/models.py`에 Snippet 모델 추가
  - [x] snippet_id, lang, code, source, links, snippet_hash, aliases 필드

**Phase 5.2: 스니펫 관리 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_manager.py` 생성
  - [x] 스니펫 ID 생성 함수 (generate_snippet_id)
  - [x] 코드 정규화 및 해시 생성 함수 (normalize_code, generate_snippet_hash)
  - [x] 언어 판별 함수 (detect_language, fence_lang 우선 → 휴리스틱)
  - [x] CodeBlock → Snippet 변환 함수 (code_blocks_to_snippets)
  - [x] 중복 제거 로직 (deduplicate_snippets, 해시 기반)
  - [x] 링킹 로직 (link_snippets_to_events, link_snippets_to_issues)
  - [x] 통합 처리 함수 (process_snippets)

**Phase 5.3: 스니펫 저장 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_storage.py` 생성
  - [x] snippets.json 생성 함수 (generate_snippets_json)

**Phase 5.4: 파이프라인 캐싱 통합 (선택적)**
- [ ] `backend/core/pipeline_cache.py`에 스니펫 캐싱 추가 (선택적)
  - [ ] get_or_create_snippets() 함수 추가

**Phase 5.5: 테스트 작성**
- [ ] `tests/test_snippet_manager.py` 작성 (단위 테스트)
  - [ ] test_generate_snippet_id()
  - [ ] test_normalize_code()
  - [ ] test_generate_snippet_hash()
  - [ ] test_detect_language()
  - [ ] test_code_blocks_to_snippets()
  - [ ] test_deduplicate_snippets()
  - [ ] test_link_snippets_to_events()
  - [ ] test_link_snippets_to_issues()
- [ ] `tests/test_snippet_e2e.py` 작성 (E2E 테스트)
  - [ ] test_snippet_e2e_with_llm() - 전체 파이프라인 통합 테스트
    - 실제 입력 파일 사용 (docs/cursor_phase_6_3.md)
    - 파싱 → 이벤트 정규화 → Timeline → Issue Cards → 스니펫 처리
    - snippets.json 생성 및 검증
    - Event/IssueCard 링킹 검증

**검증 계획**:
- [ ] 단위 테스트 실행 및 통과 확인
- [ ] E2E 테스트 실행 및 검증
  - 스니펫 ID 형식 검증
  - 중복 제거 검증 (해시 기반)
  - Event 링킹 검증 (Event.snippet_refs)
  - Issue Card 링킹 검증 (IssueCard.snippet_refs)
  - snippets.json 구조 검증
- [ ] E2E 테스트 결과 분석 및 리포트 생성

---

## Phase 6-8: 미완료 (간략 요약)

### Phase 6: 백엔드 API 구현
- [ ] FastAPI 엔드포인트 구현 (파싱, Timeline, Issues, Snippets, Export)
- [ ] Markdown 렌더러 구현
- [ ] 테스트 및 E2E 테스트 (실제 서버 실행)

### Phase 7: 프론트엔드 UI 구현
- [ ] Next.js 기반 웹 UI (메인 페이지, 입력 패널, 결과 미리보기, Export 패널)
- [ ] API 클라이언트 및 타입 정의
- [ ] 스타일링 (Tailwind CSS)

### Phase 8: 통합 테스트 및 QA
- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 4.7 완료, Phase 5 진행 예정 (코드 스니펫 분리 및 저장)

**마지막 업데이트**: 2025-12-27

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3.0-3.3: 이벤트 정규화 기본 구현 및 평가 방법 구축 (2025-12-20~23)
- Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선 (2025-12-23~26)
  - 타입 체계 개선 완료 (CODE_GENERATION 추가, ARTIFACT 제거)
- Phase 4: Timeline 및 Issue Cards 생성 기본 구현 (2025-12-26)
  - LLM 기반 E2E 테스트 완료
- Phase 4.5: Timeline 구조화 개선 및 품질 평가 (2025-12-26)
  - Timeline 품질 평가 완료 (품질 점수: 45/100)
- Phase 4.6: Issue Card 품질 개선 (2025-12-26)
  - LLM 기반 추출 함수 구현 완료
  - E2E 테스트 완료 (품질 점수: 94/100, 하지만 실제 품질 문제 발견)
- Phase 4.7.3-4.7.4: Issue Card 생성 로직 개선 및 LLM 서비스 리팩토링 (2025-12-27 완료)
  - `extract_issue_with_llm()` 통합 함수 사용으로 전환
  - 모든 필드에 일관된 fallback 적용
  - LLM 모델 통일 (`gpt-4.1-mini`)
  - 개별 추출 함수 제거 (539줄 삭제)
  - E2E 테스트 완료: Fix 항목 20개 → 1개 (95% 감소), 품질 대폭 향상

**진행 중인 Phase**:
- Phase 5: 코드 스니펫 분리 및 저장 (진행 중)
  - Phase 5.1: Snippet 모델 정의
  - Phase 5.2: 스니펫 관리 모듈 구현
  - Phase 5.3: 스니펫 저장 모듈 구현
  - Phase 5.4: 파이프라인 캐싱 통합 (선택적)
  - Phase 5.5: 테스트 작성

**다음 단계**:
- Phase 5 완료 후 Phase 6 진행 예정 (백엔드 API 구현)

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.

```

Phase 5.3 완료. snippet_storage.py 모듈 구현 완료. Phase 5.5 테스트 작성 진행.

snippet_manager.py의 링킹 로직 점검: 기존 Event의 snippet_refs가 임시 형식일 수 있어 실제 snippet_id로 교체해야 합니다.


```python
"""
스니펫 관리 모듈 (Phase 5)

코드 블록을 Snippet으로 변환하고, 중복 제거 및 링킹을 수행합니다.
"""

import re
import hashlib
from typing import List, Tuple, Dict, Optional
from collections import defaultdict

from backend.core.models import (
    CodeBlock,
    Snippet,
    Event,
    IssueCard,
    Turn,
    SessionMeta,
)


def generate_snippet_id(
    session_id: str, turn_index: int, block_index: int, lang: str
) -> str:
    """
    스니펫 ID 생성

    형식: SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang}

    Args:
        session_id: 세션 ID
        turn_index: Turn 인덱스
        block_index: 블록 인덱스
        lang: 언어 (비어있으면 "text" 사용)

    Returns:
        스니펫 ID 문자열

    예시:
        SNP-cursor_export_2025-12-14_223636_KST-012-00-sql
    """
    # lang이 비어있으면 "text" 사용
    lang_normalized = lang.strip().lower() if lang else "text"
    if not lang_normalized:
        lang_normalized = "text"

    snippet_id = f"SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang_normalized}"
    return snippet_id


def normalize_code(code: str) -> str:
    """
    코드 정규화 (공백 정규화, 줄바꿈 통일)

    Args:
        code: 원본 코드

    Returns:
        정규화된 코드
    """
    # 줄바꿈 통일 (CRLF → LF)
    normalized = code.replace("\r\n", "\n").replace("\r", "\n")

    # 트레일링 공백 제거 (각 줄 끝)
    lines = normalized.split("\n")
    lines = [line.rstrip() for line in lines]

    # 빈 줄 제거 (선택적, 하지만 중복 제거를 위해서는 공백 정규화만 수행)
    # 완전히 빈 줄은 유지하고 공백만 제거

    return "\n".join(lines)


def generate_snippet_hash(code: str) -> str:
    """
    코드 해시 생성 (SHA-256, 정규화된 코드 사용)

    Args:
        code: 코드 내용

    Returns:
        64자리 해시 문자열 (SHA-256)
    """
    normalized_code = normalize_code(code)
    hash_obj = hashlib.sha256(normalized_code.encode("utf-8"))
    return hash_obj.hexdigest()


def detect_language(code: str, fence_lang: str = "") -> str:
    """
    언어 판별 (fence_lang 우선 → 휴리스틱)

    Args:
        code: 코드 내용
        fence_lang: 코드 펜스에서 추출한 언어 (우선 사용)

    Returns:
        언어 문자열 (예: "sql", "python", "typescript", "bash", "text")

    휴리스틱 규칙:
    - SQL: ALTER TABLE|SELECT|UPDATE|INSERT|DELETE|CREATE TABLE
    - TypeScript: import ... from|export|const|interface|type
    - Python: def |import |from fastapi|from typing
    - Bash: npm |yarn |pnpm|#!/bin/bash|#!/bin/sh
    - 실패 시 "text"
    """
    # fence_lang이 있으면 우선 사용
    if fence_lang:
        lang_normalized = fence_lang.strip().lower()
        if lang_normalized:
            return lang_normalized

    # 휴리스틱: 코드 내용으로 판별
    code_lower = code.lower()
    code_start = code.strip()[:200]  # 처음 200자만 확인

    # SQL 패턴
    sql_pattern = re.compile(
        r"\b(ALTER\s+TABLE|SELECT|UPDATE|INSERT\s+INTO|DELETE\s+FROM|CREATE\s+TABLE|DROP\s+TABLE)\b",
        re.IGNORECASE,
    )
    if sql_pattern.search(code_start):
        return "sql"

    # TypeScript 패턴
    ts_pattern = re.compile(
        r"(import\s+.*\s+from|export\s+(const|interface|type|default)|const\s+\w+\s*[:=]|interface\s+\w+|type\s+\w+\s*=)",
        re.IGNORECASE,
    )
    if ts_pattern.search(code_start):
        return "typescript"

    # Python 패턴
    python_pattern = re.compile(
        r"(def\s+\w+|import\s+\w+|from\s+\w+\s+import|from\s+fastapi|from\s+typing)",
        re.IGNORECASE,
    )
    if python_pattern.search(code_start):
        return "python"

    # Bash 패턴
    bash_pattern = re.compile(
        r"(npm\s+|yarn\s+|pnpm\s+|#!/bin/bash|#!/bin/sh|#!/usr/bin/env\s+bash)",
        re.IGNORECASE,
    )
    if bash_pattern.search(code_start):
        return "bash"

    # 판별 실패 시 "text"
    return "text"


def code_blocks_to_snippets(
    code_blocks: List[CodeBlock], session_id: str, session_meta: SessionMeta
) -> List[Snippet]:
    """
    CodeBlock 리스트를 Snippet 리스트로 변환

    Args:
        code_blocks: CodeBlock 리스트
        session_id: 세션 ID
        session_meta: 세션 메타데이터 (언어 판별에 사용 가능)

    Returns:
        Snippet 리스트
    """
    snippets = []

    for code_block in code_blocks:
        # 언어 판별 (fence_lang 우선 → 휴리스틱)
        lang = detect_language(code_block.code, fence_lang=code_block.lang)

        # 스니펫 ID 생성
        snippet_id = generate_snippet_id(
            session_id=session_id,
            turn_index=code_block.turn_index,
            block_index=code_block.block_index,
            lang=lang,
        )

        # 해시 생성
        snippet_hash = generate_snippet_hash(code_block.code)

        # Snippet 생성
        snippet = Snippet(
            snippet_id=snippet_id,
            lang=lang,
            code=code_block.code,
            source={
                "turn_index": code_block.turn_index,
                "block_index": code_block.block_index,
            },
            links={},
            snippet_hash=snippet_hash,
            aliases=[],
        )

        snippets.append(snippet)

    return snippets


def deduplicate_snippets(snippets: List[Snippet]) -> List[Snippet]:
    """
    중복 스니펫 제거 (해시 기반)

    동일한 해시를 가진 스니펫은 하나만 유지하고,
    제거된 스니펫의 ID는 aliases에 추가합니다.

    Args:
        snippets: Snippet 리스트

    Returns:
        중복 제거된 Snippet 리스트
    """
    if not snippets:
        return []

    # 해시별로 그룹화
    hash_groups: Dict[str, List[Snippet]] = defaultdict(list)
    for snippet in snippets:
        hash_groups[snippet.snippet_hash].append(snippet)

    deduplicated = []

    for snippet_hash, group in hash_groups.items():
        if len(group) == 1:
            # 중복 없음
            deduplicated.append(group[0])
        else:
            # 중복 있음: 첫 번째를 대표로 사용
            representative = group[0]

            # 나머지의 ID를 aliases에 추가
            aliases = [s.snippet_id for s in group[1:]]
            representative.aliases = aliases

            # 나머지의 links 정보를 병합 (선택적)
            # 대표 snippet의 links에 모든 정보 병합
            for other in group[1:]:
                # links 병합 (issue_id, event_seq, paths)
                if other.links:
                    if not representative.links:
                        representative.links = {}
                    # issue_id 병합
                    if "issue_id" in other.links and "issue_id" not in representative.links:
                        representative.links["issue_id"] = other.links["issue_id"]
                    # event_seq 병합 (리스트로)
                    if "event_seq" in other.links:
                        if "event_seq" not in representative.links:
                            representative.links["event_seq"] = []
                        if isinstance(representative.links["event_seq"], list):
                            representative.links["event_seq"].append(other.links["event_seq"])
                    # paths 병합
                    if "paths" in other.links:
                        if "paths" not in representative.links:
                            representative.links["paths"] = []
                        if isinstance(representative.links["paths"], list):
                            representative.links["paths"].extend(other.links["paths"])

            deduplicated.append(representative)

    return deduplicated


def link_snippets_to_events(
    snippets: List[Snippet], events: List[Event]
) -> Tuple[List[Snippet], List[Event]]:
    """
    스니펫과 이벤트 간 링킹

    Event의 turn_ref와 Snippet의 source.turn_index를 매칭하여 연결합니다.

    Args:
        snippets: Snippet 리스트
        events: Event 리스트

    Returns:
        (업데이트된 Snippet 리스트, 업데이트된 Event 리스트) 튜플
    """
    # 스니펫 인덱스 생성 (turn_index, block_index) → snippet_id 매핑
    snippet_map: Dict[Tuple[int, int], Snippet] = {}
    for snippet in snippets:
        turn_idx = snippet.source["turn_index"]
        block_idx = snippet.source["block_index"]
        snippet_map[(turn_idx, block_idx)] = snippet

    # Event별로 snippet_refs 업데이트
    updated_events = []
    for event in events:
        event_snippet_refs = []

        # turn_ref와 일치하는 스니펫 찾기
        turn_idx = event.turn_ref
        for block_idx in range(100):  # 최대 100개 블록 가정 (충분)
            key = (turn_idx, block_idx)
            if key in snippet_map:
                snippet = snippet_map[key]
                event_snippet_refs.append(snippet.snippet_id)

                # Snippet의 links에 event_seq 추가
                if "event_seq" not in snippet.links:
                    snippet.links["event_seq"] = []
                if not isinstance(snippet.links["event_seq"], list):
                    snippet.links["event_seq"] = [snippet.links["event_seq"]]
                if event.seq not in snippet.links["event_seq"]:
                    snippet.links["event_seq"].append(event.seq)

        # Event의 snippet_refs 업데이트
        # Phase 5 이전에는 임시 형식(turn_{turn_index}_block_{block_index})이 있을 수 있으므로
        # 실제 snippet_id로 교체
        event.snippet_refs = event_snippet_refs

        updated_events.append(event)

    return snippets, updated_events


def link_snippets_to_issues(
    snippets: List[Snippet],
    issue_cards: List[IssueCard],
    events: List[Event],
) -> Tuple[List[Snippet], List[IssueCard]]:
    """
    스니펫과 Issue Card 간 링킹

    IssueCard의 related_events를 통해 연결된 이벤트를 찾고,
    해당 이벤트의 snippet_refs를 수집하여 IssueCard.snippet_refs를 업데이트합니다.

    Args:
        snippets: Snippet 리스트
        issue_cards: IssueCard 리스트
        events: Event 리스트 (이벤트 조회용)

    Returns:
        (업데이트된 Snippet 리스트, 업데이트된 IssueCard 리스트) 튜플
    """
    # Event 인덱스 생성 (seq → Event 매핑)
    event_map: Dict[int, Event] = {event.seq: event for event in events}

    # Snippet 인덱스 생성 (snippet_id → Snippet 매핑)
    snippet_map: Dict[str, Snippet] = {s.snippet_id: s for s in snippets}

    updated_issue_cards = []

    for issue_card in issue_cards:
        # related_events를 통해 snippet_refs 수집
        issue_snippet_refs = set()

        for event_seq in issue_card.related_events:
            if event_seq in event_map:
                event = event_map[event_seq]
                issue_snippet_refs.update(event.snippet_refs)

        # IssueCard의 snippet_refs 업데이트 (기존 refs 유지, 새 refs 추가)
        existing_refs = set(issue_card.snippet_refs)
        issue_card.snippet_refs = list(existing_refs | issue_snippet_refs)

        # Snippet의 links에 issue_id 추가
        for snippet_id in issue_card.snippet_refs:
            if snippet_id in snippet_map:
                snippet = snippet_map[snippet_id]
                if "issue_id" not in snippet.links:
                    snippet.links["issue_id"] = issue_card.issue_id

        updated_issue_cards.append(issue_card)

    return snippets, updated_issue_cards


def process_snippets(
    turns: List[Turn],
    events: List[Event],
    issue_cards: List[IssueCard],
    session_meta: SessionMeta,
) -> Tuple[List[Snippet], List[Event], List[IssueCard]]:
    """
    전체 스니펫 처리 파이프라인

    Args:
        turns: Turn 리스트
        events: Event 리스트
        issue_cards: IssueCard 리스트
        session_meta: 세션 메타데이터

    Returns:
        (snippets, updated_events, updated_issue_cards) 튜플
    """
    # 1. 모든 Turn의 code_blocks 수집
    all_code_blocks = []
    for turn in turns:
        all_code_blocks.extend(turn.code_blocks)

    # 2. CodeBlock → Snippet 변환
    snippets = code_blocks_to_snippets(
        code_blocks=all_code_blocks,
        session_id=session_meta.session_id,
        session_meta=session_meta,
    )

    # 3. 중복 제거
    snippets = deduplicate_snippets(snippets)

    # 4. Event 링킹
    snippets, events = link_snippets_to_events(snippets, events)

    # 5. Issue Card 링킹
    snippets, issue_cards = link_snippets_to_issues(snippets, issue_cards, events)

    return snippets, events, issue_cards

```

Phase 5.4는 선택 사항이므로 건너뛰고 Phase 5.5 테스트 작성으로 진행. 단위 테스트부터 작성합니다.


```python
"""
스니펫 관리 모듈 단위 테스트 (Phase 5)

⚠️ 중요: 실제 데이터만 사용 (Mock 사용 절대 금지)
"""

import pytest
from backend.core.models import CodeBlock, Snippet, Event, EventType, SessionMeta, Turn
from backend.builders.snippet_manager import (
    generate_snippet_id,
    normalize_code,
    generate_snippet_hash,
    detect_language,
    code_blocks_to_snippets,
    deduplicate_snippets,
    link_snippets_to_events,
    link_snippets_to_issues,
    process_snippets,
)


def test_generate_snippet_id():
    """스니펫 ID 생성 규칙 검증"""
    # 기본 케이스
    snippet_id = generate_snippet_id("session_123", 12, 0, "sql")
    assert snippet_id == "SNP-session_123-012-00-sql"

    # lang이 비어있는 경우
    snippet_id = generate_snippet_id("session_123", 12, 0, "")
    assert snippet_id == "SNP-session_123-012-00-text"

    # lang이 None인 경우
    snippet_id = generate_snippet_id("session_123", 12, 0, None)
    assert snippet_id == "SNP-session_123-012-00-text"

    # 블록 인덱스가 큰 경우
    snippet_id = generate_snippet_id("session_123", 1, 99, "python")
    assert snippet_id == "SNP-session_123-001-99-python"


def test_normalize_code():
    """코드 정규화 검증"""
    # CRLF → LF 변환
    code = "line1\r\nline2\r\nline3"
    normalized = normalize_code(code)
    assert "\r" not in normalized
    assert normalized == "line1\nline2\nline3"

    # 트레일링 공백 제거
    code = "line1   \nline2\t\t\nline3  "
    normalized = normalize_code(code)
    lines = normalized.split("\n")
    assert lines[0] == "line1"
    assert lines[1] == "line2"
    assert lines[2] == "line3"


def test_generate_snippet_hash():
    """해시 생성 검증 (동일 코드 → 동일 해시)"""
    code1 = "def hello():\n    print('hello')"
    code2 = "def hello():\n    print('hello')"
    code3 = "def hello():\n    print('world')"

    hash1 = generate_snippet_hash(code1)
    hash2 = generate_snippet_hash(code2)
    hash3 = generate_snippet_hash(code3)

    # 동일 코드는 동일 해시
    assert hash1 == hash2

    # 다른 코드는 다른 해시
    assert hash1 != hash3

    # 해시 길이 검증 (SHA-256은 64자리)
    assert len(hash1) == 64


def test_detect_language():
    """언어 판별 검증 (fence_lang 우선 → 휴리스틱)"""
    # fence_lang 우선
    code = "SELECT * FROM users"
    lang = detect_language(code, fence_lang="python")
    assert lang == "python"  # fence_lang이 우선

    # 휴리스틱: SQL
    code = "SELECT * FROM users WHERE id = 1"
    lang = detect_language(code, fence_lang="")
    assert lang == "sql"

    # 휴리스틱: TypeScript
    code = "import { Component } from 'react'\nexport const App = () => {}"
    lang = detect_language(code, fence_lang="")
    assert lang == "typescript"

    # 휴리스틱: Python
    code = "def hello():\n    print('hello')"
    lang = detect_language(code, fence_lang="")
    assert lang == "python"

    # 휴리스틱: Bash
    code = "npm install react"
    lang = detect_language(code, fence_lang="")
    assert lang == "bash"

    # 판별 실패 → text
    code = "some random text without keywords"
    lang = detect_language(code, fence_lang="")
    assert lang == "text"


def test_code_blocks_to_snippets():
    """CodeBlock → Snippet 변환 검증"""
    session_meta = SessionMeta(
        session_id="test_session_123",
        source_doc="test.md",
    )

    code_blocks = [
        CodeBlock(turn_index=0, block_index=0, lang="sql", code="SELECT * FROM users"),
        CodeBlock(turn_index=0, block_index=1, lang="", code="def hello():\n    pass"),
        CodeBlock(turn_index=1, block_index=0, lang="typescript", code="const x = 1"),
    ]

    snippets = code_blocks_to_snippets(code_blocks, "test_session_123", session_meta)

    assert len(snippets) == 3

    # 첫 번째 스니펫 검증
    assert snippets[0].snippet_id == "SNP-test_session_123-000-00-sql"
    assert snippets[0].lang == "sql"
    assert snippets[0].code == "SELECT * FROM users"
    assert snippets[0].source == {"turn_index": 0, "block_index": 0}

    # 두 번째 스니펫 검증 (lang 비어있음 → 휴리스틱으로 python 감지)
    assert snippets[1].snippet_id.startswith("SNP-test_session_123-000-01-")
    assert snippets[1].lang == "python"  # 휴리스틱으로 감지됨

    # 해시 생성 검증
    assert len(snippets[0].snippet_hash) == 64


def test_deduplicate_snippets():
    """중복 제거 검증 (해시 기반, aliases 포함)"""
    # 동일한 코드를 가진 스니펫 2개 생성
    code = "SELECT * FROM users"

    snippet1 = Snippet(
        snippet_id="SNP-session-000-00-sql",
        lang="sql",
        code=code,
        source={"turn_index": 0, "block_index": 0},
        links={},
        snippet_hash=generate_snippet_hash(code),
        aliases=[],
    )

    snippet2 = Snippet(
        snippet_id="SNP-session-001-00-sql",
        lang="sql",
        code=code,
        source={"turn_index": 1, "block_index": 0},
        links={},
        snippet_hash=generate_snippet_hash(code),  # 동일한 해시
        aliases=[],
    )

    # 다른 코드를 가진 스니펫 1개
    code3 = "SELECT * FROM posts"
    snippet3 = Snippet(
        snippet_id="SNP-session-002-00-sql",
        lang="sql",
        code=code3,
        source={"turn_index": 2, "block_index": 0},
        links={},
        snippet_hash=generate_snippet_hash(code3),
        aliases=[],
    )

    snippets = [snippet1, snippet2, snippet3]
    deduplicated = deduplicate_snippets(snippets)

    # 중복 제거 후 2개만 남아야 함
    assert len(deduplicated) == 2

    # 첫 번째 스니펫이 대표로 유지되고, 두 번째의 ID가 aliases에 추가됨
    representative = None
    for s in deduplicated:
        if s.snippet_id == snippet1.snippet_id:
            representative = s
            break

    assert representative is not None
    assert snippet2.snippet_id in representative.aliases


def test_link_snippets_to_events():
    """Event 링킹 검증"""
    # 스니펫 생성
    snippet = Snippet(
        snippet_id="SNP-session-000-00-sql",
        lang="sql",
        code="SELECT * FROM users",
        source={"turn_index": 0, "block_index": 0},
        links={},
        snippet_hash="test_hash",
        aliases=[],
    )

    # Event 생성 (turn_ref=0)
    session_meta = SessionMeta(session_id="session", source_doc="test.md")
    event = Event(
        seq=1,
        session_id="session",
        turn_ref=0,  # snippet과 동일한 turn_index
        type=EventType.CODE_GENERATION,
        summary="Test event",
        snippet_refs=[],  # 빈 리스트
    )

    snippets, events = link_snippets_to_events([snippet], [event])

    # Event의 snippet_refs 업데이트 검증
    assert len(events) == 1
    assert events[0].snippet_refs == ["SNP-session-000-00-sql"]

    # Snippet의 links에 event_seq 추가 검증
    assert len(snippets) == 1
    assert "event_seq" in snippets[0].links
    assert 1 in snippets[0].links["event_seq"]


def test_link_snippets_to_issues():
    """Issue Card 링킹 검증"""
    # 스니펫 생성
    snippet = Snippet(
        snippet_id="SNP-session-000-00-sql",
        lang="sql",
        code="SELECT * FROM users",
        source={"turn_index": 0, "block_index": 0},
        links={},
        snippet_hash="test_hash",
        aliases=[],
    )

    # Event 생성
    session_meta = SessionMeta(session_id="session", source_doc="test.md")
    event = Event(
        seq=1,
        session_id="session",
        turn_ref=0,
        type=EventType.DEBUG,
        summary="Test event",
        snippet_refs=["SNP-session-000-00-sql"],
    )

    # IssueCard 생성
    issue_card = IssueCard(
        issue_id="ISS-001-1234",
        scope={"session_id": "session"},
        title="Test issue",
        related_events=[1],  # event.seq = 1
        snippet_refs=[],
    )

    snippets, issue_cards = link_snippets_to_issues([snippet], [issue_card], [event])

    # IssueCard의 snippet_refs 업데이트 검증
    assert len(issue_cards) == 1
    assert "SNP-session-000-00-sql" in issue_cards[0].snippet_refs

    # Snippet의 links에 issue_id 추가 검증
    assert len(snippets) == 1
    assert snippets[0].links["issue_id"] == "ISS-001-1234"


def test_process_snippets_integration():
    """전체 파이프라인 통합 테스트"""
    # Turn 생성
    code_block = CodeBlock(
        turn_index=0, block_index=0, lang="sql", code="SELECT * FROM users"
    )
    turn = Turn(
        turn_index=0,
        speaker="Cursor",
        body="테스트",
        code_blocks=[code_block],
        path_candidates=[],
    )

    # SessionMeta 생성
    session_meta = SessionMeta(session_id="test_session", source_doc="test.md")

    # Event 생성
    event = Event(
        seq=1,
        session_id="test_session",
        turn_ref=0,
        type=EventType.CODE_GENERATION,
        summary="Test",
        snippet_refs=[],
    )

    # IssueCard 생성
    issue_card = IssueCard(
        issue_id="ISS-001",
        scope={"session_id": "test_session"},
        title="Test",
        related_events=[1],
        snippet_refs=[],
    )

    # 전체 파이프라인 실행
    snippets, events, issue_cards = process_snippets(
        turns=[turn],
        events=[event],
        issue_cards=[issue_card],
        session_meta=session_meta,
    )

    # 검증
    assert len(snippets) == 1
    assert snippets[0].snippet_id.startswith("SNP-test_session-000-00-")
    assert events[0].snippet_refs == [snippets[0].snippet_id]
    assert issue_cards[0].snippet_refs == [snippets[0].snippet_id]
```

단위 테스트 작성 완료. E2E 테스트 작성 진행. 실제 데이터로 전체 파이프라인을 테스트합니다.


```python
"""
스니펫 E2E 테스트 (Phase 5)

실제 입력 데이터로 전체 스니펫 처리 파이프라인을 테스트합니다.

⚠️ 중요: 실제 데이터만 사용 (Mock 사용 절대 금지)
"""

import pytest
import json
from pathlib import Path
from datetime import datetime

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.timeline_builder import build_structured_timeline
from backend.builders.issues_builder import build_issue_cards
from backend.builders.snippet_manager import process_snippets
from backend.builders.snippet_storage import generate_snippets_json
from backend.core.models import Snippet, Event, IssueCard

# 실제 입력 데이터 경로
INPUT_FILE = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
RESULTS_DIR = Path(__file__).parent / "results"
REPORT_DIR = Path(__file__).parent / "reports"


def test_snippet_e2e_with_llm(parsed_data, normalized_events, timeline_sections):
    """
    실제 입력 데이터로 전체 스니펫 처리 파이프라인 E2E 테스트

    테스트 단계:
    1. 파싱 (fixture 사용)
    2. 이벤트 정규화 (fixture 사용)
    3. Timeline Section 생성 (fixture 사용)
    4. Issue Cards 생성
    5. 스니펫 처리 (추출, 중복 제거, 링킹)
    6. snippets.json 생성
    7. 검증 (ID 형식, 중복 제거, 링킹 정확성)
    """
    # 1. Fixture에서 데이터 가져오기
    events, session_meta = normalized_events

    # 2. 딕셔너리를 모델로 변환
    from backend.core.models import Turn, IssueCard
    turns = [Turn(**turn_dict) for turn_dict in parsed_data["turns"]]

    # 3. Issue Cards 생성
    issue_cards = build_issue_cards(
        turns=turns,
        events=events,
        session_meta=session_meta,
        use_llm=True,  # LLM 사용 (기본값)
        timeline_sections=timeline_sections,
    )

    # 4. 스니펫 처리 (추출, 중복 제거, 링킹)
    snippets, updated_events, updated_issue_cards = process_snippets(
        turns=turns,
        events=events,
        issue_cards=issue_cards,
        session_meta=session_meta,
    )

    # 5. snippets.json 생성
    snippets_json = generate_snippets_json(
        snippets=snippets,
        session_meta=session_meta,
        output_dir=None,  # 파일 저장 안 함 (검증만)
    )

    # 6. 정합성 검증

    # 6.1 스니펫 ID 형식 검증
    for snippet in snippets:
        assert snippet.snippet_id.startswith("SNP-"), f"Invalid snippet_id format: {snippet.snippet_id}"
        assert len(snippet.snippet_id.split("-")) >= 5, f"Snippet ID should have format: SNP-session-turn-block-lang, got: {snippet.snippet_id}"
        
        # ID 형식: SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang}
        parts = snippet.snippet_id.split("-")
        assert parts[0] == "SNP"
        assert parts[1] == session_meta.session_id
        # turn_index와 block_index는 숫자 형식 확인
        assert parts[2].isdigit() or len(parts[2]) == 3
        assert parts[3].isdigit() or len(parts[3]) == 2
        # lang은 문자열

    # 6.2 중복 제거 검증 (해시 기반)
    hash_set = set()
    for snippet in snippets:
        assert snippet.snippet_hash not in hash_set, f"Duplicate snippet hash found: {snippet.snippet_hash}"
        hash_set.add(snippet.snippet_hash)

    # 6.3 Event 링킹 검증
    for event in updated_events:
        # snippet_refs가 snippet_id 형식인지 확인
        for snippet_ref in event.snippet_refs:
            assert snippet_ref.startswith("SNP-"), f"Invalid snippet_ref in Event: {snippet_ref}"

        # snippet_refs가 실제로 존재하는 snippet_id인지 확인
        snippet_ids = {s.snippet_id for s in snippets}
        for snippet_ref in event.snippet_refs:
            assert snippet_ref in snippet_ids or any(
                snippet_ref in s.aliases for s in snippets
            ), f"Snippet ref {snippet_ref} not found in snippets"

    # 6.4 Issue Card 링킹 검증
    for issue_card in updated_issue_cards:
        # snippet_refs가 snippet_id 형식인지 확인
        for snippet_ref in issue_card.snippet_refs:
            assert snippet_ref.startswith("SNP-"), f"Invalid snippet_ref in IssueCard: {snippet_ref}"

        # snippet_refs가 실제로 존재하는 snippet_id인지 확인
        snippet_ids = {s.snippet_id for s in snippets}
        for snippet_ref in issue_card.snippet_refs:
            assert snippet_ref in snippet_ids or any(
                snippet_ref in s.aliases for s in snippets
            ), f"Snippet ref {snippet_ref} not found in snippets"

    # 6.5 snippets.json 구조 검증
    assert "session_meta" in snippets_json
    assert "snippets" in snippets_json
    assert isinstance(snippets_json["snippets"], list)
    assert len(snippets_json["snippets"]) == len(snippets)

    # 각 snippet의 필수 필드 검증
    for snippet_dict in snippets_json["snippets"]:
        assert "snippet_id" in snippet_dict
        assert "lang" in snippet_dict
        assert "code" in snippet_dict
        assert "source" in snippet_dict
        assert "links" in snippet_dict
        assert "snippet_hash" in snippet_dict
        assert "aliases" in snippet_dict

    # 7. 타당성 검증

    # 7.1 스니펫 개수 검증 (코드 블록이 있는 Turn이 있으면 스니펫도 있어야 함)
    code_block_count = sum(len(turn.code_blocks) for turn in turns)
    if code_block_count > 0:
        assert len(snippets) > 0, "Code blocks exist but no snippets generated"

    # 7.2 링킹 정확성 검증
    # Event의 turn_ref와 일치하는 스니펫이 링크되어야 함
    event_with_snippets = [e for e in updated_events if e.snippet_refs]
    if event_with_snippets:
        for event in event_with_snippets:
            # 해당 event의 turn_ref에 해당하는 스니펫이 있는지 확인
            matching_snippets = [
                s for s in snippets if s.source["turn_index"] == event.turn_ref
            ]
            if matching_snippets:
                # 일부라도 링크되어 있어야 함
                linked = any(
                    s.snippet_id in event.snippet_refs for s in matching_snippets
                )
                assert linked, f"Event {event.seq} has turn_ref {event.turn_ref} but no matching snippets linked"

    # 8. 결과 분석 및 자동 보고
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 정량적 데이터 수집
    report = {
        "test_name": "snippet_e2e",
        "timestamp": timestamp,
        "input_file": str(INPUT_FILE),
        "results": {
            "total_turns": len(turns),
            "total_code_blocks": code_block_count,
            "total_snippets": len(snippets),
            "total_events": len(updated_events),
            "total_issue_cards": len(updated_issue_cards),
            "events_with_snippets": len([e for e in updated_events if e.snippet_refs]),
            "issue_cards_with_snippets": len([c for c in updated_issue_cards if c.snippet_refs]),
            "duplicate_snippets_removed": code_block_count - len(snippets),
            "snippet_languages": {
                lang: len([s for s in snippets if s.lang == lang])
                for lang in set(s.lang for s in snippets)
            },
        },
        "validation": {
            "snippet_id_format": "PASS",
            "deduplication": "PASS",
            "event_linking": "PASS",
            "issue_card_linking": "PASS",
            "snippets_json_structure": "PASS",
        },
        "warnings": [],
        "errors": [],
    }

    # 경고 검사
    if len(snippets) == 0 and code_block_count > 0:
        report["warnings"].append("Code blocks exist but no snippets generated")

    # 리포트 출력
    print("\n" + "=" * 50)
    print("Snippet E2E Test Report")
    print("=" * 50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 50)

    # 리포트 파일 저장
    RESULTS_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)

    report_file = REPORT_DIR / f"snippet_e2e_report_{timestamp}.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # 상세 결과 저장
    results_file = RESULTS_DIR / f"snippet_e2e_{timestamp}.json"
    detailed_results = {
        "session_meta": session_meta.model_dump(),
        "snippets": [s.model_dump() for s in snippets],
        "events": [e.model_dump() for e in updated_events],
        "issue_cards": [c.model_dump() for c in updated_issue_cards],
        "snippets_json": snippets_json,
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "snippet_e2e",
        },
    }
    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"\n[RESULTS] Detailed results saved to: {results_file}")
    print(f"[REPORT] Report saved to: {report_file}")

    # 최종 검증 통과
    assert len(report["errors"]) == 0, f"Test failed with errors: {report['errors']}"
```

```markdown
# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (필수)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

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

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**

프로젝트는 Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행합니다.
하지만 Phase 4나 Phase 5에서 문제가 발견되면 **Phase 3으로 돌아가서 이벤트 정규화 로직을 개선**한 후, 다시 Phase 4, 5로 넘어가는 iterative cycle을 돌고 있습니다.

**주의사항**:
- Phase 3, 4, 5의 **기본 순서는 항상 유지**: 3 → 4 → 5
- 개선 작업은 **Phase 3의 서브 Phase (3.1, 3.2, 3.4 등)**로 진행
- Phase 번호는 **절대 섞이지 않음** (3 → 4 → 3.4 → 5 ❌, 3 → 4 → 3.4 → 4 재검증 → 5 ✅)

### Phase 3.0: 기본 구현 (완료)

- ✅ 데이터 모델 정의 (EventType, Event, TimelineEvent, IssueCard)
- ✅ 이벤트 정규화 기본 구현 (규칙 기반 타입 분류)
- ✅ 단위 테스트 및 E2E 테스트 완료
- **발견된 문제점**: 이벤트 중복 생성, Summary 품질, 타입 분류 정확도

### Phase 3.1: 즉시 개선 (정규식 기반) - 완료

- ✅ 이벤트 중복 생성 방지 (117개 → 67개, 1:1 매핑 달성)
- ✅ Summary 품질 개선 (줄바꿈 정리, 의미 있는 위치에서 자르기)
- ✅ 타입 분류 엄격화 (구체적인 패턴 사용)

### Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료

- ✅ LLM 서비스 구현 (gpt-4.1-mini, 파일 기반 캐싱, `.env` 자동 로드)
- ✅ 이벤트 정규화 모듈에 LLM 옵션 추가 (`use_llm` 파라미터)
- ✅ LLM 기반 E2E 테스트 완료 (67개 Turn → 67개 Event, 1:1 매핑 달성)
- ✅ E2E 테스트 결과 분석 완료

**Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선** - 완료
- ✅ 병렬 처리 구현 (224초 → 44.99초, 약 5배 향상)
- ✅ 캐시 시스템 개선 (SHA-256 해시, 원자적 저장, 텍스트 해시 검증)
- ✅ 캐시 성능 검증: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상)

### Phase 3.3: 결과 평가 방법 구축 - 완료

- ✅ 정성적 평가 도구 구현 (`backend/builders/evaluation.py`)
- ✅ Golden 파일 관리 도구 구현
- ✅ 수동 검증 프로세스 실행 완료
- ⏸️ Golden 파일 생성: 보류 (Phase 3.4 완료 후 작성 예정)

### Phase 3.4: 이벤트 정규화 품질 개선 (Iterative Improvement Cycle)

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

**⚠️ 컨텍스트**: Phase 4 완료 후 문제 발견 → Phase 3으로 돌아온 개선 작업

**발견된 문제점**:
- Timeline: 이벤트 타입 분류 부정확, Summary 품질 낮음
- Issue Cards: Summary 품질 문제, Root cause/Fix/Validation 추출 품질 낮음

**완료된 작업**:
- [x] 수동 검증 파일 재작성 및 검증 (HTML 형식, 67개 이벤트)
- [x] 정량적/정성적 분석 완료 (타입 분류 정확도 62.69%, 문제 패턴 분류)
- [x] 문제 원인 분석 및 개선 방안 도출
- [x] 개선 작업 실행 (Type 추출 로직, Summary 로직, LLM 프롬프트 개선)
- [x] **타입 체계 개선 구현 완료** (2025-12-26)
  - [x] EventType.ARTIFACT 제거, EventType.CODE_GENERATION 추가
  - [x] ArtifactAction Enum 추가
  - [x] 분류 로직 개선 (is_code_generation_turn, create_code_generation_event)
  - [x] LLM 프롬프트 수정
  - [x] 평가 도구 업데이트
  - [x] E2E 테스트 재실행 및 검증 완료

**상세 개선 계획**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 참조

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**⚠️ 참고**: E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)**로 돌아가서 개선 작업을 수행한 후 다시 Phase 4 E2E 테스트를 재실행합니다

### 기본 구현 - 완료

- ✅ Timeline 빌더 구현 (`build_timeline()`)
- ✅ Issue Cards 빌더 구현 (`build_issue_cards()`)
  - DebugEvent 기반 이슈 탐지, 슬라이딩 윈도우 그룹화
  - Symptom/Root cause/Fix/Validation 추출 (패턴 기반)
- ✅ 단위 테스트 및 E2E 테스트 완료 (구조적 정합성 검증 완료)

**⚠️ E2E 테스트 상태**:
- 구조적 정합성 검증 완료 (테스트 통과)
- 실제 내용 품질 검증은 미완료 (Phase 4.5, 4.6에서 개선 예정)

### Phase 4.5: Timeline 구조화 개선 (진행 중)

**목표**: Timeline을 단순 나열에서 구조화된 작업 항목별 그룹으로 개선

**발견된 문제점**:
- Timeline이 단순히 Event를 seq 1, 2, 3... 순서로 나열
- 주요 작업 내용이 항목화되지 않음
- 작업 내용 중 이슈 발생 여부 표시 안 됨
- 작업 결과 연결 정보 부족

**개선 목표**:
1. Phase/Subphase별로 주요 작업 항목 추출 및 항목화 (1, 2, 3, 4...)
2. 각 항목의 작업 내용 명확화 (LLM 기반 또는 패턴 기반)
3. 작업 내용 중 이슈 발생 여부 표시 (Issue Card와 연결)
4. 작업 결과 연결 정보 추가 (코드 스니펫, 파일, Git commit 등)

**구현 계획**:
- [x] Timeline 구조화 모델 정의 (`TimelineSection` 모델 추가)
- [x] Timeline 구조화 빌더 구현 (`build_structured_timeline()`)
  - [x] Phase/Subphase별 그룹화 로직
  - [x] 주요 작업 항목 추출 로직 (패턴 기반, LLM 옵션 추가 예정)
  - [x] 이슈 연결 로직
  - [x] 작업 결과 연결 정보 추출 로직
- [x] LLM 기반 작업 항목 추출 (선택적) (2025-12-26 완료)
  - [x] LLM 프롬프트 설계 및 캐싱 로직 적용
  - [x] extract_main_tasks_with_llm() 함수 구현
  - [x] timeline_builder에 use_llm 파라미터 통합
- [x] 테스트 작성 및 E2E 테스트 업데이트 (2025-12-26 완료)
  - [x] 단위 테스트 작성 (test_structured_timeline_pattern_based, test_structured_timeline_llm_based)
  - [x] E2E 테스트 업데이트 (test_timeline_issues_e2e_with_llm에서 build_structured_timeline 사용)
  - [x] E2E 테스트 실행 완료 (7개 sections 생성, 패턴 기반 fallback 사용)

**Timeline 품질 평가 및 수동 검증** (2025-12-26 완료):
- [x] E2E 테스트 결과 분석 (결과 파일: `tests/timeline_issues_e2e_llm_20251226_130658.json`)
  - Timeline Section 개수 및 구조 분석 (7개 섹션, 67개 이벤트)
  - Section 제목/요약 품질 평가 (제목 품질 문제 발견: 모든 제목이 이벤트 타입만 나열)
  - 이슈 연결 정확성 검증 (100% 연결률)
  - 작업 결과 연결 정보 완성도 확인 (85.7% 섹션에 코드 스니펫/파일/Artifact 포함)
- [x] Timeline 품질 평가 리포트 생성 (`tests/reports/timeline_quality_evaluation.json`)
- [x] 수동 검증 및 개선점 도출 (`tests/reports/timeline_quality_analysis.md`)
  - **주요 발견사항**: 제목 품질 문제 (7개 섹션 모두), Artifact 중복 문제 (4개 섹션)
  - **품질 점수**: 45/100
  - **개선 권장사항**: 제목 생성 로직 개선, Artifact 중복 제거

**산출물**: 구조화된 Timeline 모델, Timeline 구조화 빌더, E2E 테스트 완료 및 검증 리포트, Timeline 품질 평가 리포트

### Phase 4.6: Issue Card 품질 개선 (완료)

**목표**: Issue Card의 symptom → root_cause → fix → validation 체인을 LLM 기반으로 개선하여 내용 품질 향상

**발견된 문제점** (개선 전):
- Symptom: 단순히 Turn body 처음 500자 잘라내기
- Root cause: 패턴 매칭으로 텍스트 잘라내기 (중간 과정 텍스트 포함)
- Fix: DebugEvent의 summary만 사용 (구체적이지 않음)
- Validation: 패턴 매칭으로 텍스트 잘라내기 (불완전한 텍스트)

**개선 결과** (2025-12-26):
- Symptom: 평균 길이 82.5자 → 23.5자 (약 3.5배 개선, 핵심만 추출)
- Fix: 2개 → 12개 (6배 증가, 구체적이고 상세한 해결 방법)
- Validation: 명확하고 구체적인 검증 방법 추출
- Root cause: 프롬프트 개선 완료 (중간 과정 텍스트 제거 지시 추가)
- 품질 점수: 94/100
- 디버그 부분을 각 이슈로 나누는 로직 점검 필요

**구현 계획**:
- [x] LLM 기반 추출 함수 구현 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`) (2025-12-26 완료)
  - 각 함수는 캐싱 로직 적용 (SHA-256 해시 기반)
  - Fallback 로직 유지 (LLM 실패 시 패턴 기반)
  - 재시도 로직 적용 (최대 3회, 지수 백오프)
- [x] Issue Builder에 LLM 기반 추출 통합 (`build_issue_cards()` 함수에 `use_llm` 파라미터 추가) (2025-12-26 완료)
- [x] E2E 테스트 업데이트 및 실행 완료 (2025-12-26 완료)
  - LLM 기반 Issue Card 생성 검증 완료
  - 품질 분석 완료 (품질 점수: 94/100)
- [x] Root cause 프롬프트 개선 (중간 과정 텍스트 제거) (2025-12-26 완료)
- [ ] 디버그 이슈 분리 로직 개선 (논리적 이슈 단위로 클러스터링) (선택적, 추후 개선)
- [ ] 단위 테스트 작성 (`tests/test_issues_builder.py`) (선택적, 추후 개선)

### Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토 (진행 중)

**목표**: 
1. 파이프라인 중간 결과를 Fixture와 파일 캐싱으로 관리하여 중복 실행 제거
2. Timeline Section을 Issue Card 생성에 활용
3. Issue Card 생성 로직 전면 재검토 및 개선

**발견된 문제점**:
- 각 테스트가 독립적으로 파싱/이벤트 정규화 재실행 (비효율)
- Timeline Section 생성이 Issue Card 생성 이후에 실행됨
- Timeline Section을 Issue Card에 활용할 수 없음
- Issue Card 품질 문제: LLM이 제대로 적용되지 않은 것으로 보임
  - Root cause에 중간 과정 텍스트 포함
  - Fix summary가 형식적이고 부자연스러움
  - Symptom이 핵심이 아닌 경우 발생
- 각 컴포넌트(symptom, root_cause, fix, validation)가 독립적으로 작동하여 컨텍스트 부족

**⚠️ Phase 4.7 완료 후 발견된 심각한 문제점 (2025-12-26)**:
- **Issue Card 결과가 완전히 엉망**: 사용자 평가 "100점 만점에 -100점"
- **핵심 문제**:
  1. **`extract_issue_with_llm()` 함수가 구현되어 있지만 사용되지 않음**
     - `build_issue_card_from_cluster()` 함수가 각 컴포넌트를 개별적으로 추출
     - 통합 컨텍스트를 활용하지 못함
  2. **Fix 항목이 20개나 생성됨** (각 이벤트마다 하나씩)
     - `extract_fix_with_llm()` 함수가 각 DEBUG 이벤트마다 개별 호출됨
     - 각 fix가 매우 길고 반복적인 템플릿 문구 포함 ("이벤트 요약에 기반하여 구체적인 해결 방법을 추출하고 설명하겠습니다.")
  3. **Symptom이 너무 짧고 구체적이지 않음**
     - "다음 단계" 같은 의미 없는 텍스트만 추출됨
  4. **Title이 잘림**
     - 제목 생성 로직에 문제가 있거나 길이 제한이 너무 짧음
  5. **LLM은 사용되었지만 프롬프트/로직 문제**
     - 캐시 파일 확인 결과 LLM 호출은 정상적으로 이루어짐
     - 하지만 프롬프트가 각 컴포넌트를 개별적으로 요청하여 컨텍스트 부족
     - `extract_issue_with_llm()` 함수가 구현되어 있지만 실제로 호출되지 않음
- **확인된 사항**:
  - LLM 캐시 파일 존재: `cache/issue_*.json` (92개 파일)
  - LLM 호출은 정상적으로 이루어짐 (캐시 히트율 32.84%)
  - 문제는 로직 구조: 통합 컨텍스트를 활용하지 않고 각 컴포넌트를 개별 추출
- **필요한 개선**:
  1. `build_issue_card_from_cluster()` 함수를 `extract_issue_with_llm()` 사용하도록 수정
  2. 각 이벤트마다 개별 fix 추출 대신, 클러스터 전체에 대한 통합 fix 추출
  3. Symptom 추출 프롬프트 개선 (핵심만 추출하도록)
  4. Title 생성 로직 개선 (길이 제한 확대 또는 더 나은 요약)
  5. 통합 컨텍스트(TimelineSection + Events + Turns)를 활용한 일관성 있는 추출

**개선 방향**:
1. **파이프라인 데이터 관리**: 하이브리드 방식 (Fixture + 파일 캐싱)
   - pytest Fixture로 메모리 기반 공유 (빠른 접근)
   - 파일 기반 캐싱으로 영구 저장 (디버깅, 수동 검증)
2. **Issue Card 생성 로직 전면 재검토**:
   - 입력: TimelineSection + 관련 Events + 관련 Turns (통합 컨텍스트)
   - LLM 프롬프트: 구조화된 출력 (현상-원인-개선내용)
   - 출력: 구조화된 IssueCard (Timeline Section과 연결)
3. **이슈 클러스터링**: DEBUG 타입 이벤트 주변 Turn들을 논리적 이슈 단위로 클러스터링

**구현 계획**:

**Phase 4.7.1: 중간 결과 캐싱 모듈 생성**
- [ ] `backend/core/pipeline_cache.py` 생성
  - 파싱 결과 캐싱 (파일 기반)
  - 이벤트 정규화 결과 캐싱 (파일 기반)
  - Timeline Section 결과 캐싱 (파일 기반)
  - 캐시 키 생성 (입력 파일 해시 + use_llm 플래그)
  - 캐시 무효화 전략 (입력 파일 변경 감지)

**Phase 4.7.2: pytest Fixture 추가**
- [ ] `tests/conftest.py`에 Fixture 추가
  - `parsed_data` fixture (세션 스코프)
  - `normalized_events` fixture (세션 스코프, use_llm 파라미터)
  - `timeline_sections` fixture (세션 스코프, use_llm 파라미터)
  - 각 Fixture는 pipeline_cache 모듈 사용

**Phase 4.7.3: Issue Card 생성 로직 개선** - ✅ 완료 (2025-12-27)
- [x] `backend/builders/issues_builder.py` 수정
  - [x] `build_issue_cards()` 함수 시그니처 변경: `timeline_sections` 파라미터 추가
  - [x] DEBUG 이벤트 클러스터링 로직 구현 (논리적 이슈 단위로 그룹화)
  - [x] Timeline Section과 Issue Card 매칭 로직 구현
  - [x] **`build_issue_card_from_cluster()` 함수 수정**:
    - [x] 개별 추출 함수 호출 제거 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`)
    - [x] `extract_issue_with_llm()` 한 번 호출로 통합 (통합 컨텍스트 기반)
    - [x] 모든 필드에 fallback 적용 (일관성):
      - `title`: `generate_issue_title_from_cluster()` 사용
      - `symptom`: 첫 번째 User Turn 사용
      - `root_cause`: 패턴 기반 추출
      - `fix`: 패턴 기반 추출
      - `validation`: 패턴 기반 추출
  - [x] **`build_issue_card_from_window()` 함수 수정**:
    - [x] window를 클러스터로 변환하여 `extract_issue_with_llm()` 사용
    - [x] 개별 추출 함수 호출 제거
    - [x] 모든 필드에 fallback 적용 (동일한 전략)

**Phase 4.7.4: LLM 서비스 리팩토링 및 통합** - ✅ 완료 (2025-12-27)
- [x] `backend/core/constants.py` 수정
  - [x] `LLM_MODEL = "gpt-4.1-mini"` 상수 추가 (커서룰에 맞춰 통일)
- [x] `backend/core/llm_service.py` 수정
  - [x] **공통 LLM 호출 함수 추출**: `_call_llm_with_retry()` 함수 생성
    - 캐시 확인/저장 로직 통합
    - 재시도 로직 (지수 백오프) 통합
    - 예외 처리 및 fallback 통합
  - [x] **모든 함수에서 `LLM_MODEL` 상수 사용**: 하드코딩된 모델명 제거
  - [x] **`extract_issue_with_llm()` 함수 개선**:
    - 반환값에 `title` 필드 추가 (필수)
    - 프롬프트에 title 생성 규칙 추가
    - 반환 구조: `{"title": str, "symptom": str, "root_cause": dict, "fix": dict, "validation": str}`
  - [x] **개별 추출 함수 제거**:
    - `extract_symptom_with_llm()` 제거
    - `extract_root_cause_with_llm()` 제거
    - `extract_fix_with_llm()` 제거
    - `extract_validation_with_llm()` 제거
  - 참고: 모든 LLM 호출 함수에서 `_call_llm_with_retry()` 사용 (향후 리팩토링 가능)

**Phase 4.7.5: IssueCard 모델 확장**
- [ ] `backend/core/models.py` 수정
  - `IssueCard` 모델에 필드 추가:
    - `section_id: Optional[str]` - 연결된 Timeline Section ID
    - `section_title: Optional[str]` - 연결된 Timeline Section 제목
    - `related_events: List[str]` - 관련 Event ID 리스트
    - `related_turns: List[int]` - 관련 Turn 인덱스 리스트
    - `confidence_score: Optional[float]` - 추출 신뢰도 점수

**Phase 4.7.6: 테스트 코드 수정**
- [ ] `tests/test_timeline_issues_e2e.py` 수정
  - Fixture 사용으로 변경 (parsed_data, normalized_events, timeline_sections)
  - 실행 순서 변경: Timeline Section 생성 → Issue Card 생성
  - 새로운 Issue Card 생성 로직 검증

**Phase 4.7.7: 캐시 무효화 전략 구현** - ✅ 완료 (이전 Phase에서 완료됨)
- [x] `backend/core/pipeline_cache.py`에 무효화 로직 추가
  - [x] 입력 파일 변경 감지 (파일 해시 비교) - 각 함수에서 자동 구현됨
  - [x] 자동 무효화 (캐시 키 기반) - 파일 해시 불일치 시 자동 무효화
  - [x] 수동 무효화 옵션 (테스트용) - `invalidate_cache()` 함수 구현됨

**검증 계획**:
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 캐시 동작 확인 (파일 저장/로드)
  - [x] 실행 순서 확인 (Timeline → Issue)
  - [x] 성능 개선 확인 (중복 실행 제거)
  - [x] 하위 호환성 확인 (기존 테스트 통과)
- [x] Issue Card 품질 평가 (2025-12-27 완료)
  - [x] 새로운 로직으로 생성된 Issue Card 품질 분석
    - **핵심 개선 사항 확인**:
      - Fix 항목: 20개 → 1개 (클러스터당, 95% 감소) ✅
      - Title: LLM 생성으로 품질 향상 ✅
      - Symptom: 구체적이고 명확함 ✅
      - Root Cause: 중간 과정 텍스트 제거, 핵심만 포함 ✅
      - Fix: 통합 컨텍스트 기반으로 구체적이고 명확함 ✅
      - Validation: 구체적인 검증 방법 제시 ✅
  - [x] Timeline Section 연결 정확성 검증 (100% 연결률) ✅
  - [x] LLM 적용 여부 확인 (2회 호출, 클러스터당 1회) ✅

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

**⚠️ 중요**: Phase 5는 패턴 기반 처리입니다 (LLM 미사용)
- 스니펫 ID 생성: 규칙 기반 (SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang})
- 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
- 중복 제거: 해시 기반 (SHA-256)
- 링킹: Turn/Event 인덱스 매칭

**입력-처리-출력**:
```
입력: Turns (code_blocks), Events, IssueCards, SessionMeta
처리: CodeBlock → Snippet 변환 → 중복 제거 → 링킹 → snippets.json 생성
출력: snippets.json, 업데이트된 Events/IssueCards (snippet_refs 포함)
```

**구현 계획**:

**Phase 5.1: Snippet 모델 정의** - ✅ 완료
- [x] `backend/core/models.py`에 Snippet 모델 추가
  - [x] snippet_id, lang, code, source, links, snippet_hash, aliases 필드

**Phase 5.2: 스니펫 관리 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_manager.py` 생성
  - [x] 스니펫 ID 생성 함수 (generate_snippet_id)
  - [x] 코드 정규화 및 해시 생성 함수 (normalize_code, generate_snippet_hash)
  - [x] 언어 판별 함수 (detect_language, fence_lang 우선 → 휴리스틱)
  - [x] CodeBlock → Snippet 변환 함수 (code_blocks_to_snippets)
  - [x] 중복 제거 로직 (deduplicate_snippets, 해시 기반)
  - [x] 링킹 로직 (link_snippets_to_events, link_snippets_to_issues)
  - [x] 통합 처리 함수 (process_snippets)

**Phase 5.3: 스니펫 저장 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_storage.py` 생성
  - [x] snippets.json 생성 함수 (generate_snippets_json)

**Phase 5.4: 파이프라인 캐싱 통합 (선택적)**
- [ ] `backend/core/pipeline_cache.py`에 스니펫 캐싱 추가 (선택적)
  - [ ] get_or_create_snippets() 함수 추가

**Phase 5.5: 테스트 작성** - ✅ 완료
- [x] `tests/test_snippet_manager.py` 작성 (단위 테스트)
  - [x] test_generate_snippet_id()
  - [x] test_normalize_code()
  - [x] test_generate_snippet_hash()
  - [x] test_detect_language()
  - [x] test_code_blocks_to_snippets()
  - [x] test_deduplicate_snippets()
  - [x] test_link_snippets_to_events()
  - [x] test_link_snippets_to_issues()
- [x] `tests/test_snippet_e2e.py` 작성 (E2E 테스트)
  - [x] test_snippet_e2e_with_llm() - 전체 파이프라인 통합 테스트
    - 실제 입력 파일 사용 (docs/cursor_phase_6_3.md)
    - 파싱 → 이벤트 정규화 → Timeline → Issue Cards → 스니펫 처리
    - snippets.json 생성 및 검증
    - Event/IssueCard 링킹 검증

**검증 계획**:
- [ ] 단위 테스트 실행 및 통과 확인
- [ ] E2E 테스트 실행 및 검증
  - 스니펫 ID 형식 검증
  - 중복 제거 검증 (해시 기반)
  - Event 링킹 검증 (Event.snippet_refs)
  - Issue Card 링킹 검증 (IssueCard.snippet_refs)
  - snippets.json 구조 검증
- [ ] E2E 테스트 결과 분석 및 리포트 생성

---

## Phase 6-8: 미완료 (간략 요약)

### Phase 6: 백엔드 API 구현
- [ ] FastAPI 엔드포인트 구현 (파싱, Timeline, Issues, Snippets, Export)
- [ ] Markdown 렌더러 구현
- [ ] 테스트 및 E2E 테스트 (실제 서버 실행)

### Phase 7: 프론트엔드 UI 구현
- [ ] Next.js 기반 웹 UI (메인 페이지, 입력 패널, 결과 미리보기, Export 패널)
- [ ] API 클라이언트 및 타입 정의
- [ ] 스타일링 (Tailwind CSS)

### Phase 8: 통합 테스트 및 QA
- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 4.7 완료, Phase 5 진행 예정 (코드 스니펫 분리 및 저장)

**마지막 업데이트**: 2025-12-27

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3.0-3.3: 이벤트 정규화 기본 구현 및 평가 방법 구축 (2025-12-20~23)
- Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선 (2025-12-23~26)
  - 타입 체계 개선 완료 (CODE_GENERATION 추가, ARTIFACT 제거)
- Phase 4: Timeline 및 Issue Cards 생성 기본 구현 (2025-12-26)
  - LLM 기반 E2E 테스트 완료
- Phase 4.5: Timeline 구조화 개선 및 품질 평가 (2025-12-26)
  - Timeline 품질 평가 완료 (품질 점수: 45/100)
- Phase 4.6: Issue Card 품질 개선 (2025-12-26)
  - LLM 기반 추출 함수 구현 완료
  - E2E 테스트 완료 (품질 점수: 94/100, 하지만 실제 품질 문제 발견)
- Phase 4.7.3-4.7.4: Issue Card 생성 로직 개선 및 LLM 서비스 리팩토링 (2025-12-27 완료)
  - `extract_issue_with_llm()` 통합 함수 사용으로 전환
  - 모든 필드에 일관된 fallback 적용
  - LLM 모델 통일 (`gpt-4.1-mini`)
  - 개별 추출 함수 제거 (539줄 삭제)
  - E2E 테스트 완료: Fix 항목 20개 → 1개 (95% 감소), 품질 대폭 향상

**진행 중인 Phase**:
- Phase 5: 코드 스니펫 분리 및 저장 (진행 중)
  - Phase 5.1: Snippet 모델 정의
  - Phase 5.2: 스니펫 관리 모듈 구현
  - Phase 5.3: 스니펫 저장 모듈 구현
  - Phase 5.4: 파이프라인 캐싱 통합 (선택적)
  - Phase 5.5: 테스트 작성

**다음 단계**:
- Phase 5 완료 후 Phase 6 진행 예정 (백엔드 API 구현)

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.

```

Phase 5.5 테스트 작성 완료. 구현이 완료되었으므로 현재 상황을 요약합니다.

## Phase 5 진행 상황 요약

**완료된 작업**:
- Phase 5.1: Snippet 모델 정의 완료
- Phase 5.2: 스니펫 관리 모듈 구현 완료 (`backend/builders/snippet_manager.py`)
- Phase 5.3: 스니펫 저장 모듈 구현 완료 (`backend/builders/snippet_storage.py`)
- Phase 5.5: 테스트 작성 완료 (단위 테스트 + E2E 테스트)

**생성된 파일**:
- `backend/core/models.py` - Snippet 모델 추가
- `backend/builders/snippet_manager.py` - 스니펫 관리 로직 (ID 생성, 해시, 언어 판별, 변환, 중복 제거, 링킹)
- `backend/builders/snippet_storage.py` - snippets.json 생성
- `tests/test_snippet_manager.py` - 단위 테스트 (8개 테스트 함수)
- `tests/test_snippet_e2e.py` - E2E 테스트

**다음 단계**:
1. 단위 테스트 실행 및 검증
2. E2E 테스트 실행 및 검증
3. 필요 시 로직 개선 (특히 링킹 로직)

단위 테스트를 실행하여 기본 기능을 확인할까요, 아니면 E2E 테스트를 바로 실행할까요?

---

**User**

단위, e2e 모두 확인

---

**Cursor**

단위 테스트부터 실행합니다.


`IssueCard` import 누락을 수정 중입니다.


```python
"""
스니펫 관리 모듈 단위 테스트 (Phase 5)

⚠️ 중요: 실제 데이터만 사용 (Mock 사용 절대 금지)
"""

import pytest
from backend.core.models import CodeBlock, Snippet, Event, EventType, SessionMeta, Turn, IssueCard
from backend.builders.snippet_manager import (
    generate_snippet_id,
    normalize_code,
    generate_snippet_hash,
    detect_language,
    code_blocks_to_snippets,
    deduplicate_snippets,
    link_snippets_to_events,
    link_snippets_to_issues,
    process_snippets,
)


def test_generate_snippet_id():
    """스니펫 ID 생성 규칙 검증"""
    # 기본 케이스
    snippet_id = generate_snippet_id("session_123", 12, 0, "sql")
    assert snippet_id == "SNP-session_123-012-00-sql"

    # lang이 비어있는 경우
    snippet_id = generate_snippet_id("session_123", 12, 0, "")
    assert snippet_id == "SNP-session_123-012-00-text"

    # lang이 None인 경우
    snippet_id = generate_snippet_id("session_123", 12, 0, None)
    assert snippet_id == "SNP-session_123-012-00-text"

    # 블록 인덱스가 큰 경우
    snippet_id = generate_snippet_id("session_123", 1, 99, "python")
    assert snippet_id == "SNP-session_123-001-99-python"


def test_normalize_code():
    """코드 정규화 검증"""
    # CRLF → LF 변환
    code = "line1\r\nline2\r\nline3"
    normalized = normalize_code(code)
    assert "\r" not in normalized
    assert normalized == "line1\nline2\nline3"

    # 트레일링 공백 제거
    code = "line1   \nline2\t\t\nline3  "
    normalized = normalize_code(code)
    lines = normalized.split("\n")
    assert lines[0] == "line1"
    assert lines[1] == "line2"
    assert lines[2] == "line3"


def test_generate_snippet_hash():
    """해시 생성 검증 (동일 코드 → 동일 해시)"""
    code1 = "def hello():\n    print('hello')"
    code2 = "def hello():\n    print('hello')"
    code3 = "def hello():\n    print('world')"

    hash1 = generate_snippet_hash(code1)
    hash2 = generate_snippet_hash(code2)
    hash3 = generate_snippet_hash(code3)

    # 동일 코드는 동일 해시
    assert hash1 == hash2

    # 다른 코드는 다른 해시
    assert hash1 != hash3

    # 해시 길이 검증 (SHA-256은 64자리)
    assert len(hash1) == 64


def test_detect_language():
    """언어 판별 검증 (fence_lang 우선 → 휴리스틱)"""
    # fence_lang 우선
    code = "SELECT * FROM users"
    lang = detect_language(code, fence_lang="python")
    assert lang == "python"  # fence_lang이 우선

    # 휴리스틱: SQL
    code = "SELECT * FROM users WHERE id = 1"
    lang = detect_language(code, fence_lang="")
    assert lang == "sql"

    # 휴리스틱: TypeScript
    code = "import { Component } from 'react'\nexport const App = () => {}"
    lang = detect_language(code, fence_lang="")
    assert lang == "typescript"

    # 휴리스틱: Python
    code = "def hello():\n    print('hello')"
    lang = detect_language(code, fence_lang="")
    assert lang == "python"

    # 휴리스틱: Bash
    code = "npm install react"
    lang = detect_language(code, fence_lang="")
    assert lang == "bash"

    # 판별 실패 → text
    code = "some random text without keywords"
    lang = detect_language(code, fence_lang="")
    assert lang == "text"


def test_code_blocks_to_snippets():
    """CodeBlock → Snippet 변환 검증"""
    session_meta = SessionMeta(
        session_id="test_session_123",
        source_doc="test.md",
    )

    code_blocks = [
        CodeBlock(turn_index=0, block_index=0, lang="sql", code="SELECT * FROM users"),
        CodeBlock(turn_index=0, block_index=1, lang="", code="def hello():\n    pass"),
        CodeBlock(turn_index=1, block_index=0, lang="typescript", code="const x = 1"),
    ]

    snippets = code_blocks_to_snippets(code_blocks, "test_session_123", session_meta)

    assert len(snippets) == 3

    # 첫 번째 스니펫 검증
    assert snippets[0].snippet_id == "SNP-test_session_123-000-00-sql"
    assert snippets[0].lang == "sql"
    assert snippets[0].code == "SELECT * FROM users"
    assert snippets[0].source == {"turn_index": 0, "block_index": 0}

    # 두 번째 스니펫 검증 (lang 비어있음 → 휴리스틱으로 python 감지)
    assert snippets[1].snippet_id.startswith("SNP-test_session_123-000-01-")
    assert snippets[1].lang == "python"  # 휴리스틱으로 감지됨

    # 해시 생성 검증
    assert len(snippets[0].snippet_hash) == 64


def test_deduplicate_snippets():
    """중복 제거 검증 (해시 기반, aliases 포함)"""
    # 동일한 코드를 가진 스니펫 2개 생성
    code = "SELECT * FROM users"

    snippet1 = Snippet(
        snippet_id="SNP-session-000-00-sql",
        lang="sql",
        code=code,
        source={"turn_index": 0, "block_index": 0},
        links={},
        snippet_hash=generate_snippet_hash(code),
        aliases=[],
    )

    snippet2 = Snippet(
        snippet_id="SNP-session-001-00-sql",
        lang="sql",
        code=code,
        source={"turn_index": 1, "block_index": 0},
        links={},
        snippet_hash=generate_snippet_hash(code),  # 동일한 해시
        aliases=[],
    )

    # 다른 코드를 가진 스니펫 1개
    code3 = "SELECT * FROM posts"
    snippet3 = Snippet(
        snippet_id="SNP-session-002-00-sql",
        lang="sql",
        code=code3,
        source={"turn_index": 2, "block_index": 0},
        links={},
        snippet_hash=generate_snippet_hash(code3),
        aliases=[],
    )

    snippets = [snippet1, snippet2, snippet3]
    deduplicated = deduplicate_snippets(snippets)

    # 중복 제거 후 2개만 남아야 함
    assert len(deduplicated) == 2

    # 첫 번째 스니펫이 대표로 유지되고, 두 번째의 ID가 aliases에 추가됨
    representative = None
    for s in deduplicated:
        if s.snippet_id == snippet1.snippet_id:
            representative = s
            break

    assert representative is not None
    assert snippet2.snippet_id in representative.aliases


def test_link_snippets_to_events():
    """Event 링킹 검증"""
    # 스니펫 생성
    snippet = Snippet(
        snippet_id="SNP-session-000-00-sql",
        lang="sql",
        code="SELECT * FROM users",
        source={"turn_index": 0, "block_index": 0},
        links={},
        snippet_hash="test_hash",
        aliases=[],
    )

    # Event 생성 (turn_ref=0)
    session_meta = SessionMeta(session_id="session", source_doc="test.md")
    event = Event(
        seq=1,
        session_id="session",
        turn_ref=0,  # snippet과 동일한 turn_index
        type=EventType.CODE_GENERATION,
        summary="Test event",
        snippet_refs=[],  # 빈 리스트
    )

    snippets, events = link_snippets_to_events([snippet], [event])

    # Event의 snippet_refs 업데이트 검증
    assert len(events) == 1
    assert events[0].snippet_refs == ["SNP-session-000-00-sql"]

    # Snippet의 links에 event_seq 추가 검증
    assert len(snippets) == 1
    assert "event_seq" in snippets[0].links
    assert 1 in snippets[0].links["event_seq"]


def test_link_snippets_to_issues():
    """Issue Card 링킹 검증"""
    # 스니펫 생성
    snippet = Snippet(
        snippet_id="SNP-session-000-00-sql",
        lang="sql",
        code="SELECT * FROM users",
        source={"turn_index": 0, "block_index": 0},
        links={},
        snippet_hash="test_hash",
        aliases=[],
    )

    # Event 생성
    session_meta = SessionMeta(session_id="session", source_doc="test.md")
    event = Event(
        seq=1,
        session_id="session",
        turn_ref=0,
        type=EventType.DEBUG,
        summary="Test event",
        snippet_refs=["SNP-session-000-00-sql"],
    )

    # IssueCard 생성
    issue_card = IssueCard(
        issue_id="ISS-001-1234",
        scope={"session_id": "session"},
        title="Test issue",
        related_events=[1],  # event.seq = 1
        snippet_refs=[],
    )

    snippets, issue_cards = link_snippets_to_issues([snippet], [issue_card], [event])

    # IssueCard의 snippet_refs 업데이트 검증
    assert len(issue_cards) == 1
    assert "SNP-session-000-00-sql" in issue_cards[0].snippet_refs

    # Snippet의 links에 issue_id 추가 검증
    assert len(snippets) == 1
    assert snippets[0].links["issue_id"] == "ISS-001-1234"


def test_process_snippets_integration():
    """전체 파이프라인 통합 테스트"""
    # Turn 생성
    code_block = CodeBlock(turn_index=0, block_index=0, lang="sql", code="SELECT * FROM users")
    turn = Turn(
        turn_index=0,
        speaker="Cursor",
        body="테스트",
        code_blocks=[code_block],
        path_candidates=[],
    )

    # SessionMeta 생성
    session_meta = SessionMeta(session_id="test_session", source_doc="test.md")

    # Event 생성
    event = Event(
        seq=1,
        session_id="test_session",
        turn_ref=0,
        type=EventType.CODE_GENERATION,
        summary="Test",
        snippet_refs=[],
    )

    # IssueCard 생성
    issue_card = IssueCard(
        issue_id="ISS-001",
        scope={"session_id": "test_session"},
        title="Test",
        related_events=[1],
        snippet_refs=[],
    )

    # 전체 파이프라인 실행
    snippets, events, issue_cards = process_snippets(
        turns=[turn],
        events=[event],
        issue_cards=[issue_card],
        session_meta=session_meta,
    )

    # 검증
    assert len(snippets) == 1
    assert snippets[0].snippet_id.startswith("SNP-test_session-000-00-")
    assert events[0].snippet_refs == [snippets[0].snippet_id]
    assert issue_cards[0].snippet_refs == [snippets[0].snippet_id]

```

단위 테스트 9개 모두 통과. E2E 테스트 실행 중입니다.


IssueCard의 snippet_refs에 임시 형식(`turn_34_block_1`)이 남아있습니다. IssueCard 생성 시 snippet_refs가 설정되는 위치를 확인 중입니다.


```python
"""
Issue Cards 빌더 모듈

정규화된 이벤트와 Turn으로부터 Issue Cards를 생성합니다.
Phase 4.7: Timeline Section을 활용한 개선된 Issue Card 생성
"""

import re
from typing import List, Optional, Dict, Tuple
from collections import defaultdict
from backend.core.models import (
    Event,
    EventType,
    Turn,
    SessionMeta,
    IssueCard,
    TimelineSection,
)
from backend.core.constants import DEBUG_TRIGGERS, IssueStatus, USE_LLM_BY_DEFAULT

# 슬라이딩 윈도우 크기 (최근 N개 Turn 내에서 연결)
WINDOW_SIZE = 10

# Symptom 탐지 패턴 (User 발화에서 문제 제기)
SYMPTOM_PATTERN = re.compile(
    r"(?i)\b(없|안 보|에러|문제|왜|%\s*증가|%\s*감소|안 됨|실패|오류)\b"
)

# DEBUG 이벤트 클러스터링: 최대 거리 (seq 차이)
DEBUG_CLUSTER_MAX_DISTANCE = 5


def build_issue_cards(
    turns: List[Turn],
    events: List[Event],
    session_meta: SessionMeta,
    use_llm: bool = USE_LLM_BY_DEFAULT,
    timeline_sections: Optional[List[TimelineSection]] = None,
) -> List[IssueCard]:
    """
    Turn과 Event로부터 Issue Cards 생성 (Phase 4.7 개선 버전)

    ⚠️ 중요: 기본적으로 LLM을 사용합니다 (use_llm=True).
    패턴 기반을 사용하려면 명시적으로 use_llm=False를 전달하세요.

    Args:
        turns: Turn 리스트
        events: Event 리스트
        session_meta: 세션 메타데이터
        use_llm: LLM 사용 여부 (기본값: True, USE_LLM_BY_DEFAULT 상수 사용)
        timeline_sections: Timeline Section 리스트 (선택적, Phase 4.7)

    Returns:
        IssueCard 리스트
    """
    issue_cards = []

    # Phase 4.7: Timeline Section이 제공된 경우 새로운 로직 사용
    if timeline_sections:
        # 1. DEBUG 이벤트 클러스터링 (논리적 이슈 단위로 그룹화)
        debug_clusters = cluster_debug_events(events)

        # 2. 각 클러스터에 대해 Issue Card 생성
        for cluster_events in debug_clusters:
            # 3. Timeline Section 매칭
            matched_section = match_timeline_section(cluster_events, timeline_sections)

            # 4. 통합 컨텍스트 구성 (Section + Events + Turns)
            related_turns = get_related_turns(cluster_events, turns)

            # 5. Issue Card 생성
            issue_card = build_issue_card_from_cluster(
                cluster_events=cluster_events,
                related_turns=related_turns,
                matched_section=matched_section,
                session_meta=session_meta,
                use_llm=use_llm,
            )

            if issue_card:
                issue_cards.append(issue_card)
    else:
        # 기존 로직 (하위 호환성)
        # 1. Symptom seed 탐지 (User 발화에서 문제 제기)
        seeds = find_symptom_seeds(turns)

        for seed_idx, seed_turn in seeds:
            # 2. 슬라이딩 윈도우 내에서 연결 후보 탐색
            window_turns = turns[seed_idx : seed_idx + WINDOW_SIZE]
            window_events = [
                e
                for e in events
                if seed_idx <= e.turn_ref < seed_idx + WINDOW_SIZE
            ]

            # 3. Issue Card 구성
            issue_card = build_issue_card_from_window(
                seed_turn=seed_turn,
                window_turns=window_turns,
                window_events=window_events,
                seed_idx=seed_idx,
                session_meta=session_meta,
                use_llm=use_llm,
            )

            if issue_card:
                issue_cards.append(issue_card)

    return issue_cards


def cluster_debug_events(events: List[Event]) -> List[List[Event]]:
    """
    DEBUG 이벤트를 논리적 이슈 단위로 클러스터링

    Args:
        events: Event 리스트

    Returns:
        DEBUG 이벤트 클러스터 리스트 (각 클러스터는 하나의 논리적 이슈)
    """
    # DEBUG 이벤트만 필터링
    debug_events = [e for e in events if e.type == EventType.DEBUG]

    if not debug_events:
        return []

    # seq 순서로 정렬
    debug_events.sort(key=lambda e: e.seq)

    # 클러스터링: seq 차이가 MAX_DISTANCE 이내면 같은 클러스터
    clusters = []
    current_cluster = [debug_events[0]]

    for i in range(1, len(debug_events)):
        prev_event = debug_events[i - 1]
        curr_event = debug_events[i]

        # seq 차이 확인
        seq_diff = curr_event.seq - prev_event.seq

        if seq_diff <= DEBUG_CLUSTER_MAX_DISTANCE:
            # 같은 클러스터에 추가
            current_cluster.append(curr_event)
        else:
            # 새 클러스터 시작
            if current_cluster:
                clusters.append(current_cluster)
            current_cluster = [curr_event]

    # 마지막 클러스터 추가
    if current_cluster:
        clusters.append(current_cluster)

    return clusters


def match_timeline_section(
    cluster_events: List[Event],
    timeline_sections: List[TimelineSection],
) -> Optional[TimelineSection]:
    """
    DEBUG 이벤트 클러스터와 Timeline Section 매칭

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        timeline_sections: Timeline Section 리스트

    Returns:
        매칭된 TimelineSection 또는 None
    """
    if not cluster_events:
        return None

    # 클러스터의 Event seq 리스트
    cluster_event_seqs = {e.seq for e in cluster_events}

    # 각 Section의 events와 겹치는 정도 계산
    best_match = None
    best_overlap = 0

    for section in timeline_sections:
        section_event_seqs = set(section.events)

        # 겹치는 Event 수 계산
        overlap = len(cluster_event_seqs & section_event_seqs)

        if overlap > best_overlap:
            best_overlap = overlap
            best_match = section

    # 겹치는 Event가 1개 이상이면 매칭 성공
    if best_overlap > 0:
        return best_match

    return None


def get_related_turns(cluster_events: List[Event], turns: List[Turn]) -> List[Turn]:
    """
    클러스터 이벤트와 관련된 Turn 수집

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        turns: Turn 리스트

    Returns:
        관련 Turn 리스트
    """
    related_turn_indices = {e.turn_ref for e in cluster_events}

    # 윈도우 확장: 클러스터 앞뒤로 WINDOW_SIZE/2만큼 추가
    if related_turn_indices:
        min_turn_idx = min(related_turn_indices)
        max_turn_idx = max(related_turn_indices)

        # 윈도우 확장
        window_start = max(0, min_turn_idx - WINDOW_SIZE // 2)
        window_end = min(len(turns), max_turn_idx + WINDOW_SIZE // 2 + 1)

        related_turn_indices.update(range(window_start, window_end))

    # Turn 수집
    related_turns = [
        turn for idx, turn in enumerate(turns)
        if idx in related_turn_indices
    ]

    # turn_index 순서로 정렬
    related_turns.sort(key=lambda t: t.turn_index)

    return related_turns


def build_issue_card_from_cluster(
    cluster_events: List[Event],
    related_turns: List[Turn],
    matched_section: Optional[TimelineSection],
    session_meta: SessionMeta,
    use_llm: bool = USE_LLM_BY_DEFAULT,
) -> Optional[IssueCard]:
    """
    DEBUG 이벤트 클러스터로부터 Issue Card 생성 (Phase 4.7)

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        related_turns: 관련 Turn 리스트
        matched_section: 매칭된 TimelineSection (선택적)
        session_meta: 세션 메타데이터
        use_llm: LLM 사용 여부

    Returns:
        IssueCard 또는 None
    """
    if not cluster_events:
        return None

    # 통합 컨텍스트 기반 Issue 추출 (Phase 4.7.3)
    title = None
    symptom = None
    root_cause = None
    fix = None
    validation = None

    if use_llm:
        try:
            from backend.core.llm_service import extract_issue_with_llm

            integrated_result = extract_issue_with_llm(
                timeline_section=matched_section,
                cluster_events=cluster_events,
                related_turns=related_turns,
            )

            if integrated_result:
                title = integrated_result.get("title")
                symptom = integrated_result.get("symptom")
                root_cause = integrated_result.get("root_cause")
                fix = integrated_result.get("fix")
                validation = integrated_result.get("validation")
        except Exception as e:
            logger.warning(f"[WARNING] Integrated issue extraction failed: {e}, using fallback")

    # Fallback 적용 (일관성 있게 모든 필드에 적용)
    # Title fallback
    if not title:
        title = generate_issue_title_from_cluster(cluster_events, root_cause, matched_section)

    # Symptom fallback
    if not symptom:
        # 첫 번째 User Turn 사용
        for turn in related_turns:
            if turn.speaker == "User":
                symptom = turn.body[:500]
                break

    # Symptom이 없으면 카드 생성 안 함
    if not symptom:
        return None

    symptoms = [symptom] if symptom else []

    # Root cause fallback
    if not root_cause:
        for turn in related_turns:
            if turn.speaker == "Cursor":
                if DEBUG_TRIGGERS["root_cause"].search(turn.body):
                    root_cause = {
                        "status": IssueStatus.CONFIRMED.value,
                        "text": extract_root_cause_text(turn.body),
                    }
                    break

        # Root cause가 없으면 hypothesis로 설정
        if not root_cause:
            for turn in related_turns:
                if turn.speaker == "Cursor" and DEBUG_TRIGGERS["error"].search(turn.body):
                    root_cause = {
                        "status": IssueStatus.HYPOTHESIS.value,
                        "text": turn.body[:300],
                    }
                    break

    # Fix fallback
    if not fix:
        # 첫 번째 DEBUG 이벤트의 summary 사용
        for event in cluster_events:
            if event.type == EventType.DEBUG and event.snippet_refs:
                fix = {
                    "summary": event.summary,
                    "snippet_refs": event.snippet_refs,
                }
                break

    fixes = [fix] if fix else []

    # Validation fallback
    if not validation:
        for turn in related_turns:
            if DEBUG_TRIGGERS["validation"].search(turn.body):
                validation = extract_validation_text(turn.body)
                if validation:
                    break

    validations = [validation] if validation else []

    # Root cause 또는 Fix 중 하나라도 있어야 카드 생성
    if not root_cause and not fixes:
        return None

    # Issue ID 생성
    first_event = cluster_events[0]
    issue_id = f"ISS-{first_event.seq:03d}-{hash(first_event.summary[:100]) % 10000:04d}"

    # 관련 Artifact 수집
    related_artifacts = []
    seen_paths = set()
    for event in cluster_events:
        for artifact in event.artifacts:
            path = artifact.get("path", "")
            if path and path not in seen_paths:
                seen_paths.add(path)
                related_artifacts.append(artifact)

    # Snippet 참조 수집 (Phase 5: process_snippets에서 실제 snippet_id로 업데이트됨)
    # 여기서는 빈 리스트로 시작 (임시 형식 제거)
    snippet_refs = []

    # 관련 Event seq 리스트
    related_event_seqs = [e.seq for e in cluster_events]

    # 관련 Turn 인덱스 리스트
    related_turn_indices = [t.turn_index for t in related_turns]

    # 신뢰도 점수 계산 (간단한 휴리스틱)
    confidence_score = calculate_confidence_score(cluster_events, root_cause, fixes)

    return IssueCard(
        issue_id=issue_id,
        scope={
            "session_id": session_meta.session_id,
            "phase": session_meta.phase,
            "subphase": session_meta.subphase,
        },
        title=title,
        symptoms=symptoms,
        root_cause=root_cause,
        evidence=[],
        fix=fixes,
        validation=validations,
        related_artifacts=related_artifacts,
        snippet_refs=snippet_refs,
        # Phase 4.7 추가 필드
        section_id=matched_section.section_id if matched_section else None,
        section_title=matched_section.title if matched_section else None,
        related_events=related_event_seqs,
        related_turns=related_turn_indices,
        confidence_score=confidence_score,
    )


def generate_issue_title_from_cluster(
    cluster_events: List[Event],
    root_cause: Optional[dict],
    matched_section: Optional[TimelineSection],
) -> str:
    """
    클러스터로부터 Issue 제목 생성

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        root_cause: Root cause 딕셔너리 (선택적)
        matched_section: 매칭된 TimelineSection (선택적)

    Returns:
        Issue 제목
    """
    # Section 제목이 있으면 우선 사용
    if matched_section and matched_section.title:
        if root_cause:
            root_cause_text = root_cause.get("text", "")[:50]
            if root_cause_text:
                return f"{matched_section.title} - {root_cause_text}"
        return matched_section.title

    # 첫 번째 이벤트의 summary 사용
    if cluster_events:
        summary = cluster_events[0].summary[:100]
        if root_cause:
            root_cause_text = root_cause.get("text", "")[:50]
            if root_cause_text:
                return f"{summary} - {root_cause_text}"
        return summary

    return "Issue"


def calculate_confidence_score(
    cluster_events: List[Event],
    root_cause: Optional[dict],
    fixes: List[dict],
) -> float:
    """
    Issue Card 추출 신뢰도 점수 계산

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        root_cause: Root cause 딕셔너리 (선택적)
        fixes: Fix 리스트

    Returns:
        신뢰도 점수 (0.0 ~ 1.0)
    """
    score = 0.0

    # Root cause가 있으면 +0.4
    if root_cause:
        score += 0.4
        # confirmed면 +0.2 추가
        if root_cause.get("status") == IssueStatus.CONFIRMED.value:
            score += 0.2

    # Fix가 있으면 +0.3
    if fixes:
        score += 0.3

    # 클러스터 크기가 적절하면 +0.1 (1~3개 이벤트)
    if 1 <= len(cluster_events) <= 3:
        score += 0.1

    return min(1.0, score)


def find_symptom_seeds(turns: List[Turn]) -> List[tuple]:
    """
    User Turn에서 symptom 후보 탐지

    Returns:
        [(turn_index, Turn), ...]
    """
    seeds = []

    for idx, turn in enumerate(turns):
        if turn.speaker == "User" and SYMPTOM_PATTERN.search(turn.body):
            seeds.append((idx, turn))

    return seeds


def build_issue_card_from_window(
    seed_turn: Turn,
    window_turns: List[Turn],
    window_events: List[Event],
    seed_idx: int,
    session_meta: SessionMeta,
    use_llm: bool = USE_LLM_BY_DEFAULT,
) -> Optional[IssueCard]:
    """
    슬라이딩 윈도우 내에서 Issue Card 구성

    Args:
        seed_turn: Symptom seed Turn
        window_turns: 윈도우 내 Turn 리스트
        window_events: 윈도우 내 Event 리스트
        seed_idx: Seed Turn 인덱스
        session_meta: 세션 메타데이터
        use_llm: LLM 사용 여부 (기본값: False)

    Returns:
        IssueCard 또는 None (조건 미충족 시)
    """
    # 통합 컨텍스트 기반 Issue 추출 (Phase 4.7.3)
    # window를 클러스터로 변환하여 extract_issue_with_llm() 사용
    title = None
    symptom = None
    root_cause = None
    fix = None
    validation = None

    if use_llm:
        try:
            from backend.core.llm_service import extract_issue_with_llm

            # window_events를 클러스터로 변환 (DEBUG 이벤트만)
            cluster_events = [e for e in window_events if e.type == EventType.DEBUG]

            if cluster_events:
                integrated_result = extract_issue_with_llm(
                    timeline_section=None,  # window 방식은 section 없음
                    cluster_events=cluster_events,
                    related_turns=window_turns,
                )

                if integrated_result:
                    title = integrated_result.get("title")
                    symptom = integrated_result.get("symptom")
                    root_cause = integrated_result.get("root_cause")
                    fix = integrated_result.get("fix")
                    validation = integrated_result.get("validation")
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"[WARNING] Integrated issue extraction failed: {e}, using fallback")

    # Fallback 적용 (일관성 있게 모든 필드에 적용)
    # Title fallback
    if not title:
        title = generate_issue_title(seed_turn, root_cause)

    # Symptom fallback
    if not symptom:
        symptom = seed_turn.body[:500]

    symptoms = [symptom] if symptom else []

    # Root cause fallback
    if not root_cause:
        for turn in window_turns:
            if turn.speaker == "Cursor":
                if DEBUG_TRIGGERS["root_cause"].search(turn.body):
                    root_cause = {
                        "status": IssueStatus.CONFIRMED.value,
                        "text": extract_root_cause_text(turn.body),
                    }
                    break

        # Root cause가 없으면 hypothesis로 설정
        if not root_cause:
            for turn in window_turns:
                if turn.speaker == "Cursor" and DEBUG_TRIGGERS["error"].search(turn.body):
                    root_cause = {
                        "status": IssueStatus.HYPOTHESIS.value,
                        "text": turn.body[:300],
                    }
                    break

    # Fix fallback
    if not fix:
        # 첫 번째 DEBUG 이벤트의 summary 사용
        for event in window_events:
            if event.type == EventType.DEBUG and event.snippet_refs:
                fix = {
                    "summary": event.summary,
                    "snippet_refs": event.snippet_refs,
                }
                break

    fixes = [fix] if fix else []

    # Validation fallback
    if not validation:
        for turn in window_turns:
            if DEBUG_TRIGGERS["validation"].search(turn.body):
                validation = extract_validation_text(turn.body)
                if validation:
                    break

    validations = [validation] if validation else []

    # Root cause 또는 Fix 중 하나라도 있어야 카드 생성
    if not root_cause and not fixes:
        return None

    # Issue ID 생성
    issue_id = f"ISS-{seed_idx:03d}-{hash(seed_turn.body[:100]) % 10000:04d}"

    # 관련 Artifact 수집
    related_artifacts = []
    for event in window_events:
        related_artifacts.extend(event.artifacts)

    # 중복 제거
    seen_paths = set()
    unique_artifacts = []
    for artifact in related_artifacts:
        path = artifact.get("path", "")
        if path and path not in seen_paths:
            seen_paths.add(path)
            unique_artifacts.append(artifact)

    # Snippet 참조 수집
    snippet_refs = []
    for event in window_events:
        snippet_refs.extend(event.snippet_refs)

    # 중복 제거
    snippet_refs = list(set(snippet_refs))

    return IssueCard(
        issue_id=issue_id,
        scope={
            "session_id": session_meta.session_id,
            "phase": session_meta.phase,
            "subphase": session_meta.subphase,
        },
        title=title,
        symptoms=symptoms,
        root_cause=root_cause,
        evidence=[],  # Phase 4에서는 기본 구조만, 추후 개선
        fix=fixes,
        validation=validations,
        related_artifacts=unique_artifacts,
        snippet_refs=snippet_refs,
    )


def extract_root_cause_text(text: str) -> str:
    """
    Root cause 텍스트 추출

    Args:
        text: Turn 본문

    Returns:
        Root cause 텍스트 (최대 300자)
    """
    # Root cause 패턴 이후의 텍스트 추출
    match = DEBUG_TRIGGERS["root_cause"].search(text)
    if match:
        start_pos = match.end()
        extracted = text[start_pos:start_pos + 300].strip()
        return extracted

    return text[:300].strip()


def extract_validation_text(text: str) -> str:
    """
    Validation 텍스트 추출

    Args:
        text: Turn 본문

    Returns:
        Validation 텍스트 (최대 200자)
    """
    # Validation 패턴 이후의 텍스트 추출
    match = DEBUG_TRIGGERS["validation"].search(text)
    if match:
        start_pos = match.end()
        extracted = text[start_pos:start_pos + 200].strip()
        return extracted

    return text[:200].strip()


def generate_issue_title(seed_turn: Turn, root_cause: Optional[dict]) -> str:
    """
    Issue 제목 생성

    Args:
        seed_turn: Symptom seed Turn
        root_cause: Root cause 딕셔너리 (선택적)

    Returns:
        Issue 제목
    """
    # Symptom에서 첫 문장 추출
    symptom_text = seed_turn.body.split("\n")[0][:100]

    if root_cause:
        # Root cause가 있으면 결합
        root_cause_text = root_cause.get("text", "")[:50]
        if root_cause_text:
            return f"{symptom_text} - {root_cause_text}"

    return symptom_text


```

E2E 테스트 통과. 결과 확인 및 정리 중입니다.


```markdown
# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (필수)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

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

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**

프로젝트는 Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행합니다.
하지만 Phase 4나 Phase 5에서 문제가 발견되면 **Phase 3으로 돌아가서 이벤트 정규화 로직을 개선**한 후, 다시 Phase 4, 5로 넘어가는 iterative cycle을 돌고 있습니다.

**주의사항**:
- Phase 3, 4, 5의 **기본 순서는 항상 유지**: 3 → 4 → 5
- 개선 작업은 **Phase 3의 서브 Phase (3.1, 3.2, 3.4 등)**로 진행
- Phase 번호는 **절대 섞이지 않음** (3 → 4 → 3.4 → 5 ❌, 3 → 4 → 3.4 → 4 재검증 → 5 ✅)

### Phase 3.0: 기본 구현 (완료)

- ✅ 데이터 모델 정의 (EventType, Event, TimelineEvent, IssueCard)
- ✅ 이벤트 정규화 기본 구현 (규칙 기반 타입 분류)
- ✅ 단위 테스트 및 E2E 테스트 완료
- **발견된 문제점**: 이벤트 중복 생성, Summary 품질, 타입 분류 정확도

### Phase 3.1: 즉시 개선 (정규식 기반) - 완료

- ✅ 이벤트 중복 생성 방지 (117개 → 67개, 1:1 매핑 달성)
- ✅ Summary 품질 개선 (줄바꿈 정리, 의미 있는 위치에서 자르기)
- ✅ 타입 분류 엄격화 (구체적인 패턴 사용)

### Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료

- ✅ LLM 서비스 구현 (gpt-4.1-mini, 파일 기반 캐싱, `.env` 자동 로드)
- ✅ 이벤트 정규화 모듈에 LLM 옵션 추가 (`use_llm` 파라미터)
- ✅ LLM 기반 E2E 테스트 완료 (67개 Turn → 67개 Event, 1:1 매핑 달성)
- ✅ E2E 테스트 결과 분석 완료

**Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선** - 완료
- ✅ 병렬 처리 구현 (224초 → 44.99초, 약 5배 향상)
- ✅ 캐시 시스템 개선 (SHA-256 해시, 원자적 저장, 텍스트 해시 검증)
- ✅ 캐시 성능 검증: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상)

### Phase 3.3: 결과 평가 방법 구축 - 완료

- ✅ 정성적 평가 도구 구현 (`backend/builders/evaluation.py`)
- ✅ Golden 파일 관리 도구 구현
- ✅ 수동 검증 프로세스 실행 완료
- ⏸️ Golden 파일 생성: 보류 (Phase 3.4 완료 후 작성 예정)

### Phase 3.4: 이벤트 정규화 품질 개선 (Iterative Improvement Cycle)

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

**⚠️ 컨텍스트**: Phase 4 완료 후 문제 발견 → Phase 3으로 돌아온 개선 작업

**발견된 문제점**:
- Timeline: 이벤트 타입 분류 부정확, Summary 품질 낮음
- Issue Cards: Summary 품질 문제, Root cause/Fix/Validation 추출 품질 낮음

**완료된 작업**:
- [x] 수동 검증 파일 재작성 및 검증 (HTML 형식, 67개 이벤트)
- [x] 정량적/정성적 분석 완료 (타입 분류 정확도 62.69%, 문제 패턴 분류)
- [x] 문제 원인 분석 및 개선 방안 도출
- [x] 개선 작업 실행 (Type 추출 로직, Summary 로직, LLM 프롬프트 개선)
- [x] **타입 체계 개선 구현 완료** (2025-12-26)
  - [x] EventType.ARTIFACT 제거, EventType.CODE_GENERATION 추가
  - [x] ArtifactAction Enum 추가
  - [x] 분류 로직 개선 (is_code_generation_turn, create_code_generation_event)
  - [x] LLM 프롬프트 수정
  - [x] 평가 도구 업데이트
  - [x] E2E 테스트 재실행 및 검증 완료

**상세 개선 계획**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 참조

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**⚠️ 참고**: E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)**로 돌아가서 개선 작업을 수행한 후 다시 Phase 4 E2E 테스트를 재실행합니다

### 기본 구현 - 완료

- ✅ Timeline 빌더 구현 (`build_timeline()`)
- ✅ Issue Cards 빌더 구현 (`build_issue_cards()`)
  - DebugEvent 기반 이슈 탐지, 슬라이딩 윈도우 그룹화
  - Symptom/Root cause/Fix/Validation 추출 (패턴 기반)
- ✅ 단위 테스트 및 E2E 테스트 완료 (구조적 정합성 검증 완료)

**⚠️ E2E 테스트 상태**:
- 구조적 정합성 검증 완료 (테스트 통과)
- 실제 내용 품질 검증은 미완료 (Phase 4.5, 4.6에서 개선 예정)

### Phase 4.5: Timeline 구조화 개선 (진행 중)

**목표**: Timeline을 단순 나열에서 구조화된 작업 항목별 그룹으로 개선

**발견된 문제점**:
- Timeline이 단순히 Event를 seq 1, 2, 3... 순서로 나열
- 주요 작업 내용이 항목화되지 않음
- 작업 내용 중 이슈 발생 여부 표시 안 됨
- 작업 결과 연결 정보 부족

**개선 목표**:
1. Phase/Subphase별로 주요 작업 항목 추출 및 항목화 (1, 2, 3, 4...)
2. 각 항목의 작업 내용 명확화 (LLM 기반 또는 패턴 기반)
3. 작업 내용 중 이슈 발생 여부 표시 (Issue Card와 연결)
4. 작업 결과 연결 정보 추가 (코드 스니펫, 파일, Git commit 등)

**구현 계획**:
- [x] Timeline 구조화 모델 정의 (`TimelineSection` 모델 추가)
- [x] Timeline 구조화 빌더 구현 (`build_structured_timeline()`)
  - [x] Phase/Subphase별 그룹화 로직
  - [x] 주요 작업 항목 추출 로직 (패턴 기반, LLM 옵션 추가 예정)
  - [x] 이슈 연결 로직
  - [x] 작업 결과 연결 정보 추출 로직
- [x] LLM 기반 작업 항목 추출 (선택적) (2025-12-26 완료)
  - [x] LLM 프롬프트 설계 및 캐싱 로직 적용
  - [x] extract_main_tasks_with_llm() 함수 구현
  - [x] timeline_builder에 use_llm 파라미터 통합
- [x] 테스트 작성 및 E2E 테스트 업데이트 (2025-12-26 완료)
  - [x] 단위 테스트 작성 (test_structured_timeline_pattern_based, test_structured_timeline_llm_based)
  - [x] E2E 테스트 업데이트 (test_timeline_issues_e2e_with_llm에서 build_structured_timeline 사용)
  - [x] E2E 테스트 실행 완료 (7개 sections 생성, 패턴 기반 fallback 사용)

**Timeline 품질 평가 및 수동 검증** (2025-12-26 완료):
- [x] E2E 테스트 결과 분석 (결과 파일: `tests/timeline_issues_e2e_llm_20251226_130658.json`)
  - Timeline Section 개수 및 구조 분석 (7개 섹션, 67개 이벤트)
  - Section 제목/요약 품질 평가 (제목 품질 문제 발견: 모든 제목이 이벤트 타입만 나열)
  - 이슈 연결 정확성 검증 (100% 연결률)
  - 작업 결과 연결 정보 완성도 확인 (85.7% 섹션에 코드 스니펫/파일/Artifact 포함)
- [x] Timeline 품질 평가 리포트 생성 (`tests/reports/timeline_quality_evaluation.json`)
- [x] 수동 검증 및 개선점 도출 (`tests/reports/timeline_quality_analysis.md`)
  - **주요 발견사항**: 제목 품질 문제 (7개 섹션 모두), Artifact 중복 문제 (4개 섹션)
  - **품질 점수**: 45/100
  - **개선 권장사항**: 제목 생성 로직 개선, Artifact 중복 제거

**산출물**: 구조화된 Timeline 모델, Timeline 구조화 빌더, E2E 테스트 완료 및 검증 리포트, Timeline 품질 평가 리포트

### Phase 4.6: Issue Card 품질 개선 (완료)

**목표**: Issue Card의 symptom → root_cause → fix → validation 체인을 LLM 기반으로 개선하여 내용 품질 향상

**발견된 문제점** (개선 전):
- Symptom: 단순히 Turn body 처음 500자 잘라내기
- Root cause: 패턴 매칭으로 텍스트 잘라내기 (중간 과정 텍스트 포함)
- Fix: DebugEvent의 summary만 사용 (구체적이지 않음)
- Validation: 패턴 매칭으로 텍스트 잘라내기 (불완전한 텍스트)

**개선 결과** (2025-12-26):
- Symptom: 평균 길이 82.5자 → 23.5자 (약 3.5배 개선, 핵심만 추출)
- Fix: 2개 → 12개 (6배 증가, 구체적이고 상세한 해결 방법)
- Validation: 명확하고 구체적인 검증 방법 추출
- Root cause: 프롬프트 개선 완료 (중간 과정 텍스트 제거 지시 추가)
- 품질 점수: 94/100
- 디버그 부분을 각 이슈로 나누는 로직 점검 필요

**구현 계획**:
- [x] LLM 기반 추출 함수 구현 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`) (2025-12-26 완료)
  - 각 함수는 캐싱 로직 적용 (SHA-256 해시 기반)
  - Fallback 로직 유지 (LLM 실패 시 패턴 기반)
  - 재시도 로직 적용 (최대 3회, 지수 백오프)
- [x] Issue Builder에 LLM 기반 추출 통합 (`build_issue_cards()` 함수에 `use_llm` 파라미터 추가) (2025-12-26 완료)
- [x] E2E 테스트 업데이트 및 실행 완료 (2025-12-26 완료)
  - LLM 기반 Issue Card 생성 검증 완료
  - 품질 분석 완료 (품질 점수: 94/100)
- [x] Root cause 프롬프트 개선 (중간 과정 텍스트 제거) (2025-12-26 완료)
- [ ] 디버그 이슈 분리 로직 개선 (논리적 이슈 단위로 클러스터링) (선택적, 추후 개선)
- [ ] 단위 테스트 작성 (`tests/test_issues_builder.py`) (선택적, 추후 개선)

### Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토 (진행 중)

**목표**: 
1. 파이프라인 중간 결과를 Fixture와 파일 캐싱으로 관리하여 중복 실행 제거
2. Timeline Section을 Issue Card 생성에 활용
3. Issue Card 생성 로직 전면 재검토 및 개선

**발견된 문제점**:
- 각 테스트가 독립적으로 파싱/이벤트 정규화 재실행 (비효율)
- Timeline Section 생성이 Issue Card 생성 이후에 실행됨
- Timeline Section을 Issue Card에 활용할 수 없음
- Issue Card 품질 문제: LLM이 제대로 적용되지 않은 것으로 보임
  - Root cause에 중간 과정 텍스트 포함
  - Fix summary가 형식적이고 부자연스러움
  - Symptom이 핵심이 아닌 경우 발생
- 각 컴포넌트(symptom, root_cause, fix, validation)가 독립적으로 작동하여 컨텍스트 부족

**⚠️ Phase 4.7 완료 후 발견된 심각한 문제점 (2025-12-26)**:
- **Issue Card 결과가 완전히 엉망**: 사용자 평가 "100점 만점에 -100점"
- **핵심 문제**:
  1. **`extract_issue_with_llm()` 함수가 구현되어 있지만 사용되지 않음**
     - `build_issue_card_from_cluster()` 함수가 각 컴포넌트를 개별적으로 추출
     - 통합 컨텍스트를 활용하지 못함
  2. **Fix 항목이 20개나 생성됨** (각 이벤트마다 하나씩)
     - `extract_fix_with_llm()` 함수가 각 DEBUG 이벤트마다 개별 호출됨
     - 각 fix가 매우 길고 반복적인 템플릿 문구 포함 ("이벤트 요약에 기반하여 구체적인 해결 방법을 추출하고 설명하겠습니다.")
  3. **Symptom이 너무 짧고 구체적이지 않음**
     - "다음 단계" 같은 의미 없는 텍스트만 추출됨
  4. **Title이 잘림**
     - 제목 생성 로직에 문제가 있거나 길이 제한이 너무 짧음
  5. **LLM은 사용되었지만 프롬프트/로직 문제**
     - 캐시 파일 확인 결과 LLM 호출은 정상적으로 이루어짐
     - 하지만 프롬프트가 각 컴포넌트를 개별적으로 요청하여 컨텍스트 부족
     - `extract_issue_with_llm()` 함수가 구현되어 있지만 실제로 호출되지 않음
- **확인된 사항**:
  - LLM 캐시 파일 존재: `cache/issue_*.json` (92개 파일)
  - LLM 호출은 정상적으로 이루어짐 (캐시 히트율 32.84%)
  - 문제는 로직 구조: 통합 컨텍스트를 활용하지 않고 각 컴포넌트를 개별 추출
- **필요한 개선**:
  1. `build_issue_card_from_cluster()` 함수를 `extract_issue_with_llm()` 사용하도록 수정
  2. 각 이벤트마다 개별 fix 추출 대신, 클러스터 전체에 대한 통합 fix 추출
  3. Symptom 추출 프롬프트 개선 (핵심만 추출하도록)
  4. Title 생성 로직 개선 (길이 제한 확대 또는 더 나은 요약)
  5. 통합 컨텍스트(TimelineSection + Events + Turns)를 활용한 일관성 있는 추출

**개선 방향**:
1. **파이프라인 데이터 관리**: 하이브리드 방식 (Fixture + 파일 캐싱)
   - pytest Fixture로 메모리 기반 공유 (빠른 접근)
   - 파일 기반 캐싱으로 영구 저장 (디버깅, 수동 검증)
2. **Issue Card 생성 로직 전면 재검토**:
   - 입력: TimelineSection + 관련 Events + 관련 Turns (통합 컨텍스트)
   - LLM 프롬프트: 구조화된 출력 (현상-원인-개선내용)
   - 출력: 구조화된 IssueCard (Timeline Section과 연결)
3. **이슈 클러스터링**: DEBUG 타입 이벤트 주변 Turn들을 논리적 이슈 단위로 클러스터링

**구현 계획**:

**Phase 4.7.1: 중간 결과 캐싱 모듈 생성**
- [ ] `backend/core/pipeline_cache.py` 생성
  - 파싱 결과 캐싱 (파일 기반)
  - 이벤트 정규화 결과 캐싱 (파일 기반)
  - Timeline Section 결과 캐싱 (파일 기반)
  - 캐시 키 생성 (입력 파일 해시 + use_llm 플래그)
  - 캐시 무효화 전략 (입력 파일 변경 감지)

**Phase 4.7.2: pytest Fixture 추가**
- [ ] `tests/conftest.py`에 Fixture 추가
  - `parsed_data` fixture (세션 스코프)
  - `normalized_events` fixture (세션 스코프, use_llm 파라미터)
  - `timeline_sections` fixture (세션 스코프, use_llm 파라미터)
  - 각 Fixture는 pipeline_cache 모듈 사용

**Phase 4.7.3: Issue Card 생성 로직 개선** - ✅ 완료 (2025-12-27)
- [x] `backend/builders/issues_builder.py` 수정
  - [x] `build_issue_cards()` 함수 시그니처 변경: `timeline_sections` 파라미터 추가
  - [x] DEBUG 이벤트 클러스터링 로직 구현 (논리적 이슈 단위로 그룹화)
  - [x] Timeline Section과 Issue Card 매칭 로직 구현
  - [x] **`build_issue_card_from_cluster()` 함수 수정**:
    - [x] 개별 추출 함수 호출 제거 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`)
    - [x] `extract_issue_with_llm()` 한 번 호출로 통합 (통합 컨텍스트 기반)
    - [x] 모든 필드에 fallback 적용 (일관성):
      - `title`: `generate_issue_title_from_cluster()` 사용
      - `symptom`: 첫 번째 User Turn 사용
      - `root_cause`: 패턴 기반 추출
      - `fix`: 패턴 기반 추출
      - `validation`: 패턴 기반 추출
  - [x] **`build_issue_card_from_window()` 함수 수정**:
    - [x] window를 클러스터로 변환하여 `extract_issue_with_llm()` 사용
    - [x] 개별 추출 함수 호출 제거
    - [x] 모든 필드에 fallback 적용 (동일한 전략)

**Phase 4.7.4: LLM 서비스 리팩토링 및 통합** - ✅ 완료 (2025-12-27)
- [x] `backend/core/constants.py` 수정
  - [x] `LLM_MODEL = "gpt-4.1-mini"` 상수 추가 (커서룰에 맞춰 통일)
- [x] `backend/core/llm_service.py` 수정
  - [x] **공통 LLM 호출 함수 추출**: `_call_llm_with_retry()` 함수 생성
    - 캐시 확인/저장 로직 통합
    - 재시도 로직 (지수 백오프) 통합
    - 예외 처리 및 fallback 통합
  - [x] **모든 함수에서 `LLM_MODEL` 상수 사용**: 하드코딩된 모델명 제거
  - [x] **`extract_issue_with_llm()` 함수 개선**:
    - 반환값에 `title` 필드 추가 (필수)
    - 프롬프트에 title 생성 규칙 추가
    - 반환 구조: `{"title": str, "symptom": str, "root_cause": dict, "fix": dict, "validation": str}`
  - [x] **개별 추출 함수 제거**:
    - `extract_symptom_with_llm()` 제거
    - `extract_root_cause_with_llm()` 제거
    - `extract_fix_with_llm()` 제거
    - `extract_validation_with_llm()` 제거
  - 참고: 모든 LLM 호출 함수에서 `_call_llm_with_retry()` 사용 (향후 리팩토링 가능)

**Phase 4.7.5: IssueCard 모델 확장**
- [ ] `backend/core/models.py` 수정
  - `IssueCard` 모델에 필드 추가:
    - `section_id: Optional[str]` - 연결된 Timeline Section ID
    - `section_title: Optional[str]` - 연결된 Timeline Section 제목
    - `related_events: List[str]` - 관련 Event ID 리스트
    - `related_turns: List[int]` - 관련 Turn 인덱스 리스트
    - `confidence_score: Optional[float]` - 추출 신뢰도 점수

**Phase 4.7.6: 테스트 코드 수정**
- [ ] `tests/test_timeline_issues_e2e.py` 수정
  - Fixture 사용으로 변경 (parsed_data, normalized_events, timeline_sections)
  - 실행 순서 변경: Timeline Section 생성 → Issue Card 생성
  - 새로운 Issue Card 생성 로직 검증

**Phase 4.7.7: 캐시 무효화 전략 구현** - ✅ 완료 (이전 Phase에서 완료됨)
- [x] `backend/core/pipeline_cache.py`에 무효화 로직 추가
  - [x] 입력 파일 변경 감지 (파일 해시 비교) - 각 함수에서 자동 구현됨
  - [x] 자동 무효화 (캐시 키 기반) - 파일 해시 불일치 시 자동 무효화
  - [x] 수동 무효화 옵션 (테스트용) - `invalidate_cache()` 함수 구현됨

**검증 계획**:
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 캐시 동작 확인 (파일 저장/로드)
  - [x] 실행 순서 확인 (Timeline → Issue)
  - [x] 성능 개선 확인 (중복 실행 제거)
  - [x] 하위 호환성 확인 (기존 테스트 통과)
- [x] Issue Card 품질 평가 (2025-12-27 완료)
  - [x] 새로운 로직으로 생성된 Issue Card 품질 분석
    - **핵심 개선 사항 확인**:
      - Fix 항목: 20개 → 1개 (클러스터당, 95% 감소) ✅
      - Title: LLM 생성으로 품질 향상 ✅
      - Symptom: 구체적이고 명확함 ✅
      - Root Cause: 중간 과정 텍스트 제거, 핵심만 포함 ✅
      - Fix: 통합 컨텍스트 기반으로 구체적이고 명확함 ✅
      - Validation: 구체적인 검증 방법 제시 ✅
  - [x] Timeline Section 연결 정확성 검증 (100% 연결률) ✅
  - [x] LLM 적용 여부 확인 (2회 호출, 클러스터당 1회) ✅

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

**⚠️ 중요**: Phase 5는 패턴 기반 처리입니다 (LLM 미사용)
- 스니펫 ID 생성: 규칙 기반 (SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang})
- 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
- 중복 제거: 해시 기반 (SHA-256)
- 링킹: Turn/Event 인덱스 매칭

**입력-처리-출력**:
```
입력: Turns (code_blocks), Events, IssueCards, SessionMeta
처리: CodeBlock → Snippet 변환 → 중복 제거 → 링킹 → snippets.json 생성
출력: snippets.json, 업데이트된 Events/IssueCards (snippet_refs 포함)
```

**구현 계획**:

**Phase 5.1: Snippet 모델 정의** - ✅ 완료
- [x] `backend/core/models.py`에 Snippet 모델 추가
  - [x] snippet_id, lang, code, source, links, snippet_hash, aliases 필드

**Phase 5.2: 스니펫 관리 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_manager.py` 생성
  - [x] 스니펫 ID 생성 함수 (generate_snippet_id)
  - [x] 코드 정규화 및 해시 생성 함수 (normalize_code, generate_snippet_hash)
  - [x] 언어 판별 함수 (detect_language, fence_lang 우선 → 휴리스틱)
  - [x] CodeBlock → Snippet 변환 함수 (code_blocks_to_snippets)
  - [x] 중복 제거 로직 (deduplicate_snippets, 해시 기반)
  - [x] 링킹 로직 (link_snippets_to_events, link_snippets_to_issues)
  - [x] 통합 처리 함수 (process_snippets)

**Phase 5.3: 스니펫 저장 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_storage.py` 생성
  - [x] snippets.json 생성 함수 (generate_snippets_json)

**Phase 5.4: 파이프라인 캐싱 통합 (선택적)**
- [ ] `backend/core/pipeline_cache.py`에 스니펫 캐싱 추가 (선택적)
  - [ ] get_or_create_snippets() 함수 추가

**Phase 5.5: 테스트 작성** - ✅ 완료
- [x] `tests/test_snippet_manager.py` 작성 (단위 테스트)
  - [x] test_generate_snippet_id()
  - [x] test_normalize_code()
  - [x] test_generate_snippet_hash()
  - [x] test_detect_language()
  - [x] test_code_blocks_to_snippets()
  - [x] test_deduplicate_snippets()
  - [x] test_link_snippets_to_events()
  - [x] test_link_snippets_to_issues()
- [x] `tests/test_snippet_e2e.py` 작성 (E2E 테스트)
  - [x] test_snippet_e2e_with_llm() - 전체 파이프라인 통합 테스트
    - 실제 입력 파일 사용 (docs/cursor_phase_6_3.md)
    - 파싱 → 이벤트 정규화 → Timeline → Issue Cards → 스니펫 처리
    - snippets.json 생성 및 검증
    - Event/IssueCard 링킹 검증

**검증 계획**:
- [x] 단위 테스트 실행 및 통과 확인 (9개 테스트 모두 통과)
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 스니펫 ID 형식 검증 (PASS)
  - [x] 중복 제거 검증 (해시 기반, 92개 코드 블록 → 81개 스니펫, 11개 중복 제거)
  - [x] Event 링킹 검증 (19개 이벤트에 스니펫 링크, PASS)
  - [x] Issue Card 링킹 검증 (1개 Issue Card에 스니펫 링크, PASS)
  - [x] snippets.json 구조 검증 (PASS)
- [x] E2E 테스트 결과 분석 및 리포트 생성 (2025-12-27 완료)

---

## Phase 6-8: 미완료 (간략 요약)

### Phase 6: 백엔드 API 구현
- [ ] FastAPI 엔드포인트 구현 (파싱, Timeline, Issues, Snippets, Export)
- [ ] Markdown 렌더러 구현
- [ ] 테스트 및 E2E 테스트 (실제 서버 실행)

### Phase 7: 프론트엔드 UI 구현
- [ ] Next.js 기반 웹 UI (메인 페이지, 입력 패널, 결과 미리보기, Export 패널)
- [ ] API 클라이언트 및 타입 정의
- [ ] 스타일링 (Tailwind CSS)

### Phase 8: 통합 테스트 및 QA
- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 4.7 완료, Phase 5 진행 예정 (코드 스니펫 분리 및 저장)

**마지막 업데이트**: 2025-12-27

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3.0-3.3: 이벤트 정규화 기본 구현 및 평가 방법 구축 (2025-12-20~23)
- Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선 (2025-12-23~26)
  - 타입 체계 개선 완료 (CODE_GENERATION 추가, ARTIFACT 제거)
- Phase 4: Timeline 및 Issue Cards 생성 기본 구현 (2025-12-26)
  - LLM 기반 E2E 테스트 완료
- Phase 4.5: Timeline 구조화 개선 및 품질 평가 (2025-12-26)
  - Timeline 품질 평가 완료 (품질 점수: 45/100)
- Phase 4.6: Issue Card 품질 개선 (2025-12-26)
  - LLM 기반 추출 함수 구현 완료
  - E2E 테스트 완료 (품질 점수: 94/100, 하지만 실제 품질 문제 발견)
- Phase 4.7.3-4.7.4: Issue Card 생성 로직 개선 및 LLM 서비스 리팩토링 (2025-12-27 완료)
  - `extract_issue_with_llm()` 통합 함수 사용으로 전환
  - 모든 필드에 일관된 fallback 적용
  - LLM 모델 통일 (`gpt-4.1-mini`)
  - 개별 추출 함수 제거 (539줄 삭제)
  - E2E 테스트 완료: Fix 항목 20개 → 1개 (95% 감소), 품질 대폭 향상

**진행 중인 Phase**:
- Phase 5: 코드 스니펫 분리 및 저장 (진행 중)
  - Phase 5.1: Snippet 모델 정의
  - Phase 5.2: 스니펫 관리 모듈 구현
  - Phase 5.3: 스니펫 저장 모듈 구현
  - Phase 5.4: 파이프라인 캐싱 통합 (선택적)
  - Phase 5.5: 테스트 작성

**다음 단계**:
- Phase 5 완료 후 Phase 6 진행 예정 (백엔드 API 구현)

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.

```

```markdown
**진행 중인 Phase**:
- Phase 5: 코드 스니펫 분리 및 저장 - ✅ 완료 (2025-12-27)
  - [x] Phase 5.1: Snippet 모델 정의
  - [x] Phase 5.2: 스니펫 관리 모듈 구현
  - [x] Phase 5.3: 스니펫 저장 모듈 구현
  - [x] Phase 5.5: 테스트 작성 및 검증
  - [ ] Phase 5.4: 파이프라인 캐싱 통합 (선택적, 추후 개선 가능)
```

```markdown
# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (필수)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

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

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**

프로젝트는 Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행합니다.
하지만 Phase 4나 Phase 5에서 문제가 발견되면 **Phase 3으로 돌아가서 이벤트 정규화 로직을 개선**한 후, 다시 Phase 4, 5로 넘어가는 iterative cycle을 돌고 있습니다.

**주의사항**:
- Phase 3, 4, 5의 **기본 순서는 항상 유지**: 3 → 4 → 5
- 개선 작업은 **Phase 3의 서브 Phase (3.1, 3.2, 3.4 등)**로 진행
- Phase 번호는 **절대 섞이지 않음** (3 → 4 → 3.4 → 5 ❌, 3 → 4 → 3.4 → 4 재검증 → 5 ✅)

### Phase 3.0: 기본 구현 (완료)

- ✅ 데이터 모델 정의 (EventType, Event, TimelineEvent, IssueCard)
- ✅ 이벤트 정규화 기본 구현 (규칙 기반 타입 분류)
- ✅ 단위 테스트 및 E2E 테스트 완료
- **발견된 문제점**: 이벤트 중복 생성, Summary 품질, 타입 분류 정확도

### Phase 3.1: 즉시 개선 (정규식 기반) - 완료

- ✅ 이벤트 중복 생성 방지 (117개 → 67개, 1:1 매핑 달성)
- ✅ Summary 품질 개선 (줄바꿈 정리, 의미 있는 위치에서 자르기)
- ✅ 타입 분류 엄격화 (구체적인 패턴 사용)

### Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료

- ✅ LLM 서비스 구현 (gpt-4.1-mini, 파일 기반 캐싱, `.env` 자동 로드)
- ✅ 이벤트 정규화 모듈에 LLM 옵션 추가 (`use_llm` 파라미터)
- ✅ LLM 기반 E2E 테스트 완료 (67개 Turn → 67개 Event, 1:1 매핑 달성)
- ✅ E2E 테스트 결과 분석 완료

**Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선** - 완료
- ✅ 병렬 처리 구현 (224초 → 44.99초, 약 5배 향상)
- ✅ 캐시 시스템 개선 (SHA-256 해시, 원자적 저장, 텍스트 해시 검증)
- ✅ 캐시 성능 검증: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상)

### Phase 3.3: 결과 평가 방법 구축 - 완료

- ✅ 정성적 평가 도구 구현 (`backend/builders/evaluation.py`)
- ✅ Golden 파일 관리 도구 구현
- ✅ 수동 검증 프로세스 실행 완료
- ⏸️ Golden 파일 생성: 보류 (Phase 3.4 완료 후 작성 예정)

### Phase 3.4: 이벤트 정규화 품질 개선 (Iterative Improvement Cycle)

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

**⚠️ 컨텍스트**: Phase 4 완료 후 문제 발견 → Phase 3으로 돌아온 개선 작업

**발견된 문제점**:
- Timeline: 이벤트 타입 분류 부정확, Summary 품질 낮음
- Issue Cards: Summary 품질 문제, Root cause/Fix/Validation 추출 품질 낮음

**완료된 작업**:
- [x] 수동 검증 파일 재작성 및 검증 (HTML 형식, 67개 이벤트)
- [x] 정량적/정성적 분석 완료 (타입 분류 정확도 62.69%, 문제 패턴 분류)
- [x] 문제 원인 분석 및 개선 방안 도출
- [x] 개선 작업 실행 (Type 추출 로직, Summary 로직, LLM 프롬프트 개선)
- [x] **타입 체계 개선 구현 완료** (2025-12-26)
  - [x] EventType.ARTIFACT 제거, EventType.CODE_GENERATION 추가
  - [x] ArtifactAction Enum 추가
  - [x] 분류 로직 개선 (is_code_generation_turn, create_code_generation_event)
  - [x] LLM 프롬프트 수정
  - [x] 평가 도구 업데이트
  - [x] E2E 테스트 재실행 및 검증 완료

**상세 개선 계획**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 참조

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**⚠️ 참고**: E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)**로 돌아가서 개선 작업을 수행한 후 다시 Phase 4 E2E 테스트를 재실행합니다

### 기본 구현 - 완료

- ✅ Timeline 빌더 구현 (`build_timeline()`)
- ✅ Issue Cards 빌더 구현 (`build_issue_cards()`)
  - DebugEvent 기반 이슈 탐지, 슬라이딩 윈도우 그룹화
  - Symptom/Root cause/Fix/Validation 추출 (패턴 기반)
- ✅ 단위 테스트 및 E2E 테스트 완료 (구조적 정합성 검증 완료)

**⚠️ E2E 테스트 상태**:
- 구조적 정합성 검증 완료 (테스트 통과)
- 실제 내용 품질 검증은 미완료 (Phase 4.5, 4.6에서 개선 예정)

### Phase 4.5: Timeline 구조화 개선 (진행 중)

**목표**: Timeline을 단순 나열에서 구조화된 작업 항목별 그룹으로 개선

**발견된 문제점**:
- Timeline이 단순히 Event를 seq 1, 2, 3... 순서로 나열
- 주요 작업 내용이 항목화되지 않음
- 작업 내용 중 이슈 발생 여부 표시 안 됨
- 작업 결과 연결 정보 부족

**개선 목표**:
1. Phase/Subphase별로 주요 작업 항목 추출 및 항목화 (1, 2, 3, 4...)
2. 각 항목의 작업 내용 명확화 (LLM 기반 또는 패턴 기반)
3. 작업 내용 중 이슈 발생 여부 표시 (Issue Card와 연결)
4. 작업 결과 연결 정보 추가 (코드 스니펫, 파일, Git commit 등)

**구현 계획**:
- [x] Timeline 구조화 모델 정의 (`TimelineSection` 모델 추가)
- [x] Timeline 구조화 빌더 구현 (`build_structured_timeline()`)
  - [x] Phase/Subphase별 그룹화 로직
  - [x] 주요 작업 항목 추출 로직 (패턴 기반, LLM 옵션 추가 예정)
  - [x] 이슈 연결 로직
  - [x] 작업 결과 연결 정보 추출 로직
- [x] LLM 기반 작업 항목 추출 (선택적) (2025-12-26 완료)
  - [x] LLM 프롬프트 설계 및 캐싱 로직 적용
  - [x] extract_main_tasks_with_llm() 함수 구현
  - [x] timeline_builder에 use_llm 파라미터 통합
- [x] 테스트 작성 및 E2E 테스트 업데이트 (2025-12-26 완료)
  - [x] 단위 테스트 작성 (test_structured_timeline_pattern_based, test_structured_timeline_llm_based)
  - [x] E2E 테스트 업데이트 (test_timeline_issues_e2e_with_llm에서 build_structured_timeline 사용)
  - [x] E2E 테스트 실행 완료 (7개 sections 생성, 패턴 기반 fallback 사용)

**Timeline 품질 평가 및 수동 검증** (2025-12-26 완료):
- [x] E2E 테스트 결과 분석 (결과 파일: `tests/timeline_issues_e2e_llm_20251226_130658.json`)
  - Timeline Section 개수 및 구조 분석 (7개 섹션, 67개 이벤트)
  - Section 제목/요약 품질 평가 (제목 품질 문제 발견: 모든 제목이 이벤트 타입만 나열)
  - 이슈 연결 정확성 검증 (100% 연결률)
  - 작업 결과 연결 정보 완성도 확인 (85.7% 섹션에 코드 스니펫/파일/Artifact 포함)
- [x] Timeline 품질 평가 리포트 생성 (`tests/reports/timeline_quality_evaluation.json`)
- [x] 수동 검증 및 개선점 도출 (`tests/reports/timeline_quality_analysis.md`)
  - **주요 발견사항**: 제목 품질 문제 (7개 섹션 모두), Artifact 중복 문제 (4개 섹션)
  - **품질 점수**: 45/100
  - **개선 권장사항**: 제목 생성 로직 개선, Artifact 중복 제거

**산출물**: 구조화된 Timeline 모델, Timeline 구조화 빌더, E2E 테스트 완료 및 검증 리포트, Timeline 품질 평가 리포트

### Phase 4.6: Issue Card 품질 개선 (완료)

**목표**: Issue Card의 symptom → root_cause → fix → validation 체인을 LLM 기반으로 개선하여 내용 품질 향상

**발견된 문제점** (개선 전):
- Symptom: 단순히 Turn body 처음 500자 잘라내기
- Root cause: 패턴 매칭으로 텍스트 잘라내기 (중간 과정 텍스트 포함)
- Fix: DebugEvent의 summary만 사용 (구체적이지 않음)
- Validation: 패턴 매칭으로 텍스트 잘라내기 (불완전한 텍스트)

**개선 결과** (2025-12-26):
- Symptom: 평균 길이 82.5자 → 23.5자 (약 3.5배 개선, 핵심만 추출)
- Fix: 2개 → 12개 (6배 증가, 구체적이고 상세한 해결 방법)
- Validation: 명확하고 구체적인 검증 방법 추출
- Root cause: 프롬프트 개선 완료 (중간 과정 텍스트 제거 지시 추가)
- 품질 점수: 94/100
- 디버그 부분을 각 이슈로 나누는 로직 점검 필요

**구현 계획**:
- [x] LLM 기반 추출 함수 구현 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`) (2025-12-26 완료)
  - 각 함수는 캐싱 로직 적용 (SHA-256 해시 기반)
  - Fallback 로직 유지 (LLM 실패 시 패턴 기반)
  - 재시도 로직 적용 (최대 3회, 지수 백오프)
- [x] Issue Builder에 LLM 기반 추출 통합 (`build_issue_cards()` 함수에 `use_llm` 파라미터 추가) (2025-12-26 완료)
- [x] E2E 테스트 업데이트 및 실행 완료 (2025-12-26 완료)
  - LLM 기반 Issue Card 생성 검증 완료
  - 품질 분석 완료 (품질 점수: 94/100)
- [x] Root cause 프롬프트 개선 (중간 과정 텍스트 제거) (2025-12-26 완료)
- [ ] 디버그 이슈 분리 로직 개선 (논리적 이슈 단위로 클러스터링) (선택적, 추후 개선)
- [ ] 단위 테스트 작성 (`tests/test_issues_builder.py`) (선택적, 추후 개선)

### Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토 (진행 중)

**목표**: 
1. 파이프라인 중간 결과를 Fixture와 파일 캐싱으로 관리하여 중복 실행 제거
2. Timeline Section을 Issue Card 생성에 활용
3. Issue Card 생성 로직 전면 재검토 및 개선

**발견된 문제점**:
- 각 테스트가 독립적으로 파싱/이벤트 정규화 재실행 (비효율)
- Timeline Section 생성이 Issue Card 생성 이후에 실행됨
- Timeline Section을 Issue Card에 활용할 수 없음
- Issue Card 품질 문제: LLM이 제대로 적용되지 않은 것으로 보임
  - Root cause에 중간 과정 텍스트 포함
  - Fix summary가 형식적이고 부자연스러움
  - Symptom이 핵심이 아닌 경우 발생
- 각 컴포넌트(symptom, root_cause, fix, validation)가 독립적으로 작동하여 컨텍스트 부족

**⚠️ Phase 4.7 완료 후 발견된 심각한 문제점 (2025-12-26)**:
- **Issue Card 결과가 완전히 엉망**: 사용자 평가 "100점 만점에 -100점"
- **핵심 문제**:
  1. **`extract_issue_with_llm()` 함수가 구현되어 있지만 사용되지 않음**
     - `build_issue_card_from_cluster()` 함수가 각 컴포넌트를 개별적으로 추출
     - 통합 컨텍스트를 활용하지 못함
  2. **Fix 항목이 20개나 생성됨** (각 이벤트마다 하나씩)
     - `extract_fix_with_llm()` 함수가 각 DEBUG 이벤트마다 개별 호출됨
     - 각 fix가 매우 길고 반복적인 템플릿 문구 포함 ("이벤트 요약에 기반하여 구체적인 해결 방법을 추출하고 설명하겠습니다.")
  3. **Symptom이 너무 짧고 구체적이지 않음**
     - "다음 단계" 같은 의미 없는 텍스트만 추출됨
  4. **Title이 잘림**
     - 제목 생성 로직에 문제가 있거나 길이 제한이 너무 짧음
  5. **LLM은 사용되었지만 프롬프트/로직 문제**
     - 캐시 파일 확인 결과 LLM 호출은 정상적으로 이루어짐
     - 하지만 프롬프트가 각 컴포넌트를 개별적으로 요청하여 컨텍스트 부족
     - `extract_issue_with_llm()` 함수가 구현되어 있지만 실제로 호출되지 않음
- **확인된 사항**:
  - LLM 캐시 파일 존재: `cache/issue_*.json` (92개 파일)
  - LLM 호출은 정상적으로 이루어짐 (캐시 히트율 32.84%)
  - 문제는 로직 구조: 통합 컨텍스트를 활용하지 않고 각 컴포넌트를 개별 추출
- **필요한 개선**:
  1. `build_issue_card_from_cluster()` 함수를 `extract_issue_with_llm()` 사용하도록 수정
  2. 각 이벤트마다 개별 fix 추출 대신, 클러스터 전체에 대한 통합 fix 추출
  3. Symptom 추출 프롬프트 개선 (핵심만 추출하도록)
  4. Title 생성 로직 개선 (길이 제한 확대 또는 더 나은 요약)
  5. 통합 컨텍스트(TimelineSection + Events + Turns)를 활용한 일관성 있는 추출

**개선 방향**:
1. **파이프라인 데이터 관리**: 하이브리드 방식 (Fixture + 파일 캐싱)
   - pytest Fixture로 메모리 기반 공유 (빠른 접근)
   - 파일 기반 캐싱으로 영구 저장 (디버깅, 수동 검증)
2. **Issue Card 생성 로직 전면 재검토**:
   - 입력: TimelineSection + 관련 Events + 관련 Turns (통합 컨텍스트)
   - LLM 프롬프트: 구조화된 출력 (현상-원인-개선내용)
   - 출력: 구조화된 IssueCard (Timeline Section과 연결)
3. **이슈 클러스터링**: DEBUG 타입 이벤트 주변 Turn들을 논리적 이슈 단위로 클러스터링

**구현 계획**:

**Phase 4.7.1: 중간 결과 캐싱 모듈 생성**
- [ ] `backend/core/pipeline_cache.py` 생성
  - 파싱 결과 캐싱 (파일 기반)
  - 이벤트 정규화 결과 캐싱 (파일 기반)
  - Timeline Section 결과 캐싱 (파일 기반)
  - 캐시 키 생성 (입력 파일 해시 + use_llm 플래그)
  - 캐시 무효화 전략 (입력 파일 변경 감지)

**Phase 4.7.2: pytest Fixture 추가**
- [ ] `tests/conftest.py`에 Fixture 추가
  - `parsed_data` fixture (세션 스코프)
  - `normalized_events` fixture (세션 스코프, use_llm 파라미터)
  - `timeline_sections` fixture (세션 스코프, use_llm 파라미터)
  - 각 Fixture는 pipeline_cache 모듈 사용

**Phase 4.7.3: Issue Card 생성 로직 개선** - ✅ 완료 (2025-12-27)
- [x] `backend/builders/issues_builder.py` 수정
  - [x] `build_issue_cards()` 함수 시그니처 변경: `timeline_sections` 파라미터 추가
  - [x] DEBUG 이벤트 클러스터링 로직 구현 (논리적 이슈 단위로 그룹화)
  - [x] Timeline Section과 Issue Card 매칭 로직 구현
  - [x] **`build_issue_card_from_cluster()` 함수 수정**:
    - [x] 개별 추출 함수 호출 제거 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`)
    - [x] `extract_issue_with_llm()` 한 번 호출로 통합 (통합 컨텍스트 기반)
    - [x] 모든 필드에 fallback 적용 (일관성):
      - `title`: `generate_issue_title_from_cluster()` 사용
      - `symptom`: 첫 번째 User Turn 사용
      - `root_cause`: 패턴 기반 추출
      - `fix`: 패턴 기반 추출
      - `validation`: 패턴 기반 추출
  - [x] **`build_issue_card_from_window()` 함수 수정**:
    - [x] window를 클러스터로 변환하여 `extract_issue_with_llm()` 사용
    - [x] 개별 추출 함수 호출 제거
    - [x] 모든 필드에 fallback 적용 (동일한 전략)

**Phase 4.7.4: LLM 서비스 리팩토링 및 통합** - ✅ 완료 (2025-12-27)
- [x] `backend/core/constants.py` 수정
  - [x] `LLM_MODEL = "gpt-4.1-mini"` 상수 추가 (커서룰에 맞춰 통일)
- [x] `backend/core/llm_service.py` 수정
  - [x] **공통 LLM 호출 함수 추출**: `_call_llm_with_retry()` 함수 생성
    - 캐시 확인/저장 로직 통합
    - 재시도 로직 (지수 백오프) 통합
    - 예외 처리 및 fallback 통합
  - [x] **모든 함수에서 `LLM_MODEL` 상수 사용**: 하드코딩된 모델명 제거
  - [x] **`extract_issue_with_llm()` 함수 개선**:
    - 반환값에 `title` 필드 추가 (필수)
    - 프롬프트에 title 생성 규칙 추가
    - 반환 구조: `{"title": str, "symptom": str, "root_cause": dict, "fix": dict, "validation": str}`
  - [x] **개별 추출 함수 제거**:
    - `extract_symptom_with_llm()` 제거
    - `extract_root_cause_with_llm()` 제거
    - `extract_fix_with_llm()` 제거
    - `extract_validation_with_llm()` 제거
  - 참고: 모든 LLM 호출 함수에서 `_call_llm_with_retry()` 사용 (향후 리팩토링 가능)

**Phase 4.7.5: IssueCard 모델 확장**
- [ ] `backend/core/models.py` 수정
  - `IssueCard` 모델에 필드 추가:
    - `section_id: Optional[str]` - 연결된 Timeline Section ID
    - `section_title: Optional[str]` - 연결된 Timeline Section 제목
    - `related_events: List[str]` - 관련 Event ID 리스트
    - `related_turns: List[int]` - 관련 Turn 인덱스 리스트
    - `confidence_score: Optional[float]` - 추출 신뢰도 점수

**Phase 4.7.6: 테스트 코드 수정**
- [ ] `tests/test_timeline_issues_e2e.py` 수정
  - Fixture 사용으로 변경 (parsed_data, normalized_events, timeline_sections)
  - 실행 순서 변경: Timeline Section 생성 → Issue Card 생성
  - 새로운 Issue Card 생성 로직 검증

**Phase 4.7.7: 캐시 무효화 전략 구현** - ✅ 완료 (이전 Phase에서 완료됨)
- [x] `backend/core/pipeline_cache.py`에 무효화 로직 추가
  - [x] 입력 파일 변경 감지 (파일 해시 비교) - 각 함수에서 자동 구현됨
  - [x] 자동 무효화 (캐시 키 기반) - 파일 해시 불일치 시 자동 무효화
  - [x] 수동 무효화 옵션 (테스트용) - `invalidate_cache()` 함수 구현됨

**검증 계획**:
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 캐시 동작 확인 (파일 저장/로드)
  - [x] 실행 순서 확인 (Timeline → Issue)
  - [x] 성능 개선 확인 (중복 실행 제거)
  - [x] 하위 호환성 확인 (기존 테스트 통과)
- [x] Issue Card 품질 평가 (2025-12-27 완료)
  - [x] 새로운 로직으로 생성된 Issue Card 품질 분석
    - **핵심 개선 사항 확인**:
      - Fix 항목: 20개 → 1개 (클러스터당, 95% 감소) ✅
      - Title: LLM 생성으로 품질 향상 ✅
      - Symptom: 구체적이고 명확함 ✅
      - Root Cause: 중간 과정 텍스트 제거, 핵심만 포함 ✅
      - Fix: 통합 컨텍스트 기반으로 구체적이고 명확함 ✅
      - Validation: 구체적인 검증 방법 제시 ✅
  - [x] Timeline Section 연결 정확성 검증 (100% 연결률) ✅
  - [x] LLM 적용 여부 확인 (2회 호출, 클러스터당 1회) ✅

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

**⚠️ 중요**: Phase 5는 패턴 기반 처리입니다 (LLM 미사용)
- 스니펫 ID 생성: 규칙 기반 (SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang})
- 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
- 중복 제거: 해시 기반 (SHA-256)
- 링킹: Turn/Event 인덱스 매칭

**입력-처리-출력**:
```
입력: Turns (code_blocks), Events, IssueCards, SessionMeta
처리: CodeBlock → Snippet 변환 → 중복 제거 → 링킹 → snippets.json 생성
출력: snippets.json, 업데이트된 Events/IssueCards (snippet_refs 포함)
```

**구현 계획**:

**Phase 5.1: Snippet 모델 정의** - ✅ 완료
- [x] `backend/core/models.py`에 Snippet 모델 추가
  - [x] snippet_id, lang, code, source, links, snippet_hash, aliases 필드

**Phase 5.2: 스니펫 관리 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_manager.py` 생성
  - [x] 스니펫 ID 생성 함수 (generate_snippet_id)
  - [x] 코드 정규화 및 해시 생성 함수 (normalize_code, generate_snippet_hash)
  - [x] 언어 판별 함수 (detect_language, fence_lang 우선 → 휴리스틱)
  - [x] CodeBlock → Snippet 변환 함수 (code_blocks_to_snippets)
  - [x] 중복 제거 로직 (deduplicate_snippets, 해시 기반)
  - [x] 링킹 로직 (link_snippets_to_events, link_snippets_to_issues)
  - [x] 통합 처리 함수 (process_snippets)

**Phase 5.3: 스니펫 저장 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_storage.py` 생성
  - [x] snippets.json 생성 함수 (generate_snippets_json)

**Phase 5.4: 파이프라인 캐싱 통합 (선택적)**
- [ ] `backend/core/pipeline_cache.py`에 스니펫 캐싱 추가 (선택적)
  - [ ] get_or_create_snippets() 함수 추가

**Phase 5.5: 테스트 작성** - ✅ 완료
- [x] `tests/test_snippet_manager.py` 작성 (단위 테스트)
  - [x] test_generate_snippet_id()
  - [x] test_normalize_code()
  - [x] test_generate_snippet_hash()
  - [x] test_detect_language()
  - [x] test_code_blocks_to_snippets()
  - [x] test_deduplicate_snippets()
  - [x] test_link_snippets_to_events()
  - [x] test_link_snippets_to_issues()
- [x] `tests/test_snippet_e2e.py` 작성 (E2E 테스트)
  - [x] test_snippet_e2e_with_llm() - 전체 파이프라인 통합 테스트
    - 실제 입력 파일 사용 (docs/cursor_phase_6_3.md)
    - 파싱 → 이벤트 정규화 → Timeline → Issue Cards → 스니펫 처리
    - snippets.json 생성 및 검증
    - Event/IssueCard 링킹 검증

**검증 계획**:
- [x] 단위 테스트 실행 및 통과 확인 (9개 테스트 모두 통과)
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 스니펫 ID 형식 검증 (PASS)
  - [x] 중복 제거 검증 (해시 기반, 92개 코드 블록 → 81개 스니펫, 11개 중복 제거)
  - [x] Event 링킹 검증 (19개 이벤트에 스니펫 링크, PASS)
  - [x] Issue Card 링킹 검증 (1개 Issue Card에 스니펫 링크, PASS)
  - [x] snippets.json 구조 검증 (PASS)
- [x] E2E 테스트 결과 분석 및 리포트 생성 (2025-12-27 완료)

---

## Phase 6-8: 미완료 (간략 요약)

### Phase 6: 백엔드 API 구현
- [ ] FastAPI 엔드포인트 구현 (파싱, Timeline, Issues, Snippets, Export)
- [ ] Markdown 렌더러 구현
- [ ] 테스트 및 E2E 테스트 (실제 서버 실행)

### Phase 7: 프론트엔드 UI 구현
- [ ] Next.js 기반 웹 UI (메인 페이지, 입력 패널, 결과 미리보기, Export 패널)
- [ ] API 클라이언트 및 타입 정의
- [ ] 스타일링 (Tailwind CSS)

### Phase 8: 통합 테스트 및 QA
- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 4.7 완료, Phase 5 진행 예정 (코드 스니펫 분리 및 저장)

**마지막 업데이트**: 2025-12-27

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3.0-3.3: 이벤트 정규화 기본 구현 및 평가 방법 구축 (2025-12-20~23)
- Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선 (2025-12-23~26)
  - 타입 체계 개선 완료 (CODE_GENERATION 추가, ARTIFACT 제거)
- Phase 4: Timeline 및 Issue Cards 생성 기본 구현 (2025-12-26)
  - LLM 기반 E2E 테스트 완료
- Phase 4.5: Timeline 구조화 개선 및 품질 평가 (2025-12-26)
  - Timeline 품질 평가 완료 (품질 점수: 45/100)
- Phase 4.6: Issue Card 품질 개선 (2025-12-26)
  - LLM 기반 추출 함수 구현 완료
  - E2E 테스트 완료 (품질 점수: 94/100, 하지만 실제 품질 문제 발견)
- Phase 4.7.3-4.7.4: Issue Card 생성 로직 개선 및 LLM 서비스 리팩토링 (2025-12-27 완료)
  - `extract_issue_with_llm()` 통합 함수 사용으로 전환
  - 모든 필드에 일관된 fallback 적용
  - LLM 모델 통일 (`gpt-4.1-mini`)
  - 개별 추출 함수 제거 (539줄 삭제)
  - E2E 테스트 완료: Fix 항목 20개 → 1개 (95% 감소), 품질 대폭 향상
- Phase 5: 코드 스니펫 분리 및 저장 (2025-12-27 완료)
  - Snippet 모델 정의 완료
  - 스니펫 관리 모듈 구현 완료 (ID 생성, 해시, 언어 판별, 변환, 중복 제거, 링킹)
  - 스니펫 저장 모듈 구현 완료 (snippets.json 생성)
  - 단위 테스트 완료 (9개 테스트 모두 통과)
  - E2E 테스트 완료: 92개 코드 블록 → 81개 스니펫 (11개 중복 제거), 19개 이벤트 링킹, 1개 Issue Card 링킹

**진행 중인 Phase**:
- Phase 5: 코드 스니펫 분리 및 저장 (진행 중)
  - Phase 5.1: Snippet 모델 정의
  - Phase 5.2: 스니펫 관리 모듈 구현
  - Phase 5.3: 스니펫 저장 모듈 구현
  - Phase 5.4: 파이프라인 캐싱 통합 (선택적)
  - Phase 5.5: 테스트 작성

**다음 단계**:
- Phase 5 완료 후 Phase 6 진행 예정 (백엔드 API 구현)

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.

```

```markdown
# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (필수)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

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

## Phase 3: 이벤트 추출 및 정규화

**목표**: 파싱된 Turn 데이터를 이벤트로 정규화

**⚠️ 중요: Iterative Improvement Cycle (반복 개선 사이클)**

프로젝트는 Phase 3 → Phase 4 → Phase 5 순서로 기본적으로 순차 진행합니다.
하지만 Phase 4나 Phase 5에서 문제가 발견되면 **Phase 3으로 돌아가서 이벤트 정규화 로직을 개선**한 후, 다시 Phase 4, 5로 넘어가는 iterative cycle을 돌고 있습니다.

**주의사항**:
- Phase 3, 4, 5의 **기본 순서는 항상 유지**: 3 → 4 → 5
- 개선 작업은 **Phase 3의 서브 Phase (3.1, 3.2, 3.4 등)**로 진행
- Phase 번호는 **절대 섞이지 않음** (3 → 4 → 3.4 → 5 ❌, 3 → 4 → 3.4 → 4 재검증 → 5 ✅)

### Phase 3.0: 기본 구현 (완료)

- ✅ 데이터 모델 정의 (EventType, Event, TimelineEvent, IssueCard)
- ✅ 이벤트 정규화 기본 구현 (규칙 기반 타입 분류)
- ✅ 단위 테스트 및 E2E 테스트 완료
- **발견된 문제점**: 이벤트 중복 생성, Summary 품질, 타입 분류 정확도

### Phase 3.1: 즉시 개선 (정규식 기반) - 완료

- ✅ 이벤트 중복 생성 방지 (117개 → 67개, 1:1 매핑 달성)
- ✅ Summary 품질 개선 (줄바꿈 정리, 의미 있는 위치에서 자르기)
- ✅ 타입 분류 엄격화 (구체적인 패턴 사용)

### Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini) - 완료

- ✅ LLM 서비스 구현 (gpt-4.1-mini, 파일 기반 캐싱, `.env` 자동 로드)
- ✅ 이벤트 정규화 모듈에 LLM 옵션 추가 (`use_llm` 파라미터)
- ✅ LLM 기반 E2E 테스트 완료 (67개 Turn → 67개 Event, 1:1 매핑 달성)
- ✅ E2E 테스트 결과 분석 완료

**Phase 3.2.1: LLM 병렬 처리 리팩토링 및 캐시 시스템 개선** - 완료
- ✅ 병렬 처리 구현 (224초 → 44.99초, 약 5배 향상)
- ✅ 캐시 시스템 개선 (SHA-256 해시, 원자적 저장, 텍스트 해시 검증)
- ✅ 캐시 성능 검증: 첫 실행 56.01초 → 두 번째 실행 0.26초 (약 215배 향상)

### Phase 3.3: 결과 평가 방법 구축 - 완료

- ✅ 정성적 평가 도구 구현 (`backend/builders/evaluation.py`)
- ✅ Golden 파일 관리 도구 구현
- ✅ 수동 검증 프로세스 실행 완료
- ⏸️ Golden 파일 생성: 보류 (Phase 3.4 완료 후 작성 예정)

### Phase 3.4: 이벤트 정규화 품질 개선 (Iterative Improvement Cycle)

**목표**: Phase 4 E2E 테스트 결과를 바탕으로 이벤트 정규화 품질 개선

**⚠️ 컨텍스트**: Phase 4 완료 후 문제 발견 → Phase 3으로 돌아온 개선 작업

**발견된 문제점**:
- Timeline: 이벤트 타입 분류 부정확, Summary 품질 낮음
- Issue Cards: Summary 품질 문제, Root cause/Fix/Validation 추출 품질 낮음

**완료된 작업**:
- [x] 수동 검증 파일 재작성 및 검증 (HTML 형식, 67개 이벤트)
- [x] 정량적/정성적 분석 완료 (타입 분류 정확도 62.69%, 문제 패턴 분류)
- [x] 문제 원인 분석 및 개선 방안 도출
- [x] 개선 작업 실행 (Type 추출 로직, Summary 로직, LLM 프롬프트 개선)
- [x] **타입 체계 개선 구현 완료** (2025-12-26)
  - [x] EventType.ARTIFACT 제거, EventType.CODE_GENERATION 추가
  - [x] ArtifactAction Enum 추가
  - [x] 분류 로직 개선 (is_code_generation_turn, create_code_generation_event)
  - [x] LLM 프롬프트 수정
  - [x] 평가 도구 업데이트
  - [x] E2E 테스트 재실행 및 검증 완료

**상세 개선 계획**: [docs/phase3_4_type_system_improvement.md](docs/phase3_4_type_system_improvement.md) 참조

---

## Phase 4: Timeline 및 Issue Cards 생성

**목표**: 정규화된 이벤트로부터 Timeline과 Issue Cards 생성

**⚠️ 참고**: E2E 테스트에서 품질 문제가 발견되면 **Phase 3.4 (이벤트 정규화 품질 개선)**로 돌아가서 개선 작업을 수행한 후 다시 Phase 4 E2E 테스트를 재실행합니다

### 기본 구현 - 완료

- ✅ Timeline 빌더 구현 (`build_timeline()`)
- ✅ Issue Cards 빌더 구현 (`build_issue_cards()`)
  - DebugEvent 기반 이슈 탐지, 슬라이딩 윈도우 그룹화
  - Symptom/Root cause/Fix/Validation 추출 (패턴 기반)
- ✅ 단위 테스트 및 E2E 테스트 완료 (구조적 정합성 검증 완료)

**⚠️ E2E 테스트 상태**:
- 구조적 정합성 검증 완료 (테스트 통과)
- 실제 내용 품질 검증은 미완료 (Phase 4.5, 4.6에서 개선 예정)

### Phase 4.5: Timeline 구조화 개선 (진행 중)

**목표**: Timeline을 단순 나열에서 구조화된 작업 항목별 그룹으로 개선

**발견된 문제점**:
- Timeline이 단순히 Event를 seq 1, 2, 3... 순서로 나열
- 주요 작업 내용이 항목화되지 않음
- 작업 내용 중 이슈 발생 여부 표시 안 됨
- 작업 결과 연결 정보 부족

**개선 목표**:
1. Phase/Subphase별로 주요 작업 항목 추출 및 항목화 (1, 2, 3, 4...)
2. 각 항목의 작업 내용 명확화 (LLM 기반 또는 패턴 기반)
3. 작업 내용 중 이슈 발생 여부 표시 (Issue Card와 연결)
4. 작업 결과 연결 정보 추가 (코드 스니펫, 파일, Git commit 등)

**구현 계획**:
- [x] Timeline 구조화 모델 정의 (`TimelineSection` 모델 추가)
- [x] Timeline 구조화 빌더 구현 (`build_structured_timeline()`)
  - [x] Phase/Subphase별 그룹화 로직
  - [x] 주요 작업 항목 추출 로직 (패턴 기반, LLM 옵션 추가 예정)
  - [x] 이슈 연결 로직
  - [x] 작업 결과 연결 정보 추출 로직
- [x] LLM 기반 작업 항목 추출 (선택적) (2025-12-26 완료)
  - [x] LLM 프롬프트 설계 및 캐싱 로직 적용
  - [x] extract_main_tasks_with_llm() 함수 구현
  - [x] timeline_builder에 use_llm 파라미터 통합
- [x] 테스트 작성 및 E2E 테스트 업데이트 (2025-12-26 완료)
  - [x] 단위 테스트 작성 (test_structured_timeline_pattern_based, test_structured_timeline_llm_based)
  - [x] E2E 테스트 업데이트 (test_timeline_issues_e2e_with_llm에서 build_structured_timeline 사용)
  - [x] E2E 테스트 실행 완료 (7개 sections 생성, 패턴 기반 fallback 사용)

**Timeline 품질 평가 및 수동 검증** (2025-12-26 완료):
- [x] E2E 테스트 결과 분석 (결과 파일: `tests/timeline_issues_e2e_llm_20251226_130658.json`)
  - Timeline Section 개수 및 구조 분석 (7개 섹션, 67개 이벤트)
  - Section 제목/요약 품질 평가 (제목 품질 문제 발견: 모든 제목이 이벤트 타입만 나열)
  - 이슈 연결 정확성 검증 (100% 연결률)
  - 작업 결과 연결 정보 완성도 확인 (85.7% 섹션에 코드 스니펫/파일/Artifact 포함)
- [x] Timeline 품질 평가 리포트 생성 (`tests/reports/timeline_quality_evaluation.json`)
- [x] 수동 검증 및 개선점 도출 (`tests/reports/timeline_quality_analysis.md`)
  - **주요 발견사항**: 제목 품질 문제 (7개 섹션 모두), Artifact 중복 문제 (4개 섹션)
  - **품질 점수**: 45/100
  - **개선 권장사항**: 제목 생성 로직 개선, Artifact 중복 제거

**산출물**: 구조화된 Timeline 모델, Timeline 구조화 빌더, E2E 테스트 완료 및 검증 리포트, Timeline 품질 평가 리포트

### Phase 4.6: Issue Card 품질 개선 (완료)

**목표**: Issue Card의 symptom → root_cause → fix → validation 체인을 LLM 기반으로 개선하여 내용 품질 향상

**발견된 문제점** (개선 전):
- Symptom: 단순히 Turn body 처음 500자 잘라내기
- Root cause: 패턴 매칭으로 텍스트 잘라내기 (중간 과정 텍스트 포함)
- Fix: DebugEvent의 summary만 사용 (구체적이지 않음)
- Validation: 패턴 매칭으로 텍스트 잘라내기 (불완전한 텍스트)

**개선 결과** (2025-12-26):
- Symptom: 평균 길이 82.5자 → 23.5자 (약 3.5배 개선, 핵심만 추출)
- Fix: 2개 → 12개 (6배 증가, 구체적이고 상세한 해결 방법)
- Validation: 명확하고 구체적인 검증 방법 추출
- Root cause: 프롬프트 개선 완료 (중간 과정 텍스트 제거 지시 추가)
- 품질 점수: 94/100
- 디버그 부분을 각 이슈로 나누는 로직 점검 필요

**구현 계획**:
- [x] LLM 기반 추출 함수 구현 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`) (2025-12-26 완료)
  - 각 함수는 캐싱 로직 적용 (SHA-256 해시 기반)
  - Fallback 로직 유지 (LLM 실패 시 패턴 기반)
  - 재시도 로직 적용 (최대 3회, 지수 백오프)
- [x] Issue Builder에 LLM 기반 추출 통합 (`build_issue_cards()` 함수에 `use_llm` 파라미터 추가) (2025-12-26 완료)
- [x] E2E 테스트 업데이트 및 실행 완료 (2025-12-26 완료)
  - LLM 기반 Issue Card 생성 검증 완료
  - 품질 분석 완료 (품질 점수: 94/100)
- [x] Root cause 프롬프트 개선 (중간 과정 텍스트 제거) (2025-12-26 완료)
- [ ] 디버그 이슈 분리 로직 개선 (논리적 이슈 단위로 클러스터링) (선택적, 추후 개선)
- [ ] 단위 테스트 작성 (`tests/test_issues_builder.py`) (선택적, 추후 개선)

### Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토 (진행 중)

**목표**: 
1. 파이프라인 중간 결과를 Fixture와 파일 캐싱으로 관리하여 중복 실행 제거
2. Timeline Section을 Issue Card 생성에 활용
3. Issue Card 생성 로직 전면 재검토 및 개선

**발견된 문제점**:
- 각 테스트가 독립적으로 파싱/이벤트 정규화 재실행 (비효율)
- Timeline Section 생성이 Issue Card 생성 이후에 실행됨
- Timeline Section을 Issue Card에 활용할 수 없음
- Issue Card 품질 문제: LLM이 제대로 적용되지 않은 것으로 보임
  - Root cause에 중간 과정 텍스트 포함
  - Fix summary가 형식적이고 부자연스러움
  - Symptom이 핵심이 아닌 경우 발생
- 각 컴포넌트(symptom, root_cause, fix, validation)가 독립적으로 작동하여 컨텍스트 부족

**⚠️ Phase 4.7 완료 후 발견된 심각한 문제점 (2025-12-26)**:
- **Issue Card 결과가 완전히 엉망**: 사용자 평가 "100점 만점에 -100점"
- **핵심 문제**:
  1. **`extract_issue_with_llm()` 함수가 구현되어 있지만 사용되지 않음**
     - `build_issue_card_from_cluster()` 함수가 각 컴포넌트를 개별적으로 추출
     - 통합 컨텍스트를 활용하지 못함
  2. **Fix 항목이 20개나 생성됨** (각 이벤트마다 하나씩)
     - `extract_fix_with_llm()` 함수가 각 DEBUG 이벤트마다 개별 호출됨
     - 각 fix가 매우 길고 반복적인 템플릿 문구 포함 ("이벤트 요약에 기반하여 구체적인 해결 방법을 추출하고 설명하겠습니다.")
  3. **Symptom이 너무 짧고 구체적이지 않음**
     - "다음 단계" 같은 의미 없는 텍스트만 추출됨
  4. **Title이 잘림**
     - 제목 생성 로직에 문제가 있거나 길이 제한이 너무 짧음
  5. **LLM은 사용되었지만 프롬프트/로직 문제**
     - 캐시 파일 확인 결과 LLM 호출은 정상적으로 이루어짐
     - 하지만 프롬프트가 각 컴포넌트를 개별적으로 요청하여 컨텍스트 부족
     - `extract_issue_with_llm()` 함수가 구현되어 있지만 실제로 호출되지 않음
- **확인된 사항**:
  - LLM 캐시 파일 존재: `cache/issue_*.json` (92개 파일)
  - LLM 호출은 정상적으로 이루어짐 (캐시 히트율 32.84%)
  - 문제는 로직 구조: 통합 컨텍스트를 활용하지 않고 각 컴포넌트를 개별 추출
- **필요한 개선**:
  1. `build_issue_card_from_cluster()` 함수를 `extract_issue_with_llm()` 사용하도록 수정
  2. 각 이벤트마다 개별 fix 추출 대신, 클러스터 전체에 대한 통합 fix 추출
  3. Symptom 추출 프롬프트 개선 (핵심만 추출하도록)
  4. Title 생성 로직 개선 (길이 제한 확대 또는 더 나은 요약)
  5. 통합 컨텍스트(TimelineSection + Events + Turns)를 활용한 일관성 있는 추출

**개선 방향**:
1. **파이프라인 데이터 관리**: 하이브리드 방식 (Fixture + 파일 캐싱)
   - pytest Fixture로 메모리 기반 공유 (빠른 접근)
   - 파일 기반 캐싱으로 영구 저장 (디버깅, 수동 검증)
2. **Issue Card 생성 로직 전면 재검토**:
   - 입력: TimelineSection + 관련 Events + 관련 Turns (통합 컨텍스트)
   - LLM 프롬프트: 구조화된 출력 (현상-원인-개선내용)
   - 출력: 구조화된 IssueCard (Timeline Section과 연결)
3. **이슈 클러스터링**: DEBUG 타입 이벤트 주변 Turn들을 논리적 이슈 단위로 클러스터링

**구현 계획**:

**Phase 4.7.1: 중간 결과 캐싱 모듈 생성**
- [ ] `backend/core/pipeline_cache.py` 생성
  - 파싱 결과 캐싱 (파일 기반)
  - 이벤트 정규화 결과 캐싱 (파일 기반)
  - Timeline Section 결과 캐싱 (파일 기반)
  - 캐시 키 생성 (입력 파일 해시 + use_llm 플래그)
  - 캐시 무효화 전략 (입력 파일 변경 감지)

**Phase 4.7.2: pytest Fixture 추가**
- [ ] `tests/conftest.py`에 Fixture 추가
  - `parsed_data` fixture (세션 스코프)
  - `normalized_events` fixture (세션 스코프, use_llm 파라미터)
  - `timeline_sections` fixture (세션 스코프, use_llm 파라미터)
  - 각 Fixture는 pipeline_cache 모듈 사용

**Phase 4.7.3: Issue Card 생성 로직 개선** - ✅ 완료 (2025-12-27)
- [x] `backend/builders/issues_builder.py` 수정
  - [x] `build_issue_cards()` 함수 시그니처 변경: `timeline_sections` 파라미터 추가
  - [x] DEBUG 이벤트 클러스터링 로직 구현 (논리적 이슈 단위로 그룹화)
  - [x] Timeline Section과 Issue Card 매칭 로직 구현
  - [x] **`build_issue_card_from_cluster()` 함수 수정**:
    - [x] 개별 추출 함수 호출 제거 (`extract_symptom_with_llm`, `extract_root_cause_with_llm`, `extract_fix_with_llm`, `extract_validation_with_llm`)
    - [x] `extract_issue_with_llm()` 한 번 호출로 통합 (통합 컨텍스트 기반)
    - [x] 모든 필드에 fallback 적용 (일관성):
      - `title`: `generate_issue_title_from_cluster()` 사용
      - `symptom`: 첫 번째 User Turn 사용
      - `root_cause`: 패턴 기반 추출
      - `fix`: 패턴 기반 추출
      - `validation`: 패턴 기반 추출
  - [x] **`build_issue_card_from_window()` 함수 수정**:
    - [x] window를 클러스터로 변환하여 `extract_issue_with_llm()` 사용
    - [x] 개별 추출 함수 호출 제거
    - [x] 모든 필드에 fallback 적용 (동일한 전략)

**Phase 4.7.4: LLM 서비스 리팩토링 및 통합** - ✅ 완료 (2025-12-27)
- [x] `backend/core/constants.py` 수정
  - [x] `LLM_MODEL = "gpt-4.1-mini"` 상수 추가 (커서룰에 맞춰 통일)
- [x] `backend/core/llm_service.py` 수정
  - [x] **공통 LLM 호출 함수 추출**: `_call_llm_with_retry()` 함수 생성
    - 캐시 확인/저장 로직 통합
    - 재시도 로직 (지수 백오프) 통합
    - 예외 처리 및 fallback 통합
  - [x] **모든 함수에서 `LLM_MODEL` 상수 사용**: 하드코딩된 모델명 제거
  - [x] **`extract_issue_with_llm()` 함수 개선**:
    - 반환값에 `title` 필드 추가 (필수)
    - 프롬프트에 title 생성 규칙 추가
    - 반환 구조: `{"title": str, "symptom": str, "root_cause": dict, "fix": dict, "validation": str}`
  - [x] **개별 추출 함수 제거**:
    - `extract_symptom_with_llm()` 제거
    - `extract_root_cause_with_llm()` 제거
    - `extract_fix_with_llm()` 제거
    - `extract_validation_with_llm()` 제거
  - 참고: 모든 LLM 호출 함수에서 `_call_llm_with_retry()` 사용 (향후 리팩토링 가능)

**Phase 4.7.5: IssueCard 모델 확장**
- [ ] `backend/core/models.py` 수정
  - `IssueCard` 모델에 필드 추가:
    - `section_id: Optional[str]` - 연결된 Timeline Section ID
    - `section_title: Optional[str]` - 연결된 Timeline Section 제목
    - `related_events: List[str]` - 관련 Event ID 리스트
    - `related_turns: List[int]` - 관련 Turn 인덱스 리스트
    - `confidence_score: Optional[float]` - 추출 신뢰도 점수

**Phase 4.7.6: 테스트 코드 수정**
- [ ] `tests/test_timeline_issues_e2e.py` 수정
  - Fixture 사용으로 변경 (parsed_data, normalized_events, timeline_sections)
  - 실행 순서 변경: Timeline Section 생성 → Issue Card 생성
  - 새로운 Issue Card 생성 로직 검증

**Phase 4.7.7: 캐시 무효화 전략 구현** - ✅ 완료 (이전 Phase에서 완료됨)
- [x] `backend/core/pipeline_cache.py`에 무효화 로직 추가
  - [x] 입력 파일 변경 감지 (파일 해시 비교) - 각 함수에서 자동 구현됨
  - [x] 자동 무효화 (캐시 키 기반) - 파일 해시 불일치 시 자동 무효화
  - [x] 수동 무효화 옵션 (테스트용) - `invalidate_cache()` 함수 구현됨

**검증 계획**:
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 캐시 동작 확인 (파일 저장/로드)
  - [x] 실행 순서 확인 (Timeline → Issue)
  - [x] 성능 개선 확인 (중복 실행 제거)
  - [x] 하위 호환성 확인 (기존 테스트 통과)
- [x] Issue Card 품질 평가 (2025-12-27 완료)
  - [x] 새로운 로직으로 생성된 Issue Card 품질 분석
    - **핵심 개선 사항 확인**:
      - Fix 항목: 20개 → 1개 (클러스터당, 95% 감소) ✅
      - Title: LLM 생성으로 품질 향상 ✅
      - Symptom: 구체적이고 명확함 ✅
      - Root Cause: 중간 과정 텍스트 제거, 핵심만 포함 ✅
      - Fix: 통합 컨텍스트 기반으로 구체적이고 명확함 ✅
      - Validation: 구체적인 검증 방법 제시 ✅
  - [x] Timeline Section 연결 정확성 검증 (100% 연결률) ✅
  - [x] LLM 적용 여부 확인 (2회 호출, 클러스터당 1회) ✅

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

**⚠️ 중요**: Phase 5는 패턴 기반 처리입니다 (LLM 미사용)
- 스니펫 ID 생성: 규칙 기반 (SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang})
- 언어 판별: fence_lang 우선 → 휴리스틱 (SQL/TS/Python/Bash 키워드)
- 중복 제거: 해시 기반 (SHA-256)
- 링킹: Turn/Event 인덱스 매칭

**입력-처리-출력**:
```
입력: Turns (code_blocks), Events, IssueCards, SessionMeta
처리: CodeBlock → Snippet 변환 → 중복 제거 → 링킹 → snippets.json 생성
출력: snippets.json, 업데이트된 Events/IssueCards (snippet_refs 포함)
```

**구현 계획**:

**Phase 5.1: Snippet 모델 정의** - ✅ 완료
- [x] `backend/core/models.py`에 Snippet 모델 추가
  - [x] snippet_id, lang, code, source, links, snippet_hash, aliases 필드

**Phase 5.2: 스니펫 관리 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_manager.py` 생성
  - [x] 스니펫 ID 생성 함수 (generate_snippet_id)
  - [x] 코드 정규화 및 해시 생성 함수 (normalize_code, generate_snippet_hash)
  - [x] 언어 판별 함수 (detect_language, fence_lang 우선 → 휴리스틱)
  - [x] CodeBlock → Snippet 변환 함수 (code_blocks_to_snippets)
  - [x] 중복 제거 로직 (deduplicate_snippets, 해시 기반)
  - [x] 링킹 로직 (link_snippets_to_events, link_snippets_to_issues)
  - [x] 통합 처리 함수 (process_snippets)

**Phase 5.3: 스니펫 저장 모듈 구현** - ✅ 완료
- [x] `backend/builders/snippet_storage.py` 생성
  - [x] snippets.json 생성 함수 (generate_snippets_json)

**Phase 5.4: 파이프라인 캐싱 통합 (선택적)**
- [ ] `backend/core/pipeline_cache.py`에 스니펫 캐싱 추가 (선택적)
  - [ ] get_or_create_snippets() 함수 추가

**Phase 5.5: 테스트 작성** - ✅ 완료
- [x] `tests/test_snippet_manager.py` 작성 (단위 테스트)
  - [x] test_generate_snippet_id()
  - [x] test_normalize_code()
  - [x] test_generate_snippet_hash()
  - [x] test_detect_language()
  - [x] test_code_blocks_to_snippets()
  - [x] test_deduplicate_snippets()
  - [x] test_link_snippets_to_events()
  - [x] test_link_snippets_to_issues()
- [x] `tests/test_snippet_e2e.py` 작성 (E2E 테스트)
  - [x] test_snippet_e2e_with_llm() - 전체 파이프라인 통합 테스트
    - 실제 입력 파일 사용 (docs/cursor_phase_6_3.md)
    - 파싱 → 이벤트 정규화 → Timeline → Issue Cards → 스니펫 처리
    - snippets.json 생성 및 검증
    - Event/IssueCard 링킹 검증

**검증 계획**:
- [x] 단위 테스트 실행 및 통과 확인 (9개 테스트 모두 통과)
- [x] E2E 테스트 실행 및 검증 (2025-12-27 완료)
  - [x] 스니펫 ID 형식 검증 (PASS)
  - [x] 중복 제거 검증 (해시 기반, 92개 코드 블록 → 81개 스니펫, 11개 중복 제거)
  - [x] Event 링킹 검증 (19개 이벤트에 스니펫 링크, PASS)
  - [x] Issue Card 링킹 검증 (1개 Issue Card에 스니펫 링크, PASS)
  - [x] snippets.json 구조 검증 (PASS)
- [x] E2E 테스트 결과 분석 및 리포트 생성 (2025-12-27 완료)

---

## Phase 6-8: 미완료 (간략 요약)

### Phase 6: 백엔드 API 구현
- [ ] FastAPI 엔드포인트 구현 (파싱, Timeline, Issues, Snippets, Export)
- [ ] Markdown 렌더러 구현
- [ ] 테스트 및 E2E 테스트 (실제 서버 실행)

### Phase 7: 프론트엔드 UI 구현
- [ ] Next.js 기반 웹 UI (메인 페이지, 입력 패널, 결과 미리보기, Export 패널)
- [ ] API 클라이언트 및 타입 정의
- [ ] 스타일링 (Tailwind CSS)

### Phase 8: 통합 테스트 및 QA
- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 4.7 완료, Phase 5 진행 예정 (코드 스니펫 분리 및 저장)

**마지막 업데이트**: 2025-12-27

**완료된 Phase**:
- Phase 1: 프로젝트 초기 설정 및 환경 구성 (2025-12-19)
- Phase 2: 백엔드 파서 구현 (2025-12-19)
- Phase 3.0-3.3: 이벤트 정규화 기본 구현 및 평가 방법 구축 (2025-12-20~23)
- Phase 3.4: 이벤트 정규화 품질 개선 및 타입 체계 개선 (2025-12-23~26)
  - 타입 체계 개선 완료 (CODE_GENERATION 추가, ARTIFACT 제거)
- Phase 4: Timeline 및 Issue Cards 생성 기본 구현 (2025-12-26)
  - LLM 기반 E2E 테스트 완료
- Phase 4.5: Timeline 구조화 개선 및 품질 평가 (2025-12-26)
  - Timeline 품질 평가 완료 (품질 점수: 45/100)
- Phase 4.6: Issue Card 품질 개선 (2025-12-26)
  - LLM 기반 추출 함수 구현 완료
  - E2E 테스트 완료 (품질 점수: 94/100, 하지만 실제 품질 문제 발견)
- Phase 4.7.3-4.7.4: Issue Card 생성 로직 개선 및 LLM 서비스 리팩토링 (2025-12-27 완료)
  - `extract_issue_with_llm()` 통합 함수 사용으로 전환
  - 모든 필드에 일관된 fallback 적용
  - LLM 모델 통일 (`gpt-4.1-mini`)
  - 개별 추출 함수 제거 (539줄 삭제)
  - E2E 테스트 완료: Fix 항목 20개 → 1개 (95% 감소), 품질 대폭 향상
- Phase 5: 코드 스니펫 분리 및 저장 (2025-12-27 완료)
  - Snippet 모델 정의 완료
  - 스니펫 관리 모듈 구현 완료 (ID 생성, 해시, 언어 판별, 변환, 중복 제거, 링킹)
  - 스니펫 저장 모듈 구현 완료 (snippets.json 생성)
  - 단위 테스트 완료 (9개 테스트 모두 통과)
  - E2E 테스트 완료: 92개 코드 블록 → 81개 스니펫 (11개 중복 제거), 19개 이벤트 링킹, 1개 Issue Card 링킹

**다음 단계**:
- Phase 6 진행 예정 (백엔드 API 구현)

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.

```

Phase 5 완료. 단위 테스트와 E2E 테스트 모두 통과했습니다.

## Phase 5 완료 보고

### 완료된 작업

**1. 단위 테스트 (9개 모두 통과)**
- `test_generate_snippet_id()` - 스니펫 ID 생성 규칙 검증
- `test_normalize_code()` - 코드 정규화 검증
- `test_generate_snippet_hash()` - 해시 생성 검증 (동일 코드 → 동일 해시)
- `test_detect_language()` - 언어 판별 검증 (fence_lang 우선 → 휴리스틱)
- `test_code_blocks_to_snippets()` - CodeBlock → Snippet 변환 검증
- `test_deduplicate_snippets()` - 중복 제거 검증 (해시 기반, aliases 포함)
- `test_link_snippets_to_events()` - Event 링킹 검증
- `test_link_snippets_to_issues()` - Issue Card 링킹 검증
- `test_process_snippets_integration()` - 전체 파이프라인 통합 테스트

**2. E2E 테스트 (통과)**

**테스트 결과 요약**:
- 입력: 67개 Turn, 92개 코드 블록
- 출력: 81개 스니펫 (11개 중복 제거, 12% 감소)
- 링킹: 19개 이벤트, 1개 Issue Card에 스니펫 링크 완료
- 언어 분포:
  - typescriptreact: 37개
  - typescript: 23개
  - markdown: 13개
  - tsx: 5개
  - sql: 2개
  - powershell: 1개

**검증 항목 (모두 통과)**:
- 스니펫 ID 형식 검증: PASS
- 중복 제거 검증 (해시 기반): PASS
- Event 링킹 검증: PASS
- Issue Card 링킹 검증: PASS
- snippets.json 구조 검증: PASS

### 생성된 파일

- `backend/core/models.py` - Snippet 모델 추가
- `backend/builders/snippet_manager.py` - 스니펫 관리 로직 (409줄)
- `backend/builders/snippet_storage.py` - snippets.json 생성 (75줄)
- `tests/test_snippet_manager.py` - 단위 테스트 (323줄)
- `tests/test_snippet_e2e.py` - E2E 테스트
- `tests/reports/snippet_e2e_report_20251227_185821.json` - 테스트 리포트
- `tests/results/snippet_e2e_20251227_185821.json` - 상세 결과 파일

### 수정된 파일

- `backend/builders/issues_builder.py` - IssueCard 생성 시 snippet_refs 초기화 로직 개선 (임시 형식 제거)

---

Phase 5는 완료되었습니다. 다음 단계로 Phase 6 (백엔드 API 구현) 진행 여부를 결정하면 됩니다.

---

**User**

git commit하고 마무리

---

**Cursor**

Git 상태 확인 후 커밋 진행합니다.


PowerShell 파싱 오류로 인해 커밋 메시지를 영어로 변경 중입니다.


Git 커밋 완료. Phase 5 마무리 요약입니다.

## Phase 5 완료 요약

### 완료된 작업

**1. 구현**
- Snippet 모델 정의 (`backend/core/models.py`)
- 스니펫 관리 모듈 (`backend/builders/snippet_manager.py`)
  - 스니펫 ID 생성 (SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang})
  - 코드 정규화 및 해시 생성 (SHA-256)
  - 언어 판별 (fence_lang 우선 → 휴리스틱)
  - CodeBlock → Snippet 변환
  - 중복 제거 (해시 기반, aliases 포함)
  - Event/Issue Card 링킹
- 스니펫 저장 모듈 (`backend/builders/snippet_storage.py`)
  - snippets.json 생성

**2. 테스트**
- 단위 테스트: 9개 모두 통과
- E2E 테스트: 통과
  - 92개 코드 블록 → 81개 스니펫 (11개 중복 제거)
  - 19개 이벤트 링킹, 1개 Issue Card 링킹

**3. Git 커밋**
- 커밋 메시지: `feat: Phase 5 complete - code snippet separation and storage`
- 변경 파일: 9개 파일 (1,152줄 추가, 2,747줄 삭제)

### 주요 성과

- 중복 제거: 92개 코드 블록 → 81개 스니펫 (12% 감소)
- 링킹 완료: Event 19개, Issue Card 1개에 스니펫 링크 완료
- 언어 감지: typescriptreact, typescript, markdown 등 자동 감지
- 테스트 통과: 단위/E2E 모두 통과

---

Phase 5 완료. 다음 단계는 Phase 6 (백엔드 API 구현)입니다.

