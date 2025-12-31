@echo off
REM 윈도우 바로가기 생성 배치 파일
REM PowerShell 스크립트를 실행합니다.

REM 스크립트 디렉토리로 이동 (프로젝트 루트)
cd /d "%~dp0\.."

REM PowerShell 스크립트 실행
powershell.exe -ExecutionPolicy Bypass -File "%~dp0create-shortcut.ps1"

pause

