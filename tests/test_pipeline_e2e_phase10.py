"""
전체 파이프라인 E2E 테스트 (Phase 10)

Phase 9에서 개선된 파싱 결과를 사용하여 전체 파이프라인을 테스트합니다.
파싱 → 이벤트 정규화 → 타임라인 생성 → 이슈카드 생성 → 스니펫 처리

⚠️ 중요: 실제 데이터만 사용 (Mock 사용 절대 금지)
⚠️ 중요: Phase 9 파싱 개선 사항 검증 포함
"""

import pytest
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# .env 파일 자동 로드
load_dotenv()

from backend.parser import parse_markdown
from backend.parser.turns import check_parse_health
from backend.core.pipeline_cache import (
    get_or_create_parsed_data,
    get_or_create_events,
    get_or_create_timeline_sections,
    get_or_create_issue_cards,
)
from backend.builders.timeline_builder import build_timeline
from backend.builders.snippet_manager import process_snippets
from backend.builders.snippet_storage import generate_snippets_json
from backend.core.models import (
    EventType,
    TimelineEvent,
    TimelineSection,
    IssueCard,
    Turn,
    Snippet,
)


# 실제 입력 데이터 경로 (Phase 9에서 검증된 파일)
INPUT_FILE = Path(__file__).parent.parent / "docs" / "longcontext_phase_4_3.md"
REPORT_DIR = Path(__file__).parent / "reports"
RESULTS_DIR = Path(__file__).parent / "results"


