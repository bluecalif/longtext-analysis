"""
텍스트 파일에서 수동 검증 데이터를 추출하여 JSON으로 변환하는 스크립트

사용법:
    poetry run python scripts/parse_text_review_to_json.py
"""

import re
import json
from pathlib import Path
from typing import Dict, Optional

# 유효한 이벤트 타입 목록
VALID_EVENT_TYPES = [
    "status_review",
    "plan",
    "artifact",
    "debug",
    "completion",
    "next_step",
    "turn",
]


def parse_text_review(text_file: Path, original_json_file: Path, output_file: Path):
    """
    텍스트 파일에서 수동 검증 데이터를 파싱하여 JSON으로 변환

    Args:
        text_file: 텍스트 파일 경로
        original_json_file: 원본 JSON 파일 경로
        output_file: 출력 JSON 파일 경로
    """
    print(f"[INFO] 텍스트 파일 읽는 중: {text_file}")
    text = text_file.read_text(encoding="utf-8")
    lines = text.split("\n")

    print(f"[INFO] 원본 JSON 파일 로드 중: {original_json_file}")
    with open(original_json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 이벤트별 수동 검증 데이터 저장
    # key: turn_index, value: 검증 데이터
    review_data: Dict[int, Dict] = {}

    # EVT-XXX 패턴으로 이벤트 구분
    event_pattern = re.compile(r"EVT-(\d+)\s+Turn\s+(\d+)\s+\|\s+(\w+)")

    current_turn_index = None
    current_section = None
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # 이벤트 시작 감지
        event_match = event_pattern.match(line)
        if event_match:
            event_num = int(event_match.group(1))
            turn_index = int(event_match.group(2))
            speaker = event_match.group(3)

            current_turn_index = turn_index
            current_section = None

            # 새 이벤트 데이터 초기화
            if turn_index not in review_data:
                review_data[turn_index] = {
                    "correct_type": None,
                    "type_accuracy": None,
                    "summary_quality": None,
                    "summary_completeness": None,
                    "notes": "",
                }

            i += 1
            continue

        if current_turn_index is None:
            i += 1
            continue

        # 섹션 감지
        if "올바른 타입 (correct_type)" in line:
            current_section = "correct_type"
            # 다음 줄로 이동 (빈 줄 건너뛰기)
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            # 값 읽기
            if i < len(lines):
                value = lines[i].strip()
                if value in VALID_EVENT_TYPES:
                    review_data[current_turn_index]["correct_type"] = value
            i += 1
            continue

        elif "타입 정확도 (1-5점)" in line:
            current_section = "type_accuracy"
            i += 1
            # 다음 줄에서 숫자 읽기
            if i < len(lines):
                value = lines[i].strip()
                if value.isdigit() and 1 <= int(value) <= 5:
                    review_data[current_turn_index]["type_accuracy"] = int(value)
            i += 1
            continue

        elif "요약 품질 (1-5점)" in line:
            current_section = "summary_quality"
            i += 1
            # 다음 줄에서 숫자 읽기
            if i < len(lines):
                value = lines[i].strip()
                if value.isdigit() and 1 <= int(value) <= 5:
                    review_data[current_turn_index]["summary_quality"] = int(value)
            i += 1
            continue

        elif "요약 완전성 (1-5점)" in line:
            current_section = "summary_completeness"
            i += 1
            # 다음 줄에서 숫자 읽기
            if i < len(lines):
                value = lines[i].strip()
                if value.isdigit() and 1 <= int(value) <= 5:
                    review_data[current_turn_index]["summary_completeness"] = int(
                        value
                    )
            i += 1
            continue

        elif "메모 (notes)" in line:
            current_section = "notes"
            i += 1
            # 다음 줄부터 메모 내용 읽기 (다음 이벤트까지 또는 빈 줄이 아닌 연속된 줄)
            notes_lines = []
            while i < len(lines):
                # 다음 이벤트 시작 감지
                if event_pattern.match(lines[i].strip()):
                    break
                # 빈 줄이 아닌 경우 메모로 추가
                if lines[i].strip() and lines[i].strip() != "추가 메모를 입력하세요...":
                    notes_lines.append(lines[i].strip())
                i += 1
            # 메모 내용 합치기
            if notes_lines:
                review_data[current_turn_index]["notes"] = "\n".join(notes_lines)
            continue

        i += 1

    # 원본 JSON 데이터에 수동 검증 결과 반영
    updated_count = 0
    for sample in data["samples"]:
        turn_index = sample["turn_index"]
        if turn_index in review_data:
            review = review_data[turn_index]
            if review["correct_type"]:
                sample["manual_review"]["correct_type"] = review["correct_type"]
                updated_count += 1
            if review["type_accuracy"] is not None:
                sample["manual_review"]["type_accuracy"] = review["type_accuracy"]
            if review["summary_quality"] is not None:
                sample["manual_review"]["summary_quality"] = review["summary_quality"]
            if review["summary_completeness"] is not None:
                sample["manual_review"]["summary_completeness"] = review[
                    "summary_completeness"
                ]
            if review["notes"]:
                sample["manual_review"]["notes"] = review["notes"]

    # JSON 파일로 저장
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n[SUCCESS] 수동 검증 데이터가 저장되었습니다: {output_file}")
    print(f"   총 {len(review_data)}개 이벤트의 검증 데이터를 추출했습니다.")
    print(f"   {updated_count}개 이벤트에 correct_type이 설정되었습니다.")

    # 통계 출력
    type_count = {}
    for turn_index, review in review_data.items():
        if review["correct_type"]:
            type_count[review["correct_type"]] = (
                type_count.get(review["correct_type"], 0) + 1
            )

    if type_count:
        print(f"\n[STATS] 타입별 검증 완료 수:")
        for event_type, count in sorted(type_count.items()):
            print(f"   {event_type}: {count}개")


def main():
    """메인 함수"""
    project_root = Path(__file__).parent.parent

    # 파일 경로 설정
    text_file = project_root / "docs" / "수동검증_html에 기록.txt"
    original_json_file = (
        project_root
        / "tests"
        / "manual_review"
        / "all_events_html_review_20251223_212658"
        / "manual_review_data.json"
    )
    output_file = (
        project_root
        / "tests"
        / "manual_review"
        / "all_events_html_review_20251223_212658"
        / "manual_review_updated.json"
    )

    # 파일 존재 확인
    if not text_file.exists():
        print(f"[ERROR] 텍스트 파일을 찾을 수 없습니다: {text_file}")
        return 1

    if not original_json_file.exists():
        print(f"[ERROR] 원본 JSON 파일을 찾을 수 없습니다: {original_json_file}")
        return 1

    # 파싱 실행
    try:
        parse_text_review(text_file, original_json_file, output_file)
        return 0
    except Exception as e:
        print(f"[ERROR] 파싱 중 오류 발생: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())


