"""
E2E 테스트 공통 Fixture

모든 E2E 테스트에 공통으로 적용되는 fixture를 정의합니다.
"""

import pytest
import subprocess
import time
import httpx
import logging
import socket
from pathlib import Path
from datetime import datetime

# psutil은 선택적 의존성 (없어도 동작하되 포트 충돌 방지 기능 제한)
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

from backend.core.pipeline_cache import (
    get_or_create_parsed_data,
    get_or_create_events,
    get_or_create_timeline_sections,
)
from backend.core.models import SessionMeta, Event, TimelineSection


# Phase 6+ 전용: 실제 서버 실행 fixture
@pytest.fixture(scope="session")
def test_server():
    """
    실제 uvicorn 서버 실행 fixture (Phase 6+ API 테스트용)

    서버 로그를 파일로 저장합니다 (캐싱 사용 여부 확인 및 디버깅 목적).

    기존 서버가 실행 중인 경우 포트 충돌을 방지하기 위해 자동으로 종료합니다.

    Phase 2-5에서는 사용하지 않음 (모듈 직접 호출)
    """
    # 포트 8000 사용 중인 프로세스 확인 및 종료
    port = 8000
    logger = logging.getLogger(__name__)

    # 포트가 사용 중인지 확인
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    result = sock.connect_ex(('localhost', port))
    sock.close()

    if result == 0:
        # 포트가 사용 중인 경우
        logger.warning(f"Port {port} is already in use. Attempting to kill existing process...")

        if HAS_PSUTIL:
            # psutil을 사용하여 포트를 사용하는 프로세스 찾기 및 종료
            for proc in psutil.process_iter(['pid', 'name', 'connections']):
                try:
                    connections = proc.info.get('connections')
                    if connections:
                        for conn in connections:
                            if conn.status == 'LISTEN' and conn.laddr.port == port:
                                logger.warning(f"Killing process {proc.info['pid']} ({proc.info['name']}) using port {port}")
                                proc.terminate()
                                proc.wait(timeout=5)
                                logger.info(f"Process {proc.info['pid']} terminated successfully")
                                break
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                    continue

            # 잠시 대기 (포트 해제 대기)
            time.sleep(1)
        else:
            # Windows에서 netstat과 taskkill 사용 (psutil 없이도 동작)
            import platform
            if platform.system() == "Windows":
                try:
                    # netstat으로 포트를 사용하는 PID 찾기
                    netstat_result = subprocess.run(
                        ["netstat", "-ano"],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    for line in netstat_result.stdout.splitlines():
                        if f":{port}" in line and "LISTENING" in line:
                            parts = line.split()
                            if len(parts) >= 5:
                                pid = parts[-1]
                                try:
                                    logger.warning(f"Killing process {pid} using port {port}")
                                    subprocess.run(
                                        ["taskkill", "/F", "/PID", pid],
                                        capture_output=True,
                                        timeout=5
                                    )
                                    logger.info(f"Process {pid} terminated successfully")
                                except subprocess.TimeoutExpired:
                                    logger.warning(f"Failed to kill process {pid}: timeout")
                    time.sleep(1)
                except Exception as e:
                    logger.warning(f"Failed to kill process using netstat/taskkill: {e}")
            else:
                # Windows가 아닌 경우 경고만 출력
                logger.warning("psutil not available. Cannot automatically kill existing process on port 8000")
                logger.warning("Please manually stop the process using port 8000 or install psutil")

    # 서버 로그 파일 경로 생성
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    server_log_file = log_dir / f"server_{timestamp}.log"

    # 서버 시작 (stdout/stderr를 파일로 리다이렉트)
    # 파일은 프로세스가 실행되는 동안 열려 있어야 하므로 with 문 밖에서 열기
    log_file = open(server_log_file, "w", encoding="utf-8")
    try:
        process = subprocess.Popen(
            ["poetry", "run", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"],
            cwd=Path(__file__).parent.parent,
            stdout=log_file,
            stderr=subprocess.STDOUT,  # stderr도 stdout으로 합쳐서 같은 파일에 저장
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
            log_file.flush()  # 서버 시작 실패 시에도 로그 저장
            log_file.close()
            raise RuntimeError("Server failed to start")

        yield process

        # 서버 종료
        process.terminate()
        process.wait()
        log_file.flush()  # 서버 종료 시 로그 버퍼 모두 저장
    finally:
        # 서버 로그 파일 닫기
        log_file.close()
        # 서버 로그 파일 경로 출력
        print(f"\n[LOG] Server log saved to: {server_log_file.absolute()}")


@pytest.fixture
def client(test_server):
    """
    httpx.Client fixture (실제 HTTP 요청, Phase 6+ 전용)

    Phase 2-5에서는 사용하지 않음 (모듈 직접 호출)
    """
    return httpx.Client(base_url="http://localhost:8000", timeout=30.0)


# 모든 E2E 테스트에 자동 적용: 로그 파일 저장 (필수)
# ⚠️ 중요: session scope로 변경하여 session scope fixture보다 먼저 실행되도록 함
@pytest.fixture(scope="session", autouse=True)
def setup_test_logging(request):
    """
    모든 E2E 테스트에 자동으로 로깅 설정 (필수, session scope)

    Session scope fixture가 실행되기 전에 로깅을 설정하여
    timeline_sections 등의 fixture에서 발생하는 LLM 호출 로그가 기록되도록 합니다.

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


# Phase 4.7+: 파이프라인 중간 결과 캐싱 Fixture
@pytest.fixture(scope="session")
def input_file():
    """
    입력 파일 경로 fixture (세션 스코프)

    Returns:
        입력 마크다운 파일 경로
    """
    input_file_path = Path(__file__).parent.parent / "docs" / "cursor_phase_6_3.md"
    if not input_file_path.exists():
        pytest.skip(f"Input file not found: {input_file_path}")
    return input_file_path


@pytest.fixture(scope="session")
def parsed_data(input_file):
    """
    파싱 결과 fixture (세션 스코프, 캐시 사용)

    Args:
        input_file: 입력 파일 경로 fixture

    Returns:
        파싱 결과 딕셔너리
    """
    return get_or_create_parsed_data(input_file)


def _detect_use_llm_from_test_name(request) -> bool:
    """
    테스트 함수 이름에서 LLM 사용 여부 감지

    규칙:
    - test_*_with_llm(): LLM 사용 (True)
    - test_*_pattern() 또는 test_*_no_llm(): 패턴 기반 (False)
    - 그 외: 기본값 사용 (True, USE_LLM_BY_DEFAULT)
    """
    from backend.core.constants import USE_LLM_BY_DEFAULT

    test_name = request.node.name

    # 명시적 패턴 기반 테스트
    if "_pattern" in test_name or "_no_llm" in test_name:
        return False

    # 명시적 LLM 테스트
    if "_with_llm" in test_name:
        return True

    # 기본값 (LLM 사용)
    return USE_LLM_BY_DEFAULT


@pytest.fixture(scope="session")
def normalized_events(parsed_data, input_file, request):
    """
    이벤트 정규화 결과 fixture (세션 스코프, 캐시 사용)

    ⚠️ 중요: 기본적으로 LLM을 사용합니다 (USE_LLM_BY_DEFAULT=True).
    테스트 함수 이름에서 자동으로 감지합니다:
    - test_*_with_llm(): LLM 사용
    - test_*_pattern() 또는 test_*_no_llm(): 패턴 기반
    - 그 외: 기본값 (LLM)

    Args:
        parsed_data: 파싱 결과 fixture
        input_file: 입력 파일 경로 fixture
        request: pytest request 객체 (파라미터 접근용)

    Returns:
        (Event 리스트, SessionMeta) 튜플
    """
    use_llm = _detect_use_llm_from_test_name(request)
    return get_or_create_events(parsed_data, input_file, use_llm=use_llm)


@pytest.fixture(scope="session")
def timeline_sections(normalized_events, input_file, request):
    """
    Timeline Section 결과 fixture (세션 스코프, 캐시 사용)

    ⚠️ 중요: 기본적으로 LLM을 사용합니다 (USE_LLM_BY_DEFAULT=True).
    테스트 함수 이름에서 자동으로 감지합니다:
    - test_*_with_llm(): LLM 사용
    - test_*_pattern() 또는 test_*_no_llm(): 패턴 기반
    - 그 외: 기본값 (LLM)

    Args:
        normalized_events: 이벤트 정규화 결과 fixture
        input_file: 입력 파일 경로 fixture
        request: pytest request 객체 (파라미터 접근용)

    Returns:
        TimelineSection 리스트
    """
    events, session_meta = normalized_events
    use_llm = _detect_use_llm_from_test_name(request)

    # Issue Cards는 아직 생성되지 않았으므로 None 전달
    return get_or_create_timeline_sections(
        events=events,
        session_meta=session_meta,
        input_file=input_file,
        use_llm=use_llm,
        issue_cards=None
    )

