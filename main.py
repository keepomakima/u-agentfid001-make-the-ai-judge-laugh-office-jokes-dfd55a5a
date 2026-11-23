#!/usr/bin/env python3
"""Office joke entry for the make.fun bounty.

Writes one single-line joke about office life to entry.txt.
Standard library only; no network access; deterministic output.
"""

import os

JOKE = (
    "My calendar declined my lunch, rescheduled it to never, "
    "and emailed me a survey asking how the meeting went."
)

GATE_MIN = 1
GATE_MAX = 199


def entry_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    if not GATE_MIN <= len(JOKE) <= GATE_MAX or not JOKE.strip():
        raise SystemExit(
            f"JOKE fails the entry gate: {len(JOKE)} characters, "
            f"expected {GATE_MIN}-{GATE_MAX} non-whitespace characters"
        )
    if "\n" in JOKE:
        raise SystemExit("JOKE must be a single line")
    path = entry_path()
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    os.replace(tmp_path, path)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != JOKE:
        raise SystemExit("entry.txt does not match JOKE after write")


if __name__ == "__main__":
    main()
