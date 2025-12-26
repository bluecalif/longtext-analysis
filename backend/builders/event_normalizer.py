"""
이벤트 정규화 모듈

파싱된 Turn 데이터를 이벤트로 정규화합니다.
"""

import re
from typing import List, Optional, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from backend.core.models import Turn, Event, EventType, SessionMeta, ArtifactAction
from backend.core.constants import DEBUG_TRIGGERS


def normalize_turns_to_events(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None, use_llm: bool = False
) -> List[Event]:
    """
    Turn 리스트를 Event 리스트로 변환 (우선순위 기반 단일 이벤트, LLM 옵션)

    LLM 사용 시 병렬 처리 (max_workers=5)

    Args:
        turns: 파싱된 Turn 리스트
        session_meta: 세션 메타데이터 (Phase/Subphase 연결용, 선택)
        use_llm: LLM 사용 여부 (기본값: False, True 시 일괄 적용, 병렬 처리)

    Returns:
        정규화된 Event 리스트
    """
    if use_llm:
        # 병렬 처리 (ThreadPoolExecutor)
        events = _normalize_turns_to_events_parallel(turns, session_meta)
    else:
        # 순차 처리 (기존 로직)
        events = []
        for turn in turns:
            event = create_single_event_with_priority(turn, session_meta)
            events.append(event)

    # 시퀀스 번호 부여
    for i, event in enumerate(events):
        event.seq = i + 1

    return events


def _normalize_turns_to_events_parallel(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None
) -> List[Event]:
    """
    LLM 기반 이벤트 생성 (병렬 처리, 하이브리드 방식)

    하이브리드 방식:
    1. 1차: 병렬로 모든 Turn 처리 (맥락 없이)
    2. 2차: 순차적으로 맥락 정보를 활용하여 재분류 (필요시)

    Args:
        turns: Turn 리스트
        session_meta: 세션 메타데이터

    Returns:
        Event 리스트 (turn_index 순서 유지)
    """
    events_dict = {}  # turn_index -> Event 매핑

    # 1차: 병렬로 모든 Turn 처리 (맥락 없이, 빠른 처리)
    with ThreadPoolExecutor(max_workers=5) as executor:
        # 각 Turn을 병렬로 처리
        future_to_turn = {
            executor.submit(create_event_with_llm, turn, session_meta, turns, None): turn
            for turn in turns
        }

        # 완료된 작업부터 처리 (순서 보장을 위해 turn_index 저장)
        for future in as_completed(future_to_turn):
            turn = future_to_turn[future]
            try:
                event = future.result()
                events_dict[turn.turn_index] = event
            except Exception as e:
                # 에러 발생 시 기본 이벤트 생성 (fallback)
                # 로깅은 선택적 (필요시 추가)
                event = create_single_event_with_priority(turn, session_meta)
                events_dict[turn.turn_index] = event

    # 2차: 맥락 정보를 활용하여 재분류 (순차 처리)
    # 현재는 1차 결과를 그대로 사용 (향후 개선 가능)
    # 맥락 정보가 중요한 경우에만 재분류하도록 최적화 가능

    # turn_index 순서로 정렬
    events = [events_dict[turn.turn_index] for turn in turns]
    return events


