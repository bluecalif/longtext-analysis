"""
파이프라인 캐싱 모듈 테스트
"""

import pytest
from pathlib import Path
from backend.core.pipeline_cache import (
    get_or_create_parsed_data,
    get_or_create_events,
    get_or_create_timeline_sections,
    invalidate_cache,
    get_cache_stats,
    _generate_file_hash,
    _generate_cache_key,
)


def test_generate_file_hash():
    """파일 해시 생성 테스트"""
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        pytest.skip(f"Input file not found: {input_file}")

    hash1 = _generate_file_hash(input_file)
    hash2 = _generate_file_hash(input_file)

    # 같은 파일에 대해 같은 해시 생성
    assert hash1 == hash2
    assert len(hash1) == 16


def test_generate_cache_key():
    """캐시 키 생성 테스트"""
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        pytest.skip(f"Input file not found: {input_file}")

    key1 = _generate_cache_key(input_file, use_llm=False, cache_type="parsed")
    key2 = _generate_cache_key(input_file, use_llm=True, cache_type="parsed")
    key3 = _generate_cache_key(input_file, use_llm=False, cache_type="events")

    # 같은 파일, 같은 설정이면 같은 키
    assert key1 == _generate_cache_key(input_file, use_llm=False, cache_type="parsed")

    # 다른 설정이면 다른 키
    assert key1 != key2  # use_llm 다름
    assert key1 != key3  # cache_type 다름


def test_get_or_create_parsed_data():
    """파싱 결과 캐싱 테스트"""
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        pytest.skip(f"Input file not found: {input_file}")

    # 첫 번째 호출 (캐시 미스)
    result1 = get_or_create_parsed_data(input_file)

    assert "session_meta" in result1
    assert "turns" in result1
    assert "code_blocks" in result1
    assert "artifacts" in result1
    assert len(result1["turns"]) > 0

    # 두 번째 호출 (캐시 히트)
    result2 = get_or_create_parsed_data(input_file)

    # 결과가 동일해야 함
    assert result1["session_meta"]["session_id"] == result2["session_meta"]["session_id"]
    assert len(result1["turns"]) == len(result2["turns"])


def test_get_or_create_events():
    """이벤트 정규화 결과 캐싱 테스트"""
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        pytest.skip(f"Input file not found: {input_file}")

    # 파싱 결과 가져오기
    parsed_data = get_or_create_parsed_data(input_file)

    # 첫 번째 호출 (캐시 미스, 패턴 기반)
    events1, session_meta1 = get_or_create_events(parsed_data, input_file, use_llm=False)

    assert len(events1) > 0
    assert session_meta1 is not None

    # 두 번째 호출 (캐시 히트)
    events2, session_meta2 = get_or_create_events(parsed_data, input_file, use_llm=False)

    # 결과가 동일해야 함
    assert len(events1) == len(events2)
    assert session_meta1.session_id == session_meta2.session_id

    # LLM 기반도 테스트 (캐시 키가 다름)
    events3, session_meta3 = get_or_create_events(parsed_data, input_file, use_llm=True)

    # LLM 기반은 다른 캐시 키를 사용하므로 별도로 저장됨
    assert len(events3) > 0


def test_get_or_create_timeline_sections():
    """Timeline Section 결과 캐싱 테스트"""
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        pytest.skip(f"Input file not found: {input_file}")

    # 파싱 및 이벤트 정규화
    parsed_data = get_or_create_parsed_data(input_file)
    events, session_meta = get_or_create_events(parsed_data, input_file, use_llm=False)

    # 첫 번째 호출 (캐시 미스)
    sections1 = get_or_create_timeline_sections(
        events=events,
        session_meta=session_meta,
        input_file=input_file,
        use_llm=False,
        issue_cards=None
    )

    assert len(sections1) > 0

    # 두 번째 호출 (캐시 히트)
    sections2 = get_or_create_timeline_sections(
        events=events,
        session_meta=session_meta,
        input_file=input_file,
        use_llm=False,
        issue_cards=None
    )

    # 결과가 동일해야 함
    assert len(sections1) == len(sections2)


def test_cache_invalidation():
    """캐시 무효화 테스트"""
    input_file = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        pytest.skip(f"Input file not found: {input_file}")

    # 캐시 생성
    parsed_data = get_or_create_parsed_data(input_file)

    # 캐시 통계 확인
    stats_before = get_cache_stats()
    assert stats_before["parsed"] > 0

    # 특정 파일의 캐시만 무효화
    invalidated = invalidate_cache(input_file=input_file, cache_type="parsed")
    assert invalidated > 0

    # 캐시 통계 확인 (무효화 후)
    stats_after = get_cache_stats()
    assert stats_after["parsed"] < stats_before["parsed"]


def test_get_cache_stats():
    """캐시 통계 테스트"""
    stats = get_cache_stats()

    assert "total_files" in stats
    assert "parsed" in stats
    assert "events" in stats
    assert "timeline_sections" in stats
    assert "total_size_bytes" in stats

    assert stats["total_files"] >= 0
    assert stats["total_size_bytes"] >= 0

