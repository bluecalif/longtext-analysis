"""
스니펫 관리 모듈 단위 테스트 (Phase 5)

⚠️ 중요: 실제 데이터만 사용 (Mock 사용 절대 금지)
"""

import pytest
from backend.core.models import CodeBlock, Snippet, Event, EventType, SessionMeta, Turn, IssueCard
from backend.builders.snippet_manager import (
    generate_snippet_id,
    normalize_code,
    generate_snippet_hash,
    detect_language,
    code_blocks_to_snippets,
    deduplicate_snippets,
    link_snippets_to_events,
    link_snippets_to_issues,
    process_snippets,
)


def test_generate_snippet_id():
    """스니펫 ID 생성 규칙 검증"""
    # 기본 케이스
    snippet_id = generate_snippet_id("session_123", 12, 0, "sql")
    assert snippet_id == "SNP-session_123-012-00-sql"

    # lang이 비어있는 경우
    snippet_id = generate_snippet_id("session_123", 12, 0, "")
    assert snippet_id == "SNP-session_123-012-00-text"

    # lang이 None인 경우
    snippet_id = generate_snippet_id("session_123", 12, 0, None)
    assert snippet_id == "SNP-session_123-012-00-text"

    # 블록 인덱스가 큰 경우
    snippet_id = generate_snippet_id("session_123", 1, 99, "python")
    assert snippet_id == "SNP-session_123-001-99-python"


def test_normalize_code():
    """코드 정규화 검증"""
    # CRLF → LF 변환
    code = "line1\r\nline2\r\nline3"
    normalized = normalize_code(code)
    assert "\r" not in normalized
    assert normalized == "line1\nline2\nline3"

    # 트레일링 공백 제거
    code = "line1   \nline2\t\t\nline3  "
    normalized = normalize_code(code)
    lines = normalized.split("\n")
    assert lines[0] == "line1"
    assert lines[1] == "line2"
    assert lines[2] == "line3"


def test_generate_snippet_hash():
    """해시 생성 검증 (동일 코드 → 동일 해시)"""
    code1 = "def hello():\n    print('hello')"
    code2 = "def hello():\n    print('hello')"
    code3 = "def hello():\n    print('world')"

    hash1 = generate_snippet_hash(code1)
    hash2 = generate_snippet_hash(code2)
    hash3 = generate_snippet_hash(code3)

    # 동일 코드는 동일 해시
    assert hash1 == hash2

    # 다른 코드는 다른 해시
    assert hash1 != hash3

    # 해시 길이 검증 (SHA-256은 64자리)
    assert len(hash1) == 64


def test_detect_language():
    """언어 판별 검증 (fence_lang 우선 → 휴리스틱)"""
    # fence_lang 우선
    code = "SELECT * FROM users"
    lang = detect_language(code, fence_lang="python")
    assert lang == "python"  # fence_lang이 우선

    # 휴리스틱: SQL
    code = "SELECT * FROM users WHERE id = 1"
    lang = detect_language(code, fence_lang="")
    assert lang == "sql"

    # 휴리스틱: TypeScript
    code = "import { Component } from 'react'\nexport const App = () => {}"
    lang = detect_language(code, fence_lang="")
    assert lang == "typescript"

    # 휴리스틱: Python
    code = "def hello():\n    print('hello')"
    lang = detect_language(code, fence_lang="")
    assert lang == "python"

    # 휴리스틱: Bash
    code = "npm install react"
    lang = detect_language(code, fence_lang="")
    assert lang == "bash"

    # 판별 실패 → text
    code = "some random text without keywords"
    lang = detect_language(code, fence_lang="")
    assert lang == "text"


def test_code_blocks_to_snippets():
    """CodeBlock → Snippet 변환 검증"""
    session_meta = SessionMeta(
        session_id="test_session_123",
        source_doc="test.md",
    )

    code_blocks = [
        CodeBlock(turn_index=0, block_index=0, lang="sql", code="SELECT * FROM users"),
        CodeBlock(turn_index=0, block_index=1, lang="", code="def hello():\n    pass"),
        CodeBlock(turn_index=1, block_index=0, lang="typescript", code="const x = 1"),
    ]

    snippets = code_blocks_to_snippets(code_blocks, "test_session_123", session_meta)

    assert len(snippets) == 3

    # 첫 번째 스니펫 검증
    assert snippets[0].snippet_id == "SNP-test_session_123-000-00-sql"
    assert snippets[0].lang == "sql"
    assert snippets[0].code == "SELECT * FROM users"
    assert snippets[0].source == {"turn_index": 0, "block_index": 0}

    # 두 번째 스니펫 검증 (lang 비어있음 → 휴리스틱으로 python 감지)
    assert snippets[1].snippet_id.startswith("SNP-test_session_123-000-01-")
    assert snippets[1].lang == "python"  # 휴리스틱으로 감지됨

    # 해시 생성 검증
    assert len(snippets[0].snippet_hash) == 64


