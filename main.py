#!/usr/bin/env python3
"""One Letter: Coffee or Tea - entrypoint.

Writes exactly one letter to /output/entry.txt: "A", the letter the
bounty brief assigns to coffee. The kit gate requires UTF-8 text of
exactly 1 character, not only whitespace, and the judge counts only
the letters A (coffee) and B (tea) as answers at all.
"""

import os

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """The kit's gate, as asserts: UTF-8 text of exactly 1 to 1
    characters, not only whitespace."""
    assert len(text) == 1, "entry must be exactly one character"
    assert text.isalpha(), "entry must be a letter"
    assert text.strip() != "", "entry must not be whitespace"


def main() -> None:
    check_gate(LETTER)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: re-read what actually landed on disk and hold it to
    # the same gate, byte for byte, no trailing newline.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == LETTER.encode("utf-8"), "written bytes differ from the letter"
    check_gate(raw.decode("utf-8"))
    print(f"GATE OK: {len(LETTER)} character")


if __name__ == "__main__":
    main()
