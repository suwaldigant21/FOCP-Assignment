"""1. Write and test a function that takes a string as a parameter and returns a sorted list
 of all the unique letters used in the string. So, if the string is cheese, the list
 returned should be ['c', 'e', 'h', 's']."""

def unique_letters(string):
    unique_letters = []
    for char in string:
        if char not in unique_letters:
            unique_letters.append(char)
    return sorted(unique_letters)

string = input("Enter a string: ")
print(unique_letters(string))