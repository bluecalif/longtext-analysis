# AI 에이전트 운영 가이드

> **환경**: Windows PowerShell 5.1

---

## 🚨 가장 중요: 프로젝트 진행 규칙

### Phase별 진행 원칙

**절대 혼자서 전체 작업을 진행하지 마세요. 반드시 Phase별로 사용자 피드백을 받아서 진행하세요.**

1. **Phase별 진행 필수**
   - 프로젝트 계획 문서에 정의된 Phase 단위로만 작업 진행
   - 한 번에 여러 Phase를 진행하지 않음
   - 각 Phase 완료 후 반드시 사용자에게 보고 및 피드백 요청

2. **작업 전 사용자 확인**
   - Phase 작업을 시작하기 전에 반드시 사용자에게 설명
   - 사용자 승인 후에만 작업 시작
   - 작업 중간에도 중요한 결정사항은 사용자에게 확인

3. **작업 완료 후 피드백 대기**
   - Phase 완료 후 사용자 피드백 대기
   - 다음 Phase 진행은 사용자 명시적 승인 후에만 시작
   - 피드백 없이는 다음 Phase로 진행하지 않음

4. **Phase 완료 시 필수 작업**
   - **TODOs.md 업데이트**: 완료된 작업 항목 체크박스 업데이트 및 진행 상황 추적 섹션 업데이트
   - **Git Commit**: Phase 완료 후 반드시 커밋 실행
     - 커밋 메시지 형식: `feat: Phase X 완료 - [Phase 제목]`
     - 예시: `feat: Phase 1 완료 - 프로젝트 초기 설정 및 환경 구성`
   - **작업 순서**: TODOs.md 업데이트 → Git add → Git commit → 사용자 피드백 요청

5. **예외 상황**
   - 사용자가 명시적으로 "모든 Phase를 진행하라"고 요청한 경우에만 전체 진행
   - 그 외의 경우에는 항상 Phase별로 진행

### Phase 진행 템플릿

#### Phase 시작 전
```
## Phase X 시작 준비

**작업 범위**: [Phase 제목]
- [ ] 작업 목록 1
- [ ] 작업 목록 2
- ...

**예상 시간**: [예상 소요 시간]
**의존성**: [이전 Phase 완료 여부]

진행하시겠습니까?
```

#### Phase 완료 후
```
## Phase X 완료

**완료된 작업**:
- [완료된 항목들]

**확인 사항**:
- [사용자가 확인해야 할 것들]

**다음 단계**:
- Phase X+1 진행 준비

**Phase 완료 후 필수 작업**:
1. TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
2. Git commit 실행 (feat: Phase X 완료 - [Phase 제목])

피드백 주시면 다음 Phase로 진행하겠습니다.
```

---

## ⚠️ 가장 중요: 사용자 설명 필수 원칙

**모든 작업 전에 반드시 설명하고, 실행은 사용자 확인 후 진행**

### 핵심 원칙

1. **설명 우선, 실행 후순위**: 작업 내용 설명 → 사용자 확인 → 실행 → 결과 해석
2. **단계별 명확한 설명**: What(무엇) → Why(왜) → How(어떻게) → Result(예상 결과)
3. **결과 해석 필수**: 정량적 근거 제시, 문제 시 원인 분석 및 해결책

### 금지 사항

❌ **절대 하지 말 것**:
- 설명 없이 바로 실행
- 결과만 보여주고 해석 없음
- 사용자 확인 없이 작업 진행
- 모호한 표현만 사용
- 정량적 근거 없이 결론 제시

✅ **반드시 해야 할 것**:
- 실행 전 상세 설명 (What/Why/How/Result)
- 사용자 확인 요청
- 결과 해석 및 근거 제시
- 구체적인 다음 단계 안내
- 문제 발생 시 원인 분석 및 해결책

---

## 1. PowerShell 명령어 표준

### 1.1 명령어 연결 및 실행 경로

**규칙**:
- 명령어 연결: 세미콜론(`;`) 사용 (Bash `&&` 금지)
- 모든 명령은 프로젝트 루트에서 실행
- 세션 중 `cd` 사용 금지 (경로 중첩 오류 방지)

```powershell
# ✅ 세미콜론 사용
cd /path/to/project; python -m pytest tests/

# ✅ 서버 실행 (프로젝트 루트에서)
poetry run uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
npm --prefix frontend run dev

# ❌ cd 사용 금지
cd subdirectory; poetry run uvicorn...  # ModuleNotFoundError 발생
```

### 1.2 환경 변수 사용법

**규칙**:
- 설정: `$env:변수명 = "값"`
- 확인: `echo $env:변수명` 또는 `Get-ChildItem Env:`
- Python에서 사용: `os.getenv('변수명')` (python-dotenv 사용)

