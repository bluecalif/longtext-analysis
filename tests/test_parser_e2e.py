"""
파서 E2E 테스트

실제 입력 데이터로 전체 파서 파이프라인을 테스트합니다.
"""

import pytest
import json
from pathlib import Path
from datetime import datetime
from backend.parser import parse_markdown
from backend.parser.turns import check_parse_health


# 실제 입력 데이터 경로
INPUT_FILE = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
REPORT_DIR = Path(__file__).parent / "reports"
RESULTS_DIR = Path(__file__).parent / "results"


def test_parser_e2e():
    """
    실제 입력 데이터로 전체 파서 파이프라인 테스트
    """
    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 2. 파싱 실행
    result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 3. 정합성 검증
    assert result["session_meta"] is not None, "session_meta가 없음"
    assert result["session_meta"].session_id is not None, "session_id가 없음"
    assert len(result["turns"]) > 0, "turns가 비어있음"

    # Session Meta 추출 정확성
    session_meta = result["session_meta"]
    assert session_meta.source_doc == str(INPUT_FILE), "source_doc가 올바르지 않음"
    # phase, subphase, exported_at, cursor_version은 있을 수도 없을 수도 있음

    # Turn 블록 분할 정확성
    user_turns = [t for t in result["turns"] if t.speaker == "User"]
    cursor_turns = [t for t in result["turns"] if t.speaker == "Cursor"]
    unknown_turns = [t for t in result["turns"] if t.speaker == "Unknown"]

    assert len(user_turns) > 0, "User turns가 없음"
    assert len(cursor_turns) > 0, "Cursor turns가 없음"

    # 코드 스니펫 추출 정확성
    all_code_blocks = result["code_blocks"]
    # 코드 블록이 있을 수도 없을 수도 있음

    # Artifact 추출 정확성
    all_artifacts = result["artifacts"]
    # Artifact가 있을 수도 없을 수도 있음

    # 4. 타당성 검증
    # 파싱 실패율 검증
    health = check_parse_health(result["turns"])
    unknown_ratio = health["unknown_ratio"]

    assert unknown_ratio < 0.2, f"파싱 실패율이 너무 높음: {unknown_ratio:.1%}"

    # 5. 결과 분석 및 자동 보고
    report = {
        "test_name": "parser_e2e",
        "input_file": str(INPUT_FILE),
        "results": {
            "total_turns": len(result["turns"]),
            "user_turns": len(user_turns),
            "cursor_turns": len(cursor_turns),
            "unknown_turns": len(unknown_turns),
            "unknown_ratio": unknown_ratio,
            "code_blocks": len(all_code_blocks),
            "artifacts": len(all_artifacts),
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
    print("Parser E2E Test Report")
    print("=" * 50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 50)

    # 리포트 파일 저장
    REPORT_DIR.mkdir(exist_ok=True)
    report_file = REPORT_DIR / "parser_e2e_report.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # 상세 실행 결과 저장 (필수)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"parser_e2e_{timestamp}.json"

    detailed_results = {
        "session_meta": session_meta.model_dump(),
        "turns": [turn.model_dump() for turn in result["turns"]],
        "code_blocks": [block.model_dump() for block in result["code_blocks"]],
        "artifacts": result["artifacts"],
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "parser_e2e",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\n[RESULTS] Detailed results saved to: {results_file}")

    # 최종 검증
    assert unknown_ratio < 0.2, f"Unknown speaker 비율이 너무 높음: {unknown_ratio:.1%}"
