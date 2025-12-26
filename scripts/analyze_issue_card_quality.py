"""
Issue Card 품질 분석 스크립트

LLM 기반 추출과 패턴 기반 추출 결과를 비교하여 품질 개선 효과를 분석합니다.
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


def analyze_issue_card_quality(
    llm_result_file: Path,
    pattern_result_file: Optional[Path] = None
) -> Dict[str, Any]:
    """
    Issue Card 품질 분석

    Args:
        llm_result_file: LLM 기반 추출 결과 파일
        pattern_result_file: 패턴 기반 추출 결과 파일 (비교용, 선택적)

    Returns:
        분석 결과 딕셔너리
    """
    # LLM 결과 로드
    with open(llm_result_file, "r", encoding="utf-8") as f:
        llm_data = json.load(f)

    llm_issue_cards = llm_data.get("issue_cards", [])

    if not llm_issue_cards:
        return {
            "error": "Issue cards not found in LLM result file",
            "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S")
        }

    # 1. Symptom 품질 분석
    symptom_lengths = []
    symptom_issues = []
    for card in llm_issue_cards:
        for symptom in card.get("symptoms", []):
            symptom_lengths.append(len(symptom))
            # Symptom 품질 문제 탐지
            if len(symptom) > 500:
                symptom_issues.append({
                    "issue_id": card.get("issue_id"),
                    "issue": "Symptom이 너무 김 (500자 초과)",
                    "length": len(symptom)
                })
            elif len(symptom) < 10:
                symptom_issues.append({
                    "issue_id": card.get("issue_id"),
                    "issue": "Symptom이 너무 짧음 (10자 미만)",
                    "length": len(symptom),
                    "symptom": symptom[:100]
                })

    symptom_avg_length = sum(symptom_lengths) / len(symptom_lengths) if symptom_lengths else 0

    # 2. Root cause 품질 분석
    root_cause_issues = []
    root_cause_status_dist = {"confirmed": 0, "hypothesis": 0, "none": 0}

    for card in llm_issue_cards:
        root_cause = card.get("root_cause")
        if root_cause:
            status = root_cause.get("status", "unknown")
            if status in ["confirmed", "hypothesis"]:
                root_cause_status_dist[status] += 1
            else:
                root_cause_status_dist["none"] += 1

            text = root_cause.get("text", "")
            # 중간 과정 텍스트 포함 여부 확인
            if "원인 분석 중입니다" in text or "분석 중입니다" in text:
                root_cause_issues.append({
                    "issue_id": card.get("issue_id"),
                    "issue": "Root cause에 중간 과정 텍스트 포함",
                    "text_preview": text[:200]
                })

            if len(text) > 500:
                root_cause_issues.append({
                    "issue_id": card.get("issue_id"),
                    "issue": "Root cause 텍스트가 너무 김 (500자 초과)",
                    "length": len(text)
                })
        else:
            root_cause_status_dist["none"] += 1

    # 3. Fix 품질 분석
    fix_issues = []
    fix_count = 0
    fix_with_snippets = 0

    for card in llm_issue_cards:
        fixes = card.get("fix", [])
        fix_count += len(fixes)

        for fix in fixes:
            if fix.get("snippet_refs"):
                fix_with_snippets += 1

            summary = fix.get("summary", "")
            if len(summary) > 1000:
                fix_issues.append({
                    "issue_id": card.get("issue_id"),
                    "issue": "Fix summary가 너무 김 (1000자 초과)",
                    "length": len(summary)
                })
            elif len(summary) < 20:
                fix_issues.append({
                    "issue_id": card.get("issue_id"),
                    "issue": "Fix summary가 너무 짧음 (20자 미만)",
                    "length": len(summary),
                    "summary": summary
                })

    # 4. Validation 품질 분석
    validation_issues = []
    validation_count = 0

    for card in llm_issue_cards:
        validations = card.get("validation", [])
        validation_count += len(validations)

        for validation in validations:
            if len(validation) > 500:
                validation_issues.append({
                    "issue_id": card.get("issue_id"),
                    "issue": "Validation 텍스트가 너무 김 (500자 초과)",
                    "length": len(validation)
                })
            elif len(validation) < 10:
                validation_issues.append({
                    "issue_id": card.get("issue_id"),
                    "issue": "Validation 텍스트가 너무 짧음 (10자 미만)",
                    "length": len(validation),
                    "validation": validation
                })

    # 5. 패턴 기반 결과와 비교 (있는 경우)
    comparison = None
    if pattern_result_file and pattern_result_file.exists():
        with open(pattern_result_file, "r", encoding="utf-8") as f:
            pattern_data = json.load(f)

        pattern_issue_cards = pattern_data.get("issue_cards", [])

        if pattern_issue_cards:
            # Symptom 길이 비교
            pattern_symptom_lengths = []
            for card in pattern_issue_cards:
                for symptom in card.get("symptoms", []):
                    pattern_symptom_lengths.append(len(symptom))

            pattern_symptom_avg = sum(pattern_symptom_lengths) / len(pattern_symptom_lengths) if pattern_symptom_lengths else 0

            comparison = {
                "symptom_avg_length": {
                    "llm": symptom_avg_length,
                    "pattern": pattern_symptom_avg,
                    "improvement": symptom_avg_length < pattern_symptom_avg  # 짧을수록 좋음 (핵심만 추출)
                },
                "root_cause_count": {
                    "llm": sum(1 for c in llm_issue_cards if c.get("root_cause")),
                    "pattern": sum(1 for c in pattern_issue_cards if c.get("root_cause"))
                },
                "fix_count": {
                    "llm": fix_count,
                    "pattern": sum(len(c.get("fix", [])) for c in pattern_issue_cards)
                },
                "validation_count": {
                    "llm": validation_count,
                    "pattern": sum(len(c.get("validation", [])) for c in pattern_issue_cards)
                }
            }

    # 6. 종합 평가
    total_issues = (
        len(symptom_issues) +
        len(root_cause_issues) +
        len(fix_issues) +
        len(validation_issues)
    )

    quality_score = max(0, 100 - (total_issues * 3))  # 이슈당 3점 감점

    # 분석 결과 구성
    analysis_result = {
        "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "llm_result_file": str(llm_result_file),
        "pattern_result_file": str(pattern_result_file) if pattern_result_file else None,
        "summary": {
            "total_issue_cards": len(llm_issue_cards),
            "quality_score": quality_score,
            "total_issues": total_issues
        },
        "metrics": {
            "symptom_quality": {
                "avg_length": symptom_avg_length,
                "min_length": min(symptom_lengths) if symptom_lengths else 0,
                "max_length": max(symptom_lengths) if symptom_lengths else 0,
                "issues": symptom_issues
            },
            "root_cause_quality": {
                "status_distribution": root_cause_status_dist,
                "cards_with_root_cause": sum(1 for c in llm_issue_cards if c.get("root_cause")),
                "issues": root_cause_issues
            },
            "fix_quality": {
                "total_fixes": fix_count,
                "fixes_with_snippets": fix_with_snippets,
                "snippet_rate": fix_with_snippets / fix_count if fix_count > 0 else 0,
                "issues": fix_issues
            },
            "validation_quality": {
                "total_validations": validation_count,
                "avg_per_card": validation_count / len(llm_issue_cards) if llm_issue_cards else 0,
                "issues": validation_issues
            }
        },
        "comparison": comparison,
        "recommendations": []
    }

    # 개선 권장사항 생성
    if root_cause_issues:
        analysis_result["recommendations"].append({
            "category": "root_cause_quality",
            "priority": "high",
            "message": f"{len(root_cause_issues)}개 Issue Card의 Root cause 품질 개선 필요",
            "details": root_cause_issues[:5]
        })

    if symptom_avg_length > 300:
        analysis_result["recommendations"].append({
            "category": "symptom_quality",
            "priority": "medium",
            "message": f"Symptom 평균 길이가 너무 김 ({symptom_avg_length:.1f}자)",
            "details": symptom_issues[:3]
        })

    if fix_count == 0:
        analysis_result["recommendations"].append({
            "category": "fix_quality",
            "priority": "high",
            "message": "Fix가 없는 Issue Card가 있음",
            "details": []
        })

    if comparison and comparison["symptom_avg_length"]["improvement"]:
        analysis_result["recommendations"].append({
            "category": "improvement",
            "priority": "low",
            "message": "LLM 기반 Symptom 추출이 패턴 기반보다 개선됨",
            "details": []
        })

    return analysis_result


def main():
    """메인 함수"""
    import sys

    # 결과 파일 경로
    if len(sys.argv) > 1:
        llm_result_file = Path(sys.argv[1])
    else:
        # 기본값: 최신 LLM 결과 파일
        llm_result_file = Path(__file__).parent.parent / "tests" / "results" / "timeline_issues_e2e_llm_20251226_134343.json"

    if not llm_result_file.exists():
        print(f"[ERROR] LLM 결과 파일을 찾을 수 없습니다: {llm_result_file}")
        sys.exit(1)

    # 패턴 기반 결과 파일 (비교용, 선택적)
    pattern_result_file = None
    if len(sys.argv) > 2:
        pattern_result_file = Path(sys.argv[2])
    else:
        # 기본값: 이전 패턴 기반 결과 파일
        pattern_file = Path(__file__).parent.parent / "tests" / "results" / "timeline_issues_e2e_llm_20251226_132153.json"
        if pattern_file.exists():
            pattern_result_file = pattern_file

    # 분석 실행
    print(f"[INFO] Issue Card 품질 분석 시작: {llm_result_file}")
    analysis_result = analyze_issue_card_quality(llm_result_file, pattern_result_file)

    # 리포트 저장
    reports_dir = Path(__file__).parent.parent / "tests" / "reports"
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / "issue_card_quality_analysis.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(analysis_result, f, ensure_ascii=False, indent=2)

    print(f"[INFO] 분석 리포트 저장 완료: {report_file}")

    # 요약 출력
    summary = analysis_result["summary"]
    print("\n" + "="*60)
    print("Issue Card 품질 분석 결과")
    print("="*60)
    print(f"총 Issue Card 수: {summary['total_issue_cards']}")
    print(f"품질 점수: {summary['quality_score']:.1f}/100")
    print(f"발견된 문제 수: {summary['total_issues']}")
    print("="*60)

    # 주요 지표 출력
    metrics = analysis_result["metrics"]
    print("\n[주요 지표]")
    print(f"- Symptom 평균 길이: {metrics['symptom_quality']['avg_length']:.1f}자")
    print(f"- Root cause 포함 카드: {metrics['root_cause_quality']['cards_with_root_cause']}/{summary['total_issue_cards']}")
    print(f"  - Confirmed: {metrics['root_cause_quality']['status_distribution']['confirmed']}")
    print(f"  - Hypothesis: {metrics['root_cause_quality']['status_distribution']['hypothesis']}")
    print(f"- Fix 총 개수: {metrics['fix_quality']['total_fixes']}")
    print(f"- Fix with snippets: {metrics['fix_quality']['fixes_with_snippets']} ({metrics['fix_quality']['snippet_rate']:.1%})")
    print(f"- Validation 총 개수: {metrics['validation_quality']['total_validations']}")

    # 비교 결과 출력
    if analysis_result["comparison"]:
        print("\n[패턴 기반과 비교]")
        comp = analysis_result["comparison"]
        print(f"- Symptom 평균 길이: LLM {comp['symptom_avg_length']['llm']:.1f}자 vs 패턴 {comp['symptom_avg_length']['pattern']:.1f}자")
        if comp['symptom_avg_length']['improvement']:
            print("  [OK] LLM 기반 추출이 더 간결함 (개선됨)")
        else:
            print("  [WARNING] LLM 기반 추출이 더 김 (개선 필요)")

    # 권장사항 출력
    if analysis_result["recommendations"]:
        print("\n[개선 권장사항]")
        for rec in analysis_result["recommendations"]:
            print(f"- [{rec['priority'].upper()}] {rec['message']}")


if __name__ == "__main__":
    main()

