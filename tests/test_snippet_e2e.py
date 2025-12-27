"""
스니펫 E2E 테스트 (Phase 5)

실제 입력 데이터로 전체 스니펫 처리 파이프라인을 테스트합니다.

⚠️ 중요: 실제 데이터만 사용 (Mock 사용 절대 금지)
"""

import pytest
import json
from pathlib import Path
from datetime import datetime

from backend.parser import parse_markdown
from backend.builders.event_normalizer import normalize_turns_to_events
from backend.builders.timeline_builder import build_structured_timeline
from backend.builders.issues_builder import build_issue_cards
from backend.builders.snippet_manager import process_snippets
from backend.builders.snippet_storage import generate_snippets_json
from backend.core.models import Snippet, Event, IssueCard

# 실제 입력 데이터 경로
INPUT_FILE = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
RESULTS_DIR = Path(__file__).parent / "results"
REPORT_DIR = Path(__file__).parent / "reports"


def test_snippet_e2e_with_llm(parsed_data, normalized_events, timeline_sections):
    """
    실제 입력 데이터로 전체 스니펫 처리 파이프라인 E2E 테스트

    테스트 단계:
    1. 파싱 (fixture 사용)
    2. 이벤트 정규화 (fixture 사용)
    3. Timeline Section 생성 (fixture 사용)
    4. Issue Cards 생성
    5. 스니펫 처리 (추출, 중복 제거, 링킹)
    6. snippets.json 생성
    7. 검증 (ID 형식, 중복 제거, 링킹 정확성)
    """
    # 1. Fixture에서 데이터 가져오기
    events, session_meta = normalized_events

    # 2. 딕셔너리를 모델로 변환
    from backend.core.models import Turn, IssueCard
    turns = [Turn(**turn_dict) for turn_dict in parsed_data["turns"]]

    # 3. Issue Cards 생성
    issue_cards = build_issue_cards(
        turns=turns,
        events=events,
        session_meta=session_meta,
        use_llm=True,  # LLM 사용 (기본값)
        timeline_sections=timeline_sections,
    )

    # 4. 스니펫 처리 (추출, 중복 제거, 링킹)
    snippets, updated_events, updated_issue_cards = process_snippets(
        turns=turns,
        events=events,
        issue_cards=issue_cards,
        session_meta=session_meta,
    )

    # 5. snippets.json 생성
    snippets_json = generate_snippets_json(
        snippets=snippets,
        session_meta=session_meta,
        output_dir=None,  # 파일 저장 안 함 (검증만)
    )

    # 6. 정합성 검증

    # 6.1 스니펫 ID 형식 검증
    for snippet in snippets:
        assert snippet.snippet_id.startswith("SNP-"), f"Invalid snippet_id format: {snippet.snippet_id}"
        assert len(snippet.snippet_id.split("-")) >= 5, f"Snippet ID should have format: SNP-session-turn-block-lang, got: {snippet.snippet_id}"

        # ID 형식: SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang}
        parts = snippet.snippet_id.split("-")
        assert parts[0] == "SNP"
        assert parts[1] == session_meta.session_id
        # turn_index와 block_index는 숫자 형식 확인
        assert parts[2].isdigit() or len(parts[2]) == 3
        assert parts[3].isdigit() or len(parts[3]) == 2
        # lang은 문자열

    # 6.2 중복 제거 검증 (해시 기반)
    hash_set = set()
    for snippet in snippets:
        assert snippet.snippet_hash not in hash_set, f"Duplicate snippet hash found: {snippet.snippet_hash}"
        hash_set.add(snippet.snippet_hash)

    # 6.3 Event 링킹 검증
    for event in updated_events:
        # snippet_refs가 snippet_id 형식인지 확인
        for snippet_ref in event.snippet_refs:
            assert snippet_ref.startswith("SNP-"), f"Invalid snippet_ref in Event: {snippet_ref}"

        # snippet_refs가 실제로 존재하는 snippet_id인지 확인
        snippet_ids = {s.snippet_id for s in snippets}
        for snippet_ref in event.snippet_refs:
            assert snippet_ref in snippet_ids or any(
                snippet_ref in s.aliases for s in snippets
            ), f"Snippet ref {snippet_ref} not found in snippets"

    # 6.4 Issue Card 링킹 검증
    for issue_card in updated_issue_cards:
        # snippet_refs가 snippet_id 형식인지 확인
        for snippet_ref in issue_card.snippet_refs:
            assert snippet_ref.startswith("SNP-"), f"Invalid snippet_ref in IssueCard: {snippet_ref}"

        # snippet_refs가 실제로 존재하는 snippet_id인지 확인
        snippet_ids = {s.snippet_id for s in snippets}
        for snippet_ref in issue_card.snippet_refs:
            assert snippet_ref in snippet_ids or any(
                snippet_ref in s.aliases for s in snippets
            ), f"Snippet ref {snippet_ref} not found in snippets"

    # 6.5 snippets.json 구조 검증
    assert "session_meta" in snippets_json
    assert "snippets" in snippets_json
    assert isinstance(snippets_json["snippets"], list)
    assert len(snippets_json["snippets"]) == len(snippets)

    # 각 snippet의 필수 필드 검증
    for snippet_dict in snippets_json["snippets"]:
        assert "snippet_id" in snippet_dict
        assert "lang" in snippet_dict
        assert "code" in snippet_dict
        assert "source" in snippet_dict
        assert "links" in snippet_dict
        assert "snippet_hash" in snippet_dict
        assert "aliases" in snippet_dict

    # 7. 타당성 검증

    # 7.1 스니펫 개수 검증 (코드 블록이 있는 Turn이 있으면 스니펫도 있어야 함)
    code_block_count = sum(len(turn.code_blocks) for turn in turns)
    if code_block_count > 0:
        assert len(snippets) > 0, "Code blocks exist but no snippets generated"

    # 7.2 링킹 정확성 검증
    # Event의 turn_ref와 일치하는 스니펫이 링크되어야 함
    event_with_snippets = [e for e in updated_events if e.snippet_refs]
    if event_with_snippets:
        for event in event_with_snippets:
            # 해당 event의 turn_ref에 해당하는 스니펫이 있는지 확인
            matching_snippets = [
                s for s in snippets if s.source["turn_index"] == event.turn_ref
            ]
            if matching_snippets:
                # 일부라도 링크되어 있어야 함
                linked = any(
                    s.snippet_id in event.snippet_refs for s in matching_snippets
                )
                assert linked, f"Event {event.seq} has turn_ref {event.turn_ref} but no matching snippets linked"

    # 8. 결과 분석 및 자동 보고
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 정량적 데이터 수집
    report = {
        "test_name": "snippet_e2e",
        "timestamp": timestamp,
        "input_file": str(INPUT_FILE),
        "results": {
            "total_turns": len(turns),
            "total_code_blocks": code_block_count,
            "total_snippets": len(snippets),
            "total_events": len(updated_events),
            "total_issue_cards": len(updated_issue_cards),
            "events_with_snippets": len([e for e in updated_events if e.snippet_refs]),
            "issue_cards_with_snippets": len([c for c in updated_issue_cards if c.snippet_refs]),
            "duplicate_snippets_removed": code_block_count - len(snippets),
            "snippet_languages": {
                lang: len([s for s in snippets if s.lang == lang])
                for lang in set(s.lang for s in snippets)
            },
        },
        "validation": {
            "snippet_id_format": "PASS",
            "deduplication": "PASS",
            "event_linking": "PASS",
            "issue_card_linking": "PASS",
            "snippets_json_structure": "PASS",
        },
        "warnings": [],
        "errors": [],
    }

    # 경고 검사
    if len(snippets) == 0 and code_block_count > 0:
        report["warnings"].append("Code blocks exist but no snippets generated")

    # 리포트 출력
    print("\n" + "=" * 50)
    print("Snippet E2E Test Report")
    print("=" * 50)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 50)

    # 리포트 파일 저장
    RESULTS_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)

    report_file = REPORT_DIR / f"snippet_e2e_report_{timestamp}.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # 상세 결과 저장
    results_file = RESULTS_DIR / f"snippet_e2e_{timestamp}.json"
    detailed_results = {
        "session_meta": session_meta.model_dump(),
        "snippets": [s.model_dump() for s in snippets],
        "events": [e.model_dump() for e in updated_events],
        "issue_cards": [c.model_dump() for c in updated_issue_cards],
        "snippets_json": snippets_json,
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "snippet_e2e",
        },
    }
    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"\n[RESULTS] Detailed results saved to: {results_file}")
    print(f"[REPORT] Report saved to: {report_file}")

    # 최종 검증 통과
    assert len(report["errors"]) == 0, f"Test failed with errors: {report['errors']}"
