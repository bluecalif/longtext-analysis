"""
Fixture 없이 로그 파일 생성 테스트

conftest_e2e.py의 fixture가 문제인지 확인하기 위한 테스트
"""

import logging
from pathlib import Path
from datetime import datetime


def test_logging_without_fixture():
    """
    Fixture 없이 직접 로그 파일 생성 테스트
    """
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"test_without_fixture_{timestamp}.log"

    print(f"\n[TEST] Log file path: {log_file.absolute()}")

    # 간단한 로깅 설정
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ],
        force=True
    )

    logger = logging.getLogger(__name__)
    logger.info("Test message without fixture")

    # 파일 확인
    if log_file.exists():
        print(f"[TEST] SUCCESS: Log file created")
        print(f"[TEST] Size: {log_file.stat().st_size} bytes")

        # 파일 내용 읽기
        with open(log_file, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"[TEST] Log file content:\n{content}")
    else:
        print(f"[TEST] FAILED: Log file not created")

    assert log_file.exists(), "Log file was not created"
    assert log_file.stat().st_size > 0, "Log file is empty"

