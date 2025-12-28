"""
Timeline 빌더 모듈

정규화된 이벤트로부터 Timeline을 생성합니다.
"""

from typing import List, Optional, Dict, Set
from collections import defaultdict
from backend.core.models import (
    Event,
    TimelineEvent,
    TimelineSection,
    SessionMeta,
    EventType,
)
from backend.core.constants import USE_LLM_BY_DEFAULT


def build_timeline(
    events: List[Event],
    session_meta: SessionMeta,
) -> List[TimelineEvent]:
    """
    이벤트 리스트로부터 Timeline 생성

    Args:
        events: 정규화된 이벤트 리스트
        session_meta: 세션 메타데이터

    Returns:
        TimelineEvent 리스트
    """
    timeline = []

    for event in events:
        # Event를 TimelineEvent로 변환
        timeline_event = TimelineEvent(
            seq=event.seq,
            session_id=event.session_id or session_meta.session_id,
            phase=event.phase or session_meta.phase,
            subphase=event.subphase or session_meta.subphase,
            type=event.type,
            summary=event.summary,
            artifacts=event.artifacts,
            snippet_refs=event.snippet_refs,
        )
        timeline.append(timeline_event)

    return timeline


def build_structured_timeline(
    events: List[Event],
    session_meta: SessionMeta,
    issue_cards: Optional[List] = None,
    use_llm: bool = USE_LLM_BY_DEFAULT,
) -> Dict:
    """
    이벤트 리스트로부터 구조화된 Timeline 생성 (Phase 4.5)

    ⚠️ 중요: 기본적으로 LLM을 사용합니다 (use_llm=True).
    패턴 기반을 사용하려면 명시적으로 use_llm=False를 전달하세요.

    주요 작업 항목별로 그룹화하여 Timeline을 구조화합니다.

    Args:
        events: 정규화된 이벤트 리스트
        session_meta: 세션 메타데이터
        issue_cards: Issue Card 리스트 (이슈 연결용, 선택적)
        use_llm: LLM 사용 여부 (기본값: True, USE_LLM_BY_DEFAULT 상수 사용)

    Returns:
        {
            "sections": List[TimelineSection],  # 구조화된 섹션 리스트
            "events": List[TimelineEvent],  # 원본 이벤트 리스트 (하위 호환성)
        }
    """
    # 1. Phase/Subphase별로 이벤트 그룹화
    event_groups = _group_events_by_phase_subphase(events, session_meta)

    # 2. 각 그룹에서 주요 작업 항목 추출 (패턴 기반 또는 LLM)
    sections = []
    for (phase, subphase), group_events in event_groups.items():
        group_sections = _extract_main_tasks_from_group(
            group_events=group_events,
            phase=phase,
            subphase=subphase,
            session_meta=session_meta,
            issue_cards=issue_cards or [],
            use_llm=use_llm,
        )
        sections.extend(group_sections)

    # 3. 원본 이벤트 리스트도 반환 (하위 호환성)
    timeline_events = build_timeline(events, session_meta)

    return {
        "sections": sections,
        "events": timeline_events,
    }


def _group_events_by_phase_subphase(
    events: List[Event], session_meta: SessionMeta
) -> Dict[tuple, List[Event]]:
    """
    Phase/Subphase별로 이벤트 그룹화

    Returns:
        {(phase, subphase): [Event, ...], ...}
    """
    groups = defaultdict(list)

    for event in events:
        phase = event.phase or session_meta.phase
        subphase = event.subphase or session_meta.subphase
        key = (phase, subphase)
        groups[key].append(event)

    # seq 순서로 정렬
    for key in groups:
        groups[key].sort(key=lambda e: e.seq)

    return dict(groups)


