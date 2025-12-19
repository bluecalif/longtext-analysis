"""
마크다운 파서 모듈

Cursor IDE export 마크다운 파일을 구조화된 데이터로 파싱합니다.
"""

from backend.parser.normalize import normalize_text
from backend.parser.meta import extract_session_meta
from backend.parser.turns import split_to_turns, parse_turn, check_parse_health
from backend.core.models import SessionMeta, Turn, CodeBlock
from typing import Dict, List


def parse_markdown(text: str, source_doc: str = "input.md") -> Dict:
    """
    마크다운 파일 전체 파싱

    Args:
        text: 마크다운 파일 내용
        source_doc: 소스 문서 경로

    Returns:
        {
            "session_meta": SessionMeta,
            "turns": List[Turn],
            "code_blocks": List[CodeBlock],
            "artifacts": List[str]
        }
    """
    # 1. 정규화
    normalized = normalize_text(text)

    # 2. 메타 추출
    session_meta = extract_session_meta(normalized, source_doc)

    # 3. Turn 분할
    turn_blocks = split_to_turns(normalized)

    # 4. Turn 파싱
    turns = []
    for idx, block in enumerate(turn_blocks):
        turn = parse_turn(block, idx)
        turns.append(turn)

    # 5. 코드 블록 수집
    all_code_blocks = []
    for turn in turns:
        all_code_blocks.extend(turn.code_blocks)

    # 6. Artifact 수집
    all_paths = []
    for turn in turns:
        all_paths.extend(turn.path_candidates)

    return {
        "session_meta": session_meta,
        "turns": turns,
        "code_blocks": all_code_blocks,
        "artifacts": list(set(all_paths)),
    }
