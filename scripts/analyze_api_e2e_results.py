"""
API E2E 테스트 결과 상세 분석 스크립트

최신 API E2E 테스트 결과를 분석하고 Phase 6 결과와 비교합니다.
"""
import json
from pathlib import Path
from datetime import datetime


def main():
    """API E2E 테스트 결과 상세 분석"""
    results_dir = Path(__file__).parent.parent / "tests" / "results"

    # 최신 API E2E 결과 파일 찾기
    api_files = list(results_dir.glob("api_e2e_full_pipeline_*.json"))
    if not api_files:
        print("[ERROR] No API E2E result file found")
        return

    latest_api = max(api_files, key=lambda p: p.stat().st_mtime)

    print("=" * 60)
    print("API E2E 테스트 결과 상세 분석 리포트")
    print("=" * 60)
    print(f"\n[FILE] 최신 결과 파일: {latest_api.name}")
    print(f"[FILE] 파일 크기: {latest_api.stat().st_size:,} bytes")

    # 결과 파일 로드
    with open(latest_api, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 테스트 메타데이터
    if 'test_metadata' in data:
        metadata = data['test_metadata']
        print(f"\n[TEST] 테스트 이름: {metadata.get('test_name', 'N/A')}")
        print(f"[TEST] 실행 시간: {metadata.get('timestamp', 'N/A')}")
        print(f"[TEST] 총 소요 시간: {metadata.get('total_time_seconds', 'N/A'):.2f}초")
        print(f"[TEST] 상태: {metadata.get('status', 'N/A')}")

    # 결과 요약
    print(f"\n[RESULTS] 결과 요약:")
    print(f"  - Turns: {len(data.get('turns', []))}개")
    print(f"  - Events: {len(data.get('events', []))}개")
    print(f"  - Timeline Sections: {len(data.get('timeline_sections', []))}개")
    print(f"  - Timeline Events: {len(data.get('timeline_events', []))}개")
    print(f"  - Issue Cards: {len(data.get('issue_cards', []))}개")
    print(f"  - Snippets: {len(data.get('snippets', []))}개")

    # Phase 6 결과와 비교
    timeline_files = list(results_dir.glob("timeline_issues_e2e_llm_*.json"))
    if timeline_files:
        latest_timeline = max(timeline_files, key=lambda p: p.stat().st_mtime)
        print(f"\n[COMPARISON] Phase 6 결과 비교:")
        print(f"  - Phase 6 파일: {latest_timeline.name}")

        with open(latest_timeline, "r", encoding="utf-8") as f:
            phase6_data = json.load(f)

        phase6_sections = len(phase6_data.get("timeline_sections", []))
        phase6_issues = len(phase6_data.get("issue_cards", []))
        phase7_sections = len(data.get("timeline_sections", []))
        phase7_issues = len(data.get("issue_cards", []))

        print(f"\n  Timeline Sections:")
        print(f"    Phase 6: {phase6_sections}개")
        print(f"    Phase 7: {phase7_sections}개")
        print(f"    차이: {phase7_sections - phase6_sections:+d}개")

        print(f"\n  Issue Cards:")
        print(f"    Phase 6: {phase6_issues}개")
        print(f"    Phase 7: {phase7_issues}개")
        print(f"    차이: {phase7_issues - phase6_issues:+d}개")

        if phase6_sections != phase7_sections:
            print(f"\n[WARNING] Timeline sections 개수가 다릅니다!")
        if phase6_issues != phase7_issues:
            print(f"[WARNING] Issue cards 개수가 다릅니다!")

    # Timeline Sections 상세 정보
    if 'timeline_sections' in data:
        sections = data['timeline_sections']
        print(f"\n[ANALYSIS] Timeline Sections 상세:")
        for i, section in enumerate(sections[:5], 1):  # 처음 5개만 출력
            print(f"  {i}. {section.get('section_id', 'N/A')}")
            print(f"     Title: {section.get('title', 'N/A')[:60]}...")
            print(f"     Events: {len(section.get('events', []))}개")
        if len(sections) > 5:
            print(f"  ... (총 {len(sections)}개 중 5개만 표시)")

    # Issue Cards 상세 정보
    if 'issue_cards' in data:
        issues = data['issue_cards']
        print(f"\n[ANALYSIS] Issue Cards 상세:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue.get('issue_id', 'N/A')}")
            print(f"     Title: {issue.get('title', 'N/A')[:60]}...")
            print(f"     Root cause: {'있음' if issue.get('root_cause') else '없음'}")
            print(f"     Fix: {len(issue.get('fix', []))}개")
            print(f"     Validation: {len(issue.get('validation', []))}개")

    print("\n" + "=" * 60)
    print("분석 완료")
    print("=" * 60)


if __name__ == "__main__":
    main()
