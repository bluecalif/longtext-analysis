"""
이벤트 정규화 모듈

파싱된 Turn 데이터를 이벤트로 정규화합니다.
"""

import re
from typing import List, Optional
from backend.core.models import Turn, Event, EventType, SessionMeta
from backend.core.constants import DEBUG_TRIGGERS


def normalize_turns_to_events(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None, use_llm: bool = False
) -> List[Event]:
    """
    Turn 리스트를 Event 리스트로 변환 (우선순위 기반 단일 이벤트, LLM 옵션)

    Args:
        turns: 파싱된 Turn 리스트
        session_meta: 세션 메타데이터 (Phase/Subphase 연결용, 선택)
        use_llm: LLM 사용 여부 (기본값: False, True 시 일괄 적용)

    Returns:
        정규화된 Event 리스트
    """
    events = []

    for turn in turns:
        if use_llm:
            # LLM 기반 이벤트 생성
            event = create_event_with_llm(turn, session_meta)
        else:
            # 정규식 기반 이벤트 생성
            event = create_single_event_with_priority(turn, session_meta)
        events.append(event)

    # 시퀀스 번호 부여
    for i, event in enumerate(events):
        event.seq = i + 1

    return events


def create_event_with_llm(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    LLM 기반 이벤트 생성 (gpt-4.1-mini)

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체 (processing_method="llm")
    """
    from backend.core.llm_service import classify_and_summarize_with_llm

    # LLM으로 타입 분류 및 요약 생성
    llm_result = classify_and_summarize_with_llm(turn)
    event_type = llm_result["event_type"]
    summary = llm_result["summary"]

    # Artifact 연결 (파일 경로가 있으면)
    artifacts = []
    if turn.path_candidates:
        artifacts = [{"path": path, "action": "mention"} for path in turn.path_candidates]

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


def create_single_event_with_priority(
    turn: Turn, session_meta: Optional[SessionMeta] = None
) -> Event:
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

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        Event 객체
    """
    # 1순위: DEBUG (디버그 트리거 + Cursor 발화)
    if is_debug_turn(turn):
        return create_debug_event(turn, session_meta)

    # 2순위: ARTIFACT (파일 경로 존재)
    if turn.path_candidates:
        return create_artifact_event(turn, session_meta)

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
        DebugEvent 객체
    """
    # 스니펫 참조 생성 (Phase 5에서 실제 ID로 대체될 예정)
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
        artifacts=[],  # 후속 단계에서 연결
        snippet_refs=snippet_refs,
        processing_method="regex",
    )


def create_artifact_event(turn: Turn, session_meta: Optional[SessionMeta] = None) -> Event:
    """
    ArtifactEvent 생성

    Args:
        turn: Turn 객체
        session_meta: 세션 메타데이터 (선택)

    Returns:
        ArtifactEvent 객체
    """
    # Artifact 정보 구성
    artifacts = [
        {"path": path, "action": "mention"}  # Phase 3에서는 mention만, Phase 4에서 확장
        for path in turn.path_candidates
    ]

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=EventType.ARTIFACT,
        summary=summarize_turn(turn),
        artifacts=artifacts,
        snippet_refs=[],
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
        MessageEvent 객체
    """
    # 이벤트 타입 결정 (기본은 TURN, 특정 키워드로 분류 가능)
    if event_type is None:
        event_type = classify_event_type_strict(turn)

    return Event(
        seq=0,  # 임시, normalize_turns_to_events에서 부여
        session_id=session_meta.session_id if session_meta else "",
        turn_ref=turn.turn_index,
        phase=session_meta.phase if session_meta else None,
        subphase=session_meta.subphase if session_meta else None,
        type=event_type,
        summary=summarize_turn(turn),
        artifacts=[],
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
