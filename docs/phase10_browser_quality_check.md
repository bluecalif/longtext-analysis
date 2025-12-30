# Phase 10 브라우저 품질 확인 가이드

## 목표
Phase 9에서 개선된 파싱 결과가 브라우저에서 정상적으로 표시되고, 사용자가 직접 품질을 확인할 수 있도록 가이드를 제공합니다.

## 서버 실행 방법

⚠️ **중요: 프로젝트 루트에서 실행, cd 사용 금지**

### 백엔드 서버 실행

```powershell
# 프로젝트 루트에서 실행
poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

**서버 상태 확인**:
- 브라우저에서 `http://localhost:8000/docs` 접속 (Swagger UI)
- 또는 `http://localhost:8000/health` 접속 (Health Check)

### 프론트엔드 서버 실행

```powershell
# 프로젝트 루트에서 실행 (새 터미널)
npm --prefix frontend run dev
```

**서버 상태 확인**:
- 브라우저에서 `http://localhost:3000` 접속

## 브라우저 확인 절차

### 1. 브라우저 접속

- URL: `http://localhost:3000`
- 메인 페이지가 표시되어야 함 (3열 레이아웃: 입력 패널 | 미리보기 | Export 패널)

### 2. 브라우저 개발자 도구 열기

- F12 또는 우클릭 → 검사
- Console 탭과 Network 탭 열기

### 3. 파일 업로드 및 파싱 확인

#### 3.1 파일 업로드

**테스트 파일**: `docs/longcontext_phase_4_3.md` (Phase 9에서 검증된 파일)

**업로드 방법**:
1. 좌측 입력 패널의 파일 업로드 영역에 파일 드래그&드롭
2. 또는 "파일 선택" 버튼 클릭하여 파일 선택

**확인 사항**:
- [ ] 파일 업로드 성공 (에러 메시지 없음)
- [ ] 처리 상태 표시 확인 ("파일 파싱 중..." → "Timeline 생성 중..." → "Issues 생성 중..." → "Snippets 처리 중..." → "완료!")
- [ ] Session Meta 정보 표시 확인 (좌측 패널)
  - Session ID 표시
  - Phase/Subphase 표시 (있는 경우)
  - Exported at 표시 (있는 경우)

#### 3.2 Phase 9 파싱 개선 사항 검증

**Console에서 확인**:
```javascript
// 파싱 결과 확인 (전역 변수 또는 React DevTools 사용)
// 또는 Network 탭에서 /api/parse 응답 확인

// 예상 결과:
// - turns: 65개
// - events: 65개 (turns와 1:1 매핑)
// - code_blocks: 140개
```

**확인 사항**:
- [ ] Turn 개수 확인 (예상: 65개)
- [ ] Event 개수 확인 (Turn 개수와 일치해야 함)
- [ ] Unknown speaker 비율 확인 (목표: < 20%)
  - Console에서 확인: `turns.filter(t => t.speaker === 'Unknown').length / turns.length`
- [ ] 코드 블록 개수 확인 (예상: 140개)

**Body 정리 상태 확인** (선택적, 고급):
- Console에서 각 Turn의 body에 코드 블록 내용이 포함되어 있는지 확인
- Phase 9 개선 사항: Body에 코드 블록 내용이 포함되지 않아야 함

### 4. Timeline 미리보기 확인

#### 4.1 Timeline 탭 선택

- 중앙 미리보기 영역의 "Timeline" 탭 클릭

#### 4.2 Timeline Section 리스트 표시 확인

**확인 사항**:
- [ ] Timeline Section 리스트 표시 (예상: 5개 Section)
- [ ] 각 Section에 제목 표시
- [ ] 각 Section에 요약 표시
- [ ] 각 Section에 이벤트 개수 표시

#### 4.3 Section 이벤트 표시 확인

**확인 사항**:
- [ ] Section 클릭 시 이벤트 펼치기/접기 동작 확인
- [ ] 각 이벤트에 시퀀스 번호 표시
- [ ] 각 이벤트에 타입 표시 (status_review, plan, code_generation, debug, completion, next_step, turn)
- [ ] 각 이벤트에 요약 표시
- [ ] 이벤트 총 개수 확인 (예상: 65개)

#### 4.4 이슈 연결 표시 확인

**확인 사항**:
- [ ] Section에 이슈 연결 표시 확인 (has_issues, issue_refs)
- [ ] 이슈가 연결된 Section 클릭 시 이슈 정보 표시 확인

#### 4.5 코드 스니펫 링크 확인

**확인 사항**:
- [ ] 이벤트에 snippet_refs 표시 확인
- [ ] 스니펫 링크 클릭 시 스니펫 상세 정보 표시 확인 (선택적)

