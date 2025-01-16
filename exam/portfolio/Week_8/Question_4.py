"""4. The Unix wc command counts the number of lines, words, and characters in a file.
 Write an implementation of this that takes a file name as a command-line
 argument, and then prints the number of lines and characters.
 Note: Linux (and Mac) users can use the "wc" command to check the results of their
 implementation."""

import sys

if len(sys.argv) != 2:
    print("Usage: python Question_4.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = f.readlines()
    print(f"{len(lines)} lines")
    print(f"{sum(len(line) for line in lines)} characters")