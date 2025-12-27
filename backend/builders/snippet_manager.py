"""
스니펫 관리 모듈 (Phase 5)

코드 블록을 Snippet으로 변환하고, 중복 제거 및 링킹을 수행합니다.
"""

import re
import hashlib
from typing import List, Tuple, Dict, Optional
from collections import defaultdict

from backend.core.models import (
    CodeBlock,
    Snippet,
    Event,
    IssueCard,
    Turn,
    SessionMeta,
)


def generate_snippet_id(session_id: str, turn_index: int, block_index: int, lang: str) -> str:
    """
    스니펫 ID 생성

    형식: SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang}

    Args:
        session_id: 세션 ID
        turn_index: Turn 인덱스
        block_index: 블록 인덱스
        lang: 언어 (비어있으면 "text" 사용)

    Returns:
        스니펫 ID 문자열

    예시:
        SNP-cursor_export_2025-12-14_223636_KST-012-00-sql
    """
    # lang이 비어있으면 "text" 사용
    lang_normalized = lang.strip().lower() if lang else "text"
    if not lang_normalized:
        lang_normalized = "text"

    snippet_id = f"SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang_normalized}"
    return snippet_id


def normalize_code(code: str) -> str:
    """
    코드 정규화 (공백 정규화, 줄바꿈 통일)

    Args:
        code: 원본 코드

    Returns:
        정규화된 코드
    """
    # 줄바꿈 통일 (CRLF → LF)
    normalized = code.replace("\r\n", "\n").replace("\r", "\n")

    # 트레일링 공백 제거 (각 줄 끝)
    lines = normalized.split("\n")
    lines = [line.rstrip() for line in lines]

    # 빈 줄 제거 (선택적, 하지만 중복 제거를 위해서는 공백 정규화만 수행)
    # 완전히 빈 줄은 유지하고 공백만 제거

    return "\n".join(lines)


def generate_snippet_hash(code: str) -> str:
    """
    코드 해시 생성 (SHA-256, 정규화된 코드 사용)

    Args:
        code: 코드 내용

    Returns:
        64자리 해시 문자열 (SHA-256)
    """
    normalized_code = normalize_code(code)
    hash_obj = hashlib.sha256(normalized_code.encode("utf-8"))
    return hash_obj.hexdigest()


def detect_language(code: str, fence_lang: str = "") -> str:
    """
    언어 판별 (fence_lang 우선 → 휴리스틱)

    Args:
        code: 코드 내용
        fence_lang: 코드 펜스에서 추출한 언어 (우선 사용)

    Returns:
        언어 문자열 (예: "sql", "python", "typescript", "bash", "text")

    휴리스틱 규칙:
    - SQL: ALTER TABLE|SELECT|UPDATE|INSERT|DELETE|CREATE TABLE
    - TypeScript: import ... from|export|const|interface|type
    - Python: def |import |from fastapi|from typing
    - Bash: npm |yarn |pnpm|#!/bin/bash|#!/bin/sh
    - 실패 시 "text"
    """
    # fence_lang이 있으면 우선 사용
    if fence_lang:
        lang_normalized = fence_lang.strip().lower()
        if lang_normalized:
            return lang_normalized

    # 휴리스틱: 코드 내용으로 판별
    code_lower = code.lower()
    code_start = code.strip()[:200]  # 처음 200자만 확인

    # SQL 패턴
    sql_pattern = re.compile(
        r"\b(ALTER\s+TABLE|SELECT|UPDATE|INSERT\s+INTO|DELETE\s+FROM|CREATE\s+TABLE|DROP\s+TABLE)\b",
        re.IGNORECASE,
    )
    if sql_pattern.search(code_start):
        return "sql"

    # TypeScript 패턴
    ts_pattern = re.compile(
        r"(import\s+.*\s+from|export\s+(const|interface|type|default)|const\s+\w+\s*[:=]|interface\s+\w+|type\s+\w+\s*=)",
        re.IGNORECASE,
    )
    if ts_pattern.search(code_start):
        return "typescript"

    # Python 패턴
    python_pattern = re.compile(
        r"(def\s+\w+|import\s+\w+|from\s+\w+\s+import|from\s+fastapi|from\s+typing)",
        re.IGNORECASE,
    )
    if python_pattern.search(code_start):
        return "python"

    # Bash 패턴
    bash_pattern = re.compile(
        r"(npm\s+|yarn\s+|pnpm\s+|#!/bin/bash|#!/bin/sh|#!/usr/bin/env\s+bash)",
        re.IGNORECASE,
    )
    if bash_pattern.search(code_start):
        return "bash"

    # 판별 실패 시 "text"
    return "text"


