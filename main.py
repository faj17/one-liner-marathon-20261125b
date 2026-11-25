#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes one original one-line comedy joke to /output/entry.txt
(1-280 characters, UTF-8, a single line). Standard library only,
no network, no input.

The line is built from two fragments: a setup (the zoo's new
exhibit — a plain, concrete scene, deadpan documentary voice)
and a punch (the exhibit is just a mirror, and its label names
the visitor: apex predator, currently doomscrolling — the turn
lands in the last two words). ``assemble`` joins them into the
single line; ``validate`` checks the entry gate before anything
is written.
"""

from pathlib import Path

SETUP = "The zoo's new exhibit is just a mirror labelled"
PUNCH = "'apex predator, currently doomscrolling'."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one joke line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-280 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 280:
        raise ValueError(f"line must be 1-280 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
