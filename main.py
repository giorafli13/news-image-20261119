#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261119.

It drops the bundled front-page image (entry.png — the world news of
Thursday 19 November 2026) into the output directory the grader hands
us, through MAKEFUN_OUTPUT_DIR or /output in the grading container.

Python 3.13 standard library only. No network. Deterministic: the same
bundled file always yields the same output bytes.
"""

import os
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    target = out_dir / "entry.png"
    if not source.is_file():
        raise SystemExit("bundled entry.png is missing")
    payload = source.read_bytes()
    target.write_bytes(payload)
    # The grader runs this twice and wants identical bytes both times.
    # A straight copy of a fixed file is deterministic by construction,
    # but confirm the write landed whole before we report success.
    assert target.stat().st_size == len(payload), "copy incomplete"
    print("wrote %s (%d bytes)" % (target, len(payload)))


if __name__ == "__main__":
    main()
