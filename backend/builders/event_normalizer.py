"""
이벤트 정규화 모듈

파싱된 Turn 데이터를 이벤트로 정규화합니다.
"""

import re
from typing import List
from backend.core.models import Turn, Event, EventType
from backend.core.constants import DEBUG_TRIGGERS


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

        # 3. 일반 MessageEvent (모든 Turn에 대해 생성)
        events.append(create_message_event(turn))

    return events


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


def create_debug_event(turn: Turn) -> Event:
    """
    DebugEvent 생성

    Args:
        turn: Turn 객체

    Returns:
        DebugEvent 객체
    """
    # 스니펫 참조 생성 (Phase 5에서 실제 ID로 대체될 예정)
    # 현재는 turn_index와 block_index를 조합하여 임시 ID 생성
    snippet_refs = [
        f"turn_{turn.turn_index}_block_{block.block_index}" for block in turn.code_blocks
    ]

    return Event(
        type=EventType.DEBUG,
        turn_ref=turn.turn_index,
        summary=summarize_turn(turn),
        artifacts=[],  # 후속 단계에서 연결
        snippet_refs=snippet_refs,
    )


def create_artifact_event(turn: Turn) -> Event:
    """
    ArtifactEvent 생성

    Args:
        turn: Turn 객체

    Returns:
        ArtifactEvent 객체
    """
    # Artifact 정보 구성
    artifacts = [
        {"path": path, "action": "mention"}  # Phase 3에서는 mention만, Phase 4에서 확장
        for path in turn.path_candidates
    ]

    return Event(
        type=EventType.ARTIFACT,
        turn_ref=turn.turn_index,
        summary=summarize_turn(turn),
        artifacts=artifacts,
        snippet_refs=[],
    )


def create_message_event(turn: Turn) -> Event:
    """
    MessageEvent 생성 (일반 Turn 이벤트)

    Args:
        turn: Turn 객체

    Returns:
        MessageEvent 객체
    """
    # 이벤트 타입 결정 (기본은 TURN, 특정 키워드로 분류 가능)
    event_type = classify_event_type(turn)

    return Event(
        type=event_type,
        turn_ref=turn.turn_index,
        summary=summarize_turn(turn),
        artifacts=[],
        snippet_refs=[],
    )


def classify_event_type(turn: Turn) -> EventType:
    """
    Turn의 이벤트 타입 분류

    Args:
        turn: Turn 객체

    Returns:
        EventType
    """
    text = turn.body.lower()

    # status_review: 상태 리뷰 관련 키워드
    if re.search(r"(?i)\b(status|현황|상태|리뷰|review)\b", text):
        return EventType.STATUS_REVIEW

    # plan: 계획 수립 관련 키워드
    if re.search(r"(?i)\b(plan|계획|단계|phase|subphase)\b", text):
        return EventType.PLAN

    # completion: 완료 관련 키워드
    if re.search(r"(?i)\b(완료|complete|done|finish|성공)\b", text):
        return EventType.COMPLETION

    # next_step: 다음 단계 관련 키워드
    if re.search(r"(?i)\b(next|다음|step|단계|진행)\b", text):
        return EventType.NEXT_STEP

    # 기본값: TURN
    return EventType.TURN


def summarize_turn(turn: Turn) -> str:
    """
    Turn을 요약 (간단한 버전, LLM 옵션은 Phase 3 후반에 추가)

    Args:
        turn: Turn 객체

    Returns:
        요약 텍스트
    """
    # 간단한 요약: 본문의 첫 200자 또는 전체 (200자 미만인 경우)
    body = turn.body.strip()
    if len(body) <= 200:
        return body

    # 첫 200자 + "..."
    return body[:200] + "..."
