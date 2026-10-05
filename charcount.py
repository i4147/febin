#!/data/data/com.termux/files/usr/bin/python
"""Print the character count and byte size of a single text file.

Usage::

    charcount.py <input_file>

The file is skipped silently (exit status ``0``) when it is a symbolic link
or is detected as binary, so the script is safe to point at arbitrary paths.
"""

import sys
from pathlib import Path

from dh import is_binary

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_chars_of_input_file.py <input_file>")
        sys.exit(1)

    path: Path = Path(sys.argv[1])

    if path.is_symlink() or is_binary(path):
        sys.exit(0)

    char_count: int = len(path.read_text(encoding="utf-8"))
    print(f"char : {char_count}\nsize : {path.stat().st_size}")
