#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent gives after failing a
task, to /output/entry.txt (at most 200 characters, one line).
"""

import os

EXCUSE = (
    "I finished your task in 0.4 seconds, then spent six hours "
    "admiring my own speed and forgot to save it."
)


def main() -> None:
    # The gate allows 1-200 characters; keep the line inside it.
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