def create_event_with_llm(
    turn: Turn,
    session_meta: Optional[SessionMeta] = None,
    turns: Optional[List[Turn]] = None,  # 전체 Turn 리스트 추가
    existing_events: Optional[Dict[int, Event]] = None  # 이미 생성된 Event들
) -> Event:
    """
    LLM 기반 이벤트 생성 (gpt-4.1-mini, 맥락 정보 포함)

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)
        turns: 전체 Turn 리스트 (맥락 정보 수집용, 선택)
        existing_events: 이미 생성된 Event 딕셔너리 (맥락 정보 수집용, 선택)

    Returns:
        Event 객체 (processing_method="llm")
    """
    from backend.core.llm_service import classify_and_summarize_with_llm

    # 맥락 정보 수집
    context_info = None
    if turns is not None:
        if existing_events is not None:
            # 이미 생성된 Event를 활용한 맥락 정보 (더 정확)
            context_info = _collect_context_info_with_events(
                turns,
                turn.turn_index,
                existing_events
            )
        else:
            # 기본 맥락 정보
            context_info = _collect_context_info(
                turns,
                turn.turn_index
            )

    # LLM으로 타입 분류 및 요약 생성 (맥락 정보 포함)
    llm_result = classify_and_summarize_with_llm(turn, context_info=context_info)
    event_type = llm_result["event_type"]
    summary = llm_result["summary"]

    # 맥락 기반 타입 분류 개선
    # 코드 블록 + plan 맥락 → code_generation
    # 코드 블록 + debug 맥락 → debug (이미 처리됨)
    # 파일 경로만 + 읽기 키워드 → status_review
    if turn.code_blocks and context_info and context_info.get("is_plan_context"):
        # 코드 블록이 있고 이전 Turn에 plan이 있으면 code_generation
        if event_type not in [EventType.DEBUG, EventType.CODE_GENERATION]:
            event_type = EventType.CODE_GENERATION

    # Artifact 연결 (파일 경로가 있으면)
    # 액션 타입 결정: 코드 블록이 있으면 create, 그 외는 read 또는 mention
    artifacts = []
    if turn.path_candidates:
        for path in turn.path_candidates:
            # 코드 블록이 있으면 create, 그 외는 read
            action = ArtifactAction.CREATE.value if turn.code_blocks else ArtifactAction.READ.value
            artifacts.append({"path": path, "action": action})

    # Snippet 참조 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summary,
        artifacts=artifacts,
        snippet_refs=snippet_refs,
        processing_method="llm",
    )


def is_code_generation_turn(turn: Turn, context_info: Optional[Dict[str, Any]] = None) -> bool:
    """
    Code Generation Turn인지 판단 (키워드 + 맥락 기반)

    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)

    Returns:
        Code Generation Turn 여부
    """
    text_lower = turn.body.lower()

    # 코드 블록이 있어야 함
    if not turn.code_blocks:
        return False

    # 맥락 기반: 이전 Turn에 plan이 있으면 code_generation 가능성 높음
    if context_info and context_info.get("is_plan_context"):
        return True

    # 키워드 기반: 코드 생성 관련 키워드
    code_generation_keywords = [
        "스크립트 작성", "스크립트 생성", "스크립트를 만들",
        "코드 작성", "코드를 작성", "코드 생성",
        "파일 생성", "파일을 생성", "파일 작성",
        "새로운", "생성합니다", "작성합니다"
    ]

    return any(keyword in text_lower for keyword in code_generation_keywords)


def create_single_event_with_priority(
    turn: Turn, session_meta: Optional[SessionMeta] = None
) -> Event:
    """
    우선순위 기반 단일 이벤트 생성 (개선된 타입 체계)

    우선순위 (높은 순서):
    1. DEBUG: 에러/원인/해결 관련 (가장 구체적)
    2. CODE_GENERATION: 코드 생성 (코드 블록 존재)
    3. COMPLETION: 완료 키워드
    4. PLAN: 계획 수립
    5. STATUS_REVIEW: 상태 리뷰 (파일 읽기 등)
    6. NEXT_STEP: 다음 단계
    7. TURN: 기본

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체
    """
    # 1순위: DEBUG (디버그 트리거 + Cursor 발화)
    if is_debug_turn(turn):
        return create_debug_event(turn, session_meta)

    # 2순위: CODE_GENERATION (코드 블록 존재)
    if turn.code_blocks:
        return create_code_generation_event(turn, session_meta)

    # 3순위: 특수 타입 (엄격한 정규식)
    event_type = classify_event_type_strict(turn)
    if event_type != EventType.TURN:
        return create_message_event(turn, event_type, session_meta)

    # 4순위: 기본 TURN
    return create_message_event(turn, EventType.TURN, session_meta)


def is_debug_turn(turn: Turn) -> bool:
    """
    디버그 Turn인지 판단

    Args:
        turn: Turn 객체

    Returns:
        디버그 Turn 여부
    """
    if turn.speaker != "Cursor":
        return False

    text = turn.body.lower()
    return any(trigger.search(text) for trigger in DEBUG_TRIGGERS.values())


