"""Phase 6와 Phase 7 E2E 테스트 결과 비교 스크립트"""

import json
from pathlib import Path


def main():
    """Phase 6와 Phase 7 E2E 테스트 결과 비교"""
    results_dir = Path(__file__).parent.parent / "tests" / "results"

    # 최신 Timeline E2E 결과 파일 찾기 (Phase 6)
    timeline_files = list(results_dir.glob("timeline_issues_e2e_llm_*.json"))
    if timeline_files:
        latest_timeline = max(timeline_files, key=lambda p: p.stat().st_mtime)
        print(f"[Phase 6] Latest timeline file: {latest_timeline.name}")

        with open(latest_timeline, "r", encoding="utf-8") as f:
            timeline_data = json.load(f)

        phase6_sections = len(timeline_data.get("timeline_sections", []))
        phase6_issues = len(timeline_data.get("issue_cards", []))
        print(f"[Phase 6] Timeline sections: {phase6_sections}")
        print(f"[Phase 6] Issue cards: {phase6_issues}")
    else:
        phase6_sections = None
        phase6_issues = None
        print("[Phase 6] No timeline E2E result file found")

    # 최신 API E2E 결과 파일 찾기 (Phase 7)
    api_files = list(results_dir.glob("api_e2e_full_pipeline_*.json"))
    if api_files:
        latest_api = max(api_files, key=lambda p: p.stat().st_mtime)
        print(f"\n[Phase 7] Latest API E2E file: {latest_api.name}")

        with open(latest_api, "r", encoding="utf-8") as f:
            api_data = json.load(f)

        phase7_sections = len(api_data.get("timeline_sections", []))
        phase7_issues = len(api_data.get("issue_cards", []))
        print(f"[Phase 7] Timeline sections: {phase7_sections}")
        print(f"[Phase 7] Issue cards: {phase7_issues}")

        # 비교
        if phase6_sections is not None:
            print(
                f"\n[Comparison] Timeline sections: Phase 6={phase6_sections} vs Phase 7={phase7_sections} (diff: {phase7_sections - phase6_sections})"
            )
            print(
                f"[Comparison] Issue cards: Phase 6={phase6_issues} vs Phase 7={phase7_issues} (diff: {phase7_issues - phase6_issues})"
            )


if __name__ == "__main__":
    main()
