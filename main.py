"""Fridge Roast: One Line, Biggest Laugh.

Writes a single original roast of a smart fridge to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output`` when unset).

The line is validated before writing: it must be 1-200 characters,
valid UTF-8, and not only whitespace. After writing, the file is
read back and compared byte-for-byte against the expected content
(a round-trip check).
"""

import os
import sys

ROAST = (
    "My smart fridge updated its firmware at 2 a.m., bricked the ice "
    "maker, and emailed me a photo of my leftovers with the subject "
    "line: 'We need to talk.'"
)

MAX_CHARS = 200


def validate(line: str) -> bytes:
    """Validate the roast and return it as UTF-8 bytes."""
    if not line or not line.strip():
        raise ValueError("roast line is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"roast line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    try:
        return line.encode("utf-8")
    except UnicodeEncodeError as exc:  # pragma: no cover - line is ASCII
        raise ValueError(f"roast line is not valid UTF-8: {exc}") from exc


def main() -> int:
    data = validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as fh:
        fh.write(data)
        fh.write(b"\n")
    # Round-trip check: what landed on disk must match exactly, both as
    # bytes and as a decoded string, and the on-disk line must still be
    # within the character limit (trailing newline excluded).
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data + b"\n":
        raise RuntimeError("round-trip check failed: entry.txt differs")
    decoded = written.decode("utf-8")
    if decoded != ROAST + "\n":
        raise RuntimeError("round-trip check failed: decoded text differs")
    if len(decoded.rstrip("\n")) > MAX_CHARS:
        raise RuntimeError("round-trip check failed: on-disk line too long")
    print(f"wrote {len(data)} bytes to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
