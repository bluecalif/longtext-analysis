"""
Phase 6 vs Phase 7 결과 일관성 비교 스크립트
"""

import json
from pathlib import Path

RESULTS_DIR = Path(__file__).parent.parent / "tests" / "results"


def find_latest_files():
    """최신 Phase 6와 Phase 7 결과 파일 찾기"""
    phase6_file = None
    phase7_file = None

    # Phase 6: timeline_issues_e2e_llm (fixture 사용)
    phase6_files = list(RESULTS_DIR.glob("timeline_issues_e2e_llm_*.json"))
    if phase6_files:
        phase6_file = max(phase6_files, key=lambda f: f.stat().st_mtime)

    # Phase 7: api_e2e_full_pipeline
    phase7_files = list(RESULTS_DIR.glob("api_e2e_full_pipeline_*.json"))
    if phase7_files:
        phase7_file = max(phase7_files, key=lambda f: f.stat().st_mtime)

    return phase6_file, phase7_file


def extract_key_metrics(data):
    """주요 메트릭 추출"""
    metrics = {}

    # timeline_sections
    if "timeline_sections" in data:
        metrics["timeline_sections_count"] = len(data["timeline_sections"])
    elif "results" in data and "total_timeline_sections" in data["results"]:
        metrics["timeline_sections_count"] = data["results"]["total_timeline_sections"]

    # issue_cards
    if "issue_cards" in data:
        metrics["issue_cards_count"] = len(data["issue_cards"])
    elif "results" in data and "total_issue_cards" in data["results"]:
        metrics["issue_cards_count"] = data["results"]["total_issue_cards"]

    # events
    if "events" in data:
        metrics["events_count"] = len(data["events"])
    elif "results" in data and "total_events" in data["results"]:
        metrics["events_count"] = data["results"]["total_events"]

    # turns
    if "turns" in data:
        metrics["turns_count"] = len(data["turns"])
    elif "results" in data and "total_turns" in data["results"]:
        metrics["turns_count"] = data["results"]["total_turns"]

    return metrics


def compare_results():
    """결과 비교"""
    print("=" * 60)
    print("Phase 6 vs Phase 7 결과 일관성 비교")
    print("=" * 60)

    phase6_file, phase7_file = find_latest_files()

    if not phase6_file:
        print("[WARNING] Phase 6 결과 파일을 찾을 수 없습니다")
        return

    if not phase7_file:
        print("[WARNING] Phase 7 결과 파일을 찾을 수 없습니다")
        return

    print(f"\nPhase 6 파일: {phase6_file.name}")
    print(f"Phase 7 파일: {phase7_file.name}")

    # 파일 읽기
    with open(phase6_file, "r", encoding="utf-8") as f:
        phase6_data = json.load(f)

    with open(phase7_file, "r", encoding="utf-8") as f:
        phase7_data = json.load(f)

    # 메트릭 추출
    phase6_metrics = extract_key_metrics(phase6_data)
    phase7_metrics = extract_key_metrics(phase7_data)

    # 비교
    print("\n" + "=" * 60)
    print("메트릭 비교")
    print("=" * 60)

    all_keys = set(phase6_metrics.keys()) | set(phase7_metrics.keys())
    consistent = True

    for key in sorted(all_keys):
        phase6_value = phase6_metrics.get(key, "N/A")
        phase7_value = phase7_metrics.get(key, "N/A")

        if phase6_value == phase7_value:
            status = "[OK]"
        else:
            status = "[DIFF]"
            consistent = False

        phase6_str = str(phase6_value)
        phase7_str = str(phase7_value)
        print(f"{key:30s} Phase 6: {phase6_str:10s} Phase 7: {phase7_str:10s} {status}")

    print("\n" + "=" * 60)
    if consistent:
        print("결과: 일관성 있음 (모든 메트릭이 일치)")
    else:
        print("결과: 차이 발견 (일부 메트릭이 다름)")
    print("=" * 60)

    return consistent


if __name__ == "__main__":
    compare_results()

