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

