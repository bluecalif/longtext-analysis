"""
LLM 서비스 모듈

gpt-4.1-mini를 사용하여 이벤트 타입 분류 및 요약 생성
"""

import logging
import threading
import time
import os
from typing import Dict, Optional, List, Callable, Any
from dotenv import load_dotenv

# .env 파일 자동 로드
load_dotenv()

from backend.core.models import Turn, EventType, Event, TimelineSection, SessionMeta
from backend.core.cache import (
    get_cached_result,
    save_cached_result,
    CACHE_DIR,
    _generate_text_hash,
    get_cache_stats as get_cache_dir_stats,
)
from backend.core.constants import LLM_MODEL
from backend.builders.event_normalizer import summarize_turn
import json

# 로거 설정
logger = logging.getLogger(__name__)

# 실행 중 캐시 통계 추적 (thread-safe)
_cache_stats = {"hits": 0, "misses": 0, "saves": 0}
_cache_stats_lock = threading.Lock()

# LLM 설정 상수
LLM_TIMEOUT = 120  # OpenAI API 타임아웃 (초)
LLM_MAX_RETRIES = 3  # 최대 재시도 횟수


def _call_llm_with_retry(
    messages: List[Dict[str, str]],
    cache_key: str,
    text_hash: str,
    model: str = LLM_MODEL,
    max_tokens: int = 200,
    temperature: float = 0.3,
    response_format: Optional[Dict[str, str]] = None,
    turn_index: Optional[int] = None,
    fallback_fn: Optional[Callable[[], Any]] = None,
) -> Optional[str]:
    """
    공통 LLM 호출 함수 (재시도 로직, 캐싱 포함)

    모든 LLM 호출 함수에서 이 함수를 사용하여 중복 제거

    Args:
        messages: OpenAI API messages 리스트
        cache_key: 캐시 키
        text_hash: 텍스트 해시 (검증용)
        model: LLM 모델명 (기본값: LLM_MODEL 상수)
        max_tokens: 최대 토큰 수
        temperature: 온도
        response_format: 응답 형식 (JSON 등)
        turn_index: Turn 인덱스 (로깅용)
        fallback_fn: Fallback 함수 (재시도 실패 시 호출)

    Returns:
        LLM 응답 텍스트 또는 None (실패 시)
    """
    # 1. 캐시 확인
    cached = get_cached_result(cache_key, text_hash=text_hash)
    if cached:
        with _cache_stats_lock:
            _cache_stats["hits"] += 1
        logger.info(f"[CACHE HIT] LLM call: cache_key={cache_key}, turn_index={turn_index}")
        return cached.get("result")

    # 2. 캐시 미스
    with _cache_stats_lock:
        _cache_stats["misses"] += 1
    logger.info(
        f"[CACHE MISS] LLM call: cache_key={cache_key}, turn_index={turn_index}, calling LLM"
    )

    # 3. OpenAI 클라이언트 생성
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.warning("[WARNING] OPENAI_API_KEY not set")
        if fallback_fn:
            return fallback_fn()
        return None

    client = OpenAI(api_key=api_key, timeout=LLM_TIMEOUT)

    # 4. 재시도 로직
    last_error = None
    for attempt in range(LLM_MAX_RETRIES):
        try:
            # LLM 호출 파라미터 구성
            call_params = {
                "model": model,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
            }
            if response_format:
                call_params["response_format"] = response_format

            response = client.chat.completions.create(**call_params)

            result = response.choices[0].message.content.strip()

            # 5. 캐시 저장
            cache_result = {"result": result}
            save_cached_result(cache_key, cache_result, text_hash=text_hash, turn_index=turn_index)
            with _cache_stats_lock:
                _cache_stats["saves"] += 1
            logger.info(f"[CACHE SAVE] LLM call: cache_key={cache_key}, turn_index={turn_index}")

            return result

        except Exception as e:
            last_error = e
            error_type = type(e).__name__

            # 마지막 시도가 아니면 재시도
            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt  # 지수 백오프: 1초, 2초, 4초
                logger.warning(
                    f"[WARNING] LLM call attempt {attempt + 1}/{LLM_MAX_RETRIES} failed: "
                    f"{error_type}: {str(e)[:100]}, retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                # 모든 재시도 실패 시 에러 로그
                logger.error(
                    f"[ERROR] LLM call failed after {LLM_MAX_RETRIES} attempts: "
                    f"{error_type}: {str(e)[:200]}"
                )

                # Fallback 함수가 있으면 호출
                if fallback_fn:
                    logger.info("[FALLBACK] Using fallback function")
                    fallback_result = fallback_fn()

                    # Fallback 결과도 캐시 저장
                    cache_result = {"result": fallback_result}
                    save_cached_result(
                        cache_key,
                        cache_result,
                        text_hash=text_hash,
                        turn_index=turn_index,
                    )
                    with _cache_stats_lock:
                        _cache_stats["saves"] += 1
                    logger.info(
                        f"[CACHE SAVE] LLM call (fallback): cache_key={cache_key}, turn_index={turn_index}"
                    )

                    return fallback_result

                return None

    return None


def get_cache_stats() -> dict:
    """
    현재 캐시 통계 반환 (개선 버전: 디렉토리 통계 포함)

    Returns:
        캐시 통계 딕셔너리 (hits, misses, saves, hit_rate, cache_directory, total_files 등)
    """
    with _cache_stats_lock:
        stats = _cache_stats.copy()

        # 디렉토리 통계 추가
        dir_stats = get_cache_dir_stats()
        stats.update(dir_stats)

        # 히트율 계산
        total_requests = stats["hits"] + stats["misses"]
        if total_requests > 0:
            stats["hit_rate"] = stats["hits"] / total_requests
        else:
            stats["hit_rate"] = 0.0

        return stats


def reset_cache_stats() -> None:
    """캐시 통계 초기화"""
    with _cache_stats_lock:
        _cache_stats["hits"] = 0
        _cache_stats["misses"] = 0
        _cache_stats["saves"] = 0


def classify_and_summarize_with_llm(
    turn: Turn, context_info: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (개선 버전: Artifact 정보 및 맥락 포함)

    개선 사항:
    1. 결정적 해시 함수 사용 (SHA-256)
    2. 텍스트 해시 검증으로 충돌 감지
    3. Fallback 시에도 캐시 저장
    4. 캐시 메타데이터 추가
    5. Artifact 정보(code_blocks, path_candidates) 포함
    6. 맥락 정보(context_info) 포함

    Args:
        turn: Turn 객체
        context_info: 맥락 정보 (선택적)
            - recent_turn_count: 최근 Turn 개수
            - recent_summaries: 최근 Turn 요약 리스트
            - is_debug_context: debug 맥락 여부
            - is_plan_context: plan 맥락 여부

    Returns:
        {
            "event_type": EventType,
            "summary": str
        }

    비용 분석:
    - 입력: $0.40 per 1M tokens
    - 출력: $1.60 per 1M tokens
    - 평균 500자 텍스트 → 약 125 tokens
    - 평균 응답 (타입 + 요약) → 약 30 tokens
    - 비용: (125 * 0.40 + 30 * 1.60) / 1M = $0.000098 per Turn
    - 캐싱 적용 시: 70-80% 절감 → $0.0000196-0.0000294 per Turn
    """
    # 1. Artifact 정보 수집
    artifact_info = ""
    if turn.code_blocks:
        artifact_info += f"\n## 코드 블록 정보\n"
        artifact_info += f"- 코드 블록 개수: {len(turn.code_blocks)}\n"
        for i, block in enumerate(turn.code_blocks[:3], 1):  # 최대 3개만
            artifact_info += f"- 코드 블록 {i}: 언어={block.lang}, 길이={len(block.code)}자\n"

    if turn.path_candidates:
        artifact_info += f"\n## 파일 경로 정보\n"
        artifact_info += f"- 파일 경로: {', '.join(turn.path_candidates[:5])}\n"  # 최대 5개만

    # 2. 맥락 정보 수집
    context_prompt = ""
    if context_info:
        context_prompt = f"""
## 이전 Turn 맥락 정보

최근 {context_info.get('recent_turn_count', 0)}개 Turn의 요약:
"""
        for i, summary in enumerate(context_info.get("recent_summaries", []), 1):
            context_prompt += f"- Turn {i}: {summary}\n"

        if context_info.get("is_debug_context"):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 debug 과정이 진행 중입니다. 현재 Turn도 debug 맥락 안에서 이루어질 가능성이 높습니다.\n"

        if context_info.get("is_plan_context"):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 계획 수립이 진행 중입니다.\n"

    # 3. 결정적 캐시 키 생성 (SHA-256 사용, Artifact 정보 포함)
    text_content = turn.body[:2000]  # 충분한 길이로 확장

    # Artifact 정보를 캐시 키에 포함
    artifact_hash = ""
    if turn.code_blocks:
        artifact_hash += f"_code_{len(turn.code_blocks)}"
    if turn.path_candidates:
        artifact_hash += f"_path_{len(turn.path_candidates)}"

    # 맥락 정보도 캐시 키에 포함 (있는 경우)
    context_hash = ""
    if context_info:
        context_hash = f"_ctx_{hash(str(context_info.get('recent_summaries', []))[:100]) % 10000}"

    text_hash = _generate_text_hash(text_content + artifact_hash + context_hash, max_length=2000)
    cache_key = f"llm_{text_hash}"
    cache_file = CACHE_DIR / f"{cache_key}.json"

    logger.debug(
        f"[CACHE] Turn {turn.turn_index}: cache_key={cache_key}, "
        f"text_hash={text_hash}, file_exists={cache_file.exists()}"
    )

    # 2. 캐시 확인 (텍스트 해시 검증 포함)
    cached = get_cached_result(cache_key, text_hash=text_hash)
    if cached:
        with _cache_stats_lock:
            _cache_stats["hits"] += 1
        logger.info(f"[CACHE HIT] Turn {turn.turn_index}: cache_key={cache_key}")
        return {
            "event_type": EventType(cached["event_type"]),
            "summary": cached["summary"],
        }

    # 3. 캐시 미스
    with _cache_stats_lock:
        _cache_stats["misses"] += 1
    logger.info(f"[CACHE MISS] Turn {turn.turn_index}: cache_key={cache_key}, calling LLM")

    # LLM 호출 (재시도 로직 포함)
    from openai import OpenAI

    # API 키 가져오기
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key, timeout=LLM_TIMEOUT)

    # 재시도 로직 (지수 백오프)
    last_error = None
    for attempt in range(LLM_MAX_RETRIES):
        try:
            # System 프롬프트 생성 (Artifact 정보 및 맥락 포함)
            system_prompt = f"""다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

{context_prompt}

{artifact_info}

## 이벤트 타입 선택지 및 구분 기준

**⚠️ 중요**: 맥락 정보와 Artifact 정보를 반드시 고려하세요!

- **status_review**: 상태 확인/리뷰 (파일 읽기, 현황 파악 등)
  - 예: "프로젝트 현황을 파악합니다", "진행 상황을 확인합니다", "TODOs.md 파일을 참조합니다"
  - ⚠️ 주의: debug 맥락 안에서의 상태 확인은 debug 타입이 더 적합할 수 있음
  - ⚠️ 주의: 코드 블록이 있으면 code_generation 타입이 더 적합할 수 있음
  - 파일 경로만 있고 코드 블록이 없으면 status_review 가능성 높음

- **plan**: 계획 수립 (새로운 작업 계획, 단계별 계획)
  - 예: "다음 작업을 계획합니다", "단계별 계획을 수립합니다"
  - ⚠️ 주의: debug 맥락 안에서의 계획은 debug 타입이 더 적합할 수 있음
  - ⚠️ 주의: 코드 블록이 있으면 code_generation 타입이 더 적합할 수 있음

- **code_generation**: 코드 생성 (새로운 코드 작성, 컴포넌트 생성 등)
  - **코드 블록이 있으면**: code_generation 타입 가능성 매우 높음
  - **이전 Turn에 plan이 있고 현재 Turn에 코드 블록이 있으면**: code_generation 가능성 매우 높음
  - 예: "새로운 컴포넌트를 생성합니다" + 코드 블록 → **code_generation**
  - 예: "스크립트를 작성합니다" + 코드 블록 → **code_generation**
  - 키워드: "스크립트 작성", "코드 작성", "파일 생성", "컴포넌트 생성", "생성합니다"
  - ⚠️ 구분: 문제 해결을 위한 코드 수정은 debug 타입, 새로운 코드 작성은 code_generation

- **debug**: 문제 해결 과정 (에러 분석, 원인 파악, 코드 수정, 검증)
  - 예: "원인을 분석합니다", "문제를 해결합니다", "에러를 확인합니다", "코드를 수정합니다"
  - ⚠️ 중요: 이전 Turn에 debug 맥락이 있으면 현재 Turn도 debug 가능성 높음
  - ⚠️ 중요: debug 맥락 안에서의 상태 확인, 계획, 코드 수정도 debug 타입 고려
  - ⚠️ 구분: 새로운 코드 생성은 code_generation, 문제 해결을 위한 수정은 debug

- **completion**: 완료 (작업 완료, 성공, TODOs.md 업데이트 등)
  - 예: "작업이 완료되었습니다", "성공적으로 완료했습니다", "TODOs.md에 반영합니다"
  - 파일 경로(TODOs.md 등)와 함께 완료 키워드가 있으면 completion 가능성 높음

- **next_step**: 다음 단계 (다음 작업, 진행)
  - 예: "다음 단계로 진행합니다", "다음 작업을 시작합니다"

- **turn**: 일반 대화 (기본값, 위 타입에 해당하지 않을 때)

## 타입 분류 우선순위

1. **맥락 우선**: 이전 Turn의 맥락을 먼저 고려
   - 이전 Turn에 debug가 있으면 → 현재 Turn도 debug 가능성 높음
   - 이전 Turn에 plan이 있고 현재 Turn에 코드 블록이 있으면 → code_generation 가능성 높음
2. **Code Generation 우선**: 코드 블록이 있으면 code_generation 타입 우선 고려
   - 단, debug 맥락이 있으면 debug 타입이 더 우선
   - 단, 새로운 코드 생성이 아닌 문제 해결을 위한 수정이면 debug 타입
3. **키워드 기반**: 현재 Turn의 키워드로 타입 판단
4. **기본값**: 위 조건에 해당하지 않으면 turn

## 요약 생성 규칙

**핵심 원칙**:
1. **핵심 동작 포함**: 무엇을 하는가 (동작 중심)
2. **상태 정보 포함**: 진행중/완료/요청 등 상태 명시
3. **중요 세부사항 포함**: 파일명, 수치, 변경사항 등
4. **이전 Turn과의 연관성**: 이전 Turn과 연관이 있으면 언급

**특수 기호 의미**:
- **@**: 첨부 자료 또는 참조 대상 (예: @TODOs.md → "TODOs.md 파일을 참조")
- **#**: 파일명, 항목 번호 등 (예: # Phase 6 → "Phase 6")
- **`**: 코드나 파일명 (예: `main.py` → "main.py 파일")

**요약 예시**:
- ❌ 나쁜 예: "프로젝트 현황을 파악합니다."
- ✅ 좋은 예: "TODOs.md 파일을 참조하여 프로젝트의 현재 진행 상황과 남은 작업들을 파악합니다."

- ❌ 나쁜 예: "변경사항을 확인합니다."
- ✅ 좋은 예: "기본 피드백 생성 로직 추가 완료 후, Git 커밋 진행합니다."

**요약 길이**: 150-200자 (의미 있는 단위로 자르기, 문장 중간 자르기 금지)

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약, 핵심 동작과 상태 정보 포함]"""

            # User 프롬프트 생성 (Artifact 정보 포함)
            user_content = turn.body[:2000]
            if artifact_info:
                user_content += f"\n\n{artifact_info}"

            response = client.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_content,
                    },
                ],
                max_tokens=200,  # 150 → 200으로 증가 (요약 품질 개선)
                temperature=0.3,  # 일관성 유지
            )

            result_text = response.choices[0].message.content.strip()

            # 응답 파싱
            event_type_str = None
            summary = None

            for line in result_text.split("\n"):
                if line.startswith("TYPE:"):
                    event_type_str = line.replace("TYPE:", "").strip().lower()
                elif line.startswith("SUMMARY:"):
                    summary = line.replace("SUMMARY:", "").strip()

            # 타입 검증
            try:
                event_type = EventType(event_type_str) if event_type_str else EventType.TURN
            except ValueError:
                event_type = EventType.TURN

            # 요약이 없으면 기본 요약 (정규식 기반)
            if not summary:
                summary = summarize_turn(turn)

            result = {
                "event_type": event_type.value,
                "summary": summary,
            }

            # 5. 캐시 저장 (텍스트 해시 포함)
            save_cached_result(cache_key, result, text_hash=text_hash, turn_index=turn.turn_index)
            with _cache_stats_lock:
                _cache_stats["saves"] += 1
            logger.info(f"[CACHE SAVE] Turn {turn.turn_index}: cache_key={cache_key}")

            return {
                "event_type": event_type,
                "summary": summary,
            }

        # 모든 예외 처리 (타임아웃, Rate limit, 일시적 오류 등)
        except Exception as e:
            last_error = e
            error_type = type(e).__name__

            # 마지막 시도가 아니면 재시도
            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt  # 지수 백오프: 1초, 2초, 4초
                logger.warning(
                    f"[WARNING] LLM call attempt {attempt + 1}/{LLM_MAX_RETRIES} failed for Turn {turn.turn_index}: "
                    f"{error_type}: {str(e)[:100]}, retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                # 모든 재시도 실패 시 에러 로그 및 fallback
                logger.error(
                    f"[ERROR] LLM call failed after {LLM_MAX_RETRIES} attempts for Turn {turn.turn_index}: "
                    f"{error_type}: {str(e)[:200]}"
                )
                # 6. 모든 재시도 실패 시 Fallback (캐시 저장 포함)
                logger.info(
                    f"[FALLBACK] Using regex-based event generation for Turn {turn.turn_index}"
                )

                summary = summarize_turn(turn)
                result = {
                    "event_type": EventType.TURN.value,
                    "summary": summary,
                }

                # ✅ Fallback 결과도 캐시 저장 (중요!)
                save_cached_result(
                    cache_key, result, text_hash=text_hash, turn_index=turn.turn_index
                )
                with _cache_stats_lock:
                    _cache_stats["saves"] += 1
                logger.info(
                    f"[CACHE SAVE] Turn {turn.turn_index}: cache_key={cache_key} (fallback)"
                )

                return {
                    "event_type": EventType.TURN,
                    "summary": summary,
                }

    # 모든 재시도 실패 시 마지막 오류를 다시 발생시킴 (fallback 후에는 도달하지 않음)
    raise last_error


def classify_and_summarize_batch_with_llm(
    turns: List[Turn], session_meta: Optional[SessionMeta] = None
) -> List[Dict[str, any]]:
    """
    LLM으로 배치 단위 타입 분류 및 요약 생성 (Phase 6.1)

    5개 Turn을 하나의 LLM 호출로 처리하여 호출 횟수를 감소시킵니다.
    배치 내 Turn 간 컨텍스트를 활용하여 정확도를 향상시킵니다.

    ⚠️ 중요: 배치 캐시만 사용합니다 (기존 개별 캐시는 무시)
    - 캐시 키: `llm_batch_{text_hash}` 형식
    - 기존 개별 캐시(`llm_*`)는 레거시이며 사용하지 않음
    - 새 파일 처리 시 배치 캐시를 새로 생성

    Args:
        turns: Turn 리스트 (5개)
        session_meta: 세션 메타데이터 (선택적)

    Returns:
        [
            {
                "event_type": EventType,
                "summary": str
            },
            ...
        ] (5개)

    비용 분석:
    - 입력: 5개 Turn × 평균 500자 = 약 2500자 → 약 625 tokens
    - 출력: 5개 Event × 평균 30 tokens = 약 150 tokens
    - 비용: (625 * 0.40 + 150 * 1.60) / 1M = $0.00049 per 배치
    - 개별 처리 대비: 5번 호출 → 1번 호출 (80% 비용 절감)
    """
    if not turns:
        return []

    if len(turns) > 5:
        logger.warning(f"[WARNING] Batch size exceeds 5: {len(turns)}, using first 5 turns")
        turns = turns[:5]

    # 1. 배치 단위 캐시 키 생성 (배치 내 Turn 해시 결합)
    batch_texts = []
    for turn in turns:
        # 각 Turn의 텍스트 + Artifact 정보
        turn_text = turn.body[:2000]
        if turn.code_blocks:
            turn_text += f"_code_{len(turn.code_blocks)}"
        if turn.path_candidates:
            turn_text += f"_path_{len(turn.path_candidates)}"
        batch_texts.append(f"turn_{turn.turn_index}:{turn_text[:500]}")

    combined_text = "\n".join(batch_texts)
    text_hash = _generate_text_hash(combined_text, max_length=5000)
    cache_key = f"llm_batch_{text_hash}"

    logger.debug(
        f"[CACHE] Batch (turns {turns[0].turn_index}-{turns[-1].turn_index}): "
        f"cache_key={cache_key}, text_hash={text_hash}"
    )

    # 2. 캐시 확인
    cached = get_cached_result(cache_key, text_hash=text_hash)
    if cached:
        with _cache_stats_lock:
            _cache_stats["hits"] += 1
        logger.info(
            f"[CACHE HIT] Batch (turns {turns[0].turn_index}-{turns[-1].turn_index}): "
            f"cache_key={cache_key}"
        )
        # 캐시된 결과를 Turn 순서대로 반환
        cached_events = cached.get("events", [])
        if len(cached_events) == len(turns):
            return cached_events
        else:
            logger.warning(
                f"[WARNING] Cached batch size mismatch: expected {len(turns)}, "
                f"got {len(cached_events)}, ignoring cache"
            )

    # 3. 캐시 미스
    with _cache_stats_lock:
        _cache_stats["misses"] += 1
    logger.info(
        f"[CACHE MISS] Batch (turns {turns[0].turn_index}-{turns[-1].turn_index}): "
        f"cache_key={cache_key}, calling LLM"
    )

    # 4. LLM 호출 (재시도 로직 포함)
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.warning("[WARNING] OPENAI_API_KEY not found, using fallback")
        # Fallback: 개별 처리
        return [classify_and_summarize_with_llm(turn) for turn in turns]

    client = OpenAI(api_key=api_key, timeout=LLM_TIMEOUT)

    # 재시도 로직 (지수 백오프)
    last_error = None
    for attempt in range(LLM_MAX_RETRIES):
        try:
            # 배치 내 Turn 정보 수집
            batch_content = []
            for idx, turn in enumerate(turns):
                turn_info = f"""
## Turn {idx + 1} (turn_index: {turn.turn_index})

**Speaker**: {turn.speaker}

**Body**:
{turn.body[:2000]}

"""
                # Artifact 정보 추가
                if turn.code_blocks:
                    turn_info += f"**코드 블록**: {len(turn.code_blocks)}개\n"
                    for i, block in enumerate(turn.code_blocks[:3], 1):
                        turn_info += (
                            f"- 코드 블록 {i}: 언어={block.lang}, 길이={len(block.code)}자\n"
                        )

                if turn.path_candidates:
                    turn_info += f"**파일 경로**: {', '.join(turn.path_candidates[:5])}\n"

                batch_content.append(turn_info)

            # System 프롬프트 (배치 처리용)
            system_prompt = """당신은 소프트웨어 개발 세션의 대화 로그를 분석하여 각 Turn의 이벤트 타입을 분류하고 요약하는 전문가입니다.

## 작업
다음 5개 Turn의 이벤트 타입을 각각 분류하고 1-2문장으로 요약하세요.

## 이벤트 타입 선택지 및 구분 기준

- **status_review**: 상태 확인/리뷰 (파일 읽기, 현황 파악 등)
  - 예: "프로젝트 현황을 파악합니다", "진행 상황을 확인합니다", "TODOs.md 파일을 참조합니다"
  - 파일 경로만 있고 코드 블록이 없으면 status_review 가능성 높음

- **plan**: 계획 수립 (새로운 작업 계획, 단계별 계획)
  - 예: "다음 작업을 계획합니다", "단계별 계획을 수립합니다"

- **code_generation**: 코드 생성 (새로운 코드 작성, 컴포넌트 생성 등)
  - **코드 블록이 있으면**: code_generation 타입 가능성 매우 높음
  - 예: "새로운 컴포넌트를 생성합니다" + 코드 블록 → **code_generation**
  - 키워드: "스크립트 작성", "코드 작성", "파일 생성", "컴포넌트 생성"

- **debug**: 문제 해결 과정 (에러 분석, 원인 파악, 코드 수정, 검증)
  - 예: "원인을 분석합니다", "문제를 해결합니다", "에러를 확인합니다", "코드를 수정합니다"
  - ⚠️ 구분: 새로운 코드 생성은 code_generation, 문제 해결을 위한 수정은 debug

- **completion**: 완료 (작업 완료, 성공, TODOs.md 업데이트 등)
  - 예: "작업이 완료되었습니다", "성공적으로 완료했습니다", "TODOs.md에 반영합니다"

- **next_step**: 다음 단계 (다음 작업, 진행)
  - 예: "다음 단계로 진행합니다", "다음 작업을 시작합니다"

- **turn**: 일반 대화 (기본값, 위 타입에 해당하지 않을 때)

## 타입 분류 우선순위

1. **Code Generation 우선**: 코드 블록이 있으면 code_generation 타입 우선 고려
2. **키워드 기반**: Turn의 키워드로 타입 판단
3. **기본값**: 위 조건에 해당하지 않으면 turn

## 요약 생성 규칙

**핵심 원칙**:
1. **핵심 동작 포함**: 무엇을 하는가 (동작 중심)
2. **상태 정보 포함**: 진행중/완료/요청 등 상태 명시
3. **중요 세부사항 포함**: 파일명, 수치, 변경사항 등

**요약 길이**: 150-200자 (의미 있는 단위로 자르기, 문장 중간 자르기 금지)

## 배치 내 컨텍스트 활용

- 이전 Turn의 내용을 참고하여 현재 Turn의 타입을 더 정확히 분류하세요
- 연속된 Turn의 타입 일관성을 고려하세요
- 같은 주제나 작업에 대한 Turn들은 유사한 타입을 가질 가능성이 높습니다

## 응답 형식

반드시 다음 JSON 형식으로만 응답하세요 (다른 텍스트 없이 JSON만):

{
  "events": [
    {
      "turn_index": 0,
      "event_type": "status_review",
      "summary": "요약 내용"
    },
    {
      "turn_index": 1,
      "event_type": "plan",
      "summary": "요약 내용"
    },
    ...
  ]
}

주의사항:
- 반드시 유효한 JSON 형식이어야 함
- "events" 키가 필수이며, 배열 타입이어야 함
- 각 event는 "turn_index" (정수), "event_type" (문자열), "summary" (문자열) 키를 포함해야 함
- turn_index는 입력 Turn의 순서대로 0, 1, 2, 3, 4여야 함
- 모든 Turn이 반드시 포함되어야 함 (5개)
- event_type은 반드시 위의 선택지 중 하나여야 함"""

            # User 프롬프트 (배치 내 모든 Turn)
            user_content = "\n---\n".join(batch_content)

            response = client.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_content,
                    },
                ],
                max_tokens=1000,  # 5개 Event × 평균 200 tokens
                temperature=0.3,
                response_format={"type": "json_object"},  # JSON 형식 강제
            )

            result_text = response.choices[0].message.content.strip()

            # JSON 파싱
            try:
                result = json.loads(result_text)
            except json.JSONDecodeError as e:
                logger.warning(
                    f"[WARNING] Failed to parse JSON response (attempt {attempt + 1}/{LLM_MAX_RETRIES}): {str(e)[:200]}"
                )
                if attempt < LLM_MAX_RETRIES - 1:
                    wait_time = 2**attempt
                    time.sleep(wait_time)
                    continue
                else:
                    # Fallback: 개별 처리
                    logger.info(
                        f"[FALLBACK] Using individual processing for batch "
                        f"(turns {turns[0].turn_index}-{turns[-1].turn_index})"
                    )
                    return [classify_and_summarize_with_llm(turn) for turn in turns]

            # 응답 구조 검증
            if not isinstance(result, dict):
                raise ValueError(f"LLM response is not a dict: {type(result)}")

            events = result.get("events", [])

            if not isinstance(events, list):
                raise ValueError(f"'events' is not a list: {type(events)}")

            if len(events) != len(turns):
                raise ValueError(f"Event count mismatch: expected {len(turns)}, got {len(events)}")

            # 각 event 검증 및 변환
            batch_results = []
            for idx, event_data in enumerate(events):
                if not isinstance(event_data, dict):
                    raise ValueError(f"event[{idx}] is not a dict: {type(event_data)}")

                turn_index = event_data.get("turn_index")
                if turn_index is None or turn_index != idx:
                    logger.warning(
                        f"[WARNING] turn_index mismatch: expected {idx}, got {turn_index}, "
                        f"using turn_index from turns list"
                    )
                    turn_index = turns[idx].turn_index

                event_type_str = event_data.get("event_type", "").lower()
                summary = event_data.get("summary", "")

                # 타입 검증
                try:
                    event_type = EventType(event_type_str) if event_type_str else EventType.TURN
                except ValueError:
                    logger.warning(f"[WARNING] Invalid event_type: {event_type_str}, using TURN")
                    event_type = EventType.TURN

                # 요약이 없으면 기본 요약
                if not summary:
                    summary = summarize_turn(turns[idx])

                batch_results.append(
                    {
                        "event_type": event_type,
                        "summary": summary,
                    }
                )

            # 결과 캐시 저장
            cache_result = {
                "events": [
                    {
                        "event_type": r["event_type"].value,
                        "summary": r["summary"],
                    }
                    for r in batch_results
                ]
            }
            save_cached_result(
                cache_key,
                cache_result,
                text_hash=text_hash,
                turn_index=None,  # 배치이므로 turn_index 없음
            )
            with _cache_stats_lock:
                _cache_stats["saves"] += 1
            logger.info(
                f"[CACHE SAVE] Batch (turns {turns[0].turn_index}-{turns[-1].turn_index}): "
                f"cache_key={cache_key}"
            )

            return batch_results

        # 모든 예외 처리 (타임아웃, Rate limit, 일시적 오류 등)
        except Exception as e:
            last_error = e
            error_type = type(e).__name__

            # 마지막 시도가 아니면 재시도
            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt  # 지수 백오프: 1초, 2초, 4초
                logger.warning(
                    f"[WARNING] LLM batch call attempt {attempt + 1}/{LLM_MAX_RETRIES} failed "
                    f"(turns {turns[0].turn_index}-{turns[-1].turn_index}): "
                    f"{error_type}: {str(e)[:100]}, retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                # 모든 재시도 실패 시 Fallback (개별 처리)
                logger.error(
                    f"[ERROR] LLM batch call failed after {LLM_MAX_RETRIES} attempts "
                    f"(turns {turns[0].turn_index}-{turns[-1].turn_index}): "
                    f"{error_type}: {str(e)[:200]}"
                )
                logger.info(
                    f"[FALLBACK] Using individual processing for batch "
                    f"(turns {turns[0].turn_index}-{turns[-1].turn_index})"
                )

                # Fallback: 개별 처리
                fallback_results = []
                for turn in turns:
                    try:
                        result = classify_and_summarize_with_llm(turn)
                        fallback_results.append(result)
                    except Exception as fallback_error:
                        # 개별 처리도 실패하면 기본 이벤트 생성
                        logger.warning(
                            f"[WARNING] Individual processing also failed for Turn {turn.turn_index}: "
                            f"{str(fallback_error)[:100]}"
                        )
                        fallback_results.append(
                            {
                                "event_type": EventType.TURN,
                                "summary": summarize_turn(turn),
                            }
                        )

                # Fallback 결과도 캐시 저장 (선택적)
                return fallback_results

    # 모든 재시도 실패 시 Fallback
    logger.info(
        f"[FALLBACK] Using individual processing for batch "
        f"(turns {turns[0].turn_index}-{turns[-1].turn_index})"
    )
    return [classify_and_summarize_with_llm(turn) for turn in turns]


def extract_main_tasks_with_llm(
    events: List[Event],
    phase: Optional[int] = None,
    subphase: Optional[int] = None,
) -> List[Dict[str, any]]:
    """
    LLM을 사용하여 이벤트 그룹에서 주요 작업 항목 추출 (Phase 4.5)

    이벤트 리스트를 분석하여 주요 작업 항목들을 식별하고, 각 항목의 제목과 요약을 생성합니다.

    Args:
        events: 이벤트 리스트 (같은 Phase/Subphase 그룹)
        phase: Phase 번호 (선택적, 캐시 키 생성용)
        subphase: Subphase 번호 (선택적, 캐시 키 생성용)

    Returns:
        [
            {
                "title": str,  # 작업 항목 제목
                "summary": str,  # 작업 내용 요약
                "event_seqs": List[int],  # 관련 Event seq 리스트
            },
            ...
        ]

    비용 분석:
    - 입력: 평균 10개 이벤트 → 약 5000자 → 약 1250 tokens
    - 출력: 평균 3개 작업 항목 → 약 300 tokens
    - 비용: (1250 * 0.40 + 300 * 1.60) / 1M = $0.00098 per 그룹
    - 캐싱 적용 시: 70-80% 절감
    """
    if not events:
        return []

    # 1. 캐시 키 생성 (이벤트 시퀀스 번호 기반)
    event_seqs = sorted([e.seq for e in events])
    # 이벤트 요약 텍스트를 결합하여 해시 생성
    event_texts = [f"{e.seq}:{e.type.value}:{e.summary[:200]}" for e in events]
    combined_text = "\n".join(event_texts)
    text_hash = _generate_text_hash(combined_text, max_length=5000)
    cache_key = f"main_tasks_{text_hash}"
    cache_file = CACHE_DIR / f"{cache_key}.json"

    logger.debug(
        f"[CACHE] Extract main tasks: cache_key={cache_key}, "
        f"phase={phase}, subphase={subphase}, events_count={len(events)}"
    )

    # 2. 캐시 확인
    cached = get_cached_result(cache_key, text_hash=text_hash)
    if cached:
        with _cache_stats_lock:
            _cache_stats["hits"] += 1
        logger.info(
            f"[CACHE HIT] Extract main tasks: cache_key={cache_key}, "
            f"tasks_count={len(cached.get('tasks', []))}"
        )
        return cached.get("tasks", [])

    # 3. 캐시 미스
    with _cache_stats_lock:
        _cache_stats["misses"] += 1
    logger.info(f"[CACHE MISS] Extract main tasks: cache_key={cache_key}, calling LLM")

    # 4. LLM 호출 (재시도 로직 포함)
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.warning("[WARNING] OPENAI_API_KEY not found, using fallback")
        return _extract_main_tasks_fallback(events)

    client = OpenAI(api_key=api_key, timeout=LLM_TIMEOUT)

    # 이벤트 정보 정리
    event_info_list = []
    for event in events:
        event_info = {
            "seq": event.seq,
            "type": event.type.value,
            "summary": event.summary,
        }
        if event.artifacts:
            event_info["artifacts"] = [
                {
                    "path": a.get("path", ""),
                    "action": a.get("action", ""),
                }
                for a in event.artifacts[:3]  # 최대 3개만
            ]
        if event.snippet_refs:
            event_info["snippet_refs"] = event.snippet_refs[:3]  # 최대 3개만
        event_info_list.append(event_info)

    system_prompt = """당신은 소프트웨어 개발 세션의 이벤트 로그를 분석하여 주요 작업 항목을 추출하는 전문가입니다.

## 역할
이벤트 리스트를 분석하여 논리적으로 연결된 이벤트들을 그룹화하고, 각 그룹을 하나의 주요 작업 항목으로 식별합니다.

## 입력 데이터
각 이벤트는 다음과 같은 정보를 포함합니다:
- seq: 이벤트 시퀀스 번호
- type: 이벤트 타입 (status_review, plan, code_generation, debug, completion, next_step, turn)
- summary: 이벤트 요약
- artifacts: 관련 파일 (선택적)
- snippet_refs: 관련 코드 스니펫 (선택적)

## 작업 항목 추출 규칙

1. **논리적 그룹화**: 관련된 이벤트들을 하나의 작업 항목으로 그룹화
   - 같은 파일/컴포넌트에 대한 작업
   - 같은 목적을 가진 작업
   - 순차적으로 진행되는 작업

2. **제목 생성 규칙**:
   - 작업의 핵심 내용을 간결하게 표현 (20-50자)
   - 동작 중심으로 작성 (예: "프론트엔드 컴포넌트 생성", "데이터베이스 스키마 수정")
   - 파일명이나 컴포넌트명 포함 권장

3. **요약 생성 규칙**:
   - 작업의 전체적인 흐름과 목적을 설명 (100-200자)
   - 주요 변경사항이나 결과 포함
   - 단순히 이벤트 요약을 나열하지 말고, 전체 맥락을 설명

4. **그룹화 제외 이벤트**:
   - DEBUG 타입 이벤트는 별도로 Issue Card에서 처리되므로 작업 항목에서 제외 가능
   - 하지만 작업의 일부로 포함되어야 할 경우 포함 가능

5. **작업 항목 개수**:
   - 이벤트 수가 적으면 (3개 이하) 1개 작업 항목으로 통합 가능
   - 이벤트 수가 많으면 (10개 이상) 3-5개 작업 항목으로 분리 권장

## 응답 형식

반드시 다음 JSON 형식으로만 응답하세요 (다른 텍스트 없이 JSON만):

{
  "tasks": [
    {
      "title": "작업 항목 제목",
      "summary": "작업 내용 요약",
      "event_seqs": [1, 2, 3]
    }
  ]
}

⚠️ 중요: event_seqs 정확성 규칙 (Phase 6.2)
- event_seqs는 반드시 입력 이벤트의 seq 값과 정확히 일치해야 함
- 입력 이벤트에 없는 seq 값을 포함하면 해당 task는 무시됨
- 모든 이벤트가 최소한 하나의 작업 항목에 포함되어야 함
- 누락된 이벤트는 자동으로 별도 작업 항목으로 추가됨

주의사항:
- 반드시 유효한 JSON 형식이어야 함
- "tasks" 키가 필수이며, 배열 타입이어야 함
- 각 task는 "title" (문자열), "summary" (문자열), "event_seqs" (정수 배열) 키를 포함해야 함
- event_seqs는 반드시 입력 이벤트의 seq 값이어야 함 (정확히 일치)
- 모든 이벤트가 최소한 하나의 작업 항목에 포함되어야 함
- 작업 항목은 1개 이상이어야 함"""

    user_content = json.dumps(
        {
            "phase": phase,
            "subphase": subphase,
            "events": event_info_list,
        },
        ensure_ascii=False,
        indent=2,
    )

    last_error = None
    for attempt in range(LLM_MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                max_tokens=2500,  # 증가: 67개 이벤트 처리 시 충분한 크기
                temperature=0.3,
                response_format={"type": "json_object"},  # JSON만 반환하도록 강제
            )

            result_text = response.choices[0].message.content.strip()

            # response_format={"type": "json_object"} 사용 시 순수 JSON만 반환됨
            # 하지만 안전을 위해 코드 블록 제거 로직 유지 (fallback)
            if "```json" in result_text:
                result_text = result_text.split("```json")[1].split("```")[0].strip()
            elif "```" in result_text:
                result_text = result_text.split("```")[1].split("```")[0].strip()

            result = json.loads(result_text)

            # 응답 구조 검증
            if not isinstance(result, dict):
                raise ValueError(f"LLM response is not a dict: {type(result)}")

            tasks = result.get("tasks", [])

            # tasks 검증
            if not isinstance(tasks, list):
                raise ValueError(f"'tasks' is not a list: {type(tasks)}")

            # 각 task의 구조 검증
            for idx, task in enumerate(tasks):
                if not isinstance(task, dict):
                    raise ValueError(f"task[{idx}] is not a dict: {type(task)}")
                required_keys = ["title", "summary", "event_seqs"]
                missing_keys = [key for key in required_keys if key not in task]
                if missing_keys:
                    raise ValueError(f"task[{idx}] missing keys: {missing_keys}")
                if not isinstance(task.get("event_seqs"), list):
                    raise ValueError(
                        f"task[{idx}]['event_seqs'] is not a list: {type(task.get('event_seqs'))}"
                    )

            # 검증 및 개선: 유효한 seq만 필터링, 누락된 이벤트 자동 포함 (Phase 6.2)
            input_seqs = set(event_seqs)
            output_seqs = set()
            valid_tasks = []

            logger.info(
                f"[LLM VALIDATION] Starting validation: input_seqs={sorted(input_seqs)}, "
                f"tasks_count={len(tasks)}"
            )

            for idx, task in enumerate(tasks):
                task_event_seqs = task.get("event_seqs", [])
                # 유효한 seq만 필터링 (입력 이벤트에 존재하는 seq만)
                valid_seqs = [seq for seq in task_event_seqs if seq in input_seqs]
                invalid_seqs = [seq for seq in task_event_seqs if seq not in input_seqs]

                if invalid_seqs:
                    logger.warning(
                        f"[LLM VALIDATION] Task[{idx}] has invalid seqs: {invalid_seqs}, "
                        f"filtering out. Valid seqs: {valid_seqs}"
                    )

                if valid_seqs:
                    # 유효한 seq만 사용하여 task 수정
                    task["event_seqs"] = valid_seqs
                    output_seqs.update(valid_seqs)
                    valid_tasks.append(task)
                    logger.debug(
                        f"[LLM VALIDATION] Task[{idx}] validated: "
                        f"title='{task.get('title', '')[:50]}', "
                        f"valid_seqs={valid_seqs}"
                    )
                else:
                    logger.warning(
                        f"[LLM VALIDATION] Task[{idx}] has no valid seqs, skipping. "
                        f"Original seqs: {task_event_seqs}"
                    )

            # 누락된 이벤트 자동 포함 (Phase 6.2)
            missing_seqs = input_seqs - output_seqs
            if missing_seqs:
                logger.warning(
                    f"[LLM VALIDATION] Missing event seqs: {sorted(missing_seqs)}, "
                    f"auto-including as separate task"
                )
                # 누락된 이벤트를 별도 작업 항목으로 추가
                for missing_seq in sorted(missing_seqs):
                    missing_event = next((e for e in events if e.seq == missing_seq), None)
                    if missing_event:
                        auto_task = {
                            "title": f"{missing_event.type.value} 작업",
                            "summary": missing_event.summary[:200],
                            "event_seqs": [missing_seq],
                        }
                        valid_tasks.append(auto_task)
                        logger.info(
                            f"[LLM VALIDATION] Auto-included missing event seq={missing_seq} "
                            f"as task: '{auto_task['title']}'"
                        )

            # 유효한 task가 없으면 fallback
            if not valid_tasks:
                logger.error(f"[LLM VALIDATION] No valid tasks after validation, using fallback")
                return _extract_main_tasks_fallback(events)

            logger.info(
                f"[LLM VALIDATION] Validation complete: "
                f"valid_tasks={len(valid_tasks)}, "
                f"covered_seqs={len(output_seqs)}/{len(input_seqs)}, "
                f"missing_seqs={len(missing_seqs)}"
            )

            # 유효한 tasks로 교체
            tasks = valid_tasks

            # 결과 캐시 저장
            cache_result = {
                "tasks": tasks,
            }
            save_cached_result(
                cache_key,
                cache_result,
                text_hash=text_hash,
                turn_index=None,  # 이벤트 그룹이므로 turn_index 없음
            )
            with _cache_stats_lock:
                _cache_stats["saves"] += 1
            logger.info(
                f"[CACHE SAVE] Extract main tasks: cache_key={cache_key}, "
                f"tasks_count={len(tasks)}"
            )

            return tasks

        except json.JSONDecodeError as e:
            last_error = e
            logger.warning(
                f"[WARNING] LLM response JSON decode failed (attempt {attempt + 1}/{LLM_MAX_RETRIES}): "
                f"{str(e)[:200]}"
            )
            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt
                logger.warning(f"[WARNING] Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logger.error(
                    f"[ERROR] LLM JSON decode failed after {LLM_MAX_RETRIES} attempts: "
                    f"{str(e)[:200]}"
                )
                logger.debug(
                    f"[DEBUG] Failed JSON text (first 500 chars): {result_text[:500] if 'result_text' in locals() else 'N/A'}"
                )
                logger.info("[FALLBACK] Using pattern-based task extraction")
                return _extract_main_tasks_fallback(events)
        except (ValueError, KeyError, TypeError) as e:
            # 구조 검증 오류
            last_error = e
            error_type = type(e).__name__
            logger.warning(
                f"[WARNING] LLM response validation failed (attempt {attempt + 1}/{LLM_MAX_RETRIES}): "
                f"{error_type}: {str(e)[:200]}"
            )
            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt
                logger.warning(f"[WARNING] Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logger.error(
                    f"[ERROR] LLM response validation failed after {LLM_MAX_RETRIES} attempts: "
                    f"{error_type}: {str(e)[:200]}"
                )
                # Traceback 로깅 추가
                import traceback
                logger.debug(f"[LLM ERROR] Validation traceback: {traceback.format_exc()}")
                logger.info("[FALLBACK] Using pattern-based task extraction")
                return _extract_main_tasks_fallback(events)
        except Exception as e:
            last_error = e
            error_type = type(e).__name__

            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt
                logger.warning(
                    f"[WARNING] LLM call attempt {attempt + 1}/{LLM_MAX_RETRIES} failed: "
                    f"{error_type}: {str(e)[:100]}, retrying in {wait_time}s..."
                )
                # Traceback 로깅 (재시도 시에도 기록)
                import traceback
                logger.debug(
                    f"[LLM ERROR] Attempt {attempt + 1} traceback: {traceback.format_exc()}"
                )
                time.sleep(wait_time)
            else:
                logger.error(
                    f"[ERROR] LLM call failed after {LLM_MAX_RETRIES} attempts: "
                    f"{error_type}: {str(e)[:200]}"
                )
                # Traceback 로깅 (최종 실패 시)
                import traceback
                logger.debug(f"[LLM ERROR] Final failure traceback: {traceback.format_exc()}")
                logger.info("[FALLBACK] Using pattern-based task extraction")
                return _extract_main_tasks_fallback(events)

    # 모든 재시도 실패 시 fallback
    return _extract_main_tasks_fallback(events)


def _extract_main_tasks_fallback(events: List[Event]) -> List[Dict[str, any]]:
    """
    패턴 기반 작업 항목 추출 (Fallback)

    LLM 호출 실패 시 사용하는 기본 방법입니다.
    """
    if not events:
        return []

    # 간단한 방법: 이벤트 타입별로 그룹화
    task_groups = {}
    for event in events:
        task_key = event.type.value
        if task_key not in task_groups:
            task_groups[task_key] = []
        task_groups[task_key].append(event)

    tasks = []
    for task_key, task_events in task_groups.items():
        event_seqs = sorted([e.seq for e in task_events])
        title = f"{task_key} 작업"
        summary = " ".join([e.summary[:100] for e in task_events[:3]])
        summary = summary[:200].strip()

        tasks.append(
            {
                "title": title,
                "summary": summary,
                "event_seqs": event_seqs,
            }
        )

    # Fallback 결과도 캐시 저장 (선택적, 여기서는 생략)
    return tasks


def extract_issue_with_llm(
    timeline_section: Optional[TimelineSection],
    cluster_events: List[Event],
    related_turns: List[Turn],
) -> Optional[Dict[str, any]]:
    """
    LLM으로 통합 컨텍스트 기반 Issue 추출 (Phase 4.7)

    TimelineSection + 관련 Events + 관련 Turns를 통합 컨텍스트로 사용하여
    symptom, root_cause, fix, validation을 한 번에 추출합니다.

    Args:
        timeline_section: TimelineSection (선택적)
        cluster_events: DEBUG 이벤트 클러스터
        related_turns: 관련 Turn 리스트

    Returns:
        {
            "title": str,  # 이슈 제목 (20-50자, 핵심 내용을 간결하게)
            "symptom": str,  # 증상 (핵심만)
            "root_cause": {"status": "confirmed" | "hypothesis", "text": str},  # 원인
            "fix": {"summary": str, "snippet_refs": List[str]},  # 조치 방법
            "validation": str,  # 검증 방법
        } 또는 None
    """
    if not cluster_events:
        return None

    # 통합 컨텍스트 구성
    context_parts = []

    # Timeline Section 정보
    if timeline_section:
        context_parts.append(f"작업 항목: {timeline_section.title}")
        context_parts.append(f"작업 요약: {timeline_section.summary}")

    # 관련 Turn 정보 (User 발화 우선)
    user_turns = [t for t in related_turns if t.speaker == "User"]
    cursor_turns = [t for t in related_turns if t.speaker == "Cursor"]

    if user_turns:
        context_parts.append("\n사용자 발화:")
        for turn in user_turns[:3]:  # 최대 3개
            context_parts.append(f"- {turn.body[:500]}")

    if cursor_turns:
        context_parts.append("\n개발자 응답:")
        for turn in cursor_turns[:5]:  # 최대 5개
            context_parts.append(f"- {turn.body[:500]}")

    # Event 정보
    context_parts.append("\n이벤트 요약:")
    for event in cluster_events[:5]:  # 최대 5개
        context_parts.append(f"- [{event.type.value}] {event.summary}")

    context_text = "\n".join(context_parts)

    # 캐시 키 생성 (통합 컨텍스트 기반)
    text_hash = _generate_text_hash(context_text, max_length=5000)
    cache_key = f"issue_integrated_{text_hash}"

    # 캐시 확인
    cached = get_cached_result(cache_key, text_hash=text_hash)
    if cached:
        with _cache_stats_lock:
            _cache_stats["hits"] += 1
        logger.info(f"[CACHE HIT] Integrated issue extraction: cache_key={cache_key}")
        return cached

    # 캐시 미스
    with _cache_stats_lock:
        _cache_stats["misses"] += 1
    logger.info(f"[CACHE MISS] Integrated issue extraction: cache_key={cache_key}, calling LLM")

    # LLM 호출
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.warning("[WARNING] OPENAI_API_KEY not set, using fallback")
        return None

    client = OpenAI(api_key=api_key, timeout=LLM_TIMEOUT)

    # 재시도 로직
    last_error = None
    for attempt in range(LLM_MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": """다음 대화 내용에서 이슈 정보를 추출하세요. JSON 형식으로 반환하세요.

반드시 제외해야 할 텍스트:
- '원인 분석 중입니다...'
- '분석 중입니다...'
- '확인합니다...'
- '정리합니다...'

JSON 형식:
{
  "title": "이슈 제목 (20-50자, 핵심 내용을 간결하게 표현, 동작 중심으로 작성)",
  "symptom": "사용자가 발견한 문제 현상 (핵심만, 1-2문장)",
  "root_cause": {
    "status": "confirmed" 또는 "hypothesis",
    "text": "실제 원인 분석 결과만 (중간 과정 텍스트 제외)"
  },
  "fix": {
    "summary": "구체적인 해결 방법 (어떤 변경을 했고, 왜 그렇게 했는지)",
    "snippet_refs": []
  },
  "validation": "검증 방법 (어떻게 확인했는지)"
}

title과 symptom은 반드시 반환해야 합니다. 다른 필드는 선택적입니다. 없으면 null을 반환하세요.""",
                    },
                    {
                        "role": "user",
                        "content": f"다음 대화 내용에서 이슈 정보를 추출하세요:\n\n{context_text[:4000]}",
                    },
                ],
                max_tokens=800,
                temperature=0.3,
                response_format={"type": "json_object"},
            )

            result_text = response.choices[0].message.content.strip()

            # JSON 파싱
            try:
                result = json.loads(result_text)
            except json.JSONDecodeError:
                logger.warning(f"[WARNING] Failed to parse JSON response: {result_text[:200]}")
                return None

            # 결과 검증 및 정규화
            normalized_result = {
                "title": result.get("title"),
                "symptom": result.get("symptom"),
                "root_cause": result.get("root_cause"),
                "fix": result.get("fix"),
                "validation": result.get("validation"),
            }

            # 결과 캐시 저장
            save_cached_result(
                cache_key,
                normalized_result,
                text_hash=text_hash,
            )
            with _cache_stats_lock:
                _cache_stats["saves"] += 1
            logger.info(f"[CACHE SAVE] Integrated issue extraction: cache_key={cache_key}")

            return normalized_result

        except Exception as e:
            last_error = e
            error_type = type(e).__name__

            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt
                logger.warning(
                    f"[WARNING] Integrated issue extraction attempt {attempt + 1}/{LLM_MAX_RETRIES} failed: "
                    f"{error_type}: {str(e)[:100]}, retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                logger.error(
                    f"[ERROR] Integrated issue extraction failed after {LLM_MAX_RETRIES} attempts: "
                    f"{error_type}: {str(e)[:200]}"
                )
                return None

    return None
