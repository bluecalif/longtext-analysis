# 상세 지침 초안 (v0.1)
대상: Cursor 세션 대화 Markdown → Timeline / IssueCards / Snippets 생성 앱  
목표: “사람이 읽기 쉬움 + LLM/IDE Rule로 재사용 가능” 수준의 안정성 확보

---

## 1) 파서(구조 추출) 레이어 지침
**핵심:** “포맷이 조금 바뀌어도 무너지지 않는” 견고한 구조 추출이 전체 품질을 좌우함.

### 1.1 입력 포맷 가정(최소)
- 문서 상단: 메타 텍스트(Phase/Exported at/Cursor version 등) — 없을 수도 있음
- Turn 블록: 구분선(`---`) 기준 분리, 블록 내부에 `**User**` 또는 `**Cursor**` 라벨 포함(변형 가능)
- 코드 블록: 펜스 ```lang ... ``` (lang 누락 가능)
- 파일/경로: `TODOs.md`, `*.mdc`, `backend/...`, `*.ts(x)`, `*.py`, `*.sql` 등이 자연어 문장 중간에 등장

> “Cursor export 템플릿 변경”을 전제로, **룰 기반 + fallback(LMM)** 구조로 설계한다.

### 1.2 파싱 단계(권장 파이프라인)
1) **Normalize**
   - 줄바꿈 통일(`\r\n` → `\n`)
   - 탭/공백 정리(단, 코드블록 내부는 보존)
2) **Extract Header Meta (best-effort)**
   - 상단 N줄에서 phase/subphase/exported_at/cursor_version 추출
3) **Split to Turn Blocks**
   - 1차: `^\s*---\s*$` 기준
   - 2차 fallback: `**User**`/`**Cursor**` 라벨 기준으로 재분할(구분선이 없을 때)
4) **Parse Turn**
   - speaker: User/Cursor/Unknown
   - body: 코드블록 제거한 텍스트
   - code_blocks: lang + code
   - path_candidates: 파일/경로 후보 리스트
   - inline_commands: `npm ...`, `python ...`, `psql ...` 같은 실행 커맨드 후보(선택)
5) **Parse Health Check**
   - 전체 Turn 중 speaker Unknown 비율이 높으면 “포맷 감지 실패”로 간주 → fallback 파서/LLM 메타 추출

### 1.3 정규식 세트(예시)
#### (A) 구분선 / speaker
- Turn split:
  - `TURN_SPLIT_RE = r"^\s*---\s*$" (re.M)`
- Speaker:
  - `SPEAKER_RE = r"^\s*\*\*(User|Cursor)\*\*\s*$" (re.M)`

#### (B) 코드블록
- `CODE_FENCE_RE = r"```(\w+)?\n(.*?)```" (re.S)`
- lang 누락 시 `""` 처리, 이후 “언어 추정” 단계에서 보완(선택)

#### (C) 파일/경로 후보(보수적으로)
- 단순 확장자 기반:
  - `PATH_RE = r"(?:(?:[\w.-]+[/\\])+[\w.-]+\.(?:md|mdc|py|ts|tsx|sql)|TODOs\.md|[\w.-]+\.(?:md|mdc|py|ts|tsx|sql))"`
- 너무 공격적으로 잡으면 false positive 증가 → MVP에서는 “후보”로만 저장하고 후단에서 확정(action 판단 포함)한다.

### 1.4 출력(파서 산출물) 표준
`Turn` 표준 구조(예):
- turn_index
- speaker: "User" | "Cursor" | "Unknown"
- body: string
- code_blocks: [{lang, code, block_index}]
- path_candidates: string[]
- anchors: {mentions_phase?, mentions_subphase?, has_error_triggers?} (선택)

### 1.5 실패 대응(Fallback)
#### Fallback 1: Split heuristic
- `---`가 거의 없으면:
  - `**User**` 등장 위치를 기준으로 분할
  - `**Cursor**`를 기준으로 분할
  - “speaker 라벨이 없는 구간”은 Unknown turn으로 두되, body만 유지

#### Fallback 2: LLM meta extraction (옵션)
- 상단/전체에서 meta만 뽑기:
  - phase/subphase/exported_at/cursor_version
- 단, **LLM은 구조 추출의 주역이 되면 비용/불안정이 커짐** → meta/요약 보조로 제한

