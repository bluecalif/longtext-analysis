"""
이벤트 정규화 결과 생성 스크립트 (LLM 사용, 비용 발생)

⚠️ 주의: 대부분의 경우 이 스크립트를 실행할 필요가 없습니다.

일반적인 워크플로우:
1. E2E 테스트 실행 (이벤트 정규화 결과 자동 생성):
   poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v

2. HTML 생성/재생성 (비용 없음):
   poetry run python scripts/create_html_review.py

이 스크립트는 다음 경우에만 사용하세요:
- E2E 테스트를 실행하지 않고 직접 이벤트 정규화 결과만 생성하고 싶을 때
- 새로운 입력 파일이 있거나 이벤트 정규화 로직이 변경되어 재생성이 필요할 때

사용법:
    poetry run python scripts/create_events_for_review.py
"""

import sys
import json
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# .env 파일 자동 로드
load_dotenv()

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.core.llm_service import reset_cache_stats, get_cache_stats


def main():
    """이벤트 정규화 결과 생성 (1~3단계만)"""

    # 입력 파일 경로
    input_file = project_root / "docs" / "cursor_phase_6_3.md"

    if not input_file.exists():
        print(f"[ERROR] Input file not found: {input_file}")
        return 1

    print(f"[INFO] Loading input file: {input_file}")
    text = input_file.read_text(encoding="utf-8")

    # 1단계: 파싱 실행
    print("[INFO] Step 1: Parsing markdown file...")
    parse_result = parse_markdown(text, source_doc=str(input_file))
    print(f"[INFO] Parsed: {len(parse_result['turns'])} turns")

    # 2-3단계: 이벤트 정규화 실행 (LLM 기반)
    print("[INFO] Step 2-3: Normalizing turns to events (LLM-based)...")
    print("[WARNING] LLM 호출로 인한 비용이 발생합니다!")

    # 캐시 통계 초기화
    reset_cache_stats()

    session_meta = parse_result["session_meta"]
    start_time = time.time()
    events = normalize_turns_to_events(
        parse_result["turns"], session_meta=session_meta, use_llm=True
    )
    elapsed_time = time.time() - start_time

    # 실행 중 캐시 통계 수집
    runtime_cache_stats = get_cache_stats()

    print(f"[INFO] Normalized: {len(events)} events")
    print(f"[INFO] Elapsed time: {elapsed_time:.2f} seconds")
    print(f"[INFO] Cache hit rate: {runtime_cache_stats.get('hit_rate', 0):.2%}")

    # 결과 저장
    results_dir = project_root / "tests" / "results"
    results_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = results_dir / f"event_normalizer_e2e_llm_{timestamp}.json"

    # 이벤트 타입 분포 계산
    from collections import Counter
    event_type_distribution = Counter(e.type.value for e in events)

    # 결과 저장
    detailed_results = {
        "session_meta": parse_result["session_meta"].model_dump(),
        "turns_count": len(parse_result["turns"]),
        "turns": [turn.model_dump() for turn in parse_result["turns"]],  # Turn 정보도 저장
        "events": [event.model_dump() for event in events],
        "event_type_distribution": dict(event_type_distribution),
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(input_file),
            "test_name": "create_events_for_review",
            "processing_method": "llm",
            "elapsed_time_seconds": round(elapsed_time, 2),
            "cache_statistics": runtime_cache_stats,
        },
    }

    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(detailed_results, f, ensure_ascii=False, indent=2)

    print(f"\n[SUCCESS] 이벤트 정규화 결과가 저장되었습니다!")
    print(f"  Results file: {results_file}")
    print(f"  Total events: {len(events)}")
    print(f"  Event type distribution:")
    for event_type, count in sorted(event_type_distribution.items()):
        print(f"    {event_type}: {count}개")

    print(f"\n[INFO] 다음 단계:")
    print(f"  HTML 수동 검증 데이터셋을 생성하려면 다음 명령어를 실행하세요:")
    print(f"    poetry run python scripts/create_html_review.py")
    print(f"  (최신 결과 파일을 자동으로 사용합니다)")
    print(f"  또는 특정 결과 파일을 지정하려면:")
    print(f"    poetry run python scripts/create_html_review.py --results-file {results_file.name}")

    return 0


if __name__ == "__main__":
    exit(main())

