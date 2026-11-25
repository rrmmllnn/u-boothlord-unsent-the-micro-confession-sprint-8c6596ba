#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes a two-part micro-confession to /output/entry.txt: a To: line
naming who the unsent message was meant for, and the unsent line
itself, written exactly as it was typed, with no explanation after it.

Gate: /output/entry.txt must be UTF-8 text of 1 to 260 characters;
the message line itself is at most 200 characters.
"""

from pathlib import Path

ENTRY = (
    "To: my little brother\n"
    "I broke your bike the summer you blamed Sam, and I let you stay angry at him for three years.\n"
)


def main() -> None:
    lines = ENTRY.splitlines()
    assert len(lines) == 2, "entry must be exactly two parts"
    assert lines[0].startswith("To: "), "first line must name the addressee"
    assert 1 <= len(ENTRY) <= 260, "gate: entry must be 1-260 characters"
    assert len(lines[1]) <= 200, "judge brief: message at most 200 characters"
    assert ENTRY.strip(), "gate: entry must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
