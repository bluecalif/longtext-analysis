"""
수동 검증 결과 정량적 평가 스크립트

Phase 3.4 1단계: 정량적 평가 실행
- evaluate_manual_review() 함수 실행
- 타입 분류 정확도 계산
- 혼동 행렬 생성 및 분석
- 처리 방법별 정확도 비교 (LLM vs Regex)
- Summary 품질 점수 통계 분석
- 평가 결과 리포트 생성 및 저장
"""

import argparse
import json
from pathlib import Path
from datetime import datetime
from backend.builders.evaluation import evaluate_manual_review
from backend.core.models import Event, Turn


def load_events_and_turns_from_results(results_file: Path):
    """
    E2E 테스트 결과 파일에서 Event와 Turn 리스트 로드

    Args:
        results_file: E2E 테스트 결과 파일 경로

    Returns:
        (events, turns) 튜플
    """
    with open(results_file, "r", encoding="utf-8") as f:
        results_data = json.load(f)

    # Event 리스트 복원
    events_dict = {e["turn_ref"]: Event(**e) for e in results_data.get("events", [])}
    events_list = list(events_dict.values())

    # Turn 리스트 복원 (turns 필드가 있으면 사용, 없으면 빈 리스트)
    turns_list = []
    if "turns" in results_data:
        turns_dict = {
            t["turn_index"]: Turn(**t)
            for t in results_data.get("turns", [])
            if "turn_index" in t
        }
        turns_list = list(turns_dict.values())

    return events_list, turns_list


def main():
    parser = argparse.ArgumentParser(
        description="수동 검증 결과 정량적 평가 실행"
    )
    parser.add_argument(
        "--review-file",
        type=str,
        required=True,
        help="수동 검증 결과 파일 경로 (manual_review_updated.json)"
    )
    parser.add_argument(
        "--results-file",
        type=str,
        default=None,
        help="E2E 테스트 결과 파일 경로 (event_normalizer_e2e_llm_*.json, 선택적)"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="출력 리포트 파일 경로 (기본값: tests/reports/manual_review_evaluation_YYYYMMDD_HHMMSS.json)"
    )

    args = parser.parse_args()

    review_file = Path(args.review_file)
    results_file = Path(args.results_file) if args.results_file else None

    # 파일 존재 확인
    if not review_file.exists():
        print(f"[ERROR] Review file not found: {review_file}")
        return 1

    # E2E 테스트 결과 파일이 있으면 events와 turns 로드
    events = None
    turns = None
    if results_file and results_file.exists():
        print(f"[INFO] Loading events and turns from: {results_file}")
        events, turns = load_events_and_turns_from_results(results_file)
        print(f"[INFO] Loaded {len(events)} events, {len(turns)} turns")
    else:
        print(f"[INFO] Results file not provided or not found, evaluating without events/turns")

    # 정량적 평가 실행
    print(f"\n[INFO] Evaluating manual review: {review_file}")
    evaluation = evaluate_manual_review(review_file, events=events, turns=turns)

    # 평가 결과 출력
    print("\n" + "=" * 70)
    print("Manual Review Evaluation Report (Quantitative)")
    print("=" * 70)

    # 메타데이터
    metadata = evaluation.get("metadata", {})
    print(f"\n[Metadata]")
    print(f"  Total samples: {metadata.get('total_samples', 0)}")
    print(f"  Evaluated samples: {metadata.get('evaluated_samples', 0)}")

    # 타입 분류 정확도
    type_classification = evaluation.get("type_classification", {})
    type_accuracy = type_classification.get("accuracy", 0.0)
    type_correct = type_classification.get("correct", 0)
    type_total = type_classification.get("total", 0)

    print(f"\n[Type Classification Accuracy]")
    print(f"  Accuracy: {type_accuracy:.2%} ({type_correct}/{type_total})")

    # 혼동 행렬
    confusion_matrix = type_classification.get("confusion_matrix", {})
    if confusion_matrix:
        print(f"\n[Confusion Matrix]")
        print(f"  Format: predicted_type -> actual_type: count")
        for predicted, actuals in sorted(confusion_matrix.items()):
            for actual, count in sorted(actuals.items()):
                if predicted != actual:  # 오류만 표시
                    print(f"    {predicted} -> {actual}: {count}")

    # Summary 품질
    summary_quality = evaluation.get("summary_quality", {})
    avg_quality = summary_quality.get("average_quality")
    avg_completeness = summary_quality.get("average_completeness")
    quality_count = summary_quality.get("samples_count", 0)

    print(f"\n[Summary Quality]")
    if avg_quality is not None:
        print(f"  Average quality: {avg_quality:.2f} / 5.0 ({quality_count} samples)")
    if avg_completeness is not None:
        print(f"  Average completeness: {avg_completeness:.2f} / 5.0 ({quality_count} samples)")

    # Type accuracy scores
    type_accuracy_scores = evaluation.get("type_accuracy_scores", {})
    avg_type_accuracy = type_accuracy_scores.get("average")
    accuracy_count = type_accuracy_scores.get("samples_count", 0)

    if avg_type_accuracy is not None:
        print(f"\n[Type Accuracy Scores (Manual)]")
        print(f"  Average: {avg_type_accuracy:.2f} / 5.0 ({accuracy_count} samples)")

    # 처리 방법별 정확도
    method_comparison = evaluation.get("method_comparison", {})
    if method_comparison:
        print(f"\n[Method Comparison]")
        for method, stats in sorted(method_comparison.items()):
            acc = stats.get("accuracy", 0.0)
            correct = stats.get("correct", 0)
            total = stats.get("total", 0)
            print(f"  {method}: {acc:.2%} ({correct}/{total})")

    print("\n" + "=" * 70)

    # 리포트 파일 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if args.output_file:
        output_file = Path(args.output_file)
    else:
        reports_dir = Path(__file__).parent.parent / "tests" / "reports"
        reports_dir.mkdir(exist_ok=True)
        output_file = reports_dir / f"manual_review_evaluation_{timestamp}.json"

    # 평가 결과에 메타데이터 추가
    evaluation_report = {
        "evaluation_metadata": {
            "timestamp": timestamp,
            "review_file": str(review_file),
            "results_file": str(results_file) if results_file else None,
        },
        **evaluation
    }

    output_file.write_text(
        json.dumps(evaluation_report, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"\n[SUCCESS] Evaluation report saved to: {output_file}")

    return 0


if __name__ == "__main__":
    exit(main())