def test_deduplicate_snippets():
    """중복 제거 검증 (해시 기반, aliases 포함)"""
    # 동일한 코드를 가진 스니펫 2개 생성
    code = "SELECT * FROM users"

    snippet1 = Snippet(
        snippet_id="SNP-session-000-00-sql",
        lang="sql",
        code=code,
        source={"turn_index": 0, "block_index": 0},
        links={},
        snippet_hash=generate_snippet_hash(code),
        aliases=[],
    )

    snippet2 = Snippet(
        snippet_id="SNP-session-001-00-sql",
        lang="sql",
        code=code,
        source={"turn_index": 1, "block_index": 0},
        links={},
        snippet_hash=generate_snippet_hash(code),  # 동일한 해시
        aliases=[],
    )

    # 다른 코드를 가진 스니펫 1개
    code3 = "SELECT * FROM posts"
    snippet3 = Snippet(
        snippet_id="SNP-session-002-00-sql",
        lang="sql",
        code=code3,
        source={"turn_index": 2, "block_index": 0},
        links={},
        snippet_hash=generate_snippet_hash(code3),
        aliases=[],
    )

    snippets = [snippet1, snippet2, snippet3]
    deduplicated = deduplicate_snippets(snippets)

    # 중복 제거 후 2개만 남아야 함
    assert len(deduplicated) == 2

    # 첫 번째 스니펫이 대표로 유지되고, 두 번째의 ID가 aliases에 추가됨
    representative = None
    for s in deduplicated:
        if s.snippet_id == snippet1.snippet_id:
            representative = s
            break

    assert representative is not None
    assert snippet2.snippet_id in representative.aliases


def test_link_snippets_to_events():
    """Event 링킹 검증"""
    # 스니펫 생성
    snippet = Snippet(
        snippet_id="SNP-session-000-00-sql",
        lang="sql",
        code="SELECT * FROM users",
        source={"turn_index": 0, "block_index": 0},
        links={},
        snippet_hash="test_hash",
        aliases=[],
    )

    # Event 생성 (turn_ref=0)
    session_meta = SessionMeta(session_id="session", source_doc="test.md")
    event = Event(
        seq=1,
        session_id="session",
        turn_ref=0,  # snippet과 동일한 turn_index
        type=EventType.CODE_GENERATION,
        summary="Test event",
        snippet_refs=[],  # 빈 리스트
    )

    snippets, events = link_snippets_to_events([snippet], [event])

    # Event의 snippet_refs 업데이트 검증
    assert len(events) == 1
    assert events[0].snippet_refs == ["SNP-session-000-00-sql"]

    # Snippet의 links에 event_seq 추가 검증
    assert len(snippets) == 1
    assert "event_seq" in snippets[0].links
    assert 1 in snippets[0].links["event_seq"]


def test_link_snippets_to_issues():
    """Issue Card 링킹 검증"""
    # 스니펫 생성
    snippet = Snippet(
        snippet_id="SNP-session-000-00-sql",
        lang="sql",
        code="SELECT * FROM users",
        source={"turn_index": 0, "block_index": 0},
        links={},
        snippet_hash="test_hash",
        aliases=[],
    )

    # Event 생성
    session_meta = SessionMeta(session_id="session", source_doc="test.md")
    event = Event(
        seq=1,
        session_id="session",
        turn_ref=0,
        type=EventType.DEBUG,
        summary="Test event",
        snippet_refs=["SNP-session-000-00-sql"],
    )

    # IssueCard 생성
    issue_card = IssueCard(
        issue_id="ISS-001-1234",
        scope={"session_id": "session"},
        title="Test issue",
        related_events=[1],  # event.seq = 1
        snippet_refs=[],
    )

    snippets, issue_cards = link_snippets_to_issues([snippet], [issue_card], [event])

    # IssueCard의 snippet_refs 업데이트 검증
    assert len(issue_cards) == 1
    assert "SNP-session-000-00-sql" in issue_cards[0].snippet_refs

    # Snippet의 links에 issue_id 추가 검증
    assert len(snippets) == 1
    assert snippets[0].links["issue_id"] == "ISS-001-1234"


def test_process_snippets_integration():
    """전체 파이프라인 통합 테스트"""
    # Turn 생성
    code_block = CodeBlock(turn_index=0, block_index=0, lang="sql", code="SELECT * FROM users")
    turn = Turn(
        turn_index=0,
        speaker="Cursor",
        body="테스트",
        code_blocks=[code_block],
        path_candidates=[],
    )

    # SessionMeta 생성
    session_meta = SessionMeta(session_id="test_session", source_doc="test.md")

    # Event 생성
    event = Event(
        seq=1,
        session_id="test_session",
        turn_ref=0,
        type=EventType.CODE_GENERATION,
        summary="Test",
        snippet_refs=[],
    )

    # IssueCard 생성
    issue_card = IssueCard(
        issue_id="ISS-001",
        scope={"session_id": "test_session"},
        title="Test",
        related_events=[1],
        snippet_refs=[],
    )

    # 전체 파이프라인 실행
    snippets, events, issue_cards = process_snippets(
        turns=[turn],
        events=[event],
        issue_cards=[issue_card],
        session_meta=session_meta,
    )

    # 검증
    assert len(snippets) == 1
    assert snippets[0].snippet_id.startswith("SNP-test_session-000-00-")
    assert events[0].snippet_refs == [snippets[0].snippet_id]
    assert issue_cards[0].snippet_refs == [snippets[0].snippet_id]