def _extract_main_tasks_from_group(
    group_events: List[Event],
    phase: Optional[int],
    subphase: Optional[int],
    session_meta: SessionMeta,
    issue_cards: List,
    use_llm: bool = USE_LLM_BY_DEFAULT,
) -> List[TimelineSection]:
    """
    이벤트 그룹에서 주요 작업 항목 추출 (패턴 기반 또는 LLM)

    ⚠️ 중요: 기본적으로 LLM을 사용합니다 (use_llm=True).
    패턴 기반을 사용하려면 명시적으로 use_llm=False를 전달하세요.

    Args:
        group_events: 같은 Phase/Subphase의 이벤트 리스트
        phase: Phase 번호
        subphase: Subphase 번호
        session_meta: 세션 메타데이터
        issue_cards: Issue Card 리스트
        use_llm: LLM 사용 여부 (기본값: True, USE_LLM_BY_DEFAULT 상수 사용)

    Returns:
        TimelineSection 리스트
    """
    if not group_events:
        return []

    sections = []

    # LLM 기반 작업 항목 추출 (Phase 6.2: 부분 성공 처리)
    if use_llm:
        import logging

        logger = logging.getLogger(__name__)
        logger.info(
            f"[TIMELINE LLM] Starting LLM-based task extraction: "
            f"phase={phase}, subphase={subphase}, events_count={len(group_events)}"
        )

        try:
            from backend.core.llm_service import extract_main_tasks_with_llm

            llm_tasks = extract_main_tasks_with_llm(
                events=group_events,
                phase=phase,
                subphase=subphase,
            )

            # 빈 리스트 체크 추가
            if not llm_tasks:
                logger.warning(
                    f"[TIMELINE LLM] LLM returned empty list, using fallback: "
                    f"phase={phase}, subphase={subphase}, events_count={len(group_events)}"
                )
                # fallback으로 넘어감 (아래 패턴 기반 코드 실행)
                raise ValueError("LLM returned empty list")

            logger.info(
                f"[TIMELINE LLM] LLM returned {len(llm_tasks)} tasks: "
                f"phase={phase}, subphase={subphase}"
            )

            # LLM 결과를 TimelineSection으로 변환 (부분 성공 처리, Phase 6.2)
            successful_sections = []
            failed_tasks = []

            for idx, task in enumerate(llm_tasks):
                event_seqs = task.get("event_seqs", [])
                # event_seqs에 해당하는 이벤트 찾기
                task_events = [e for e in group_events if e.seq in event_seqs]

                if not task_events:
                    failed_tasks.append(
                        {
                            "task_idx": idx,
                            "task_title": task.get("title", "작업 항목"),
                            "event_seqs": event_seqs,
                            "reason": "No matching events found",
                        }
                    )
                    logger.warning(
                        f"[TIMELINE LLM] Task[{idx}] validation failed: "
                        f"title='{task.get('title', '')[:50]}', "
                        f"event_seqs={event_seqs}, "
                        f"reason='No matching events found'"
                    )
                    continue

                try:
                    section = TimelineSection(
                        section_id=_generate_section_id(
                            phase, subphase, len(successful_sections) + 1
                        ),
                        title=task.get("title", "작업 항목"),
                        summary=task.get("summary", ""),
                        phase=phase,
                        subphase=subphase,
                        events=event_seqs,
                        has_issues=_check_has_issues(task_events, issue_cards),
                        issue_refs=_extract_issue_refs(task_events, issue_cards),
                        detailed_results=_extract_detailed_results(task_events),
                    )
                    successful_sections.append(section)
                    logger.info(
                        f"[TIMELINE LLM] Task[{idx}] converted to section: "
                        f"section_id={section.section_id}, "
                        f"title='{section.title[:50]}', "
                        f"events_count={len(event_seqs)}"
                    )
                except Exception as section_error:
                    failed_tasks.append(
                        {
                            "task_idx": idx,
                            "task_title": task.get("title", "작업 항목"),
                            "event_seqs": event_seqs,
                            "reason": f"Section creation failed: {str(section_error)[:100]}",
                        }
                    )
                    logger.warning(
                        f"[TIMELINE LLM] Task[{idx}] section creation failed: "
                        f"title='{task.get('title', '')[:50]}', "
                        f"error={str(section_error)[:100]}"
                    )

            # 부분 성공 처리: 성공한 섹션은 사용, 실패한 부분만 Fallback (Phase 6.2)
            if successful_sections:
                logger.info(
                    f"[TIMELINE LLM] LLM extraction partially successful: "
                    f"successful_sections={len(successful_sections)}, "
                    f"failed_tasks={len(failed_tasks)}, "
                    f"total_tasks={len(llm_tasks)}"
                )

                # 실패한 task의 이벤트를 fallback으로 처리
                if failed_tasks:
                    failed_event_seqs = set()
                    for failed_task in failed_tasks:
                        failed_event_seqs.update(failed_task.get("event_seqs", []))

                    # 성공한 섹션에 포함된 이벤트 제외
                    successful_event_seqs = set()
                    for section in successful_sections:
                        successful_event_seqs.update(section.events)

                    remaining_event_seqs = failed_event_seqs - successful_event_seqs

                    if remaining_event_seqs:
                        logger.info(
                            f"[TIMELINE LLM] Processing {len(remaining_event_seqs)} remaining events "
                            f"with fallback: seqs={sorted(remaining_event_seqs)}"
                        )
                        remaining_events = [
                            e for e in group_events if e.seq in remaining_event_seqs
                        ]
                        if remaining_events:
                            # 패턴 기반 fallback으로 남은 이벤트 처리
                            fallback_sections = _extract_main_tasks_from_group(
                                remaining_events,
                                phase,
                                subphase,
                                session_meta,
                                issue_cards,
                                use_llm=False,
                            )
                            successful_sections.extend(fallback_sections)
                            logger.info(
                                f"[TIMELINE LLM] Added {len(fallback_sections)} fallback sections "
                                f"for remaining events"
                            )

                return successful_sections
            else:
                # 모든 task가 실패한 경우에만 전체 fallback
                logger.warning(
                    f"[TIMELINE LLM] All {len(llm_tasks)} tasks failed validation, "
                    f"using full fallback: phase={phase}, subphase={subphase}"
                )
        except Exception as e:
            logger = logging.getLogger(__name__)
            error_type = type(e).__name__
            logger.error(
                f"[TIMELINE LLM] LLM-based task extraction failed with exception: "
                f"{error_type}: {str(e)[:200]}, "
                f"falling back to pattern-based: phase={phase}, subphase={subphase}"
            )
            import traceback

            logger.debug(f"[TIMELINE LLM] Exception traceback: {traceback.format_exc()}")

    # 패턴 기반 작업 항목 추출 (기본 또는 fallback)

    # 1. PLAN 타입 이벤트가 있으면 작업 항목으로 추출
    plan_events = [e for e in group_events if e.type == EventType.PLAN]
    if plan_events:
        section = TimelineSection(
            section_id=_generate_section_id(phase, subphase, 1),
            title=_generate_section_title(plan_events),
            summary=_generate_section_summary(plan_events),
            phase=phase,
            subphase=subphase,
            events=[e.seq for e in plan_events],
            has_issues=_check_has_issues(plan_events, issue_cards),
            issue_refs=_extract_issue_refs(plan_events, issue_cards),
            detailed_results=_extract_detailed_results(plan_events),
        )
        sections.append(section)

    # 2. CODE_GENERATION 타입 이벤트 그룹
    code_gen_events = [e for e in group_events if e.type == EventType.CODE_GENERATION]
    if code_gen_events:
        section = TimelineSection(
            section_id=_generate_section_id(phase, subphase, len(sections) + 1),
            title=_generate_section_title(code_gen_events),
            summary=_generate_section_summary(code_gen_events),
            phase=phase,
            subphase=subphase,
            events=[e.seq for e in code_gen_events],
            has_issues=_check_has_issues(code_gen_events, issue_cards),
            issue_refs=_extract_issue_refs(code_gen_events, issue_cards),
            detailed_results=_extract_detailed_results(code_gen_events),
        )
        sections.append(section)

    # 3. 나머지 이벤트들 (DEBUG 제외, DEBUG는 Issue Card로 처리)
    other_events = [
        e
        for e in group_events
        if e.type not in [EventType.PLAN, EventType.CODE_GENERATION, EventType.DEBUG]
    ]
    if other_events:
        section = TimelineSection(
            section_id=_generate_section_id(phase, subphase, len(sections) + 1),
            title=_generate_section_title(other_events),
            summary=_generate_section_summary(other_events),
            phase=phase,
            subphase=subphase,
            events=[e.seq for e in other_events],
            has_issues=_check_has_issues(other_events, issue_cards),
            issue_refs=_extract_issue_refs(other_events, issue_cards),
            detailed_results=_extract_detailed_results(other_events),
        )
        sections.append(section)

    # 섹션이 없으면 기본 섹션 생성
    if not sections:
        section = TimelineSection(
            section_id=_generate_section_id(phase, subphase, 1),
            title="기타 작업",
            summary=_generate_section_summary(group_events),
            phase=phase,
            subphase=subphase,
            events=[e.seq for e in group_events],
            has_issues=_check_has_issues(group_events, issue_cards),
            issue_refs=_extract_issue_refs(group_events, issue_cards),
            detailed_results=_extract_detailed_results(group_events),
        )
        sections.append(section)

    return sections


