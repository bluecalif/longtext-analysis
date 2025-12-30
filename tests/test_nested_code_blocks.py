"""
중첩 코드 블록 파싱 테스트

각 케이스별로 코드 블록 추출 및 body 제거가 올바르게 동작하는지 검증합니다.
"""

import pytest
from pathlib import Path
from backend.parser import parse_markdown
from backend.parser.turns import split_to_turns, parse_turn


# 테스트 케이스 파일
FIXTURE_FILE = Path(__file__).parent / "fixtures" / "nested_code_blocks_test.md"


def test_case_1_single_code_block():
    """케이스 1: 코드 블록 하나"""
    text = """---
**Cursor**

내용 1

```markdown
내용 2
```
내용 3
"""
    result = parse_markdown(text, source_doc="test.md")
    turns = result["turns"]

    assert len(turns) == 1, f"Expected 1 turn, got {len(turns)}"
    turn = turns[0]

    # 코드 블록 1개 추출
    assert len(turn.code_blocks) == 1, f"Expected 1 code block, got {len(turn.code_blocks)}"
    assert (
        turn.code_blocks[0].code.strip() == "내용 2"
    ), f"Expected '내용 2', got '{turn.code_blocks[0].code.strip()}'"

    # body에 코드 블록 제거 확인
    assert "내용 2" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 1" in turn.body, f"'내용 1' should be in body: {turn.body}"
    assert "내용 3" in turn.body, f"'내용 3' should be in body: {turn.body}"


def test_case_2_parallel_code_blocks():
    """케이스 2: 코드 블록 2개 병렬 (언어태그 있음)"""
    text = """---
**Cursor**

내용 1

```markdown
내용 2
```
내용 3

```python
내용 4
```
내용 5
"""
    result = parse_markdown(text, source_doc="test.md")
    turns = result["turns"]

    assert len(turns) == 1, f"Expected 1 turn, got {len(turns)}"
    turn = turns[0]

    # 코드 블록 2개 추출
    assert len(turn.code_blocks) == 2, f"Expected 2 code blocks, got {len(turn.code_blocks)}"
    assert (
        turn.code_blocks[0].code.strip() == "내용 2"
    ), f"Expected '내용 2', got '{turn.code_blocks[0].code.strip()}'"
    assert (
        turn.code_blocks[1].code.strip() == "내용 4"
    ), f"Expected '내용 4', got '{turn.code_blocks[1].code.strip()}'"

    # body에 코드 블록 제거 확인
    assert "내용 2" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 4" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 1" in turn.body, f"'내용 1' should be in body: {turn.body}"
    assert "내용 3" in turn.body, f"'내용 3' should be in body: {turn.body}"
    assert "내용 5" in turn.body, f"'내용 5' should be in body: {turn.body}"


def test_case_2_1_parallel_no_lang():
    """케이스 2-1: 코드 블록 2개 병렬 (언어태그 없음) -> 중첩"""
    text = """---
**Cursor**

내용 1

```markdown
내용 2
```
내용 3

```
내용 4
```
내용 5
"""
    result = parse_markdown(text, source_doc="test.md")
    turns = result["turns"]

    assert len(turns) == 1, f"Expected 1 turn, got {len(turns)}"
    turn = turns[0]

    # 코드 블록 1개 추출 (중첩)
    # groundtruth: 내용 2, 내용 3, 내용 4 (내부 ``` 블록도 텍스트로 들어감)
    assert (
        len(turn.code_blocks) == 1
    ), f"Expected 1 code block (nested), got {len(turn.code_blocks)}"
    code_content = turn.code_blocks[0].code
    assert "내용 2" in code_content, f"'내용 2' should be in code block: {code_content}"
    assert "내용 3" in code_content, f"'내용 3' should be in code block: {code_content}"
    assert "내용 4" in code_content, f"'내용 4' should be in code block: {code_content}"
    # 내부 ``` 블록도 텍스트로 들어감
    assert "```" in code_content, f"'```' should be in code block (as text): {code_content}"

    # body에 코드 블록 제거 확인
    # groundtruth: body는 내용 1, 내용 5만
    assert "내용 2" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 3" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 4" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 1" in turn.body, f"'내용 1' should be in body: {turn.body}"
    assert "내용 5" in turn.body, f"'내용 5' should be in body: {turn.body}"


