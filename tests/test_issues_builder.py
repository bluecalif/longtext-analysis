"""
Issue Cards 빌더 단위 테스트

실제 데이터를 사용하여 Issue Cards 빌더 모듈을 테스트합니다.
"""

import pytest
from pathlib import Path
from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.issues_builder import (
    build_issue_cards,
    find_symptom_seeds,
)
from backend.core.models import IssueCard, EventType
from backend.core.constants import IssueStatus


# 실제 입력 데이터 경로
FIXTURE_DIR = Path(__file__).parent / "fixtures"
INPUT_FILE = FIXTURE_DIR / "cursor_phase_6_3.md"


def test_issue_detection():
    """이슈 탐지 테스트 (실제 데이터 사용)"""
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

    # Issue Cards 생성
    issue_cards = build_issue_cards(
        parse_result["turns"], events, session_meta
    )

    # 검증
    # Issue Cards가 생성되었는지 확인 (없을 수도 있음)
    assert isinstance(issue_cards, list), "Issue Cards가 리스트가 아님"

    # 생성된 카드가 모두 IssueCard 객체인지 확인
    for card in issue_cards:
        assert isinstance(card, IssueCard), "IssueCard 객체가 아님"
        assert hasattr(card, "issue_id"), "issue_id가 없음"
        assert hasattr(card, "title"), "title이 없음"
        assert hasattr(card, "symptoms"), "symptoms가 없음"


def test_issue_grouping():
    """이슈 그룹화 테스트 (실제 데이터 사용)"""
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

    # Issue Cards 생성
    issue_cards = build_issue_cards(
        parse_result["turns"], events, session_meta
    )

    # 검증
    if len(issue_cards) > 0:
        # 각 카드가 고유한 issue_id를 가지고 있는지 확인
        issue_ids = [card.issue_id for card in issue_cards]
        unique_ids = set(issue_ids)
        assert len(issue_ids) == len(unique_ids), "중복된 issue_id가 있음"

        # 각 카드가 scope를 가지고 있는지 확인
        for card in issue_cards:
            assert hasattr(card, "scope"), "scope가 없음"
            assert "session_id" in card.scope, "scope에 session_id가 없음"


def test_symptom_extraction():
    """Symptom 추출 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    # 파싱 실행
    text = INPUT_FILE.read_text(encoding="utf-8")
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # Symptom seed 탐지
    seeds = find_symptom_seeds(parse_result["turns"])

    # 검증
    # Symptom seed가 탐지되었는지 확인 (없을 수도 있음)
    assert isinstance(seeds, list), "Symptom seeds가 리스트가 아님"

    # 각 seed가 User Turn인지 확인
    for seed_idx, seed_turn in seeds:
        assert seed_turn.speaker == "User", f"Symptom seed가 User Turn이 아님: {seed_idx}"


def test_root_cause_extraction():
    """Root cause 추출 테스트 (실제 데이터 사용)"""
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

    # Issue Cards 생성
    issue_cards = build_issue_cards(
        parse_result["turns"], events, session_meta
    )

    # 검증
    if len(issue_cards) > 0:
        # Root cause가 있는 카드 확인
        cards_with_root_cause = [card for card in issue_cards if card.root_cause]

        if cards_with_root_cause:
            for card in cards_with_root_cause:
                assert card.root_cause is not None, "root_cause가 None임"
                assert isinstance(card.root_cause, dict), "root_cause가 dict가 아님"
                assert "status" in card.root_cause, "root_cause에 status가 없음"
                assert "text" in card.root_cause, "root_cause에 text가 없음"
                # status가 유효한 값인지 확인
                assert card.root_cause["status"] in [
                    IssueStatus.CONFIRMED.value,
                    IssueStatus.HYPOTHESIS.value,
                ], f"유효하지 않은 root_cause status: {card.root_cause['status']}"


def test_fix_extraction():
    """Fix 추출 테스트 (실제 데이터 사용)"""
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

    # Issue Cards 생성
    issue_cards = build_issue_cards(
        parse_result["turns"], events, session_meta
    )

    # 검증
    if len(issue_cards) > 0:
        # Fix가 있는 카드 확인
        for card in issue_cards:
            assert isinstance(card.fix, list), "fix가 list가 아님"
            # Fix 항목 구조 확인
            for fix_item in card.fix:
                assert isinstance(fix_item, dict), "fix 항목이 dict가 아님"
                assert "summary" in fix_item, "fix 항목에 summary가 없음"
                assert "snippet_refs" in fix_item, "fix 항목에 snippet_refs가 없음"


def test_validation_extraction():
    """Validation 추출 테스트 (실제 데이터 사용)"""
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

    # Issue Cards 생성
    issue_cards = build_issue_cards(
        parse_result["turns"], events, session_meta
    )

    # 검증
    if len(issue_cards) > 0:
        # Validation이 있는 카드 확인
        for card in issue_cards:
            assert isinstance(card.validation, list), "validation이 list가 아님"
            # Validation 항목이 문자열인지 확인
            for validation_item in card.validation:
                assert isinstance(validation_item, str), "validation 항목이 문자열이 아님"


def test_issue_card_completeness():
    """Issue Card 완전성 테스트 (실제 데이터 사용)"""
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

    # Issue Cards 생성
    issue_cards = build_issue_cards(
        parse_result["turns"], events, session_meta
    )

    # 검증
    if len(issue_cards) > 0:
        for card in issue_cards:
            # 필수 필드 확인
            assert card.issue_id, "issue_id가 비어있음"
            assert card.title, "title이 비어있음"
            assert card.scope, "scope가 비어있음"
            # Root cause 또는 Fix 중 하나는 있어야 함 (카드 생성 조건)
            assert card.root_cause is not None or len(card.fix) > 0, "root_cause와 fix가 모두 없음 (카드 생성 조건 위반)"

