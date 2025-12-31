# 백엔드와 프론트엔드 서버를 동시에 실행하는 스크립트
# 프로젝트 루트에서 실행해야 합니다.

# 프로젝트 루트로 이동
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
Set-Location $projectRoot

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "백엔드 및 프론트엔드 서버 시작" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "프로젝트 루트: $projectRoot" -ForegroundColor Gray
Write-Host ""

# 백엔드 스크립트 경로
$backendScript = Join-Path $scriptDir "start-backend.ps1"
$frontendScript = Join-Path $scriptDir "start-frontend.ps1"

# 백엔드 서버를 새 창에서 실행
Write-Host "백엔드 서버를 새 창에서 시작합니다..." -ForegroundColor Cyan
Start-Process powershell.exe -ArgumentList "-NoExit", "-File", "`"$backendScript`"" -WorkingDirectory $projectRoot

# 잠시 대기 (백엔드 서버 시작 시간 확보)
Start-Sleep -Seconds 3

# 프론트엔드 서버를 새 창에서 실행
Write-Host "프론트엔드 서버를 새 창에서 시작합니다..." -ForegroundColor Cyan
Start-Process powershell.exe -ArgumentList "-NoExit", "-File", "`"$frontendScript`"" -WorkingDirectory $projectRoot

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "서버 시작 완료" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host "백엔드 서버: http://localhost:8000" -ForegroundColor Green
Write-Host "프론트엔드 서버: http://localhost:3000" -ForegroundColor Green
Write-Host "API 문서: http://localhost:8000/docs" -ForegroundColor Green
Write-Host ""
Write-Host "각 서버 창에서 Ctrl+C를 눌러 서버를 종료할 수 있습니다." -ForegroundColor Yellow
Write-Host ""

# 브라우저 자동 실행 여부 확인 (5초 후)
Write-Host "5초 후 브라우저가 자동으로 열립니다..." -ForegroundColor Cyan
Write-Host "취소하려면 Ctrl+C를 누르세요." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# 브라우저 열기
try {
    Start-Process "http://localhost:3000"
    Write-Host "브라우저가 열렸습니다." -ForegroundColor Green
} catch {
    Write-Host "[경고] 브라우저를 자동으로 열 수 없습니다. 수동으로 http://localhost:3000 을 열어주세요." -ForegroundColor Yellow
}

