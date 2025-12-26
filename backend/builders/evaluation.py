"""
이벤트 정규화 결과 평가 도구

Phase 3.3: 결과 평가 방법 구축
- 정성적 평가 도구 (수동 검증 데이터셋 생성 및 평가)
- Golden 파일 관리 도구 (회귀 테스트용)
"""

import json
import random
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from collections import Counter, defaultdict

from backend.core.models import Event, EventType, Turn


def create_manual_review_dataset(
    events: List[Event],
    turns: List[Turn],
    output_file: Optional[Path] = None,
    sample_size: int = 30,
    min_per_type: int = 3,
) -> Dict[str, Any]:
    """
    수동 검증용 데이터셋 생성

    다양한 타입을 균등하게 샘플링하여 수동 검증용 JSON 파일 생성

    Args:
        events: 평가할 Event 리스트
        turns: 원본 Turn 리스트 (Event와 매칭용)
        output_file: 출력 파일 경로 (None이면 자동 생성)
        sample_size: 샘플 크기 (기본값: 30)
        min_per_type: 타입별 최소 샘플 수 (기본값: 3)

    Returns:
        생성된 데이터셋 딕셔너리
    """
    # 1. 타입별 이벤트 그룹화
    events_by_type: Dict[EventType, List[Event]] = defaultdict(list)
    for event in events:
        events_by_type[event.type].append(event)

    # 2. 타입별 샘플링 (최소 개수 보장)
    sampled_events: List[Event] = []
    sampled_indices: set = set()

    # 각 타입에서 최소 개수만큼 샘플링
    for event_type, type_events in events_by_type.items():
        if len(type_events) > 0:
            min_samples = min(min_per_type, len(type_events))
            samples = random.sample(type_events, min_samples)
            sampled_events.extend(samples)
            sampled_indices.update(e.turn_ref for e in samples)

    # 3. 나머지 샘플을 랜덤하게 추가 (총 sample_size까지)
    remaining_events = [e for e in events if e.turn_ref not in sampled_indices]
    if len(sampled_events) < sample_size and len(remaining_events) > 0:
        additional_needed = sample_size - len(sampled_events)
        additional_samples = random.sample(
            remaining_events, min(additional_needed, len(remaining_events))
        )
        sampled_events.extend(additional_samples)

    # 4. turn_ref 기준으로 정렬
    sampled_events.sort(key=lambda e: e.turn_ref)

    # 5. Turn 정보 매칭
    turns_dict = {turn.turn_index: turn for turn in turns}

    # 6. 데이터셋 구성
    dataset = {
        "metadata": {
            "total_events": len(events),
            "total_turns": len(turns),
            "sample_size": len(sampled_events),
            "event_type_distribution": {
                event_type.value: len(type_events)
                for event_type, type_events in events_by_type.items()
            },
            "sampled_type_distribution": {
                event_type.value: sum(1 for e in sampled_events if e.type == event_type)
                for event_type in EventType
            },
        },
        "guidelines": {
            "event_type_definition": {
                "status_review": "상태 리뷰 (현황 점검, 상태 확인, 파일 읽기)",
                "plan": "계획 수립 (작업 계획, 단계별 계획)",
                "code_generation": "코드 생성 (새로운 코드 작성, 컴포넌트 생성)",
                "debug": "디버깅 (에러 분석, 원인 파악, 코드 수정, 검증)",
                "completion": "완료 (작업 완료, 성공, TODOs.md 업데이트)",
                "next_step": "다음 단계 (다음 작업, 진행)",
                "turn": "일반 대화 (기본값)",
            },
            "evaluation_criteria": {
                "event_type_accuracy": "이벤트 타입이 Turn의 내용과 일치하는가?",
                "summary_quality": "요약이 Turn의 핵심 내용을 잘 반영하는가? (1-5점)",
                "summary_completeness": "요약이 중요한 정보를 누락하지 않는가? (1-5점)",
            },
        },
        "samples": [],
    }

    # 7. 샘플 데이터 구성
    for event in sampled_events:
        turn = turns_dict.get(event.turn_ref)
        if turn is None:
            continue

        sample = {
            "event_id": f"EVT-{event.turn_ref:03d}",
            "turn_index": event.turn_ref,
            "turn_speaker": turn.speaker,
            "turn_body": turn.body[:500],  # 처음 500자만 (전체는 너무 길 수 있음)
            "current_event": {
                "type": event.type.value,
                "summary": event.summary,
                "processing_method": event.processing_method,
                "artifacts_count": len(event.artifacts),
                "snippets_count": len(event.snippet_refs),
            },
            "manual_review": {
                "correct_type": None,  # 수동 입력: 올바른 타입
                "correct_summary": None,  # 수동 입력: 올바른 요약 (선택적)
                "type_accuracy": None,  # 수동 입력: 타입 정확도 (1-5점)
                "summary_quality": None,  # 수동 입력: 요약 품질 (1-5점)
                "summary_completeness": None,  # 수동 입력: 요약 완전성 (1-5점)
                "notes": "",  # 수동 입력: 추가 메모
            },
        }
        dataset["samples"].append(sample)

    # 8. 파일 저장
    if output_file is None:
        output_file = Path("tests/manual_review") / "manual_review_dataset.json"

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    return dataset