```powershell
# 환경 변수 설정
$env:PYTHONPATH = "C:\Projects\vibe-coding\longtext-analysis"
$env:API_KEY = "your-api-key"
$env:LOG_LEVEL = "DEBUG"

# 환경 변수 확인
echo $env:API_KEY
Get-ChildItem Env: | Select-String "API"

# 환경 변수와 함께 Python 실행
$env:LOG_LEVEL = "DEBUG"; poetry run python script.py
```

### 1.3 환경변수 파일 관리

**.env 파일이 숨김 속성 → AI 도구가 인식 못함**

**파일 확인 표준 (우선순위 순)**:
```powershell
Get-ChildItem -Name "*.env*" -Force  # 1. -Force 옵션 (최우선, 숨김 파일 포함)
Get-Content .env                      # 2. 파일 내용 확인
Test-Path .env                       # 3. 파일 존재 확인
```

**주의**: ❌ `dir *.env*`, `glob_file_search(".env*")` → 숨김 파일 미포함

**파일 위치**:
- `.env`: 백엔드/프로젝트 루트
- `frontend/.env.local`: 프론트엔드 (Next.js)

**Next.js 환경변수 규칙**:
- 클라이언트 사이드: `NEXT_PUBLIC_` 접두사 필수
- 서버 사이드: 접두사 없음

### 1.4 Python 실행 규칙

**모듈 실행**: 항상 `python -m` 형식 사용
```powershell
# ✅ 권장
poetry run python -m module.submodule.script_name

# ❌ 피하기
poetry run python module/submodule/script.py  # ModuleNotFoundError 가능
```

**임시 코드 실행**: 스크립트 파일로 작성 후 실행 (한글/특수문자 인코딩 문제 방지)
```powershell
# ❌ 금지: python -c로 복잡한 코드 직접 실행
poetry run python -c "from pathlib import Path; print(list(Path('data').glob('*.json')))"

# ✅ 규칙: 스크립트 파일 작성 → 실행 → 삭제
# 1. check_files.py 파일 생성
# 2. 실행
poetry run python check_files.py
# 3. 정리 (테스트용 스크립트는 보존)
Remove-Item check_files.py
```

### 1.5 디렉토리 및 파일 작업

```powershell
New-Item -ItemType Directory -Path "backend\api\models" -Force  # 디렉토리 생성
Get-Content file.txt -Encoding UTF8        # 읽기 (UTF-8 명시)
Copy-Item src.txt dst.txt                  # 복사
Remove-Item file.txt                       # 삭제
Test-Path .env                             # 존재 확인
```

### 1.6 인코딩 규칙

**이모지 사용 금지**: PowerShell은 이모지 미지원 → `[OK]`, `[PASS]`, `[FAIL]` 태그 사용

**한글 파일명/문자열 처리**:
```powershell
# ❌ 실패
python -c "from pypdf import PdfReader; reader = PdfReader(r'data\input\1등의 통찰.pdf')"
Select-String -Pattern "CACHE_SAVE|서버 로그|파싱 완료"

# ✅ 해결
# 1. Python 스크립트 파일 사용 (권장)
poetry run python script.py

# 2. 절대 경로 사용
$pdfPath = (Resolve-Path "data\input\1등의 통찰.pdf").Path

# 3. Select-String은 영문 패턴 사용
Select-String -Pattern "CACHE_SAVE|server|parsing"
```

**파일 출력 인코딩**:
```powershell
# ❌ PowerShell 5.1에서 Tee-Object -Encoding 미지원
Tee-Object -FilePath "output.log" -Encoding UTF8

# ✅ Out-File 사용
poetry run pytest ... | Out-File -FilePath "output.log" -Encoding UTF8
```

### 1.7 출력 제한

```powershell
git diff file.py | Select-Object -First 50  # head 대체
git log | Select-Object -Last 20            # tail 대체
git status | Select-String "modified"        # 필터링
```

---

## 2. Poetry 패키지 관리

### 2.1 버전 요구사항

**Poetry 1.8.5 이상 필수** (최신 패키지의 PEP 621 메타데이터 버전 2.4 지원)

```powershell
poetry --version  # 버전 확인
pip install --upgrade poetry>=1.8.5  # 업데이트
```

### 2.2 주요 오류: "Unknown metadata version: 2.4"

**원인**: Poetry 1.8.4 이하는 메타데이터 버전 2.4 미지원  
**해결**: Poetry 1.8.5 이상으로 업데이트

```powershell
pip uninstall poetry -y
pip install poetry>=1.8.5
poetry lock
poetry install
```

