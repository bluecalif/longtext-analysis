"""
코드 스니펫 추출 모듈

마크다운 파일에서 코드 블록을 추출합니다.
"""

import re
import logging
from typing import List, Tuple
from backend.core.models import CodeBlock


# 코드 펜스 시작 패턴 (백틱 3개 이상, 줄 시작 또는 중간)
CODE_FENCE_START_RE = re.compile(r"^(\s*)(```+)([a-zA-Z0-9_+-]+)?\s*$", re.MULTILINE)
# 코드 펜스 종료 패턴 (백틱 3개 이상)
CODE_FENCE_END_RE = re.compile(r"^(\s*)(```+)\s*$", re.MULTILINE)

logger = logging.getLogger(__name__)


def extract_code_blocks(text: str, turn_index: int, debug: bool = False) -> List[CodeBlock]:
    """
    코드 펜스 추출 (중첩 블록 처리)

    extract_code_blocks_with_positions()를 호출하여 코드 블록을 추출하고,
    위치 정보를 제외한 CodeBlock 리스트만 반환합니다.

    Args:
        text: 텍스트
        turn_index: Turn 인덱스
        debug: 디버그 로깅 활성화 여부

    Returns:
        CodeBlock 리스트
    """
    blocks_with_positions = extract_code_blocks_with_positions(text, turn_index, debug)
    return [code_block for code_block, _, _ in blocks_with_positions]