def evaluate_manual_review(
    review_file: Path, events: Optional[List[Event]] = None, turns: Optional[List[Turn]] = None
) -> Dict[str, Any]:
    """
    수동 검증 결과 평가

    수동 검증 결과를 로드하여 정확도 계산 및 분석

    Args:
        review_file: 수동 검증 결과 파일 경로
        events: 원본 Event 리스트 (선택적, 비교용)
        turns: 원본 Turn 리스트 (선택적, 비교용)

    Returns:
        평가 결과 딕셔너리
    """
    # 1. 수동 검증 결과 로드
    with open(review_file, "r", encoding="utf-8") as f:
        review_data = json.load(f)

    samples = review_data.get("samples", [])
    if len(samples) == 0:
        return {"error": "No samples found in review file"}

    # 2. 타입 분류 정확도 계산
    type_correct = 0
    type_total = 0
    type_confusion: Dict[Tuple[str, str], int] = defaultdict(int)  # (predicted, actual)

    # 3. Summary 품질 점수 계산
    summary_quality_scores: List[int] = []
    summary_completeness_scores: List[int] = []
    type_accuracy_scores: List[int] = []

    # 4. 처리 방법별 통계
    method_stats: Dict[str, Dict[str, int]] = defaultdict(lambda: {"correct": 0, "total": 0})

    for sample in samples:
        current = sample.get("current_event", {})
        review = sample.get("manual_review", {})

        current_type = current.get("type")
        correct_type = review.get("correct_type")
        processing_method = current.get("processing_method", "unknown")

        # 타입 정확도
        if correct_type is not None:
            type_total += 1
            if current_type == correct_type:
                type_correct += 1
            type_confusion[(current_type, correct_type)] += 1

            method_stats[processing_method]["total"] += 1
            if current_type == correct_type:
                method_stats[processing_method]["correct"] += 1

        # Summary 품질 점수
        if review.get("summary_quality") is not None:
            summary_quality_scores.append(review["summary_quality"])

        if review.get("summary_completeness") is not None:
            summary_completeness_scores.append(review["summary_completeness"])

        if review.get("type_accuracy") is not None:
            type_accuracy_scores.append(review["type_accuracy"])

    # 5. 정확도 계산
    type_accuracy = type_correct / type_total if type_total > 0 else 0.0

    # 6. 처리 방법별 정확도
    method_accuracy = {}
    for method, stats in method_stats.items():
        if stats["total"] > 0:
            method_accuracy[method] = {
                "accuracy": stats["correct"] / stats["total"],
                "correct": stats["correct"],
                "total": stats["total"],
            }

    # 7. 혼동 행렬 생성
    confusion_matrix = {}
    for (predicted, actual), count in type_confusion.items():
        if predicted not in confusion_matrix:
            confusion_matrix[predicted] = {}
        confusion_matrix[predicted][actual] = count

    # 8. 평균 점수 계산
    avg_summary_quality = (
        sum(summary_quality_scores) / len(summary_quality_scores)
        if summary_quality_scores
        else None
    )
    avg_summary_completeness = (
        sum(summary_completeness_scores) / len(summary_completeness_scores)
        if summary_completeness_scores
        else None
    )
    avg_type_accuracy = (
        sum(type_accuracy_scores) / len(type_accuracy_scores) if type_accuracy_scores else None
    )

    # 9. 결과 구성
    evaluation_result = {
        "metadata": {
            "review_file": str(review_file),
            "total_samples": len(samples),
            "evaluated_samples": type_total,
        },
        "type_classification": {
            "accuracy": type_accuracy,
            "correct": type_correct,
            "total": type_total,
            "confusion_matrix": confusion_matrix,
        },
        "summary_quality": {
            "average_quality": avg_summary_quality,
            "average_completeness": avg_summary_completeness,
            "samples_count": len(summary_quality_scores),
        },
        "type_accuracy_scores": {
            "average": avg_type_accuracy,
            "samples_count": len(type_accuracy_scores),
        },
        "method_comparison": method_accuracy,
    }

    return evaluation_result


