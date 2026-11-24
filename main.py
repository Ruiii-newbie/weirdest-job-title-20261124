#!/usr/bin/env python3
"""Weirdest Job Title entry for make.fun.

Writes exactly one job title (60 characters or fewer, nothing else)
to /output/entry.txt. No network, no input files, no randomness:
the output is the same on every run.
"""

TITLE = "Professional Mourner for Strangers' Funerals"

# The gate requires 1-60 characters of non-whitespace UTF-8 text.
# Fail loudly instead of shipping an invalid entry.
assert 1 <= len(TITLE.strip()) <= 60, "title must be 1-60 characters"
assert TITLE.strip() == TITLE, "title must have no leading/trailing space"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)
    print(TITLE)


if __name__ == "__main__":
    main()
