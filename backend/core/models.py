"""
데이터 모델 정의

이 모듈은 파서, 빌더, API에서 사용하는 Pydantic 모델을 정의합니다.
"""

from pydantic import BaseModel
from typing import Optional, List


class SessionMeta(BaseModel):
    """세션 메타데이터"""

    session_id: str
    exported_at: Optional[str] = None
    cursor_version: Optional[str] = None
    phase: Optional[int] = None
    subphase: Optional[int] = None
    source_doc: str


class CodeBlock(BaseModel):
    """코드 블록"""

    turn_index: int  # 어느 Turn에서 추출되었는지
    block_index: int  # Turn 내에서의 인덱스
    lang: str  # 언어 (빈 문자열 가능)
    code: str  # 코드 내용


class Turn(BaseModel):
    """Turn 블록 (User/Cursor 대화 단위)"""

    turn_index: int
    speaker: str  # "User", "Cursor", "Unknown"
    body: str  # 본문 텍스트 (코드 블록 제외)
    code_blocks: List[CodeBlock] = []  # 코드 블록 리스트
    path_candidates: List[str] = []  # 파일/경로 후보 리스트
