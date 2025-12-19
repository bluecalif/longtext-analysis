# 상세 지침 (구체화 버전 v0.2)
대상: Cursor 세션 대화 Markdown → Timeline / IssueCards / Snippets (JSON + MD) 생성  
목표: “포맷 변화에 견딤 + 재사용 가능한 연결(링킹) + 코드 분리 저장”을 **규칙/테스트 중심**으로 고정

---

## 0) 권장 구현 구조(파일/모듈)
- `parser/`
  - `normalize.py` : 텍스트 정규화
  - `meta.py` : 세션 메타 추출
  - `turns.py` : Turn 분할/파싱
  - `snippets.py` : 코드펜스 추출/언어판별/마스킹/중복제거
  - `artifacts.py` : 파일경로 후보 추출/분류/액션추정
- `builders/`
  - `timeline_builder.py`
  - `issues_builder.py` (링킹/카드생성)
- `render/`
  - `render_md.py`
- `tests/`
  - `fixtures/*.md`
  - `golden/*.json`
  - `test_parser.py`, `test_linking.py`, `test_snippets.py`

---

## 1) 파서(구조 추출) — 규칙 테이블 + 구현 지침

### 1.1 Normalize 규칙(필수)
| 항목 | 규칙 | 비고 |
|---|---|---|
| 줄바꿈 | `\r\n` → `\n`, `\r` → `\n` | 코드블록 내부도 동일 적용 OK |
| BOM 제거 | `\ufeff` 제거 | Windows export 대비 |
| 트레일링 공백 | 라인 끝 공백 제거(코드블록 제외 옵션) | MVP는 전체 제거해도 대체로 OK |
| 너무 긴 공백 | 3개 이상 공백은 2개로 축소(코드블록 제외 옵션) | 가독성 |

---

### 1.2 Session Meta 추출 규칙(정규식 카탈로그)
> 상단 2000~4000 chars 범위에서 best-effort로 추출. 없으면 null.

| 필드 | 정규식(우선순위) | 예시 |
|---|---|---|
| exported_at | `(?i)Exported\s+(\d{4}-\d{2}-\d{2}[^,\n]*?(?:KST|UTC|GMT|[+\-]\d{2}:\d{2})?)` | `Exported 2025-12-14 22:36:36 KST` |
| cursor_version | `(?i)\bCursor\s+(\d+\.\d+\.\d+)\b` | `Cursor 2.2.20` |
| phase | `(?i)\bPhase\s+(\d+)\b` | `Phase 6` |
| subphase | `(?i)\bSub\s*Phase\s+(\d+)\b` | `Sub Phase 7` |

**세션ID 생성 규칙(고정):**
- `session_id = f"cursor_export_{exported_at_or_fallback}"`  
- 문자열 정규화: 공백 `_`, `:` 제거, `+09:00` 같은 tz 유지 가능

---

### 1.3 Turn 분할 규칙(핵심)
#### 1차 분할(가장 신뢰)
- `TURN_SPLIT_RE = r"^\s*---\s*$" (re.M)`
- 결과 block list: 빈 블록 제거

#### 2차 Fallback 분할(구분선 누락 대비)
- 스캐닝하면서 `**User**` / `**Cursor**` 라벨 라인을 기준으로 새로운 Turn 시작
- 라벨이 없는 텍스트는 이전 Turn에 붙이되, 첫 라벨 전 텍스트는 `preamble`로 따로 저장

---

### 1.4 Speaker 라벨 판별(허용 변형 포함)
| 케이스 | 정규식 |
|---|---|
| 기본 | `^\s*\*\*(User|Cursor)\*\*\s*$` (re.M) |
| 변형(콜론 포함) | `^\s*\*\*(User|Cursor)\*\*\s*:\s*$` (re.M) |
| 변형(굵게 누락) | `^\s*(User|Cursor)\s*:\s*$` (re.M) *(fallback 전용)* |

> speaker가 Unknown인 Turn이 20% 이상이면 “포맷 감지 실패 경고” + fallback 파서 적용

---

### 1.5 코드블록 추출(펜스)
- `CODE_FENCE_RE = r"```([a-zA-Z0-9_+-]+)?\n(.*?)```" (re.S)`
- 추출 결과:
  - `lang`: 소문자화, 없으면 `""`
  - `code`: 원문 유지(단, 후속 단계에서 마스킹/정규화)

