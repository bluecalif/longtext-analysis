"""
이벤트 정규화 E2E 테스트

실제 입력 데이터로 전체 이벤트 정규화 파이프라인을 테스트합니다.
"""

import pytest
import json
import os
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# .env 파일 자동 로드
load_dotenv()

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.evaluation import (
    create_manual_review_dataset,
    evaluate_manual_review,
    create_golden_file,
    compare_with_golden
)
from backend.core.models import EventType


# 실제 입력 데이터 경로
INPUT_FILE = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
REPORT_DIR = Path(__file__).parent / "reports"
RESULTS_DIR = Path(__file__).parent / "results"


def test_event_normalizer_e2e():
    """
    실제 입력 데이터로 전체 이벤트 정규화 파이프라인 테스트 (정규식 기반)
    """
    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 2. 파싱 실행 (Phase 2 결과)
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 3. 이벤트 정규화 실행 (정규식 기반)
    session_meta = parse_result["session_meta"]
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=False
    )

    # 4. 정합성 검증
    assert len(events) > 0, "이벤트가 생성되지 않음"
    # 우선순위 기반 단일 이벤트 생성이므로 이벤트 수는 Turn 수와 같아야 함
    assert len(events) == len(
        parse_result["turns"]
    ), f"이벤트 수({len(events)})가 Turn 수({len(parse_result['turns'])})와 일치하지 않음"

    # Turn → Event 변환 정확성 (모든 Turn이 이벤트로 변환되었는지 확인)
    turn_refs = [event.turn_ref for event in events]
    unique_turn_refs = set(turn_refs)
    assert len(unique_turn_refs) == len(parse_result["turns"]), "모든 Turn이 이벤트로 변환되지 않음"

    # 중복 이벤트 확인 (같은 turn_ref가 여러 번 나타나면 안 됨)
    assert len(turn_refs) == len(unique_turn_refs), "중복된 turn_ref가 있음 (단일 이벤트 생성 실패)"

    # Event 타입 분류 정확성
    event_types = [event.type for event in events]
    unique_types = set(event_types)
    valid_types = {
        EventType.STATUS_REVIEW,
        EventType.PLAN,
        EventType.CODE_GENERATION,
        EventType.DEBUG,
        EventType.COMPLETION,
        EventType.NEXT_STEP,
        EventType.TURN,
    }
    for event_type in unique_types:
        assert event_type in valid_types, f"유효하지 않은 이벤트 타입: {event_type}"

    # Phase/Subphase 연결 정확성 (SessionMeta에서 가져옴)
    session_meta = parse_result["session_meta"]
    # Phase/Subphase는 Timeline 빌더에서 연결되므로 여기서는 기본 구조만 확인

    # Code Generation 연결 정확성
    code_generation_events = [e for e in events if e.type == EventType.CODE_GENERATION]
    if code_generation_events:
        for event in code_generation_events:
            # 코드 블록이 있으면 snippet_refs가 있어야 함 (필수)
            turn = parse_result["turns"][event.turn_ref]
            if turn.code_blocks:
                assert len(event.snippet_refs) > 0, "CODE_GENERATION 타입 이벤트에 코드 블록이 있지만 snippet_refs가 비어있음"
            # 파일 경로가 있으면 artifacts가 있어야 함 (선택적)
            if turn.path_candidates:
                assert len(event.artifacts) > 0, "CODE_GENERATION 타입 이벤트에 파일 경로가 있지만 artifacts가 비어있음"
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
        event_type_distribution[event_type.value] = (
            event_type_distribution.get(event_type.value, 0) + 1
        )

    # TURN 타입이 가장 많아야 함 (기본 타입)
    assert event_type_distribution.get(EventType.TURN.value, 0) > 0, "TURN 타입 이벤트가 없음"

    # 연결 관계의 정확성
    # Code Generation 연결률 계산 (코드 블록이 있는 Turn 중 code_generation 타입으로 분류된 비율)
    turns_with_code_blocks = [t for t in parse_result["turns"] if t.code_blocks]
    code_generation_linking_rate = (
        len(code_generation_events) / len(turns_with_code_blocks) if turns_with_code_blocks else 0.0
    )
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
            "code_generation_events_count": len(code_generation_events),
            "events_with_snippets_count": len(events_with_snippets),
            "code_generation_linking_rate": code_generation_linking_rate,
        },
        "warnings": [],
        "errors": [],
    }

    # 문제 발견 시 경고 추가
    if len(events) != len(parse_result["turns"]):
        report["warnings"].append(
            f"이벤트 수({len(events)})가 Turn 수({len(parse_result['turns'])})와 일치하지 않음 (단일 이벤트 생성 실패)"
        )

    # 중복 이벤트 확인
    turn_refs = [event.turn_ref for event in events]
    if len(turn_refs) != len(set(turn_refs)):
        report["warnings"].append(f"중복된 turn_ref가 발견됨 (단일 이벤트 생성 실패)")

    if code_generation_linking_rate < 0.5 and len(turns_with_code_blocks) > 0:
        report["warnings"].append(f"Code Generation 연결률이 낮음: {code_generation_linking_rate:.1%}")

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


