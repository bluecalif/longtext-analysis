"""서버 로그 분석 스크립트"""
from pathlib import Path
import re


def main():
    """서버 로그 분석"""
    logs_dir = Path(__file__).parent.parent / "tests" / "logs"

    # 최신 서버 로그 파일 찾기
    server_logs = list(logs_dir.glob("server_*.log"))
    if not server_logs:
        print("[ERROR] No server log file found")
        return

    latest_log = max(server_logs, key=lambda p: p.stat().st_mtime)

    print("=" * 60)
    print("서버 로그 분석 리포트")
    print("=" * 60)
    print(f"\n[FILE] 최신 서버 로그: {latest_log.name}")
    print(f"[FILE] 파일 크기: {latest_log.stat().st_size:,} bytes")

    # 로그 파일 읽기
    with open(latest_log, "r", encoding="utf-8") as f:
        content = f.read()

    # 패턴 매칭
    cache_hits = len(re.findall(r"\[CACHE HIT\]", content))
    cache_misses = len(re.findall(r"\[CACHE MISS\]", content))
    cache_saves = len(re.findall(r"\[CACHE SAVE\]", content))

    parse_api_logs = len(re.findall(r"\[PARSE API\]", content))
    timeline_api_logs = len(re.findall(r"\[TIMELINE API\]", content))
    issues_api_logs = len(re.findall(r"\[ISSUES API\]", content))

    print(f"\n[LLM Cache]")
    print(f"  - CACHE HIT: {cache_hits}회")
    print(f"  - CACHE MISS: {cache_misses}회")
    print(f"  - CACHE SAVE: {cache_saves}회")

    print(f"\n[API Logs]")
    print(f"  - PARSE API: {parse_api_logs}회")
    print(f"  - TIMELINE API: {timeline_api_logs}회")
    print(f"  - ISSUES API: {issues_api_logs}회")

    # 로그 샘플 출력
    print(f"\n[LOG SAMPLES]")

    # CACHE HIT 샘플
    cache_hit_lines = re.findall(r".*\[CACHE HIT\].*", content)
    if cache_hit_lines:
        print(f"\n  CACHE HIT 샘플 (최대 5개):")
        for line in cache_hit_lines[:5]:
            print(f"    {line.strip()[:100]}")

    # CACHE MISS 샘플
    cache_miss_lines = re.findall(r".*\[CACHE MISS\].*", content)
    if cache_miss_lines:
        print(f"\n  CACHE MISS 샘플 (최대 5개):")
        for line in cache_miss_lines[:5]:
            print(f"    {line.strip()[:100]}")

    # API 로그 샘플
    parse_api_lines = re.findall(r".*\[PARSE API\].*", content)
    if parse_api_lines:
        print(f"\n  PARSE API 로그:")
        for line in parse_api_lines:
            print(f"    {line.strip()}")

    timeline_api_lines = re.findall(r".*\[TIMELINE API\].*", content)
    if timeline_api_lines:
        print(f"\n  TIMELINE API 로그:")
        for line in timeline_api_lines:
            print(f"    {line.strip()}")

    issues_api_lines = re.findall(r".*\[ISSUES API\].*", content)
    if issues_api_lines:
        print(f"\n  ISSUES API 로그:")
        for line in issues_api_lines:
            print(f"    {line.strip()}")

    print("\n" + "=" * 60)
    print("분석 완료")
    print("=" * 60)


if __name__ == "__main__":
    main()
