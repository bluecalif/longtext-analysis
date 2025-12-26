"""
conftest_e2e.py의 fixture를 사용하는 로그 파일 생성 테스트

autouse fixture가 정상 작동하는지 확인하기 위한 테스트
"""

import pytest
import logging
from pathlib import Path
from datetime import datetime


def test_logging_with_fixture():
    """
    conftest_e2e.py의 setup_test_logging fixture를 사용하는 테스트

    이 테스트는 autouse=True fixture가 자동으로 적용되어야 함
    """
    # print로 테스트 시작 확인
    print(f"\n[TEST] Starting test with fixture")
    print(f"[TEST] This test should use setup_test_logging fixture automatically")

    # 로그 디렉토리 확인
    log_dir = Path(__file__).parent / "logs"
    print(f"[TEST] Log directory: {log_dir.absolute()}")
    print(f"[TEST] Log directory exists: {log_dir.exists()}")

    # 현재 루트 로거 핸들러 확인
    root_handlers = logging.root.handlers
    print(f"[TEST] Root logger handlers count: {len(root_handlers)}")
    for i, handler in enumerate(root_handlers):
        print(f"[TEST] Handler {i}: {type(handler).__name__}")
        if isinstance(handler, logging.FileHandler):
            print(f"[TEST]   FileHandler baseFilename: {handler.baseFilename}")

    # 테스트 로그 작성
    logger = logging.getLogger(__name__)
    logger.info("Test message with fixture")
    logger.debug("Debug message with fixture")

    # 모든 핸들러 flush
    for handler in root_handlers:
        if hasattr(handler, 'flush'):
            handler.flush()

    # 로그 디렉토리의 파일 목록 확인
    if log_dir.exists():
        log_files = list(log_dir.glob("test_logging_with_fixture_*.log"))
        print(f"[TEST] Found log files: {len(log_files)}")
        for log_file in log_files:
            print(f"[TEST]   - {log_file.name} ({log_file.stat().st_size} bytes)")

    # 최소한 fixture가 실행되었는지 확인 (핸들러가 있어야 함)
    assert len(root_handlers) > 0, "No handlers found - fixture may not have run"

    print(f"[TEST] Test completed")

