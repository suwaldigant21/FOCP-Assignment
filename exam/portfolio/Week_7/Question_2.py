"""2. Write and test three functions that each take two words (strings) as parameters and
 return sorted lists (as defined above) representing respectively:
 Letters that appear in at least one of the two words.
 Letters that appear in both words.
 Letters that appear in either word, but not in both.
 Hint: These could all be done programmatically, but consider carefully what topic we
 have been discussing this week! Each function can be exactly one line."""

def letters_in_at_least_one(string1, string2):
    return sorted(list(set(string1) | set(string2)))

def letters_in_both(string1, string2):
    return sorted(list(set(string1) & set(string2)))

def letters_in_either_but_not_both(string1, string2):
    return sorted(list(set(string1) ^ set(string2)))

string1 = input("Enter the first word: ")
string2 = input("Enter the second word: ")

print(f"Letters that appear in at least one of the two words: {letters_in_at_least_one(string1, string2)}")
print(f"Letters that appear in both words: {letters_in_both(string1, string2)}")
print(f"Letters that appear in either word, but not in both: {letters_in_either_but_not_both(string1, string2)}")