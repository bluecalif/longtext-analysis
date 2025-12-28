"""
Timeline 및 Issue Cards E2E 테스트

실제 입력 데이터로 전체 Timeline 및 Issue Cards 생성 파이프라인을 테스트합니다.
"""

import pytest
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# .env 파일 자동 로드
load_dotenv()

from backend.core.pipeline_cache import (
    get_or_create_parsed_data,
    get_or_create_events,
    get_or_create_timeline_sections,
    get_or_create_issue_cards,
)
from backend.builders.timeline_builder import build_timeline
from backend.core.models import EventType, TimelineEvent, TimelineSection, IssueCard, Turn


# 실제 입력 데이터 경로
INPUT_FILE = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
REPORT_DIR = Path(__file__).parent / "reports"
RESULTS_DIR = Path(__file__).parent / "results"


def test_timeline_issues_e2e_pattern():
    """
    실제 입력 데이터로 전체 Timeline 및 Issue Cards 생성 파이프라인 테스트 (패턴 기반)

    ⚠️ 주의: 이 테스트는 의도적으로 패턴 기반(REGEX)을 사용합니다.
    LLM 기반 테스트는 test_timeline_issues_e2e_with_llm()을 사용하세요.
    """
    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 2. 파싱 실행 (Phase 2 결과, pipeline_cache 사용)
    parsed_data = get_or_create_parsed_data(input_file=INPUT_FILE)

    # 3. 이벤트 정규화 실행 (Phase 3 결과, pipeline_cache 사용)
    events, session_meta = get_or_create_events(
        parsed_data=parsed_data,
        input_file=INPUT_FILE,
        use_llm=False
    )

    # Turn 모델 변환
    turns = [Turn(**turn_dict) for turn_dict in parsed_data["turns"]]

    # 4. Timeline 생성 (Phase 4, 기존 방식 유지)
    timeline = build_timeline(events, session_meta)

    # 5. Timeline Sections 생성 (pipeline_cache 사용)
    timeline_sections = get_or_create_timeline_sections(
        events=events,
        session_meta=session_meta,
        input_file=INPUT_FILE,
        use_llm=False,
        issue_cards=None
    )

    # 6. Issue Cards 생성 (Phase 4, 패턴 기반, pipeline_cache 사용)
    issue_cards = get_or_create_issue_cards(
        turns=turns,
        events=events,
        session_meta=session_meta,
        input_file=INPUT_FILE,
        use_llm=False,
        timeline_sections=timeline_sections
    )

    # 6. 정합성 검증
    # Timeline 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"
    assert len(timeline) == len(
        events
    ), f"Timeline 이벤트 수({len(timeline)})가 Event 수({len(events)})와 일치하지 않음"

    # Timeline 시퀀스 번호 부여 정확성
    for i, timeline_event in enumerate(timeline):
        assert isinstance(timeline_event, TimelineEvent), "TimelineEvent 객체가 아님"
        assert (
            timeline_event.seq == i + 1
        ), f"시퀀스 번호가 올바르지 않음: {timeline_event.seq} != {i + 1}"
        assert timeline_event.session_id == session_meta.session_id, "session_id가 올바르지 않음"

    # Timeline Phase/Subphase 그룹화 정확성
    timeline_with_phase = [te for te in timeline if te.phase is not None]
    timeline_with_subphase = [te for te in timeline if te.subphase is not None]
    # Phase/Subphase가 있는 이벤트가 있는지 확인 (없을 수도 있음)

    # Timeline Artifact/Snippet 연결 정확성
    timeline_with_artifacts = [te for te in timeline if te.artifacts]
    timeline_with_snippets = [te for te in timeline if te.snippet_refs]
    # Artifact/Snippet가 있는 이벤트가 있는지 확인 (없을 수도 있음)

    # Issue Cards 검증
    assert isinstance(issue_cards, list), "Issue Cards가 리스트가 아님"
    # Issue Cards가 없을 수도 있음 (symptom seed가 없거나 root_cause/fix가 없는 경우)

    if len(issue_cards) > 0:
        # Issue Cards 탐지 정확성
        for card in issue_cards:
            assert isinstance(card, IssueCard), "IssueCard 객체가 아님"
            assert card.issue_id, "issue_id가 비어있음"
            assert card.title, "title이 비어있음"
            assert card.scope, "scope가 비어있음"
            assert "session_id" in card.scope, "scope에 session_id가 없음"
            # Root cause 또는 Fix 중 하나는 있어야 함 (카드 생성 조건)
            assert (
                card.root_cause is not None or len(card.fix) > 0
            ), "root_cause와 fix가 모두 없음 (카드 생성 조건 위반)"

        # Issue Cards 그룹화 정확성
        issue_ids = [card.issue_id for card in issue_cards]
        unique_ids = set(issue_ids)
        assert len(issue_ids) == len(unique_ids), "중복된 issue_id가 있음"

        # Issue Cards symptom/root_cause/fix/validation 추출 정확성
        for card in issue_cards:
            assert isinstance(card.symptoms, list), "symptoms가 list가 아님"
            assert len(card.symptoms) > 0, "symptoms가 비어있음"
            assert isinstance(card.fix, list), "fix가 list가 아님"
            assert isinstance(card.validation, list), "validation이 list가 아님"

        # Issue Cards Artifact/Snippet 연결 정확성
        cards_with_artifacts = [card for card in issue_cards if card.related_artifacts]
        cards_with_snippets = [card for card in issue_cards if card.snippet_refs]
        # Artifact/Snippet가 있는 카드가 있는지 확인 (없을 수도 있음)

    # 7. 타당성 검증
    # Timeline 요약의 적절성
    timeline_summaries = [te.summary for te in timeline]
    assert all(summary for summary in timeline_summaries), "Timeline 요약이 비어있는 이벤트가 있음"

    # Issue Cards 탐지의 적절성
    if len(issue_cards) > 0:
        # Issue Cards 내용의 완전성
        for card in issue_cards:
            # 최소한 symptom은 있어야 함
            assert len(card.symptoms) > 0, "symptoms가 비어있음"

    # 8. 결과 분석 및 자동 보고
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 정량적 데이터 수집
    report = {
        "test_name": "timeline_issues_e2e",
        "timestamp": timestamp,
        "input_file": str(INPUT_FILE),
        "results": {
            "total_turns": len(turns),
            "total_events": len(events),
            "total_timeline_sections": len(timeline_sections),
            "total_timeline_events": len(timeline),
            "total_issue_cards": len(issue_cards),
            "timeline_event_type_distribution": {
                event_type.value: sum(1 for te in timeline if te.type == event_type)
                for event_type in EventType
            },
            "timeline_with_phase": len(timeline_with_phase),
            "timeline_with_subphase": len(timeline_with_subphase),
            "timeline_with_artifacts": len(timeline_with_artifacts),
            "timeline_with_snippets": len(timeline_with_snippets),
            "issue_cards_with_root_cause": len([card for card in issue_cards if card.root_cause]),
            "issue_cards_with_fix": len([card for card in issue_cards if len(card.fix) > 0]),
            "issue_cards_with_validation": len(
                [card for card in issue_cards if len(card.validation) > 0]
            ),
            "issue_cards_with_artifacts": len(cards_with_artifacts) if len(issue_cards) > 0 else 0,
            "issue_cards_with_snippets": len(cards_with_snippets) if len(issue_cards) > 0 else 0,
        },
        "warnings": [],
        "errors": [],
    }

    # 문제 발견 시 경고 추가
    if len(timeline) != len(events):
        report["warnings"].append(
            f"Timeline 이벤트 수({len(timeline)})가 Event 수({len(events)})와 일치하지 않음"
        )

    if len(issue_cards) > 0:
        for card in issue_cards:
            if not card.root_cause and len(card.fix) == 0:
                report["warnings"].append(
                    f"Issue Card({card.issue_id})에 root_cause와 fix가 모두 없음"
                )

    # 리포트 출력
    print("\n" + "=" * 50)
    print("Timeline & Issue Cards E2E Test Report")
    print("=" * 50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 50)

    # 리포트 파일 저장
    REPORT_DIR.mkdir(exist_ok=True)
    report_file = REPORT_DIR / "timeline_issues_e2e_report.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n[REPORT] Test report saved to: {report_file}")

    # 실행 결과 저장 (상세 Timeline/Issue Cards 생성 결과)
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"timeline_issues_e2e_{timestamp}.json"

    detailed_results = {
        "session_meta": session_meta.model_dump(),
        "turns_count": len(turns),
        "events_count": len(events),
        "timeline": [te.model_dump() for te in timeline],
        "issue_cards": [card.model_dump() for card in issue_cards],
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "timeline_issues_e2e",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[RESULTS] Detailed results saved to: {results_file}")


def test_timeline_issues_e2e_with_llm(parsed_data, normalized_events, timeline_sections):
    """
    실제 입력 데이터로 전체 Timeline 및 Issue Cards 생성 파이프라인 테스트 (LLM 기반, Phase 4.7)
    Phase 4.7: Fixture 기반 파이프라인, Timeline Section → Issue Card 순서
    """
    import os
    import time
    import logging

    logger = logging.getLogger(__name__)

    # API 키 확인 (없으면 스킵)
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 환경 변수가 설정되지 않음")

    # 전체 시작 시간
    total_start = time.time()

    # 1. Fixture 데이터 로드
    logger.info("=" * 60)
    logger.info("[STEP 1] Fixture 데이터 로드 시작")
    fixture_load_start = time.time()

    events, session_meta = normalized_events
    logger.info(f"  - parsed_data turns 수: {len(parsed_data['turns'])}")
    logger.info(f"  - events 수: {len(events)}")
    logger.info(f"  - timeline_sections 수: {len(timeline_sections)}")

    # Turn 리스트 생성 (parsed_data에서)
    from backend.core.models import Turn

    turns = [Turn(**turn_dict) for turn_dict in parsed_data["turns"]]
    logger.info(f"  - turns 수: {len(turns)}")

    fixture_load_time = time.time() - fixture_load_start
    logger.info(f"[STEP 1] 완료 (소요 시간: {fixture_load_time:.2f}초)")

    # 2. DEBUG 이벤트 클러스터링
    logger.info("=" * 60)
    logger.info("[STEP 2] DEBUG 이벤트 클러스터링 시작")
    cluster_start = time.time()

    from backend.builders.issues_builder import cluster_debug_events

    debug_clusters = cluster_debug_events(events)
    logger.info(f"  - DEBUG 이벤트 클러스터 수: {len(debug_clusters)}")

    debug_events = [e for e in events if e.type == EventType.DEBUG]
    logger.info(f"  - 전체 DEBUG 이벤트 수: {len(debug_events)}")

    for i, cluster in enumerate(debug_clusters):
        cluster_seqs = [e.seq for e in cluster]
        logger.info(f"    클러스터 {i+1}: {len(cluster)}개 이벤트, seq={cluster_seqs}")

    cluster_time = time.time() - cluster_start
    logger.info(f"[STEP 2] 완료 (소요 시간: {cluster_time:.2f}초)")

    # 3. Timeline Section 매칭 검증 (클러스터별)
    logger.info("=" * 60)
    logger.info("[STEP 3] Timeline Section 매칭 검증 (클러스터별)")
    match_start = time.time()

    from backend.builders.issues_builder import match_timeline_section

    for i, cluster in enumerate(debug_clusters):
        matched_section = match_timeline_section(cluster, timeline_sections)
        if matched_section:
            cluster_seqs = {e.seq for e in cluster}
            section_event_seqs = set(matched_section.events)
            overlap = cluster_seqs & section_event_seqs
            logger.info(f"  클러스터 {i+1}: Section '{matched_section.section_id}' 매칭 성공")
            logger.info(f"    - 클러스터 events: {sorted(cluster_seqs)}")
            logger.info(f"    - Section events: {sorted(section_event_seqs)}")
            logger.info(f"    - 겹치는 events: {sorted(overlap)} ({len(overlap)}개)")
        else:
            cluster_seqs = [e.seq for e in cluster]
            logger.warning(f"  클러스터 {i+1}: Section 매칭 실패 (seq={cluster_seqs})")

    match_time = time.time() - match_start
    logger.info(f"[STEP 3] 완료 (소요 시간: {match_time:.2f}초)")

    # 4. Issue Cards 생성
    logger.info("=" * 60)
    logger.info("[STEP 4] Issue Cards 생성 시작")
    issue_start = time.time()

    # 캐시 통계 수집 (Issue Card 생성 전)
    from backend.core.llm_service import get_cache_stats

    cache_stats_before = get_cache_stats()
    logger.info(
        f"  - LLM 캐시 통계 (생성 전): hits={cache_stats_before.get('hits', 0)}, misses={cache_stats_before.get('misses', 0)}"
    )

    issue_cards = build_issue_cards(
        turns=turns,
        events=events,
        session_meta=session_meta,
        use_llm=True,
        timeline_sections=timeline_sections,  # Phase 4.7: Timeline Section 전달
    )

    cache_stats_after = get_cache_stats()
    logger.info(
        f"  - LLM 캐시 통계 (생성 후): hits={cache_stats_after.get('hits', 0)}, misses={cache_stats_after.get('misses', 0)}"
    )
    logger.info(f"  - 생성된 Issue Cards 수: {len(issue_cards)}")

    for i, card in enumerate(issue_cards):
        logger.info(f"    Issue Card {i+1}:")
        logger.info(f"      - issue_id: {card.issue_id}")
        logger.info(
            f"      - title: {card.title[:100]}..."
            if len(card.title) > 100
            else f"      - title: {card.title}"
        )
        logger.info(f"      - section_id: {card.section_id}")
        logger.info(
            f"      - section_title: {card.section_title[:100] if card.section_title else None}..."
        )
        logger.info(
            f"      - related_events: {len(card.related_events)}개 {card.related_events[:10]}"
        )
        logger.info(f"      - related_turns: {len(card.related_turns)}개")
        logger.info(f"      - confidence_score: {card.confidence_score}")
        logger.info(f"      - symptoms: {len(card.symptoms)}개")
        logger.info(f"      - root_cause: {'있음' if card.root_cause else '없음'}")
        logger.info(f"      - fix: {len(card.fix)}개")
        logger.info(f"      - validation: {len(card.validation)}개")

    issue_time = time.time() - issue_start
    logger.info(f"[STEP 4] 완료 (소요 시간: {issue_time:.2f}초)")

    # 5. Timeline Section 매칭 검증 (Issue Card별)
    logger.info("=" * 60)
    logger.info("[STEP 5] Timeline Section 매칭 검증 (Issue Card별)")
    validation_start = time.time()

    for card in issue_cards:
        if card.section_id:
            matched_section = next(
                (s for s in timeline_sections if s.section_id == card.section_id), None
            )
            if matched_section:
                overlap = set(card.related_events) & set(matched_section.events)
                logger.info(f"  ✓ Issue Card {card.issue_id} → Section {card.section_id} 매칭 성공")
                logger.info(f"    - Section events: {len(matched_section.events)}개")
                logger.info(f"    - Card related_events: {len(card.related_events)}개")
                logger.info(f"    - 겹치는 events: {len(overlap)}개 {sorted(overlap)[:10]}")
            else:
                logger.warning(
                    f"  ✗ Issue Card {card.issue_id} → Section {card.section_id} 매칭 실패 (Section 없음)"
                )
        else:
            logger.warning(f"  ✗ Issue Card {card.issue_id} → Section 매칭 없음 (section_id=None)")

    validation_time = time.time() - validation_start
    logger.info(f"[STEP 5] 완료 (소요 시간: {validation_time:.2f}초)")

    # 6. Timeline 생성 (하위 호환성)
    logger.info("=" * 60)
    logger.info("[STEP 6] Timeline 생성 시작")
    timeline_start = time.time()

    timeline = build_timeline(events, session_meta)
    logger.info(f"  - Timeline events 수: {len(timeline)}")

    timeline_time = time.time() - timeline_start
    logger.info(f"[STEP 6] 완료 (소요 시간: {timeline_time:.2f}초)")

    # 전체 소요 시간
    total_time = time.time() - total_start
    logger.info("=" * 60)
    logger.info(f"[TIMING] 전체 소요 시간: {total_time:.2f}초")
    logger.info(
        f"  - Fixture 로드: {fixture_load_time:.2f}초 ({fixture_load_time/total_time*100:.1f}%)"
    )
    logger.info(f"  - 클러스터링: {cluster_time:.2f}초 ({cluster_time/total_time*100:.1f}%)")
    logger.info(f"  - Section 매칭: {match_time:.2f}초 ({match_time/total_time*100:.1f}%)")
    logger.info(f"  - Issue Cards 생성: {issue_time:.2f}초 ({issue_time/total_time*100:.1f}%)")
    logger.info(f"  - 검증: {validation_time:.2f}초 ({validation_time/total_time*100:.1f}%)")
    logger.info(f"  - Timeline 생성: {timeline_time:.2f}초 ({timeline_time/total_time*100:.1f}%)")
    logger.info("=" * 60)

    # 7. 정합성 검증
    logger.info("[STEP 7] 정합성 검증 시작")
    assert_start = time.time()

    # Timeline 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"
    assert len(timeline) == len(
        events
    ), f"Timeline 이벤트 수({len(timeline)})가 Event 수({len(events)})와 일치하지 않음"

    # Timeline 시퀀스 번호 부여 정확성
    for i, timeline_event in enumerate(timeline):
        assert isinstance(timeline_event, TimelineEvent), "TimelineEvent 객체가 아님"
        assert (
            timeline_event.seq == i + 1
        ), f"시퀀스 번호가 올바르지 않음: {timeline_event.seq} != {i + 1}"
        assert timeline_event.session_id == session_meta.session_id, "session_id가 올바르지 않음"

    # Timeline Phase/Subphase 그룹화 정확성
    timeline_with_phase = [te for te in timeline if te.phase is not None]
    timeline_with_subphase = [te for te in timeline if te.subphase is not None]

    # Timeline Artifact/Snippet 연결 정확성
    timeline_with_artifacts = [te for te in timeline if te.artifacts]
    timeline_with_snippets = [te for te in timeline if te.snippet_refs]

    # Event 타입 분류 정확성 (새로운 타입 체계)
    event_types = [event.type for event in events]
    unique_types = set(event_types)
    valid_types = {
        EventType.STATUS_REVIEW,
        EventType.PLAN,
        EventType.CODE_GENERATION,  # 새로운 타입
        EventType.DEBUG,
        EventType.COMPLETION,
        EventType.NEXT_STEP,
        EventType.TURN,
    }
    for event_type in unique_types:
        assert event_type in valid_types, f"유효하지 않은 이벤트 타입: {event_type}"

    # Issue Cards 검증
    assert isinstance(issue_cards, list), "Issue Cards가 리스트가 아님"

    if len(issue_cards) > 0:
        # Issue Cards 탐지 정확성
        for card in issue_cards:
            assert isinstance(card, IssueCard), "IssueCard 객체가 아님"
            assert card.issue_id, "issue_id가 비어있음"
            assert card.title, "title이 비어있음"
            assert card.scope, "scope가 비어있음"
            assert "session_id" in card.scope, "scope에 session_id가 없음"
            # Root cause 또는 Fix 중 하나는 있어야 함 (카드 생성 조건)
            assert (
                card.root_cause is not None or len(card.fix) > 0
            ), "root_cause와 fix가 모두 없음 (카드 생성 조건 위반)"

            # Phase 4.7 필드 검증
            assert len(card.related_events) > 0, "related_events가 비어있음"
            assert len(card.related_turns) > 0, "related_turns가 비어있음"
            assert card.confidence_score is not None, "confidence_score가 None임"
            assert (
                0.0 <= card.confidence_score <= 1.0
            ), f"confidence_score가 범위를 벗어남: {card.confidence_score}"

            # Timeline Section 연결 검증 (연결된 경우)
            if card.section_id:
                assert card.section_title is not None, "section_id가 있는데 section_title이 None임"
                # 해당 Section이 실제로 존재하는지 확인
                matched_section = next(
                    (s for s in timeline_sections if s.section_id == card.section_id), None
                )
                assert (
                    matched_section is not None
                ), f"section_id({card.section_id})에 해당하는 Section이 없음"

        # Issue Cards 그룹화 정확성
        issue_ids = [card.issue_id for card in issue_cards]
        unique_ids = set(issue_ids)
        assert len(issue_ids) == len(unique_ids), "중복된 issue_id가 있음"

        # Issue Cards symptom/root_cause/fix/validation 추출 정확성
        for card in issue_cards:
            assert isinstance(card.symptoms, list), "symptoms가 list가 아님"
            assert len(card.symptoms) > 0, "symptoms가 비어있음"
            assert isinstance(card.fix, list), "fix가 list가 아님"
            assert isinstance(card.validation, list), "validation이 list가 아님"

        # Issue Cards Artifact/Snippet 연결 정확성
        cards_with_artifacts = [card for card in issue_cards if card.related_artifacts]
        cards_with_snippets = [card for card in issue_cards if card.snippet_refs]
    else:
        cards_with_artifacts = []
        cards_with_snippets = []

    assert_time = time.time() - assert_start
    logger.info(f"[STEP 7] 완료 (소요 시간: {assert_time:.2f}초)")

    # 8. 타당성 검증
    logger.info("=" * 60)
    logger.info("[STEP 8] 타당성 검증 시작")
    validity_start = time.time()

    # Timeline 요약의 적절성
    timeline_summaries = [te.summary for te in timeline]
    assert all(summary for summary in timeline_summaries), "Timeline 요약이 비어있는 이벤트가 있음"

    # Issue Cards 탐지의 적절성
    if len(issue_cards) > 0:
        # Issue Cards 내용의 완전성
        for card in issue_cards:
            # 최소한 symptom은 있어야 함
            assert len(card.symptoms) > 0, "symptoms가 비어있음"

    # 8. 결과 분석 및 자동 보고
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 이벤트 타입 분포 (새로운 타입 체계 확인)
    event_type_distribution = {
        event_type.value: sum(1 for e in events if e.type == event_type) for event_type in EventType
    }

    # 정량적 데이터 수집
    report = {
        "test_name": "timeline_issues_e2e_with_llm",
        "timestamp": timestamp,
        "input_file": str(INPUT_FILE),
        "processing_method": "llm",
        "results": {
            "total_turns": len(turns),
            "total_events": len(events),
            "total_timeline_sections": len(timeline_sections),
            "total_timeline_events": len(timeline),
            "total_issue_cards": len(issue_cards),
            "event_type_distribution": event_type_distribution,
            "timeline_event_type_distribution": {
                event_type.value: sum(1 for te in timeline if te.type == event_type)
                for event_type in EventType
            },
            "timeline_with_phase": len(timeline_with_phase),
            "timeline_with_subphase": len(timeline_with_subphase),
            "timeline_with_artifacts": len(timeline_with_artifacts),
            "timeline_with_snippets": len(timeline_with_snippets),
            "issue_cards_with_root_cause": len([card for card in issue_cards if card.root_cause]),
            "issue_cards_with_fix": len([card for card in issue_cards if len(card.fix) > 0]),
            "issue_cards_with_validation": len(
                [card for card in issue_cards if len(card.validation) > 0]
            ),
            "issue_cards_with_artifacts": len(cards_with_artifacts),
            "issue_cards_with_snippets": len(cards_with_snippets),
            "issue_cards_with_section": len(
                [card for card in issue_cards if card.section_id]
            ),  # Phase 4.7
            "timeline_sections_with_issues": len([s for s in timeline_sections if s.has_issues]),
            "timeline_sections_avg_events_per_section": (
                round(sum(len(s.events) for s in timeline_sections) / len(timeline_sections), 2)
                if timeline_sections
                else 0
            ),
            "timing": {
                "total_seconds": round(total_time, 2),
                "fixture_load_seconds": round(fixture_load_time, 2),
                "clustering_seconds": round(cluster_time, 2),
                "section_matching_seconds": round(match_time, 2),
                "issue_cards_creation_seconds": round(issue_time, 2),
                "validation_seconds": round(validation_time, 2),
                "timeline_creation_seconds": round(timeline_time, 2),
                "assertion_seconds": round(assert_time, 2),
            },
            "cache_statistics": {
                "cache_hits": cache_stats_after.get("hits", 0),
                "cache_misses": cache_stats_after.get("misses", 0),
                "cache_saves": cache_stats_after.get("saves", 0),
                "cache_hit_rate": round(
                    cache_stats_after.get("hits", 0) / len(turns) if turns else 0.0, 4
                ),
            },
        },
        "warnings": [],
        "errors": [],
    }

    # 새로운 타입 체계 확인 (code_generation 타입이 있는지, artifact 타입이 없는지)
    code_generation_count = event_type_distribution.get("code_generation", 0)
    artifact_count = event_type_distribution.get("artifact", 0)

    if code_generation_count == 0:
        report["warnings"].append(
            "code_generation 타입 이벤트가 0개입니다 (새로운 타입 체계 확인 필요)"
        )
    if artifact_count > 0:
        report["warnings"].append(
            f"artifact 타입 이벤트가 {artifact_count}개 발견되었습니다 (제거되어야 함)"
        )

    # 문제 발견 시 경고 추가
    if len(timeline) != len(events):
        report["warnings"].append(
            f"Timeline 이벤트 수({len(timeline)})가 Event 수({len(events)})와 일치하지 않음"
        )

    if len(issue_cards) > 0:
        for card in issue_cards:
            if not card.root_cause and len(card.fix) == 0:
                report["warnings"].append(
                    f"Issue Card({card.issue_id})에 root_cause와 fix가 모두 없음"
                )

    # 리포트 출력
    print("\n" + "=" * 50)
    print("Timeline & Issue Cards E2E Test Report (LLM)")
    print("=" * 50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 50)

    # 리포트 파일 저장
    REPORT_DIR.mkdir(exist_ok=True)
    report_file = REPORT_DIR / "timeline_issues_e2e_llm_report.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n[REPORT] LLM E2E test report saved to: {report_file}")

    # 실행 결과 저장 (상세 Timeline/Issue Cards 생성 결과)
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"timeline_issues_e2e_llm_{timestamp}.json"

    detailed_results = {
        "session_meta": session_meta.model_dump(),
        "turns_count": len(turns),
        "events_count": len(events),
        "events": [event.model_dump() for event in events],
        "timeline_sections": [section.model_dump() for section in timeline_sections],
        "timeline": [te.model_dump() for te in timeline],  # 하위 호환성
        "issue_cards": [card.model_dump() for card in issue_cards],
        "event_type_distribution": event_type_distribution,
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "timeline_issues_e2e_with_llm",
            "processing_method": "llm",
            "timeline_method": "structured_llm",
            "pipeline_version": "4.7",  # Phase 4.7 표시
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[RESULTS] Detailed results saved to: {results_file}")
