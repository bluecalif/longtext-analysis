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

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.timeline_builder import build_timeline, build_structured_timeline
from backend.builders.issues_builder import build_issue_cards
from backend.core.models import EventType, TimelineEvent, TimelineSection, IssueCard


# 실제 입력 데이터 경로
INPUT_FILE = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
REPORT_DIR = Path(__file__).parent / "reports"
RESULTS_DIR = Path(__file__).parent / "results"


def test_timeline_issues_e2e():
    """
    실제 입력 데이터로 전체 Timeline 및 Issue Cards 생성 파이프라인 테스트
    """
    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 2. 파싱 실행 (Phase 2 결과)
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 3. 이벤트 정규화 실행 (Phase 3 결과)
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )

    # 4. Timeline 생성 (Phase 4)
    timeline = build_timeline(events, session_meta)

    # 5. Issue Cards 생성 (Phase 4)
    issue_cards = build_issue_cards(
        parse_result["turns"], events, session_meta
    )

    # 6. 정합성 검증
    # Timeline 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"
    assert len(timeline) == len(events), f"Timeline 이벤트 수({len(timeline)})가 Event 수({len(events)})와 일치하지 않음"

    # Timeline 시퀀스 번호 부여 정확성
    for i, timeline_event in enumerate(timeline):
        assert isinstance(timeline_event, TimelineEvent), "TimelineEvent 객체가 아님"
        assert timeline_event.seq == i + 1, f"시퀀스 번호가 올바르지 않음: {timeline_event.seq} != {i + 1}"
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
            assert card.root_cause is not None or len(card.fix) > 0, "root_cause와 fix가 모두 없음 (카드 생성 조건 위반)"

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
            "total_turns": len(parse_result["turns"]),
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
            "issue_cards_with_validation": len([card for card in issue_cards if len(card.validation) > 0]),
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
        "session_meta": parse_result["session_meta"].model_dump(),
        "turns_count": len(parse_result["turns"]),
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


def test_timeline_issues_e2e_with_llm():
    """
    실제 입력 데이터로 전체 Timeline 및 Issue Cards 생성 파이프라인 테스트 (LLM 기반)
    Phase 3.4 타입 체계 개선 후 전체 파이프라인 검증
    """
    import os
    import time

    # API 키 확인 (없으면 스킵)
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 환경 변수가 설정되지 않음")

    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 2. 파싱 실행 (Phase 2 결과)
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 3. 이벤트 정규화 실행 (Phase 3 결과, LLM 기반, 새로운 타입 체계)
    from backend.core.llm_service import reset_cache_stats, get_cache_stats

    # 캐시 통계 초기화
    reset_cache_stats()

    session_meta = parse_result["session_meta"]
    start_time = time.time()
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=True
    )
    elapsed_time = time.time() - start_time

    # 실행 중 캐시 통계 수집
    runtime_cache_stats = get_cache_stats()

    # 4. Issue Cards 생성 (Phase 4.6, LLM 기반)
    issue_cards = build_issue_cards(
        parse_result["turns"], events, session_meta, use_llm=True
    )

    # 5. 구조화된 Timeline 생성 (Phase 4.5, LLM 기반)
    structured_result = build_structured_timeline(
        events, session_meta, issue_cards=issue_cards, use_llm=True
    )
    timeline_sections = structured_result["sections"]
    timeline = structured_result["events"]  # 하위 호환성을 위한 원본 이벤트 리스트

    # 6. 정합성 검증
    # Timeline 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"
    assert len(timeline) == len(events), f"Timeline 이벤트 수({len(timeline)})가 Event 수({len(events)})와 일치하지 않음"

    # Timeline 시퀀스 번호 부여 정확성
    for i, timeline_event in enumerate(timeline):
        assert isinstance(timeline_event, TimelineEvent), "TimelineEvent 객체가 아님"
        assert timeline_event.seq == i + 1, f"시퀀스 번호가 올바르지 않음: {timeline_event.seq} != {i + 1}"
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
            assert card.root_cause is not None or len(card.fix) > 0, "root_cause와 fix가 모두 없음 (카드 생성 조건 위반)"

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

    # 이벤트 타입 분포 (새로운 타입 체계 확인)
    event_type_distribution = {
        event_type.value: sum(1 for e in events if e.type == event_type)
        for event_type in EventType
    }

    # 정량적 데이터 수집
    report = {
        "test_name": "timeline_issues_e2e_with_llm",
        "timestamp": timestamp,
        "input_file": str(INPUT_FILE),
        "processing_method": "llm",
        "results": {
            "total_turns": len(parse_result["turns"]),
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
            "issue_cards_with_validation": len([card for card in issue_cards if len(card.validation) > 0]),
            "issue_cards_with_artifacts": len(cards_with_artifacts),
            "issue_cards_with_snippets": len(cards_with_snippets),
            "timeline_sections_with_issues": len([s for s in timeline_sections if s.has_issues]),
            "timeline_sections_avg_events_per_section": (
                round(sum(len(s.events) for s in timeline_sections) / len(timeline_sections), 2)
                if timeline_sections else 0
            ),
            "elapsed_time_seconds": round(elapsed_time, 2),
            "average_time_per_turn": (
                round(elapsed_time / len(parse_result["turns"]), 2) if parse_result["turns"] else 0
            ),
            "cache_statistics": {
                "cache_hits": runtime_cache_stats.get("hits", 0),
                "cache_misses": runtime_cache_stats.get("misses", 0),
                "cache_saves": runtime_cache_stats.get("saves", 0),
                "cache_hit_rate": round(
                    runtime_cache_stats.get("hits", 0) / len(parse_result["turns"]) if parse_result["turns"] else 0.0,
                    4
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
        report["warnings"].append("code_generation 타입 이벤트가 0개입니다 (새로운 타입 체계 확인 필요)")
    if artifact_count > 0:
        report["warnings"].append(f"artifact 타입 이벤트가 {artifact_count}개 발견되었습니다 (제거되어야 함)")

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
        "session_meta": parse_result["session_meta"].model_dump(),
        "turns_count": len(parse_result["turns"]),
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
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[RESULTS] Detailed results saved to: {results_file}")