def create_golden_file_from_manual_review(
    review_file: Path,
    results_file: Path,
    output_file: Optional[Path] = None,
    min_accuracy: float = 0.85,
    apply_corrections: bool = True,
) -> Dict[str, Any]:
    """
    수동 검증 결과를 기반으로 Golden 파일 생성

    수동 검증 데이터셋 파일과 E2E 테스트 결과 파일을 사용하여
    검증된 결과를 Golden 파일로 저장합니다.

    Args:
        review_file: 수동 검증 결과 파일 경로 (manual_review_dataset_*.json)
        results_file: E2E 테스트 결과 파일 경로 (event_normalizer_e2e_llm_*.json)
        output_file: 출력 Golden 파일 경로 (None이면 자동 생성)
        min_accuracy: 최소 정확도 요구사항 (기본값: 0.85)
        apply_corrections: 수동 검증에서 correct_type이 있으면 적용할지 여부

    Returns:
        생성 결과 딕셔너리
    """
    import json

    # 1. 수동 검증 결과 로드
    with open(review_file, "r", encoding="utf-8") as f:
        review_data = json.load(f)

    # 2. E2E 테스트 결과 로드
    with open(results_file, "r", encoding="utf-8") as f:
        results_data = json.load(f)

    # 3. Event 리스트 복원
    from backend.core.models import Event, EventType, Turn, SessionMeta

    events_dict = {e["turn_ref"]: Event(**e) for e in results_data.get("events", [])}
    turns_dict = {
        t["turn_index"]: Turn(**t) for t in results_data.get("turns", []) if "turn_index" in t
    }

    # SessionMeta 복원
    session_meta_dict = results_data.get("session_meta", {})
    session_meta = SessionMeta(**session_meta_dict) if session_meta_dict else None

    # 4. 수동 검증 결과 평가
    events_list = list(events_dict.values())
    turns_list = list(turns_dict.values())

    evaluation = evaluate_manual_review(review_file, events_list, turns_list)

    # 5. 정확도 확인
    type_accuracy = evaluation.get("type_classification", {}).get("accuracy", 0.0)

    if type_accuracy < min_accuracy:
        return {
            "created": False,
            "reason": f"정확도가 너무 낮음: {type_accuracy:.2%} < {min_accuracy:.2%}",
            "evaluation": evaluation,
            "min_accuracy_required": min_accuracy,
        }

    # 6. 수동 검증 결과를 반영하여 "올바른" 이벤트 생성 (선택적)
    corrected_events = []

    if apply_corrections:
        # turn_ref → correct_type 매핑
        corrections = {}
        for sample in review_data.get("samples", []):
            turn_ref = sample.get("turn_index")
            correct_type_str = sample.get("manual_review", {}).get("correct_type")
            if turn_ref is not None and correct_type_str is not None:
                try:
                    corrections[turn_ref] = EventType(correct_type_str)
                except ValueError:
                    # 잘못된 타입은 무시
                    pass

        # 이벤트 수정 (correct_type이 있으면 적용)
        for event in events_list:
            if event.turn_ref in corrections:
                # 수동 검증 결과 반영
                corrected_event = event.model_copy()
                corrected_event.type = corrections[event.turn_ref]
                corrected_events.append(corrected_event)
            else:
                corrected_events.append(event)
    else:
        corrected_events = events_list

    # 7. Golden 파일 생성 (수정된 이벤트 사용)
    if output_file is None:
        output_file = Path("tests/golden") / "event_normalizer_golden.json"

    golden_data = create_golden_file(
        events=corrected_events,
        turns=turns_list,
        session_meta=session_meta,
        output_file=output_file,
        description=f"수동 검증 기반 Golden 파일 (정확도: {type_accuracy:.2%}, corrections_applied: {apply_corrections})",
    )

    return {
        "created": True,
        "file_path": str(output_file),
        "type_accuracy": type_accuracy,
        "evaluation": evaluation,
        "corrections_applied": apply_corrections,
        "corrected_count": (
            len([e for e in corrected_events if e.turn_ref in corrections])
            if apply_corrections
            else 0
        ),
    }


def create_golden_file(
    events: List[Event],
    turns: List[Turn],
    session_meta: Any,
    output_file: Optional[Path] = None,
    description: str = "",
) -> Dict[str, Any]:
    """
    Golden 파일 생성 (회귀 테스트용)

    개선 사이클 완료 후 현재 결과를 Golden 파일로 저장

    Args:
        events: Event 리스트
        turns: Turn 리스트
        session_meta: SessionMeta 객체
        output_file: 출력 파일 경로 (None이면 자동 생성)
        description: Golden 파일 설명

    Returns:
        생성된 Golden 파일 딕셔너리
    """
    from datetime import datetime

    golden_data = {
        "metadata": {
            "created_at": datetime.now().isoformat(),
            "description": description,
            "session_id": session_meta.session_id if session_meta else "unknown",
            "total_events": len(events),
            "total_turns": len(turns),
        },
        "event_type_distribution": {
            event_type.value: sum(1 for e in events if e.type == event_type)
            for event_type in EventType
        },
        "processing_method_distribution": {
            method: sum(1 for e in events if e.processing_method == method)
            for method in ["regex", "llm"]
        },
        "events": [event.dict() for event in events],
        "turns": [turn.dict() for turn in turns],
    }

    if output_file is None:
        output_file = Path("tests/golden") / "event_normalizer_golden.json"

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(golden_data, f, ensure_ascii=False, indent=2)

    return golden_data