def test_event_normalizer_e2e_with_llm():
    """
    실제 입력 데이터로 전체 이벤트 정규화 파이프라인 테스트 (LLM 기반)
    """
    import os

    # API 키 확인 (없으면 스킵)
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 환경 변수가 설정되지 않음")

    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8")

    # 2. 파싱 실행 (Phase 2 결과)
    parse_result = parse_markdown(text, source_doc=str(INPUT_FILE))

    # 3. 이벤트 정규화 실행 (LLM 기반, 병렬 처리)
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

    # 4. 정합성 검증
    assert len(events) > 0, "이벤트가 생성되지 않음"
    assert len(events) == len(
        parse_result["turns"]
    ), f"이벤트 수({len(events)})가 Turn 수({len(parse_result['turns'])})와 일치하지 않음"

    # 처리 방법 확인 (LLM 기반이므로 모두 "llm")
    processing_methods = [getattr(event, "processing_method", "regex") for event in events]
    assert all(
        method == "llm" for method in processing_methods
    ), "LLM 기반 테스트인데 processing_method가 'llm'이 아님"

    # Turn → Event 변환 정확성
    turn_refs = [event.turn_ref for event in events]
    unique_turn_refs = set(turn_refs)
    assert len(unique_turn_refs) == len(parse_result["turns"]), "모든 Turn이 이벤트로 변환되지 않음"
    assert len(turn_refs) == len(unique_turn_refs), "중복된 turn_ref가 있음"

    # 병렬 처리 후 순서 유지 확인 (turn_ref가 순차적으로 증가하는지 확인)
    for i, event in enumerate(events):
        assert (
            event.turn_ref == parse_result["turns"][i].turn_index
        ), f"이벤트 순서가 올바르지 않음: 인덱스 {i}에서 turn_ref {event.turn_ref} != turn_index {parse_result['turns'][i].turn_index}"

    # Event 타입 분류 정확성
    event_types = [event.type for event in events]
    unique_types = set(event_types)
    valid_types = {
        EventType.STATUS_REVIEW,
        EventType.PLAN,
        EventType.CODE_GENERATION,
        EventType.DEBUG,
        EventType.COMPLETION,
        EventType.NEXT_STEP,
        EventType.TURN,
    }
    for event_type in unique_types:
        assert event_type in valid_types, f"유효하지 않은 이벤트 타입: {event_type}"

    # Code Generation 연결 정확성
    # LLM 기반에서는 code_generation 타입으로 분류되었지만 실제 코드 블록이 없을 수 있음
    # 실제 코드 블록이 있는 Turn에 대해서만 검증
    code_generation_events = [e for e in events if e.type == EventType.CODE_GENERATION]
    if code_generation_events:
        for event in code_generation_events:
            # 해당 Turn에 실제 코드 블록이 있는지 확인
            turn = parse_result["turns"][event.turn_ref]
            if turn.code_blocks:
                # 코드 블록이 있으면 snippet_refs 배열에도 포함되어야 함
                assert (
                    len(event.snippet_refs) > 0
                ), f"CODE_GENERATION 타입 이벤트(turn_ref={event.turn_ref})에 코드 블록이 있지만 snippet_refs 배열이 비어있음"

    # Snippet 참조 연결 정확성
    events_with_snippets = [e for e in events if e.snippet_refs]
    if events_with_snippets:
        for event in events_with_snippets:
            assert len(event.snippet_refs) > 0, "snippet_refs가 비어있음"

    # 5. 타당성 검증
    event_type_distribution = {}
    for event_type in event_types:
        event_type_distribution[event_type.value] = (
            event_type_distribution.get(event_type.value, 0) + 1
        )

    # Code Generation 연결률 계산 (코드 블록이 있는 Turn 중 code_generation 타입으로 분류된 비율)
    turns_with_code_blocks = [t for t in parse_result["turns"] if t.code_blocks]
    code_generation_linking_rate = (
        len(code_generation_events) / len(turns_with_code_blocks) if turns_with_code_blocks else 0.0
    )

    # 캐시 사용 통계 계산 (실행 중 통계 + 파일 기반 통계)
    from backend.core.cache import CACHE_DIR

    # 실행 중 통계 (실제 캐시 사용 여부)
    runtime_cache_hits = runtime_cache_stats["hits"]
    runtime_cache_misses = runtime_cache_stats["misses"]
    runtime_cache_saves = runtime_cache_stats["saves"]
    runtime_cache_hit_rate = (
        runtime_cache_hits / len(parse_result["turns"]) if parse_result["turns"] else 0.0
    )

    # 파일 기반 통계 (테스트 실행 후 캐시 파일 존재 여부)
    file_based_cache_hits = 0
    file_based_cache_misses = 0
    for turn in parse_result["turns"]:
        cache_key = f"llm_{hash(turn.body[:1000]) % 1000000}"
        cache_file = CACHE_DIR / f"{cache_key}.json"
        if cache_file.exists():
            file_based_cache_hits += 1
        else:
            file_based_cache_misses += 1
    file_based_cache_hit_rate = (
        file_based_cache_hits / len(parse_result["turns"]) if parse_result["turns"] else 0.0
    )

    # 6. 결과 분석 및 자동 보고
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    report = {
        "test_name": "event_normalizer_e2e_with_llm",
        "timestamp": timestamp,
        "input_file": str(INPUT_FILE),
        "results": {
            "total_turns": len(parse_result["turns"]),
            "total_events": len(events),
            "event_type_distribution": event_type_distribution,
            "code_generation_events_count": len(code_generation_events),
            "events_with_snippets_count": len(events_with_snippets),
            "code_generation_linking_rate": code_generation_linking_rate,
            "processing_method": "llm",
            "parallel_processing": True,
            "max_workers": 5,
            "elapsed_time_seconds": round(elapsed_time, 2),
            "average_time_per_turn": (
                round(elapsed_time / len(parse_result["turns"]), 2) if parse_result["turns"] else 0
            ),
            "cache_statistics": {
                "runtime": {
                    "cache_hits": runtime_cache_hits,
                    "cache_misses": runtime_cache_misses,
                    "cache_saves": runtime_cache_saves,
                    "cache_hit_rate": round(runtime_cache_hit_rate, 4),
                },
                "file_based": {
                    "cache_hits": file_based_cache_hits,
                    "cache_misses": file_based_cache_misses,
                    "cache_hit_rate": round(file_based_cache_hit_rate, 4),
                },
            },
        },
        "warnings": [],
        "errors": [],
    }

    # 문제 발견 시 경고 추가
    if len(events) != len(parse_result["turns"]):
        report["warnings"].append(
            f"이벤트 수({len(events)})가 Turn 수({len(parse_result['turns'])})와 일치하지 않음"
        )

    turn_refs = [event.turn_ref for event in events]
    if len(turn_refs) != len(set(turn_refs)):
        report["warnings"].append(f"중복된 turn_ref가 발견됨")

    if code_generation_linking_rate < 0.5 and len(turns_with_code_blocks) > 0:
        report["warnings"].append(f"Code Generation 연결률이 낮음: {code_generation_linking_rate:.1%}")

    # 리포트 출력
    print("\n" + "=" * 50)
    print("Event Normalizer E2E Test Report (LLM)")
    print("=" * 50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 50)

    # 리포트 파일 저장
    REPORT_DIR.mkdir(exist_ok=True)
    report_file = REPORT_DIR / "event_normalizer_e2e_llm_report.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n[REPORT] LLM E2E test report saved to: {report_file}")

    # 실행 결과 저장 (상세 이벤트 정규화 결과)
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"event_normalizer_e2e_llm_{timestamp}.json"

    detailed_results = {
        "session_meta": parse_result["session_meta"].model_dump(),
        "turns_count": len(parse_result["turns"]),
        "events": [event.model_dump() for event in events],
        "event_type_distribution": event_type_distribution,
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "event_normalizer_e2e_with_llm",
            "processing_method": "llm",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[RESULTS] Detailed results saved to: {results_file}")

    # 7. 평가 도구 통합 (Phase 3.3)
    # 7-1. 수동 검증 데이터셋 생성
    MANUAL_REVIEW_DIR = Path(__file__).parent / "manual_review"
    MANUAL_REVIEW_DIR.mkdir(exist_ok=True)

    manual_review_dataset = create_manual_review_dataset(
        events=events,
        turns=parse_result["turns"],
        output_file=MANUAL_REVIEW_DIR / f"manual_review_dataset_{timestamp}.json",
        sample_size=30,
        min_per_type=3
    )
    print(f"\n[EVALUATION] Manual review dataset created: {len(manual_review_dataset['samples'])} samples")
    print(f"[EVALUATION] Dataset saved to: {MANUAL_REVIEW_DIR / f'manual_review_dataset_{timestamp}.json'}")

    # 7-2. Golden 파일 비교 (회귀 테스트용, 수동 검증 후 생성됨)
    GOLDEN_DIR = Path(__file__).parent / "golden"
    GOLDEN_DIR.mkdir(exist_ok=True)

    golden_file = GOLDEN_DIR / "event_normalizer_golden.json"

    if golden_file.exists():
        # Golden 파일과 비교 (회귀 감지)
        comparison_result = compare_with_golden(
            current_events=events,
            golden_file=golden_file,
            similarity_threshold=0.95
        )

        if comparison_result.get("regression_detected"):
            print(f"\n[WARNING] Regression detected!")
            for reason in comparison_result.get("regression_reasons", []):
                print(f"  - {reason}")
        else:
            print(f"\n[EVALUATION] No regression detected (similarity >= 95%)")

        # 비교 결과 리포트에 추가
        report["evaluation"] = {
            "golden_comparison": comparison_result,
            "manual_review_dataset": {
                "samples_count": len(manual_review_dataset["samples"]),
                "file": str(MANUAL_REVIEW_DIR / f"manual_review_dataset_{timestamp}.json")
            }
        }

        # 리포트 파일 업데이트
        report_file.write_text(
            json.dumps(report, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
    else:
        # Golden 파일이 없으면 안내 메시지 출력
        print(f"\n[INFO] Golden file not found: {golden_file}")
        print("[INFO] Golden 파일 생성 방법:")
        print("  1. 수동 검증 데이터셋 파일을 열어서 각 샘플에 대해 평가 입력")
        print("  2. 수동 검증 완료 후 다음 명령어 실행:")
        print(f"     poetry run python -c \"")
        print(f"     from backend.builders.evaluation import create_golden_file_from_manual_review;")
        print(f"     from backend.parser import parse_markdown;")
        print(f"     from pathlib import Path;")
        print(f"     # ... (스크립트 예시)\"")
        print(f"  3. 또는 별도 스크립트 사용: scripts/create_golden_file.py")

        # 리포트에 수동 검증 안내 추가
        report["evaluation"] = {
            "manual_review_dataset": {
                "samples_count": len(manual_review_dataset["samples"]),
                "file": str(MANUAL_REVIEW_DIR / f"manual_review_dataset_{timestamp}.json"),
                "status": "pending_manual_review"
            },
            "golden_file": {
                "status": "not_created",
                "message": "수동 검증 완료 후 생성 필요"
            }
        }

        # 리포트 파일 업데이트
        report_file.write_text(
            json.dumps(report, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
