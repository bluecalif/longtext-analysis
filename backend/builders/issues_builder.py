"""
Issue Cards 빌더 모듈

정규화된 이벤트와 Turn으로부터 Issue Cards를 생성합니다.
Phase 4.7: Timeline Section을 활용한 개선된 Issue Card 생성
"""

import re
from typing import List, Optional, Dict, Tuple
from collections import defaultdict
from backend.core.models import (
    Event,
    EventType,
    Turn,
    SessionMeta,
    IssueCard,
    TimelineSection,
)
from backend.core.constants import DEBUG_TRIGGERS, IssueStatus, USE_LLM_BY_DEFAULT

# 슬라이딩 윈도우 크기 (최근 N개 Turn 내에서 연결)
WINDOW_SIZE = 10

# Symptom 탐지 패턴 (User 발화에서 문제 제기)
SYMPTOM_PATTERN = re.compile(
    r"(?i)\b(없|안 보|에러|문제|왜|%\s*증가|%\s*감소|안 됨|실패|오류)\b"
)

# DEBUG 이벤트 클러스터링: 최대 거리 (seq 차이)
DEBUG_CLUSTER_MAX_DISTANCE = 5


def build_issue_cards(
    turns: List[Turn],
    events: List[Event],
    session_meta: SessionMeta,
    use_llm: bool = USE_LLM_BY_DEFAULT,
    timeline_sections: Optional[List[TimelineSection]] = None,
) -> List[IssueCard]:
    """
    Turn과 Event로부터 Issue Cards 생성 (Phase 4.7 개선 버전)

    ⚠️ 중요: 기본적으로 LLM을 사용합니다 (use_llm=True).
    패턴 기반을 사용하려면 명시적으로 use_llm=False를 전달하세요.

    Args:
        turns: Turn 리스트
        events: Event 리스트
        session_meta: 세션 메타데이터
        use_llm: LLM 사용 여부 (기본값: True, USE_LLM_BY_DEFAULT 상수 사용)
        timeline_sections: Timeline Section 리스트 (선택적, Phase 4.7)

    Returns:
        IssueCard 리스트
    """
    issue_cards = []

    # Phase 4.7: Timeline Section이 제공된 경우 새로운 로직 사용
    if timeline_sections:
        # 1. DEBUG 이벤트 클러스터링 (논리적 이슈 단위로 그룹화)
        debug_clusters = cluster_debug_events(events)

        # 2. 각 클러스터에 대해 Issue Card 생성
        for cluster_events in debug_clusters:
            # 3. Timeline Section 매칭
            matched_section = match_timeline_section(cluster_events, timeline_sections)

            # 4. 통합 컨텍스트 구성 (Section + Events + Turns)
            related_turns = get_related_turns(cluster_events, turns)

            # 5. Issue Card 생성
            issue_card = build_issue_card_from_cluster(
                cluster_events=cluster_events,
                related_turns=related_turns,
                matched_section=matched_section,
                session_meta=session_meta,
                use_llm=use_llm,
            )

            if issue_card:
                issue_cards.append(issue_card)
    else:
        # 기존 로직 (하위 호환성)
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
                use_llm=use_llm,
            )

            if issue_card:
                issue_cards.append(issue_card)

    return issue_cards


def cluster_debug_events(events: List[Event]) -> List[List[Event]]:
    """
    DEBUG 이벤트를 논리적 이슈 단위로 클러스터링

    Args:
        events: Event 리스트

    Returns:
        DEBUG 이벤트 클러스터 리스트 (각 클러스터는 하나의 논리적 이슈)
    """
    # DEBUG 이벤트만 필터링
    debug_events = [e for e in events if e.type == EventType.DEBUG]

    if not debug_events:
        return []

    # seq 순서로 정렬
    debug_events.sort(key=lambda e: e.seq)

    # 클러스터링: seq 차이가 MAX_DISTANCE 이내면 같은 클러스터
    clusters = []
    current_cluster = [debug_events[0]]

    for i in range(1, len(debug_events)):
        prev_event = debug_events[i - 1]
        curr_event = debug_events[i]

        # seq 차이 확인
        seq_diff = curr_event.seq - prev_event.seq

        if seq_diff <= DEBUG_CLUSTER_MAX_DISTANCE:
            # 같은 클러스터에 추가
            current_cluster.append(curr_event)
        else:
            # 새 클러스터 시작
            if current_cluster:
                clusters.append(current_cluster)
            current_cluster = [curr_event]

    # 마지막 클러스터 추가
    if current_cluster:
        clusters.append(current_cluster)

    return clusters


