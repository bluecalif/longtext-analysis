"""
Export API 라우터

Timeline, Issue Cards, 전체 산출물을 JSON/Markdown/ZIP 형식으로 다운로드합니다.
"""

import json
import zipfile
import tempfile
from pathlib import Path
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, Response
from backend.render.render_md import render_timeline_md, render_issues_md
from backend.core.models import (
    ExportTimelineRequest,
    ExportIssuesRequest,
    ExportAllRequest,
    ExportFormat,
)

router = APIRouter(prefix="/api/export", tags=["export"])


@router.post("/timeline")
async def export_timeline(request: ExportTimelineRequest):
    """
    Timeline을 JSON 또는 Markdown 형식으로 다운로드합니다.

    Args:
        request: ExportTimelineRequest (session_meta, sections, events, format)

    Returns:
        FileResponse: 다운로드할 파일 (JSON 또는 MD)

    Raises:
        HTTPException: Export 실패 시
    """
    try:
        if request.format == ExportFormat.JSON:
            # JSON 형식
            result = {
                "session_meta": request.session_meta.model_dump(),
                "sections": [section.model_dump() for section in request.sections],
                "events": [event.model_dump() for event in request.events],
            }

            # JSON 문자열 생성
            json_str = json.dumps(result, ensure_ascii=False, indent=2)

            # Response 반환
            return Response(
                content=json_str,
                media_type="application/json",
                headers={
                    "Content-Disposition": f'attachment; filename="timeline_{request.session_meta.session_id}.json"'
                },
            )
        else:
            # Markdown 형식
            md_content = render_timeline_md(
                session_meta=request.session_meta,
                sections=request.sections,
                events=request.events,
            )

            # Response 반환
            return Response(
                content=md_content,
                media_type="text/markdown",
                headers={
                    "Content-Disposition": f'attachment; filename="timeline_{request.session_meta.session_id}.md"'
                },
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to export timeline: {str(e)}"
        )


@router.post("/issues")
async def export_issues(request: ExportIssuesRequest):
    """
    Issue Cards를 JSON 또는 Markdown 형식으로 다운로드합니다.

    Args:
        request: ExportIssuesRequest (session_meta, issues, format)

    Returns:
        FileResponse: 다운로드할 파일 (JSON 또는 MD)

    Raises:
        HTTPException: Export 실패 시
    """
    try:
        if request.format == ExportFormat.JSON:
            # JSON 형식
            result = {
                "session_meta": request.session_meta.model_dump(),
                "issues": [issue.model_dump() for issue in request.issues],
            }

            # JSON 문자열 생성
            json_str = json.dumps(result, ensure_ascii=False, indent=2)

            # Response 반환
            return Response(
                content=json_str,
                media_type="application/json",
                headers={
                    "Content-Disposition": f'attachment; filename="issues_{request.session_meta.session_id}.json"'
                },
            )
        else:
            # Markdown 형식
            md_content = render_issues_md(
                session_meta=request.session_meta,
                issues=request.issues,
            )

            # Response 반환
            return Response(
                content=md_content,
                media_type="text/markdown",
                headers={
                    "Content-Disposition": f'attachment; filename="issues_{request.session_meta.session_id}.md"'
                },
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to export issues: {str(e)}"
        )


@router.post("/all")
async def export_all(request: ExportAllRequest):
    """
    전체 산출물을 ZIP 파일로 다운로드합니다.

    Args:
        request: ExportAllRequest (session_meta, sections, events, issues, snippets, format)

    Returns:
        FileResponse: 다운로드할 ZIP 파일

    Raises:
        HTTPException: Export 실패 시
    """
    try:
        # 임시 디렉토리 생성
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            session_id = request.session_meta.session_id

            # 1. Timeline 파일 생성
            if request.format == ExportFormat.JSON:
                timeline_file = temp_path / "timeline.json"
                timeline_data = {
                    "session_meta": request.session_meta.model_dump(),
                    "sections": [
                        section.model_dump() for section in request.sections
                    ],
                    "events": [event.model_dump() for event in request.events],
                }
                with open(timeline_file, "w", encoding="utf-8") as f:
                    json.dump(timeline_data, f, ensure_ascii=False, indent=2)
            else:
                timeline_file = temp_path / "timeline.md"
                timeline_content = render_timeline_md(
                    session_meta=request.session_meta,
                    sections=request.sections,
                    events=request.events,
                )
                with open(timeline_file, "w", encoding="utf-8") as f:
                    f.write(timeline_content)

            # 2. Issues 파일 생성
            if request.format == ExportFormat.JSON:
                issues_file = temp_path / "issues.json"
                issues_data = {
                    "session_meta": request.session_meta.model_dump(),
                    "issues": [issue.model_dump() for issue in request.issues],
                }
                with open(issues_file, "w", encoding="utf-8") as f:
                    json.dump(issues_data, f, ensure_ascii=False, indent=2)
            else:
                issues_file = temp_path / "issues.md"
                issues_content = render_issues_md(
                    session_meta=request.session_meta,
                    issues=request.issues,
                )
                with open(issues_file, "w", encoding="utf-8") as f:
                    f.write(issues_content)

            # 3. Snippets 파일 생성 (항상 JSON)
            snippets_file = temp_path / "snippets.json"
            snippets_data = {
                "session_meta": request.session_meta.model_dump(),
                "snippets": [snippet.model_dump() for snippet in request.snippets],
            }
            with open(snippets_file, "w", encoding="utf-8") as f:
                json.dump(snippets_data, f, ensure_ascii=False, indent=2)

            # 4. ZIP 파일 생성
            zip_file = temp_path / f"export_{session_id}.zip"
            with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(timeline_file, timeline_file.name)
                zipf.write(issues_file, issues_file.name)
                zipf.write(snippets_file, snippets_file.name)

            # 5. ZIP 파일을 읽어서 Response 반환
            # FileResponse는 파일 경로를 받지만, 임시 파일이므로
            # 파일 내용을 읽어서 Response로 반환
            with open(zip_file, "rb") as f:
                zip_content = f.read()

            return Response(
                content=zip_content,
                media_type="application/zip",
                headers={
                    "Content-Disposition": f'attachment; filename="export_{session_id}.zip"'
                },
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to export all: {str(e)}"
        )

