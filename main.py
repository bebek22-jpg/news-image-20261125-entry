#!/usr/bin/env python3
"""news-image-20261125 entry: copy the image beside this file to the output.

The image is drawn once and shipped in the repository, so the copy is
byte-identical on every run: no network, no randomness, no timestamps.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(OUT_DIR, "entry.png"))


if __name__ == "__main__":
    main()
