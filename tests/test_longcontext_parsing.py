"""
longcontext 마크다운 파일 파싱 테스트

실제 마크다운 파일에 대한 파싱 정확도 및 품질 검증
"""

import pytest
import json
from pathlib import Path
from datetime import datetime
from backend.parser import parse_markdown
from backend.parser.turns import check_parse_health
from backend.core.models import SessionMeta, Turn


# 실제 입력 데이터 경로
INPUT_FILE_PHASE_2 = Path(__file__).parent.parent / "docs" / "longcontext_phase_2.md"
INPUT_FILE_PHASE_4_3 = Path(__file__).parent.parent / "docs" / "longcontext_phase_4_3.md"
REPORT_DIR = Path(__file__).parent / "reports"
RESULTS_DIR = Path(__file__).parent / "results"


def test_longcontext_parsing_phase_2():
    """
    longcontext_phase_2.md 파일 파싱 테스트
    """
    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE_PHASE_2.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE_PHASE_2}")

    text = INPUT_FILE_PHASE_2.read_text(encoding="utf-8")

    # 2. 파싱 실행
    result = parse_markdown(text, source_doc=str(INPUT_FILE_PHASE_2))

    # 이미 모델 객체로 반환됨
    session_meta = result["session_meta"]
    turns = result["turns"]

    # 3. 정합성 검증
    assert session_meta is not None, "session_meta가 없음"
    assert session_meta.session_id is not None, "session_id가 없음"
    assert len(turns) > 0, "turns가 비어있음"

    # Turn 블록 분할 정확성
    user_turns = [t for t in turns if t.speaker == "User"]
    cursor_turns = [t for t in turns if t.speaker == "Cursor"]
    unknown_turns = [t for t in turns if t.speaker == "Unknown"]

    assert len(user_turns) > 0, "User turns가 없음"
    assert len(cursor_turns) > 0, "Cursor turns가 없음"

    # 코드 스니펫 추출 정확성
    all_code_blocks = []
    for turn in turns:
        all_code_blocks.extend(turn.code_blocks)

    # 4. 타당성 검증
    # 파싱 실패율 검증
    health = check_parse_health(turns)
    unknown_ratio = health["unknown_ratio"]

    # 5. 결과 분석 및 자동 보고
    report = {
        "test_name": "longcontext_parsing_phase_2",
        "input_file": str(INPUT_FILE_PHASE_2),
        "results": {
            "total_turns": len(turns),
            "user_turns": len(user_turns),
            "cursor_turns": len(cursor_turns),
            "unknown_turns": len(unknown_turns),
            "unknown_ratio": unknown_ratio,
            "code_blocks": len(all_code_blocks),
            "artifacts": len(result.get("artifacts", [])),
            "session_meta": {
                "session_id": session_meta.session_id,
                "exported_at": session_meta.exported_at,
                "cursor_version": session_meta.cursor_version,
                "phase": session_meta.phase,
                "subphase": session_meta.subphase,
            },
        },
        "warnings": health.get("warnings", []),
        "errors": [],
        "status": "PASS" if unknown_ratio < 0.2 else "WARNING",
    }

    # 리포트 출력
    print("\n" + "=" * 50)
    print("Longcontext Parsing Test Report")
    print("=" * 50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 50)

    # 리포트 파일 저장
    REPORT_DIR.mkdir(exist_ok=True)
    report_file = REPORT_DIR / "longcontext_parsing_report.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # 상세 실행 결과 저장 (필수)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"longcontext_parsing_{timestamp}.json"

    detailed_results = {
        "session_meta": session_meta.model_dump(),
        "turns": [turn.model_dump() for turn in turns],
        "code_blocks": [block.model_dump() for block in all_code_blocks],
        "artifacts": result.get("artifacts", []),
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE_PHASE_2),
            "test_name": "longcontext_parsing_phase_2",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\n[RESULTS] Detailed results saved to: {results_file}")

    # 최종 검증
    assert unknown_ratio < 0.2, f"Unknown speaker 비율이 너무 높음: {unknown_ratio:.1%}"


def test_longcontext_parsing_phase_4_3():
    """
    longcontext_phase_4_3.md 파일 파싱 테스트
    """
    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE_PHASE_4_3.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE_PHASE_4_3}")

    text = INPUT_FILE_PHASE_4_3.read_text(encoding="utf-8")

    # 2. 파싱 실행
    result = parse_markdown(text, source_doc=str(INPUT_FILE_PHASE_4_3))

    # 이미 모델 객체로 반환됨
    session_meta = result["session_meta"]
    turns = result["turns"]

    # 3. 정합성 검증
    assert session_meta is not None, "session_meta가 없음"
    assert session_meta.session_id is not None, "session_id가 없음"
    assert len(turns) > 0, "turns가 비어있음"

    # Turn 블록 분할 정확성
    user_turns = [t for t in turns if t.speaker == "User"]
    cursor_turns = [t for t in turns if t.speaker == "Cursor"]
    unknown_turns = [t for t in turns if t.speaker == "Unknown"]

    assert len(user_turns) > 0, "User turns가 없음"
    assert len(cursor_turns) > 0, "Cursor turns가 없음"

    # 코드 스니펫 추출 정확성
    all_code_blocks = []
    for turn in turns:
        all_code_blocks.extend(turn.code_blocks)

    # 4. 타당성 검증
    # 파싱 실패율 검증
    health = check_parse_health(turns)
    unknown_ratio = health["unknown_ratio"]

    # 5. 결과 분석 및 자동 보고
    report = {
        "test_name": "longcontext_parsing_phase_4_3",
        "input_file": str(INPUT_FILE_PHASE_4_3),
        "results": {
            "total_turns": len(turns),
            "user_turns": len(user_turns),
            "cursor_turns": len(cursor_turns),
            "unknown_turns": len(unknown_turns),
            "unknown_ratio": unknown_ratio,
            "code_blocks": len(all_code_blocks),
            "artifacts": len(result.get("artifacts", [])),
            "session_meta": {
                "session_id": session_meta.session_id,
                "exported_at": session_meta.exported_at,
                "cursor_version": session_meta.cursor_version,
                "phase": session_meta.phase,
                "subphase": session_meta.subphase,
            },
        },
        "warnings": health.get("warnings", []),
        "errors": [],
        "status": "PASS" if unknown_ratio < 0.2 else "WARNING",
    }

    # 리포트 출력
    print("\n" + "=" * 50)
    print("Longcontext Parsing Test Report (Phase 4.3)")
    print("=" * 50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 50)

    # 리포트 파일 저장
    REPORT_DIR.mkdir(exist_ok=True)
    report_file = REPORT_DIR / "longcontext_parsing_phase_4_3_report.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # 상세 실행 결과 저장 (필수)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"longcontext_parsing_phase_4_3_{timestamp}.json"

    detailed_results = {
        "session_meta": session_meta.model_dump(),
        "turns": [turn.model_dump() for turn in turns],
        "code_blocks": [block.model_dump() for block in all_code_blocks],
        "artifacts": result.get("artifacts", []),
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE_PHASE_4_3),
            "test_name": "longcontext_parsing_phase_4_3",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\n[RESULTS] Detailed results saved to: {results_file}")

    # 최종 검증
    assert unknown_ratio < 0.2, f"Unknown speaker 비율이 너무 높음: {unknown_ratio:.1%}"
