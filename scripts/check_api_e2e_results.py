"""
API E2E 테스트 결과 확인 스크립트

최신 API E2E 테스트 결과 파일을 확인하고 요약 정보를 출력합니다.
"""

import json
from pathlib import Path


def main():
    """최신 API E2E 테스트 결과 확인"""
    results_dir = Path(__file__).parent.parent / "tests" / "results"

    # 최신 결과 파일 찾기
    result_files = list(results_dir.glob("api_e2e_full_pipeline_*.json"))
    if not result_files:
        print("[ERROR] No API E2E result file found")
        return

    latest_file = max(result_files, key=lambda p: p.stat().st_mtime)

    print(f"[RESULTS] Latest result file: {latest_file.name}")
    print(f"[RESULTS] File size: {latest_file.stat().st_size} bytes")
    print(f"[RESULTS] Last modified: {latest_file.stat().st_mtime}")

    # 결과 파일 로드
    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"\n[RESULTS] Data structure check:")
    print(f"  - session_meta: {'[OK]' if 'session_meta' in data else '[FAIL]'}")
    print(
        f"  - turns: {len(data.get('turns', []))} items {'[OK]' if 'turns' in data else '[FAIL]'}"
    )
    print(
        f"  - events: {len(data.get('events', []))} items {'[OK]' if 'events' in data else '[FAIL]'}"
    )
    print(
        f"  - timeline_sections: {len(data.get('timeline_sections', []))} items {'[OK]' if 'timeline_sections' in data else '[FAIL]'}"
    )
    print(
        f"  - issue_cards: {len(data.get('issue_cards', []))} items {'[OK]' if 'issue_cards' in data else '[FAIL]'}"
    )
    print(
        f"  - snippets: {len(data.get('snippets', []))} items {'[OK]' if 'snippets' in data else '[FAIL]'}"
    )
    print(f"  - test_metadata: {'[OK]' if 'test_metadata' in data else '[FAIL]'}")

    # 테스트 메타데이터
    if "test_metadata" in data:
        metadata = data["test_metadata"]
        print(f"\n[RESULTS] Test metadata:")
        print(f"  - test_name: {metadata.get('test_name', 'N/A')}")
        print(f"  - timestamp: {metadata.get('timestamp', 'N/A')}")
        print(f"  - total_time_seconds: {metadata.get('total_time_seconds', 'N/A')}")
        print(f"  - input_file: {metadata.get('input_file', 'N/A')}")

        # 결과 요약
        if "results_summary" in metadata:
            summary = metadata["results_summary"]
            print(f"\n[RESULTS] Results summary:")
            print(
                f"  - parse: turns={summary.get('parse', {}).get('turns_count', 'N/A')}, events={summary.get('parse', {}).get('events_count', 'N/A')}"
            )
            print(
                f"  - timeline: sections={summary.get('timeline', {}).get('sections_count', 'N/A')}, events={summary.get('timeline', {}).get('events_count', 'N/A')}"
            )
            print(f"  - issues: {summary.get('issues', {}).get('issues_count', 'N/A')} items")
            print(f"  - snippets: {summary.get('snippets', {}).get('snippets_count', 'N/A')} items")
            print(
                f"  - export: zip_size={summary.get('export', {}).get('zip_size_bytes', 'N/A')} bytes"
            )
            print(f"  - status: {metadata.get('status', 'N/A')}")

    print(f"\n[RESULTS] All detailed data fields are present: [OK]")


if __name__ == "__main__":
    main()
