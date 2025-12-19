"""
E2E 테스트 공통 Fixture

모든 E2E 테스트에 공통으로 적용되는 fixture를 정의합니다.
"""

import pytest
import subprocess
import time
import httpx
import logging
from pathlib import Path
from datetime import datetime


# Phase 6+ 전용: 실제 서버 실행 fixture
@pytest.fixture(scope="session")
def test_server():
    """
    실제 uvicorn 서버 실행 fixture (Phase 6+ API 테스트용)

    Phase 2-5에서는 사용하지 않음 (모듈 직접 호출)
    """
    # 서버 시작
    process = subprocess.Popen(
        ["poetry", "run", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"],
        cwd=Path(__file__).parent.parent,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # 서버 준비 대기
    max_retries = 30
    for _ in range(max_retries):
        try:
            response = httpx.get("http://localhost:8000/health", timeout=1.0)
            if response.status_code == 200:
                break
        except:
            time.sleep(0.5)
    else:
        process.terminate()
        raise RuntimeError("Server failed to start")

    yield process

    # 서버 종료
    process.terminate()
    process.wait()


@pytest.fixture
def client(test_server):
    """
    httpx.Client fixture (실제 HTTP 요청, Phase 6+ 전용)

    Phase 2-5에서는 사용하지 않음 (모듈 직접 호출)
    """
    return httpx.Client(base_url="http://localhost:8000", timeout=30.0)


# 모든 E2E 테스트에 자동 적용: 로그 파일 저장 (필수)
@pytest.fixture(autouse=True)
def setup_test_logging(request):
    """
    모든 E2E 테스트에 자동으로 로깅 설정 (필수)

    로그 파일 위치: tests/logs/{test_name}_{timestamp}.log
    """
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_name = request.node.name
    log_file = log_dir / f"{test_name}_{timestamp}.log"

    # 기존 핸들러 제거 (중복 방지)
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
        force=True,
    )

    logger = logging.getLogger(__name__)
    logger.info(f"Test started: {test_name}")
    logger.info(f"Log file: {log_file}")

    yield

    # 테스트 종료 후 로그 파일 경로 출력
    logger.info(f"Test completed: {test_name}")
    print(f"\n[LOG] Test log saved to: {log_file}")

