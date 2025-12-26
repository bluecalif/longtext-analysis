"""
파이프라인 중간 결과 캐싱 모듈

parsing → event → timeline → issuecard 파이프라인의 중간 결과를
파일 기반으로 캐싱하여 중복 실행을 방지합니다.

캐시 전략:
- 입력 파일 해시 + use_llm 플래그를 기반으로 캐시 키 생성
- 파일 변경 감지 시 자동 무효화
- 디버깅 및 수동 검증을 위한 영구 저장
"""

import json
import hashlib
import time
from pathlib import Path
from typing import Optional, Dict, List, Tuple, Any
from datetime import datetime

from backend.core.models import SessionMeta, Event, TimelineSection, Turn
from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.timeline_builder import build_structured_timeline

# 캐시 디렉토리 경로
PIPELINE_CACHE_DIR = Path(__file__).parent.parent.parent / "cache" / "pipeline"
PIPELINE_CACHE_DIR.mkdir(parents=True, exist_ok=True)


def _generate_file_hash(file_path: Path) -> str:
    """
    파일의 해시 생성 (SHA-256)

    Args:
        file_path: 파일 경로

    Returns:
        16자리 해시 문자열
    """
    try:
        with open(file_path, "rb") as f:
            content = f.read()
            hash_obj = hashlib.sha256(content)
            return hash_obj.hexdigest()[:16]
    except (IOError, FileNotFoundError):
        # 파일이 없거나 읽을 수 없으면 빈 해시 반환
        return "0000000000000000"


def _generate_cache_key(input_file: Path, use_llm: bool = True, cache_type: str = "parsed") -> str:
    """
    캐시 키 생성

    Args:
        input_file: 입력 파일 경로
        use_llm: LLM 사용 여부
        cache_type: 캐시 타입 ("parsed", "events", "timeline_sections")

    Returns:
        캐시 키 문자열
    """
    file_hash = _generate_file_hash(input_file)
    llm_flag = "llm" if use_llm else "pattern"
    cache_key = f"{cache_type}_{file_hash}_{llm_flag}"
    return cache_key


def get_or_create_parsed_data(input_file: Path) -> Dict[str, Any]:
    """
    파싱 결과를 가져오거나 생성 (캐시 우선)

    Args:
        input_file: 입력 마크다운 파일 경로

    Returns:
        파싱 결과 딕셔너리
    """
    cache_key = _generate_cache_key(input_file, use_llm=False, cache_type="parsed")
    cache_file = PIPELINE_CACHE_DIR / f"{cache_key}.json"

    # 캐시 확인
    if cache_file.exists():
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                cached_data = json.load(f)

            # 캐시 메타데이터 확인
            cache_meta = cached_data.get("_cache_meta", {})
            cached_file_hash = cache_meta.get("file_hash")
            current_file_hash = _generate_file_hash(input_file)

            # 파일 해시가 일치하면 캐시 사용
            if cached_file_hash == current_file_hash:
                print(f"[CACHE HIT] Parsed data: {cache_key}")
                # 캐시 메타데이터 제거
                cached_data.pop("_cache_meta", None)
                return cached_data
        except (json.JSONDecodeError, IOError, KeyError):
            # 캐시 파일 손상 시 무시하고 재생성
            pass

    # 캐시 미스 또는 무효화 → 파싱 실행
    print(f"[CACHE MISS] Parsing file: {input_file}")
    text = input_file.read_text(encoding="utf-8")
    parse_result = parse_markdown(text, source_doc=str(input_file))

    # 결과를 딕셔너리로 변환
    result = {
        "session_meta": parse_result["session_meta"].model_dump(),
        "turns": [turn.model_dump() for turn in parse_result["turns"]],
        "code_blocks": [block.model_dump() for block in parse_result["code_blocks"]],
        "artifacts": parse_result["artifacts"],
    }

    # 캐시 저장
    cache_meta = {
        "cached_at": time.time(),
        "cache_key": cache_key,
        "file_hash": _generate_file_hash(input_file),
        "input_file": str(input_file),
    }
    result["_cache_meta"] = cache_meta

    # 임시 파일로 먼저 저장 후 원자적 이동
    temp_file = cache_file.with_suffix('.tmp')
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    temp_file.replace(cache_file)

    print(f"[CACHE SAVE] Parsed data: {cache_key}")

    # 캐시 메타데이터 제거 후 반환
    result.pop("_cache_meta", None)
    return result