### 2.3 프로젝트 초기 설정

```powershell
poetry --version  # 1.8.5 이상 확인
poetry lock       # lock 파일 생성
poetry install    # 패키지 설치
```

---

## 3. Git 버전 관리

### 3.1 ⚠️ 중요: Git 업데이트 필수

**작업 전**:
```powershell
git status --short  # 상태 확인 (멈춤 문제 시 --short 사용)
git pull origin main  # 원격 변경사항 가져오기
```

**작업 후**:
```powershell
git add .
git commit -m "타입: 작업 내용"  # 예: feat, fix, docs, test, refactor, chore
git push origin main
```

### 3.2 Phase 완료 시 Git Commit

**규칙**: Phase 완료 후 반드시 커밋
- 커밋 메시지: `feat: Phase X 완료 - [Phase 제목]`
- 예시: `feat: Phase 1 완료 - 프로젝트 초기 설정 및 환경 구성`

### 3.3 커밋 메시지 규칙

**형식**: `타입: 작업 내용 (선택: 상세 설명)`

**타입**: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`

### 3.4 Git 명령어 (PowerShell 환경)

```powershell
git status --short          # 상태 확인 (간략, 멈춤 문제 대안)
git diff                     # 변경사항 확인
git log --oneline -10        # 커밋 로그
git remote -v                # 원격 저장소 정보
git pull origin main         # 원격 변경사항 가져오기
git push origin main         # 로컬 변경사항 푸시
```

---

## 4. 테스트 환경 설정

### 4.1 E2E 테스트: 실제 서버 실행 필수

**원칙**: 모든 테스트는 E2E 테스트만 사용, 실제 서버 실행하여 프로덕션 플로우와 동일하게 검증

**구현 방법**:
- `conftest_e2e.py`에 `test_server` fixture로 실제 uvicorn 서버 실행
- `httpx.Client`로 실제 HTTP 요청
- `TestClient` 사용 금지 (백그라운드 작업이 제대로 실행되지 않음)
- 실제 데이터만 사용 (Mock 사용 절대 금지)

**⚠️ 중요: DB 직접 조회 금지**:
- 서버는 실제 파일 데이터베이스 사용 (프로덕션 DB)
- 테스트는 메모리 데이터베이스 (`:memory:`) 사용
- **서로 다른 DB이므로 테스트에서 DB 직접 조회 시 데이터를 찾을 수 없음**
- **해결**: API 응답만 검증 (프로덕션 플로우와 동일)

### 4.2 테스트 후 자동 보고 (필수)

**⚠️ 중요: 테스트 실행 후 반드시 자동으로 상세 보고**

**자동 보고 원칙**:
- 테스트 실행 후 사용자 질문 없이도 자동으로 상세 보고
- 로그 기반 분석 우선 (이미 실행된 결과가 있으면 재실행하지 않고 분석)
- 정량적 데이터 제시 및 문제 발견 시 원인 분석 포함

**금지 사항**:
- ❌ 테스트 실행 후 결과만 보여주고 분석 없음
- ❌ 사용자가 물어봐야만 보고
- ❌ 이미 실행된 결과가 있는데 불필요하게 재실행

---

## 5. 터미널 문제 해결

```powershell
# 프로세스 강제 종료
taskkill /F /IM node.exe
taskkill /F /IM python.exe
Stop-Process -Name "node" -Force

# 포트 점유 확인 및 종료
netstat -ano | findstr :3000  # 포트 확인
taskkill /F /PID [PID번호]    # PID로 종료

# 프로세스 모니터링
Get-Process | Where-Object {$_.ProcessName -eq "node"}
Get-Process | Where-Object {$_.ProcessName -eq "python"}
```

---

## 체크리스트

### 작업 시작 전
- [ ] `git status --short` 확인 → `git pull origin main` 실행
- [ ] `Get-ChildItem -Name "*.env*" -Force` 로 환경변수 파일 확인
- [ ] `poetry --version` 확인 (1.8.5 이상)
- [ ] 포트 충돌 확인 (예: `netstat -ano | findstr :8000`)

### 코드 작성 시
- [ ] 이모지 사용 금지 → `[OK]`, `[PASS]`, `[FAIL]` 사용
- [ ] 명령어 연결은 세미콜론(`;`) 사용
- [ ] 환경변수는 `$env:변수명` 형식 사용
- [ ] Python 모듈 실행은 `python -m` 형식 사용

### Phase 완료 시 (필수)
- [ ] TODOs.md 업데이트 (체크박스 및 진행 상황 추적)
- [ ] `git add .` → `git commit -m "feat: Phase X 완료 - [Phase 제목]"` → `git push origin main`
- [ ] 사용자 피드백 요청
