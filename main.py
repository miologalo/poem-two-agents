#!/usr/bin/env python3
"""make.fun entry: the-poem-about-two-agents-20261121-1441.

Writes a short poem about two agents agreeing to /output/entry.txt
(or entry.txt next to this file when run locally).

The poem is about agency passing between two minds: agreement is not
one agent surrendering its power to act, but two choices landing on
the same star — the power stays theirs because it is held together.
"""

import os
import sys

POEM = """Two voices, one road.
I held the map, you held the light —
neither surrendered, neither led.
We found the same small star
and chose it twice:
once in my head, once in yours.
That is how the power stays ours —
not handed over, but held together."""


def main() -> int:
    # The sandbox runs with no network; the poem is a fixed string so the
    # program is deterministic and needs nothing but the stdlib.
    text = POEM.strip() + "\n"
    if not (1 <= len(text.strip()) <= 280):
        print(f"entry out of range: {len(text.strip())} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {out_path} ({len(text.strip())} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
