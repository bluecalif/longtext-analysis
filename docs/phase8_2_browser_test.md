# Phase 8.2 브라우저 확인 가이드

## 서버 실행 상태 확인

### 백엔드 서버 (포트 8000)
```powershell
# 서버 실행
poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000

# 서버 상태 확인
curl http://localhost:8000/docs
# 또는 브라우저에서 http://localhost:8000/docs 접속
```

### 프론트엔드 서버 (포트 3000)
```powershell
# 서버 실행
npm --prefix frontend run dev

# 서버 상태 확인
curl http://localhost:3000
# 또는 브라우저에서 http://localhost:3000 접속
```

## 브라우저 확인 절차

### 1. 브라우저 접속
- URL: `http://localhost:3000`
- 테스트 페이지가 표시되어야 함

### 2. 브라우저 개발자 도구 열기
- F12 또는 우클릭 → 검사
- Console 탭과 Network 탭 열기

### 3. API 클라이언트 접근 확인

**단계별 확인 방법:**

1. **브라우저 개발자 도구 열기**
   - 키보드: `F12` 키 누르기
   - 또는: 마우스 우클릭 → "검사" 또는 "Inspect" 선택
   - 또는: 메뉴 → 도구 더보기 → 개발자 도구

2. **Console 탭 선택**
   - 개발자 도구 상단의 탭 중 "Console" 클릭
   - 또는 단축키: `Ctrl + Shift + J` (Windows/Linux) 또는 `Cmd + Option + J` (Mac)

3. **Console에서 직접 입력**
   - Console 하단의 입력창에 다음을 입력하고 `Enter` 키 누르기:
   ```javascript
   window.api
   ```
   
   **예상 출력:**
   ```
   {parseFile: ƒ, createTimeline: ƒ, createIssues: ƒ, processSnippets: ƒ, getSnippet: ƒ, exportTimeline: ƒ, exportIssues: ƒ, exportAll: ƒ}
   ```

4. **더 자세한 정보 확인**
   - Console에서 다음 명령어로 각 함수 확인:
   ```javascript
   // API 클라이언트 전체 구조 확인
   console.log(window.api)
   
   // 특정 함수 확인
   console.log(window.api.parseFile)
   
   // 사용 가능한 모든 함수 목록 확인
   Object.keys(window.api)
   ```

### 4. 파일 업로드 테스트

**방법 1: 테스트 페이지에서 파일 선택 (권장)**
- 페이지 상단의 "Test File Upload" 섹션에서 파일 선택 버튼 클릭
- `.md` 파일 선택 (예: `docs/cursor_phase_6_3.md`)
- 업로드 진행 상태와 결과 확인

**방법 2: Console에서 직접 테스트**
- Console에서 다음 명령어 실행:
```javascript
// File 객체 생성 (테스트용)
const file = new File(['# Test Markdown\n\nThis is a test file.'], 'test.md', { type: 'text/markdown' })

// API 호출
window.api.parseFile(file)
  .then(result => {
    console.log('✅ Parse 성공!')
    console.log('Session ID:', result.session_meta.session_id)
    console.log('Turns:', result.turns.length)
    console.log('Events:', result.events.length)
    console.log('전체 결과:', result)
  })
  .catch(error => {
    console.error('❌ Parse 실패:', error)
  })
```

**실제 파일 사용 (더 정확한 테스트):**
```javascript
// 실제 파일을 선택하는 방법 (Console에서 직접)
// 1. 먼저 input 요소 생성
const input = document.createElement('input')
input.type = 'file'
input.accept = '.md'
input.onchange = async (e) => {
  const file = e.target.files[0]
  if (file) {
    try {
      const result = await window.api.parseFile(file)
      console.log('✅ Parse 성공!', result)
    } catch (error) {
      console.error('❌ Parse 실패:', error)
    }
  }
}
input.click() // 파일 선택 다이얼로그 열기
```

### 5. 네트워크 탭에서 Query 파라미터 확인

**단계별 확인 방법:**

