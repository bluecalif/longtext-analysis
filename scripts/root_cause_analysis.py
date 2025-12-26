"""
문제 원인 분석 및 개선 방안 도출 스크립트

Phase 3.4 3단계: 문제 원인 분석 및 개선 방안 도출
- 정량적 평가 결과와 정성적 분석 결과를 종합
- 타입 분류 오류 및 Summary 품질 문제의 원인 도출
- 개선 방안 제시 및 우선순위화
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any


def analyze_root_causes(
    evaluation_file: Path,
    notes_analysis_file: Path
) -> Dict[str, Any]:
    """
    정량적 평가와 정성적 분석 결과를 종합하여 원인 분석 및 개선 방안 도출

    Args:
        evaluation_file: 정량적 평가 결과 파일
        notes_analysis_file: 정성적 분석 결과 파일

    Returns:
        원인 분석 및 개선 방안 딕셔너리
    """
    # 1. 정량적 평가 결과 로드
    with open(evaluation_file, "r", encoding="utf-8") as f:
        evaluation = json.load(f)

    # 2. 정성적 분석 결과 로드
    with open(notes_analysis_file, "r", encoding="utf-8") as f:
        notes_analysis = json.load(f)

    # 3. 원인 분석
    root_cause_analysis = {
        "type_classification_issues": {
            "primary_causes": [],
            "secondary_causes": [],
            "improvement_plans": []
        },
        "summary_quality_issues": {
            "primary_causes": [],
            "secondary_causes": [],
            "improvement_plans": []
        },
        "overall_recommendations": []
    }

    # 4. 타입 분류 문제 원인 분석
    confusion_matrix = evaluation.get("type_classification", {}).get("confusion_matrix", {})
    type_accuracy = evaluation.get("type_classification", {}).get("accuracy", 0.0)

    # 주요 혼동 패턴 분석
    major_confusions = []
    for predicted, actuals in confusion_matrix.items():
        for actual, count in actuals.items():
            if predicted != actual and count >= 2:  # 2개 이상인 경우만
                major_confusions.append({
                    "predicted": predicted,
                    "actual": actual,
                    "count": count
                })

    major_confusions.sort(key=lambda x: x["count"], reverse=True)

    # Notes 분석 결과에서 타입 분류 오류 패턴 추출
    type_errors = notes_analysis.get("notes_by_category", {}).get("type_classification_errors", [])

    # 원인 1: 맥락 부족 문제 (가장 많은 오류)
    status_review_to_debug = [e for e in type_errors if e["current_type"] == "status_review" and e["correct_type"] == "debug"]
    if status_review_to_debug:
        root_cause_analysis["type_classification_issues"]["primary_causes"].append({
            "cause": "맥락 부족 문제",
            "description": "status_review가 debug 맥락 안에서 이루어지는 경우를 구분하지 못함",
            "evidence": {
                "count": len(status_review_to_debug),
                "examples": [e["notes"][:200] for e in status_review_to_debug[:3]]
            },
            "improvement_plan": {
                "priority": "HIGH",
                "actions": [
                    "LLM 프롬프트에 이전 Turn의 맥락 정보 제공",
                    "debug 맥락 감지 로직 추가 (슬라이딩 윈도우로 최근 3-5 Turn 확인)",
                    "타입 분류 시 맥락 점수 가중치 적용"
                ]
            }
        })

    # 원인 2: 타입 정의 부족
    type_def_issues = notes_analysis.get("notes_by_category", {}).get("type_definition_issues", [])
    if type_def_issues:
        root_cause_analysis["type_classification_issues"]["primary_causes"].append({
            "cause": "타입 정의 부족",
            "description": "사용자 확인 요청 등 새로운 타입이 필요함",
            "evidence": {
                "count": len(type_def_issues),
                "examples": [e["notes"][:200] for e in type_def_issues]
            },
            "improvement_plan": {
                "priority": "MEDIUM",
                "actions": [
                    "새로운 타입 정의 검토 (예: 'request_to_user', 'confirmation_needed')",
                    "기존 타입 정의 명확화 (status_review vs debug vs plan 구분 기준)",
                    "타입 정의 문서화 및 LLM 프롬프트에 반영"
                ]
            }
        })

    # 원인 3: artifact 타입 분류 실패
    plan_to_artifact = [e for e in type_errors if e["current_type"] == "plan" and e["correct_type"] == "artifact"]
    status_review_to_artifact = [e for e in type_errors if e["current_type"] == "status_review" and e["correct_type"] == "artifact"]
    if plan_to_artifact or status_review_to_artifact:
        root_cause_analysis["type_classification_issues"]["secondary_causes"].append({
            "cause": "Artifact 타입 분류 실패",
            "description": "스크립트 생성 등 artifact 작업을 plan이나 status_review로 분류",
            "evidence": {
                "count": len(plan_to_artifact) + len(status_review_to_artifact),
                "examples": [e["notes"][:200] for e in (plan_to_artifact + status_review_to_artifact)[:3]]
            },
            "improvement_plan": {
                "priority": "MEDIUM",
                "actions": [
                    "파일 생성/수정 키워드 감지 로직 강화",
                    "LLM 프롬프트에 artifact 타입 정의 명확화",
                    "path_candidates가 있으면 artifact 타입 우선 고려"
                ]
            }
        })

    # 원인 4: plan vs debug 구분 실패
    plan_to_debug = [e for e in type_errors if e["current_type"] == "plan" and e["correct_type"] == "debug"]
    if plan_to_debug:
        root_cause_analysis["type_classification_issues"]["secondary_causes"].append({
            "cause": "Plan vs Debug 구분 실패",
            "description": "debug 맥락 안에서의 계획을 plan으로 분류",
            "evidence": {
                "count": len(plan_to_debug),
                "examples": [e["notes"][:200] for e in plan_to_debug[:3]]
            },
            "improvement_plan": {
                "priority": "MEDIUM",
                "actions": [
                    "맥락 기반 타입 분류 로직 추가",
                    "debug 맥락 감지 시 plan 타입 점수 감소",
                    "LLM 프롬프트에 plan vs debug 구분 기준 명확화"
                ]
            }
        })

    # 5. Summary 품질 문제 원인 분석
    summary_issues = notes_analysis.get("notes_by_category", {}).get("summary_quality_issues", [])
    avg_summary_quality = evaluation.get("summary_quality", {}).get("average_quality", 0.0)

    if summary_issues or avg_summary_quality < 4.0:
        root_cause_analysis["summary_quality_issues"]["primary_causes"].append({
            "cause": "요약이 Turn의 핵심 내용을 잘 반영하지 못함",
            "description": "요약이 단순 텍스트 자르기만 수행하거나 중요한 정보를 누락",
            "evidence": {
                "average_quality": avg_summary_quality,
                "samples_count": len(summary_issues),
                "examples": [e["notes"][:200] for e in summary_issues[:3]]
            },
            "improvement_plan": {
                "priority": "HIGH",
                "actions": [
                    "LLM 프롬프트에 요약 품질 기준 명확화 (핵심 내용 포함, 구체적 정보 포함)",
                    "요약 생성 시 문장 단위로 자르지 않고 의미 단위로 자르기",
                    "요약 길이 제한을 늘려서 더 많은 정보 포함 (현재 150자 → 200자)"
                ]
            }
        })

    # 6. 종합 개선 방안
    root_cause_analysis["overall_recommendations"] = [
        {
            "priority": "HIGH",
            "title": "맥락 기반 타입 분류 개선",
            "description": "이전 Turn의 맥락 정보를 활용하여 타입 분류 정확도 향상",
            "estimated_impact": "타입 분류 정확도 62.69% → 75%+",
            "implementation_steps": [
                "슬라이딩 윈도우로 최근 3-5 Turn의 타입 정보 수집",
                "LLM 프롬프트에 맥락 정보 포함",
                "맥락 점수 가중치 적용"
            ]
        },
        {
            "priority": "HIGH",
            "title": "Summary 품질 개선",
            "description": "LLM 프롬프트 개선 및 요약 생성 로직 개선",
            "estimated_impact": "Summary 품질 3.95 → 4.5+",
            "implementation_steps": [
                "LLM 프롬프트에 요약 품질 기준 명확화",
                "요약 길이 제한 확대 (150자 → 200자)",
                "의미 단위로 요약 생성"
            ]
        },
        {
            "priority": "MEDIUM",
            "title": "타입 정의 명확화",
            "description": "기존 타입 정의 명확화 및 새로운 타입 검토",
            "estimated_impact": "타입 분류 정확도 추가 5-10% 향상",
            "implementation_steps": [
                "타입 정의 문서화",
                "LLM 프롬프트에 타입 정의 명확히 반영",
                "새로운 타입 필요성 검토 (request_to_user 등)"
            ]
        },
        {
            "priority": "MEDIUM",
            "title": "Artifact 타입 분류 강화",
            "description": "파일 생성/수정 작업을 artifact 타입으로 정확히 분류",
            "estimated_impact": "Artifact 타입 분류 정확도 향상",
            "implementation_steps": [
                "파일 생성/수정 키워드 감지 로직 강화",
                "path_candidates가 있으면 artifact 타입 우선 고려",
                "LLM 프롬프트에 artifact 타입 정의 명확화"
            ]
        }
    ]

    return root_cause_analysis


def print_root_cause_analysis(analysis: Dict[str, Any]):
    """원인 분석 결과 출력"""
    print("\n" + "=" * 70)
    print("Root Cause Analysis & Improvement Plan")
    print("=" * 70)

    # 타입 분류 문제
    type_issues = analysis.get("type_classification_issues", {})
    primary_causes = type_issues.get("primary_causes", [])
    secondary_causes = type_issues.get("secondary_causes", [])

    print(f"\n[Type Classification Issues]")
    print(f"\n  Primary Causes ({len(primary_causes)}):")
    for i, cause in enumerate(primary_causes, 1):
        print(f"    {i}. {cause['cause']}")
        print(f"       Description: {cause['description']}")
        print(f"       Evidence: {cause['evidence']['count']} cases")
        print(f"       Priority: {cause['improvement_plan']['priority']}")
        print(f"       Actions:")
        for action in cause['improvement_plan']['actions']:
            print(f"         - {action}")

    if secondary_causes:
        print(f"\n  Secondary Causes ({len(secondary_causes)}):")
        for i, cause in enumerate(secondary_causes, 1):
            print(f"    {i}. {cause['cause']}")
            print(f"       Description: {cause['description']}")
            print(f"       Evidence: {cause['evidence']['count']} cases")
            print(f"       Priority: {cause['improvement_plan']['priority']}")

    # Summary 품질 문제
    summary_issues = analysis.get("summary_quality_issues", {})
    summary_primary = summary_issues.get("primary_causes", [])

    if summary_primary:
        print(f"\n[Summary Quality Issues]")
        for i, cause in enumerate(summary_primary, 1):
            print(f"    {i}. {cause['cause']}")
            print(f"       Description: {cause['description']}")
            print(f"       Evidence: avg_quality={cause['evidence'].get('average_quality', 0):.2f}, samples={cause['evidence'].get('samples_count', 0)}")
            print(f"       Priority: {cause['improvement_plan']['priority']}")
            print(f"       Actions:")
            for action in cause['improvement_plan']['actions']:
                print(f"         - {action}")

    # 종합 개선 방안
    recommendations = analysis.get("overall_recommendations", [])
    print(f"\n[Overall Recommendations]")
    for i, rec in enumerate(recommendations, 1):
        print(f"    {i}. [{rec['priority']}] {rec['title']}")
        print(f"       Description: {rec['description']}")
        print(f"       Estimated Impact: {rec['estimated_impact']}")
        print(f"       Implementation Steps:")
        for step in rec['implementation_steps']:
            print(f"         - {step}")

    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="문제 원인 분석 및 개선 방안 도출"
    )
    parser.add_argument(
        "--evaluation-file",
        type=str,
        required=True,
        help="정량적 평가 결과 파일 경로"
    )
    parser.add_argument(
        "--notes-analysis-file",
        type=str,
        required=True,
        help="정성적 분석 결과 파일 경로"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="출력 리포트 파일 경로"
    )

    args = parser.parse_args()

    evaluation_file = Path(args.evaluation_file)
    notes_analysis_file = Path(args.notes_analysis_file)

    # 파일 존재 확인
    if not evaluation_file.exists():
        print(f"[ERROR] Evaluation file not found: {evaluation_file}")
        return 1

    if not notes_analysis_file.exists():
        print(f"[ERROR] Notes analysis file not found: {notes_analysis_file}")
        return 1

    # 원인 분석 실행
    print(f"[INFO] Analyzing root causes...")
    analysis = analyze_root_causes(evaluation_file, notes_analysis_file)

    # 분석 결과 출력
    print_root_cause_analysis(analysis)

    # 리포트 파일 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if args.output_file:
        output_file = Path(args.output_file)
    else:
        reports_dir = Path(__file__).parent.parent / "tests" / "reports"
        reports_dir.mkdir(exist_ok=True)
        output_file = reports_dir / f"root_cause_analysis_{timestamp}.json"

    analysis_report = {
        "analysis_metadata": {
            "timestamp": timestamp,
            "evaluation_file": str(evaluation_file),
            "notes_analysis_file": str(notes_analysis_file),
        },
        **analysis
    }

    output_file.write_text(
        json.dumps(analysis_report, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"\n[SUCCESS] Root cause analysis report saved to: {output_file}")

    return 0


if __name__ == "__main__":
    import argparse
    exit(main())

