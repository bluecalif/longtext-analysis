"""
Timeline 빌더 단위 테스트

실제 데이터를 사용하여 Timeline 빌더 모듈을 테스트합니다.
"""

import pytest
from pathlib import Path
from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.timeline_builder import build_timeline, build_structured_timeline
from backend.core.models import TimelineEvent, TimelineSection, EventType


# 실제 입력 데이터 경로
FIXTURE_DIR = Path(__file__).parent / "fixtures"
INPUT_FILE = FIXTURE_DIR / "cursor_phase_6_3.md"


def test_timeline_sequence():
    """시퀀스 번호 부여 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 이벤트 정규화
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )

    # Timeline 생성
    timeline = build_timeline(events, session_meta)

    # 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"
    assert len(timeline) == len(events), f"Timeline 이벤트 수({len(timeline)})가 Event 수({len(events)})와 일치하지 않음"

    # 시퀀스 번호가 순차적으로 부여되었는지 확인
    for i, timeline_event in enumerate(timeline):
        assert isinstance(timeline_event, TimelineEvent), "TimelineEvent 객체가 아님"
        assert timeline_event.seq == i + 1, f"시퀀스 번호가 올바르지 않음: {timeline_event.seq} != {i + 1}"


def test_timeline_grouping():
    """Phase/Subphase 그룹화 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 이벤트 정규화
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )

    # Timeline 생성
    timeline = build_timeline(events, session_meta)

    # 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"

    # 모든 TimelineEvent가 session_id를 가지고 있는지 확인
    for timeline_event in timeline:
        assert timeline_event.session_id == session_meta.session_id, "session_id가 올바르지 않음"
        # phase, subphase는 Event 또는 SessionMeta에서 가져옴
        assert timeline_event.phase is not None or session_meta.phase is None, "phase가 예상과 다름"


def test_timeline_artifact_linking():
    """Artifact 연결 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 이벤트 정규화
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )

    # Timeline 생성
    timeline = build_timeline(events, session_meta)

    # 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"

    # Artifact가 있는 Event가 Timeline에서도 Artifact를 가지고 있는지 확인
    artifact_events = [e for e in events if e.artifacts]
    if artifact_events:
        for event in artifact_events:
            timeline_event = next(
                (te for te in timeline if te.seq == event.seq), None
            )
            if timeline_event:
                assert len(timeline_event.artifacts) > 0, f"TimelineEvent(seq={timeline_event.seq})에 artifact가 연결되지 않음"
                # Artifact 구조 확인
                for artifact in timeline_event.artifacts:
                    assert isinstance(artifact, dict), "Artifact가 dict가 아님"
                    assert "path" in artifact, "Artifact에 path가 없음"


def test_timeline_snippet_linking():
    """Snippet 참조 연결 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 이벤트 정규화
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )

    # Timeline 생성
    timeline = build_timeline(events, session_meta)

    # 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"

    # Snippet 참조가 있는 Event가 Timeline에서도 snippet_refs를 가지고 있는지 확인
    events_with_snippets = [e for e in events if e.snippet_refs]
    if events_with_snippets:
        for event in events_with_snippets:
            timeline_event = next(
                (te for te in timeline if te.seq == event.seq), None
            )
            if timeline_event:
                assert len(timeline_event.snippet_refs) > 0, f"TimelineEvent(seq={timeline_event.seq})에 snippet_refs가 연결되지 않음"
                # snippet_refs가 리스트인지 확인
                assert isinstance(timeline_event.snippet_refs, list), "snippet_refs가 list가 아님"


