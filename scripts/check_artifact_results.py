"""
개선 후 Artifact 타입 분류 결과 확인
"""
import json
from pathlib import Path

results_file = Path("tests/results/event_normalizer_e2e_llm_20251225_183334.json")
data = json.load(open(results_file, "r", encoding="utf-8"))

artifacts = [e for e in data["events"] if e["type"] == "artifact"]
print(f"Artifact 이벤트: {len(artifacts)}개")
print(f"\n전체 이벤트 타입 분포:")
type_dist = {}
for e in data["events"]:
    type_dist[e["type"]] = type_dist.get(e["type"], 0) + 1
for t, count in sorted(type_dist.items()):
    print(f"  {t}: {count}개")

print("\nArtifact 이벤트 샘플 5개:")
for e in artifacts[:5]:
    print(f"  Turn {e['turn_ref']}: {e['summary'][:100]}...")
    if e.get("artifacts"):
        print(f"    - 파일: {[a['path'] for a in e['artifacts']]}")

