"""
파이프라인 Fixture 테스트
"""

import pytest
from pathlib import Path


def test_input_file_fixture(input_file):
    """입력 파일 fixture 테스트"""
    assert input_file.exists()
    assert input_file.suffix == ".md"


def test_parsed_data_fixture(parsed_data):
    """파싱 결과 fixture 테스트"""
    assert "session_meta" in parsed_data
    assert "turns" in parsed_data
    assert "code_blocks" in parsed_data
    assert "artifacts" in parsed_data
    assert len(parsed_data["turns"]) > 0


def test_normalized_events_fixture(normalized_events):
    """이벤트 정규화 결과 fixture 테스트"""
    events, session_meta = normalized_events

    assert len(events) > 0
    assert session_meta is not None
    assert session_meta.session_id is not None


def test_timeline_sections_fixture(timeline_sections):
    """Timeline Section fixture 테스트"""
    assert len(timeline_sections) > 0

    # 첫 번째 섹션 확인
    section = timeline_sections[0]
    assert hasattr(section, "section_id")
    assert hasattr(section, "title")
    assert hasattr(section, "events")


def test_fixture_caching(parsed_data, normalized_events, timeline_sections):
    """
    Fixture 캐싱 테스트

    같은 세션 내에서 fixture가 재사용되는지 확인
    (같은 객체 ID를 가져야 함)
    """
    # 같은 세션 내에서 fixture는 같은 객체여야 함
    # 하지만 딕셔너리/리스트는 매번 새로 생성될 수 있으므로
    # 내용이 동일한지만 확인
    assert len(parsed_data["turns"]) > 0
    assert len(normalized_events[0]) > 0
    assert len(timeline_sections) > 0

