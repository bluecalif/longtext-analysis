# Phase 3 품질 개선 계획

> **목적**: Phase 3에서 발견된 3가지 최상급 문제점 해결
> - 이벤트 중복 생성 문제
> - Summary 품질 문제
> - 타입 분류 정확도 문제

**참고**: 이 문서는 Phase 3의 품질 개선 작업에 대한 상세 계획입니다. 진행 상황은 `TODOs.md`의 Phase 3 섹션에서 확인할 수 있습니다.

---

## 문제점 분석

### 현재 상태
- 총 Turn: 67개
- 총 Event: 117개 (1.75배, 중복 생성)
- 이벤트 타입 분류 정확도: 약 60-70% (정규식 기반)
- Summary 품질: 200자 단순 자르기, 줄바꿈 미처리

### 주요 문제점

1. **이벤트 중복 생성** (최상급)
   - 같은 Turn에서 artifact + debug + status_review 등 다중 생성
   - 결과: 117개 Event (중복으로 인한 저장 공간 낭비)

2. **Summary 품질** (최상급)
   - 200자 단순 자르기로 의미 없는 위치에서 잘림
   - 줄바꿈 문자 미처리 (`\n\n\n\n`)

3. **타입 분류 정확도** (최상급)
   - 정규식만으로는 95% 달성 어려움 (현재 60-70%)
   - 일반 단어("상태", "phase")가 특수 타입으로 과도하게 매칭

---

## Phase 3.1: 즉시 개선 (정규식 기반)

### 1. 이벤트 중복 생성 방지

**목표**: 우선순위 기반 단일 이벤트 생성

**구현**:
```python
def normalize_turns_to_events(turns: List[Turn]) -> List[Event]:
    """
    우선순위 기반 단일 이벤트 생성
    """
    events = []
    
    for turn in turns:
        # 우선순위 기반 단일 이벤트 생성
        event = create_single_event_with_priority(turn)
        events.append(event)
    
    return events

def create_single_event_with_priority(turn: Turn) -> Event:
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
    """
    # 1순위: DEBUG (디버그 트리거 + Cursor 발화)
    if is_debug_turn(turn):
        return create_debug_event(turn, processing_method="regex")
    
    # 2순위: ARTIFACT (파일 경로 존재)
    if turn.path_candidates:
        return create_artifact_event(turn, processing_method="regex")
    
    # 3순위: 특수 타입 (엄격한 정규식)
    event_type = classify_event_type_strict(turn)
    if event_type != EventType.TURN:
        return create_message_event(turn, event_type, processing_method="regex")
    
    # 4순위: 기본 TURN
    return create_message_event(turn, EventType.TURN, processing_method="regex")
```

**예상 효과**:
- 117개 → 약 70-80개 이벤트 (30-40% 감소)
- 중복 제거, 저장 공간 절감

---

### 2. Summary 품질 개선 (정규식 기반)

**목표**: 의미 있는 위치에서 자르기, 줄바꿈 정리

**구현**:
```python
def summarize_turn(turn: Turn, processing_method: str = "regex") -> str:
    """
    Turn을 요약 (정규식 기반 개선)
    
    Args:
        turn: Turn 객체
        processing_method: "regex" 또는 "llm" (결과 파일에 기록용)
    
    Returns:
        요약 텍스트
    """
    body = turn.body.strip()
    
    # 1. 줄바꿈 정리 (연속된 \n을 최대 2개로 제한)
    body = re.sub(r'\n{3,}', '\n\n', body)
    
    # 2. 200자 이하면 그대로 반환
    if len(body) <= 200:
        return body
    
    # 3. 의미 있는 위치에서 자르기 (우선순위 순)
    
    # 옵션 A: 마지막 완전한 문장까지만 (마침표/물음표/느낌표 기준)
    sentences = re.split(r'([.!?。！？]\s+)', body[:250])
    if len(sentences) > 1:
        summary = ''.join(sentences[:-2])
        if 100 <= len(summary) <= 200:
            return summary.rstrip() + "..."
    
    # 옵션 B: 마지막 줄바꿈 기준 (문단 단위)
    last_newline = body[:200].rfind('\n\n')
    if last_newline > 100:
        return body[:last_newline].rstrip() + "..."
    
    # 옵션 C: 마지막 공백 기준 (단어 중간 자르기 방지)
    last_space = body[:200].rfind(' ')
    if last_space > 150:
        return body[:last_space] + "..."
    
    # 최후: 200자 자르기
    return body[:200] + "..."
```

