# Phase 8.2 브라우저 확인 - 빠른 가이드

## 1분 안에 확인하기

### 1단계: 브라우저 개발자 도구 열기
- **F12** 키 누르기
- 또는 페이지에서 **우클릭 → 검사**

### 2단계: Console 탭에서 확인
- 개발자 도구 상단에서 **"Console"** 탭 클릭
- Console 하단 입력창에 다음 입력 후 **Enter**:
  ```javascript
  window.api
  ```

### 3단계: 결과 확인
**정상적인 경우:**
```
{parseFile: ƒ, createTimeline: ƒ, createIssues: ƒ, ...}
```

**문제가 있는 경우:**
```
undefined
```
→ 이 경우 페이지가 제대로 로드되지 않았거나, `window.api`가 노출되지 않은 것입니다.

### 4단계: 파일 업로드 테스트
- 페이지 상단의 **"Test File Upload"** 섹션에서 파일 선택 버튼 클릭
- `.md` 파일 선택 (예: `docs/cursor_phase_6_3.md`)
- 결과 확인

### 5단계: Network 탭에서 Query 파라미터 확인
- 개발자 도구에서 **"Network"** 탭 클릭
- 파일 업로드 후 `/api/parse` 요청 찾기
- 요청 클릭 → **Headers** 탭에서 **Request URL** 확인:
  ```
  http://localhost:8000/api/parse?use_llm=true
  ```
- ✅ `use_llm`이 **snake_case**로 되어 있는지 확인 (camelCase 아님!)

## 문제 해결

### `window.api`가 `undefined`인 경우
1. 페이지 새로고침 (F5)
2. 브라우저 콘솔에 에러가 있는지 확인
3. 프론트엔드 서버가 정상 실행 중인지 확인

### API 호출이 실패하는 경우
1. 백엔드 서버가 실행 중인지 확인 (`http://localhost:8000/docs`)
2. Network 탭에서 에러 응답 확인
3. Console 탭에서 에러 메시지 확인

