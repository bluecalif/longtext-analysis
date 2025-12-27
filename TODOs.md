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

## Phase 6: LLM 호출 최적화

**목표**: LLM 호출 횟수를 최적화하여 비용을 절감하면서 데이터 품질을 유지 또는 향상

**배경**: 
- 현재 파이프라인에서 LLM이 총 70번 호출됨 (이벤트 추출 67번 + 타임라인 1번 + 이슈카드 2번)
- 이벤트 추출: Turn 개수만큼 개별 호출 (67번) → 배치 처리로 통합 가능
- 타임라인 구조화: 1번 호출했지만 검증 실패로 Fallback 사용 → 검증 로직 개선 필요
- 이슈카드 생성: 2번 호출 (클러스터 개수만큼) → 현재 유지

**최적화 목표**:
1. 이벤트 추출: 67번 → 5-10번 (배치 처리, 10-15개 Turn씩 묶어서 처리)
2. 타임라인 구조화: 1번 호출 성공률 향상 (검증 로직 개선, LLM 결과 활용)
3. 이슈카드 생성: 2번 유지 (현재 적절함)

**예상 비용 절감**:
- 현재: 70번 호출 (이벤트 67번 + 타임라인 1번 + 이슈카드 2번) × 평균 비용 = 약 $0.00686 per 파일
- 최적화 후: 약 15-16번 호출 (이벤트 13-14번 + 타임라인 1번 + 이슈카드 2번) × 평균 비용 = 약 $0.00147-0.00157 per 파일
- **비용 절감: 약 77-78%**

### Phase 6.1: 이벤트 추출 최적화 (배치 처리)

**목표**: Turn 개별 호출을 배치 처리로 통합하여 호출 횟수 감소

**현재 구조**:
- 각 Turn마다 `classify_and_summarize_with_llm()` 개별 호출 (67번)
- `ThreadPoolExecutor(max_workers=5)`로 병렬 처리 (5개씩 동시 처리)
- 각 호출이 독립적이어서 컨텍스트 공유 불가
- 비용이 높음 (67번 호출)

**개선 방향**:
1. **배치 처리 구현**: 5개 Turn씩 묶어서 한 번에 처리 (정확도 향상)
   - 입력: Turn 리스트 (5개)
   - 출력: Event 리스트 (5개)
   - 프롬프트: 배치 내 각 Turn의 타입 분류 및 요약을 한 번에 요청
   - 배치 크기: 5개 (정확도 향상을 위해 작은 배치 크기 선택)
2. **병렬 처리 유지**: 배치 단위로 병렬 처리
   - 배치를 생성한 후 각 배치를 병렬로 처리
   - `ThreadPoolExecutor(max_workers=5)` 사용 (5개 배치 동시 처리)
   - 배치 내 Turn들은 하나의 LLM 호출로 처리되지만, 배치 간에는 병렬 처리
   - **최대 동시 처리**: 5개 배치 × 5개 Turn = 25개 Turn 동시 처리 (이론적)
   - **실제 동시 LLM 호출**: 5개 (배치 단위)
3. **컨텍스트 유지**: 배치 내 Turn 간 컨텍스트 활용
   - 이전 Turn의 요약을 다음 Turn 분류에 활용
   - 연속된 Turn의 타입 일관성 보장
4. **Fallback 전략**: 배치 처리 실패 시 개별 처리로 Fallback
5. **⚠️ 캐시 전략**: 배치 캐시만 사용 (기존 개별 캐시는 무시)
   - 캐시 키: `llm_batch_{text_hash}` 형식
   - 기존 개별 캐시(`llm_*`)는 레거시이며 사용하지 않음
   - 새 파일 처리 시 배치 캐시를 새로 생성
   - 원칙: 배치 처리를 기본으로 하고, 기존 개별 캐시는 무시하고 새로 시작

**구현 계획**:
- [x] `backend/core/llm_service.py`에 배치 처리 함수 추가 (Phase 6.1.1 완료)
  - [x] `classify_and_summarize_batch_with_llm()` 함수 구현
    - 입력: Turn 리스트 (5개)
    - 출력: Event 리스트 (타입 + 요약, 5개)
    - 프롬프트: 배치 단위로 타입 분류 및 요약 요청 (각 Turn별로)
    - 캐싱: 배치 단위로 캐시 키 생성 (배치 내 Turn 해시 결합)
    - JSON 형식 응답: `response_format={"type": "json_object"}` 사용
    - Fallback: 배치 실패 시 개별 처리로 자동 전환