**예상 효과**:
- Summary 가독성 향상
- 의미 있는 위치에서 자르기
- 줄바꿈 정리

---

### 3. 타입 분류 엄격화 (정규식 기반)

**목표**: 일반 단어 매칭을 피하기 위해 더 구체적인 패턴 사용

**구현**:
```python
def classify_event_type_strict(turn: Turn) -> EventType:
    """
    엄격한 조건으로 이벤트 타입 분류 (정규식 기반)
    
    일반 단어 매칭을 피하기 위해 더 구체적인 패턴 사용
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
```

**예상 효과**:
- 정확도: 60-70% → 75-80%
- 과도한 매칭 감소

---

## Phase 3.2: LLM 선택적 적용 (gpt-4.1-mini)

### 4. LLM 적용 전략

**전략**: 일괄 LLM 적용 (모든 Turn에 대해)

**이유**:
- "불확실한 경우" 판단이 모호함
- 일괄 적용 시 일관성 확보
- 캐싱으로 비용 절감 가능

**구현**:
```python
def normalize_turns_to_events(turns: List[Turn], use_llm: bool = True) -> List[Event]:
    """
    Turn 리스트를 Event 리스트로 변환 (LLM 옵션)
    
    Args:
        turns: 파싱된 Turn 리스트
        use_llm: LLM 사용 여부 (기본값: True, 일괄 적용)
    
    Returns:
        정규화된 Event 리스트
    """
    events = []
    
    for turn in turns:
        if use_llm:
            # LLM 기반 이벤트 생성
            event = create_event_with_llm(turn)
        else:
            # 정규식 기반 이벤트 생성
            event = create_single_event_with_priority(turn)
        
        events.append(event)
    
    return events
```

---

### 5. Event 모델에 processing_method 필드 추가

**목표**: 결과 파일에 정규식/LLM 구분 표시

**구현**:
```python
class Event(BaseModel):
    """이벤트 기본 모델 (정규화된 Turn)"""

    type: EventType
    turn_ref: int
    summary: str
    artifacts: List[dict] = []
    snippet_refs: List[str] = []
    processing_method: str = "regex"  # "regex" 또는 "llm" (결과 파일에 기록)
```

---

### 6. LLM 서비스 구현 (gpt-4.1-mini)

**중요**: 모델명은 반드시 `"gpt-4.1-mini"` 사용 (사용자 지시)

**구현**:
```python
def classify_and_summarize_with_llm(turn: Turn) -> dict:
    """
    LLM으로 타입 분류 및 요약 생성 (gpt-4.1-mini, 캐싱 적용)
    
    Args:
        turn: Turn 객체
    
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
    cache_key = f"llm_{hash(turn.body[:1000]) % 1000000}"
    
    # 캐시 확인
    cached = get_cached_result(cache_key)
    if cached:
        return {
            "event_type": EventType(cached["event_type"]),
            "summary": cached["summary"],
        }
    
    # LLM 호출
    from openai import OpenAI
    client = OpenAI()
    
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
SUMMARY: [1-2문장 요약]"""
            },
            {
                "role": "user",
                "content": turn.body[:2000]  # 토큰 절감
            }
        ],
        max_tokens=150,  # 타입 + 요약
        temperature=0.3  # 일관성 유지
    )
    
    result_text = response.choices[0].message.content.strip()
    
    # 응답 파싱
    event_type_str = None
    summary = None
    
    for line in result_text.split('\n'):
        if line.startswith('TYPE:'):
            event_type_str = line.replace('TYPE:', '').strip().lower()
        elif line.startswith('SUMMARY:'):
            summary = line.replace('SUMMARY:', '').strip()
    
    # 타입 검증
    try:
        event_type = EventType(event_type_str) if event_type_str else EventType.TURN
    except ValueError:
        event_type = EventType.TURN
    
    # 요약이 없으면 기본 요약
    if not summary:
        summary = summarize_turn(turn, processing_method="regex")
    
    result = {
        "event_type": event_type.value,
        "summary": summary,
    }
    
    # 캐시 저장
    save_cached_result(cache_key, result)
    
    return {
        "event_type": event_type,
        "summary": summary,
    }
```

