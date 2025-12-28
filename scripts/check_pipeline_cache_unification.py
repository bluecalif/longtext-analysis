"""
Pipeline Cache 통일 검증 스크립트

Phase 7.11 완료 후 검증:
1. pipeline_cache 파일 확인
2. 캐시 통계 확인
3. 최신 테스트 결과 비교
"""

import json
from pathlib import Path
from datetime import datetime

# 프로젝트 루트
PROJECT_ROOT = Path(__file__).parent.parent
CACHE_DIR = PROJECT_ROOT / "cache" / "pipeline"
RESULTS_DIR = PROJECT_ROOT / "tests" / "results"


def check_pipeline_cache_files():
    """pipeline_cache 파일 확인"""
    print("=" * 60)
    print("Pipeline Cache 파일 확인")
    print("=" * 60)

    if not CACHE_DIR.exists():
        print(f"[WARNING] Cache directory does not exist: {CACHE_DIR}")
        return

    cache_files = list(CACHE_DIR.glob("*.json"))
    print(f"캐시 파일 수: {len(cache_files)}")

    # 타입별 분류
    cache_types = {
        "parsed": [],
        "events": [],
        "timeline_sections": [],
        "issue_cards": [],
    }

    for cache_file in cache_files:
        if cache_file.name.startswith("parsed_"):
            cache_types["parsed"].append(cache_file)
        elif cache_file.name.startswith("events_"):
            cache_types["events"].append(cache_file)
        elif cache_file.name.startswith("timeline_sections_"):
            cache_types["timeline_sections"].append(cache_file)
        elif cache_file.name.startswith("issue_cards_"):
            cache_types["issue_cards"].append(cache_file)

    print("\n타입별 캐시 파일 수:")
    for cache_type, files in cache_types.items():
        print(f"  - {cache_type}: {len(files)}개")
        if files:
            print(f"    예시: {files[0].name[:50]}...")

    return cache_types


def get_latest_test_results():
    """최신 테스트 결과 파일 찾기"""
    print("\n" + "=" * 60)
    print("최신 테스트 결과 확인")
    print("=" * 60)

    result_files = list(RESULTS_DIR.glob("*_e2e_*.json"))
    if not result_files:
        print("[WARNING] Test result files not found")
        return None

    # 최신 파일 찾기
    latest_file = max(result_files, key=lambda f: f.stat().st_mtime)
    print(f"최신 결과 파일: {latest_file.name}")
    print(f"수정 시간: {datetime.fromtimestamp(latest_file.stat().st_mtime)}")

    return latest_file


def analyze_test_result(result_file):
    """테스트 결과 분석"""
    if not result_file:
        return

    print("\n" + "=" * 60)
    print("테스트 결과 분석")
    print("=" * 60)

    with open(result_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 테스트 메타데이터
    test_metadata = data.get("test_metadata", {})
    print(f"\n테스트 이름: {test_metadata.get('test_name', 'unknown')}")
    print(f"타임스탬프: {test_metadata.get('timestamp', 'unknown')}")

    # 결과 요약
    results_summary = test_metadata.get("results_summary", {})
    if results_summary:
        print("\n결과 요약:")
        for key, value in results_summary.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for sub_key, sub_value in value.items():
                    print(f"    - {sub_key}: {sub_value}")
            else:
                print(f"  {key}: {value}")

    # 데이터 구조 확인
    print("\n데이터 구조:")
    if "session_meta" in data:
        print("  - session_meta: OK")
    if "turns" in data:
        print(f"  - turns: {len(data['turns'])}개")
    if "events" in data:
        print(f"  - events: {len(data['events'])}개")
    if "timeline_sections" in data:
        print(f"  - timeline_sections: {len(data['timeline_sections'])}개")
    if "issue_cards" in data:
        print(f"  - issue_cards: {len(data['issue_cards'])}개")
    if "snippets" in data:
        print(f"  - snippets: {len(data['snippets'])}개")


def main():
    """메인 함수"""
    print("\n" + "=" * 60)
    print("Pipeline Cache 통일 검증")
    print("=" * 60)

    # 1. pipeline_cache 파일 확인
    cache_types = check_pipeline_cache_files()

    # 2. 최신 테스트 결과 확인
    latest_result = get_latest_test_results()

    # 3. 테스트 결과 분석
    analyze_test_result(latest_result)

    print("\n" + "=" * 60)
    print("검증 완료")
    print("=" * 60)


if __name__ == "__main__":
    main()

