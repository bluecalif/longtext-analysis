"""
Artifact 추출 모듈

마크다운 파일에서 파일/경로 후보를 추출합니다.
"""

import re
from typing import List


# 파일 경로 패턴 (보수적)
PATH_RE = re.compile(
    r"(?:(?:[\w.-]+[/\\])+[\w.-]+\.(?:md|mdc|py|ts|tsx|sql|json)|"
    r"TODOs\.md|[\w.-]+\.(?:md|mdc|py|ts|tsx|sql|json))",
    re.IGNORECASE,
)


def extract_path_candidates(text: str) -> List[str]:
    """
    파일/경로 후보 추출

    Args:
        text: 텍스트

    Returns:
        경로 후보 리스트 (중복 제거)
    """
    matches = PATH_RE.findall(text)
    # 중복 제거 및 정규화
    candidates = list(set(matches))
    return candidates

