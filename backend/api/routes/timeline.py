"""
Timeline API 라우터

이벤트 리스트로부터 구조화된 Timeline을 생성합니다.
"""

import logging
from fastapi import APIRouter, HTTPException, Query
from backend.core.pipeline_cache import get_or_create_timeline_sections
from backend.core.models import TimelineRequest, TimelineResponse
from backend.core.constants import USE_LLM_BY_DEFAULT

router = APIRouter(prefix="/api/timeline", tags=["timeline"])
logger = logging.getLogger(__name__)


@router.post("", response_model=TimelineResponse)
async def create_timeline(
    request: TimelineRequest,
    use_llm: bool = Query(
        default=USE_LLM_BY_DEFAULT,
        description="LLM 사용 여부 (기본값: True)",
    ),
):
    """
    이벤트 리스트로부터 구조화된 Timeline을 생성합니다.

    Args:
        request: TimelineRequest (session_meta, events, issue_cards)
        use_llm: LLM 사용 여부 (기본값: True, USE_LLM_BY_DEFAULT 상수 사용)

    Returns:
        TimelineResponse: 세션 메타데이터, Timeline Section 리스트, Timeline Event 리스트

    Raises:
        HTTPException: Timeline 생성 실패 시
    """
    logger.info(f"[TIMELINE API] use_llm={use_llm}, events_count={len(request.events)}")

    try:
        # pipeline_cache 사용하여 Timeline Sections 생성
        if request.content_hash:
            # content_hash가 있으면 pipeline_cache 사용
            timeline_sections = get_or_create_timeline_sections(
                events=request.events,
                session_meta=request.session_meta,
                content_hash=request.content_hash,
                use_llm=use_llm,
                issue_cards=request.issue_cards or [],
            )

            # TimelineEvent 리스트 생성 (하위 호환성)
            from backend.builders.timeline_builder import build_timeline
            timeline_events = build_timeline(request.events, request.session_meta)

            logger.info(f"[TIMELINE API] sections_count={len(timeline_sections)}, use_llm={use_llm}")

            return TimelineResponse(
                session_meta=request.session_meta,
                sections=timeline_sections,
                events=timeline_events,
            )
        else:
            # content_hash가 없으면 기존 방식 사용 (하위 호환성)
            from backend.builders.timeline_builder import build_structured_timeline
            result = build_structured_timeline(
                events=request.events,
                session_meta=request.session_meta,
                issue_cards=request.issue_cards,
                use_llm=use_llm,
            )

            logger.info(f"[TIMELINE API] sections_count={len(result['sections'])}, use_llm={use_llm}")

            return TimelineResponse(
                session_meta=request.session_meta,
                sections=result["sections"],
                events=result["events"],
            )
    except Exception as e:
        logger.error(f"[TIMELINE API] Failed to build timeline: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"Failed to build timeline: {str(e)}"
        )

