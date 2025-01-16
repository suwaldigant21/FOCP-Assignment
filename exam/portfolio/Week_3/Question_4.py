"""4.Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""

password = input("Enter a new password: ")
password1 = input("Enter the password again: ")

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

if password in BAD_PASSWORDS:
    print("Error: The password is not set. It is a bad password.")
else:
    if len(password) >= 8 and len(password) <= 12:
        if password == password1:
            print("Password Set")
        else:
            print("Error: Passwords does not match.The password is not set.")    
    else:
        print("Error: Password must be between 8 and 12 characters long.")