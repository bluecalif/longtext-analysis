"""
파서 단위 테스트

실제 데이터를 사용하여 파서 모듈을 테스트합니다.
"""

import pytest
from pathlib import Path
from backend.parser import parse_markdown, normalize_text
from backend.parser.meta import extract_session_meta
from backend.parser.turns import split_to_turns, parse_turn, check_parse_health
from backend.parser.snippets import extract_code_blocks
from backend.parser.artifacts import extract_path_candidates


# 실제 입력 데이터 경로
FIXTURE_DIR = Path(__file__).parent / "fixtures"
INPUT_FILE = FIXTURE_DIR / "cursor_phase_6_3.md"


def test_normalize():
    """정규화 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 정규화 실행
    normalized = normalize_text(text)

    # 검증
    assert "\r\n" not in normalized, "줄바꿈이 통일되지 않음"
    assert "\r" not in normalized, "줄바꿈이 통일되지 않음"
    assert not normalized.startswith("\ufeff"), "BOM이 제거되지 않음"


def test_meta_extraction():
    """메타 추출 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 메타 추출 실행
    session_meta = extract_session_meta(text, str(INPUT_FILE))

    # 검증
    assert session_meta.session_id is not None, "session_id가 생성되지 않음"
    assert session_meta.source_doc == str(INPUT_FILE), "source_doc가 올바르지 않음"
    # phase, subphase, exported_at, cursor_version은 있을 수도 없을 수도 있음


def test_turn_parsing():
    """Turn 파싱 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")
    normalized = normalize_text(text)

    # Turn 분할 실행
    turn_blocks = split_to_turns(normalized)

    # 검증
    assert len(turn_blocks) > 0, "Turn 블록이 분할되지 않음"

    # Turn 파싱 실행
    turns = []
    for idx, block in enumerate(turn_blocks):
        turn = parse_turn(block, idx)
        turns.append(turn)

    # 검증
    assert len(turns) > 0, "Turn이 파싱되지 않음"

    # Parse Health Check
    health = check_parse_health(turns)
    assert (
        health["unknown_ratio"] < 0.2
    ), f"Unknown speaker 비율이 너무 높음: {health['unknown_ratio']:.1%}"


def test_snippet_extraction():
    """스니펫 추출 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 스니펫 추출 실행
    code_blocks = extract_code_blocks(text, turn_index=0)

    # 검증 (코드 블록이 있을 수도 없을 수도 있음)
    # 최소한 함수가 정상 동작하는지 확인
    assert isinstance(code_blocks, list), "코드 블록이 리스트가 아님"


def test_artifact_extraction():
    """Artifact 추출 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # Artifact 추출 실행
    path_candidates = extract_path_candidates(text)

    # 검증 (경로 후보가 있을 수도 없을 수도 있음)
    # 최소한 함수가 정상 동작하는지 확인
    assert isinstance(path_candidates, list), "경로 후보가 리스트가 아님"


def test_parse_markdown_full():
    """전체 파싱 파이프라인 테스트 (실제 데이터 사용)"""
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 전체 파싱 실행
    result = parse_markdown(text, str(INPUT_FILE))

    # 검증
    assert "session_meta" in result, "session_meta가 없음"
    assert "turns" in result, "turns가 없음"
    assert "code_blocks" in result, "code_blocks가 없음"
    assert "artifacts" in result, "artifacts가 없음"

    assert result["session_meta"].session_id is not None, "session_id가 없음"
    assert len(result["turns"]) > 0, "turns가 비어있음"

    # Parse Health Check
    health = check_parse_health(result["turns"])
    assert (
        health["unknown_ratio"] < 0.2
    ), f"Unknown speaker 비율이 너무 높음: {health['unknown_ratio']:.1%}"
