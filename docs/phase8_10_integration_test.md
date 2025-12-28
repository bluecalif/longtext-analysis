# Phase 8.10 통합 테스트 및 검증 가이드

## 목표
프론트엔드-백엔드 통합 검증 및 API Contract 일치 확인

## 테스트 시나리오

### 1. 서버 실행

```powershell
# 백엔드 서버 (프로젝트 루트에서)
poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000

# 프론트엔드 서버 (프로젝트 루트에서, 새 터미널)
npm --prefix frontend run dev
```

### 2. 전체 플로우 E2E 테스트

#### 2.1 파일 업로드
- 브라우저에서 `http://localhost:3000` 접속
- 파일 드래그&드롭 또는 클릭하여 업로드
- 테스트 파일: `docs/cursor_phase_6_3.md`

#### 2.2 파싱 완료 확인
- Session Meta 정보 표시 확인
- 처리 상태 표시 확인 ("파일 파싱 중...")

#### 2.3 Timeline 생성 및 표시 확인
- Timeline 탭 클릭
- Timeline Section 리스트 표시 확인
- Section 클릭 시 이벤트 펼치기/접기 확인

#### 2.4 Issues 생성 및 표시 확인
- Issues 탭 클릭
- Issue Card 리스트 표시 확인
- 카드 클릭 시 상세 정보 표시 확인

#### 2.5 Snippets 처리 및 표시 확인
- Snippets 탭 클릭
- 언어별 필터 동작 확인
- 스니펫 목록 표시 확인
- 코드 접기/펼치기 기능 확인

#### 2.6 Export 다운로드 동작 확인
- Timeline 다운로드 (JSON/MD)
- Issues 다운로드 (JSON/MD)
- 전체 다운로드 (ZIP)
- 다운로드된 파일명 확인 (session_id 기반)
- 다운로드된 파일 내용 확인

### 3. 에러 처리 확인

#### 3.1 파일 크기 초과
- 10MB 이상의 파일 업로드 시도
- 에러 메시지 표시 확인

#### 3.2 잘못된 파일 형식
- `.md`가 아닌 파일 업로드 시도
- 에러 메시지 표시 확인

## API Contract 일치 확인

### 1. Query 파라미터 이름 확인
- 네트워크 탭에서 API 요청 확인
- `use_llm` 파라미터가 snake_case로 전송되는지 확인
- 예: `http://localhost:8000/api/parse?use_llm=true`

### 2. Enum 값 일치 확인
- `scripts/verify_api_contract.py` 실행
- EventType, ArtifactAction, ExportFormat, IssueStatus 값 일치 확인

### 3. Request/Response 타입 일치 확인
- TypeScript 컴파일 오류 없음 확인
- 실제 API 응답과 프론트엔드 타입 비교

### 4. Optional 필드 일치 확인
- 백엔드 모델의 Optional 필드와 프론트엔드 타입의 Optional 필드 비교

## 검증 체크리스트

- [ ] 모든 타입이 백엔드 모델과 1:1 매핑
- [ ] Enum 값이 문자열 리터럴로 정확히 일치
- [ ] Query 파라미터 이름이 snake_case로 일치 (`use_llm`)
- [ ] 필드명, 타입, Optional 여부 모두 일치
- [ ] Request/Response 스키마 일치
- [ ] 파일 업로드 및 파싱 동작
- [ ] Timeline 생성 및 표시
- [ ] Issues 생성 및 표시
- [ ] Snippets 처리 및 표시
- [ ] Export 다운로드 동작

## 테스트 결과 문서화

테스트 완료 후 다음 정보를 기록하세요:

1. **테스트 실행 명령어**
   - 서버 실행 명령어
   - 테스트 파일 경로

2. **테스트 통과 상태**
   - PASS / FAIL
   - 각 단계별 통과 여부

3. **발견된 문제점**
   - 문제 설명
   - 재현 방법
   - 해결 방법 (해결된 경우)

4. **사용자 피드백**
   - UI/UX 개선 사항
   - 버그 또는 문제점
   - 기능 요청 사항