def match_timeline_section(
    cluster_events: List[Event],
    timeline_sections: List[TimelineSection],
) -> Optional[TimelineSection]:
    """
    DEBUG 이벤트 클러스터와 Timeline Section 매칭

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        timeline_sections: Timeline Section 리스트

    Returns:
        매칭된 TimelineSection 또는 None
    """
    if not cluster_events:
        return None

    # 클러스터의 Event seq 리스트
    cluster_event_seqs = {e.seq for e in cluster_events}

    # 각 Section의 events와 겹치는 정도 계산
    best_match = None
    best_overlap = 0

    for section in timeline_sections:
        section_event_seqs = set(section.events)

        # 겹치는 Event 수 계산
        overlap = len(cluster_event_seqs & section_event_seqs)

        if overlap > best_overlap:
            best_overlap = overlap
            best_match = section

    # 겹치는 Event가 1개 이상이면 매칭 성공
    if best_overlap > 0:
        return best_match

    return None


def get_related_turns(cluster_events: List[Event], turns: List[Turn]) -> List[Turn]:
    """
    클러스터 이벤트와 관련된 Turn 수집

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        turns: Turn 리스트

    Returns:
        관련 Turn 리스트
    """
    related_turn_indices = {e.turn_ref for e in cluster_events}

    # 윈도우 확장: 클러스터 앞뒤로 WINDOW_SIZE/2만큼 추가
    if related_turn_indices:
        min_turn_idx = min(related_turn_indices)
        max_turn_idx = max(related_turn_indices)

        # 윈도우 확장
        window_start = max(0, min_turn_idx - WINDOW_SIZE // 2)
        window_end = min(len(turns), max_turn_idx + WINDOW_SIZE // 2 + 1)

        related_turn_indices.update(range(window_start, window_end))

    # Turn 수집
    related_turns = [
        turn for idx, turn in enumerate(turns)
        if idx in related_turn_indices
    ]

    # turn_index 순서로 정렬
    related_turns.sort(key=lambda t: t.turn_index)

    return related_turns


def build_issue_card_from_cluster(
    cluster_events: List[Event],
    related_turns: List[Turn],
    matched_section: Optional[TimelineSection],
    session_meta: SessionMeta,
    use_llm: bool = USE_LLM_BY_DEFAULT,
) -> Optional[IssueCard]:
    """
    DEBUG 이벤트 클러스터로부터 Issue Card 생성 (Phase 4.7)

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        related_turns: 관련 Turn 리스트
        matched_section: 매칭된 TimelineSection (선택적)
        session_meta: 세션 메타데이터
        use_llm: LLM 사용 여부

    Returns:
        IssueCard 또는 None
    """
    if not cluster_events:
        return None

    # 통합 컨텍스트 기반 Issue 추출 (Phase 4.7.3)
    title = None
    symptom = None
    root_cause = None
    fix = None
    validation = None

    if use_llm:
        try:
            from backend.core.llm_service import extract_issue_with_llm
            
            integrated_result = extract_issue_with_llm(
                timeline_section=matched_section,
                cluster_events=cluster_events,
                related_turns=related_turns,
            )
            
            if integrated_result:
                title = integrated_result.get("title")
                symptom = integrated_result.get("symptom")
                root_cause = integrated_result.get("root_cause")
                fix = integrated_result.get("fix")
                validation = integrated_result.get("validation")
        except Exception as e:
            logger.warning(f"[WARNING] Integrated issue extraction failed: {e}, using fallback")

    # Fallback 적용 (일관성 있게 모든 필드에 적용)
    # Title fallback
    if not title:
        title = generate_issue_title_from_cluster(cluster_events, root_cause, matched_section)
    
    # Symptom fallback
    if not symptom:
        # 첫 번째 User Turn 사용
        for turn in related_turns:
            if turn.speaker == "User":
                symptom = turn.body[:500]
                break
    
    # Symptom이 없으면 카드 생성 안 함
    if not symptom:
        return None
    
    symptoms = [symptom] if symptom else []
    
    # Root cause fallback
    if not root_cause:
        for turn in related_turns:
            if turn.speaker == "Cursor":
                if DEBUG_TRIGGERS["root_cause"].search(turn.body):
                    root_cause = {
                        "status": IssueStatus.CONFIRMED.value,
                        "text": extract_root_cause_text(turn.body),
                    }
                    break
        
        # Root cause가 없으면 hypothesis로 설정
        if not root_cause:
            for turn in related_turns:
                if turn.speaker == "Cursor" and DEBUG_TRIGGERS["error"].search(turn.body):
                    root_cause = {
                        "status": IssueStatus.HYPOTHESIS.value,
                        "text": turn.body[:300],
                    }
                    break
    
    # Fix fallback
    if not fix:
        # 첫 번째 DEBUG 이벤트의 summary 사용
        for event in cluster_events:
            if event.type == EventType.DEBUG and event.snippet_refs:
                fix = {
                    "summary": event.summary,
                    "snippet_refs": event.snippet_refs,
                }
                break
    
    fixes = [fix] if fix else []
    
    # Validation fallback
    if not validation:
        for turn in related_turns:
            if DEBUG_TRIGGERS["validation"].search(turn.body):
                validation = extract_validation_text(turn.body)
                if validation:
                    break
    
    validations = [validation] if validation else []
    
    # Root cause 또는 Fix 중 하나라도 있어야 카드 생성
    if not root_cause and not fixes:
        return None

    # Issue ID 생성
    first_event = cluster_events[0]
    issue_id = f"ISS-{first_event.seq:03d}-{hash(first_event.summary[:100]) % 10000:04d}"

    # 관련 Artifact 수집
    related_artifacts = []
    seen_paths = set()
    for event in cluster_events:
        for artifact in event.artifacts:
            path = artifact.get("path", "")
            if path and path not in seen_paths:
                seen_paths.add(path)
                related_artifacts.append(artifact)

    # Snippet 참조 수집
    snippet_refs = []
    for event in cluster_events:
        snippet_refs.extend(event.snippet_refs)
    snippet_refs = list(set(snippet_refs))

    # 관련 Event seq 리스트
    related_event_seqs = [e.seq for e in cluster_events]

    # 관련 Turn 인덱스 리스트
    related_turn_indices = [t.turn_index for t in related_turns]

    # 신뢰도 점수 계산 (간단한 휴리스틱)
    confidence_score = calculate_confidence_score(cluster_events, root_cause, fixes)

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
        evidence=[],
        fix=fixes,
        validation=validations,
        related_artifacts=related_artifacts,
        snippet_refs=snippet_refs,
        # Phase 4.7 추가 필드
        section_id=matched_section.section_id if matched_section else None,
        section_title=matched_section.title if matched_section else None,
        related_events=related_event_seqs,
        related_turns=related_turn_indices,
        confidence_score=confidence_score,
    )


def generate_issue_title_from_cluster(
    cluster_events: List[Event],
    root_cause: Optional[dict],
    matched_section: Optional[TimelineSection],
) -> str:
    """
    클러스터로부터 Issue 제목 생성

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        root_cause: Root cause 딕셔너리 (선택적)
        matched_section: 매칭된 TimelineSection (선택적)

    Returns:
        Issue 제목
    """
    # Section 제목이 있으면 우선 사용
    if matched_section and matched_section.title:
        if root_cause:
            root_cause_text = root_cause.get("text", "")[:50]
            if root_cause_text:
                return f"{matched_section.title} - {root_cause_text}"
        return matched_section.title

    # 첫 번째 이벤트의 summary 사용
    if cluster_events:
        summary = cluster_events[0].summary[:100]
        if root_cause:
            root_cause_text = root_cause.get("text", "")[:50]
            if root_cause_text:
                return f"{summary} - {root_cause_text}"
        return summary

    return "Issue"


def calculate_confidence_score(
    cluster_events: List[Event],
    root_cause: Optional[dict],
    fixes: List[dict],
) -> float:
    """
    Issue Card 추출 신뢰도 점수 계산

    Args:
        cluster_events: DEBUG 이벤트 클러스터
        root_cause: Root cause 딕셔너리 (선택적)
        fixes: Fix 리스트

    Returns:
        신뢰도 점수 (0.0 ~ 1.0)
    """
    score = 0.0

    # Root cause가 있으면 +0.4
    if root_cause:
        score += 0.4
        # confirmed면 +0.2 추가
        if root_cause.get("status") == IssueStatus.CONFIRMED.value:
            score += 0.2

    # Fix가 있으면 +0.3
    if fixes:
        score += 0.3

    # 클러스터 크기가 적절하면 +0.1 (1~3개 이벤트)
    if 1 <= len(cluster_events) <= 3:
        score += 0.1

    return min(1.0, score)


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
    use_llm: bool = USE_LLM_BY_DEFAULT,
) -> Optional[IssueCard]:
    """
    슬라이딩 윈도우 내에서 Issue Card 구성

    Args:
        seed_turn: Symptom seed Turn
        window_turns: 윈도우 내 Turn 리스트
        window_events: 윈도우 내 Event 리스트
        seed_idx: Seed Turn 인덱스
        session_meta: 세션 메타데이터
        use_llm: LLM 사용 여부 (기본값: False)

    Returns:
        IssueCard 또는 None (조건 미충족 시)
    """
    # 통합 컨텍스트 기반 Issue 추출 (Phase 4.7.3)
    # window를 클러스터로 변환하여 extract_issue_with_llm() 사용
    title = None
    symptom = None
    root_cause = None
    fix = None
    validation = None

    if use_llm:
        try:
            from backend.core.llm_service import extract_issue_with_llm
            
            # window_events를 클러스터로 변환 (DEBUG 이벤트만)
            cluster_events = [e for e in window_events if e.type == EventType.DEBUG]
            
            if cluster_events:
                integrated_result = extract_issue_with_llm(
                    timeline_section=None,  # window 방식은 section 없음
                    cluster_events=cluster_events,
                    related_turns=window_turns,
                )
                
                if integrated_result:
                    title = integrated_result.get("title")
                    symptom = integrated_result.get("symptom")
                    root_cause = integrated_result.get("root_cause")
                    fix = integrated_result.get("fix")
                    validation = integrated_result.get("validation")
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"[WARNING] Integrated issue extraction failed: {e}, using fallback")

    # Fallback 적용 (일관성 있게 모든 필드에 적용)
    # Title fallback
    if not title:
        title = generate_issue_title(seed_turn, root_cause)
    
    # Symptom fallback
    if not symptom:
        symptom = seed_turn.body[:500]
    
    symptoms = [symptom] if symptom else []
    
    # Root cause fallback
    if not root_cause:
        for turn in window_turns:
            if turn.speaker == "Cursor":
                if DEBUG_TRIGGERS["root_cause"].search(turn.body):
                    root_cause = {
                        "status": IssueStatus.CONFIRMED.value,
                        "text": extract_root_cause_text(turn.body),
                    }
                    break
        
        # Root cause가 없으면 hypothesis로 설정
        if not root_cause:
            for turn in window_turns:
                if turn.speaker == "Cursor" and DEBUG_TRIGGERS["error"].search(turn.body):
                    root_cause = {
                        "status": IssueStatus.HYPOTHESIS.value,
                        "text": turn.body[:300],
                    }
                    break
    
    # Fix fallback
    if not fix:
        # 첫 번째 DEBUG 이벤트의 summary 사용
        for event in window_events:
            if event.type == EventType.DEBUG and event.snippet_refs:
                fix = {
                    "summary": event.summary,
                    "snippet_refs": event.snippet_refs,
                }
                break
    
    fixes = [fix] if fix else []
    
    # Validation fallback
    if not validation:
        for turn in window_turns:
            if DEBUG_TRIGGERS["validation"].search(turn.body):
                validation = extract_validation_text(turn.body)
                if validation:
                    break
    
    validations = [validation] if validation else []
    
    # Root cause 또는 Fix 중 하나라도 있어야 카드 생성
    if not root_cause and not fixes:
        return None

    # Issue ID 생성
    issue_id = f"ISS-{seed_idx:03d}-{hash(seed_turn.body[:100]) % 10000:04d}"

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

