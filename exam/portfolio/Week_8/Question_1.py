"""1.  The Unix nl command prints the lines of a text file with a line number at the start
 of each line. (It can be useful when printing out programs for dry runs or white-box
 testing). Write an implementation of this command. It should take the name of the
 files as a command-line argument."""

import sys

if len(sys.argv) != 2:
    print("Usage: python Question_1.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as f:
        for i, line in enumerate(f, 1):
            print(f"{i} {line}", end="")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")