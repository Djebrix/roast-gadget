#!/usr/bin/env python3
"""Write a one-line roast of a gadget used every day to entry.txt.

Standard library only, no network, deterministic: the same roast is
written on every run.
"""

import os

ROAST = (
    "My robot vacuum mapped my whole flat in one afternoon, then spent "
    "every morning since eating the same charging cable like it's the "
    "only thing it was built to find."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert text.strip(), "roast must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
