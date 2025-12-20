"""
LLM 서비스 모듈

gpt-4.1-mini를 사용하여 이벤트 타입 분류 및 요약 생성
"""

from typing import Dict
from dotenv import load_dotenv

# .env 파일 자동 로드
load_dotenv()

from backend.core.models import Turn, EventType
from backend.core.cache import get_cached_result, save_cached_result
from backend.builders.event_normalizer import summarize_turn


def classify_and_summarize_with_llm(turn: Turn) -> Dict[str, any]:
    """
    LLM으로 타입 분류 및 요약 생성 (gpt-4.1-mini, 캐싱 적용)

    Args:
        turn: Turn 객체

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
    # 캐시 키 생성 (텍스트 해시 기반)
    cache_key = f"llm_{hash(turn.body[:1000]) % 1000000}"

    # 캐시 확인
    cached = get_cached_result(cache_key)
    if cached:
        return {
            "event_type": EventType(cached["event_type"]),
            "summary": cached["summary"],
        }

    # LLM 호출
    from openai import OpenAI

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # 사용자 지시대로 정확히 사용
        messages=[
            {
                "role": "system",
                "content": """다음 텍스트의 이벤트 타입을 분류하고 1-2문장으로 요약하세요.

이벤트 타입 선택지:
- status_review: 상태 리뷰 (현황 점검, 상태 확인)
- plan: 계획 수립 (작업 계획, 단계별 계획)
- artifact: 파일/경로 관련 (파일 생성/수정/언급)
- debug: 디버깅 (에러, 원인, 해결, 검증)
- completion: 완료 (작업 완료, 성공)
- next_step: 다음 단계 (다음 작업, 진행)
- turn: 일반 대화 (기본값)

응답 형식:
TYPE: [이벤트 타입]
SUMMARY: [1-2문장 요약]""",
            },
            {
                "role": "user",
                "content": turn.body[:2000],  # 토큰 절감
            },
        ],
        max_tokens=150,  # 타입 + 요약
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

    # 캐시 저장
    save_cached_result(cache_key, result)

    return {
        "event_type": event_type,
        "summary": summary,
    }