def code_blocks_to_snippets(
    code_blocks: List[CodeBlock], session_id: str, session_meta: SessionMeta
) -> List[Snippet]:
    """
    CodeBlock 리스트를 Snippet 리스트로 변환

    Args:
        code_blocks: CodeBlock 리스트
        session_id: 세션 ID
        session_meta: 세션 메타데이터 (언어 판별에 사용 가능)

    Returns:
        Snippet 리스트
    """
    snippets = []

    for code_block in code_blocks:
        # 언어 판별 (fence_lang 우선 → 휴리스틱)
        lang = detect_language(code_block.code, fence_lang=code_block.lang)

        # 스니펫 ID 생성
        snippet_id = generate_snippet_id(
            session_id=session_id,
            turn_index=code_block.turn_index,
            block_index=code_block.block_index,
            lang=lang,
        )

        # 해시 생성
        snippet_hash = generate_snippet_hash(code_block.code)

        # Snippet 생성
        snippet = Snippet(
            snippet_id=snippet_id,
            lang=lang,
            code=code_block.code,
            source={
                "turn_index": code_block.turn_index,
                "block_index": code_block.block_index,
            },
            links={},
            snippet_hash=snippet_hash,
            aliases=[],
        )

        snippets.append(snippet)

    return snippets


def deduplicate_snippets(snippets: List[Snippet]) -> List[Snippet]:
    """
    중복 스니펫 제거 (해시 기반)

    동일한 해시를 가진 스니펫은 하나만 유지하고,
    제거된 스니펫의 ID는 aliases에 추가합니다.

    Args:
        snippets: Snippet 리스트

    Returns:
        중복 제거된 Snippet 리스트
    """
    if not snippets:
        return []

    # 해시별로 그룹화
    hash_groups: Dict[str, List[Snippet]] = defaultdict(list)
    for snippet in snippets:
        hash_groups[snippet.snippet_hash].append(snippet)

    deduplicated = []

    for snippet_hash, group in hash_groups.items():
        if len(group) == 1:
            # 중복 없음
            deduplicated.append(group[0])
        else:
            # 중복 있음: 첫 번째를 대표로 사용
            representative = group[0]

            # 나머지의 ID를 aliases에 추가
            aliases = [s.snippet_id for s in group[1:]]
            representative.aliases = aliases

            # 나머지의 links 정보를 병합 (선택적)
            # 대표 snippet의 links에 모든 정보 병합
            for other in group[1:]:
                # links 병합 (issue_id, event_seq, paths)
                if other.links:
                    if not representative.links:
                        representative.links = {}
                    # issue_id 병합
                    if "issue_id" in other.links and "issue_id" not in representative.links:
                        representative.links["issue_id"] = other.links["issue_id"]
                    # event_seq 병합 (리스트로)
                    if "event_seq" in other.links:
                        if "event_seq" not in representative.links:
                            representative.links["event_seq"] = []
                        if isinstance(representative.links["event_seq"], list):
                            representative.links["event_seq"].append(other.links["event_seq"])
                    # paths 병합
                    if "paths" in other.links:
                        if "paths" not in representative.links:
                            representative.links["paths"] = []
                        if isinstance(representative.links["paths"], list):
                            representative.links["paths"].extend(other.links["paths"])

            deduplicated.append(representative)

    return deduplicated


