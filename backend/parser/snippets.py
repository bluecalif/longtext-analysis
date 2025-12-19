"""
코드 스니펫 추출 모듈

마크다운 파일에서 코드 블록을 추출합니다.
"""

import re
from typing import List
from backend.core.models import CodeBlock


CODE_FENCE_RE = re.compile(
    r"```([a-zA-Z0-9_+-]+)?\n(.*?)```",
    re.DOTALL,
)


def extract_code_blocks(text: str, turn_index: int) -> List[CodeBlock]:
    """
    코드 펜스 추출

    Args:
        text: 텍스트
        turn_index: Turn 인덱스

    Returns:
        CodeBlock 리스트
    """
    blocks = []
    matches = CODE_FENCE_RE.finditer(text)

    for idx, match in enumerate(matches):
        lang = (match.group(1) or "").lower()
        code = match.group(2)

        blocks.append(
            CodeBlock(
                turn_index=turn_index,
                block_index=idx,
                lang=lang,
                code=code,
            )
        )

    return blocks
