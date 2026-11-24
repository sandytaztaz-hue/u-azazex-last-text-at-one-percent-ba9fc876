#!/usr/bin/env python3
"""Last Text at One Percent — the last text a phone sends at 1% battery."""

import os

ENTRY = "1% left. Confession: I was never at 2%. I lied for an hour. I just wanted attention."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
