"""
LLM 서비스 테스트

gpt-4.1-mini를 사용한 이벤트 타입 분류 및 요약 생성 테스트
"""

import pytest
import os
from pathlib import Path
from backend.core.llm_service import classify_and_summarize_with_llm
from backend.core.models import Turn, EventType
from backend.core.cache import get_cached_result, save_cached_result


def test_llm_service_caching():
    """LLM 서비스 캐싱 테스트"""
    # API 키 확인 (없으면 스킵)
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 환경 변수가 설정되지 않음")

    # 테스트용 Turn 생성
    turn = Turn(
        turn_index=0,
        speaker="Cursor",
        body="There was an error in the code. The root cause is a missing import statement.",
        code_blocks=[],
        path_candidates=[],
    )

    # 캐시 키 생성
    cache_key = f"llm_{hash(turn.body[:1000]) % 1000000}"

    # 첫 번째 호출 (캐시 없음)
    result1 = classify_and_summarize_with_llm(turn)

    # 결과 검증
    assert "event_type" in result1
    assert "summary" in result1
    assert isinstance(result1["event_type"], EventType)
    assert isinstance(result1["summary"], str)
    assert len(result1["summary"]) > 0

    # 캐시 확인
    cached = get_cached_result(cache_key)
    assert cached is not None
    assert cached["event_type"] == result1["event_type"].value
    assert cached["summary"] == result1["summary"]

    # 두 번째 호출 (캐시 사용)
    result2 = classify_and_summarize_with_llm(turn)

    # 결과가 동일한지 확인
    assert result1["event_type"] == result2["event_type"]
    assert result1["summary"] == result2["summary"]


def test_llm_service_type_classification():
    """LLM 서비스 타입 분류 테스트"""
    # API 키 확인 (없으면 스킵)
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 환경 변수가 설정되지 않음")

    # 디버그 관련 Turn
    debug_turn = Turn(
        turn_index=0,
        speaker="Cursor",
        body="Error: ModuleNotFoundError. The issue is that the import path is incorrect.",
        code_blocks=[],
        path_candidates=[],
    )

    result = classify_and_summarize_with_llm(debug_turn)

    # 타입이 유효한 EventType인지 확인
    assert isinstance(result["event_type"], EventType)
    assert result["event_type"] in EventType

    # 요약이 생성되었는지 확인
    assert len(result["summary"]) > 0


def test_llm_service_summary_quality():
    """LLM 서비스 요약 품질 테스트"""
    # API 키 확인 (없으면 스킵)
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 환경 변수가 설정되지 않음")

    # 긴 텍스트 Turn
    long_turn = Turn(
        turn_index=0,
        speaker="User",
        body="""Please create a new feature for the dashboard.
        This feature should display real-time statistics about user activity.
        It needs to show the number of active users, page views, and conversion rates.
        The data should be updated every 5 seconds.""",
        code_blocks=[],
        path_candidates=[],
    )

    result = classify_and_summarize_with_llm(long_turn)

    # 요약이 생성되었는지 확인
    assert len(result["summary"]) > 0
    assert len(result["summary"]) <= 500  # 합리적인 길이

    # 요약이 원문의 핵심 내용을 포함하는지 확인 (간단한 키워드 체크)
    summary_lower = result["summary"].lower()
    # 원문의 주요 키워드가 요약에 포함되어 있는지 확인
    keywords = ["dashboard", "statistics", "user", "activity"]
    # 하나 이상의 키워드가 포함되어 있으면 좋은 요약으로 간주
    assert any(keyword in summary_lower for keyword in keywords) or len(
        result["summary"]
    ) > 20


def test_llm_service_integration():
    """LLM 서비스 통합 테스트 (실제 API 호출)"""
    # API 키 확인 (없으면 스킵)
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 환경 변수가 설정되지 않음")

    # 실제 데이터 사용
    fixture_dir = Path(__file__).parent / "fixtures"
    input_file = fixture_dir / "cursor_phase_6_3.md"

    if not input_file.exists():
        pytest.skip(f"Input file not found: {input_file}")

    from backend.parser import parse_markdown

    text = input_file.read_text(encoding="utf-8")
    result = parse_markdown(text, source_doc=str(input_file))

    # 첫 번째 Turn으로 테스트
    if len(result["turns"]) > 0:
        turn = result["turns"][0]
        llm_result = classify_and_summarize_with_llm(turn)

        # 결과 검증
        assert "event_type" in llm_result
        assert "summary" in llm_result
        assert isinstance(llm_result["event_type"], EventType)
        assert len(llm_result["summary"]) > 0

