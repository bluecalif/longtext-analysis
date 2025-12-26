"""
수동 검증 후 Golden 파일 생성 스크립트

사용법:
    poetry run python scripts/create_golden_file.py \
        --review-file tests/manual_review/manual_review_dataset_YYYYMMDD_HHMMSS.json \
        --results-file tests/results/event_normalizer_e2e_llm_YYYYMMDD_HHMMSS.json \
        --min-accuracy 0.85
"""

import argparse
import json
from pathlib import Path
from backend.builders.evaluation import create_golden_file_from_manual_review


def main():
    parser = argparse.ArgumentParser(description="수동 검증 결과를 기반으로 Golden 파일 생성")
    parser.add_argument(
        "--review-file",
        type=str,
        required=True,
        help="수동 검증 결과 파일 경로 (manual_review_dataset_*.json)",
    )
    parser.add_argument(
        "--results-file",
        type=str,
        required=True,
        help="E2E 테스트 결과 파일 경로 (event_normalizer_e2e_llm_*.json)",
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="출력 Golden 파일 경로 (기본값: tests/golden/event_normalizer_golden.json)",
    )
    parser.add_argument(
        "--min-accuracy", type=float, default=0.85, help="최소 정확도 요구사항 (기본값: 0.85)"
    )
    parser.add_argument(
        "--no-corrections",
        action="store_true",
        help="수동 검증의 correct_type을 적용하지 않음 (기본값: 적용함)",
    )

    args = parser.parse_args()

    review_file = Path(args.review_file)
    results_file = Path(args.results_file)
    output_file = Path(args.output_file) if args.output_file else None

    # 파일 존재 확인
    if not review_file.exists():
        print(f"[ERROR] Review file not found: {review_file}")
        return 1

    if not results_file.exists():
        print(f"[ERROR] Results file not found: {results_file}")
        return 1

    # Golden 파일 생성
    print(f"[INFO] Creating golden file from manual review...")
    print(f"  Review file: {review_file}")
    print(f"  Results file: {results_file}")
    print(f"  Min accuracy: {args.min_accuracy:.2%}")
    print(f"  Apply corrections: {not args.no_corrections}")

    result = create_golden_file_from_manual_review(
        review_file=review_file,
        results_file=results_file,
        output_file=output_file,
        min_accuracy=args.min_accuracy,
        apply_corrections=not args.no_corrections,
    )

    if result.get("created"):
        print(f"\n[SUCCESS] Golden file created: {result['file_path']}")
        print(f"  Type accuracy: {result['type_accuracy']:.2%}")
        print(f"  Corrections applied: {result['corrections_applied']}")
        if result["corrections_applied"]:
            print(f"  Corrected events: {result['corrected_count']}")
        return 0
    else:
        print(f"\n[FAILED] Golden file creation failed")
        print(f"  Reason: {result.get('reason', 'Unknown error')}")
        if "evaluation" in result:
            eval_data = result["evaluation"]
            if "type_classification" in eval_data:
                acc = eval_data["type_classification"].get("accuracy", 0.0)
                print(f"  Current accuracy: {acc:.2%}")
        return 1


if __name__ == "__main__":
    exit(main())