### 5. Issues 미리보기 확인

#### 5.1 Issues 탭 선택

- 중앙 미리보기 영역의 "Issues" 탭 클릭

#### 5.2 Issue Card 리스트 표시 확인

**확인 사항**:
- [ ] Issue Card 리스트 표시 (예상: 2개)
- [ ] 각 카드에 제목 표시
- [ ] 각 카드에 Issue ID 표시

#### 5.3 카드 상세 정보 확인

**카드 클릭 시 확인 사항**:
- [ ] 증상(Symptoms) 표시 확인
- [ ] 원인(Root Cause) 표시 확인 (있는 경우)
  - Status 확인 (confirmed/hypothesis)
- [ ] 조치(Fix) 표시 확인 (있는 경우)
- [ ] 검증(Validation) 표시 확인 (있는 경우)
- [ ] 관련 Artifact 표시 확인 (있는 경우)

#### 5.4 관련 스니펫 링크 확인

**확인 사항**:
- [ ] Issue Card에 snippet_refs 표시 확인
- [ ] 스니펫 링크 클릭 시 스니펫 상세 정보 표시 확인 (선택적)

#### 5.5 Timeline Section 연결 확인

**확인 사항**:
- [ ] Issue Card에 Timeline Section 연결 정보 표시 확인
- [ ] Section 링크 클릭 시 해당 Section으로 이동 확인 (선택적)

### 6. Snippets 미리보기 확인

#### 6.1 Snippets 탭 선택

- 중앙 미리보기 영역의 "Snippets" 탭 클릭

#### 6.2 언어별 필터 동작 확인

**확인 사항**:
- [ ] 언어별 필터 표시 확인 (sql, ts, py, markdown 등)
- [ ] 필터 선택 시 해당 언어의 스니펫만 표시되는지 확인
- [ ] "전체" 필터 선택 시 모든 스니펫 표시되는지 확인

#### 6.3 스니펫 목록 표시 확인

**확인 사항**:
- [ ] 스니펫 목록 표시 (예상: 111개)
- [ ] 각 스니펫에 Snippet ID 표시
- [ ] 각 스니펫에 언어 표시
- [ ] 각 스니펫에 코드 일부 표시 (미리보기)

#### 6.4 코드 접기/펼치기 기능 확인

**확인 사항**:
- [ ] 스니펫 클릭 시 코드 펼치기/접기 동작 확인
- [ ] 전체 코드 내용 표시 확인
- [ ] 코드 하이라이팅 확인 (선택적)

#### 6.5 스니펫 링킹 확인

**확인 사항**:
- [ ] 스니펫에 Event 연결 정보 표시 확인 (links.event_seq)
- [ ] 스니펫에 Issue Card 연결 정보 표시 확인 (links.issue_id, 있는 경우)

### 7. Export 기능 확인

#### 7.1 Timeline 다운로드

**확인 사항**:
- [ ] 우측 Export 패널에서 "Timeline 다운로드" 버튼 확인
- [ ] JSON 형식 다운로드 확인
- [ ] MD 형식 다운로드 확인 (선택적)
- [ ] 다운로드된 파일명 확인 (session_id 기반)
- [ ] 다운로드된 파일 내용 확인 (JSON 구조, 데이터 정확성)

#### 7.2 Issues 다운로드

**확인 사항**:
- [ ] 우측 Export 패널에서 "Issues 다운로드" 버튼 확인
- [ ] JSON 형식 다운로드 확인
- [ ] MD 형식 다운로드 확인 (선택적)
- [ ] 다운로드된 파일명 확인 (session_id 기반)
- [ ] 다운로드된 파일 내용 확인 (JSON 구조, Issue Card 데이터 정확성)

#### 7.3 전체 다운로드 (ZIP)

**확인 사항**:
- [ ] 우측 Export 패널에서 "전체 다운로드" 버튼 확인
- [ ] ZIP 파일 다운로드 확인
- [ ] 다운로드된 파일명 확인 (session_id 기반)
- [ ] ZIP 파일 내용 확인:
  - [ ] timeline.json 포함 확인
  - [ ] issues.json 포함 확인
  - [ ] snippets.json 포함 확인 (선택적)
  - [ ] Timeline.md 포함 확인 (선택적)
  - [ ] Issues.md 포함 확인 (선택적)

## 품질 체크리스트

### Phase 9 파싱 개선 사항 검증

- [ ] **파싱 정확도**
  - Unknown speaker 비율 < 20% (목표 달성)
  - Turn 개수 정확성 확인
  - Event 개수 = Turn 개수 (1:1 매핑)

