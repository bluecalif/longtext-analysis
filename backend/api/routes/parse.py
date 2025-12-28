"""
Parse API 라우터

마크다운 파일을 업로드하고 파싱하여 이벤트로 정규화합니다.
"""

import logging
import hashlib
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from backend.core.pipeline_cache import (
    get_or_create_parsed_data,
    get_or_create_events,
)
from backend.core.models import ParseResponse, SessionMeta, Turn
from backend.core.constants import USE_LLM_BY_DEFAULT

router = APIRouter(prefix="/api/parse", tags=["parse"])
logger = logging.getLogger(__name__)

# 파일 크기 제한 (10MB)
MAX_FILE_SIZE = 10 * 1024 * 1024


@router.post("", response_model=ParseResponse)
async def parse_file(
    file: UploadFile = File(...),
    use_llm: bool = Query(
        default=USE_LLM_BY_DEFAULT,
        description="LLM 사용 여부 (기본값: True)",
    ),
):
    """
    마크다운 파일을 업로드하고 파싱합니다.

    Args:
        file: 업로드할 마크다운 파일 (.md)
        use_llm: LLM 사용 여부 (기본값: True, USE_LLM_BY_DEFAULT 상수 사용)

    Returns:
        ParseResponse: 세션 메타데이터, Turn 리스트, Event 리스트

    Raises:
        HTTPException: 파일 검증 실패 또는 파싱 오류 시
    """
    # 1. 파일 확장자 검증
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    if not file.filename.endswith(".md"):
        raise HTTPException(
            status_code=400, detail="Only .md files are supported"
        )

    # 2. 파일 크기 검증
    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size: {MAX_FILE_SIZE / 1024 / 1024:.0f}MB",
        )

    # 3. UTF-8 인코딩 검증
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError as e:
        raise HTTPException(
            status_code=400, detail=f"Invalid UTF-8 encoding: {str(e)}"
        )

    # 4. 파일 내용 해시 계산 (캐시 키 생성용)
    hash_obj = hashlib.sha256(content)
    content_hash = hash_obj.hexdigest()[:16]

    # 5. 마크다운 파싱 (pipeline_cache 사용)
    try:
        parsed_data = get_or_create_parsed_data(
            content_hash=content_hash,
            content=content,
            source_doc=file.filename
        )

        # 딕셔너리를 모델로 변환
        session_meta = SessionMeta(**parsed_data["session_meta"])
        turns = [Turn(**turn_dict) for turn_dict in parsed_data["turns"]]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to parse markdown: {str(e)}"
        )

    logger.info(f"[PARSE API] use_llm={use_llm}, turns_count={len(turns)}, filename={file.filename}")

    # 6. 이벤트 정규화 (pipeline_cache 사용)
    try:
        events, session_meta = get_or_create_events(
            parsed_data=parsed_data,
            content_hash=content_hash,
            use_llm=use_llm
        )
        logger.info(f"[PARSE API] events_count={len(events)}, use_llm={use_llm}")
    except Exception as e:
        logger.error(f"[PARSE API] Failed to normalize events: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"Failed to normalize events: {str(e)}"
        )

    # 7. 응답 반환 (content_hash 포함)
    return ParseResponse(
        session_meta=session_meta,
        turns=turns,
        events=events,
        content_hash=content_hash,
    )

