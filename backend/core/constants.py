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
    "root_cause": re.compile(r"(?i)\b(원인|Root cause|because|due to)\b"),
    "fix": re.compile(r"(?i)\b(해결|조치|수정|patch|fix|ALTER TABLE|UPDATE|script)\b"),
    "validation": re.compile(r"(?i)\b(검증|확인|테스트|scenario|check)\b"),
}


class IssueStatus(str, Enum):
    """Issue 상태 Enum"""

    CONFIRMED = "confirmed"  # 원인 확인됨
    HYPOTHESIS = "hypothesis"  # 가설 (미확정)


# 파일 타입 목록 (Artifact 추출에서 사용)
# backend/parser/artifacts.py의 PATH_RE 패턴과 일치해야 함
FILE_TYPES = [
    "md",      # Markdown
    "mdc",     # Markdown (Cursor)
    "py",      # Python
    "ts",      # TypeScript
    "tsx",     # TypeScript React
    "sql",     # SQL
    "json",    # JSON
]


# ============================================================================
# ⚠️ 중요: LLM 사용 규칙 (프로젝트 전역)
# ============================================================================

# LLM 사용 기본값 (프로젝트 전역 규칙)
# 모든 빌더 함수는 기본적으로 LLM을 사용합니다.
# 패턴 기반(REGEX)은 LLM 실패 시 fallback으로만 사용됩니다.
USE_LLM_BY_DEFAULT = True

# LLM 모델 상수 (프로젝트 전역)
# 커서룰(.cursor/rules/llm-service.mdc)에 명시된 모델 사용
LLM_MODEL = "gpt-4.1-mini"

# LLM 사용 규칙 문서
LLM_USAGE_RULES = """
LLM 사용 규칙 (프로젝트 전역):

1. 기본 원칙:
   - 모든 빌더 함수의 기본값은 use_llm=True입니다.
   - 패턴 기반(REGEX)은 LLM 실패 시 fallback으로만 사용됩니다.
   - 테스트에서 패턴 기반을 사용하려면 명시적으로 use_llm=False를 전달하세요.

2. 함수 기본값:
   - normalize_turns_to_events(..., use_llm=USE_LLM_BY_DEFAULT)
   - build_structured_timeline(..., use_llm=USE_LLM_BY_DEFAULT)
   - build_issue_cards(..., use_llm=USE_LLM_BY_DEFAULT)

3. 테스트 규칙:
   - test_*_with_llm(): LLM 사용 (명시적)
   - test_*_pattern() 또는 test_*_no_llm(): 패턴 기반 (명시적)
   - 그 외: 기본값 사용 (LLM)

4. API 규칙 (Phase 6+):
   - 모든 API 엔드포인트도 기본적으로 LLM을 사용합니다.
   - 클라이언트가 명시적으로 use_llm=false를 전달하지 않는 한 LLM 사용.

5. 주의사항:
   - 다음 세션에서 코드를 작성할 때도 이 규칙을 따라야 합니다.
   - 새로운 빌더 함수를 추가할 때도 use_llm=True를 기본값으로 설정하세요.
   - 이 규칙은 .cursor/rules/llm-default-rule.mdc에도 문서화되어 있습니다.
"""
