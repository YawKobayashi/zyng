import sys
from pathlib import Path
from typing import List, Tuple, Optional

ZYNG_FENCE = "```zyng"

def extract_zyng_blocks(markdown: str) -> List[str]:
    """
    Extract ```zyng ... ``` fenced code blocks from a markdown string.
    Returns a list of block contents (without fences).
    """
    lines = markdown.splitlines()
    in_block = False
    current: List[str] = []
    blocks: List[str] = []

    for line in lines:
        if not in_block and line.strip().startswith(ZYNG_FENCE):
            in_block = True
            current = []
            continue
        if in_block and line.strip().startswith("```"):
            # end of block
            blocks.append("\n".join(current))
            in_block = False
            current = []
            continue
        if in_block:
            current.append(line)
    return blocks


def parse_line(line: str) -> Optional[Tuple[str, str, Optional[str]]]:
    """
    Very small subset of Zyng:
      show "message" :::now
      show "message" :::yest
      show "message" :::tomo
      show "message" :::at:"2025-12-03T21:00:00+09:00"
    Returns (command, message, time_attr).
    Lines that are empty or unsupported return None.
    """
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None

    # split time attribute if present
    time_attr = None
    if ":::at:" in stripped:
        before, after = stripped.split(":::at:", 1)
        stripped = before.strip()
        time_attr = f'at:{after.strip()}'
    elif ":::" in stripped:
        before, after = stripped.split(":::", 1)
        stripped = before.strip()
        time_attr = after.strip()

    if stripped.startswith("show "):
        # expect show "message"
        rest = stripped[len("show "):].strip()
        if rest.startswith('"') and rest.endswith('"') and len(rest) >= 2:
            msg = rest[1:-1]
        else:
            # not strict; accept raw text
            msg = rest
        return ("show", msg, time_attr)

    return None


def run_zyng_block(block: str) -> None:
    for raw_line in block.splitlines():
        parsed = parse_line(raw_line)
        if parsed is None:
            continue
        cmd, msg, time_attr = parsed
        if cmd == "show":
            prefix = ""
            if time_attr:
                prefix = f"[{time_attr}] "
            print(prefix + msg)


def run_markdown_file(path: str) -> None:
    p = Path(path)
    if not p.is_file():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    text = p.read_text(encoding="utf-8")
    blocks = extract_zyng_blocks(text)
    if not blocks:
        print("No ```zyng blocks found.")
        return
    for block in blocks:
        run_zyng_block(block)


def main(argv: Optional[List[str]] = None) -> None:
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print("Usage: python -m zyng.runner <markdown-file>", file=sys.stderr)
        sys.exit(1)
    run_markdown_file(argv[0])


if __name__ == "__main__":
    main()
