"""Entry for make.fun fortune-cookie-wisdom-for-developers.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt, then validates the output: UTF-8 text,
a single line, 1 to 120 characters.

Deterministic: the program writes the same line every run. No network
access.
"""

import os
import sys

ENTRY = "The legacy code you fear was once someone's proudest Friday deploy."
MAX_CHARS = 120


def _validate(path: str) -> None:
    """Check the written file is one UTF-8 line within the char limit."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if "\n" in text:
        sys.exit("entry.txt must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        sys.exit("entry is %d chars, expected 1-%d" % (len(text), MAX_CHARS))
    if text != ENTRY:
        sys.exit("entry.txt does not match the entry line")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    _validate(dest)
    print("wrote %s (%d chars)" % (dest, len(ENTRY)))


if __name__ == "__main__":
    main()
