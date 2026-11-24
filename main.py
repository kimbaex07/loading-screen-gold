#!/usr/bin/env python3
"""Write the loading-screen tip in entry.txt to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python standard library. Validates the tip against the competition gate:
UTF-8 text of 1 to 200 characters, not only whitespace, a single line.
"""

import os
import sys

MAX_CHARS = 200


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(here, "entry.txt")
    try:
        with open(src_path, "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        print(f"error: cannot read {src_path}: {exc}", file=sys.stderr)
        return 1
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"error: entry.txt is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    # Strip at most one trailing newline, then at most one trailing CR.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]

    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"error: entry must be 1-{MAX_CHARS} characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    if text.strip() == "":
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print(
            "error: entry must be a single line (no newline/CR inside)",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)
    os.chmod(out_path, 0o644)
    print(f"wrote {out_path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
