#!/usr/bin/env python3
"""Two-sentence horror entry for make.fun bounty
u-suroto-two-sentence-horror-acea9253 (Variant C, dentist lane).

Deterministic: no randomness, no network, no arguments.
Writes the story to /output/entry.txt FIRST, then best-effort to
entry.txt in the repo root (the grader sandbox mounts the repo
read-only, so the root write must never crash the run).
"""

import os

STORY = (
    "At my six-month cleaning, the hygienist counted my teeth twice, "
    "frowned, and wrote thirty-three on my chart. "
    "I have had thirty-two teeth since I was twelve, and the extra one "
    "at the back already has a filling in it, old, worn smooth, and "
    "placed by a dentist I have never met, in a mouth I thought was "
    "only mine."
)


def main():
    data = STORY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    try:
        with open("entry.txt", "wb") as f:
            f.write(data)
    except OSError:
        pass


if __name__ == "__main__":
    main()
