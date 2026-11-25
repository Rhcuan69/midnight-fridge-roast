#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes exactly one line of text to /output/entry.txt: an original
one-line roast of a smart fridge that refuses to open after midnight.

Pure Python standard library only. Deterministic: every run produces
byte-identical output.
"""

import os

LINE = "My fridge after midnight: 'We're closed.' It's my fridge, it's my food — and it still carded me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
