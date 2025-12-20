"""
파일 기반 캐시 관리 모듈

LLM 호출 결과를 파일로 캐싱하여 비용 절감 및 성능 향상
"""

import json
import os
from pathlib import Path
from typing import Optional, Any


# 캐시 디렉토리 경로
CACHE_DIR = Path(__file__).parent.parent.parent / "cache"
CACHE_DIR.mkdir(exist_ok=True)


def get_cached_result(cache_key: str) -> Optional[dict]:
    """
    캐시된 결과 조회

    Args:
        cache_key: 캐시 키

    Returns:
        캐시된 결과 (dict) 또는 None
    """
    cache_file = CACHE_DIR / f"{cache_key}.json"
    if cache_file.exists():
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            # 캐시 파일 손상 시 무시
            return None
    return None


def save_cached_result(cache_key: str, result: dict) -> None:
    """
    결과를 캐시에 저장

    Args:
        cache_key: 캐시 키
        result: 저장할 결과 (dict)
    """
    cache_file = CACHE_DIR / f"{cache_key}.json"
    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
    except IOError:
        # 캐시 저장 실패 시 무시 (디스크 공간 부족 등)
        pass

