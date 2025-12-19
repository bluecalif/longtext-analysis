"""
Turn 블록 파싱 모듈

마크다운 파일을 Turn 블록으로 분할하고 파싱합니다.
"""

import re
from typing import List
from backend.core.models import Turn
from backend.parser.snippets import extract_code_blocks
from backend.parser.artifacts import extract_path_candidates


# 구분선 패턴
TURN_SPLIT_RE = re.compile(r"^\s*---\s*$", re.MULTILINE)

# Speaker 라벨 패턴
SPEAKER_RE = re.compile(
    r"^\s*\*\*(User|Cursor)\*\*\s*:?\s*$",
    re.MULTILINE,
)

# Fallback: 굵게 누락된 경우
SPEAKER_FALLBACK_RE = re.compile(
    r"^\s*(User|Cursor)\s*:?\s*$",
    re.MULTILINE,
)


def split_to_turns(text: str) -> List[str]:
    """
    구분선 기준으로 Turn 블록 분할

    Args:
        text: 정규화된 텍스트

    Returns:
        Turn 블록 리스트
    """
    # 1차: 구분선 기준 분할
    blocks = TURN_SPLIT_RE.split(text)
    blocks = [b.strip() for b in blocks if b.strip()]

    # 구분선이 없거나 너무 적으면 fallback
    if len(blocks) < 2:
        return fallback_split_by_speaker(text)

    return blocks


def fallback_split_by_speaker(text: str) -> List[str]:
    """
    Speaker 라벨 기준으로 분할 (fallback)
    """
    turns = []
    current_turn = []
    current_speaker = None

    for line in text.split("\n"):
        speaker_match = SPEAKER_RE.match(line) or SPEAKER_FALLBACK_RE.match(line)

        if speaker_match:
            # 새 Turn 시작
            if current_turn:
                turns.append("\n".join(current_turn))
            current_speaker = speaker_match.group(1)
            current_turn = [line]
        else:
            current_turn.append(line)

    if current_turn:
        turns.append("\n".join(current_turn))

    return turns


def parse_turn(block: str, turn_index: int) -> Turn:
    """
    Turn 블록 파싱

    Args:
        block: Turn 블록 텍스트
        turn_index: Turn 인덱스

    Returns:
        Turn 객체
    """
    # Speaker 추출
    speaker_match = SPEAKER_RE.search(block) or SPEAKER_FALLBACK_RE.search(block)
    speaker = speaker_match.group(1) if speaker_match else "Unknown"

    # 코드 블록 제거한 body 추출
    body = re.sub(r"```.*?```", "", block, flags=re.DOTALL)
    body = re.sub(r"^\s*\*\*(User|Cursor)\*\*\s*:?\s*", "", body, flags=re.MULTILINE)
    body = body.strip()

    # 코드 블록 추출
    code_blocks = extract_code_blocks(block, turn_index)

    # 파일 경로 후보 추출
    path_candidates = extract_path_candidates(block)

    return Turn(
        turn_index=turn_index,
        speaker=speaker,
        body=body,
        code_blocks=code_blocks,
        path_candidates=path_candidates,
    )


def check_parse_health(turns: List[Turn]) -> dict:
    """
    파싱 품질 검사

    Args:
        turns: Turn 리스트

    Returns:
        {
            "unknown_ratio": float,
            "warnings": List[str]
        }
    """
    total = len(turns)
    unknown_count = sum(1 for t in turns if t.speaker == "Unknown")
    unknown_ratio = unknown_count / total if total > 0 else 0.0

    warnings = []
    if unknown_ratio > 0.2:
        warnings.append(
            f"High Unknown speaker ratio: {unknown_ratio:.1%}. " "Format detection may have failed."
        )

    return {
        "unknown_ratio": unknown_ratio,
        "warnings": warnings,
    }
