"""2.Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program"""

def letters(string):
    uppercase = 0
    lowercase = 0
    for char in string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
    return uppercase, lowercase

string = input("Enter a string: ")
uppercase, lowercase = letters(string)
print(f"There are {uppercase} uppercase letters and {lowercase} lowercase letters in the string.")
