"""
세션 메타데이터 추출 모듈

마크다운 파일에서 세션 메타데이터(Phase, Subphase, Exported at, Cursor version)를 추출합니다.
"""

import re
from typing import Optional
from backend.core.models import SessionMeta


# 정규식 패턴
EXPORTED_AT_RE = re.compile(
    r"(?i)Exported\s+(\d{4}-\d{2}-\d{2}[^,\n]*?(?:KST|UTC|GMT|[+\-]\d{2}:\d{2})?)",
    re.MULTILINE,
)

CURSOR_VERSION_RE = re.compile(
    r"(?i)\bCursor\s+(\d+\.\d+\.\d+)\b",
    re.MULTILINE,
)

PHASE_RE = re.compile(
    r"(?i)\bPhase\s+(\d+)\b",
    re.MULTILINE,
)

SUBPHASE_RE = re.compile(
    r"(?i)\bSub\s*Phase\s+(\d+)\b",
    re.MULTILINE,
)


def extract_session_meta(text: str, source_doc: str) -> SessionMeta:
    """
    상단 2000~4000 chars 범위에서 best-effort로 메타 추출

    Args:
        text: 원본 텍스트
        source_doc: 소스 문서 경로

    Returns:
        SessionMeta 객체
    """
    # 상단 범위 추출
    header_text = text[:4000]

    # exported_at 추출
    exported_at_match = EXPORTED_AT_RE.search(header_text)
    exported_at = exported_at_match.group(1) if exported_at_match else None

    # cursor_version 추출
    version_match = CURSOR_VERSION_RE.search(header_text)
    cursor_version = version_match.group(1) if version_match else None

    # phase 추출
    phase_match = PHASE_RE.search(header_text)
    phase = int(phase_match.group(1)) if phase_match else None

    # subphase 추출
    subphase_match = SUBPHASE_RE.search(header_text)
    subphase = int(subphase_match.group(1)) if subphase_match else None

    # session_id 생성
    if exported_at:
        # 문자열 정규화: 공백 → _, : 제거
        session_id_base = exported_at.replace(" ", "_").replace(":", "")
        session_id = f"cursor_export_{session_id_base}"
    else:
        session_id = f"cursor_export_unknown_{hash(text) % 10000}"

    return SessionMeta(
        session_id=session_id,
        exported_at=exported_at,
        cursor_version=cursor_version,
        phase=phase,
        subphase=subphase,
        source_doc=source_doc,
    )