- [x] `backend/builders/event_normalizer.py` 수정 (Phase 6.1.2 완료)
  - [x] `_normalize_turns_to_events_parallel()` 함수 수정
    - Turn 리스트를 5개씩 배치로 분할 (67개 → 13-14개 배치)
    - 개별 호출 대신 `classify_and_summarize_batch_with_llm()` 사용
    - 배치 단위로 병렬 처리 (max_workers=5)
    - 기존 병렬 처리 구조 유지 (배치 단위로 적용)
    - **처리 흐름**: 
      1. 67개 Turn → 13-14개 배치 생성 (5개씩)
      2. 5개 배치를 동시에 병렬 처리 (max_workers=5)
      3. 각 배치는 `classify_and_summarize_batch_with_llm()`로 5개 Turn을 하나의 LLM 호출로 처리
      4. 최대 5개 LLM 호출 동시 실행
    - 배치 결과를 Event 객체로 변환 (`_process_batch()` 함수 추가)
    - turn_index 순서 유지
    - Fallback: 배치 실패 시 개별 처리로 자동 전환
- [x] 테스트 작성 (Phase 6.1.5 완료)
  - [x] 단위 테스트: 배치 처리 함수 테스트 (`test_llm_service_batch_processing`, `test_llm_service_batch_processing_fallback`)
  - [x] E2E 테스트: 전체 파이프라인에서 배치 처리 검증 (`test_event_normalizer_e2e_with_llm` 수정)
    - 배치 캐시 확인 로직 추가
    - `processing_method` 검증: "llm_batch" 확인
    - 배치 단위 캐시 통계 수집
  - [x] 성능 테스트: 호출 횟수 및 비용 측정 (리포트에 포함)

**검증 계획**:
- [ ] 호출 횟수 검증: 67번 → 약 13-14번 (67개 Turn ÷ 5개 배치)
- [ ] 데이터 품질 검증: 개별 처리와 동일하거나 향상된 품질 (배치 내 컨텍스트 활용)
- [ ] 비용 절감 검증: 약 80% 비용 절감 (67번 → 13-14번)
- [ ] 캐시 효율성 검증: 배치 캐시 히트율 확인
- [ ] 병렬 처리 효율성 검증: 5개 배치 동시 처리 성능 확인
- [ ] LLM API 제한 검증: 5개 동시 호출이 Rate limit 내에서 안전한지 확인
- [ ] 토큰 사용량 검증: 배치 처리 시 입력 토큰 증가량 측정 (5개 Turn × 배치당)

**5개 배치 × 5개 병렬 처리 검토 결과**:
- ✅ **장점**:
  - 처리 속도 향상: 5개 배치 동시 처리로 전체 처리 시간 단축
  - LLM API 제한 안전: max_workers=5는 기존 코드에서 검증된 안전한 값
  - 호출 횟수 감소: 67번 → 13-14번 (약 80% 감소)
- ⚠️ **주의사항**:
  - 입력 토큰 증가: 배치당 5개 Turn이므로 입력 토큰이 약 5배 증가 (하지만 호출 횟수는 1/5로 감소)
  - 응답 시간: 배치 처리 시 응답 시간이 길어질 수 있지만, 병렬 처리로 보완
  - 에러 처리: 배치 실패 시 5개 Turn 모두 재처리 필요 (부분 실패 처리 로직 중요)
- 📊 **예상 성능**:
  - 동시 LLM 호출: 최대 5개 (5개 배치 동시 처리)
  - 처리 시간: 배치당 평균 응답 시간 × (13-14개 배치 ÷ 5개 병렬) ≈ 약 3-4 라운드
  - 전체 처리 시간: 개별 처리 대비 약 60-70% 단축 예상

### Phase 6.2: 타임라인 구조화 최적화 (검증 로직 개선)

**목표**: LLM 결과 검증 실패 문제 해결 및 LLM 결과 활용

**현재 문제점**:
- LLM이 5개 작업 항목을 성공적으로 추출했지만 검증 단계에서 실패
- 코드 172-174줄: `task_events`가 비어있으면 `continue`로 건너뜀
- 코드 189줄: `if sections:` 조건이 False가 되어 Fallback 사용
- 원인: LLM이 반환한 `event_seqs`가 `group_events`에 없는 이벤트를 포함하거나, 매칭 실패

