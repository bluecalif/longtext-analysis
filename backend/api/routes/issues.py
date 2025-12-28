"""
Issues API 라우터

이벤트 및 Turn 리스트로부터 Issue Cards를 생성합니다.
"""

import logging
from fastapi import APIRouter, HTTPException, Query
from backend.core.pipeline_cache import get_or_create_issue_cards
from backend.core.models import IssuesRequest, IssuesResponse
from backend.core.constants import USE_LLM_BY_DEFAULT

router = APIRouter(prefix="/api/issues", tags=["issues"])
logger = logging.getLogger(__name__)


@router.post("", response_model=IssuesResponse)
async def create_issues(
    request: IssuesRequest,
    use_llm: bool = Query(
        default=USE_LLM_BY_DEFAULT,
        description="LLM 사용 여부 (기본값: True)",
    ),
):
    """
    이벤트 및 Turn 리스트로부터 Issue Cards를 생성합니다.

    Args:
        request: IssuesRequest (session_meta, turns, events, timeline_sections)
        use_llm: LLM 사용 여부 (기본값: True, USE_LLM_BY_DEFAULT 상수 사용)

    Returns:
        IssuesResponse: 세션 메타데이터, Issue Card 리스트

    Raises:
        HTTPException: Issue Cards 생성 실패 시
    """
    logger.info(f"[ISSUES API] use_llm={use_llm}, events_count={len(request.events)}, turns_count={len(request.turns)}")

    try:
        # pipeline_cache 사용하여 Issue Cards 생성
        if request.content_hash:
            # content_hash가 있으면 pipeline_cache 사용
            issue_cards = get_or_create_issue_cards(
                turns=request.turns,
                events=request.events,
                session_meta=request.session_meta,
                content_hash=request.content_hash,
                use_llm=use_llm,
                timeline_sections=request.timeline_sections or [],
            )

            logger.info(f"[ISSUES API] issues_count={len(issue_cards)}, use_llm={use_llm}")

            return IssuesResponse(
                session_meta=request.session_meta,
                issues=issue_cards,
            )
        else:
            # content_hash가 없으면 기존 방식 사용 (하위 호환성)
            from backend.builders.issues_builder import build_issue_cards
            issue_cards = build_issue_cards(
                turns=request.turns,
                events=request.events,
                session_meta=request.session_meta,
                use_llm=use_llm,
                timeline_sections=request.timeline_sections,
            )

            logger.info(f"[ISSUES API] issues_count={len(issue_cards)}, use_llm={use_llm}")

            return IssuesResponse(
                session_meta=request.session_meta,
                issues=issue_cards,
            )
    except Exception as e:
        logger.error(f"[ISSUES API] Failed to build issue cards: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"Failed to build issue cards: {str(e)}"
        )