def get_or_create_events(
    parsed_data: Dict[str, Any],
    input_file: Path,
    use_llm: bool = True
) -> Tuple[List[Event], SessionMeta]:
    """
    이벤트 정규화 결과를 가져오거나 생성 (캐시 우선)

    Args:
        parsed_data: 파싱 결과 딕셔너리
        input_file: 입력 파일 경로 (캐시 키 생성용)
        use_llm: LLM 사용 여부

    Returns:
        (Event 리스트, SessionMeta) 튜플
    """
    cache_key = _generate_cache_key(input_file, use_llm=use_llm, cache_type="events")
    cache_file = PIPELINE_CACHE_DIR / f"{cache_key}.json"

    # 캐시 확인
    if cache_file.exists():
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                cached_data = json.load(f)

            # 캐시 메타데이터 확인
            cache_meta = cached_data.get("_cache_meta", {})
            cached_file_hash = cache_meta.get("file_hash")
            current_file_hash = _generate_file_hash(input_file)

            # 파일 해시가 일치하면 캐시 사용
            if cached_file_hash == current_file_hash:
                print(f"[CACHE HIT] Events: {cache_key}")
                # 캐시 메타데이터 제거
                cached_data.pop("_cache_meta", None)

                # 딕셔너리를 모델로 변환
                from backend.core.models import SessionMeta, Event
                session_meta = SessionMeta(**cached_data["session_meta"])
                events = [Event(**event_dict) for event_dict in cached_data["events"]]

                return events, session_meta
        except (json.JSONDecodeError, IOError, KeyError):
            # 캐시 파일 손상 시 무시하고 재생성
            pass

    # 캐시 미스 또는 무효화 → 이벤트 정규화 실행
    print(f"[CACHE MISS] Normalizing events: {cache_key}")

    # 딕셔너리를 모델로 변환
    from backend.core.models import SessionMeta, Turn
    session_meta = SessionMeta(**parsed_data["session_meta"])
    turns = [Turn(**turn_dict) for turn_dict in parsed_data["turns"]]

    # 이벤트 정규화
    events = normalize_turns_to_events(turns, session_meta=session_meta, use_llm=use_llm)

    # 결과를 딕셔너리로 변환
    result = {
        "session_meta": session_meta.model_dump(),
        "events": [event.model_dump() for event in events],
    }

    # 캐시 저장
    cache_meta = {
        "cached_at": time.time(),
        "cache_key": cache_key,
        "file_hash": _generate_file_hash(input_file),
        "input_file": str(input_file),
        "use_llm": use_llm,
    }
    result["_cache_meta"] = cache_meta

    # 임시 파일로 먼저 저장 후 원자적 이동
    temp_file = cache_file.with_suffix('.tmp')
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    temp_file.replace(cache_file)

    print(f"[CACHE SAVE] Events: {cache_key}")

    return events, session_meta


