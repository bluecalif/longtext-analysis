"""
Turn 블록 파싱 모듈

마크다운 파일을 Turn 블록으로 분할하고 파싱합니다.
"""

import re
from typing import List, Tuple
from backend.core.models import Turn
from backend.parser.snippets import extract_code_blocks, extract_code_blocks_with_positions
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

# 코드 블록 시작 패턴 (백틱 3개 이상)
CODE_FENCE_START_PATTERN = re.compile(r"^(\s*)(```+)([a-zA-Z0-9_+-]+)?\s*$")
# 코드 블록 종료 패턴 (백틱 3개 이상)
CODE_FENCE_END_PATTERN = re.compile(r"^(\s*)(```+)\s*$")


def is_valid_turn_separator(text: str, separator_pos: int, context_lines: int = 5) -> bool:
    """
    구분선이 Turn 구분자인지 확인 (마크다운 섹션 구분자와 구분)

    Args:
        text: 전체 텍스트
        separator_pos: 구분선 위치 (문자 인덱스)
        context_lines: 앞뒤로 확인할 줄 수

    Returns:
        True: Turn 구분자, False: 마크다운 섹션 구분자
    """
    lines = text.split("\n")
    char_pos = 0
    line_index = 0

    # 구분선이 있는 줄 찾기
    for i, line in enumerate(lines):
        if char_pos <= separator_pos < char_pos + len(line) + 1:
            line_index = i
            break
        char_pos += len(line) + 1

    # 앞뒤 컨텍스트 추출
    start_line = max(0, line_index - context_lines)
    end_line = min(len(lines), line_index + context_lines + 1)
    context = "\n".join(lines[start_line:end_line])

    # 앞뒤 컨텍스트에서 User/Cursor 라벨 확인
    has_speaker_before = bool(
        SPEAKER_RE.search("\n".join(lines[max(0, line_index - context_lines) : line_index]))
        or SPEAKER_FALLBACK_RE.search(
            "\n".join(lines[max(0, line_index - context_lines) : line_index])
        )
    )

    has_speaker_after = bool(
        SPEAKER_RE.search(
            "\n".join(lines[line_index + 1 : min(len(lines), line_index + context_lines + 1)])
        )
        or SPEAKER_FALLBACK_RE.search(
            "\n".join(lines[line_index + 1 : min(len(lines), line_index + context_lines + 1)])
        )
    )

    # 앞 또는 뒤에 Speaker 라벨이 있으면 Turn 구분자로 판단
    return has_speaker_before or has_speaker_after


def split_by_separator_with_context(text: str) -> List[str]:
    """
    컨텍스트 기반 구분자로 텍스트 분할 (코드블록 보호)

    참고: 이 함수는 더 이상 사용되지 않으며, split_to_turns_by_speaker()로 대체됨

    Args:
        text: 정규화된 텍스트

    Returns:
        Turn 블록 리스트
    """
    # 더 이상 사용되지 않는 함수이므로 Speaker 기준 분리로 대체
    return split_to_turns_by_speaker(text)

    # 2. 구분선 위치 찾기
    separator_positions = []
    for match in TURN_SPLIT_RE.finditer(protected_text):
        separator_positions.append(match.start())

    # 3. 유효한 구분선만 필터링 (컨텍스트 검증)
    valid_separators = []
    for pos in separator_positions:
        if is_valid_turn_separator(protected_text, pos):
            valid_separators.append(pos)

    # 4. 유효한 구분선으로 분할
    if not valid_separators:
        # 유효한 구분선이 없으면 fallback
        # 코드 블록 복원
        restored_text = protected_text
        for i, marker in enumerate(code_block_markers):
            restored_text = restored_text.replace(marker, code_blocks[i])
        return fallback_split_by_speaker(restored_text)

    # 구분선 기준으로 분할
    blocks = []
    start = 0
    for sep_pos in valid_separators:
        if sep_pos > start:
            block = protected_text[start:sep_pos].strip()
            if block:
                blocks.append(block)
        start = sep_pos + 3  # "---" 길이

    # 마지막 블록
    if start < len(protected_text):
        block = protected_text[start:].strip()
        if block:
            blocks.append(block)

    # 5. 코드 블록 복원
    restored_blocks = []
    for block in blocks:
        restored_block = block
        for i, marker in enumerate(code_block_markers):
            restored_block = restored_block.replace(marker, code_blocks[i])
        restored_blocks.append(restored_block)

    return restored_blocks