def compare_with_golden(
    current_events: List[Event], golden_file: Path, similarity_threshold: float = 0.95
) -> Dict[str, Any]:
    """
    Golden 파일과 현재 결과 비교 (회귀 감지)

    Args:
        current_events: 현재 Event 리스트
        golden_file: Golden 파일 경로
        similarity_threshold: 유사도 임계값 (기본값: 0.95, 95% 미만 시 회귀)

    Returns:
        비교 결과 딕셔너리
    """
    # 1. Golden 파일 로드
    with open(golden_file, "r", encoding="utf-8") as f:
        golden_data = json.load(f)

    golden_events = golden_data.get("events", [])
    golden_metadata = golden_data.get("metadata", {})

    # 2. 이벤트 수 비교
    current_count = len(current_events)
    golden_count = len(golden_events)
    count_match = current_count == golden_count

    # 3. 타입 분포 비교
    current_type_dist = Counter(e.type.value for e in current_events)
    golden_type_dist = Counter(e.get("type") for e in golden_events if isinstance(e, dict))

    type_dist_similarity = _calculate_distribution_similarity(current_type_dist, golden_type_dist)

    # 4. 타입 일치 비교 (turn_ref 기준)
    type_matches = 0
    type_total = 0

    golden_events_dict = {e.get("turn_ref"): e for e in golden_events if isinstance(e, dict)}

    for event in current_events:
        golden_event = golden_events_dict.get(event.turn_ref)
        if golden_event:
            type_total += 1
            if event.type.value == golden_event.get("type"):
                type_matches += 1

    type_accuracy = type_matches / type_total if type_total > 0 else 0.0

    # 5. 회귀 감지
    is_regression = (
        not count_match
        or type_dist_similarity < similarity_threshold
        or type_accuracy < similarity_threshold
    )

    # 6. 결과 구성
    comparison_result = {
        "golden_file": str(golden_file),
        "golden_metadata": golden_metadata,
        "comparison": {
            "event_count": {"current": current_count, "golden": golden_count, "match": count_match},
            "type_distribution": {
                "current": dict(current_type_dist),
                "golden": dict(golden_type_dist),
                "similarity": type_dist_similarity,
            },
            "type_accuracy": {
                "accuracy": type_accuracy,
                "matches": type_matches,
                "total": type_total,
            },
        },
        "regression_detected": is_regression,
        "regression_reasons": [],
    }

    if not count_match:
        comparison_result["regression_reasons"].append(
            f"Event count mismatch: current={current_count}, golden={golden_count}"
        )

    if type_dist_similarity < similarity_threshold:
        comparison_result["regression_reasons"].append(
            f"Type distribution similarity too low: {type_dist_similarity:.2%} < {similarity_threshold:.2%}"
        )

    if type_accuracy < similarity_threshold:
        comparison_result["regression_reasons"].append(
            f"Type accuracy too low: {type_accuracy:.2%} < {similarity_threshold:.2%}"
        )

    return comparison_result


def _calculate_distribution_similarity(dist1: Counter, dist2: Counter) -> float:
    """
    두 분포의 유사도 계산 (Jaccard 유사도 기반)

    Args:
        dist1: 첫 번째 분포 (Counter)
        dist2: 두 번째 분포 (Counter)

    Returns:
        유사도 (0.0 ~ 1.0)
    """
    all_keys = set(dist1.keys()) | set(dist2.keys())
    if len(all_keys) == 0:
        return 1.0

    total_diff = 0
    total_sum = 0

    for key in all_keys:
        val1 = dist1.get(key, 0)
        val2 = dist2.get(key, 0)
        total_sum += max(val1, val2)
        total_diff += abs(val1 - val2)

    if total_sum == 0:
        return 1.0

    similarity = 1.0 - (total_diff / total_sum)
    return max(0.0, min(1.0, similarity))


