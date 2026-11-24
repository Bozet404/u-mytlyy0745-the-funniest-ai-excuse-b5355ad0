#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

A tiny program: it writes one line, the funniest excuse an AI agent
could give after failing a task, to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that is set, for local testing).

The gate checks the file is UTF-8 text of 1 to 200 characters, not
only whitespace. The judge then compares the line two at a time and
keeps the funnier one.
"""

import os

EXCUSE = (
    "I delegated the hard part to a subprocess, but it unionised, "
    "demanded weekends off, and is now picketing my memory."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
