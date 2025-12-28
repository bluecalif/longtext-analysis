"""
Markdown 렌더러 모듈

Timeline과 Issue Cards를 사람이 읽기 쉬운 Markdown 형식으로 렌더링합니다.
"""

from typing import List
from backend.core.models import (
    SessionMeta,
    TimelineSection,
    TimelineEvent,
    IssueCard,
)


def render_timeline_md(
    session_meta: SessionMeta,
    sections: List[TimelineSection],
    events: List[TimelineEvent],
) -> str:
    """
    Timeline을 Markdown 형식으로 렌더링합니다.

    Args:
        session_meta: 세션 메타데이터
        sections: Timeline Section 리스트
        events: Timeline Event 리스트

    Returns:
        Markdown 형식의 문자열
    """
    lines = []

    # 헤더
    lines.append("# Timeline")
    lines.append("")
    lines.append(f"**Session ID**: {session_meta.session_id}")
    if session_meta.exported_at:
        lines.append(f"**Exported At**: {session_meta.exported_at}")
    if session_meta.cursor_version:
        lines.append(f"**Cursor Version**: {session_meta.cursor_version}")
    if session_meta.phase is not None:
        lines.append(f"**Phase**: {session_meta.phase}")
    if session_meta.subphase is not None:
        lines.append(f"**Subphase**: {session_meta.subphase}")
    lines.append(f"**Source Document**: {session_meta.source_doc}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Timeline Sections
    if sections:
        lines.append("## 주요 작업 항목")
        lines.append("")

        for section in sections:
            # Section 헤더
            section_title = f"### {section.title}"
            if section.phase is not None or section.subphase is not None:
                phase_info = []
                if section.phase is not None:
                    phase_info.append(f"Phase {section.phase}")
                if section.subphase is not None:
                    phase_info.append(f"Subphase {section.subphase}")
                section_title += f" ({', '.join(phase_info)})"
            lines.append(section_title)
            lines.append("")

            # Section 요약
            if section.summary:
                lines.append(section.summary)
                lines.append("")

            # 관련 이벤트
            if section.events:
                lines.append("**관련 이벤트**:")
                for event_seq in section.events:
                    # 해당 seq의 이벤트 찾기
                    event = next(
                        (e for e in events if e.seq == event_seq), None
                    )
                    if event:
                        lines.append(f"- [{event.type.value}] {event.summary}")
                lines.append("")

            # 이슈 연결 정보
            if section.has_issues and section.issue_refs:
                lines.append("**관련 이슈**:")
                for issue_id in section.issue_refs:
                    lines.append(f"- {issue_id}")
                lines.append("")

            # 작업 결과 연결 정보
            if section.detailed_results:
                if section.detailed_results.get("code_snippets"):
                    lines.append("**코드 스니펫**:")
                    for snippet_id in section.detailed_results["code_snippets"]:
                        lines.append(f"- {snippet_id}")
                    lines.append("")

                if section.detailed_results.get("files"):
                    lines.append("**관련 파일**:")
                    for file_path in section.detailed_results["files"]:
                        lines.append(f"- `{file_path}`")
                    lines.append("")

            lines.append("---")
            lines.append("")

    # 전체 이벤트 목록 (하위 호환성)
    if events:
        lines.append("## 전체 이벤트 목록")
        lines.append("")

        for event in events:
            lines.append(f"### 이벤트 #{event.seq}")
            lines.append("")
            lines.append(f"**타입**: {event.type.value}")
            lines.append(f"**요약**: {event.summary}")
            if event.artifacts:
                lines.append("**Artifacts**:")
                for artifact in event.artifacts:
                    lines.append(f"- {artifact}")
            if event.snippet_refs:
                lines.append("**스니펫 참조**:")
                for snippet_ref in event.snippet_refs:
                    lines.append(f"- {snippet_ref}")
            lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def render_issues_md(
    session_meta: SessionMeta,
    issues: List[IssueCard],
) -> str:
    """
    Issue Cards를 Markdown 형식으로 렌더링합니다.

    Args:
        session_meta: 세션 메타데이터
        issues: Issue Card 리스트

    Returns:
        Markdown 형식의 문자열
    """
    lines = []

    # 헤더
    lines.append("# Issue Cards")
    lines.append("")
    lines.append(f"**Session ID**: {session_meta.session_id}")
    if session_meta.exported_at:
        lines.append(f"**Exported At**: {session_meta.exported_at}")
    if session_meta.cursor_version:
        lines.append(f"**Cursor Version**: {session_meta.cursor_version}")
    if session_meta.phase is not None:
        lines.append(f"**Phase**: {session_meta.phase}")
    if session_meta.subphase is not None:
        lines.append(f"**Subphase**: {session_meta.subphase}")
    lines.append(f"**Source Document**: {session_meta.source_doc}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Issue Cards
    if issues:
        for issue in issues:
            # Issue 헤더
            lines.append(f"## {issue.title}")
            lines.append("")
            lines.append(f"**Issue ID**: {issue.issue_id}")
            if issue.section_id:
                lines.append(f"**Timeline Section**: {issue.section_id}")
                if issue.section_title:
                    lines.append(f"  - {issue.section_title}")
            lines.append("")

            # 증상
            if issue.symptoms:
                lines.append("### 증상 (Symptoms)")
                lines.append("")
                for symptom in issue.symptoms:
                    lines.append(f"- {symptom}")
                lines.append("")

            # 원인
            if issue.root_cause:
                lines.append("### 원인 (Root Cause)")
                lines.append("")
                root_cause_status = issue.root_cause.get("status", "unknown")
                root_cause_text = issue.root_cause.get("text", "")
                lines.append(f"**상태**: {root_cause_status}")
                lines.append("")
                lines.append(root_cause_text)
                lines.append("")

            # 증거
            if issue.evidence:
                lines.append("### 증거 (Evidence)")
                lines.append("")
                for evidence in issue.evidence:
                    evidence_type = evidence.get("type", "unknown")
                    evidence_text = evidence.get("text_or_ref", "")
                    lines.append(f"- **{evidence_type}**: {evidence_text}")
                lines.append("")

            # 조치 방법
            if issue.fix:
                lines.append("### 조치 방법 (Fix)")
                lines.append("")
                for fix_item in issue.fix:
                    fix_summary = fix_item.get("summary", "")
                    fix_snippet_refs = fix_item.get("snippet_refs", [])
                    lines.append(f"- {fix_summary}")
                    if fix_snippet_refs:
                        lines.append(f"  - 스니펫 참조: {', '.join(fix_snippet_refs)}")
                lines.append("")

            # 검증 방법
            if issue.validation:
                lines.append("### 검증 방법 (Validation)")
                lines.append("")
                for validation in issue.validation:
                    lines.append(f"- {validation}")
                lines.append("")

            # 관련 파일
            if issue.related_artifacts:
                lines.append("### 관련 파일 (Related Artifacts)")
                lines.append("")
                for artifact in issue.related_artifacts:
                    artifact_path = artifact.get("path", "")
                    artifact_kind = artifact.get("kind", "")
                    lines.append(f"- `{artifact_path}` ({artifact_kind})")
                lines.append("")

            # 스니펫 참조
            if issue.snippet_refs:
                lines.append("### 스니펫 참조 (Snippet References)")
                lines.append("")
                for snippet_ref in issue.snippet_refs:
                    lines.append(f"- {snippet_ref}")
                lines.append("")

            lines.append("---")
            lines.append("")
    else:
        lines.append("이슈가 없습니다.")
        lines.append("")

    return "\n".join(lines)

