"""5.The Unix spell command is a simple spell-checker. It prints out all the words in a
 text file that are not found in a dictionary. Write and test an implementation of this,
 that takes a file name as a command-line argument.
 Note: You may want to simplify the program at first by testing with a text file that
 does not contain any punctuation. A complete version should obviously be able to
 handle normal files, with punctuation.
 Another Note: You will need a list of valid words. Linux users will already have one
 (probably in /usr/share/dict/words). It is more complicated, as usual, for
 Windows users. Happily, there are several available on GitHub."""

import sys
import string

if len(sys.argv) != 2:
    print("Usage: python Question5.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Load the dictionary words into a set for efficient lookup
with open("/usr/share/dict/words", "r") as dict_file:
    dictionary = set(word.strip().lower() for word in dict_file)

# Function to clean and split words
def clean_word(word):
    return word.strip(string.punctuation).lower()

# Check the words in the file
with open(filename, "r") as f:
    for line in f:
        for word in line.split():
            cleaned_word = clean_word(word)
            if cleaned_word and cleaned_word not in dictionary:
                print(cleaned_word)