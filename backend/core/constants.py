"""
상수 정의

이벤트 타입, Debug 트리거 패턴, Issue 상태 등 프로젝트 전역 상수를 정의합니다.
"""

import re
from enum import Enum
from backend.core.models import EventType


# Event 타입 Enum 값 (models.py의 EventType과 동일)
# 이미 models.py에 정의되어 있으므로 여기서는 참조만

# Debug 트리거 패턴 (정규식)
DEBUG_TRIGGERS = {
    "error": re.compile(
        r"(?i)\b(error|exception|stack trace|violates check constraint|constraint)\b"
    ),
    "root_cause": re.compile(
        r"(?i)\b(원인|Root cause|because|due to)\b"
    ),
    "fix": re.compile(
        r"(?i)\b(해결|조치|수정|patch|fix|ALTER TABLE|UPDATE|script)\b"
    ),
    "validation": re.compile(
        r"(?i)\b(검증|확인|테스트|scenario|check)\b"
    ),
}


class IssueStatus(str, Enum):
    """Issue 상태 Enum"""

    CONFIRMED = "confirmed"  # 원인 확인됨
    HYPOTHESIS = "hypothesis"  # 가설 (미확정)