**주의(엣지):**
- 코드 내부에 ``` 등장 가능(희소). MVP는 “단순 펜스”로 충분.
- 필요 시 고도화: “펜스가 열린 뒤 동일 펜스 길이로 닫히는지” 검사

---

### 1.6 파일/경로 후보 추출(보수적 + 후보로만)
| 목적 | 정규식 |
|---|---|
| 일반 경로 | `(?:(?:[\w.-]+[/\\])+[\w.-]+\.(?:md|mdc|py|ts|tsx|sql|json))` |
| 단일 파일 | `(?:\b[\w.-]+\.(?:md|mdc|py|ts|tsx|sql|json)\b)` |
| 특수(고정) | `\bTODOs\.md\b` |

**권장:** 후보를 바로 확정하지 말고 `path_candidates[]`로 저장 후, artifacts 단계에서 필터/분류.

---

## 2) Snippets(코드 분리 저장) — 규칙 테이블 + 골든 테스트

### 2.1 snippet_id 규칙(안정성 최우선)
- `snippet_id = f"SNP-{session_id}-{turn_index:03d}-{block_index:02d}-{lang_or_guess}"`

### 2.2 언어 추정(펜스 lang 없을 때) — 휴리스틱 룰
| lang | 트리거(정규식) |
|---|---|
| sql | `(?i)\b(ALTER\s+TABLE|SELECT\s+|UPDATE\s+|INSERT\s+INTO|DELETE\s+FROM|CREATE\s+TABLE)\b` |
| typescript | `(?i)\b(import\s+.+from|export\s+|interface\s+|type\s+|const\s+|let\s+|async\s+function)\b` |
| python | `(?i)\b(def\s+|from\s+\w+\s+import|import\s+\w+|if\s+__name__\s*==\s*['"]__main__['"])\b` |
| bash/ps | `(?i)^\s*(npm|yarn|pnpm|python|pip|uv|git)\b` *(라인 시작 기반)* |

결정 규칙:
- fence lang가 있으면 우선 사용
- 없으면 위 트리거 매칭 점수 합산 → 최고 점수 lang 선택
- 모두 0점이면 `text`

---

### 2.3 중복 제거(dedup)
- `snippet_hash = sha256(normalize_code(code))`
- `normalize_code` 권장:
  - 줄끝 공백 제거
  - 연속 빈 줄 3개 이상 → 2개로
  - (옵션) 탭→4스페이스
- 동일 hash면 대표 1개 저장 + `aliases[]`로 원래 snippet_id 기록(선택)

---

### 2.4 민감정보 마스킹(기본 ON 권장)
**마스킹 대상(대표 패턴):**
- `(?i)\b(api[_-]?key|secret|token|service[_-]?role)\b`
- `(?i)\bBearer\s+[A-Za-z0-9\-_\.=]+\b`
- Supabase 키 흔적:
  - `(?i)\bSUPABASE_(URL|ANON_KEY|SERVICE_ROLE_KEY)\b\s*=\s*.+`
  - `(?i)\b(anon|service_role)\b\s*key` (자연어 포함)

**마스킹 규칙:**
- 값 부분을 `***REDACTED***`로 치환
- 원문 보존 모드는 옵션(기본은 저장 전 마스킹)

---

## 3) Artifacts(산출물) 분류 & action 추정 — 규칙 테이블

### 3.1 kind 분류(확장자 기반)
- `.md` → `document`
- `.mdc` → `cursor_rule`
- `.py` → `python`
- `.ts|.tsx` → `typescript`
- `.sql` → `sql`
- 그 외 → `other`

### 3.2 action 추정(룰 기반, MVP)
> 텍스트가 “정확히 무엇을 했다”를 명시하지 않는 경우가 많으므로, action은 보수적으로.

| action | 트리거(본문/문구) |
|---|---|
| create | `작성|생성|추가|create|add` + 파일경로 |
| modify | `수정|변경|반영|update|modify|patch` + 파일경로 |
| execute | `실행|run|테스트|검증` + 커맨드/스크립트 |
| mention | 위 조건 불충분 시 기본 |

**주의:** Cursor 응답에 “수정된 파일:” 목록이 자주 등장 → 그 블록은 modify로 우선 추정.

---

## 4) 링킹(대화 ↔ 산출물 ↔ 디버깅) — 구체 알고리즘

### 4.1 이벤트 타입 taxonomy(MVP 고정)
Timeline Event `type`은 아래 최소 집합으로 시작:
- `status_review`
- `plan_gate`
- `completion_summary`
- `artifact`
- `debug_hypothesis`
- `debug_root_cause_confirmed`
- `fix_proposed`
- `validation_instruction`
- `ops_maintenance`
- `next_step`
- `turn` *(fallback)*

> 너무 세분화하면 오탐/미탐이 늘고 유지보수가 어려워짐. MVP는 위로 고정.

---

### 4.2 Debug trigger 규칙(정규식)
| 분류 | 트리거 |
|---|---|
| error line | `(?i)\b(error|exception|stack trace|violates check constraint|constraint)\b` |
| 원인 암시 | `원인|Root cause|because|due to` |
| 조치 암시 | `해결|조치|수정|patch|fix|ALTER TABLE|UPDATE|script` |
| 검증 암시 | `검증|확인|테스트|scenario|check` |

**DebugEvent 생성 조건(MVP):**
- Cursor turn이며 `error line` 또는 `원인/조치/검증` 중 하나라도 존재 → DebugEvent 후보

---

### 4.3 Issue 카드 생성(슬라이딩 윈도우 + 스코어링)
**핵심:** “근접성 + 트리거 점수”로 연결을 안정화.

- 윈도우: `W = 10 turns` (User symptom seed 이후 Cursor 10턴까지 탐색)
- seed(시작) 조건:
  - User turn에 아래 중 1개 이상:
    - `없|안 보|에러|문제|왜` 또는 `%` 또는 숫자 지표(예: 79.6)
- attach 규칙:
  - 후보 Cursor turn마다 점수 계산 후 상위 turn을 root_cause/fix/validation에 배정

**점수 예시(간단):**
- `error line` 포함: +5
- `원인` 포함: +4
- `ALTER TABLE|UPDATE` 등 SQL 트리거: +4 (fix 후보)
- `검증|확인|테스트` 포함: +3 (validation 후보)
- 파일경로 언급 1개당: +1 (artifact 연결 강화)
- seed에서의 거리(턴 차이) 패널티: `-0.3 * distance`

**카드 완료 조건(MVP):**
- root_cause 또는 fix 중 하나라도 있으면 카드 생성
- root_cause 없으면 `status=hypothesis`

---

### 4.4 “이어지는 이슈(세션 넘김)” 대비 필드
IssueCard에 다음 필드를 추가 권장:
- `canonical_key` (옵션)
  - 생성 규칙(룰): root_cause 텍스트에서 `table/constraint/endpoint` 같은 엔티티 추출 → join
  - 예: `insights.type:insights_type_check`

---

## 5) 출력 스키마(고정) + 검증 규칙

### 5.1 timeline.json schema(핵심 필드)
- `session_meta`: {session_id, exported_at?, cursor_version?, phase?, subphase?, source_doc}
- `timeline`: [
  - {seq, type, phase?, subphase?, summary, artifacts?, snippet_refs?, turn_ref?}
]

### 5.2 issues.json schema(핵심 필드)
- `issues`: [
  - {issue_id, scope:{session_id, phase?, subphase?}, title, symptoms[], root_cause:{status,text}?, evidence[], fix[], validation[], related_artifacts[], snippet_refs[]}
]

### 5.3 snippets.json schema(핵심 필드)
- `snippets`: [
  - {snippet_id, lang, code, hash, source:{turn_index,block_index}, links:{issue_id?, event_seq?}, masked:bool}
]

**QA 규칙(필수):**
- timeline의 snippet_refs는 snippets.json에 모두 존재해야 함
- issues의 snippet_refs도 동일
- speaker Unknown 비율 20% 이상이면 경고

---

## 6) 골든 테스트(fixtures + expected outputs)

### 6.1 Fixture 1 — 정상(구분선 + speaker + SQL)
**파일:** `tests/fixtures/fixture1.md`
```md
Phase 6 - Exported 2025-12-14 22:36:36 KST, Cursor 2.2.20
---
**User**
202502가 3개월 평균 대비 79.6% 증가인데도 피드백이 없어요. 왜죠?
---
**Cursor**
DB 저장 시 오류가 발생합니다: new row violates check constraint insights_type_check
해결: 아래 SQL을 실행하세요.
```sql
ALTER TABLE insights DROP CONSTRAINT IF EXISTS insights_type_check;
ALTER TABLE insights ADD CONSTRAINT insights_type_check
  CHECK (type IN ('negative','positive','improvement','next_month'));
