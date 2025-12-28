"""
API E2E 테스트 (Phase 7)

모든 API 엔드포인트를 실제 서버 실행으로 테스트합니다.

⚠️ 중요: 실제 서버 실행 필수 (test_server fixture 사용)
⚠️ 중요: httpx.Client 사용 (TestClient 금지)
⚠️ 중요: 실제 데이터 사용 (Mock 사용 절대 금지)
"""

import pytest
import json
from pathlib import Path
from datetime import datetime

# 실제 입력 데이터 경로
INPUT_FILE = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
RESULTS_DIR = Path(__file__).parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)


def test_parse_endpoint_e2e(client):
    """
    POST /api/parse 엔드포인트 E2E 테스트

    검증 항목:
    - 파일 업로드 성공
    - 응답 스키마 검증 (ParseResponse)
    - session_meta, turns, events 필드 존재
    - 이벤트 개수 검증
    """
    # 실제 입력 파일 사용
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("cursor_phase_6_3.md", f, "text/markdown")}
        response = client.post("/api/parse", files=files)

    assert (
        response.status_code == 200
    ), f"Parse API failed: {response.status_code} - {response.text}"

    data = response.json()

    # 응답 스키마 검증
    assert "session_meta" in data
    assert "turns" in data
    assert "events" in data

    # 파싱 결과 정확성
    assert data["session_meta"]["session_id"] is not None
    assert len(data["turns"]) > 0
    assert len(data["events"]) > 0

    # 이벤트 개수는 Turn 개수와 일치해야 함 (1:1 매핑)
    assert len(data["events"]) == len(data["turns"]), "Event count should match Turn count"


def test_timeline_endpoint_e2e(client):
    """
    POST /api/timeline 엔드포인트 E2E 테스트

    검증 항목:
    - Timeline 생성 성공
    - 응답 스키마 검증 (TimelineResponse)
    - sections, events 필드 존재
    """
    # 1. 먼저 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("cursor_phase_6_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert parse_response.status_code == 200
    parse_data = parse_response.json()

    # 2. Timeline 생성
    timeline_request = {
        "session_meta": parse_data["session_meta"],
        "events": parse_data["events"],
        "issue_cards": None,
        "content_hash": parse_data.get("content_hash"),  # pipeline_cache 사용
    }
    timeline_response = client.post("/api/timeline", json=timeline_request)

    assert (
        timeline_response.status_code == 200
    ), f"Timeline API failed: {timeline_response.status_code} - {timeline_response.text}"

    timeline_data = timeline_response.json()

    # Timeline JSON 구조 검증
    assert "session_meta" in timeline_data
    assert "sections" in timeline_data
    assert "events" in timeline_data
    assert len(timeline_data["sections"]) > 0
    assert len(timeline_data["events"]) > 0


def test_issues_endpoint_e2e(client):
    """
    POST /api/issues 엔드포인트 E2E 테스트

    검증 항목:
    - Issue Cards 생성 성공
    - 응답 스키마 검증 (IssuesResponse)
    - issues 필드 존재
    """
    # 1. 먼저 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("cursor_phase_6_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert parse_response.status_code == 200
    parse_data = parse_response.json()

    # 2. Timeline 생성
    timeline_request = {
        "session_meta": parse_data["session_meta"],
        "events": parse_data["events"],
        "issue_cards": None,
        "content_hash": parse_data.get("content_hash"),  # pipeline_cache 사용
    }
    timeline_response = client.post("/api/timeline", json=timeline_request)
    assert timeline_response.status_code == 200
    timeline_data = timeline_response.json()

    # 3. Issue Cards 생성
    issues_request = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "timeline_sections": timeline_data["sections"],
    }
    issues_response = client.post("/api/issues", json=issues_request)

    assert (
        issues_response.status_code == 200
    ), f"Issues API failed: {issues_response.status_code} - {issues_response.text}"

    issues_data = issues_response.json()

    # Issues JSON 구조 검증
    assert "session_meta" in issues_data
    assert "issues" in issues_data
    assert isinstance(issues_data["issues"], list)


def test_snippets_endpoint_e2e(client):
    """
    GET /api/snippets/{snippet_id} 및 POST /api/snippets/process 엔드포인트 E2E 테스트

    검증 항목:
    - 스니펫 처리 성공
    - 스니펫 조회 성공
    - 응답 스키마 검증
    """
    # 1. 먼저 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("cursor_phase_6_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert parse_response.status_code == 200
    parse_data = parse_response.json()

    # 2. Timeline 생성
    timeline_request = {
        "session_meta": parse_data["session_meta"],
        "events": parse_data["events"],
        "issue_cards": None,
        "content_hash": parse_data.get("content_hash"),  # pipeline_cache 사용
    }
    timeline_response = client.post("/api/timeline", json=timeline_request)
    assert timeline_response.status_code == 200
    timeline_data = timeline_response.json()

    # 3. Issue Cards 생성
    issues_request = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "timeline_sections": timeline_data["sections"],
    }
    issues_response = client.post("/api/issues", json=issues_request)
    assert issues_response.status_code == 200
    issues_data = issues_response.json()

    # 4. 스니펫 처리
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

    # Snippets Process JSON 구조 검증
    assert "session_meta" in snippets_process_data
    assert "snippets" in snippets_process_data
    assert "events" in snippets_process_data
    assert "issue_cards" in snippets_process_data
    assert len(snippets_process_data["snippets"]) > 0

    # 5. 스니펫 조회 (첫 번째 스니펫)
    if snippets_process_data["snippets"]:
        first_snippet_id = snippets_process_data["snippets"][0]["snippet_id"]
        snippet_response = client.get(f"/api/snippets/{first_snippet_id}")

        assert (
            snippet_response.status_code == 200
        ), f"Snippet get API failed: {snippet_response.status_code} - {snippet_response.text}"

        snippet_data = snippet_response.json()

        # Snippet JSON 구조 검증
        assert "snippet" in snippet_data
        assert snippet_data["snippet"]["snippet_id"] == first_snippet_id