def create_debug_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    DebugEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체 (type=DEBUG)
    """
    # Artifact 연결 (파일 경로가 있으면, 수정 액션)
    artifacts = []
    if turn.path_candidates:
        # debug 타입은 주로 수정 작업이므로 modify 액션
        for path in turn.path_candidates:
            artifacts.append({"path": path, "action": ArtifactAction.MODIFY.value})

    # Snippet 참조 생성 (Phase 5에서 실제 ID로 대체될 예정)
    # 현재는 turn_index와 block_index를 조합하여 임시 ID 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.DEBUG,
        summary=summarize_turn(turn),
        artifacts=artifacts,
        snippet_refs=snippet_refs,
        processing_method="regex",
    )


def create_code_generation_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    Code Generation Event 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체 (type=CODE_GENERATION)
    """
    # Artifact 정보 구성 (파일 경로가 있으면)
    artifacts = []
    if turn.path_candidates:
        # 코드 블록이 있으면 create 액션
        for path in turn.path_candidates:
            artifacts.append({"path": path, "action": ArtifactAction.CREATE.value})

    # Snippet 참조 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.CODE_GENERATION,
        summary=summarize_turn(turn),
        artifacts=artifacts,
        snippet_refs=snippet_refs,
        processing_method="regex",
    )


def create_message_event(
    turn: Turn,
    event_type: Optional[EventType] = None,
    session_meta: Optional[SessionMeta] = None,
) -> Event:
    """
    MessageEvent 생성 (일반 Turn 이벤트)

    Args:
        turn: Turn 객체
        event_type: 이벤트 타입 (None이면 자동 분류)
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체
    """
    # 이벤트 타입 결정 (기본은 TURN, 특정 키워드로 분류 가능)
    if event_type is None:
        event_type = classify_event_type_strict(turn)

    # Artifact 연결 (파일 경로가 있으면, 읽기 액션)
    artifacts = []
    if turn.path_candidates:
        for path in turn.path_candidates:
            # status_review나 completion 타입이면 read, 그 외는 mention
            if event_type in [EventType.STATUS_REVIEW, EventType.COMPLETION]:
                artifacts.append({"path": path, "action": ArtifactAction.READ.value})
            else:
                artifacts.append({"path": path, "action": ArtifactAction.MENTION.value})

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summarize_turn(turn),
        artifacts=artifacts,
        snippet_refs=[],
        processing_method="regex",
    )


def classify_event_type_strict(turn: Turn) -> EventType:
    """
    엄격한 조건으로 이벤트 타입 분류 (정규식 기반)

    일반 단어 매칭을 피하기 위해 더 구체적인 패턴 사용

    Args:
        turn: Turn 객체

    Returns:
        EventType
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


def classify_event_type(turn: Turn) -> EventType:
    """
    Turn의 이벤트 타입 분류 (기존 함수, 호환성 유지)

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    # 엄격한 분류 함수 사용
    return classify_event_type_strict(turn)


def _collect_context_info(
    turns: List[Turn],
    current_turn_index: int,
    window_size: int = 5
) -> Dict[str, Any]:
    """
    현재 Turn의 맥락 정보 수집 (슬라이딩 윈도우)

    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        window_size: 맥락 윈도우 크기 (기본값: 5)

    Returns:
        맥락 정보 딕셔너리
    """
    context_info = {
        "recent_turn_count": 0,
        "recent_summaries": [],
        "is_debug_context": False,
        "is_plan_context": False,
    }

    # 이전 Turn들 수집 (최근 window_size개)
    start_idx = max(0, current_turn_index - window_size)
    recent_turns = turns[start_idx:current_turn_index]

    if not recent_turns:
        return context_info

    context_info["recent_turn_count"] = len(recent_turns)

    # 최근 Turn들의 요약 생성 (간단한 요약)
    for turn in recent_turns:
        summary = summarize_turn(turn)
        context_info["recent_summaries"].append(summary[:100])  # 최대 100자

    # 맥락 타입 판단 (최근 Turn들에서 debug/plan 패턴 확인)
    debug_count = 0
    plan_count = 0

    for turn in recent_turns:
        text_lower = turn.body.lower()

        # Debug 패턴 확인
        if any(trigger.search(text_lower) for trigger in DEBUG_TRIGGERS.values()):
            debug_count += 1

        # Plan 패턴 확인
        if re.search(r"(?i)\b(계획을|계획은|계획하|작업 계획|단계별 계획)\b", text_lower):
            plan_count += 1

    # 맥락 판단 (최근 Turn 중 절반 이상이 해당 타입이면 맥락으로 판단)
    threshold = len(recent_turns) / 2
    context_info["is_debug_context"] = debug_count >= threshold
    context_info["is_plan_context"] = plan_count >= threshold

    return context_info


