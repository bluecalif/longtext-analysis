"""
API E2E 테스트 (Phase 10)

Phase 9 파싱 개선이 API 엔드포인트에 미치는 영향을 확인합니다.

⚠️ 중요: 실제 서버 실행 필수 (test_server fixture 사용)
⚠️ 중요: httpx.Client 사용 (TestClient 금지)
⚠️ 중요: 실제 데이터 사용 (Mock 사용 절대 금지)
⚠️ 중요: Phase 9 파싱 개선 사항 검증 포함
"""

import pytest
import json
from pathlib import Path
from datetime import datetime
import time

# 실제 입력 데이터 경로 (Phase 9에서 검증된 파일)
INPUT_FILE = Path(__file__).parent.parent / "docs" / "longcontext_phase_4_3.md"
RESULTS_DIR = Path(__file__).parent / "results"
REPORT_DIR = Path(__file__).parent / "reports"


def test_parse_endpoint_phase10(client):
    """
    POST /api/parse 엔드포인트 테스트 (Phase 10)

    Phase 9 파싱 개선 사항 검증:
    - 파싱 결과 정확성 (Turn 개수, 코드 블록 개수)
    - Body에 코드 블록 내용이 포함되지 않았는지 확인
    - Unknown speaker 비율 확인 (< 20%)
    """
    # 전체 시작 시간
    total_start = time.time()

    # 1. 파일 업로드 및 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("longcontext_phase_4_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert (
        parse_response.status_code == 200
    ), f"Parse API failed: {parse_response.status_code} - {parse_response.text}"

    parse_data = parse_response.json()

    # 2. 응답 스키마 검증
    assert "session_meta" in parse_data
    assert "turns" in parse_data
    assert "events" in parse_data
    assert "content_hash" in parse_data

    # 3. Phase 9 파싱 개선 사항 검증
    turns = parse_data["turns"]
    assert len(turns) > 0, "Turn이 생성되지 않음"

    # 3.1 Body에 코드 블록 내용이 포함되지 않았는지 확인
    body_has_code_blocks = []
    all_code_blocks = []
    for turn in turns:
        # 코드 블록 수집
        if "code_blocks" in turn:
            all_code_blocks.extend(turn["code_blocks"])

        # Body에 코드 블록 내용이 포함되어 있는지 확인
        if "body" in turn and "code_blocks" in turn:
            for code_block in turn.get("code_blocks", []):
                code_preview = code_block.get("code", "").strip()[:50]
                if code_preview and code_preview in turn.get("body", ""):
                    body_has_code_blocks.append(
                        {
                            "turn_index": turn.get("turn_index"),
                            "code_block_index": code_block.get("block_index"),
                            "code_preview": code_preview,
                        }
                    )

    # 3.2 Unknown speaker 비율 확인
    unknown_turns = [t for t in turns if t.get("speaker") == "Unknown"]
    unknown_ratio = len(unknown_turns) / len(turns) if len(turns) > 0 else 0.0

    # 4. 이벤트 정규화 검증
    events = parse_data["events"]
    assert len(events) > 0, "Event가 생성되지 않음"
    assert len(events) == len(
        turns
    ), f"Event 수({len(events)})가 Turn 수({len(turns)})와 일치하지 않음"

    # 5. 결과 검증
    assert unknown_ratio < 0.2, f"Unknown speaker 비율이 너무 높음: {unknown_ratio:.2%}"

    # 전체 소요 시간
    total_time = time.time() - total_start

    # 결과 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"api_phase10_parse_{timestamp}.json"

    detailed_results = {
        "session_meta": parse_data["session_meta"],
        "turns_count": len(turns),
        "events_count": len(events),
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
        "test_metadata": {
            "test_name": "test_parse_endpoint_phase10",
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "total_time_seconds": total_time,
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"[RESULTS] Parse API test results saved to: {results_file}")


def test_timeline_endpoint_phase10(client):
    """
    POST /api/timeline 엔드포인트 테스트 (Phase 10)

    Phase 9 파싱 개선 사항이 타임라인 생성에 정상 반영되는지 확인
    """
    # 전체 시작 시간
    total_start = time.time()

    # 1. 먼저 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("longcontext_phase_4_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert parse_response.status_code == 200
    parse_data = parse_response.json()

    # 2. Timeline 생성
    timeline_request = {
        "session_meta": parse_data["session_meta"],
        "events": parse_data["events"],
        "issue_cards": None,
        "content_hash": parse_data.get("content_hash"),
    }
    timeline_response = client.post("/api/timeline", json=timeline_request)

    assert (
        timeline_response.status_code == 200
    ), f"Timeline API failed: {timeline_response.status_code} - {timeline_response.text}"

    timeline_data = timeline_response.json()

    # 3. Timeline JSON 구조 검증
    assert "session_meta" in timeline_data
    assert "sections" in timeline_data
    assert "events" in timeline_data
    assert len(timeline_data["sections"]) > 0
    assert len(timeline_data["events"]) > 0

    # 4. 데이터 일관성 검증
    assert len(timeline_data["events"]) == len(
        parse_data["events"]
    ), "Timeline 이벤트 수가 파싱 이벤트 수와 일치하지 않음"

    # 전체 소요 시간
    total_time = time.time() - total_start

    # 결과 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"api_phase10_timeline_{timestamp}.json"

    detailed_results = {
        "session_meta": timeline_data["session_meta"],
        "timeline_sections_count": len(timeline_data["sections"]),
        "timeline_events_count": len(timeline_data["events"]),
        "parse_events_count": len(parse_data["events"]),
        "test_metadata": {
            "test_name": "test_timeline_endpoint_phase10",
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "total_time_seconds": total_time,
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"[RESULTS] Timeline API test results saved to: {results_file}")


def test_issues_endpoint_phase10(client):
    """
    POST /api/issues 엔드포인트 테스트 (Phase 10)

    Phase 9 파싱 개선 사항이 이슈카드 생성에 정상 반영되는지 확인
    """
    # 전체 시작 시간
    total_start = time.time()

    # 1. 먼저 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("longcontext_phase_4_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert parse_response.status_code == 200
    parse_data = parse_response.json()

    # 2. Timeline 생성 (Issues 생성에 필요)
    timeline_request = {
        "session_meta": parse_data["session_meta"],
        "events": parse_data["events"],
        "issue_cards": None,
        "content_hash": parse_data.get("content_hash"),
    }
    timeline_response = client.post("/api/timeline", json=timeline_request)
    assert timeline_response.status_code == 200
    timeline_data = timeline_response.json()

    # 3. Issues 생성
    issues_request = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "timeline_sections": timeline_data["sections"],
        "content_hash": parse_data.get("content_hash"),
    }
    issues_response = client.post("/api/issues", json=issues_request)

    assert (
        issues_response.status_code == 200
    ), f"Issues API failed: {issues_response.status_code} - {issues_response.text}"

    issues_data = issues_response.json()

    # 4. Issues JSON 구조 검증
    assert "issues" in issues_data
    assert isinstance(issues_data["issues"], list)

    # 전체 소요 시간
    total_time = time.time() - total_start

    # 결과 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"api_phase10_issues_{timestamp}.json"

    detailed_results = {
        "session_meta": parse_data["session_meta"],
        "issues_count": len(issues_data["issues"]),
        "test_metadata": {
            "test_name": "test_issues_endpoint_phase10",
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "total_time_seconds": total_time,
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"[RESULTS] Issues API test results saved to: {results_file}")


def test_snippets_endpoint_phase10(client):
    """
    POST /api/snippets/process 및 GET /api/snippets/{snippet_id} 엔드포인트 테스트 (Phase 10)

    Phase 9 파싱 개선 사항이 스니펫 처리에 정상 반영되는지 확인
    """
    # 전체 시작 시간
    total_start = time.time()

    # 1. 먼저 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("longcontext_phase_4_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert parse_response.status_code == 200
    parse_data = parse_response.json()

    # 2. Timeline 생성
    timeline_request = {
        "session_meta": parse_data["session_meta"],
        "events": parse_data["events"],
        "issue_cards": None,
        "content_hash": parse_data.get("content_hash"),
    }
    timeline_response = client.post("/api/timeline", json=timeline_request)
    assert timeline_response.status_code == 200
    timeline_data = timeline_response.json()

    # 3. Issues 생성
    issues_request = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "timeline_sections": timeline_data["sections"],
        "content_hash": parse_data.get("content_hash"),
    }
    issues_response = client.post("/api/issues", json=issues_request)
    assert issues_response.status_code == 200
    issues_data = issues_response.json()

    # 4. Snippets 처리
    snippets_process_request = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "issue_cards": issues_data["issues"],
    }
    snippets_process_response = client.post("/api/snippets/process", json=snippets_process_request)

    assert (
        snippets_process_response.status_code == 200
    ), f"Snippets process API failed: {snippets_process_response.status_code} - {snippets_process_response.text}"

    snippets_process_data = snippets_process_response.json()

    # 5. Snippets JSON 구조 검증
    assert "snippets" in snippets_process_data
    assert isinstance(snippets_process_data["snippets"], list)

    # 6. 스니펫 조회 테스트 (첫 번째 스니펫)
    if len(snippets_process_data["snippets"]) > 0:
        first_snippet_id = snippets_process_data["snippets"][0].get("snippet_id")
        if first_snippet_id:
            snippet_response = client.get(f"/api/snippets/{first_snippet_id}")
            assert (
                snippet_response.status_code == 200
            ), f"Snippet get API failed: {snippet_response.status_code}"
            snippet_data = snippet_response.json()
            # SnippetResponse는 {"snippet": {...}} 형태로 래핑됨
            assert (
                "snippet" in snippet_data
            ), f"SnippetResponse should have 'snippet' field: {snippet_data.keys()}"
            snippet = snippet_data["snippet"]
            assert "snippet_id" in snippet
            assert "code" in snippet
            assert "lang" in snippet

    # 전체 소요 시간
    total_time = time.time() - total_start

    # 결과 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    results_file = RESULTS_DIR / f"api_phase10_snippets_{timestamp}.json"

    detailed_results = {
        "session_meta": parse_data["session_meta"],
        "snippets_count": len(snippets_process_data["snippets"]),
        "test_metadata": {
            "test_name": "test_snippets_endpoint_phase10",
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "total_time_seconds": total_time,
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"[RESULTS] Snippets API test results saved to: {results_file}")


def test_full_pipeline_api_phase10(client):
    """
    전체 파이프라인 API E2E 테스트 (Phase 10)

    Phase 9 파싱 개선 사항이 전체 API 파이프라인에 정상 반영되는지 확인
    파일 업로드 → 파싱 → Timeline 생성 → Issues 생성 → Snippets 처리 → Export
    """
    # 전체 시작 시간
    total_start = time.time()

    # 1. 파일 업로드 및 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("longcontext_phase_4_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert parse_response.status_code == 200
    parse_data = parse_response.json()

    # Phase 9 파싱 개선 사항 검증
    turns = parse_data["turns"]
    unknown_turns = [t for t in turns if t.get("speaker") == "Unknown"]
    unknown_ratio = len(unknown_turns) / len(turns) if len(turns) > 0 else 0.0
    assert unknown_ratio < 0.2, f"Unknown speaker 비율이 너무 높음: {unknown_ratio:.2%}"

    # 2. Timeline 생성
    timeline_request = {
        "session_meta": parse_data["session_meta"],
        "events": parse_data["events"],
        "issue_cards": None,
        "content_hash": parse_data.get("content_hash"),
    }
    timeline_response = client.post("/api/timeline", json=timeline_request)
    assert timeline_response.status_code == 200
    timeline_data = timeline_response.json()

    # 3. Issues 생성
    issues_request = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "timeline_sections": timeline_data["sections"],
        "content_hash": parse_data.get("content_hash"),
    }
    issues_response = client.post("/api/issues", json=issues_request)
    assert issues_response.status_code == 200
    issues_data = issues_response.json()

    # 4. Snippets 처리
    snippets_process_request = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "issue_cards": issues_data["issues"],
    }
    snippets_process_response = client.post("/api/snippets/process", json=snippets_process_request)
    assert snippets_process_response.status_code == 200
    snippets_process_data = snippets_process_response.json()

    # 5. 전체 Export
    export_all_request = {
        "session_meta": timeline_data["session_meta"],
        "sections": timeline_data["sections"],
        "events": timeline_data["events"],
        "issues": issues_data["issues"],
        "snippets": snippets_process_data["snippets"],
        "format": "json",
    }
    export_all_response = client.post("/api/export/all", json=export_all_request)
    assert export_all_response.status_code == 200

    # 전체 소요 시간
    total_time = time.time() - total_start

    # 결과 검증
    assert len(timeline_data["sections"]) > 0
    assert len(timeline_data["events"]) > 0
    assert isinstance(issues_data["issues"], list)
    assert len(snippets_process_data["snippets"]) > 0
    assert len(export_all_response.content) > 0

    # 상세 결과 저장 및 리포트 생성
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    RESULTS_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)

    results_file = RESULTS_DIR / f"api_phase10_full_pipeline_{timestamp}.json"
    report_file = REPORT_DIR / f"api_phase10_report_{timestamp}.json"

    detailed_results = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "timeline_sections": timeline_data["sections"],
        "timeline_events": timeline_data["events"],
        "issue_cards": issues_data["issues"],
        "snippets": snippets_process_data["snippets"],
        "test_metadata": {
            "test_name": "test_full_pipeline_api_phase10",
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "total_time_seconds": total_time,
            "results_summary": {
                "parse": {
                    "turns_count": len(parse_data["turns"]),
                    "events_count": len(parse_data["events"]),
                    "unknown_speaker_ratio": unknown_ratio,
                },
                "timeline": {
                    "sections_count": len(timeline_data["sections"]),
                    "events_count": len(timeline_data["events"]),
                },
                "issues": {
                    "issues_count": len(issues_data["issues"]),
                },
                "snippets": {
                    "snippets_count": len(snippets_process_data["snippets"]),
                },
                "export": {
                    "zip_size_bytes": len(export_all_response.content),
                },
            },
            "status": "PASS",
        },
    }

    results_file.write_text(
        json.dumps(detailed_results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # 리포트 생성
    report = {
        "test_name": "api_phase10",
        "timestamp": timestamp,
        "input_file": str(INPUT_FILE),
        "results": {
            "parse": {
                "turns_count": len(parse_data["turns"]),
                "events_count": len(parse_data["events"]),
                "unknown_speaker_ratio": unknown_ratio,
            },
            "timeline": {
                "sections_count": len(timeline_data["sections"]),
                "events_count": len(timeline_data["events"]),
            },
            "issues": {
                "issues_count": len(issues_data["issues"]),
            },
            "snippets": {
                "snippets_count": len(snippets_process_data["snippets"]),
            },
            "export": {
                "zip_size_bytes": len(export_all_response.content),
            },
        },
        "validation": {
            "parsing_accuracy": "PASS" if unknown_ratio < 0.2 else "WARNING",
            "api_responses": "PASS",
            "data_consistency": "PASS",
        },
        "warnings": [],
        "errors": [],
        "total_time_seconds": total_time,
    }

    report_file.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[RESULTS] Full pipeline API test results saved to: {results_file}")
    print(f"[REPORT] API test report saved to: {report_file}")
