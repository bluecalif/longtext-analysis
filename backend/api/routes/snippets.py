"""
Snippets API 라우터

코드 스니펫 처리 및 조회를 제공합니다.
"""

from fastapi import APIRouter, HTTPException, Path
from backend.builders.snippet_manager import process_snippets
from backend.core.models import (
    SnippetResponse,
    SnippetsProcessRequest,
    SnippetsProcessResponse,
)

router = APIRouter(prefix="/api/snippets", tags=["snippets"])

# 메모리 기반 스니펫 저장소 (세션별 관리)
# 실제 프로덕션에서는 DB나 파일 기반 저장소 사용 권장
_snippet_store: dict[str, dict[str, dict]] = {}  # {session_id: {snippet_id: snippet_dict}}


def _store_snippets(session_id: str, snippets: list) -> None:
    """
    스니펫을 메모리 저장소에 저장

    Args:
        session_id: 세션 ID
        snippets: Snippet 리스트
    """
    if session_id not in _snippet_store:
        _snippet_store[session_id] = {}

    for snippet in snippets:
        snippet_dict = snippet.model_dump() if hasattr(snippet, "model_dump") else snippet
        _snippet_store[session_id][snippet.snippet_id] = snippet_dict


@router.get("/{snippet_id}", response_model=SnippetResponse)
async def get_snippet(
    snippet_id: str = Path(..., description="스니펫 ID"),
):
    """
    스니펫 ID로 스니펫을 조회합니다.

    Args:
        snippet_id: 스니펫 ID (형식: SNP-{session_id}-{turn_index}-{block_index}-{lang})

    Returns:
        SnippetResponse: 스니펫 정보

    Raises:
        HTTPException: 스니펫을 찾을 수 없을 때
    """
    # snippet_id에서 session_id 추출 (SNP-{session_id}-... 형식)
    parts = snippet_id.split("-", 2)
    if len(parts) < 3:
        raise HTTPException(
            status_code=400, detail=f"Invalid snippet_id format: {snippet_id}"
        )

    extracted_session_id = parts[1]  # session_id 부분

    # 저장소에서 조회
    if extracted_session_id not in _snippet_store:
        raise HTTPException(
            status_code=404,
            detail=f"Snippet not found: {snippet_id} (session not found)",
        )

    session_store = _snippet_store[extracted_session_id]
    if snippet_id not in session_store:
        raise HTTPException(
            status_code=404, detail=f"Snippet not found: {snippet_id}"
        )

    snippet_dict = session_store[snippet_id]

    # Snippet 모델로 변환 (이미 dict이므로 직접 사용)
    from backend.core.models import Snippet

    snippet = Snippet(**snippet_dict)

    return SnippetResponse(snippet=snippet)


@router.post("/process", response_model=SnippetsProcessResponse)
async def process_snippets_endpoint(request: SnippetsProcessRequest):
    """
    스니펫을 처리합니다 (변환, 중복 제거, 링킹).

    Args:
        request: SnippetsProcessRequest (session_meta, turns, events, issue_cards)

    Returns:
        SnippetsProcessResponse: 처리된 스니펫 리스트, 업데이트된 이벤트 리스트, 업데이트된 Issue Card 리스트

    Raises:
        HTTPException: 스니펫 처리 실패 시
    """
    try:
        # process_snippets 호출
        snippets, updated_events, updated_issue_cards = process_snippets(
            turns=request.turns,
            events=request.events,
            issue_cards=request.issue_cards,
            session_meta=request.session_meta,
        )

        # 메모리 저장소에 저장
        _store_snippets(request.session_meta.session_id, snippets)

        # SnippetsProcessResponse 생성
        return SnippetsProcessResponse(
            session_meta=request.session_meta,
            snippets=snippets,
            events=updated_events,
            issue_cards=updated_issue_cards,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to process snippets: {str(e)}"
        )

