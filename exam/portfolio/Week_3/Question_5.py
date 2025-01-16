"""5. Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time"""

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password = input("Enter a new password: ")
    password1 = input("Enter the password again: ")

    if password in BAD_PASSWORDS:
        print("Error: The password is not set. It is a bad password.")
    else:
        if len(password) >= 8 and len(password) <= 12:
            if password == password1:
                print("Password Set")
                break
            else:
                print("Error: Passwords do not match. The password is not set.")    
        else:
            print("Error: Password must be between 8 and 12 characters long.")