def link_snippets_to_events(
    snippets: List[Snippet], events: List[Event]
) -> Tuple[List[Snippet], List[Event]]:
    """
    스니펫과 이벤트 간 링킹

    Event의 turn_ref와 Snippet의 source.turn_index를 매칭하여 연결합니다.

    Args:
        snippets: Snippet 리스트
        events: Event 리스트

    Returns:
        (업데이트된 Snippet 리스트, 업데이트된 Event 리스트) 튜플
    """
    # 스니펫 인덱스 생성 (turn_index, block_index) → snippet_id 매핑
    snippet_map: Dict[Tuple[int, int], Snippet] = {}
    for snippet in snippets:
        turn_idx = snippet.source["turn_index"]
        block_idx = snippet.source["block_index"]
        snippet_map[(turn_idx, block_idx)] = snippet

    # Event별로 snippet_refs 업데이트
    updated_events = []
    for event in events:
        event_snippet_refs = []

        # turn_ref와 일치하는 스니펫 찾기
        turn_idx = event.turn_ref
        for block_idx in range(100):  # 최대 100개 블록 가정 (충분)
            key = (turn_idx, block_idx)
            if key in snippet_map:
                snippet = snippet_map[key]
                event_snippet_refs.append(snippet.snippet_id)

                # Snippet의 links에 event_seq 추가
                if "event_seq" not in snippet.links:
                    snippet.links["event_seq"] = []
                if not isinstance(snippet.links["event_seq"], list):
                    snippet.links["event_seq"] = [snippet.links["event_seq"]]
                if event.seq not in snippet.links["event_seq"]:
                    snippet.links["event_seq"].append(event.seq)

        # Event의 snippet_refs 업데이트
        # Phase 5 이전에는 임시 형식(turn_{turn_index}_block_{block_index})이 있을 수 있으므로
        # 실제 snippet_id로 교체
        event.snippet_refs = event_snippet_refs

        updated_events.append(event)

    return snippets, updated_events


def link_snippets_to_issues(
    snippets: List[Snippet],
    issue_cards: List[IssueCard],
    events: List[Event],
) -> Tuple[List[Snippet], List[IssueCard]]:
    """
    스니펫과 Issue Card 간 링킹

    IssueCard의 related_events를 통해 연결된 이벤트를 찾고,
    해당 이벤트의 snippet_refs를 수집하여 IssueCard.snippet_refs를 업데이트합니다.

    Args:
        snippets: Snippet 리스트
        issue_cards: IssueCard 리스트
        events: Event 리스트 (이벤트 조회용)

    Returns:
        (업데이트된 Snippet 리스트, 업데이트된 IssueCard 리스트) 튜플
    """
    # Event 인덱스 생성 (seq → Event 매핑)
    event_map: Dict[int, Event] = {event.seq: event for event in events}

    # Snippet 인덱스 생성 (snippet_id → Snippet 매핑)
    snippet_map: Dict[str, Snippet] = {s.snippet_id: s for s in snippets}

    updated_issue_cards = []

    for issue_card in issue_cards:
        # related_events를 통해 snippet_refs 수집
        issue_snippet_refs = set()

        for event_seq in issue_card.related_events:
            if event_seq in event_map:
                event = event_map[event_seq]
                issue_snippet_refs.update(event.snippet_refs)

        # IssueCard의 snippet_refs 업데이트 (기존 refs 유지, 새 refs 추가)
        existing_refs = set(issue_card.snippet_refs)
        issue_card.snippet_refs = list(existing_refs | issue_snippet_refs)

        # Snippet의 links에 issue_id 추가
        for snippet_id in issue_card.snippet_refs:
            if snippet_id in snippet_map:
                snippet = snippet_map[snippet_id]
                if "issue_id" not in snippet.links:
                    snippet.links["issue_id"] = issue_card.issue_id

        updated_issue_cards.append(issue_card)

    return snippets, updated_issue_cards


def process_snippets(
    turns: List[Turn],
    events: List[Event],
    issue_cards: List[IssueCard],
    session_meta: SessionMeta,
) -> Tuple[List[Snippet], List[Event], List[IssueCard]]:
    """
    전체 스니펫 처리 파이프라인

    Args:
        turns: Turn 리스트
        events: Event 리스트
        issue_cards: IssueCard 리스트
        session_meta: 세션 메타데이터

    Returns:
        (snippets, updated_events, updated_issue_cards) 튜플
    """
    # 1. 모든 Turn의 code_blocks 수집
    all_code_blocks = []
    for turn in turns:
        all_code_blocks.extend(turn.code_blocks)

    # 2. CodeBlock → Snippet 변환
    snippets = code_blocks_to_snippets(
        code_blocks=all_code_blocks,
        session_id=session_meta.session_id,
        session_meta=session_meta,
    )

    # 3. 중복 제거
    snippets = deduplicate_snippets(snippets)

    # 4. Event 링킹
    snippets, events = link_snippets_to_events(snippets, events)

    # 5. Issue Card 링킹
    snippets, issue_cards = link_snippets_to_issues(snippets, issue_cards, events)

    return snippets, events, issue_cards
