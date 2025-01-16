"""2.The Unix diff command compares two files and reports the differences, if any.
 Write a simple implementation of this that takes two file names as command-line
 arguments and reports whether or not the two files are the same. (Define "same" as
 having the same contents.)"""

import sys

if len(sys.argv) != 3:
    print("Usage: python Question_2.py <file1> <file2>")
    sys.exit(1)

try:
    with open(sys.argv[1], "r") as f1, open(sys.argv[2], "r") as f2:
        if f1.read() == f2.read():
            print("The files are the same.")
        else:
            print("The files are different.")
except FileNotFoundError as e:
    print(f"Error: {e}")