def extract_code_blocks_with_positions(
    text: str, turn_index: int, debug: bool = False
) -> List[Tuple[CodeBlock, int, int]]:
    """
    코드 펜스 추출 (위치 정보 포함, 중첩 블록 처리)

    중첩 레벨 추적을 통해 중첩된 코드 블록을 올바르게 처리합니다.

    핵심 규칙:
    - 언어태그 있는 펜스: 항상 시작 펜스 (nesting_level++)
    - 언어태그 없는 펜스:
      - nesting_level > 0이면 → 내부 블록 종료 (nesting_level--)
      - nesting_level = 0이면:
        - 다음 ``` 확인 (look-ahead)
        - 다음 ```가 언어태그 있으면 → 외부 블록 종료
        - 다음 ```가 언어태그 없으면 → 내부 블록 시작 (nesting_level++)
        - 다음 ```가 없으면 → 외부 블록 종료

    Args:
        text: 텍스트
        turn_index: Turn 인덱스
        debug: 디버그 로깅 활성화 여부

    Returns:
        List[Tuple[CodeBlock, start_line_idx, end_line_idx]]
        - CodeBlock: 코드 블록 객체
        - start_line_idx: 코드 펜스 시작 라인 인덱스 (0-based)
        - end_line_idx: 코드 펜스 종료 라인 인덱스 (0-based, 포함)
    """
    blocks_with_positions = []
    lines = text.split("\n")

    in_code_block = False
    nesting_level = 0  # 중첩 레벨: 0 = 외부 블록만, >0 = 내부 블록 있음
    current_code_lines = []
    current_lang = ""
    current_backtick_count = 0
    block_start_line = 0
    block_end_line = 0
    block_idx = 0

    def find_next_fence(start_idx: int) -> tuple[int, bool]:
        """
        다음 코드 펜스를 찾습니다.

        Returns:
            (line_idx, has_lang_tag): 다음 펜스의 라인 인덱스와 언어태그 여부
            다음 펜스가 없으면 (-1, False)
        """
        for i in range(start_idx + 1, len(lines)):
            line = lines[i]
            start_match = CODE_FENCE_START_RE.match(line)
            end_match = CODE_FENCE_END_RE.match(line)

            if start_match:
                has_lang = bool(start_match.group(3))
                return (i, has_lang)
            elif end_match:
                return (i, False)

        return (-1, False)

    for line_idx, line in enumerate(lines):
        start_match = CODE_FENCE_START_RE.match(line)
        end_match = CODE_FENCE_END_RE.match(line)

        # 언어태그 있는 펜스: 항상 시작 펜스
        if start_match and start_match.group(3):
            if not in_code_block:
                # 외부 블록 시작
                in_code_block = True
                nesting_level = 0
                current_lang = start_match.group(3).lower()
                current_backtick_count = len(start_match.group(2))
                block_start_line = line_idx
                current_code_lines = []
                if debug:
                    logger.debug(
                        f"[Turn {turn_index}] Line {line_idx}: Outer code block start (lang={current_lang}, backticks={current_backtick_count})"
                    )
                continue
            elif in_code_block:
                # 내부 블록 시작
                nesting_level += 1
                current_code_lines.append(line)
                if debug:
                    logger.debug(
                        f"[Turn {turn_index}] Line {line_idx}: Inner code block start (nesting_level={nesting_level})"
                    )
                continue

        # 언어태그 없는 펜스 처리
        if (start_match and not start_match.group(3)) or end_match:
            if not in_code_block:
                # 코드 블록 밖에서 언어태그 없는 펜스 → 시작 펜스로 처리
                in_code_block = True
                nesting_level = 0
                current_lang = ""
                current_backtick_count = len((start_match or end_match).group(2))
                block_start_line = line_idx
                current_code_lines = []
                if debug:
                    logger.debug(
                        f"[Turn {turn_index}] Line {line_idx}: Outer code block start (no lang, backticks={current_backtick_count})"
                    )
                continue

            # 코드 블록 안에서 언어태그 없는 펜스
            backtick_count = len((start_match or end_match).group(2))

            if nesting_level > 0:
                # 내부 블록이 열려있음 → 내부 블록 종료
                nesting_level -= 1
                current_code_lines.append(line)
                if debug:
                    logger.debug(
                        f"[Turn {turn_index}] Line {line_idx}: Inner code block end (nesting_level={nesting_level})"
                    )
                continue

            # nesting_level = 0: 외부 블록만 열려있음
            if backtick_count == current_backtick_count:
                # 백틱 개수 일치 → look-ahead로 종료 여부 확인
                next_fence_idx, next_has_lang = find_next_fence(line_idx)

                if next_fence_idx == -1:
                    # 다음 펜스 없음 → 외부 블록 종료
                    code = "\n".join(current_code_lines)
                    block_end_line = line_idx
                    code_block = CodeBlock(
                        turn_index=turn_index,
                        block_index=block_idx,
                        lang=current_lang,
                        code=code,
                    )
                    blocks_with_positions.append((code_block, block_start_line, block_end_line))
                    if debug:
                        logger.debug(
                            f"[Turn {turn_index}] Line {line_idx}: Outer code block end (extracted block {block_idx}, lines {block_start_line}-{block_end_line})"
                        )
                    block_idx += 1
                    in_code_block = False
                    nesting_level = 0
                    current_code_lines = []
                    current_lang = ""
                    current_backtick_count = 0
                    continue
                elif next_has_lang:
                    # 다음 펜스가 언어태그 있음 → 외부 블록 종료 (병렬)
                    code = "\n".join(current_code_lines)
                    block_end_line = line_idx
                    code_block = CodeBlock(
                        turn_index=turn_index,
                        block_index=block_idx,
                        lang=current_lang,
                        code=code,
                    )
                    blocks_with_positions.append((code_block, block_start_line, block_end_line))
                    if debug:
                        logger.debug(
                            f"[Turn {turn_index}] Line {line_idx}: Outer code block end (parallel, extracted block {block_idx}, lines {block_start_line}-{block_end_line})"
                        )
                    block_idx += 1
                    in_code_block = False
                    nesting_level = 0
                    current_code_lines = []
                    current_lang = ""
                    current_backtick_count = 0
                    continue
                else:
                    # 다음 펜스가 언어태그 없음 → 내부 블록 시작 (중첩)
                    nesting_level += 1
                    current_code_lines.append(line)
                    if debug:
                        logger.debug(
                            f"[Turn {turn_index}] Line {line_idx}: Inner code block start (nesting_level={nesting_level})"
                        )
                    continue
            else:
                # 백틱 개수 불일치 → 내용으로 처리
                current_code_lines.append(line)
                continue

        # 코드 블록 내용
        if in_code_block:
            current_code_lines.append(line)

    # Handle unclosed code blocks at the end of the text
    if in_code_block and current_code_lines:
        code = "\n".join(current_code_lines)
        block_end_line = len(lines) - 1
        code_block = CodeBlock(
            turn_index=turn_index,
            block_index=block_idx,
            lang=current_lang,
            code=code,
        )
        blocks_with_positions.append((code_block, block_start_line, block_end_line))
        if debug:
            logger.debug(
                f"[Turn {turn_index}] Unclosed code block extracted at end (block {block_idx}, lines {block_start_line}-{block_end_line})"
            )

    if debug:
        logger.debug(
            f"[Turn {turn_index}] Extraction complete: {len(blocks_with_positions)} blocks extracted with positions"
        )

    return blocks_with_positions
