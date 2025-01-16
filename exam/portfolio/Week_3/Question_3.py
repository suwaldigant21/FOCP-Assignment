"""3.Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long."""

password = input("Enter a new password: ")
password1 = input("Enter the password again: ")

if len(password) >= 8 and len(password) <= 12:
    if password == password1:
        print("Password Set")
    else:
        print("Error: Passwords does not match.The password is not set.")    
else:
    print("Error: Password must be between 8 and 12 characters long.")