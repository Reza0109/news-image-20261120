#!/usr/bin/env python3
"""Entrypoint: copy the pre-rendered entry.png to the output directory.

Python standard library only, no network. The program runs twice and both
runs must write the same bytes, so this copies the file as-is and verifies
the copy landed intact.
"""

import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_SIDE = 1024


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def check_png(path):
    """Gate checks: valid PNG, at most 1 MiB, at most 1024x1024."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        return "too large: %d bytes" % size
    with open(path, "rb") as f:
        head = f.read(33)
    if head[:8] != PNG_MAGIC:
        return "not a PNG file"
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        return "too big: %dx%d" % (width, height)
    return None


def main():
    problem = check_png(SRC)
    if problem:
        print("error: entry.png fails the gate: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    if sha256(SRC) != sha256(dst):
        print("error: copy mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