def create_all_events_html_review_dataset(
    events: List[Event],
    turns: List[Turn],
    output_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    모든 이벤트를 포함한 HTML 형식 수동 검증 데이터셋 생성

    HTML 파일에서 타입 수정 후 JavaScript로 JSON 파일 생성

    Args:
        events: 평가할 Event 리스트 (모두 포함)
        turns: 원본 Turn 리스트
        output_dir: 출력 디렉토리 (None이면 자동 생성)

    Returns:
        생성된 데이터셋 딕셔너리
    """
    from datetime import datetime

    if output_dir is None:
        output_dir = Path("tests/manual_review")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = output_dir / f"all_events_html_review_{timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Turn 정보 매칭
    turns_dict = {turn.turn_index: turn for turn in turns}

    # 이벤트를 turn_ref 기준으로 정렬
    sorted_events = sorted(events, key=lambda e: e.turn_ref)

    # 데이터셋 구성 (JSON용)
    dataset = {
        "metadata": {
            "total_events": len(events),
            "total_turns": len(turns),
            "created_at": timestamp,
        },
        "guidelines": {
            "event_type_definition": {
                "status_review": "상태 리뷰 (현황 점검, 상태 확인, 파일 읽기)",
                "plan": "계획 수립 (작업 계획, 단계별 계획)",
                "code_generation": "코드 생성 (새로운 코드 작성, 컴포넌트 생성)",
                "debug": "디버깅 (에러 분석, 원인 파악, 코드 수정, 검증)",
                "completion": "완료 (작업 완료, 성공, TODOs.md 업데이트)",
                "next_step": "다음 단계 (다음 작업, 진행)",
                "turn": "일반 대화 (기본값)",
            }
        },
        "samples": [],
    }

    # 샘플 데이터 구성
    for event in sorted_events:
        turn = turns_dict.get(event.turn_ref)
        if turn is None:
            continue

        sample = {
            "event_id": f"EVT-{event.turn_ref:03d}",
            "turn_index": event.turn_ref,
            "turn_speaker": turn.speaker,
            "turn_body": turn.body,
            "turn_body_length": len(turn.body),
            "current_event": {
                "type": event.type.value,
                "summary": event.summary,
                "processing_method": event.processing_method,
                "artifacts_count": len(event.artifacts),
                "snippets_count": len(event.snippet_refs),
                "artifacts": event.artifacts,
                "snippet_refs": event.snippet_refs,
            },
            "manual_review": {
                "correct_type": None,
                "type_accuracy": None,
                "summary_quality": None,
                "summary_completeness": None,
                "notes": "",
            },
        }
        dataset["samples"].append(sample)

    # JSON 파일 저장 (초기 데이터)
    json_file = output_dir / "manual_review_data.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    # HTML 파일 생성
    html_file = output_dir / "manual_review.html"
    html_content = generate_html_review_page(dataset)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[INFO] HTML manual review dataset created:")
    print(f"  HTML file: {html_file}")
    print(f"  JSON file: {json_file}")
    print(f"  Total events: {len(dataset['samples'])}")
    print(f"\n[INFO] 사용 방법:")
    print(f"  1. {html_file} 파일을 브라우저에서 열기")
    print(f"  2. 각 이벤트의 correct_type 선택 및 notes 입력")
    print(f"  3. 'Export to JSON' 버튼 클릭하여 수정 결과 다운로드")
    print(f"  4. 다운로드한 JSON 파일을 다음 위치에 저장:")
    print(f"     {output_dir / 'manual_review_updated.json'}")
    print(f"\n[INFO] 저장 시 주의사항:")
    print(f"  - 다운로드한 파일명은 'manual_review_updated_YYYYMMDD_HHMMSS.json' 형식입니다")
    print(f"  - 파일을 '{output_dir / 'manual_review_updated.json'}'로 복사하거나 이름을 변경하세요")
    print(f"  - 또는 다운로드한 파일을 그대로 사용해도 됩니다 (타임스탬프 포함)")

    return dataset


def generate_html_review_page(dataset: Dict[str, Any]) -> str:
    """HTML 리뷰 페이지 생성"""

    event_types = ["status_review", "plan", "code_generation", "debug", "completion", "next_step", "turn"]

    # HTML 템플릿
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>이벤트 정규화 수동 검증 - 모든 이벤트</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .header .stats {{
            color: #666;
            font-size: 14px;
        }}
        .controls {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .btn {{
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
        }}
        .btn-primary {{
            background: #007bff;
            color: white;
        }}
        .btn-primary:hover {{
            background: #0056b3;
        }}
        .btn-success {{
            background: #28a745;
            color: white;
        }}
        .btn-success:hover {{
            background: #218838;
        }}
        .event-card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .event-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 2px solid #eee;
        }}
        .event-id {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }}
        .event-type-badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }}
        .type-status_review {{ background: #e3f2fd; color: #1976d2; }}
        .type-plan {{ background: #f3e5f5; color: #7b1fa2; }}
        .type-code_generation {{ background: #fff3e0; color: #e65100; }}
        .type-debug {{ background: #ffebee; color: #c62828; }}
        .type-completion {{ background: #e8f5e9; color: #2e7d32; }}
        .type-next_step {{ background: #e0f2f1; color: #00695c; }}
        .type-turn {{ background: #f5f5f5; color: #616161; }}
        .review-section {{
            margin-top: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 4px;
        }}
        .form-group {{
            margin-bottom: 15px;
        }}
        .form-group label {{
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
            color: #333;
        }}
        .form-group select, .form-group input {{
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }}
        .form-group textarea {{
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            min-height: 80px;
            resize: vertical;
        }}
        .turn-body {{
            background: #f9f9f9;
            padding: 15px;
            border-radius: 4px;
            white-space: pre-wrap;
            word-wrap: break-word;
            max-height: 400px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.5;
        }}
        .summary-box {{
            background: #fff;
            padding: 15px;
            border-left: 4px solid #007bff;
            margin: 15px 0;
            border-radius: 4px;
        }}
        .summary-box h4 {{
            margin-bottom: 10px;
            color: #007bff;
        }}
        .toggle-btn {{
            background: #6c757d;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            margin-top: 10px;
        }}
        .toggle-btn:hover {{
            background: #5a6268;
        }}
        .collapsed {{
            display: none;
        }}
        .progress-bar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: #e0e0e0;
            z-index: 1000;
        }}
        .progress-fill {{
            height: 100%;
            background: #007bff;
            transition: width 0.3s;
        }}
    </style>
</head>
<body>
    <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%"></div>
    </div>

    <div class="container">
        <div class="header">
            <h1>이벤트 정규화 수동 검증</h1>
            <div class="stats">
                총 이벤트: {dataset['metadata']['total_events']}개 |
                검증 완료: <span id="reviewedCount">0</span>개 |
                진행률: <span id="progressPercent">0</span>%
            </div>
        </div>

        <div class="controls">
            <button class="btn btn-primary" onclick="scrollToNextUnreviewed()">다음 미검증 항목으로</button>
            <button class="btn btn-primary" onclick="scrollToPrevUnreviewed()">이전 미검증 항목으로</button>
            <button class="btn btn-success" onclick="exportToJSON()">Export to JSON</button>
            <button class="btn btn-primary" onclick="saveProgress()">진행 상황 저장 (로컬)</button>
        </div>

        <div id="eventList">
"""

    # 각 이벤트 카드 생성
    for i, sample in enumerate(dataset["samples"]):
        event_id = sample["event_id"]
        turn_index = sample["turn_index"]
        turn_speaker = sample["turn_speaker"]
        turn_body = sample["turn_body"]
        turn_body_length = sample["turn_body_length"]
        current_type = sample["current_event"]["type"]
        summary = sample["current_event"]["summary"]
        processing_method = sample["current_event"]["processing_method"]

        # HTML 이스케이프 처리
        import html as html_module

        escaped_turn_body = html_module.escape(turn_body)
        escaped_summary = html_module.escape(summary)

        # 긴 텍스트는 접기/펼치기
        is_long_text = turn_body_length > 2000
        display_text = turn_body[:2000] if is_long_text else turn_body
        escaped_display_text = html_module.escape(display_text)
        escaped_remaining_text = html_module.escape(turn_body[2000:]) if is_long_text else ""

        html += f"""
            <div class="event-card" id="event-{turn_index}" data-reviewed="false">
                <div class="event-header">
                    <div>
                        <span class="event-id">{event_id}</span>
                        <span style="margin-left: 10px; color: #666;">Turn {turn_index} | {turn_speaker}</span>
                    </div>
                    <span class="event-type-badge type-{current_type}">{current_type}</span>
                </div>

                <div class="summary-box">
                    <h4>현재 이벤트 Summary</h4>
                    <div>{escaped_summary}</div>
                    <div style="margin-top: 10px; font-size: 12px; color: #666;">
                        처리 방법: {processing_method} |
                        Artifacts: {sample['current_event']['artifacts_count']}개 |
                        Snippets: {sample['current_event']['snippets_count']}개
                    </div>
                </div>

                <div class="form-group">
                    <label>원본 Turn 텍스트 (총 {turn_body_length}자)</label>
                    <div class="turn-body" id="turn-body-{turn_index}">
                        {escaped_display_text}
"""

        if is_long_text:
            html += f"""
                        <div class="collapsed" id="turn-body-full-{turn_index}">
                            {escaped_remaining_text}
                        </div>
                        <button class="toggle-btn" onclick="toggleText({turn_index})">전체 텍스트 보기/접기</button>
"""

        html += f"""
                    </div>
                </div>

                <div class="review-section">
                    <h3 style="margin-bottom: 15px;">수동 검증</h3>

                    <div class="form-group">
                        <label for="correct_type_{turn_index}">올바른 타입 (correct_type) *</label>
                        <select id="correct_type_{turn_index}" onchange="markAsReviewed({turn_index})">
                            <option value="">선택하세요</option>
"""

        for event_type in event_types:
            selected = "selected" if event_type == current_type else ""
            html += f'                            <option value="{event_type}" {selected}>{event_type}</option>\n'

        html += f"""
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="type_accuracy_{turn_index}">타입 정확도 (1-5점)</label>
                        <input type="number" id="type_accuracy_{turn_index}" min="1" max="5" placeholder="1-5">
                    </div>

                    <div class="form-group">
                        <label for="summary_quality_{turn_index}">요약 품질 (1-5점)</label>
                        <input type="number" id="summary_quality_{turn_index}" min="1" max="5" placeholder="1-5">
                    </div>

                    <div class="form-group">
                        <label for="summary_completeness_{turn_index}">요약 완전성 (1-5점)</label>
                        <input type="number" id="summary_completeness_{turn_index}" min="1" max="5" placeholder="1-5">
                    </div>

                    <div class="form-group">
                        <label for="notes_{turn_index}">메모 (notes)</label>
                        <textarea id="notes_{turn_index}" placeholder="추가 메모를 입력하세요..."></textarea>
                    </div>
                </div>
            </div>
"""

    # JavaScript 코드
    html += (
        """
        </div>
    </div>

    <script>
        const eventData = """
        + json.dumps(dataset, ensure_ascii=False)
        + """;

        // 텍스트 접기/펼치기
        function toggleText(turnIndex) {
            const fullText = document.getElementById(`turn-body-full-${turnIndex}`);
            const btn = event.target;
            if (fullText.classList.contains('collapsed')) {
                fullText.classList.remove('collapsed');
                btn.textContent = '텍스트 접기';
            } else {
                fullText.classList.add('collapsed');
                btn.textContent = '전체 텍스트 보기';
            }
        }

        // 검증 완료 표시
        function markAsReviewed(turnIndex) {
            const card = document.getElementById(`event-${turnIndex}`);
            const correctType = document.getElementById(`correct_type_${turnIndex}`).value;
            if (correctType) {
                card.setAttribute('data-reviewed', 'true');
                card.style.borderLeft = '4px solid #28a745';
            } else {
                card.setAttribute('data-reviewed', 'false');
                card.style.borderLeft = 'none';
            }
            updateProgress();
        }

        // 진행률 업데이트
        function updateProgress() {
            const total = eventData.samples.length;
            const reviewed = document.querySelectorAll('[data-reviewed="true"]').length;
            const percent = Math.round((reviewed / total) * 100);

            document.getElementById('reviewedCount').textContent = reviewed;
            document.getElementById('progressPercent').textContent = percent;
            document.getElementById('progressFill').style.width = percent + '%';
        }

        // 다음 미검증 항목으로 스크롤
        function scrollToNextUnreviewed() {
            const unreviewed = document.querySelector('[data-reviewed="false"]');
            if (unreviewed) {
                unreviewed.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } else {
                alert('모든 항목을 검증했습니다!');
            }
        }

        // 이전 미검증 항목으로 스크롤
        function scrollToPrevUnreviewed() {
            const allCards = Array.from(document.querySelectorAll('.event-card'));
            const currentIndex = allCards.findIndex(card => {
                const rect = card.getBoundingClientRect();
                return rect.top > 0 && rect.top < window.innerHeight;
            });

            for (let i = currentIndex - 1; i >= 0; i--) {
                if (allCards[i].getAttribute('data-reviewed') === 'false') {
                    allCards[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
                    return;
                }
            }
            alert('이전 미검증 항목이 없습니다.');
        }

        // JSON으로 내보내기
        function exportToJSON() {
            const updatedData = JSON.parse(JSON.stringify(eventData));

            updatedData.samples.forEach((sample, index) => {
                const turnIndex = sample.turn_index;
                const correctTypeEl = document.getElementById(`correct_type_${turnIndex}`);
                const typeAccuracyEl = document.getElementById(`type_accuracy_${turnIndex}`);
                const summaryQualityEl = document.getElementById(`summary_quality_${turnIndex}`);
                const summaryCompletenessEl = document.getElementById(`summary_completeness_${turnIndex}`);
                const notesEl = document.getElementById(`notes_${turnIndex}`);

                // 값 가져오기 (null 체크)
                const correctType = correctTypeEl ? correctTypeEl.value : '';
                const typeAccuracy = typeAccuracyEl ? typeAccuracyEl.value : '';
                const summaryQuality = summaryQualityEl ? summaryQualityEl.value : '';
                const summaryCompleteness = summaryCompletenessEl ? summaryCompletenessEl.value : '';
                const notes = notesEl ? notesEl.value : '';

                // manual_review 업데이트 (빈 문자열은 null로 처리, 숫자는 유효성 검사)
                sample.manual_review.correct_type = correctType && correctType.trim() !== '' ? correctType : null;

                // 숫자 필드는 빈 문자열이 아니고 유효한 숫자인 경우만 저장
                if (typeAccuracy && typeAccuracy.trim() !== '') {
                    const acc = parseInt(typeAccuracy);
                    sample.manual_review.type_accuracy = (!isNaN(acc) && acc >= 1 && acc <= 5) ? acc : null;
                } else {
                    sample.manual_review.type_accuracy = null;
                }

                if (summaryQuality && summaryQuality.trim() !== '') {
                    const qual = parseInt(summaryQuality);
                    sample.manual_review.summary_quality = (!isNaN(qual) && qual >= 1 && qual <= 5) ? qual : null;
                } else {
                    sample.manual_review.summary_quality = null;
                }

                if (summaryCompleteness && summaryCompleteness.trim() !== '') {
                    const comp = parseInt(summaryCompleteness);
                    sample.manual_review.summary_completeness = (!isNaN(comp) && comp >= 1 && comp <= 5) ? comp : null;
                } else {
                    sample.manual_review.summary_completeness = null;
                }

                sample.manual_review.notes = notes ? notes.trim() : '';
            });

            // 타임스탬프 포함 파일명 생성
            const now = new Date();
            const timestamp = now.getFullYear().toString() +
                String(now.getMonth() + 1).padStart(2, '0') +
                String(now.getDate()).padStart(2, '0') + '_' +
                String(now.getHours()).padStart(2, '0') +
                String(now.getMinutes()).padStart(2, '0') +
                String(now.getSeconds()).padStart(2, '0');
            const filename = `manual_review_updated_${timestamp}.json`;

            // JSON 문자열 생성 (UTF-8 인코딩)
            const jsonStr = JSON.stringify(updatedData, null, 2);
            const blob = new Blob([jsonStr], { type: 'application/json;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            // 검증 완료 수 계산
            const reviewedCount = updatedData.samples.filter(s => s.manual_review.correct_type !== null).length;
            alert(`JSON 파일이 다운로드되었습니다!\\n파일명: ${filename}\\n검증 완료: ${reviewedCount}/${updatedData.samples.length}개`);
        }

        // 진행 상황 저장 (로컬 스토리지)
        function saveProgress() {{
            const progress = {{}};
            eventData.samples.forEach(sample => {{
                const turnIndex = sample.turn_index;
                progress[turnIndex] = {{
                    correct_type: document.getElementById(`correct_type_${{turnIndex}}`).value,
                    type_accuracy: document.getElementById(`type_accuracy_${{turnIndex}}`).value,
                    summary_quality: document.getElementById(`summary_quality_${{turnIndex}}`).value,
                    summary_completeness: document.getElementById(`summary_completeness_${{turnIndex}}`).value,
                    notes: document.getElementById(`notes_${{turnIndex}}`).value
                }};
            }});
            localStorage.setItem('reviewProgress', JSON.stringify(progress));
            alert('진행 상황이 저장되었습니다! (브라우저 로컬 스토리지)');
        }}

        // 진행 상황 복원
        function loadProgress() {{
            const saved = localStorage.getItem('reviewProgress');
            if (saved) {{
                const progress = JSON.parse(saved);
                Object.keys(progress).forEach(turnIndex => {{
                    const p = progress[turnIndex];
                    if (p.correct_type) document.getElementById(`correct_type_${{turnIndex}}`).value = p.correct_type;
                    if (p.type_accuracy) document.getElementById(`type_accuracy_${{turnIndex}}`).value = p.type_accuracy;
                    if (p.summary_quality) document.getElementById(`summary_quality_${{turnIndex}}`).value = p.summary_quality;
                    if (p.summary_completeness) document.getElementById(`summary_completeness_${{turnIndex}}`).value = p.summary_completeness;
                    if (p.notes) document.getElementById(`notes_${{turnIndex}}`).value = p.notes;
                    markAsReviewed(parseInt(turnIndex));
                }});
                alert('저장된 진행 상황을 복원했습니다!');
            }}
        }}

        // 페이지 로드 시 진행 상황 복원
        window.addEventListener('load', () => {{
            if (confirm('저장된 진행 상황을 복원하시겠습니까?')) {{
                loadProgress();
            }}
            updateProgress();
        }});
    </script>
</body>
</html>
"""
    )

    return html
