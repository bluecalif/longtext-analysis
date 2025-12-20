# Phase 3.2 LLM 기반 E2E 테스트 결과 분석

> **테스트 실행 시점**: 2025-12-20 16:00:31
> **처리 방법**: LLM (gpt-4.1-mini)
> **실행 시간**: 약 3분 44초 (224.59초)

---

## 실행 결과 요약

### 기본 통계

- **총 Turn**: 67개
- **총 Event**: 67개 (1:1 매핑 달성 ✅)
- **처리 방법**: 모든 이벤트가 `processing_method: "llm"`으로 처리됨

### 이벤트 타입 분포 (LLM 기반)

| 타입 | 개수 | 비율 |
|------|------|------|
| status_review | 25 | 37.3% |
| plan | 21 | 31.3% |
| next_step | 4 | 6.0% |
| completion | 5 | 7.5% |
| debug | 7 | 10.4% |
| turn | 5 | 7.5% |
| **artifact** | **0** | **0%** |

### 정규식 기반과 비교

| 항목 | 정규식 기반 | LLM 기반 | 차이 |
|------|------------|----------|------|
| 총 이벤트 | 67개 | 67개 | 동일 |
| turn 타입 | 31개 (46.3%) | 5개 (7.5%) | -26개 |
| artifact 타입 | 10개 (14.9%) | 0개 (0%) | -10개 |
| debug 타입 | 26개 (38.8%) | 7개 (10.4%) | -19개 |
| status_review | 0개 (0%) | 25개 (37.3%) | +25개 |
| plan | 0개 (0%) | 21개 (31.3%) | +21개 |
| next_step | 0개 (0%) | 4개 (6.0%) | +4개 |
| completion | 0개 (0%) | 5개 (7.5%) | +5개 |

---

## 주요 발견사항

### 1. 이벤트 타입 분류 개선

**LLM의 장점**:
- 정규식 기반에서는 대부분 `turn` (31개) 또는 `debug` (26개)로 분류
- LLM은 더 세밀하게 분류: `status_review` (25개), `plan` (21개) 등
- 의미 있는 타입 분류 비율이 크게 증가

**예시**:
- 정규식: "프로젝트 현황을 파악 중입니다" → `debug` 또는 `turn`
- LLM: "프로젝트 현황을 파악 중입니다" → `status_review` ✅

### 2. Artifact 타입 분류 이슈

**문제점**:
- LLM 기반에서는 `artifact` 타입 이벤트가 0개
- 하지만 실제로는 `artifacts` 배열에 파일 경로가 포함되어 있음

**원인 분석**:
- LLM은 파일 경로를 인식하고 `artifacts` 배열에 추가함
- 하지만 이벤트 타입은 파일 경로보다 텍스트의 주요 목적을 우선시하여 분류
- 예: "@TODOs.md를 확인하세요" → 타입: `status_review`, artifacts: [TODOs.md]

**영향**:
- Artifact 연결은 정상 작동 (artifacts 배열에 포함)
- 하지만 이벤트 타입 통계에서 artifact 타입이 0%로 표시됨
- 이는 LLM의 분류 방식 특성상 정상적인 동작일 수 있음

### 3. Summary 품질 개선

**LLM Summary 예시**:
```json
{
  "type": "status_review",
  "summary": "프로젝트는 Phase 5를 완료하고 Phase 6의 Sub Phase 7 대시보드 기능 재구성을 앞두고 있으며, 백엔드는 완료 상태이고 프론트엔드는 약 67% 진행 중입니다. 다음 작업으로 Sub Phase 7을 시작할 준비가 되어 있습니다."
}
```

**정규식 Summary 예시**:
```json
{
  "type": "debug",
  "summary": "TODOs.md를 확인해 프로젝트 현황을 파악 중입니다.\n\n프로젝트 현황 요약:\n\n- 현재 상태: Phase 5 완료, Phase 6 진행 중..."
}
```

**개선점**:
- LLM Summary는 더 간결하고 의미 있는 요약 제공
- 정규식 Summary는 원문을 그대로 자르는 경향

### 4. Artifact 연결 분석

**LLM 기반 Artifact 연결**:
- `artifacts` 배열에 파일 경로가 포함된 이벤트: 다수
- 하지만 이벤트 타입은 `artifact`가 아닌 다른 타입으로 분류
- 예: `status_review` 타입이지만 `artifacts: [TODOs.md]` 포함

**정규식 기반 Artifact 연결**:
- `artifact` 타입 이벤트: 10개
- 파일 경로가 있으면 무조건 `artifact` 타입으로 분류

---

## 종합 평가

### 개선된 부분

1. ✅ **이벤트 타입 분류 정확도**: LLM이 더 세밀하고 의미 있는 분류 제공
2. ✅ **Summary 품질**: LLM이 더 간결하고 의미 있는 요약 생성
3. ✅ **1:1 매핑 달성**: 모든 Turn이 정확히 1개의 Event로 변환

### 주의할 부분

1. ⚠️ **Artifact 타입 분류**: LLM은 파일 경로를 인식하지만 `artifact` 타입으로 분류하지 않음
   - 실제로는 `artifacts` 배열에 포함되어 있어 연결은 정상 작동
   - 이벤트 타입 통계에서만 `artifact` 타입이 0%로 표시됨

2. ⚠️ **실행 시간**: 약 3분 44초 (정규식 기반 대비 약 220배 느림)
   - 캐싱 적용 시 재실행 시에는 훨씬 빠를 것으로 예상

---

## 다음 단계

1. **Phase 3.3**: 결과 평가 방법 구축
   - 수동 검증 데이터셋 생성
   - 정성적 평가 수행
   - LLM vs 정규식 비교 분석

2. **Artifact 타입 분류 개선** (선택적)
   - LLM 프롬프트에 artifact 타입 분류 가이드라인 강화
   - 또는 정규식과 LLM 하이브리드 접근 (파일 경로가 있으면 artifact 우선)

---

## 참고 파일

- **LLM E2E 테스트 리포트**: `tests/reports/event_normalizer_e2e_llm_report.json`
- **LLM E2E 테스트 결과**: `tests/results/event_normalizer_e2e_llm_20251220_160031.json`
- **정규식 E2E 테스트 결과**: `tests/results/event_normalizer_e2e_20251220_152352.json`

