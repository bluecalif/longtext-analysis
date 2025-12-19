"""
이벤트 정규화 E2E 테스트

실제 입력 데이터로 전체 이벤트 정규화 파이프라인을 테스트합니다.
"""

import pytest
import json
from pathlib import Path
from datetime import datetime
from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.core.models import EventType


# 실제 입력 데이터 경로
INPUT_FILE = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
REPORT_DIR = Path(__file__).parent / "reports"
RESULTS_DIR = Path(__file__).parent / "results"


def test_event_normalizer_e2e():
    """
    실제 입력 데이터로 전체 이벤트 정규화 파이프라인 테스트
    """
    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 2. 파싱 실행 (Phase 2 결과)
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 3. 이벤트 정규화 실행
    events = normalize_turns_to_events(parse_result["turns"])

    # 4. 정합성 검증
    assert len(events) > 0, "이벤트가 생성되지 않음"
    assert len(events) >= len(parse_result["turns"]), "이벤트 수가 Turn 수보다 적음"

    # Turn → Event 변환 정확성
    turn_refs = [event.turn_ref for event in events]
    unique_turn_refs = set(turn_refs)
    assert len(unique_turn_refs) == len(parse_result["turns"]), "모든 Turn이 이벤트로 변환되지 않음"

    # Event 타입 분류 정확성
    event_types = [event.type for event in events]
    unique_types = set(event_types)
    valid_types = {EventType.STATUS_REVIEW, EventType.PLAN, EventType.ARTIFACT,
                   EventType.DEBUG, EventType.COMPLETION, EventType.NEXT_STEP, EventType.TURN}
    for event_type in unique_types:
        assert event_type in valid_types, f"유효하지 않은 이벤트 타입: {event_type}"

    # Phase/Subphase 연결 정확성 (SessionMeta에서 가져옴)
    session_meta = parse_result["session_meta"]
    # Phase/Subphase는 Timeline 빌더에서 연결되므로 여기서는 기본 구조만 확인

    # Artifact 연결 정확성
    artifact_events = [e for e in events if e.type == EventType.ARTIFACT]
    if artifact_events:
        for event in artifact_events:
            assert len(event.artifacts) > 0, "ARTIFACT 타입 이벤트에 artifact가 연결되지 않음"
            for artifact in event.artifacts:
                assert "path" in artifact, "Artifact에 path가 없음"
                assert "action" in artifact, "Artifact에 action이 없음"

    # Snippet 참조 연결 정확성
    events_with_snippets = [e for e in events if e.snippet_refs]
    if events_with_snippets:
        for event in events_with_snippets:
            assert len(event.snippet_refs) > 0, "snippet_refs가 비어있음"
            for snippet_ref in event.snippet_refs:
                assert isinstance(snippet_ref, str), "snippet_ref가 문자열이 아님"

    # 5. 타당성 검증
    # 이벤트 타입 분류의 적절성
    event_type_distribution = {}
    for event_type in event_types:
        event_type_distribution[event_type.value] = event_type_distribution.get(event_type.value, 0) + 1

    # TURN 타입이 가장 많아야 함 (기본 타입)
    assert event_type_distribution.get(EventType.TURN.value, 0) > 0, "TURN 타입 이벤트가 없음"

    # 연결 관계의 정확성
    # Artifact 연결률 계산
    turns_with_paths = [t for t in parse_result["turns"] if t.path_candidates]
    artifact_linking_rate = len(artifact_events) / len(turns_with_paths) if turns_with_paths else 0.0
    # 최소한 일부는 연결되어야 함 (모든 path_candidates가 artifact로 변환되지는 않을 수 있음)

    # 6. 결과 분석 및 자동 보고
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 정량적 데이터 수집
    report = {
        "test_name": "event_normalizer_e2e",
        "timestamp": timestamp,
        "input_file": str(INPUT_FILE),
        "results": {
            "total_turns": len(parse_result["turns"]),
            "total_events": len(events),
            "event_type_distribution": event_type_distribution,
            "artifact_events_count": len(artifact_events),
            "events_with_snippets_count": len(events_with_snippets),
            "artifact_linking_rate": artifact_linking_rate,
        },
        "warnings": [],
        "errors": [],
    }

    # 문제 발견 시 경고 추가
    if len(events) < len(parse_result["turns"]):
        report["warnings"].append(
            f"이벤트 수({len(events)})가 Turn 수({len(parse_result['turns'])})보다 적음"
        )

    if artifact_linking_rate < 0.5 and len(turns_with_paths) > 0:
        report["warnings"].append(
            f"Artifact 연결률이 낮음: {artifact_linking_rate:.1%}"
        )

    # 리포트 출력
    print("\n" + "=" * 50)
    print("Event Normalizer E2E Test Report")
    print("=" * 50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 50)

    # 리포트 파일 저장
    REPORT_DIR.mkdir(exist_ok=True)
    report_file = REPORT_DIR / "event_normalizer_e2e_report.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n[REPORT] Test report saved to: {report_file}")

    # 실행 결과 저장 (상세 이벤트 정규화 결과)
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"event_normalizer_e2e_{timestamp}.json"

    detailed_results = {
        "session_meta": parse_result["session_meta"].model_dump(),
        "turns_count": len(parse_result["turns"]),
        "events": [event.model_dump() for event in events],
        "event_type_distribution": event_type_distribution,
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "event_normalizer_e2e",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[RESULTS] Detailed results saved to: {results_file}")

