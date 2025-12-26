"""
수동 검증 Notes 정성적 분석 스크립트

Phase 3.4 2단계: 정성적 분석 - Notes 내용 확인
- manual_review_updated.json의 모든 샘플(67개) 순회
- 각 샘플의 notes 필드 내용 확인
- 문제 패턴 분류
- Notes 분석 결과 리포트 생성 및 저장
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Any


def analyze_notes(review_file: Path) -> Dict[str, Any]:
    """
    Notes 내용을 분석하여 문제 패턴 분류

    Args:
        review_file: 수동 검증 결과 파일 경로

    Returns:
        분석 결과 딕셔너리
    """
    # 1. 수동 검증 결과 로드
    with open(review_file, "r", encoding="utf-8") as f:
        review_data = json.load(f)

    samples = review_data.get("samples", [])
    if len(samples) == 0:
        return {"error": "No samples found in review file"}

    # 2. 분석 결과 저장
    analysis_result = {
        "metadata": {
            "review_file": str(review_file),
            "total_samples": len(samples),
            "samples_with_notes": 0,
            "samples_with_type_mismatch": 0,
            "samples_with_low_quality": 0,
        },
        "notes_by_category": {
            "type_classification_errors": [],
            "summary_quality_issues": [],
            "llm_prompt_issues": [],
            "regex_pattern_issues": [],
            "context_lack_issues": [],
            "type_definition_issues": [],
            "other_issues": [],
        },
        "problem_patterns": {
            "type_mismatches": defaultdict(list),  # predicted -> actual: [samples]
            "low_quality_samples": [],  # summary_quality <= 3 or summary_completeness <= 3
            "low_accuracy_samples": [],  # type_accuracy <= 3
        },
        "detailed_analysis": []
    }

    # 3. 각 샘플 분석
    for sample in samples:
        event_id = sample.get("event_id", "UNKNOWN")
        turn_index = sample.get("turn_index", -1)
        current_event = sample.get("current_event", {})
        manual_review = sample.get("manual_review", {})

        current_type = current_event.get("type")
        correct_type = manual_review.get("correct_type")
        notes = manual_review.get("notes", "").strip()
        summary_quality = manual_review.get("summary_quality")
        summary_completeness = manual_review.get("summary_completeness")
        type_accuracy = manual_review.get("type_accuracy")

        # Notes가 있는 샘플
        if notes:
            analysis_result["metadata"]["samples_with_notes"] += 1

        # 타입 불일치 샘플
        type_mismatch = False
        if correct_type is not None and current_type != correct_type:
            type_mismatch = True
            analysis_result["metadata"]["samples_with_type_mismatch"] += 1
            analysis_result["problem_patterns"]["type_mismatches"][f"{current_type} -> {correct_type}"].append({
                "event_id": event_id,
                "turn_index": turn_index,
                "notes": notes
            })

        # 낮은 품질 샘플
        low_quality = False
        if (summary_quality is not None and summary_quality <= 3) or \
           (summary_completeness is not None and summary_completeness <= 3):
            low_quality = True
            analysis_result["metadata"]["samples_with_low_quality"] += 1
            analysis_result["problem_patterns"]["low_quality_samples"].append({
                "event_id": event_id,
                "turn_index": turn_index,
                "summary_quality": summary_quality,
                "summary_completeness": summary_completeness,
                "notes": notes
            })

        # 낮은 정확도 샘플
        if type_accuracy is not None and type_accuracy <= 3:
            analysis_result["problem_patterns"]["low_accuracy_samples"].append({
                "event_id": event_id,
                "turn_index": turn_index,
                "type_accuracy": type_accuracy,
                "notes": notes
            })

        # Notes 내용 분석 및 분류
        if notes:
            notes_lower = notes.lower()

            # 타입 분류 오류
            if any(keyword in notes_lower for keyword in ["타입 문제", "타입", "분류", "type"]):
                if "새로운 type 정의 필요" in notes or "type 정의" in notes:
                    analysis_result["notes_by_category"]["type_definition_issues"].append({
                        "event_id": event_id,
                        "turn_index": turn_index,
                        "current_type": current_type,
                        "correct_type": correct_type,
                        "notes": notes
                    })
                else:
                    analysis_result["notes_by_category"]["type_classification_errors"].append({
                        "event_id": event_id,
                        "turn_index": turn_index,
                        "current_type": current_type,
                        "correct_type": correct_type,
                        "notes": notes
                    })

            # Summary 품질 문제
            elif any(keyword in notes_lower for keyword in ["요약 문제", "요약", "summary"]):
                analysis_result["notes_by_category"]["summary_quality_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "summary_quality": summary_quality,
                    "summary_completeness": summary_completeness,
                    "notes": notes
                })

            # LLM 프롬프트 문제
            elif any(keyword in notes_lower for keyword in ["llm", "프롬프트", "prompt", "이해"]):
                analysis_result["notes_by_category"]["llm_prompt_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })

            # 정규식 패턴 문제
            elif any(keyword in notes_lower for keyword in ["정규식", "패턴", "regex", "pattern"]):
                analysis_result["notes_by_category"]["regex_pattern_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })

            # 맥락 부족 문제
            elif any(keyword in notes_lower for keyword in ["맥락", "이전 turn", "이전 turn의", "context", "어려운"]):
                analysis_result["notes_by_category"]["context_lack_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })

            # 기타
            else:
                analysis_result["notes_by_category"]["other_issues"].append({
                    "event_id": event_id,
                    "turn_index": turn_index,
                    "notes": notes
                })

        # 상세 분석 항목 추가
        detailed_item = {
            "event_id": event_id,
            "turn_index": turn_index,
            "current_type": current_type,
            "correct_type": correct_type,
            "type_mismatch": type_mismatch,
            "summary_quality": summary_quality,
            "summary_completeness": summary_completeness,
            "type_accuracy": type_accuracy,
            "notes": notes,
            "has_notes": bool(notes),
            "is_problematic": type_mismatch or low_quality or (type_accuracy is not None and type_accuracy <= 3)
        }
        analysis_result["detailed_analysis"].append(detailed_item)

    # 4. 통계 계산
    analysis_result["statistics"] = {
        "total_samples": len(samples),
        "samples_with_notes": analysis_result["metadata"]["samples_with_notes"],
        "samples_with_type_mismatch": analysis_result["metadata"]["samples_with_type_mismatch"],
        "samples_with_low_quality": analysis_result["metadata"]["samples_with_low_quality"],
        "samples_with_low_accuracy": len(analysis_result["problem_patterns"]["low_accuracy_samples"]),
        "notes_category_counts": {
            "type_classification_errors": len(analysis_result["notes_by_category"]["type_classification_errors"]),
            "summary_quality_issues": len(analysis_result["notes_by_category"]["summary_quality_issues"]),
            "llm_prompt_issues": len(analysis_result["notes_by_category"]["llm_prompt_issues"]),
            "regex_pattern_issues": len(analysis_result["notes_by_category"]["regex_pattern_issues"]),
            "context_lack_issues": len(analysis_result["notes_by_category"]["context_lack_issues"]),
            "type_definition_issues": len(analysis_result["notes_by_category"]["type_definition_issues"]),
            "other_issues": len(analysis_result["notes_by_category"]["other_issues"]),
        },
        "type_mismatch_counts": {
            mismatch: len(samples)
            for mismatch, samples in analysis_result["problem_patterns"]["type_mismatches"].items()
        }
    }

    return analysis_result


def print_analysis_summary(analysis_result: Dict[str, Any]):
    """분석 결과 요약 출력"""
    print("\n" + "=" * 70)
    print("Manual Review Notes Analysis Report (Qualitative)")
    print("=" * 70)

    metadata = analysis_result.get("metadata", {})
    stats = analysis_result.get("statistics", {})

    print(f"\n[Metadata]")
    print(f"  Total samples: {metadata.get('total_samples', 0)}")
    print(f"  Samples with notes: {stats.get('samples_with_notes', 0)}")
    print(f"  Samples with type mismatch: {stats.get('samples_with_type_mismatch', 0)}")
    print(f"  Samples with low quality: {stats.get('samples_with_low_quality', 0)}")
    print(f"  Samples with low accuracy: {stats.get('samples_with_low_accuracy', 0)}")

    print(f"\n[Notes Category Counts]")
    category_counts = stats.get("notes_category_counts", {})
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"  {category}: {count}")

    print(f"\n[Type Mismatch Patterns]")
    mismatch_counts = stats.get("type_mismatch_counts", {})
    for mismatch, count in sorted(mismatch_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {mismatch}: {count}")

    # 주요 문제 샘플 출력
    notes_by_category = analysis_result.get("notes_by_category", {})

    # 타입 분류 오류 샘플 (상위 5개)
    type_errors = notes_by_category.get("type_classification_errors", [])
    if type_errors:
        print(f"\n[Type Classification Errors - Sample (Top 5)]")
        for item in type_errors[:5]:
            print(f"  EVT-{item['turn_index']:03d}: {item['current_type']} -> {item['correct_type']}")
            print(f"    Notes: {item['notes'][:100]}...")

    # Summary 품질 문제 샘플 (상위 5개)
    summary_issues = notes_by_category.get("summary_quality_issues", [])
    if summary_issues:
        print(f"\n[Summary Quality Issues - Sample (Top 5)]")
        for item in summary_issues[:5]:
            print(f"  EVT-{item['turn_index']:03d}: quality={item.get('summary_quality')}, completeness={item.get('summary_completeness')}")
            print(f"    Notes: {item['notes'][:100]}...")

    # 맥락 부족 문제 샘플
    context_issues = notes_by_category.get("context_lack_issues", [])
    if context_issues:
        print(f"\n[Context Lack Issues - Sample (Top 5)]")
        for item in context_issues[:5]:
            print(f"  EVT-{item['turn_index']:03d}")
            print(f"    Notes: {item['notes'][:100]}...")

    # 타입 정의 부족 문제 샘플
    type_def_issues = notes_by_category.get("type_definition_issues", [])
    if type_def_issues:
        print(f"\n[Type Definition Issues - Sample]")
        for item in type_def_issues:
            print(f"  EVT-{item['turn_index']:03d}: {item['current_type']} -> {item['correct_type']}")
            print(f"    Notes: {item['notes'][:100]}...")

    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="수동 검증 Notes 정성적 분석"
    )
    parser.add_argument(
        "--review-file",
        type=str,
        required=True,
        help="수동 검증 결과 파일 경로 (manual_review_updated.json)"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="출력 리포트 파일 경로 (기본값: tests/reports/manual_review_notes_analysis_YYYYMMDD_HHMMSS.json)"
    )

    args = parser.parse_args()

    review_file = Path(args.review_file)

    # 파일 존재 확인
    if not review_file.exists():
        print(f"[ERROR] Review file not found: {review_file}")
        return 1

    # Notes 분석 실행
    print(f"[INFO] Analyzing notes from: {review_file}")
    analysis_result = analyze_notes(review_file)

    # 분석 결과 출력
    print_analysis_summary(analysis_result)

    # 리포트 파일 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if args.output_file:
        output_file = Path(args.output_file)
    else:
        reports_dir = Path(__file__).parent.parent / "tests" / "reports"
        reports_dir.mkdir(exist_ok=True)
        output_file = reports_dir / f"manual_review_notes_analysis_{timestamp}.json"

    # 분석 결과에 메타데이터 추가
    analysis_report = {
        "analysis_metadata": {
            "timestamp": timestamp,
            "review_file": str(review_file),
        },
        **analysis_result
    }

    output_file.write_text(
        json.dumps(analysis_report, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"\n[SUCCESS] Analysis report saved to: {output_file}")

    return 0


if __name__ == "__main__":
    import argparse
    exit(main())

