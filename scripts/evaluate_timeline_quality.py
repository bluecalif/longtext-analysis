"""
Timeline Section 품질 평가 스크립트

E2E 테스트 결과 파일을 분석하여 Timeline Section 품질을 평가합니다.
"""

import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime
from collections import defaultdict


def evaluate_timeline_sections(result_file: Path) -> Dict[str, Any]:
    """
    Timeline Section 품질 평가

    Args:
        result_file: E2E 테스트 결과 JSON 파일 경로

    Returns:
        평가 결과 딕셔너리
    """
    # 결과 파일 로드
    with open(result_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    timeline_sections = data.get("timeline_sections", [])
    issue_cards = data.get("issue_cards", [])
    events = data.get("events", [])

    if not timeline_sections:
        return {
            "error": "Timeline sections not found in result file",
            "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S")
        }

    # 1. 기본 통계
    total_sections = len(timeline_sections)
    sections_with_issues = sum(1 for s in timeline_sections if s.get("has_issues", False))
    sections_with_issue_refs = sum(1 for s in timeline_sections if s.get("issue_refs"))

    # 2. 제목 품질 분석
    title_lengths = [len(s.get("title", "")) for s in timeline_sections]
    title_avg_length = sum(title_lengths) / len(title_lengths) if title_lengths else 0
    title_min_length = min(title_lengths) if title_lengths else 0
    title_max_length = max(title_lengths) if title_lengths else 0

    # 제목 품질 문제 탐지
    title_issues = []
    for i, section in enumerate(timeline_sections):
        title = section.get("title", "")
        if len(title) < 5:
            title_issues.append({
                "section_id": section.get("section_id"),
                "issue": "제목이 너무 짧음",
                "title": title,
                "length": len(title)
            })
        elif len(title) > 100:
            title_issues.append({
                "section_id": section.get("section_id"),
                "issue": "제목이 너무 김",
                "title": title,
                "length": len(title)
            })
        # 제목이 이벤트 타입만 나열하는 경우 (예: "status_review 작업")
        if "작업" in title and len(title.split()) <= 3:
            title_issues.append({
                "section_id": section.get("section_id"),
                "issue": "제목이 너무 일반적임 (이벤트 타입만 나열)",
                "title": title
            })

    # 3. 요약 품질 분석
    summary_lengths = [len(s.get("summary", "")) for s in timeline_sections]
    summary_avg_length = sum(summary_lengths) / len(summary_lengths) if summary_lengths else 0
    summary_min_length = min(summary_lengths) if summary_lengths else 0
    summary_max_length = max(summary_lengths) if summary_lengths else 0

    # 요약 품질 문제 탐지
    summary_issues = []
    for i, section in enumerate(timeline_sections):
        summary = section.get("summary", "")
        if len(summary) < 20:
            summary_issues.append({
                "section_id": section.get("section_id"),
                "issue": "요약이 너무 짧음",
                "summary": summary[:100],
                "length": len(summary)
            })
        elif len(summary) > 500:
            summary_issues.append({
                "section_id": section.get("section_id"),
                "issue": "요약이 너무 김 (500자 초과)",
                "summary": summary[:100],
                "length": len(summary)
            })
        # 요약이 중간에 잘린 경우 (500자 제한)
        if len(summary) == 500 and not summary.endswith((".", "!", "?", "다", "요", "니다")):
            summary_issues.append({
                "section_id": section.get("section_id"),
                "issue": "요약이 중간에 잘림 (500자 제한)",
                "summary": summary[-50:],
                "length": len(summary)
            })

    # 4. 이슈 연결 정확성 분석
    issue_refs_all = []
    for section in timeline_sections:
        issue_refs_all.extend(section.get("issue_refs", []))

    unique_issue_refs = set(issue_refs_all)
    issue_connection_rate = len(unique_issue_refs) / len(issue_cards) if issue_cards else 0

    # 이슈 연결 문제 탐지
    issue_connection_issues = []
    for section in timeline_sections:
        section_issue_refs = section.get("issue_refs", [])
        if section.get("has_issues") and not section_issue_refs:
            issue_connection_issues.append({
                "section_id": section.get("section_id"),
                "issue": "has_issues가 True인데 issue_refs가 비어있음"
            })
        # issue_refs에 있는 이슈가 실제로 존재하는지 확인
        for issue_ref in section_issue_refs:
            issue_exists = any(card.get("issue_id") == issue_ref for card in issue_cards)
            if not issue_exists:
                issue_connection_issues.append({
                    "section_id": section.get("section_id"),
                    "issue": f"issue_refs에 존재하지 않는 이슈 ID 포함: {issue_ref}"
                })

    # 5. 작업 결과 연결 정보 완성도 분석
    sections_with_code_snippets = sum(
        1 for s in timeline_sections
        if s.get("detailed_results", {}).get("code_snippets")
    )
    sections_with_files = sum(
        1 for s in timeline_sections
        if s.get("detailed_results", {}).get("files")
    )
    sections_with_artifacts = sum(
        1 for s in timeline_sections
        if s.get("detailed_results", {}).get("artifacts")
    )

    # 작업 결과 연결 정보 품질 분석
    detailed_results_issues = []
    for section in timeline_sections:
        detailed_results = section.get("detailed_results", {})
        code_snippets = detailed_results.get("code_snippets", [])
        files = detailed_results.get("files", [])
        artifacts = detailed_results.get("artifacts", [])

        # 코드 생성 섹션인데 코드 스니펫이 없는 경우
        if "code_generation" in section.get("title", "").lower() and not code_snippets:
            detailed_results_issues.append({
                "section_id": section.get("section_id"),
                "issue": "코드 생성 작업인데 코드 스니펫이 없음",
                "title": section.get("title")
            })

        # Artifact 중복 제거 필요 여부 확인
        artifact_paths = [a.get("path", "") for a in artifacts if isinstance(a, dict)]
        if len(artifact_paths) != len(set(artifact_paths)):
            detailed_results_issues.append({
                "section_id": section.get("section_id"),
                "issue": "Artifact에 중복된 경로가 있음",
                "duplicate_paths": [p for p in artifact_paths if artifact_paths.count(p) > 1]
            })

    # 6. 이벤트 그룹화 품질 분석
    event_coverage = []
    all_event_seqs = set()
    for section in timeline_sections:
        section_events = section.get("events", [])
        all_event_seqs.update(section_events)
        event_coverage.append({
            "section_id": section.get("section_id"),
            "event_count": len(section_events),
            "events": section_events
        })

    total_events = len(events)
    coverage_rate = len(all_event_seqs) / total_events if total_events > 0 else 0

    # 이벤트 중복 확인
    event_duplicates = []
    event_section_map = defaultdict(list)
    for section in timeline_sections:
        for event_seq in section.get("events", []):
            event_section_map[event_seq].append(section.get("section_id"))

    for event_seq, section_ids in event_section_map.items():
        if len(section_ids) > 1:
            event_duplicates.append({
                "event_seq": event_seq,
                "sections": section_ids,
                "issue": "이벤트가 여러 섹션에 중복 포함됨"
            })

    # 7. 종합 평가
    total_issues = (
        len(title_issues) +
        len(summary_issues) +
        len(issue_connection_issues) +
        len(detailed_results_issues) +
        len(event_duplicates)
    )

    quality_score = max(0, 100 - (total_issues * 5))  # 이슈당 5점 감점

    # 평가 결과 구성
    evaluation_result = {
        "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "input_file": str(result_file),
        "test_name": data.get("test_metadata", {}).get("test_name", "unknown"),
        "summary": {
            "total_sections": total_sections,
            "total_events": total_events,
            "total_issue_cards": len(issue_cards),
            "quality_score": quality_score,
            "total_issues": total_issues
        },
        "metrics": {
            "sections_with_issues": {
                "count": sections_with_issues,
                "rate": sections_with_issues / total_sections if total_sections > 0 else 0
            },
            "sections_with_issue_refs": {
                "count": sections_with_issue_refs,
                "rate": sections_with_issue_refs / total_sections if total_sections > 0 else 0
            },
            "title_quality": {
                "avg_length": title_avg_length,
                "min_length": title_min_length,
                "max_length": title_max_length,
                "issues": title_issues
            },
            "summary_quality": {
                "avg_length": summary_avg_length,
                "min_length": summary_min_length,
                "max_length": summary_max_length,
                "issues": summary_issues
            },
            "issue_connection": {
                "connection_rate": issue_connection_rate,
                "unique_issue_refs": len(unique_issue_refs),
                "total_issue_cards": len(issue_cards),
                "issues": issue_connection_issues
            },
            "detailed_results": {
                "sections_with_code_snippets": sections_with_code_snippets,
                "sections_with_files": sections_with_files,
                "sections_with_artifacts": sections_with_artifacts,
                "code_snippets_rate": sections_with_code_snippets / total_sections if total_sections > 0 else 0,
                "files_rate": sections_with_files / total_sections if total_sections > 0 else 0,
                "artifacts_rate": sections_with_artifacts / total_sections if total_sections > 0 else 0,
                "issues": detailed_results_issues
            },
            "event_coverage": {
                "coverage_rate": coverage_rate,
                "covered_events": len(all_event_seqs),
                "total_events": total_events,
                "event_duplicates": event_duplicates
            }
        },
        "section_details": [
            {
                "section_id": s.get("section_id"),
                "title": s.get("title"),
                "title_length": len(s.get("title", "")),
                "summary_length": len(s.get("summary", "")),
                "event_count": len(s.get("events", [])),
                "has_issues": s.get("has_issues", False),
                "issue_refs_count": len(s.get("issue_refs", [])),
                "code_snippets_count": len(s.get("detailed_results", {}).get("code_snippets", [])),
                "files_count": len(s.get("detailed_results", {}).get("files", [])),
                "artifacts_count": len(s.get("detailed_results", {}).get("artifacts", []))
            }
            for s in timeline_sections
        ],
        "recommendations": []
    }

    # 개선 권장사항 생성
    if title_issues:
        evaluation_result["recommendations"].append({
            "category": "title_quality",
            "priority": "high",
            "message": f"{len(title_issues)}개 섹션의 제목 품질 개선 필요",
            "details": title_issues[:5]  # 상위 5개만
        })

    if summary_issues:
        evaluation_result["recommendations"].append({
            "category": "summary_quality",
            "priority": "high",
            "message": f"{len(summary_issues)}개 섹션의 요약 품질 개선 필요",
            "details": summary_issues[:5]  # 상위 5개만
        })

    if issue_connection_rate < 0.5:
        evaluation_result["recommendations"].append({
            "category": "issue_connection",
            "priority": "medium",
            "message": f"이슈 연결률이 낮음 ({issue_connection_rate:.1%})",
            "details": issue_connection_issues[:5]
        })

    if coverage_rate < 0.9:
        evaluation_result["recommendations"].append({
            "category": "event_coverage",
            "priority": "medium",
            "message": f"이벤트 커버리지가 낮음 ({coverage_rate:.1%})",
            "details": event_duplicates[:5]
        })

    if event_duplicates:
        evaluation_result["recommendations"].append({
            "category": "event_duplication",
            "priority": "low",
            "message": f"{len(event_duplicates)}개 이벤트가 여러 섹션에 중복 포함됨",
            "details": event_duplicates[:5]
        })

    return evaluation_result


