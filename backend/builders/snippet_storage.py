"""
스니펫 저장 모듈 (Phase 5)

snippets.json 파일을 생성합니다.
"""

from pathlib import Path
from typing import List, Optional, Dict, Any
import json

from backend.core.models import Snippet, SessionMeta


def generate_snippets_json(
    snippets: List[Snippet],
    session_meta: SessionMeta,
    output_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    snippets.json 생성 (dict 반환)

    형식:
    {
        "session_meta": {
            "session_id": "...",
            "exported_at": "...",
            "cursor_version": "...",
            "phase": ...,
            "subphase": ...,
            "source_doc": "..."
        },
        "snippets": [
            {
                "snippet_id": "...",
                "lang": "...",
                "code": "...",
                "source": {"turn_index": ..., "block_index": ...},
                "links": {"issue_id": "...", "event_seq": [...], "paths": [...]},
                "snippet_hash": "...",
                "aliases": [...]
            }
        ]
    }

    Args:
        snippets: Snippet 리스트
        session_meta: 세션 메타데이터
        output_dir: 출력 디렉토리 (선택적, None이면 파일 저장 안 함)

    Returns:
        snippets.json 딕셔너리
    """
    # session_meta를 딕셔너리로 변환
    session_meta_dict = session_meta.model_dump()

    # snippets를 딕셔너리 리스트로 변환
    snippets_list = [snippet.model_dump() for snippet in snippets]

    # snippets.json 구조 생성
    snippets_json = {
        "session_meta": session_meta_dict,
        "snippets": snippets_list,
    }

    # 파일 저장 (output_dir이 제공된 경우)
    if output_dir is not None:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        snippets_file = output_dir / "snippets.json"
        with open(snippets_file, "w", encoding="utf-8") as f:
            json.dump(snippets_json, f, ensure_ascii=False, indent=2)

    return snippets_json
