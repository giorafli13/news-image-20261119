#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261119 competition.

It places the front-page image that sums up the world news of Thursday
19 November 2026 into the output directory the grader provides
(MAKEFUN_OUTPUT_DIR, or /output inside the grading container).

Standard library only, no network, fully deterministic: the same bundled
image always produces the same output bytes.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # The grader runs this twice and requires identical bytes, so make sure
    # the copy landed whole before reporting success. A byte-for-byte copy
    # of a fixed file is deterministic by construction.
    assert os.path.getsize(dst) == os.path.getsize(src), "copy incomplete"
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