def get_or_create_timeline_sections(
    events: List[Event],
    session_meta: SessionMeta,
    input_file: Path,
    use_llm: bool = True,
    issue_cards: Optional[List] = None
) -> List[TimelineSection]:
    """
    Timeline Section 결과를 가져오거나 생성 (캐시 우선)

    Args:
        events: 정규화된 이벤트 리스트
        session_meta: 세션 메타데이터
        input_file: 입력 파일 경로 (캐시 키 생성용)
        use_llm: LLM 사용 여부
        issue_cards: Issue Cards 리스트 (선택적, 연결용)

    Returns:
        TimelineSection 리스트
    """
    cache_key = _generate_cache_key(input_file, use_llm=use_llm, cache_type="timeline_sections")
    cache_file = PIPELINE_CACHE_DIR / f"{cache_key}.json"

    # 캐시 확인
    if cache_file.exists():
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                cached_data = json.load(f)

            # 캐시 메타데이터 확인
            cache_meta = cached_data.get("_cache_meta", {})
            cached_file_hash = cache_meta.get("file_hash")
            current_file_hash = _generate_file_hash(input_file)

            # 파일 해시가 일치하면 캐시 사용
            if cached_file_hash == current_file_hash:
                print(f"[CACHE HIT] Timeline sections: {cache_key}")
                # 캐시 메타데이터 제거
                cached_data.pop("_cache_meta", None)

                # 딕셔너리를 모델로 변환
                from backend.core.models import TimelineSection
                sections = [TimelineSection(**section_dict) for section_dict in cached_data["timeline_sections"]]

                return sections
        except (json.JSONDecodeError, IOError, KeyError):
            # 캐시 파일 손상 시 무시하고 재생성
            pass

    # 캐시 미스 또는 무효화 → Timeline Section 생성 실행
    print(f"[CACHE MISS] Building timeline sections: {cache_key}")

    # Timeline Section 생성
    timeline_result = build_structured_timeline(
        events=events,
        session_meta=session_meta,
        use_llm=use_llm,
        issue_cards=issue_cards or []
    )

    # Dict에서 sections 추출
    timeline_sections = timeline_result["sections"]

    # 결과를 딕셔너리로 변환
    result = {
        "timeline_sections": [section.model_dump() for section in timeline_sections],
    }

    # 캐시 저장
    cache_meta = {
        "cached_at": time.time(),
        "cache_key": cache_key,
        "file_hash": _generate_file_hash(input_file),
        "input_file": str(input_file),
        "use_llm": use_llm,
    }
    result["_cache_meta"] = cache_meta

    # 임시 파일로 먼저 저장 후 원자적 이동
    temp_file = cache_file.with_suffix('.tmp')
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    temp_file.replace(cache_file)

    print(f"[CACHE SAVE] Timeline sections: {cache_key}")

    return timeline_sections


def invalidate_cache(input_file: Optional[Path] = None, cache_type: Optional[str] = None) -> int:
    """
    캐시 무효화 (수동)

    Args:
        input_file: 입력 파일 경로 (지정 시 해당 파일의 캐시만 무효화)
        cache_type: 캐시 타입 ("parsed", "events", "timeline_sections", None=전체)

    Returns:
        무효화된 캐시 파일 수
    """
    invalidated_count = 0

    if input_file:
        # 특정 파일의 캐시만 무효화
        file_hash = _generate_file_hash(input_file)
        pattern = f"*_{file_hash}_*.json"
        for cache_file in PIPELINE_CACHE_DIR.glob(pattern):
            if cache_type is None or cache_type in cache_file.name:
                cache_file.unlink()
                invalidated_count += 1
    else:
        # 전체 캐시 무효화
        if cache_type:
            pattern = f"{cache_type}_*.json"
        else:
            pattern = "*.json"

        for cache_file in PIPELINE_CACHE_DIR.glob(pattern):
            cache_file.unlink()
            invalidated_count += 1

    print(f"[CACHE INVALIDATE] {invalidated_count} cache files removed")
    return invalidated_count


def get_cache_stats() -> Dict[str, Any]:
    """
    캐시 통계 반환

    Returns:
        캐시 통계 딕셔너리
    """
    stats = {
        "total_files": 0,
        "parsed": 0,
        "events": 0,
        "timeline_sections": 0,
        "total_size_bytes": 0,
    }

    for cache_file in PIPELINE_CACHE_DIR.glob("*.json"):
        if cache_file.name.endswith('.tmp'):
            continue

        stats["total_files"] += 1
        stats["total_size_bytes"] += cache_file.stat().st_size

        if cache_file.name.startswith("parsed_"):
            stats["parsed"] += 1
        elif cache_file.name.startswith("events_"):
            stats["events"] += 1
        elif cache_file.name.startswith("timeline_sections_"):
            stats["timeline_sections"] += 1

    return stats

