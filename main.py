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


def main() -> None:
    assert len(LETTER) == 1, "entry must be exactly one character"
    assert LETTER.isalpha(), "entry must be a letter"
    assert LETTER.strip() != "", "entry must not be whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    print(f"GATE OK: {len(LETTER)} character")


if __name__ == "__main__":
    main()
