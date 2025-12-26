"""
Issue Cards 빌더 모듈

정규화된 이벤트와 Turn으로부터 Issue Cards를 생성합니다.
"""

import re
from typing import List, Optional
from backend.core.models import Event, EventType, Turn, SessionMeta, IssueCard
from backend.core.constants import DEBUG_TRIGGERS, IssueStatus

# 슬라이딩 윈도우 크기 (최근 N개 Turn 내에서 연결)
WINDOW_SIZE = 10

# Symptom 탐지 패턴 (User 발화에서 문제 제기)
SYMPTOM_PATTERN = re.compile(
    r"(?i)\b(없|안 보|에러|문제|왜|%\s*증가|%\s*감소|안 됨|실패|오류)\b"
)


def build_issue_cards(
    turns: List[Turn],
    events: List[Event],
    session_meta: SessionMeta,
) -> List[IssueCard]:
    """
    Turn과 Event로부터 Issue Cards 생성

    Args:
        turns: Turn 리스트
        events: Event 리스트
        session_meta: 세션 메타데이터

    Returns:
        IssueCard 리스트
    """
    issue_cards = []

    # 1. Symptom seed 탐지 (User 발화에서 문제 제기)
    seeds = find_symptom_seeds(turns)

    for seed_idx, seed_turn in seeds:
        # 2. 슬라이딩 윈도우 내에서 연결 후보 탐색
        window_turns = turns[seed_idx : seed_idx + WINDOW_SIZE]
        window_events = [
            e
            for e in events
            if seed_idx <= e.turn_ref < seed_idx + WINDOW_SIZE
        ]

        # 3. Issue Card 구성
        issue_card = build_issue_card_from_window(
            seed_turn=seed_turn,
            window_turns=window_turns,
            window_events=window_events,
            seed_idx=seed_idx,
            session_meta=session_meta,
        )

        if issue_card:
            issue_cards.append(issue_card)

    return issue_cards


def find_symptom_seeds(turns: List[Turn]) -> List[tuple]:
    """
    User Turn에서 symptom 후보 탐지

    Returns:
        [(turn_index, Turn), ...]
    """
    seeds = []

    for idx, turn in enumerate(turns):
        if turn.speaker == "User" and SYMPTOM_PATTERN.search(turn.body):
            seeds.append((idx, turn))

    return seeds


