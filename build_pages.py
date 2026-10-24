#!/usr/bin/env python3
"""Produce a verified, self-contained GitHub Pages site."""
import shutil

from play import GAME, ROOT, SHA256, digest, prepare


def main():
    prepare()
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    target = output / "index.html"
    shutil.copyfile(GAME, target)
    if digest(target) != SHA256:
        raise RuntimeError("Pages artifact checksum mismatch")
    (output / ".nojekyll").touch()
    print("Verified Pages entry point:", target)


if __name__ == "__main__":
    main()