### 1.6 파서 테스트 케이스(필수)
최소 6종을 준비:
1) 정상 케이스: `---` + speaker 라벨 + 코드펜스 + 파일경로
2) `---` 없음: speaker 라벨만 존재
3) speaker 라벨 변형(공백/대소문자/굵게 누락)
4) 코드펜스 lang 누락
5) 코드블록 내부에 ```가 포함된 edge(희소)
6) 파일 경로가 괄호/백틱/인용문 안에 존재

테스트는 “turn_count / speaker 분포 / code_blocks 수 / path 후보 수”를 기본 검증으로 둔다.

---

## 2) 이벤트/이슈 연결(링킹) 지침
**핵심:** “요약”을 넘어 “재사용 가능한 작업지식”이 되려면 연결이 필요함.
- User 증상 ↔ Cursor 원인 ↔ Fix(코드/SQL) ↔ 검증 방법 ↔ 수정 파일
이 5개가 카드/타임라인에서 **서로 참조**되어야 한다.

### 2.1 표준 이벤트 모델(최소)
- `MessageEvent`: 사용자 요청/커서 응답 (요약 + 원문참조)
- `ArtifactEvent`: 파일/스크립트/문서에 대한 작업(mention/create/modify/execute)
- `DebugEvent`: symptom/cause/evidence/fix/validation 단서를 포함하는 사건

> 처음부터 “정교한 타입 분류”를 과하게 하지 말고,  
> MVP는 `type=turn|debug|artifact|completion|plan` 정도로 시작 → 점진 고도화.

### 2.2 연결의 기본 원칙(룰 기반)
#### (A) “근접성” 우선
- 이슈 카드는 보통 “User 문제제기 → 바로 이어지는 Cursor 분석/수정 제안” 구조가 많음
- 따라서 **슬라이딩 윈도우(예: 최근 6~10 turns)** 내에서 연결 후보를 찾는다.

#### (B) “키워드 트리거”로 후보 생성
- Debug trigger(원인/에러):
  - `violates check constraint`, `ERROR`, `Exception`, `stack trace`, `constraint`, `failed`, `원인`, `해결`, `조치`, `검증`
- Fix trigger(조치):
  - `ALTER TABLE`, `UPDATE`, `git commit`, `scripts/`, `fix`, `patch`, `수정`, `반영`
- Validation trigger(검증):
  - `확인`, `검증`, `테스트`, `scenario`, `체크`, `repro`, `UI에서 확인`

#### (C) “산출물(파일/코드)”은 링크의 접착제
- Turn 안에 파일 경로나 코드블록이 있으면
  - 해당 Turn을 `ArtifactEvent`로 만들고
  - 가장 가까운 `DebugEvent` 또는 해당 subphase의 `TimelineEvent`에 붙인다.

### 2.3 이슈 카드 생성 알고리즘(권장 MVP)
1) **Seed(시작점)**: User turn에서 symptom 후보 탐지  
   - 예: “안 보임/없음/에러/% 증가인데도…” 같은 패턴
2) **Attach(원인/증거)**: 이후 Cursor turns에서 debug trigger 매칭
3) **Attach(fix)**: 코드펜스(sql/ts/py) 또는 “수정/스크립트/SQL 제시” 문구 탐지
4) **Attach(validation)**: “이렇게 확인하세요/테스트 시나리오” 목록 탐지
5) **Close(완결)**: root_cause + fix 중 하나라도 확보되면 카드 생성
   - root_cause 없으면 status=hypothesis
   - fix가 없으면 “조치 미확정 카드”로 남겨도 됨(추후 세션에서 이어붙이기 위해)

### 2.4 “이어지는 이슈” 처리(세션을 넘나듦)
- issue_id에 `session_id + local_seq`를 기본으로 하되,
- 다음 세션에서 동일 이슈를 “reopen/continue”할 수 있게 `canonical_key` 필드를 둔다(선택).
  - 예: `canonical_key = "insights.type.check_constraint_negative"`

### 2.5 LLM 보조 적용 포인트(추천)
룰로 뽑은 카드 초안이 “조잡할 때”만 LLM을 호출:
- 입력: 최근 N개 turn 텍스트 + 뽑힌 후보들(symptom candidates, error lines, code blocks id)
- 출력:  
  - root_cause 요약(confirmed/hypothesis)  
  - evidence 핵심 1~3개  
  - fix 요약 + snippet_id 연결  
  - validation 체크리스트 2~5개

**주의:** LLM에게 “새로운 사실” 만들지 않게
- “반드시 입력 텍스트에 있는 내용만”
- “없는 건 null 또는 hypothesis로”

### 2.6 링킹 테스트 케이스
- (1) 한 이슈에 fix가 여러 개(sql + ts)인 경우 → 모두 같은 카드에 연결
- (2) 한 turn에 2개 이슈가 섞인 경우 → 카드 분리(LLM 보조 필요 가능)
- (3) 증상(User) 없이 Cursor가 선제 디버깅하는 경우 → seed를 Cursor trigger로 허용
- (4) fix는 있는데 root cause가 없는 경우 → status=hypothesis 유지

---

## 3) 코드 스니펫 분리 저장 + 참조 설계 지침
**핵심:** “문서 비대화/중복/민감정보”를 막으면서도, timeline/issue에서 코드가 쉽게 열람되어야 함.

### 3.1 스니펫 저장의 기본 정책
- 원본 MD의 코드펜스는 전부 추출하여 `Snippet`으로 저장한다.
- Timeline/IssueCards에는 코드를 “직접 포함”하지 않고 `snippet_id[]`로 참조한다.
- Markdown 렌더에서만 “미리보기(일부/접기)” 형태로 노출(옵션)

### 3.2 snippet_id 규칙(중요)
권장:
- `SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang}`
예:
- `SNP-cursor_export_2025-12-14_223636_KST-012-00-sql`

장점:
- 재생성해도 ID가 안정적(원본 순서가 바뀌지 않는 한)
- 추적이 쉬움(turn/block로 원문 역추적)

### 3.3 중복 제거(dedup) 규칙
- 코드가 완전히 동일하면(공백 정규화 후) 같은 `snippet_hash`로 묶고
- 대표 snippet을 하나만 저장하되, `aliases[]`에 원래 snippet_id를 기록(선택)

예시 해시:
- `sha256(normalize(code))`

### 3.4 언어 판별(lang) 규칙
- fence lang가 있으면 우선 사용
- 없으면 간단 휴리스틱:
  - `ALTER TABLE|SELECT|UPDATE` → sql
  - `import ... from|export|const|interface` → ts/tsx
  - `def |import |from fastapi` → python
  - `npm |yarn |pnpm` → bash
- 판별 실패 시 `lang="text"`로 두고, UI에서 수동 수정(차기)

### 3.5 파일 분리 저장 구조(권장)
- `snippets.json` : 전체 메타 + code 포함(기본)
- `snippets/` 폴더:
  - `SNP-...sql`, `SNP-...ts`, `SNP-...py`로 개별 파일 저장(옵션)
- 다운로드:
  - `snippets.json` 단일 다운로드
  - `snippets.zip` (폴더 압축) 제공(옵션)

### 3.6 참조(링크) 구조
- IssueCard.fix: `{summary, snippet_refs:[...]}`
- TimelineEvent.snippet_refs: `[...]`
- Snippet.links: `{issue_id?, event_seq?, paths?:[...]}`

“paths”는 해당 코드가 언급한 파일경로 후보를 함께 담아두면 재사용성이 올라감.

### 3.7 민감정보/비밀정보 마스킹(필수 권장)
- 기본 마스킹 룰(정규식):
  - `(?i)apikey|api_key|secret|token|bearer\s+[A-Za-z0-9\-_\.]+`
  - `service_role|supabase.*key`
- 마스킹 정책:
  - 원본 코드는 보존하지 않는(=저장 전에 마스킹) 모드와
  - 원본 보존 + 내보내기 시 마스킹 모드를 분리(설정)
- MVP 권장: “저장 전 마스킹” 기본값(안전)

### 3.8 스니펫 테스트 케이스
- (1) 동일 SQL이 여러 번 등장(중복 제거 동작)
- (2) lang 누락 펜스(휴리스틱으로 sql/ts/py 판별)
- (3) 민감정보 포함(마스킹 적용)
- (4) 매우 긴 코드(미리보기는 앞 20줄만, 전체는 다운로드에서)

---

## 부록 A) MVP 구현 순서(추천)
1) 파서 안정화(턴 파싱 + 코드펜스 + path 후보)
2) snippets 분리 저장 + 참조 구조 확정
3) 룰 기반 Issue seed/attach/close 구현
4) LLM은 “요약/라벨링 보조”로 마지막에 추가

---

## 부록 B) 최소 QA 체크리스트
- speaker Unknown 비율이 20% 이상이면 경고
- code_blocks 추출 0인데 코드가 있는 듯하면 경고(펜스 탐지 실패)
- issues 0인데 debug trigger가 존재하면 경고(링킹 실패 가능)
- snippets 참조가 있는데 snippets.json에 없으면 오류
