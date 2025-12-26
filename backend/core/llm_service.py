"""
LLM 서비스 모듈

gpt-4.1-mini를 사용하여 이벤트 타입 분류 및 요약 생성
"""

import logging
import threading
import time
import os
from typing import Dict, Optional, List
from dotenv import load_dotenv

# .env 파일 자동 로드
load_dotenv()

from backend.core.models import Turn, EventType, Event
from backend.core.cache import (
    get_cached_result,
    save_cached_result,
    CACHE_DIR,
    _generate_text_hash,
    get_cache_stats as get_cache_dir_stats
)
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
    turn: Turn,
    context_info: Optional[Dict[str, any]] = None
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
        for i, summary in enumerate(context_info.get('recent_summaries', []), 1):
            context_prompt += f"- Turn {i}: {summary}\n"

        if context_info.get('is_debug_context'):
            context_prompt += "\n⚠️ 중요: 이전 Turn들에서 debug 과정이 진행 중입니다. 현재 Turn도 debug 맥락 안에서 이루어질 가능성이 높습니다.\n"

        if context_info.get('is_plan_context'):
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
                model="gpt-4.1-mini",  # 사용자 지시대로 정확히 사용
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
            save_cached_result(
                cache_key,
                result,
                text_hash=text_hash,
                turn_index=turn.turn_index
            )
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
                    cache_key,
                    result,
                    text_hash=text_hash,
                    turn_index=turn.turn_index
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
    logger.info(
        f"[CACHE MISS] Extract main tasks: cache_key={cache_key}, calling LLM"
    )

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

JSON 형식으로 반환하세요:

```json
{
  "tasks": [
    {
      "title": "작업 항목 제목",
      "summary": "작업 내용 요약",
      "event_seqs": [1, 2, 3]
    },
    ...
  ]
}
```

주의사항:
- event_seqs는 반드시 입력 이벤트의 seq 값이어야 함
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
                max_tokens=1000,
                temperature=0.3,
            )

            result_text = response.choices[0].message.content.strip()

            # JSON 파싱 (코드 블록 제거)
            if "```json" in result_text:
                result_text = result_text.split("```json")[1].split("```")[0].strip()
            elif "```" in result_text:
                result_text = result_text.split("```")[1].split("```")[0].strip()

            result = json.loads(result_text)
            tasks = result.get("tasks", [])

            # 검증: 모든 이벤트 seq가 포함되어야 함
            input_seqs = set(event_seqs)
            output_seqs = set()
            for task in tasks:
                output_seqs.update(task.get("event_seqs", []))

            # 누락된 이벤트가 있으면 fallback
            missing_seqs = input_seqs - output_seqs
            if missing_seqs:
                logger.warning(
                    f"[WARNING] Missing event seqs in LLM response: {missing_seqs}, "
                    f"using fallback"
                )
                return _extract_main_tasks_fallback(events)

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

        except Exception as e:
            last_error = e
            error_type = type(e).__name__

            if attempt < LLM_MAX_RETRIES - 1:
                wait_time = 2**attempt
                logger.warning(
                    f"[WARNING] LLM call attempt {attempt + 1}/{LLM_MAX_RETRIES} failed: "
                    f"{error_type}: {str(e)[:100]}, retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                logger.error(
                    f"[ERROR] LLM call failed after {LLM_MAX_RETRIES} attempts: "
                    f"{error_type}: {str(e)[:200]}"
                )
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
