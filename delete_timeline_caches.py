"""
Timeline 관련 캐시 삭제 스크립트
"""
from backend.core.pipeline_cache import invalidate_cache
from backend.core.cache import CACHE_DIR
from pathlib import Path

print("=" * 80)
print("Timeline 관련 캐시 삭제")
print("=" * 80)

# 1. timeline_sections 캐시 삭제
print("\n[1] timeline_sections 캐시 삭제:")
count1 = invalidate_cache(cache_type="timeline_sections")
print(f"  - 삭제된 파일 수: {count1}개")

# 2. main_tasks 캐시 삭제
print("\n[2] main_tasks 캐시 삭제:")
main_tasks_files = list(Path(CACHE_DIR).glob("main_tasks_*.json"))
count2 = len(main_tasks_files)
for cache_file in main_tasks_files:
    print(f"  - 삭제: {cache_file.name}")
    cache_file.unlink()

print(f"  - 삭제된 파일 수: {count2}개")

print("\n" + "=" * 80)
print("캐시 삭제 완료")
print("=" * 80)

