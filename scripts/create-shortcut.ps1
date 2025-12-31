# 윈도우 바로가기 생성 스크립트
# 이 스크립트는 프로젝트 루트에 "Start App.lnk" 바로가기를 생성합니다.

# 프로젝트 루트로 이동
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
Set-Location $projectRoot

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "바로가기 생성" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "프로젝트 루트: $projectRoot" -ForegroundColor Gray
Write-Host ""

# 바로가기 대상 파일 (배치 파일 또는 PowerShell 스크립트)
$targetScript = Join-Path $scriptDir "start-all.bat"
$shortcutPath = Join-Path $projectRoot "Start App.lnk"

# 바로가기 생성
try {
    # WScript.Shell COM 객체 생성
    $shell = New-Object -ComObject WScript.Shell
    
    # 바로가기 생성
    $shortcut = $shell.CreateShortcut($shortcutPath)
    $shortcut.TargetPath = $targetScript
    $shortcut.WorkingDirectory = $projectRoot
    $shortcut.Description = "Longtext Analysis 앱 시작"
    $shortcut.WindowStyle = 1  # Normal window
    
    # 아이콘 설정 (PowerShell 아이콘 사용, 또는 사용자 지정 아이콘 경로 지정 가능)
    # $shortcut.IconLocation = "C:\Windows\System32\shell32.dll,13"  # 실행 아이콘
    
    $shortcut.Save()
    
    Write-Host "[성공] 바로가기가 생성되었습니다:" -ForegroundColor Green
    Write-Host "  $shortcutPath" -ForegroundColor White
    Write-Host ""
    Write-Host "이제 'Start App.lnk' 파일을 더블클릭하여 앱을 시작할 수 있습니다." -ForegroundColor Cyan
} catch {
    Write-Host "[오류] 바로가기 생성 실패: $_" -ForegroundColor Red
    exit 1
}