def split_to_turns_by_speaker(text: str) -> List[str]:
    """
    Turn 구분 패턴 기준으로 분할: `---` + 빈 줄(0개 이상) + `**User**` 또는 `**Cursor**`
    (단순화: 코드블록 보호 없이 직접 분할, 코드 블록은 parse_turn에서 추출)

    Args:
        text: 정규화된 텍스트

    Returns:
        Turn 블록 리스트
    """
    lines = text.split("\n")

    # Turn 구분 패턴 찾기: `---` + 빈 줄(0개 이상) + `**User**` 또는 `**Cursor**`
    turn_start_indices = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # `---` 구분선 확인
        if TURN_SPLIT_RE.match(line):
            # 다음 줄들 확인 (빈 줄 건너뛰기)
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1

            # Speaker 라벨 확인
            if j < len(lines):
                next_line = lines[j]
                speaker_match = SPEAKER_RE.match(next_line) or SPEAKER_FALLBACK_RE.match(next_line)
                if speaker_match:
                    # Turn 시작 위치 기록 (--- 포함)
                    turn_start_indices.append(i)
                    i = j  # Speaker 라벨 위치로 이동
                    continue

        i += 1

    # Turn 구분 위치 기준으로 분할
    turns = []
    if not turn_start_indices:
        # Turn 구분 패턴이 없으면 전체를 하나의 Turn으로
        turn_text = text.strip()
        if turn_text:
            turns.append(turn_text)
    else:
        # 첫 번째 Turn (시작 ~ 첫 번째 구분자)
        if turn_start_indices[0] > 0:
            first_turn = "\n".join(lines[:turn_start_indices[0]]).strip()
            if first_turn:
                turns.append(first_turn)

        # 중간 Turn들
        for idx in range(len(turn_start_indices)):
            start_idx = turn_start_indices[idx]
            end_idx = turn_start_indices[idx + 1] if idx + 1 < len(turn_start_indices) else len(lines)

            turn_lines = lines[start_idx:end_idx]
            turn_text = "\n".join(turn_lines).strip()
            if turn_text:
                turns.append(turn_text)

    return turns


def split_to_turns(text: str) -> List[str]:
    """
    Speaker 라벨 기준으로 Turn 블록 분할 (메인 로직)

    Args:
        text: 정규화된 텍스트

    Returns:
        Turn 블록 리스트
    """
    return split_to_turns_by_speaker(text)


def fallback_split_by_speaker(text: str) -> List[str]:
    """
    Speaker 라벨 기준으로 분할 (fallback, 코드블록 보호 없음)

    참고: 이 함수는 더 이상 사용되지 않으며, split_to_turns_by_speaker()로 대체됨
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

    # 코드 블록 추출 (위치 정보 포함)
    code_blocks_with_positions = extract_code_blocks_with_positions(block, turn_index)
    code_blocks = [cb for cb, _, _ in code_blocks_with_positions]

    # body에서 코드 블록 제거 (위치 정보 활용)
    lines = block.split("\n")
    code_block_line_indices = set()

    # 코드 블록이 포함된 라인 인덱스 수집 (시작/종료 라인 포함)
    for code_block, start_line, end_line in code_blocks_with_positions:
        for line_idx in range(start_line, end_line + 1):
            code_block_line_indices.add(line_idx)

    # 코드 블록이 포함된 라인 제외하여 body 생성
    body_lines = [
        line for idx, line in enumerate(lines) if idx not in code_block_line_indices
    ]

    # Speaker 라벨 제거
    body = "\n".join(body_lines)
    body = re.sub(r"^\s*\*\*(User|Cursor)\*\*\s*:?\s*", "", body, flags=re.MULTILINE)
    body = body.strip()

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
