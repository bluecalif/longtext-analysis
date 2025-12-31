@echo off
REM 백엔드와 프론트엔드 서버를 동시에 실행하는 배치 파일
REM 프로젝트 루트에서 실행해야 합니다.

REM 스크립트 디렉토리로 이동 (프로젝트 루트)
cd /d "%~dp0\.."

echo ==========================================
echo 백엔드 및 프론트엔드 서버 시작
echo ==========================================
echo.

REM PowerShell 스크립트 실행
powershell.exe -ExecutionPolicy Bypass -File "%~dp0start-all.ps1"

pause