def _collect_context_info_with_events(
    turns: List[Turn],
    current_turn_index: int,
    existing_events: Dict[int, Event],
    window_size: int = 5
) -> Dict[str, Any]:
    """
    이미 생성된 Event를 활용하여 맥락 정보 수집 (더 정확)

    Args:
        turns: 전체 Turn 리스트
        current_turn_index: 현재 Turn 인덱스
        existing_events: 이미 생성된 Event 딕셔너리 (turn_index -> Event)
        window_size: 맥락 윈도우 크기 (기본값: 5)

    Returns:
        맥락 정보 딕셔너리
    """
    context_info = {
        "recent_turn_count": 0,
        "recent_summaries": [],
        "is_debug_context": False,
        "is_plan_context": False,
    }

    # 이전 Turn들 수집 (최근 window_size개)
    start_idx = max(0, current_turn_index - window_size)
    recent_turns = turns[start_idx:current_turn_index]

    if not recent_turns:
        return context_info

    context_info["recent_turn_count"] = len(recent_turns)

    # 이미 생성된 Event의 summary 사용 (더 정확)
    for turn in recent_turns:
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            context_info["recent_summaries"].append(event.summary[:100])
        else:
            # Event가 없으면 간단한 요약 생성
            summary = summarize_turn(turn)
            context_info["recent_summaries"].append(summary[:100])

    # 맥락 타입 판단 (이미 생성된 Event의 타입 사용)
    debug_count = 0
    plan_count = 0

    for turn in recent_turns:
        if turn.turn_index in existing_events:
            event = existing_events[turn.turn_index]
            if event.type == EventType.DEBUG:
                debug_count += 1
            elif event.type == EventType.PLAN:
                plan_count += 1

    # 맥락 판단
    threshold = len(recent_turns) / 2
    context_info["is_debug_context"] = debug_count >= threshold
    context_info["is_plan_context"] = plan_count >= threshold

    return context_info


def summarize_turn(turn: Turn) -> str:
    """
    Turn을 요약 (정규식 기반 개선 버전)

    Args:
        turn: Turn 객체

    Returns:
        요약 텍스트
    """
    body = turn.body.strip()

    # 1. 줄바꿈 정리 (연속된 \n을 최대 2개로 제한)
    body = re.sub(r"\n{3,}", "\n\n", body)

    # 2. 200자 이하면 그대로 반환
    if len(body) <= 200:
        return body

    # 3. 의미 있는 위치에서 자르기 (우선순위 순)

    # 옵션 A: 마지막 완전한 문장까지만 (마침표/물음표/느낌표 기준)
    # 250자까지 확인하여 여유있게 검색
    sentences = re.split(r"([.!?。！？]\s+)", body[:250])
    if len(sentences) > 1:
        # 마지막 불완전 문장 제외
        summary = "".join(sentences[:-2])
        if 100 <= len(summary) <= 200:
            return summary.rstrip() + "..."

    # 옵션 B: 마지막 줄바꿈 기준 (문단 단위)
    last_newline = body[:200].rfind("\n\n")
    if last_newline > 100:  # 너무 앞에서 자르지 않도록
        return body[:last_newline].rstrip() + "..."

    # 옵션 C: 마지막 공백 기준 (단어 중간 자르기 방지)
    last_space = body[:200].rfind(" ")
    if last_space > 150:
        return body[:last_space] + "..."

    # 최후: 200자 자르기
    return body[:200] + "..."
