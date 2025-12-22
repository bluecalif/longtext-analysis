"""
파일 기반 캐시 관리 모듈 (개선 버전)

LLM 호출 결과를 파일로 캐싱하여 비용 절감 및 성능 향상

개선 사항:
- 임시 파일 + 원자적 이동으로 Race Condition 방지
- 캐시 메타데이터로 검증 및 디버깅
- 결정적 해시 함수 지원
- 텍스트 해시 검증 기능
"""
import json
import hashlib
import time
import os
from pathlib import Path
from typing import Optional, Dict, Any

# 캐시 디렉토리 경로
CACHE_DIR = Path(__file__).parent.parent.parent / "cache"
CACHE_DIR.mkdir(exist_ok=True)


def _generate_text_hash(text: str, max_length: int = 2000) -> str:
    """
    텍스트의 결정적 해시 생성 (SHA-256)

    Args:
        text: 입력 텍스트
        max_length: 해시 생성에 사용할 최대 길이

    Returns:
        16자리 해시 문자열
    """
    text_content = text[:max_length]
    hash_obj = hashlib.sha256(text_content.encode('utf-8'))
    return hash_obj.hexdigest()[:16]  # 16자리만 사용 (충분함)


def get_cached_result(cache_key: str, text_hash: Optional[str] = None) -> Optional[dict]:
    """
    캐시된 결과 조회 (개선 버전)

    Args:
        cache_key: 캐시 키
        text_hash: 텍스트 해시 (검증용, 선택적)

    Returns:
        캐시된 결과 (dict) 또는 None
    """
    cache_file = CACHE_DIR / f"{cache_key}.json"

    if not cache_file.exists():
        return None

    try:
        with open(cache_file, "r", encoding="utf-8") as f:
            cached_data = json.load(f)

        # 캐시 메타데이터 추출 (검증용)
        cached_meta = cached_data.get("_cache_meta", {})

        # 텍스트 해시 검증 (제공된 경우)
        if text_hash:
            cached_text_hash = cached_meta.get("text_hash")
            if cached_text_hash != text_hash:
                # 캐시 키 충돌 감지
                return None

        # 캐시 메타데이터 제거 (사용자에게 반환하지 않음)
        cached_data.pop("_cache_meta", None)

        return cached_data

    except (json.JSONDecodeError, IOError, KeyError):
        # 캐시 파일 손상 시 무시
        return None


def save_cached_result(
    cache_key: str,
    result: dict,
    text_hash: Optional[str] = None,
    turn_index: Optional[int] = None
) -> None:
    """
    결과를 캐시에 저장 (개선 버전: 임시 파일 + 원자적 이동)

    Args:
        cache_key: 캐시 키
        result: 저장할 결과 (dict)
        text_hash: 텍스트 해시 (검증용, 선택적)
        turn_index: Turn 인덱스 (디버깅용, 선택적)
    """
    cache_file = CACHE_DIR / f"{cache_key}.json"

    try:
        # 결과 복사본 생성
        result_to_cache = result.copy()

        # 캐시 메타데이터 추가
        cache_meta = {
            "cached_at": time.time(),
            "cache_key": cache_key,
        }

        if text_hash:
            cache_meta["text_hash"] = text_hash

        if turn_index is not None:
            cache_meta["turn_index"] = turn_index

        result_to_cache["_cache_meta"] = cache_meta

        # 임시 파일로 먼저 저장 (원자적 이동을 위해)
        temp_file = cache_file.with_suffix('.tmp')

        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(result_to_cache, f, ensure_ascii=False, indent=2)

        # 원자적 이동 (Windows/Linux 모두 지원)
        temp_file.replace(cache_file)

    except IOError:
        # 캐시 저장 실패 시 무시 (디스크 공간 부족 등)
        # 로깅은 호출자에서 처리
        pass


def get_cache_stats() -> Dict[str, Any]:
    """
    캐시 통계 정보 (cache_manager.py 패턴 적용)

    Returns:
        캐시 통계 딕셔너리
    """
    try:
        cache_files = list(CACHE_DIR.glob("llm_*.json"))
        total_size = sum(f.stat().st_size for f in cache_files)

        return {
            "cache_directory": str(CACHE_DIR),
            "total_files": len(cache_files),
            "total_size_bytes": total_size,
            "total_size_mb": round(total_size / (1024 * 1024), 2)
        }
    except Exception as e:
        return {"error": str(e)}

