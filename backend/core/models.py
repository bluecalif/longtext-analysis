"""
데이터 모델 정의

이 모듈은 파서, 빌더, API에서 사용하는 Pydantic 모델을 정의합니다.
"""

from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


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


class EventType(str, Enum):
    """이벤트 타입 Enum

    각 타입은 수행되는 활동(activity)을 명확히 표현합니다.
    Artifact 정보(파일 경로, 코드 블록 등)는 Event.artifacts 필드에 별도로 저장됩니다.
    """

    STATUS_REVIEW = "status_review"  # 상태 확인/리뷰
    PLAN = "plan"  # 계획 수립
    CODE_GENERATION = "code_generation"  # 코드 생성 (새로 추가)
    DEBUG = "debug"  # 문제 해결
    COMPLETION = "completion"  # 완료
    NEXT_STEP = "next_step"  # 다음 단계
    TURN = "turn"  # 일반 대화 (fallback)


class ArtifactAction(str, Enum):
    """Artifact Action 타입 Enum

    파일이나 코드 블록에 대해 수행된 작업의 종류를 나타냅니다.
    """

    READ = "read"  # 읽기/확인
    CREATE = "create"  # 생성
    MODIFY = "modify"  # 수정
    EXECUTE = "execute"  # 실행
    MENTION = "mention"  # 단순 언급 (기본값)


class Event(BaseModel):
    """이벤트 기본 모델 (정규화된 Turn)"""

    seq: int = 0  # 시퀀스 번호 (normalize_turns_to_events에서 부여)
    session_id: str = ""  # 세션 ID
    turn_ref: int  # 원본 Turn 인덱스
    phase: Optional[int] = None  # Phase 번호
    subphase: Optional[int] = None  # Subphase 번호
    type: EventType  # 이벤트 타입
    summary: str  # 요약
    artifacts: List[dict] = []  # 연결된 Artifact (파일 경로, 액션 등)
    snippet_refs: List[str] = []  # 연결된 스니펫 ID (Phase 5에서 생성될 ID)
    processing_method: str = "regex"  # "regex" 또는 "llm" (결과 파일에 기록)


class TimelineEvent(BaseModel):
    """Timeline 이벤트 모델"""

    seq: int  # 시퀀스 번호
    session_id: str  # 세션 ID
    phase: Optional[int] = None  # Phase 번호
    subphase: Optional[int] = None  # Subphase 번호
    type: EventType  # 이벤트 타입
    summary: str  # 요약
    artifacts: List[dict] = []  # 연결된 Artifact (파일 경로, 액션 등)
    snippet_refs: List[str] = []  # 연결된 스니펫 ID


class TimelineSection(BaseModel):
    """Timeline 섹션 모델 (주요 작업 항목)

    Phase/Subphase별로 주요 작업을 항목화하여 구조화된 Timeline을 생성합니다.
    각 섹션은 하나의 주요 작업 항목을 나타내며, 관련 Event들을 그룹화합니다.
    """

    section_id: str  # 섹션 ID (예: "6.7-main-task-1")
    title: str  # 작업 항목 제목
    summary: str  # 작업 내용 요약
    phase: Optional[int] = None  # Phase 번호
    subphase: Optional[int] = None  # Subphase 번호
    events: List[int] = []  # 관련 Event seq 리스트
    has_issues: bool = False  # 이슈 발생 여부
    issue_refs: List[str] = []  # 관련 Issue Card ID 리스트
    detailed_results: dict = {}  # 작업 결과 연결 정보
    # detailed_results 구조 예시:
    # {
    #   "code_snippets": ["snippet_id_1", "snippet_id_2"],  # 관련 코드 스니펫
    #   "files": ["path/to/file1.py", "path/to/file2.ts"],  # 관련 파일
    #   "artifacts": [{"path": "...", "action": "create"}],  # Artifact 정보
    #   "git_commit": "abc123def456",  # Git commit 해시 (선택적)
    # }


class IssueCard(BaseModel):
    """Issue Card 모델"""

    issue_id: str  # 이슈 ID (예: "ISS-003-1234")
    scope: dict  # 범위 (session_id, phase, subphase)
    title: str  # 이슈 제목
    symptoms: List[str] = []  # 증상 (주로 User 발화)
    root_cause: Optional[dict] = None  # 원인 (status: "confirmed" | "hypothesis", text: str)
    evidence: List[dict] = []  # 증거
    fix: List[dict] = []  # 조치 방법 (summary, snippet_refs)
    validation: List[str] = []  # 검증 방법
    related_artifacts: List[dict] = []  # 관련 파일
    snippet_refs: List[str] = []  # 관련 코드 스니펫 ID
    # Phase 4.7 추가 필드
    section_id: Optional[str] = None  # 연결된 Timeline Section ID
    section_title: Optional[str] = None  # 연결된 Timeline Section 제목
    related_events: List[int] = []  # 관련 Event seq 리스트
    related_turns: List[int] = []  # 관련 Turn 인덱스 리스트
    confidence_score: Optional[float] = None  # 추출 신뢰도 점수 (0.0 ~ 1.0)


class Snippet(BaseModel):
    """코드 스니펫 모델 (Phase 5)

    코드 블록을 별도로 저장하고 Timeline/Issue Cards와 링킹하기 위한 모델입니다.
    """

    snippet_id: str  # 스니펫 ID (예: "SNP-session-012-00-sql")
    lang: str  # 언어 (예: "sql", "python", "typescript")
    code: str  # 코드 내용
    source: dict  # 출처 정보 {turn_index: int, block_index: int}
    links: dict = {}  # 링크 정보 {issue_id?: str, event_seq?: int, paths?: List[str]}
    snippet_hash: str  # 중복 제거용 해시 (SHA-256)
    aliases: List[str] = []  # 중복 제거 시 원본 ID 목록 (선택적)
