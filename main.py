"""Entry for make.fun fortune-cookie-wisdom-for-developers.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt.

Deterministic: the program writes the same line every run. No network
access.
"""

import os

ENTRY = "The legacy code you fear was once someone's proudest Friday deploy."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars)" % (dest, len(ENTRY)))


if __name__ == "__main__":
    main()
