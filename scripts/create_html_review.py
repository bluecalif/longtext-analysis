"""
HTML 수동 검증 데이터셋 생성 스크립트 (비용 없음)

저장된 이벤트 정규화 결과를 읽어서 HTML만 생성합니다.
HTML UI 수정 후 재생성 시 이 스크립트만 실행하세요.

⚠️ 중요: 이 스크립트는 LLM을 호출하지 않으므로 비용이 발생하지 않습니다.
반복 실행이 가능하며, HTML UI 수정 후 재생성 시 사용하세요.

사용법:
    # 최신 결과 파일 자동 사용 (권장)
    poetry run python scripts/create_html_review.py

    # 특정 결과 파일 지정
    poetry run python scripts/create_html_review.py --results-file tests/results/event_normalizer_e2e_llm_20251225_183334.json

참고:
    - 이벤트 정규화 결과 파일은 E2E 테스트 실행 시 자동 생성됩니다:
      poetry run pytest tests/test_event_normalizer_e2e.py::test_event_normalizer_e2e_with_llm -v
    - 결과 파일이 없으면 에러 메시지가 표시됩니다.
"""

import sys
import json
import argparse
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# .env 파일 자동 로드
load_dotenv()

from backend.core.models import Event, Turn, SessionMeta
from backend.builders.evaluation import create_all_events_html_review_dataset


def find_latest_results_file() -> Path:
    """가장 최근의 이벤트 정규화 결과 파일 찾기"""
    results_dir = project_root / "tests" / "results"
    pattern = "event_normalizer_e2e_llm_*.json"
    files = sorted(
        results_dir.glob(pattern),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )
    if not files:
        raise FileNotFoundError(
            f"이벤트 정규화 결과 파일을 찾을 수 없습니다: {results_dir / pattern}\n"
            f"먼저 이벤트 정규화를 실행하세요:\n"
            f"  poetry run python scripts/create_events_for_review.py"
        )
    return files[0]


def load_events_from_results_file(results_file: Path):
    """결과 파일에서 Event와 Turn 리스트 로드"""
    print(f"[INFO] 결과 파일 로드 중: {results_file}")

    with open(results_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Event 리스트 복원
    events = [Event(**e) for e in data.get("events", [])]
    print(f"[INFO] {len(events)}개 이벤트 로드 완료")

    # Turn 리스트 복원 (results 파일에 turns가 있으면 사용, 없으면 파싱 필요)
    turns = []
    if "turns" in data and data["turns"]:
        turns = [Turn(**t) for t in data["turns"]]
        print(f"[INFO] {len(turns)}개 Turn 로드 완료 (결과 파일에서)")
    else:
        # Turn 정보가 없으면 파싱 실행 (비용 없음, LLM 사용 안 함)
        print("[INFO] Turn 정보가 없어 파싱 실행 중... (LLM 사용 안 함, 비용 없음)")
        from backend.parser import parse_markdown
        input_file = project_root / "docs" / "cursor_phase_6_3.md"
        if not input_file.exists():
            raise FileNotFoundError(
                f"입력 파일을 찾을 수 없습니다: {input_file}\n"
                f"Turn 정보를 복원할 수 없습니다."
            )
        text = input_file.read_text(encoding="utf-8")
        parse_result = parse_markdown(text, source_doc=str(input_file))
        turns = parse_result["turns"]
        print(f"[INFO] {len(turns)}개 Turn 파싱 완료")

    # SessionMeta 복원
    session_meta_dict = data.get("session_meta", {})
    session_meta = SessionMeta(**session_meta_dict) if session_meta_dict else None

    return events, turns, session_meta


def main():
    parser = argparse.ArgumentParser(
        description="저장된 이벤트 정규화 결과를 읽어서 HTML 수동 검증 데이터셋 생성 (비용 없음)"
    )
    parser.add_argument(
        "--results-file",
        type=str,
        default=None,
        help="이벤트 정규화 결과 파일 경로 (지정하지 않으면 최신 파일 자동 사용)"
    )

    args = parser.parse_args()

    # 결과 파일 경로 결정
    if args.results_file:
        results_file = Path(args.results_file)
        if not results_file.is_absolute():
            results_file = project_root / results_file
        if not results_file.exists():
            print(f"[ERROR] 결과 파일을 찾을 수 없습니다: {results_file}")
            return 1
    else:
        try:
            results_file = find_latest_results_file()
            print(f"[INFO] 최신 결과 파일 자동 선택: {results_file.name}")
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            return 1

    # 이벤트 및 Turn 로드
    try:
        events, turns, session_meta = load_events_from_results_file(results_file)
    except Exception as e:
        print(f"[ERROR] 결과 파일 로드 실패: {e}")
        import traceback
        traceback.print_exc()
        return 1

    # HTML 수동 검증 데이터셋 생성 (비용 없음)
    print("[INFO] HTML 수동 검증 데이터셋 생성 중...")
    dataset = create_all_events_html_review_dataset(
        events=events,
        turns=turns,
        output_dir=None  # 자동 생성
    )

    print("\n[SUCCESS] HTML manual review dataset created successfully!")
    print(f"  Total events: {len(dataset['samples'])}")
    print(f"\n[INFO] 사용된 결과 파일: {results_file.name}")
    print(f"[INFO] HTML UI 수정 후 이 스크립트를 다시 실행하면 비용 없이 재생성됩니다!")
    print(f"\n[INFO] 사용 방법:")
    print(f"  1. 생성된 HTML 파일을 브라우저에서 열기")
    print(f"  2. 각 이벤트의 correct_type 선택 및 notes 입력")
    print(f"  3. 'Export to JSON' 버튼 클릭하여 수정 결과 다운로드")

    return 0


if __name__ == "__main__":
    exit(main())

