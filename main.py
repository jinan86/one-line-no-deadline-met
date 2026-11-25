#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry program (program/v1).

Writes a single one-line excuse for a missed deadline to
/output/entry.txt. Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "I tried to negotiate a two-day extension and somehow agreed "
    "to deliver it yesterday instead."
)


def entry() -> str:
    """Return the final one-line entry text, exactly as submitted."""
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must be one complete sentence"
    return text


def main() -> None:
    """Write the entry text to /output/entry.txt."""
    text = entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