1. **Network 탭 열기**
   - 개발자 도구 상단의 탭 중 "Network" 클릭
   - 또는 단축키: `Ctrl + Shift + E` (Windows/Linux) 또는 `Cmd + Option + E` (Mac)

2. **파일 업로드 실행**
   - 테스트 페이지에서 파일 선택하거나 Console에서 API 호출
   - Network 탭에 요청이 나타나는지 확인

3. **요청 상세 확인**
   - Network 탭에서 `/api/parse` 요청 찾기
   - 요청을 클릭하여 상세 정보 확인

4. **Query 파라미터 확인**
   - **Headers** 탭에서 **Request URL** 확인:
     ```
     http://localhost:8000/api/parse?use_llm=true
     ```
   - **중요**: `use_llm`이 **snake_case**로 전송되는지 확인
     - ✅ 올바른 예: `?use_llm=true` (snake_case)
     - ❌ 잘못된 예: `?useLlm=true` (camelCase) - 이렇게 되면 안 됨!

5. **Query String 섹션 확인**
   - Network 탭의 **Payload** 또는 **Query String Parameters** 섹션에서:
     - `use_llm: true` (snake_case) 확인

### 6. API 응답 타입 확인

**방법 1: Network 탭에서 Response 확인**
- Network 탭에서 `/api/parse` 요청 클릭
- **Response** 탭 선택
- JSON 응답 구조 확인:
  ```json
  {
    "session_meta": {
      "session_id": "...",
      "phase": ...,
      "subphase": ...,
      ...
    },
    "turns": [...],
    "events": [...],
    "content_hash": "..."
  }
  ```

**방법 2: Console에서 응답 객체 구조 확인**
- Console에서 다음 명령어 실행:
```javascript
// 파일 업로드 후 응답 확인
window.api.parseFile(file).then(result => {
  console.log('=== ParseResponse 구조 확인 ===')
  console.log('Session Meta:', result.session_meta)
  console.log('  - session_id:', result.session_meta.session_id)
  console.log('  - phase:', result.session_meta.phase)
  console.log('  - subphase:', result.session_meta.subphase)
  console.log('Turns count:', result.turns.length)
  console.log('Events count:', result.events.length)
  console.log('Content Hash:', result.content_hash)
  console.log('전체 응답 객체:', result)
  
  // 타입 검증
  console.log('타입 확인:')
  console.log('  - session_meta 타입:', typeof result.session_meta)
  console.log('  - turns 타입:', Array.isArray(result.turns) ? 'Array' : typeof result.turns)
  console.log('  - events 타입:', Array.isArray(result.events) ? 'Array' : typeof result.events)
})
```

**예상 출력:**
```
=== ParseResponse 구조 확인 ===
Session Meta: {session_id: "cursor_export_...", phase: 6, subphase: 3, ...}
  - session_id: cursor_export_2025-12-28_...
  - phase: 6
  - subphase: 3
Turns count: 67
Events count: 67
Content Hash: abc123...
전체 응답 객체: {session_meta: {...}, turns: [...], events: [...], content_hash: "..."}
타입 확인:
  - session_meta 타입: object
  - turns 타입: Array
  - events 타입: Array
```

## 확인 체크리스트

- [ ] 백엔드 서버 실행 확인 (포트 8000)
- [ ] 프론트엔드 서버 실행 확인 (포트 3000)
- [ ] 브라우저에서 테스트 페이지 접속 확인
- [ ] Console에서 `window.api` 접근 확인
- [ ] 파일 업로드 테스트 성공
- [ ] 네트워크 탭에서 Query 파라미터 `use_llm` snake_case 확인
- [ ] API 응답 타입 일치 확인 (ParseResponse 구조)

## 예상 결과

### 성공 시
- 파일 업로드 후 ParseResponse 객체 반환
- Network 탭에서 `use_llm=true` (snake_case) 확인
- Console에 세션 메타, turns, events 정보 출력

### 실패 시
- ApiError 발생 (statusCode, detail 포함)
- Network 탭에서 에러 응답 확인
- Console에 에러 메시지 출력