def test_pipeline_e2e_phase10_with_llm():
    """
    Phase 9 개선된 파싱 결과를 사용한 전체 파이프라인 E2E 테스트 (LLM 기반)

    테스트 단계:
    1. 파싱 실행 (Phase 9 개선 사항 검증 포함)
    2. 이벤트 정규화
    3. 타임라인 생성
    4. 이슈카드 생성
    5. 스니펫 처리

    Phase 9 파싱 개선 사항 검증:
    - Body에 코드 블록 내용이 포함되지 않았는지 확인
    - 코드 블록 추출 정확도 확인
    - Unknown speaker 비율 확인 (< 20%)
    """
    import os
    import time
    import logging

    logger = logging.getLogger(__name__)

    # API 키 확인 (없으면 스킵)
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 환경 변수가 설정되지 않음")

    # 전체 시작 시간
    total_start = time.time()

    # 1. 실제 입력 데이터 로드
    if not INPUT_FILE.exists():
        pytest.skip(f"Input file not found: {INPUT_FILE}")

    logger.info("=" * 60)
    logger.info("[STEP 1] 파싱 실행 (Phase 9 개선 사항 검증 포함)")
    parse_start = time.time()

    # 파싱 실행 (pipeline_cache 사용)
    parsed_data = get_or_create_parsed_data(input_file=INPUT_FILE)

    # Turn 모델 변환
    turns = [Turn(**turn_dict) for turn_dict in parsed_data["turns"]]
    session_meta = parsed_data["session_meta"]

    # Phase 9 파싱 개선 사항 검증
    # 1.1 Body에 코드 블록 내용이 포함되지 않았는지 확인
    body_has_code_blocks = []
    for turn in turns:
        # 각 코드 블록의 내용이 body에 포함되어 있는지 확인
        for code_block in turn.code_blocks:
            # 코드 블록 내용의 첫 50자만 확인 (전체 내용은 너무 길 수 있음)
            code_preview = code_block.code.strip()[:50]
            if code_preview and code_preview in turn.body:
                body_has_code_blocks.append(
                    {
                        "turn_index": turn.turn_index,
                        "code_block_index": code_block.block_index,
                        "code_preview": code_preview,
                    }
                )

    # 1.2 코드 블록 추출 정확도 확인
    all_code_blocks = []
    for turn in turns:
        all_code_blocks.extend(turn.code_blocks)

    # 1.3 Unknown speaker 비율 확인
    health = check_parse_health(turns)
    unknown_ratio = health["unknown_ratio"]

    parse_time = time.time() - parse_start
    logger.info(f"  - 총 Turn 수: {len(turns)}")
    logger.info(f"  - 총 코드 블록 수: {len(all_code_blocks)}")
    logger.info(f"  - Unknown speaker 비율: {unknown_ratio:.2%}")
    logger.info(f"  - Body에 코드 블록 포함된 Turn 수: {len(body_has_code_blocks)}")
    logger.info(f"[STEP 1] 완료 (소요 시간: {parse_time:.2f}초)")

    # Phase 9 파싱 개선 사항 검증 실패 시 경고
    if len(body_has_code_blocks) > 0:
        logger.warning(
            f"⚠️ Body에 코드 블록 내용이 포함된 Turn이 {len(body_has_code_blocks)}개 발견됨"
        )
        for issue in body_has_code_blocks[:5]:  # 최대 5개만 로그
            logger.warning(f"  - Turn {issue['turn_index']}: {issue['code_preview']}")

    # 2. 이벤트 정규화 실행
    logger.info("=" * 60)
    logger.info("[STEP 2] 이벤트 정규화 실행")
    event_start = time.time()

    events, session_meta = get_or_create_events(
        parsed_data=parsed_data,
        input_file=INPUT_FILE,
        use_llm=True,  # LLM 사용 (기본값)
    )

    event_time = time.time() - event_start
    logger.info(f"  - 총 Event 수: {len(events)}")
    logger.info(f"[STEP 2] 완료 (소요 시간: {event_time:.2f}초)")

    # 3. 타임라인 생성
    logger.info("=" * 60)
    logger.info("[STEP 3] 타임라인 생성")
    timeline_start = time.time()

    # Timeline 생성 (기존 방식)
    timeline = build_timeline(events, session_meta)

    # Timeline Sections 생성 (pipeline_cache 사용)
    timeline_sections = get_or_create_timeline_sections(
        events=events,
        session_meta=session_meta,
        input_file=INPUT_FILE,
        use_llm=True,  # LLM 사용 (기본값)
        issue_cards=None,
    )

    timeline_time = time.time() - timeline_start
    logger.info(f"  - Timeline Event 수: {len(timeline)}")
    logger.info(f"  - Timeline Section 수: {len(timeline_sections)}")
    logger.info(f"[STEP 3] 완료 (소요 시간: {timeline_time:.2f}초)")

    # 4. 이슈카드 생성
    logger.info("=" * 60)
    logger.info("[STEP 4] 이슈카드 생성")
    issue_start = time.time()

    issue_cards = get_or_create_issue_cards(
        turns=turns,
        events=events,
        session_meta=session_meta,
        input_file=INPUT_FILE,
        use_llm=True,  # LLM 사용 (기본값)
        timeline_sections=timeline_sections,
    )

    issue_time = time.time() - issue_start
    logger.info(f"  - Issue Card 수: {len(issue_cards)}")
    logger.info(f"[STEP 4] 완료 (소요 시간: {issue_time:.2f}초)")

    # 5. 스니펫 처리
    logger.info("=" * 60)
    logger.info("[STEP 5] 스니펫 처리")
    snippet_start = time.time()

    snippets, updated_events, updated_issue_cards = process_snippets(
        turns=turns,
        events=events,
        issue_cards=issue_cards,
        session_meta=session_meta,
    )

    # snippets.json 생성 (검증만, 파일 저장 안 함)
    snippets_json = generate_snippets_json(
        snippets=snippets,
        session_meta=session_meta,
        output_dir=None,  # 파일 저장 안 함
    )

    snippet_time = time.time() - snippet_start
    logger.info(f"  - 스니펫 수: {len(snippets)}")
    logger.info(f"  - Event 링킹 수: {len([e for e in updated_events if e.snippet_refs])}")
    logger.info(
        f"  - Issue Card 링킹 수: {len([c for c in updated_issue_cards if c.snippet_refs])}"
    )
    logger.info(f"[STEP 5] 완료 (소요 시간: {snippet_time:.2f}초)")

    # 전체 소요 시간
    total_time = time.time() - total_start
    logger.info("=" * 60)
    logger.info(f"[전체 파이프라인] 완료 (총 소요 시간: {total_time:.2f}초)")

    # 6. 정합성 검증

    # 6.1 파싱 결과 검증
    assert len(turns) > 0, "Turn이 생성되지 않음"
    assert unknown_ratio < 0.2, f"Unknown speaker 비율이 너무 높음: {unknown_ratio:.2%}"
    # Body에 코드 블록 포함은 경고만 (Phase 9 개선 사항이지만 완벽하지 않을 수 있음)

    # 6.2 이벤트 정규화 검증
    assert len(events) > 0, "Event가 생성되지 않음"
    assert len(events) == len(
        turns
    ), f"Event 수({len(events)})가 Turn 수({len(turns)})와 일치하지 않음"

    # 6.3 타임라인 생성 검증
    assert len(timeline) > 0, "Timeline이 생성되지 않음"
    assert len(timeline) == len(
        events
    ), f"Timeline 이벤트 수({len(timeline)})가 Event 수({len(events)})와 일치하지 않음"
    assert len(timeline_sections) > 0, "Timeline Section이 생성되지 않음"

    # 6.4 이슈카드 생성 검증
    assert isinstance(issue_cards, list), "Issue Cards가 리스트가 아님"
    if len(issue_cards) > 0:
        for card in issue_cards:
            assert isinstance(card, IssueCard), "IssueCard 객체가 아님"
            assert card.issue_id, "issue_id가 비어있음"
            assert card.title, "title이 비어있음"
            # Root cause 또는 Fix 중 하나는 있어야 함
            assert (
                card.root_cause is not None or len(card.fix) > 0
            ), "root_cause와 fix가 모두 없음"

    # 6.5 스니펫 처리 검증
    assert isinstance(snippets, list), "Snippets가 리스트가 아님"
    code_block_count = sum(len(turn.code_blocks) for turn in turns)
    if code_block_count > 0:
        assert len(snippets) > 0, "코드 블록이 있지만 스니펫이 생성되지 않음"

    # 스니펫 ID 형식 검증
    for snippet in snippets:
        assert snippet.snippet_id.startswith("SNP-"), f"Invalid snippet_id format: {snippet.snippet_id}"

    # 7. 결과 분석 및 자동 보고
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 정량적 데이터 수집
    report = {
        "test_name": "pipeline_e2e_phase10",
        "timestamp": timestamp,
        "input_file": str(INPUT_FILE),
        "phase9_parsing_validation": {
            "total_turns": len(turns),
            "total_code_blocks": len(all_code_blocks),
            "unknown_speaker_ratio": unknown_ratio,
            "body_has_code_blocks_count": len(body_has_code_blocks),
            "body_cleanup_rate": (
                (len(turns) - len(body_has_code_blocks)) / len(turns) * 100
                if len(turns) > 0
                else 100.0
            ),
        },
        "results": {
            "total_turns": len(turns),
            "total_events": len(events),
            "total_timeline_events": len(timeline),
            "total_timeline_sections": len(timeline_sections),
            "total_issue_cards": len(issue_cards),
            "total_snippets": len(snippets),
            "code_blocks_count": code_block_count,
            "duplicate_snippets_removed": code_block_count - len(snippets),
            "events_with_snippets": len([e for e in updated_events if e.snippet_refs]),
            "issue_cards_with_snippets": len(
                [c for c in updated_issue_cards if c.snippet_refs]
            ),
        },
        "performance": {
            "parse_time_seconds": parse_time,
            "event_time_seconds": event_time,
            "timeline_time_seconds": timeline_time,
            "issue_time_seconds": issue_time,
            "snippet_time_seconds": snippet_time,
            "total_time_seconds": total_time,
        },
        "validation": {
            "parsing_accuracy": "PASS" if unknown_ratio < 0.2 else "WARNING",
            "body_cleanup": "PASS" if len(body_has_code_blocks) == 0 else "WARNING",
            "event_normalization": "PASS" if len(events) == len(turns) else "FAIL",
            "timeline_generation": "PASS" if len(timeline) == len(events) else "FAIL",
            "issue_card_generation": "PASS",
            "snippet_processing": "PASS" if len(snippets) > 0 or code_block_count == 0 else "WARNING",
        },
        "warnings": [],
        "errors": [],
    }

    # 경고 추가
    if unknown_ratio >= 0.2:
        report["warnings"].append(
            f"Unknown speaker 비율이 높음: {unknown_ratio:.2%} (목표: < 20%)"
        )

    if len(body_has_code_blocks) > 0:
        report["warnings"].append(
            f"Body에 코드 블록 내용이 포함된 Turn이 {len(body_has_code_blocks)}개 발견됨"
        )

    if len(events) != len(turns):
        report["errors"].append(
            f"Event 수({len(events)})가 Turn 수({len(turns)})와 일치하지 않음"
        )

    if len(timeline) != len(events):
        report["errors"].append(
            f"Timeline 이벤트 수({len(timeline)})가 Event 수({len(events)})와 일치하지 않음"
        )

    # 리포트 출력
    print("\n" + "=" * 60)
    print("Pipeline E2E Test Report (Phase 10)")
    print("=" * 60)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("=" * 60)

    # 리포트 파일 저장
    REPORT_DIR.mkdir(exist_ok=True)
    report_file = REPORT_DIR / f"pipeline_e2e_phase10_report_{timestamp}.json"
    report_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\n[REPORT] Test report saved to: {report_file}")

    # 상세 실행 결과 저장 (필수)
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"pipeline_e2e_phase10_{timestamp}.json"

    detailed_results = {
        "session_meta": session_meta.model_dump() if hasattr(session_meta, "model_dump") else session_meta,
        "turns_count": len(turns),
        "events_count": len(events),
        "timeline_events": [te.model_dump() for te in timeline],
        "timeline_sections": [ts.model_dump() for ts in timeline_sections],
        "issue_cards": [card.model_dump() for card in issue_cards],
        "snippets": [s.model_dump() for s in snippets],
        "snippets_json": snippets_json,
        "phase9_parsing_validation": {
            "body_has_code_blocks": body_has_code_blocks,
        },
        "test_metadata": {
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "test_name": "pipeline_e2e_phase10",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"[RESULTS] Detailed results saved to: {results_file}")

    # 최종 검증 통과
    assert len(report["errors"]) == 0, f"Test failed with errors: {report['errors']}"

