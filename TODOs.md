# Longtext Analysis 프로젝트 TODOs

> **프로젝트 개요**: Cursor IDE에서 export된 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 웹 애플리케이션

**기술 스택**: Python FastAPI (Poetry), Next.js 14+ (App Router, TypeScript), OpenAI API (옵션)

**참고 문서**: [PRD](docs/PRD_longtext.md), [상세 지침](docs/instruction_detail.md), [구체화 지침](docs/instruction_moredetail.md)

**E2E 테스트 입력 데이터**: `docs/cursor_phase_6_3.md`

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

**Phase 4.7.3: Issue Card 생성 로직 개선**
- [ ] `backend/builders/issues_builder.py` 수정
  - `build_issue_cards()` 함수 시그니처 변경: `timeline_sections` 파라미터 추가
  - DEBUG 이벤트 클러스터링 로직 구현 (논리적 이슈 단위로 그룹화)
  - Timeline Section과 Issue Card 매칭 로직 구현
  - 각 클러스터별로 통합 컨텍스트 구성 (Section + Events + Turns)

**Phase 4.7.4: LLM 프롬프트 및 출력 구조 개선**
- [ ] `backend/core/llm_service.py`에 새로운 함수 추가
  - `extract_issue_with_llm()` 함수 구현
    - 입력: TimelineSection + 관련 Events + 관련 Turns (통합 컨텍스트)
    - 프롬프트: 구조화된 출력 요청 (현상-원인-개선내용)
    - 출력: 구조화된 JSON (symptom, root_cause, fix, validation)
  - 기존 개별 추출 함수는 유지 (하위 호환성)

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

**Phase 4.7.7: 캐시 무효화 전략 구현**
- [ ] `backend/core/pipeline_cache.py`에 무효화 로직 추가
  - 입력 파일 변경 감지 (파일 해시 비교)
  - 자동 무효화 (캐시 키 기반)
  - 수동 무효화 옵션 (테스트용)

**검증 계획**:
- [ ] E2E 테스트 실행 및 검증
  - 캐시 동작 확인 (파일 저장/로드)
  - 실행 순서 확인 (Timeline → Issue)
  - 성능 개선 확인 (중복 실행 제거)
  - 하위 호환성 확인 (기존 테스트 통과)
- [ ] Issue Card 품질 평가
  - 새로운 로직으로 생성된 Issue Card 품질 분석
  - Timeline Section 연결 정확성 검증
  - LLM 적용 여부 확인

---

## Phase 5: 코드 스니펫 분리 및 저장

**목표**: 코드 스니펫을 별도로 저장하고 참조 연결

- [ ] 스니펫 ID 생성 규칙 구현
- [ ] 스니펫 중복 제거 로직 (코드 내용 해시 기반)
- [ ] 스니펫 파일 저장 기능 (선택)
- [ ] Issue/Timeline과의 링킹 로직
- [ ] 테스트 작성 및 E2E 테스트

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

**현재 Phase**: Phase 4.7 진행 중 (파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토)

**마지막 업데이트**: 2025-12-26

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

**진행 중인 Phase**:
- Phase 4.7: 파이프라인 데이터 관리 개선 및 Issue Card 로직 전면 재검토 (2025-12-26 시작)
  - 목표: 중복 실행 제거, Timeline Section 활용, Issue Card 로직 전면 재검토
  - 7개 서브 Phase로 구성 (4.7.1 ~ 4.7.7)

**다음 단계**:
- Phase 4.7 완료 후 Phase 5 진행 예정
  - Phase 4.7 완료 후 사용자 피드백 대기

---

## 참고: 이전 Archive

자세한 내용은 `TODOs_archive_20251226.md` 파일을 참조하세요.