def test_export_endpoint_e2e(client):
    """
    POST /api/export/timeline, /api/export/issues, /api/export/all 엔드포인트 E2E 테스트

    검증 항목:
    - Timeline Export 성공 (JSON/MD)
    - Issues Export 성공 (JSON/MD)
    - 전체 Export 성공 (ZIP)
    """
    # 1. 먼저 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("cursor_phase_6_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert parse_response.status_code == 200
    parse_data = parse_response.json()

    # 2. Timeline 생성
    timeline_request = {
        "session_meta": parse_data["session_meta"],
        "events": parse_data["events"],
        "issue_cards": None,
        "content_hash": parse_data.get("content_hash"),  # pipeline_cache 사용
    }
    timeline_response = client.post("/api/timeline", json=timeline_request)
    assert timeline_response.status_code == 200
    timeline_data = timeline_response.json()

    # 3. Issue Cards 생성
    issues_request = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "timeline_sections": timeline_data["sections"],
    }
    issues_response = client.post("/api/issues", json=issues_request)
    assert issues_response.status_code == 200
    issues_data = issues_response.json()

    # 4. 스니펫 처리
    snippets_process_request = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "issue_cards": issues_data["issues"],
    }
    snippets_process_response = client.post("/api/snippets/process", json=snippets_process_request)
    assert snippets_process_response.status_code == 200
    snippets_process_data = snippets_process_response.json()

    # 5. Timeline Export (JSON)
    timeline_export_request = {
        "session_meta": timeline_data["session_meta"],
        "sections": timeline_data["sections"],
        "events": timeline_data["events"],
        "format": "json",
    }
    timeline_export_response = client.post("/api/export/timeline", json=timeline_export_request)

    assert (
        timeline_export_response.status_code == 200
    ), f"Timeline export API failed: {timeline_export_response.status_code}"
    assert timeline_export_response.headers.get("content-type") == "application/json"

    # 6. Issues Export (JSON)
    issues_export_request = {
        "session_meta": issues_data["session_meta"],
        "issues": issues_data["issues"],
        "format": "json",
    }
    issues_export_response = client.post("/api/export/issues", json=issues_export_request)

    assert (
        issues_export_response.status_code == 200
    ), f"Issues export API failed: {issues_export_response.status_code}"
    assert issues_export_response.headers.get("content-type") == "application/json"

    # 7. 전체 Export (ZIP)
    export_all_request = {
        "session_meta": timeline_data["session_meta"],
        "sections": timeline_data["sections"],
        "events": timeline_data["events"],
        "issues": issues_data["issues"],
        "snippets": snippets_process_data["snippets"],
        "format": "json",
    }
    export_all_response = client.post("/api/export/all", json=export_all_request)

    assert (
        export_all_response.status_code == 200
    ), f"Export all API failed: {export_all_response.status_code}"
    assert export_all_response.headers.get("content-type") == "application/zip"
    assert len(export_all_response.content) > 0, "ZIP file should not be empty"


def test_full_pipeline_e2e(client):
    """
    전체 파이프라인 E2E 테스트
    파일 업로드 → 파싱 → Timeline 생성 → Issues 생성 → Snippets 처리 → Export

    검증 항목:
    - 전체 파이프라인 성공
    - 각 단계 간 데이터 연결 정확성
    """
    # 전체 시작 시간
    import time

    total_start = time.time()

    # 1. 파일 업로드 및 파싱
    with open(INPUT_FILE, "rb") as f:
        files = {"file": ("cursor_phase_6_3.md", f, "text/markdown")}
        parse_response = client.post("/api/parse", files=files)

    assert parse_response.status_code == 200
    parse_data = parse_response.json()

    # 2. Timeline 생성
    timeline_request = {
        "session_meta": parse_data["session_meta"],
        "events": parse_data["events"],
        "issue_cards": None,
        "content_hash": parse_data.get("content_hash"),  # pipeline_cache 사용
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
        "content_hash": parse_data.get("content_hash"),  # pipeline_cache 사용
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

    # 상세 결과 저장 (다른 E2E 테스트들과 동일한 형식)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = RESULTS_DIR / f"api_e2e_full_pipeline_{timestamp}.json"

    detailed_results = {
        "session_meta": parse_data["session_meta"],
        "turns": parse_data["turns"],
        "events": parse_data["events"],
        "timeline_sections": timeline_data["sections"],
        "timeline_events": timeline_data["events"],  # 하위 호환성
        "issue_cards": issues_data["issues"],
        "snippets": snippets_process_data["snippets"],
        "test_metadata": {
            "test_name": "test_full_pipeline_e2e",
            "timestamp": timestamp,
            "input_file": str(INPUT_FILE),
            "total_time_seconds": total_time,
            "results_summary": {
                "parse": {
                    "turns_count": len(parse_data["turns"]),
                    "events_count": len(parse_data["events"]),
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
        json.dumps(detailed_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[RESULTS] Detailed results saved to: {results_file}")
