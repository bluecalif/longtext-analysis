"""
Turn 36 디버깅: 코드 블록이 body에 남아있는 이유 확인
"""
from pathlib import Path
from backend.parser import parse_markdown
from backend.parser.snippets import extract_code_blocks_with_positions

# 테스트 파일 파싱
input_file = Path('docs') / 'longcontext_phase_2.md'
text = input_file.read_text(encoding='utf-8')

# Turn 분할
from backend.parser.turns import split_to_turns
turn_blocks = split_to_turns(text)

# Turn 36 확인
if len(turn_blocks) > 36:
    block_36 = turn_blocks[36]
    lines_36 = block_36.split('\n')
    print(f"Turn 36 total lines: {len(lines_36)}")

    # 코드 블록 위치 정보 추출
    code_blocks_with_positions = extract_code_blocks_with_positions(block_36, 36, debug=False)
    print(f"Code blocks extracted: {len(code_blocks_with_positions)}")

    # 각 코드 블록의 위치 출력
    print("\nCode block positions:")
    for idx, (cb, start_line, end_line) in enumerate(code_blocks_with_positions[:10]):  # 처음 10개만
        print(f"  Block {idx}: lines {start_line}-{end_line}, lang={cb.lang}, code_length={len(cb.code)}")

    # 마지막 코드 블록 위치 확인
    if code_blocks_with_positions:
        last_cb, last_start, last_end = code_blocks_with_positions[-1]
        print(f"\nLast code block: lines {last_start}-{last_end}, code_length={len(last_cb.code)}")
        print(f"  Start line: {lines_36[last_start] if last_start < len(lines_36) else 'N/A'}")
        print(f"  End line: {lines_36[last_end] if last_end < len(lines_36) else 'N/A'}")

    # body에서 제거된 라인 확인
    code_block_line_indices = set()
    for cb, start_line, end_line in code_blocks_with_positions:
        for line_idx in range(start_line, end_line + 1):
            code_block_line_indices.add(line_idx)

    print(f"\nTotal lines in code blocks: {len(code_block_line_indices)}")
    print(f"Total lines in block: {len(lines_36)}")
    print(f"Lines to keep in body: {len(lines_36) - len(code_block_line_indices)}")

    # body 생성
    body_lines = [line for idx, line in enumerate(lines_36) if idx not in code_block_line_indices]
    body = '\n'.join(body_lines)

    # body에 코드 펜스가 있는지 확인
    import re
    code_fences = list(re.finditer(r'```+', body))
    print(f"\nCode fences in body: {len(code_fences)}")
    if code_fences:
        print("  Positions:")
        for match in code_fences[:5]:  # 처음 5개만
            start_pos = match.start()
            # 해당 위치 주변 텍스트 출력
            context_start = max(0, start_pos - 50)
            context_end = min(len(body), start_pos + 50)
            print(f"    Position {start_pos}: ...{body[context_start:context_end]}...")