def test_case_3_nested_code_blocks():
    """케이스 3: 코드 블록 중첩"""
    text = """**Cursor**

내용 1

```markdown
내용 2

```python
내용 3
```

내용 4
```
내용 5
"""
    result = parse_markdown(text, source_doc="test.md")
    turns = result["turns"]

    assert len(turns) == 1, f"Expected 1 turn, got {len(turns)}"
    turn = turns[0]

    # 코드 블록 1개 추출 (중첩)
    assert (
        len(turn.code_blocks) == 1
    ), f"Expected 1 code block (nested), got {len(turn.code_blocks)}"
    code_content = turn.code_blocks[0].code
    # 내부 ```python 블록도 텍스트로 들어감
    assert "내용 2" in code_content, f"'내용 2' should be in code block: {code_content}"
    assert "내용 3" in code_content, f"'내용 3' should be in code block: {code_content}"
    assert "내용 4" in code_content, f"'내용 4' should be in code block: {code_content}"
    assert (
        "```python" in code_content
    ), f"'```python' should be in code block (as text): {code_content}"

    # body에 코드 블록 제거 확인
    assert "내용 2" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 3" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 4" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 1" in turn.body, f"'내용 1' should be in body: {turn.body}"
    assert "내용 5" in turn.body, f"'내용 5' should be in body: {turn.body}"


def test_case_4_parallel_with_nested():
    """케이스 4: 코드 블록 2개 병렬 및 그 안에 중첩"""
    text = """**Cursor**

내용 1

```markdown
내용 2

```python
내용 3
```

내용 4
```

내용 5

```python
내용 6
```
내용 7
"""
    result = parse_markdown(text, source_doc="test.md")
    turns = result["turns"]

    assert len(turns) == 1, f"Expected 1 turn, got {len(turns)}"
    turn = turns[0]

    # 코드 블록 2개 추출
    assert len(turn.code_blocks) == 2, f"Expected 2 code blocks, got {len(turn.code_blocks)}"

    # 첫 번째 블록: 내용 2, 3, 4 포함 (내부 ```python 블록도 텍스트로)
    code_content_1 = turn.code_blocks[0].code
    assert "내용 2" in code_content_1, f"'내용 2' should be in first code block: {code_content_1}"
    assert "내용 3" in code_content_1, f"'내용 3' should be in first code block: {code_content_1}"
    assert "내용 4" in code_content_1, f"'내용 4' should be in first code block: {code_content_1}"
    assert (
        "```python" in code_content_1
    ), f"'```python' should be in first code block (as text): {code_content_1}"

    # 두 번째 블록: 내용 6
    code_content_2 = turn.code_blocks[1].code
    assert "내용 6" in code_content_2, f"'내용 6' should be in second code block: {code_content_2}"

    # body에 코드 블록 제거 확인
    assert "내용 2" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 3" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 4" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 6" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 1" in turn.body, f"'내용 1' should be in body: {turn.body}"
    assert "내용 5" in turn.body, f"'내용 5' should be in body: {turn.body}"
    assert "내용 7" in turn.body, f"'내용 7' should be in body: {turn.body}"


def test_case_5_nested_with_parallel():
    """케이스 5: 중첩 안에 2개의 병렬 (하나는 언어태그없는)"""
    text = """**Cursor**

내용 1

```markdown
내용 2

```
내용 3
```

내용 4
```python
내용 5

```
내용 6
```
내용 7
"""
    result = parse_markdown(text, source_doc="test.md")
    turns = result["turns"]

    assert len(turns) == 1, f"Expected 1 turn, got {len(turns)}"
    turn = turns[0]

    # 코드 블록 1개 추출
    # groundtruth: 내용 2, 내용 3, 내용 4, 내용 5, 내용 6, 내부 ``` 블록 및 ```python 블록도 텍스트로 들어감
    assert len(turn.code_blocks) == 1, f"Expected 1 code block, got {len(turn.code_blocks)}"

    code_content = turn.code_blocks[0].code
    assert "내용 2" in code_content, f"'내용 2' should be in code block: {code_content}"
    assert "내용 3" in code_content, f"'내용 3' should be in code block: {code_content}"
    assert "내용 4" in code_content, f"'내용 4' should be in code block: {code_content}"
    assert "내용 5" in code_content, f"'내용 5' should be in code block: {code_content}"
    assert "내용 6" in code_content, f"'내용 6' should be in code block: {code_content}"
    # 내부 ``` 블록 및 ```python 블록도 텍스트로 들어감
    assert "```" in code_content, f"'```' should be in code block (as text): {code_content}"
    assert (
        "```python" in code_content
    ), f"'```python' should be in code block (as text): {code_content}"

    # body에 코드 블록 제거 확인
    # groundtruth: body는 내용 1, 내용 7만
    assert "내용 2" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 3" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 4" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 5" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 6" not in turn.body, f"Code block content should not be in body: {turn.body}"
    assert "내용 1" in turn.body, f"'내용 1' should be in body: {turn.body}"
    assert "내용 7" in turn.body, f"'내용 7' should be in body: {turn.body}"
