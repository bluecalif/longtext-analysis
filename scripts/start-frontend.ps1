# 프론트엔드 서버 실행 스크립트
# 프로젝트 루트에서 실행해야 합니다.

# 프로젝트 루트로 이동
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
Set-Location $projectRoot

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "프론트엔드 서버 시작" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "프로젝트 루트: $projectRoot" -ForegroundColor Gray

# Node.js 설치 확인
try {
    $nodeVersion = node --version 2>&1
    Write-Host "Node.js 버전: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "[오류] Node.js가 설치되어 있지 않습니다." -ForegroundColor Red
    Write-Host "[오류] Node.js를 설치한 후 다시 시도하세요: https://nodejs.org/" -ForegroundColor Red
    exit 1
}

# npm 설치 확인
try {
    $npmVersion = npm --version 2>&1
    Write-Host "npm 버전: $npmVersion" -ForegroundColor Green
} catch {
    Write-Host "[오류] npm이 설치되어 있지 않습니다." -ForegroundColor Red
    Write-Host "[오류] Node.js를 설치하면 npm도 함께 설치됩니다." -ForegroundColor Red
    exit 1
}

# frontend 디렉토리 확인
$frontendDir = Join-Path $projectRoot "frontend"
if (-not (Test-Path $frontendDir)) {
    Write-Host "[오류] frontend 디렉토리를 찾을 수 없습니다." -ForegroundColor Red
    exit 1
}

# node_modules 확인
$nodeModules = Join-Path $frontendDir "node_modules"
if (-not (Test-Path $nodeModules)) {
    Write-Host "[경고] node_modules를 찾을 수 없습니다. 의존성을 설치합니다..." -ForegroundColor Yellow
    Set-Location $frontendDir
    npm install
    Set-Location $projectRoot
}

# 포트 3000 사용 중인 프로세스 확인 및 종료
$port = 3000
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

# 프론트엔드 서버 실행
Write-Host ""
Write-Host "프론트엔드 서버를 시작합니다..." -ForegroundColor Cyan
Write-Host "서버 URL: http://localhost:3000" -ForegroundColor Green
Write-Host ""
Write-Host "서버를 종료하려면 Ctrl+C를 누르세요." -ForegroundColor Yellow
Write-Host ""

# npm run dev 실행 (프로젝트 루트에서)
npm --prefix frontend run dev

