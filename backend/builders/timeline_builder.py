"""
Timeline 빌더 모듈

정규화된 이벤트로부터 Timeline을 생성합니다.
"""

from typing import List, Optional
from backend.core.models import Event, TimelineEvent, SessionMeta, EventType


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