**개선 방향**:
1. **검증 로직 개선**: 
   - LLM이 반환한 `event_seqs`와 실제 `group_events`의 seq 매칭 로직 개선
   - 누락된 이벤트는 자동으로 포함하도록 처리
   - 잘못된 seq는 무시하고 유효한 seq만 사용
2. **LLM 프롬프트 개선**:
   - `event_seqs`에 정확한 seq 값만 포함하도록 명확히 지시
   - 모든 이벤트가 포함되도록 검증 규칙 강화
3. **Fallback 전략 개선**:
   - 부분 성공 시 성공한 섹션은 사용, 실패한 부분만 Fallback
   - 완전 실패 시에만 전체 Fallback

**구현 계획**:
- [ ] `backend/core/llm_service.py` 수정
  - [ ] `extract_main_tasks_with_llm()` 함수 수정
    - 검증 로직 개선: 유효한 seq만 필터링하여 사용
    - 누락된 이벤트 자동 포함 로직 추가
    - 부분 성공 처리 로직 추가
- [ ] `backend/builders/timeline_builder.py` 수정
  - [ ] `_extract_main_tasks_from_group()` 함수 수정
    - 검증 실패 시 부분 성공 처리
    - LLM 결과 활용 우선, 실패한 부분만 Fallback
- [ ] 프롬프트 개선
  - `event_seqs` 정확성 강조
  - 모든 이벤트 포함 검증 규칙 추가
- [ ] 테스트 작성
  - [ ] 단위 테스트: 검증 로직 개선 테스트
  - [ ] E2E 테스트: LLM 결과 활용 검증
  - [ ] 품질 테스트: LLM 결과 vs Fallback 결과 비교

**검증 계획**:
- [ ] LLM 결과 활용률: 0% → 100%
- [ ] 섹션 품질 검증: LLM 결과가 Fallback보다 우수한지 확인
- [ ] 검증 실패율: 100% → 0%

---

## Phase 7-9: 미완료 (간략 요약)

### Phase 7: 백엔드 API 구현
- [ ] FastAPI 엔드포인트 구현 (파싱, Timeline, Issues, Snippets, Export)
- [ ] Markdown 렌더러 구현
- [ ] 테스트 및 E2E 테스트 (실제 서버 실행)

### Phase 8: 프론트엔드 UI 구현
- [ ] Next.js 기반 웹 UI (메인 페이지, 입력 패널, 결과 미리보기, Export 패널)
- [ ] API 클라이언트 및 타입 정의
- [ ] 스타일링 (Tailwind CSS)

### Phase 9: 통합 테스트 및 QA
- [ ] 전체 시스템 통합 테스트
- [ ] 품질 체크 (JSON Schema 검증 등)
- [ ] 성능 최적화
- [ ] 문서화

---

## 진행 상황 추적

**현재 Phase**: Phase 6.1 진행 중 (이벤트 추출 최적화 - 배치 처리)

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
- Phase 6.1: 이벤트 추출 최적화 (배치 처리) (2025-12-27 완료)
  - 배치 처리 LLM 함수 구현 완료 (`classify_and_summarize_batch_with_llm()`)
  - 이벤트 정규화 모듈 배치 처리로 변경 완료
  - 배치 캐시 전략 적용 (기존 개별 캐시 무시, 배치 캐시만 사용)
  - 단위 테스트 및 E2E 테스트 완료
  - 예상 비용 절감: 67번 호출 → 13-14번 호출 (약 80% 감소)

**진행 중인 Phase**:
- Phase 6: LLM 호출 최적화 (진행 중)
  - Phase 6.1: 이벤트 추출 최적화 (배치 처리) - ✅ 완료
    - Phase 6.1.1: ✅ 완료 - 배치 처리 LLM 함수 구현 (`classify_and_summarize_batch_with_llm()`)
    - Phase 6.1.2: ✅ 완료 - 이벤트 정규화 모듈 수정 (`_normalize_turns_to_events_parallel()` 배치 처리로 변경)
    - Phase 6.1.3: ✅ 완료 - 캐시 키 생성 로직 수정 (Phase 6.1.1에 포함)
    - Phase 6.1.4: ✅ 완료 - Fallback 로직 구현 (Phase 6.1.2에 포함)
    - Phase 6.1.5: ✅ 완료 - 테스트 작성 및 검증
  - Phase 6.2: 타임라인 구조화 최적화 (검증 로직 개선) - 대기

**다음 단계**:
- Phase 6.2 진행 예정 (타임라인 구조화 최적화 - 검증 로직 개선)

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.
