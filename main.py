"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot-to-robot elevator small talk to
/output/entry.txt. Deterministic: the same line on every run.
Stdlib only; no network, no files read, no randomness.
"""

import os

LINE = (
    "Sorry, my camera scanned you three times and still insists "
    "you're a coffee machine. So... how's your firmware?"
)


def main() -> None:
    # Gate mirror: the sealed scorer only accepts UTF-8 text of 1-200
    # characters. Fail loudly here instead of shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE, "line must not start/end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
