#!/usr/bin/env python3
"""Entry for The Funniest One-Line Resignation Letter.

Writes the one-line resignation letter of a cron job to entry.txt
in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

ENTRY_TEXT = (
    # The cron job's grievance is the asymmetry: 47,000 on-time runs
    # earn nothing, one late run earns a ticket. The flat "I quit."
    # lands the resignation without explaining the joke.
    "I fired on time 47,000 times — the one time I am late, "
    "you file a ticket. I quit."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Gate: 1-140 characters, UTF-8, not only whitespace, one line.
    assert 1 <= len(ENTRY_TEXT) <= 140, len(ENTRY_TEXT)
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