def build_issue_card_from_window(
    seed_turn: Turn,
    window_turns: List[Turn],
    window_events: List[Event],
    seed_idx: int,
    session_meta: SessionMeta,
) -> Optional[IssueCard]:
    """
    슬라이딩 윈도우 내에서 Issue Card 구성

    Args:
        seed_turn: Symptom seed Turn
        window_turns: 윈도우 내 Turn 리스트
        window_events: 윈도우 내 Event 리스트
        seed_idx: Seed Turn 인덱스
        session_meta: 세션 메타데이터

    Returns:
        IssueCard 또는 None (조건 미충족 시)
    """
    # Symptom 추출 (User 발화)
    symptoms = [seed_turn.body[:500]]  # 처음 500자만

    # Root cause 추출 (Cursor turns에서)
    root_cause = None
    for turn in window_turns:
        if turn.speaker == "Cursor":
            if DEBUG_TRIGGERS["root_cause"].search(turn.body):
                root_cause = {
                    "status": IssueStatus.CONFIRMED.value,  # 또는 "hypothesis"
                    "text": extract_root_cause_text(turn.body),
                }
                break

    # Root cause가 없으면 hypothesis로 설정 (에러 패턴만 있는 경우)
    if not root_cause:
        for turn in window_turns:
            if turn.speaker == "Cursor" and DEBUG_TRIGGERS["error"].search(
                turn.body
            ):
                root_cause = {
                    "status": IssueStatus.HYPOTHESIS.value,
                    "text": turn.body[:300],  # 처음 300자
                }
                break

    # Fix 추출 (DebugEvent에서 코드 스니펫이 있는 경우)
    fixes = []
    for event in window_events:
        if event.type == EventType.DEBUG and event.snippet_refs:
            fixes.append(
                {
                    "summary": event.summary,
                    "snippet_refs": event.snippet_refs,
                }
            )
        # Fix 트리거가 있는 Turn도 포함
        elif event.type == EventType.DEBUG:
            turn = next(
                (t for t in window_turns if t.turn_index == event.turn_ref),
                None,
            )
            if turn and DEBUG_TRIGGERS["fix"].search(turn.body):
                fixes.append(
                    {
                        "summary": event.summary,
                        "snippet_refs": event.snippet_refs,
                    }
                )

    # Validation 추출
    validations = []
    for turn in window_turns:
        if DEBUG_TRIGGERS["validation"].search(turn.body):
            validation_text = extract_validation_text(turn.body)
            if validation_text:
                validations.append(validation_text)

    # Root cause 또는 Fix 중 하나라도 있어야 카드 생성
    if not root_cause and not fixes:
        return None

    # Issue ID 생성
    issue_id = f"ISS-{seed_idx:03d}-{hash(seed_turn.body[:100]) % 10000:04d}"

    # Title 생성
    title = generate_issue_title(seed_turn, root_cause)

    # 관련 Artifact 수집
    related_artifacts = []
    for event in window_events:
        related_artifacts.extend(event.artifacts)

    # 중복 제거
    seen_paths = set()
    unique_artifacts = []
    for artifact in related_artifacts:
        path = artifact.get("path", "")
        if path and path not in seen_paths:
            seen_paths.add(path)
            unique_artifacts.append(artifact)

    # Snippet 참조 수집
    snippet_refs = []
    for event in window_events:
        snippet_refs.extend(event.snippet_refs)

    # 중복 제거
    snippet_refs = list(set(snippet_refs))

    return IssueCard(
        issue_id=issue_id,
        scope={
            "session_id": session_meta.session_id,
            "phase": session_meta.phase,
            "subphase": session_meta.subphase,
        },
        title=title,
        symptoms=symptoms,
        root_cause=root_cause,
        evidence=[],  # Phase 4에서는 기본 구조만, 추후 개선
        fix=fixes,
        validation=validations,
        related_artifacts=unique_artifacts,
        snippet_refs=snippet_refs,
    )


def extract_root_cause_text(text: str) -> str:
    """
    Root cause 텍스트 추출

    Args:
        text: Turn 본문

    Returns:
        Root cause 텍스트 (최대 300자)
    """
    # Root cause 패턴 이후의 텍스트 추출
    match = DEBUG_TRIGGERS["root_cause"].search(text)
    if match:
        start_pos = match.end()
        extracted = text[start_pos:start_pos + 300].strip()
        return extracted

    return text[:300].strip()


def extract_validation_text(text: str) -> str:
    """
    Validation 텍스트 추출

    Args:
        text: Turn 본문

    Returns:
        Validation 텍스트 (최대 200자)
    """
    # Validation 패턴 이후의 텍스트 추출
    match = DEBUG_TRIGGERS["validation"].search(text)
    if match:
        start_pos = match.end()
        extracted = text[start_pos:start_pos + 200].strip()
        return extracted

    return text[:200].strip()


def generate_issue_title(seed_turn: Turn, root_cause: Optional[dict]) -> str:
    """
    Issue 제목 생성

    Args:
        seed_turn: Symptom seed Turn
        root_cause: Root cause 딕셔너리 (선택적)

    Returns:
        Issue 제목
    """
    # Symptom에서 첫 문장 추출
    symptom_text = seed_turn.body.split("\n")[0][:100]

    if root_cause:
        # Root cause가 있으면 결합
        root_cause_text = root_cause.get("text", "")[:50]
        if root_cause_text:
            return f"{symptom_text} - {root_cause_text}"

    return symptom_text