**비용 추정**:
- Turn당 평균: $0.0000196-0.0000294 (캐싱 후)
- 67개 Turn 처리 시: $0.0013-0.0020
- 월 1000개 세션 처리 시: $1.3-2.0

---

## Phase 3.3: 결과 평가 방법 구축

### 7. 정성적 평가 (수동 검증)

**목표**: 타입 분류 정확도를 수동 검증으로 평가

**프로세스**:
1. **데이터셋 생성**: `create_manual_review_dataset()` 실행 → `tests/golden/manual_review_dataset.json` 생성
2. **수동 라벨링**: 사용자가 파일을 열어 각 샘플의 `manual_label` 채움
3. **정확도 계산**: `evaluate_manual_review()` 실행하여 정확도 계산 (AI가 실행 또는 사용자가 직접 실행)

**구현**:
```python
def create_manual_review_dataset(
    events: List[Event],
    turns: List[Turn],
    sample_size: int = 30,
    output_file: Path
) -> dict:
    """
    수동 검증용 데이터셋 생성
    
    Args:
        events: 이벤트 리스트
        turns: Turn 리스트
        sample_size: 샘플 크기
        output_file: 출력 파일 경로
    
    Returns:
        {
            "sample_events": List[dict],  # 평가 대상 샘플
            "review_instructions": str,    # 검증 가이드라인
        }
    """
    # 샘플링 전략: 다양한 타입 균등 샘플링
    events_by_type = {}
    for event in events:
        event_type = event.type.value
        if event_type not in events_by_type:
            events_by_type[event_type] = []
        events_by_type[event_type].append(event)
    
    # 각 타입에서 균등하게 샘플링
    samples_per_type = max(1, sample_size // len(events_by_type))
    sample_events = []
    
    for event_type, type_events in events_by_type.items():
        import random
        sampled = random.sample(type_events, min(samples_per_type, len(type_events)))
        for event in sampled:
            turn = turns[event.turn_ref]
            sample_events.append({
                "event_index": events.index(event),
                "turn_ref": event.turn_ref,
                "predicted_type": event.type.value,
                "processing_method": getattr(event, 'processing_method', 'regex'),
                "turn_body": turn.body[:500],  # 원문 일부
                "summary": event.summary,
                "manual_label": {
                    "correct_type": None,  # 수동 검증용
                    "correct_summary": None,  # 수동 검증용
                    "notes": None,  # 추가 메모
                },
            })
    
    # 검증 가이드라인 작성
    review_instructions = """
# 이벤트 타입 분류 수동 검증 가이드라인

## 검증 방법

1. 각 샘플의 `predicted_type`이 올바른지 확인하세요.
2. `turn_body`를 읽고 실제 이벤트 타입을 판단하세요.
3. `correct_type`에 올바른 타입을 입력하세요.
4. `summary`가 적절한지 확인하고, 필요시 `correct_summary`에 수정된 요약을 입력하세요.

## 이벤트 타입 판단 기준

- **status_review**: 상태 리뷰, 현황 점검, 진행 상황 확인
- **plan**: 계획 수립, 작업 계획, 단계별 계획
- **artifact**: 파일/경로 언급, 생성, 수정
- **debug**: 에러, 원인 분석, 해결 방법, 검증
- **completion**: 작업 완료, 성공
- **next_step**: 다음 단계, 다음 작업
- **turn**: 일반 대화 (기본값)

## 검증 후 작업

1. `manual_review_results.json` 파일을 생성하세요.
2. 각 샘플의 `manual_label`을 채워주세요.
3. 검증 완료 후 `evaluate_manual_review()` 함수로 정확도 계산
"""
    
    # JSON 파일로 저장
    dataset = {
        "sample_events": sample_events,
        "review_instructions": review_instructions,
        "total_samples": len(sample_events),
        "created_at": datetime.now().isoformat(),
    }
    
    output_file.write_text(
        json.dumps(dataset, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    
    return dataset

def evaluate_manual_review(
    events: List[Event],
    manual_review_file: Path
) -> dict:
    """
    수동 검증 결과를 기반으로 정확도 계산
    
    Args:
        events: 이벤트 리스트
        manual_review_file: 수동 검증 결과 파일
    
    Returns:
        {
            "type_classification_accuracy": float,  # 타입 분류 정확도
            "summary_accuracy": float,              # Summary 정확도
            "confusion_matrix": dict,                # 혼동 행렬
            "by_processing_method": dict,          # 처리 방법별 정확도
        }
    """
    if not manual_review_file.exists():
        return {
            "type_classification_accuracy": None,
            "summary_accuracy": None,
            "confusion_matrix": None,
            "by_processing_method": None,
            "message": "수동 검증 파일이 없습니다. create_manual_review_dataset()을 먼저 실행하세요.",
        }
    
    # 수동 검증 결과 로드
    review_data = json.loads(manual_review_file.read_text(encoding="utf-8"))
    
    # 정확도 계산
    correct_type_count = 0
    correct_summary_count = 0
    total_count = 0
    
    confusion_matrix = {}
    by_method = {"regex": {"correct": 0, "total": 0}, "llm": {"correct": 0, "total": 0}}
    
    for sample in review_data.get("sample_events", []):
        if sample["manual_label"]["correct_type"] is None:
            continue  # 검증되지 않은 샘플 제외
        
        total_count += 1
        
        # 타입 정확도
        if sample["predicted_type"] == sample["manual_label"]["correct_type"]:
            correct_type_count += 1
        
        # 처리 방법별 정확도
        method = sample.get("processing_method", "regex")
        by_method[method]["total"] += 1
        if sample["predicted_type"] == sample["manual_label"]["correct_type"]:
            by_method[method]["correct"] += 1
        
        # 혼동 행렬
        predicted = sample["predicted_type"]
        actual = sample["manual_label"]["correct_type"]
        if predicted not in confusion_matrix:
            confusion_matrix[predicted] = {}
        confusion_matrix[predicted][actual] = confusion_matrix[predicted].get(actual, 0) + 1
        
        # Summary 정확도 (수정된 summary가 있으면 비교)
        if sample["manual_label"]["correct_summary"]:
            # 간단한 유사도 계산 (실제로는 더 정교한 방법 사용 가능)
            if sample["summary"] == sample["manual_label"]["correct_summary"]:
                correct_summary_count += 1
    
    type_accuracy = correct_type_count / total_count if total_count > 0 else 0.0
    summary_accuracy = correct_summary_count / total_count if total_count > 0 else 0.0
    
    # 처리 방법별 정확도 계산
    for method in by_method:
        if by_method[method]["total"] > 0:
            by_method[method]["accuracy"] = by_method[method]["correct"] / by_method[method]["total"]
        else:
            by_method[method]["accuracy"] = None
    
    return {
        "type_classification_accuracy": type_accuracy,
        "summary_accuracy": summary_accuracy,
        "confusion_matrix": confusion_matrix,
        "by_processing_method": by_method,
        "total_reviewed": total_count,
    }
```