def test_timeline_event_type_preservation():
    """이벤트 타입 보존 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 이벤트 정규화
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )

    # Timeline 생성
    timeline = build_timeline(events, session_meta)

    # 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"

    # 모든 Event의 타입이 TimelineEvent에 보존되었는지 확인
    for event in events:
        timeline_event = next(
            (te for te in timeline if te.seq == event.seq), None
        )
        if timeline_event:
            assert timeline_event.type == event.type, f"이벤트 타입이 보존되지 않음: {timeline_event.type} != {event.type}"


def test_structured_timeline_pattern_based():
    """구조화된 Timeline 생성 테스트 (패턴 기반, 실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 이벤트 정규화
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )

    # Issue Cards 생성 (패턴 기반)
    from backend.builders.issues_builder import build_issue_cards
    issue_cards = build_issue_cards(parse_result["turns"], events, session_meta, use_llm=False)

    # 구조화된 Timeline 생성 (패턴 기반)
    structured_result = build_structured_timeline(
        events, session_meta, issue_cards=issue_cards, use_llm=False
    )

    # 검증
    assert "sections" in structured_result, "sections 키가 없음"
    assert "events" in structured_result, "events 키가 없음"

    sections = structured_result["sections"]
    timeline_events = structured_result["events"]

    # Sections 검증
    assert len(sections) > 0, "Sections가 생성되지 않음"
    for section in sections:
        assert isinstance(section, TimelineSection), "TimelineSection 객체가 아님"
        assert section.section_id, "section_id가 비어있음"
        assert section.title, "title이 비어있음"
        assert section.summary, "summary가 비어있음"
        assert len(section.events) > 0, "events가 비어있음"
        # event_seqs는 실제 Event seq와 일치해야 함
        for event_seq in section.events:
            assert any(e.seq == event_seq for e in events), f"event_seq {event_seq}가 실제 Event에 없음"

    # Events 검증 (하위 호환성)
    assert len(timeline_events) == len(events), "Timeline events 수가 일치하지 않음"

    # 모든 Event가 최소한 하나의 Section에 포함되어야 함
    all_section_event_seqs = set()
    for section in sections:
        all_section_event_seqs.update(section.events)

    # 대부분의 이벤트가 포함되어야 함 (DEBUG 타입은 Issue Card로 처리되므로 제외 가능)
    event_seqs = set(e.seq for e in events)
    debug_event_seqs = set(e.seq for e in events if e.type == EventType.DEBUG)
    non_debug_event_seqs = event_seqs - debug_event_seqs

    # DEBUG가 아닌 이벤트 중 대부분이 포함되어야 함
    covered_ratio = (
        len(all_section_event_seqs & non_debug_event_seqs) / len(non_debug_event_seqs)
        if non_debug_event_seqs
        else 1.0
    )
    assert covered_ratio > 0.8, f"Section에 포함된 이벤트 비율이 너무 낮음: {covered_ratio:.1%} (DEBUG 제외)"


def test_structured_timeline_llm_based():
    """구조화된 Timeline 생성 테스트 (LLM 기반, 실제 데이터 사용, 선택적)"""
    import os
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY not set, skipping LLM test")

    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 이벤트 정규화 (LLM 사용)
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=True
    )

    # Issue Cards 생성
    from backend.builders.issues_builder import build_issue_cards
    issue_cards = build_issue_cards(parse_result["turns"], events, session_meta)

    # 구조화된 Timeline 생성 (LLM 기반)
    structured_result = build_structured_timeline(
        events, session_meta, issue_cards=issue_cards, use_llm=True
    )

    # 검증 (패턴 기반 테스트와 동일)
    assert "sections" in structured_result, "sections 키가 없음"
    assert "events" in structured_result, "events 키가 없음"

    sections = structured_result["sections"]
    timeline_events = structured_result["events"]

    # Sections 검증
    assert len(sections) > 0, "Sections가 생성되지 않음"
    for section in sections:
        assert isinstance(section, TimelineSection), "TimelineSection 객체가 아님"
        assert section.section_id, "section_id가 비어있음"
        assert section.title, "title이 비어있음"
        assert section.summary, "summary가 비어있음"
        assert len(section.events) > 0, "events가 비어있음"

    # Events 검증 (하위 호환성)
    assert len(timeline_events) == len(events), "Timeline events 수가 일치하지 않음"

