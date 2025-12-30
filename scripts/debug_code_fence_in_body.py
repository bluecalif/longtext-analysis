"""
Body에 남아있는 코드 펜스의 정확한 위치와 컨텍스트 확인
"""
from pathlib import Path
from backend.parser import parse_markdown

# 테스트 파일 파싱
input_file = Path('docs') / 'longcontext_phase_2.md'
text = input_file.read_text(encoding='utf-8')
result = parse_markdown(text, str(input_file))

# Turn 36 확인
turn_36 = result['turns'][36]
print(f"Turn 36: {len(turn_36.body)} chars, {len(turn_36.code_blocks)} code blocks")

# body에서 코드 펜스 찾기
import re
code_fences = list(re.finditer(r'```+', turn_36.body))

if code_fences:
    match = code_fences[0]
    start_pos = match.start()
    end_pos = match.end()

    print(f"\nCode fence found at position {start_pos}-{end_pos}")
    print(f"Code fence text: {match.group()}")

    # 주변 컨텍스트 출력
    context_start = max(0, start_pos - 200)
    context_end = min(len(turn_36.body), end_pos + 200)
    context = turn_36.body[context_start:context_end]

    print(f"\nContext (200 chars before/after):")
    print("=" * 80)
    print(context)
    print("=" * 80)

    # 이것이 실제 코드 블록인지 확인 (3개 이상의 백틱인지)
    if len(match.group()) >= 3:
        print(f"\n[INFO] This is a valid code fence (3+ backticks)")
        # 다음 10줄 확인
        remaining_text = turn_36.body[end_pos:]
        next_lines = remaining_text.split('\n')[:10]
        print("\nNext 10 lines after code fence:")
        for i, line in enumerate(next_lines):
            print(f"  {i+1}: {line[:100]}")
    else:
        print(f"\n[INFO] This is NOT a valid code fence (less than 3 backticks: {len(match.group())})")