def main():
    """메인 함수"""
    import sys

    # 결과 파일 경로
    if len(sys.argv) > 1:
        result_file = Path(sys.argv[1])
    else:
        # 기본값: 최신 E2E 테스트 결과 파일
        results_dir = Path(__file__).parent.parent / "tests" / "timeline_issues_e2e_llm_20251226_130658.json"
        result_file = results_dir

    if not result_file.exists():
        print(f"[ERROR] 결과 파일을 찾을 수 없습니다: {result_file}")
        sys.exit(1)

    # 평가 실행
    print(f"[INFO] Timeline Section 품질 평가 시작: {result_file}")
    evaluation_result = evaluate_timeline_sections(result_file)

    # 리포트 저장
    reports_dir = Path(__file__).parent.parent / "tests" / "reports"
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / "timeline_quality_evaluation.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(evaluation_result, f, ensure_ascii=False, indent=2)

    print(f"[INFO] 평가 리포트 저장 완료: {report_file}")

    # 요약 출력
    summary = evaluation_result["summary"]
    print("\n" + "="*60)
    print("Timeline Section 품질 평가 결과")
    print("="*60)
    print(f"총 섹션 수: {summary['total_sections']}")
    print(f"총 이벤트 수: {summary['total_events']}")
    print(f"총 이슈 카드 수: {summary['total_issue_cards']}")
    print(f"품질 점수: {summary['quality_score']:.1f}/100")
    print(f"발견된 문제 수: {summary['total_issues']}")
    print("="*60)

    # 주요 지표 출력
    metrics = evaluation_result["metrics"]
    print("\n[주요 지표]")
    print(f"- 이슈 연결률: {metrics['issue_connection']['connection_rate']:.1%}")
    print(f"- 이벤트 커버리지: {metrics['event_coverage']['coverage_rate']:.1%}")
    print(f"- 제목 평균 길이: {metrics['title_quality']['avg_length']:.1f}자")
    print(f"- 요약 평균 길이: {metrics['summary_quality']['avg_length']:.1f}자")
    print(f"- 코드 스니펫 포함 섹션 비율: {metrics['detailed_results']['code_snippets_rate']:.1%}")

    # 권장사항 출력
    if evaluation_result["recommendations"]:
        print("\n[개선 권장사항]")
        for rec in evaluation_result["recommendations"]:
            print(f"- [{rec['priority'].upper()}] {rec['message']}")


if __name__ == "__main__":
    main()