---

### 8. Golden 파일 관리 (회귀 테스트용)

**목적**: 개선 사이클 완료 후 회귀 테스트용 (개선 사이클 자체에는 미사용)

**프로세스**:
1. **생성 시점**: 개선 사이클 완료 후, 품질 검증 통과 시
2. **생성 위치**: `tests/golden/event_normalizer_expected.json`
3. **생성 주체**: E2E 테스트 자동 생성 또는 사용자 수동 생성
4. **사용 시점**: 이후 코드 변경 시 기존 결과와 비교하여 회귀(악화) 확인

**구현**:
```python
def create_golden_file(
    events: List[Event],
    turns: List[Turn],
    session_meta: SessionMeta,
    golden_file: Path,
    force: bool = False
) -> dict:
    """
    Golden 파일 생성 (회귀 테스트용)
    
    Args:
        events: 현재 생성된 이벤트
        turns: Turn 리스트
        session_meta: 세션 메타데이터
        golden_file: Golden 파일 경로
        force: 기존 파일이 있어도 덮어쓰기 여부
    
    Returns:
        {
            "created": bool,
            "file_path": str,
            "message": str
        }
    """
    if golden_file.exists() and not force:
        return {
            "created": False,
            "file_path": str(golden_file),
            "message": "Golden 파일이 이미 존재합니다. force=True로 덮어쓰려면 설정하세요.",
        }
    
    # Golden 파일 생성
    golden_data = {
        "session_meta": session_meta.model_dump(),
        "turns_count": len(turns),
        "events": [
            {
                "type": event.type.value,
                "turn_ref": event.turn_ref,
                "summary": event.summary[:200],  # 요약만 저장 (전체는 너무 큼)
                "processing_method": getattr(event, 'processing_method', 'regex'),
                "artifacts_count": len(event.artifacts),
                "snippet_refs_count": len(event.snippet_refs),
            }
            for event in events
        ],
        "event_type_distribution": {},
        "created_at": datetime.now().isoformat(),
        "created_by": "e2e_test",  # 또는 사용자명
        "input_file": str(session_meta.source_doc),
    }
    
    # 이벤트 타입 분포 계산
    for event in events:
        event_type = event.type.value
        golden_data["event_type_distribution"][event_type] = (
            golden_data["event_type_distribution"].get(event_type, 0) + 1
        )
    
    # 파일 저장
    golden_file.parent.mkdir(parents=True, exist_ok=True)
    golden_file.write_text(
        json.dumps(golden_data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    
    return {
        "created": True,
        "file_path": str(golden_file),
        "message": f"Golden 파일 생성 완료: {golden_file}",
    }

def compare_with_golden(events: List[Event], golden_file: Path) -> dict:
    """
    Golden 파일과 비교하여 회귀 테스트
    
    Args:
        events: 현재 생성된 이벤트
        golden_file: Golden 파일 경로
    
    Returns:
        {
            "match_rate": float,      # 일치율
            "differences": List[dict], # 차이점
            "regression_detected": bool
        }
    """
    if not golden_file.exists():
        return {
            "match_rate": None,
            "differences": [],
            "regression_detected": False,
            "message": "Golden 파일이 없습니다. create_golden_file()을 먼저 실행하세요.",
        }
    
    # Golden 파일 로드
    golden_data = json.loads(golden_file.read_text(encoding="utf-8"))
    golden_events = golden_data["events"]
    
    # 비교 (주요 필드만)
    differences = []
    match_count = 0
    
    # 이벤트 수 비교
    if len(events) != len(golden_events):
        differences.append({
            "type": "count_mismatch",
            "current": len(events),
            "golden": len(golden_events),
        })
    
    # 각 이벤트 비교
    for i, (current, golden) in enumerate(zip(events, golden_events)):
        diff = {}
        
        if current.type.value != golden["type"]:
            diff["type"] = {"current": current.type.value, "golden": golden["type"]}
        
        if current.turn_ref != golden["turn_ref"]:
            diff["turn_ref"] = {"current": current.turn_ref, "golden": golden["turn_ref"]}
        
        # processing_method 비교
        current_method = getattr(current, 'processing_method', 'regex')
        golden_method = golden.get('processing_method', 'regex')
        if current_method != golden_method:
            diff["processing_method"] = {"current": current_method, "golden": golden_method}
        
        if diff:
            differences.append({"event_index": i, "differences": diff})
        else:
            match_count += 1
    
    match_rate = match_count / len(events) if events else 0.0
    regression_detected = match_rate < 0.95  # 95% 미만이면 회귀
    
    return {
        "match_rate": match_rate,
        "differences": differences,
        "regression_detected": regression_detected,
        "total_events": len(events),
        "matched_events": match_count,
    }
```

---

## 예상 효과

### Phase 3.1 완료 후
- 이벤트 수: 117개 → 70-80개 (30-40% 감소)
- Summary 품질: 가독성 향상
- 타입 분류 정확도: 60-70% → 75-80%

### Phase 3.2 완료 후 (LLM 적용)
- 타입 분류 정확도: 75-80% → 90-95%
- LLM 비용: 세션당 $0.0013-0.0020 (캐싱 후)

---

## 참고 사항

- **모델명**: 반드시 `"gpt-4.1-mini"` 사용 (사용자 지시)
- **LLM 적용**: 일괄 적용 (모든 Turn에 대해)
- **결과 파일**: `processing_method` 필드로 정규식/LLM 구분 표시
- **정량적 평가**: 제외 (타입 분류는 정량적 평가 불가능)
- **정성적 평가**: 수동 검증 (사용자가 라벨 채움 → AI가 평가 함수 실행)
- **Golden 파일**: 개선 사이클 완료 후 회귀 테스트용 (개선 사이클에는 미사용)

