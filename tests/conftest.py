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
    log_dir = None
    log_file = None
    file_handler = None

    try:
        # 1. 로그 디렉토리 생성
        log_dir = Path(__file__).parent / "logs"
        log_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        log_file = log_dir / f"{test_name}_{timestamp}.log"

        # 디버깅: 시작 메시지
        print(f"\n[DEBUG] Setting up logging for test: {test_name}")
        print(f"[DEBUG] Log directory: {log_dir.absolute()}")
        print(f"[DEBUG] Log file: {log_file.absolute()}")

        # 2. 기존 핸들러 제거
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
            handler.close()  # 핸들러 닫기

        # 3. FileHandler 생성 (버퍼링 비활성화 또는 즉시 flush)
        file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="w")
        file_handler.setLevel(logging.DEBUG)

        # StreamHandler 생성
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        # 포맷터 설정
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # 4. 루트 로거 설정
        logging.root.setLevel(logging.DEBUG)
        logging.root.addHandler(file_handler)
        logging.root.addHandler(stream_handler)

        # 5. backend.core.llm_service 로거 명시적으로 DEBUG 레벨로 설정
        llm_logger = logging.getLogger("backend.core.llm_service")
        llm_logger.setLevel(logging.DEBUG)
        llm_logger.propagate = True  # 루트 로거로 전파

        # 6. Fixture 로거로 테스트 시작 로그
        logger = logging.getLogger(__name__)
        logger.info(f"Test started: {test_name}")
        logger.info(f"Log file: {log_file.absolute()}")

        # 즉시 flush하여 파일에 쓰기 확인
        file_handler.flush()

        # 7. 파일 생성 확인
        if log_file.exists():
            print(f"[DEBUG] Log file created: {log_file.absolute()}")
            print(f"[DEBUG] Log file size: {log_file.stat().st_size} bytes")
        else:
            print(f"[ERROR] Log file was not created: {log_file.absolute()}")

        # 8. 핸들러 확인
        root_handlers = logging.root.handlers
        print(f"[DEBUG] Root logger handlers: {len(root_handlers)}")
        for i, handler in enumerate(root_handlers):
            print(f"[DEBUG] Handler {i}: {type(handler).__name__}")

        yield

        # 9. 테스트 종료 후 처리
        logger.info(f"Test completed: {test_name}")

        # 10. FileHandler 명시적으로 flush 및 닫기
        if file_handler:
            file_handler.flush()
            # 파일 핸들러는 루트 로거에서 제거하지 않고 닫기만 함
            # (다른 핸들러가 사용 중일 수 있음)

        # 11. 최종 파일 확인
        if log_file and log_file.exists():
            file_size = log_file.stat().st_size
            print(f"\n[LOG] Test log saved to: {log_file.absolute()}")
            print(f"[LOG] Log file size: {file_size} bytes")

            if file_size == 0:
                print(f"[WARNING] Log file is empty!")
            else:
                # 파일 내용 일부 확인 (처음 500자)
                try:
                    with open(log_file, "r", encoding="utf-8") as f:
                        content_preview = f.read(500)
                        print(f"[LOG] Log file preview (first 500 chars):")
                        print(content_preview)
                except Exception as e:
                    print(f"[ERROR] Failed to read log file: {e}")
        else:
            print(
                f"\n[ERROR] Log file was not created: {log_file.absolute() if log_file else 'Unknown'}"
            )

    except Exception as e:
        # 예외 발생 시 상세 정보 출력
        print(f"\n[ERROR] Failed to setup logging: {e}")
        import traceback

        traceback.print_exc()

        # 가능한 경우 로그 파일 경로 출력
        if log_file:
            print(f"[ERROR] Intended log file: {log_file.absolute()}")

        # 예외를 다시 발생시켜 테스트 실패로 표시
        raise

    finally:
        # 12. 정리 작업 (필요한 경우)
        # FileHandler는 루트 로거에 남겨두고, 다음 테스트에서 제거됨
        pass

