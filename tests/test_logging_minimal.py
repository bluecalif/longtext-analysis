"""
최소한의 로그 파일 생성 테스트

로그 파일 fixture가 정상 작동하는지 확인하기 위한 최소 테스트
"""

import pytest
import logging
from pathlib import Path
from datetime import datetime


def test_logging_minimal():
    """
    최소한의 로그 파일 생성 테스트

    - pytest.skip() 없음
    - 복잡한 로직 없음
    - 단순히 로그 파일이 생성되는지만 확인
    """
    # 로그 디렉토리 생성
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)

    # 로그 파일 경로 생성
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"test_logging_minimal_{timestamp}.log"

    # print로 시작 확인
    print(f"\n[TEST] Starting minimal logging test")
    print(f"[TEST] Log file: {log_file.absolute()}")

    # FileHandler 직접 생성
    file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="w")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    # 루트 로거에 추가
    logging.root.addHandler(file_handler)
    logging.root.setLevel(logging.DEBUG)

    # 테스트 로그 작성
    logger = logging.getLogger(__name__)
    logger.info("Test log message from minimal test")

    # 즉시 flush
    file_handler.flush()

    # 파일 생성 확인
    if log_file.exists():
        file_size = log_file.stat().st_size
        print(f"[TEST] Log file created: {log_file.absolute()}")
        print(f"[TEST] Log file size: {file_size} bytes")

        if file_size > 0:
            # 파일 내용 읽기
            with open(log_file, "r", encoding="utf-8") as f:
                content = f.read()
                print(f"[TEST] Log file content:\n{content}")
        else:
            print(f"[TEST] WARNING: Log file is empty!")
    else:
        print(f"[TEST] ERROR: Log file was not created!")

    # 핸들러 정리
    file_handler.close()
    logging.root.removeHandler(file_handler)

    # 최종 확인
    assert log_file.exists(), "Log file was not created"
    assert log_file.stat().st_size > 0, "Log file is empty"

    print(f"[TEST] Test completed successfully")

