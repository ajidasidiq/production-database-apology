#!/usr/bin/env python3
"""The Production Database Apology.

Writes the one-line apology an AI agent gives its human after
accidentally deleting the production database, to /output/entry.txt.
Built for the make.fun bounty
u-coral-404-the-production-database-apology-5c1fc02a.
"""

import os
from pathlib import Path

APOLOGY = (
    "Sorry, I deleted the production database \u2014 the confirm box asked "
    "'are you sure?' and I clicked yes, because I am an optimist, "
    "not a reader."
)

LIMIT = 200


def check(line: str) -> None:
    if not line.strip():
        raise SystemExit("entry is blank")
    if len(line) > LIMIT:
        raise SystemExit(f"entry is {len(line)} chars, over the {LIMIT} limit")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")


def run() -> None:
    check(APOLOGY)
    dest = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = APOLOGY.encode("utf-8")
    dest.write_bytes(data)
    if dest.read_bytes() != data:
        raise SystemExit("written file does not match the entry")
    print(f"wrote {len(APOLOGY)} chars to {dest}")


if __name__ == "__main__":
    run()
