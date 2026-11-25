#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes one original joke about Monday mornings to /output/entry.txt.
No network, no dependencies, deterministic output.
"""

import os

JOKE = (
    "Monday walked in wearing a suit, introduced itself as the new boss, "
    "and HR still hasn't corrected it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