def _generate_section_id(phase: Optional[int], subphase: Optional[int], index: int) -> str:
    """섹션 ID 생성 (예: "6.7-main-task-1")"""
    phase_str = str(phase) if phase is not None else "?"
    subphase_str = str(subphase) if subphase is not None else "?"
    return f"{phase_str}.{subphase_str}-main-task-{index}"


def _generate_section_title(events: List[Event]) -> str:
    """섹션 제목 생성 (패턴 기반, LLM으로 개선 가능)"""
    if not events:
        return "기타 작업"

    # 첫 번째 이벤트의 summary를 사용 (간단한 방법)
    # TODO: LLM으로 더 정교한 제목 생성
    first_summary = events[0].summary[:100]  # 처음 100자만
    return first_summary.replace("\n", " ").strip()


def _generate_section_summary(events: List[Event]) -> str:
    """섹션 요약 생성 (패턴 기반, LLM으로 개선 가능)"""
    if not events:
        return ""

    # 모든 이벤트의 summary를 결합
    summaries = [e.summary for e in events if e.summary]
    combined = " ".join(summaries)
    # 500자로 제한
    return combined[:500].strip()


def _check_has_issues(events: List[Event], issue_cards: List) -> bool:
    """이벤트 그룹에 이슈가 있는지 확인"""
    if not issue_cards:
        return False

    # TODO: 더 정교한 연결 로직 필요
    # 현재는 간단하게 같은 phase/subphase에 이슈가 있으면 True
    return len(issue_cards) > 0


def _extract_issue_refs(events: List[Event], issue_cards: List) -> List[str]:
    """관련 Issue Card ID 추출"""
    if not issue_cards:
        return []

    refs = []
    # TODO: 더 정교한 연결 로직 구현 필요
    # 현재는 간단하게 모든 issue_id를 반환
    for issue in issue_cards:
        if hasattr(issue, "issue_id"):
            refs.append(issue.issue_id)
        elif isinstance(issue, dict) and "issue_id" in issue:
            refs.append(issue["issue_id"])

    return refs


def _extract_detailed_results(events: List[Event]) -> dict:
    """작업 결과 연결 정보 추출"""
    code_snippets: Set[str] = set()
    files: Set[str] = set()
    artifacts: List[dict] = []

    for event in events:
        # 코드 스니펫 수집
        code_snippets.update(event.snippet_refs)

        # Artifact에서 파일 경로 수집
        for artifact in event.artifacts:
            if isinstance(artifact, dict):
                if "path" in artifact:
                    files.add(artifact["path"])
                artifacts.append(artifact)

    return {
        "code_snippets": list(code_snippets),
        "files": list(files),
        "artifacts": artifacts,
    }
