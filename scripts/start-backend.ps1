# 백엔드 서버 실행 스크립트
# 프로젝트 루트에서 실행해야 합니다.

# 프로젝트 루트로 이동
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
Set-Location $projectRoot

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "백엔드 서버 시작" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "프로젝트 루트: $projectRoot" -ForegroundColor Gray

# 환경 변수 파일 확인
$envFile = Join-Path $projectRoot ".env"
if (-not (Test-Path $envFile)) {
    Write-Host "[경고] .env 파일을 찾을 수 없습니다." -ForegroundColor Yellow
    Write-Host "[경고] OPENAI_API_KEY 환경 변수가 설정되어 있는지 확인하세요." -ForegroundColor Yellow
}

# Poetry 설치 확인
try {
    $poetryVersion = poetry --version 2>&1
    Write-Host "Poetry 버전: $poetryVersion" -ForegroundColor Green
} catch {
    Write-Host "[오류] Poetry가 설치되어 있지 않습니다." -ForegroundColor Red
    Write-Host "[오류] Poetry를 설치한 후 다시 시도하세요: pip install poetry" -ForegroundColor Red
    exit 1
}

# 포트 8000 사용 중인 프로세스 확인 및 종료
$port = 8000
$processes = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
if ($processes) {
    Write-Host "[경고] 포트 $port가 사용 중입니다. 기존 프로세스를 종료합니다..." -ForegroundColor Yellow
    foreach ($proc in $processes) {
        $procId = $proc.OwningProcess
        try {
            Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
            Write-Host "[정보] 프로세스 $procId 종료됨" -ForegroundColor Gray
        } catch {
            Write-Host "[경고] 프로세스 $procId 종료 실패 (이미 종료되었을 수 있음)" -ForegroundColor Yellow
        }
    }
    Start-Sleep -Seconds 1
}

# 백엔드 서버 실행
Write-Host ""
Write-Host "백엔드 서버를 시작합니다..." -ForegroundColor Cyan
Write-Host "서버 URL: http://localhost:8000" -ForegroundColor Green
Write-Host "API 문서: http://localhost:8000/docs" -ForegroundColor Green
Write-Host ""
Write-Host "서버를 종료하려면 Ctrl+C를 누르세요." -ForegroundColor Yellow
Write-Host ""

# Poetry로 uvicorn 실행
poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

