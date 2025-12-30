"""
Body에 코드 블록이 제거되었는지 확인하는 스크립트 (Phase 4.3)
"""

from pathlib import Path
from backend.parser import parse_markdown

# 테스트 파일 파싱
input_file = Path("docs") / "longcontext_phase_4_3.md"
text = input_file.read_text(encoding="utf-8")
result = parse_markdown(text, str(input_file))

# Body에 코드 펜스(```)가 포함된 Turn 찾기
turns_with_code = [t for t in result["turns"] if "```" in t.body]

print(f"Total turns: {len(result['turns'])}")
print(f"Turns with code blocks in body: {len(turns_with_code)}/{len(result['turns'])}")

if turns_with_code:
    print("\n[WARNING] Turns with code blocks in body:")
    for t in turns_with_code[:10]:  # 처음 10개만 출력
        print(f"  Turn {t.turn_index}: {len(t.body)} chars, code_blocks: {len(t.code_blocks)}")
        print(f"    Body preview: {t.body[:100]}...")
        # 코드 펜스가 있는 위치 확인
        import re

        code_fences = list(re.finditer(r"```+", t.body))
        print(
            f"    Code fences found: {len(code_fences)} at positions: {[m.start() for m in code_fences]}"
        )
else:
    print("\n[PASS] No code blocks in body! All code blocks were successfully removed.")
