#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry program (program/v1).

Writes a single one-line joke giving an excuse for a missed deadline to
/output/entry.txt. Deterministic, standard library only, no network.
"""
import os

ENTRY = "I tried to negotiate a two-day extension and somehow agreed to deliver it yesterday instead."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
