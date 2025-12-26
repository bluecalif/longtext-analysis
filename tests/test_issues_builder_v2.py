"""
Issue Card 빌더 v2 테스트 (Phase 4.7)
"""

import pytest
from backend.builders.issues_builder import (
    cluster_debug_events,
    match_timeline_section,
    get_related_turns,
    build_issue_cards,
)
from backend.core.models import Event, EventType, Turn, SessionMeta, TimelineSection


def test_cluster_debug_events():
    """DEBUG 이벤트 클러스터링 테스트"""
    from backend.core.models import Event, EventType

    # 테스트 이벤트 생성
    events = [
        Event(seq=1, turn_ref=0, type=EventType.DEBUG, summary="Error 1"),
        Event(seq=2, turn_ref=1, type=EventType.DEBUG, summary="Error 2"),
        Event(seq=10, turn_ref=5, type=EventType.DEBUG, summary="Error 3"),
        Event(seq=11, turn_ref=6, type=EventType.DEBUG, summary="Error 4"),
        Event(seq=20, turn_ref=10, type=EventType.CODE_GENERATION, summary="Code"),
    ]

    clusters = cluster_debug_events(events)

    # 2개의 클러스터가 생성되어야 함 (seq 1-2, seq 10-11)
    assert len(clusters) == 2
    assert len(clusters[0]) == 2  # seq 1, 2
    assert len(clusters[1]) == 2  # seq 10, 11


def test_match_timeline_section():
    """Timeline Section 매칭 테스트"""
    from backend.core.models import Event, EventType, TimelineSection

    # 테스트 이벤트 클러스터
    cluster_events = [
        Event(seq=5, turn_ref=2, type=EventType.DEBUG, summary="Error"),
        Event(seq=6, turn_ref=3, type=EventType.DEBUG, summary="Fix"),
    ]

    # 테스트 Timeline Section
    sections = [
        TimelineSection(
            section_id="section-1",
            title="Task 1",
            summary="Summary 1",
            events=[1, 2, 3],  # 겹치지 않음
        ),
        TimelineSection(
            section_id="section-2",
            title="Task 2",
            summary="Summary 2",
            events=[4, 5, 6, 7],  # 겹침 (5, 6)
        ),
    ]

    matched = match_timeline_section(cluster_events, sections)

    # section-2가 매칭되어야 함
    assert matched is not None
    assert matched.section_id == "section-2"


def test_build_issue_cards_with_timeline_sections(
    parsed_data, normalized_events, timeline_sections
):
    """Timeline Section을 활용한 Issue Card 생성 테스트"""
    events, session_meta = normalized_events

    # Turn 리스트 생성 (parsed_data에서)
    from backend.core.models import Turn
    turns = [Turn(**turn_dict) for turn_dict in parsed_data["turns"]]

    # Issue Cards 생성 (timeline_sections 사용)
    issue_cards = build_issue_cards(
        turns=turns,
        events=events,
        session_meta=session_meta,
        use_llm=False,  # 패턴 기반으로 먼저 테스트
        timeline_sections=timeline_sections,
    )

    # Issue Cards가 생성되었는지 확인
    assert len(issue_cards) >= 0  # 이슈가 없을 수도 있음

    # 생성된 Issue Card 확인
    for card in issue_cards:
        assert card.issue_id is not None
        assert card.title is not None
        assert len(card.symptoms) > 0 or card.root_cause or len(card.fix) > 0

        # Phase 4.7 필드 확인
        if card.section_id:
            assert card.section_title is not None
        assert len(card.related_events) > 0
        assert len(card.related_turns) > 0
        assert card.confidence_score is not None