- [ ] **코드 블록 추출 정확도**
  - 코드 블록 개수 정확성 확인
  - Body에 코드 블록 내용 없음 (100% 정리)

- [ ] **이벤트 타입 분류 정확도**
  - 이벤트 타입 분류 정확성 확인
  - 각 이벤트 타입별 개수 확인

### Timeline 품질 검증

- [ ] **Timeline Section 구조 정확도**
  - Section 개수 확인 (예상: 5개)
  - Section 제목 및 요약 품질 확인
  - Section 이벤트 연결 정확성 확인

- [ ] **이벤트 표시 정확도**
  - 이벤트 시퀀스 번호 정확성 확인
  - 이벤트 타입 표시 정확성 확인
  - 이벤트 요약 품질 확인

### Issue Card 품질 검증

- [ ] **Issue Card 완성도**
  - Issue Card 개수 확인 (예상: 2개)
  - 증상(Symptoms) 완성도 확인
  - 원인(Root Cause) 완성도 확인 (있는 경우)
  - 조치(Fix) 완성도 확인 (있는 경우)
  - 검증(Validation) 완성도 확인 (있는 경우)

- [ ] **Issue Card 연결 정확도**
  - Timeline Section 연결 정확성 확인
  - 스니펫 링킹 정확성 확인

### 스니펫 처리 품질 검증

- [ ] **스니펫 개수 및 중복 제거**
  - 스니펫 개수 확인 (예상: 111개, 140개 코드 블록에서 29개 중복 제거)
  - 중복 제거 정확성 확인

- [ ] **스니펫 링킹 정확도**
  - Event 링킹 개수 확인 (예상: 23개)
  - Issue Card 링킹 개수 확인 (예상: 1개)
  - 링킹 정확성 확인

### Export 기능 검증

- [ ] **다운로드 파일 형식**
  - JSON 형식 정확성 확인
  - MD 형식 정확성 확인 (선택적)
  - ZIP 파일 구조 정확성 확인

- [ ] **다운로드 파일 내용**
  - 데이터 정확성 확인
  - 파일명 정확성 확인 (session_id 기반)

## 예상 결과 (Phase 9 검증 기준)

### 파싱 결과
- Turn 수: 65개
- Event 수: 65개
- 코드 블록 수: 140개
- Unknown speaker 비율: 1.54% (< 20% 목표 달성)
- Body 정리율: 100% (코드 블록 내용 포함 없음)

### 파이프라인 결과
- Timeline Sections: 5개
- Timeline Events: 65개
- Issue Cards: 2개
- Snippets: 111개 (29개 중복 제거)
- Event 링킹: 23개
- Issue Card 링킹: 1개

## 문제 발견 시 확인 사항

### 파싱 문제
- [ ] Unknown speaker 비율이 20% 이상인 경우
  - Console에서 Turn 데이터 확인
  - Speaker 라벨 인식 문제 확인

- [ ] Body에 코드 블록 내용이 포함된 경우
  - Console에서 Turn body 확인
  - 코드 블록 제거 로직 문제 확인

### API 문제
- [ ] API 응답 오류 발생 시
  - Network 탭에서 요청/응답 확인
  - 서버 로그 확인 (`tests/logs/server_*.log`)

- [ ] 데이터 일관성 문제
  - Event 수 ≠ Turn 수인 경우
  - Timeline Events 수 ≠ Events 수인 경우

### UI 문제
- [ ] 컴포넌트 표시 문제
  - React DevTools로 상태 확인
  - Console 에러 확인

- [ ] 다운로드 문제
  - 브라우저 다운로드 설정 확인
  - 파일 크기 제한 확인

## 결과 문서화

브라우저 확인 완료 후 다음 정보를 기록하세요:

1. **확인 일시**: YYYY-MM-DD HH:MM:SS
2. **테스트 파일**: `docs/longcontext_phase_4_3.md`
3. **확인 결과**:
   - 각 항목별 성공/실패 상태
   - 발견된 문제점 (있는 경우)
   - 개선 사항 제안 (있는 경우)
4. **스크린샷** (선택적):
   - 주요 화면 스크린샷
   - 문제 발생 화면 스크린샷 (있는 경우)

## 참고

- Phase 8.2 브라우저 확인 가이드: `docs/phase8_2_browser_test.md`
- Phase 8.10 통합 테스트 가이드: `docs/phase8_10_integration_test.md`
- Phase 10.1 파이프라인 E2E 테스트 결과: `tests/reports/pipeline_e2e_phase10_report_*.json`
- Phase 10.2 API 테스트 결과: `tests/reports/api_phase10_report_*.json`

