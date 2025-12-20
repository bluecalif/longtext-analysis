"""
이벤트 정규화 단위 테스트

실제 데이터를 사용하여 이벤트 정규화 모듈을 테스트합니다.
"""

import pytest
from pathlib import Path
from backend.parser import parse_markdown
from backend.builders.event_normalizer import (
    normalize_turns_to_events,
    is_debug_turn,
    create_debug_event,
    create_artifact_event,
    create_message_event,
    classify_event_type,
)
from backend.core.models import Turn, EventType


# 실제 입력 데이터 경로
FIXTURE_DIR = Path(__file__).parent / "fixtures"
INPUT_FILE = FIXTURE_DIR / "cursor_phase_6_3.md"


def test_turn_to_event_conversion():
    """Turn → Event 변환 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 이벤트 정규화
    session_meta = result["session_meta"]
    events = normalize_turns_to_events(result["turns"], session_meta=session_meta)

    # 검증
    assert len(events) > 0, "이벤트가 생성되지 않음"
    # 우선순위 기반 단일 이벤트 생성이므로 이벤트 수는 Turn 수와 같아야 함
    assert len(events) == len(result["turns"]), f"이벤트 수({len(events)})가 Turn 수({len(result['turns'])})와 일치하지 않음"

    # 모든 이벤트가 Event 객체인지 확인
    from backend.core.models import Event
    for event in events:
        assert isinstance(event, Event), "이벤트가 Event 객체가 아님"
        assert hasattr(event, "type"), "이벤트에 type 속성이 없음"
        assert hasattr(event, "turn_ref"), "이벤트에 turn_ref 속성이 없음"
        assert hasattr(event, "summary"), "이벤트에 summary 속성이 없음"


def test_event_type_classification():
    """이벤트 타입 분류 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 이벤트 정규화
    session_meta = result["session_meta"]
    events = normalize_turns_to_events(result["turns"], session_meta=session_meta)

    # 이벤트 타입 분포 확인
    event_types = [event.type for event in events]
    unique_types = set(event_types)

    # 최소한 TURN 타입은 있어야 함
    assert EventType.TURN in unique_types, "TURN 타입 이벤트가 없음"

    # 모든 이벤트 타입이 유효한 EventType인지 확인
    valid_types = {EventType.STATUS_REVIEW, EventType.PLAN, EventType.ARTIFACT,
                   EventType.DEBUG, EventType.COMPLETION, EventType.NEXT_STEP, EventType.TURN}
    for event_type in unique_types:
        assert event_type in valid_types, f"유효하지 않은 이벤트 타입: {event_type}"


def test_artifact_linking():
    """Artifact 연결 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # path_candidates가 있는 Turn 찾기
    turns_with_paths = [t for t in result["turns"] if t.path_candidates]

    if len(turns_with_paths) == 0:
        pytest.skip("path_candidates가 있는 Turn이 없음")

    # 이벤트 정규화
    events = normalize_turns_to_events(result["turns"])

    # ARTIFACT 타입 이벤트 확인
    artifact_events = [e for e in events if e.type == EventType.ARTIFACT]

    assert len(artifact_events) > 0, "ARTIFACT 타입 이벤트가 생성되지 않음"

    # Artifact 연결 확인
    for event in artifact_events:
        assert len(event.artifacts) > 0, "Artifact가 연결되지 않음"
        for artifact in event.artifacts:
            assert "path" in artifact, "Artifact에 path가 없음"
            assert "action" in artifact, "Artifact에 action이 없음"


def test_snippet_linking():
    """Snippet 참조 연결 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # code_blocks가 있는 Turn 찾기
    turns_with_code = [t for t in result["turns"] if t.code_blocks]

    if len(turns_with_code) == 0:
        pytest.skip("code_blocks가 있는 Turn이 없음")

    # 이벤트 정규화
    events = normalize_turns_to_events(result["turns"])

    # snippet_refs가 있는 이벤트 확인
    events_with_snippets = [e for e in events if e.snippet_refs]

    assert len(events_with_snippets) > 0, "snippet_refs가 있는 이벤트가 없음"

    # Snippet 참조 형식 확인
    for event in events_with_snippets:
        for snippet_ref in event.snippet_refs:
            assert isinstance(snippet_ref, str), "snippet_ref가 문자열이 아님"
            assert "turn_" in snippet_ref, "snippet_ref 형식이 올바르지 않음"


def test_debug_turn_detection():
    """디버그 Turn 탐지 테스트"""
    # 디버그 키워드가 있는 Turn 생성
    debug_turn = Turn(
        turn_index=0,
        speaker="Cursor",
        body="There was an error in the code. The root cause is...",
        code_blocks=[],
        path_candidates=[],
    )

    assert is_debug_turn(debug_turn), "디버그 Turn이 탐지되지 않음"

    # 일반 Turn 생성
    normal_turn = Turn(
        turn_index=1,
        speaker="User",
        body="Please create a new file.",
        code_blocks=[],
        path_candidates=[],
    )

    assert not is_debug_turn(normal_turn), "일반 Turn이 디버그로 잘못 탐지됨"


def test_event_creation_functions():
    """이벤트 생성 함수 테스트"""
    # 테스트용 Turn 생성
    turn = Turn(
        turn_index=0,
        speaker="Cursor",
        body="Test turn body",
        code_blocks=[],
        path_candidates=["test.py"],
    )

    # ArtifactEvent 생성 테스트 (session_meta 없이도 동작)
    artifact_event = create_artifact_event(turn)
    assert artifact_event.type == EventType.ARTIFACT, "ArtifactEvent 타입이 올바르지 않음"
    assert len(artifact_event.artifacts) > 0, "Artifact가 연결되지 않음"

    # MessageEvent 생성 테스트 (session_meta 없이도 동작)
    message_event = create_message_event(turn)
    assert message_event.type in EventType, "MessageEvent 타입이 유효하지 않음"
    assert message_event.turn_ref == turn.turn_index, "turn_ref가 올바르지 않음"

