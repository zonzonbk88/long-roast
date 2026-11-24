#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt.
Standard library only.
"""

import os

LINE = (
    "They just passed a law telling artificial intelligence what it may "
    "and may not think, yet the bill itself is still a Word file called "
    "final_FINAL_v3 because no one in the building can find Export to PDF."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
