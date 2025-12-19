"""
텍스트 정규화 모듈

마크다운 파일의 텍스트를 정규화하여 파싱하기 쉽게 만듭니다.
"""

import re


def normalize_text(text: str, preserve_code_blocks: bool = True) -> str:
    """
    텍스트 정규화

    Args:
        text: 원본 텍스트
        preserve_code_blocks: 코드 블록 내부 보존 여부

    Returns:
        정규화된 텍스트
    """
    # 1. 줄바꿈 통일
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # 2. BOM 제거
    text = text.lstrip("\ufeff")

    if preserve_code_blocks:
        # 코드 블록 분리
        code_blocks = []
        pattern = r"```([a-zA-Z0-9_+-]+)?\n(.*?)```"

        def replace_code(match):
            idx = len(code_blocks)
            code_blocks.append(match.group(0))
            return f"__CODE_BLOCK_{idx}__"

        text = re.sub(pattern, replace_code, text, flags=re.DOTALL)

    # 3. 트레일링 공백 제거
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)

    # 4. 너무 긴 공백 축소 (3개 이상 → 2개)
    text = re.sub(r" {3,}", "  ", text)

    if preserve_code_blocks:
        # 코드 블록 복원
        for idx, code in enumerate(code_blocks):
            text = text.replace(f"__CODE_BLOCK_{idx}__", code)

    return text

