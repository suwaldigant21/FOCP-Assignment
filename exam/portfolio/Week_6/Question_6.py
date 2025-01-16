"""6. Write a program that decrypts messages encoded as above."""

def decrypt(encrypted_message, interval):
    decrypted_message = ""
    i = 0  

    while i < len(encrypted_message):
        char = encrypted_message[i]
        decrypted_message += char  
        if char == " ":
            i += 1  
        else:
            i += interval  
    
    return decrypted_message

encrypted_message = input("Enter the encrypted message: ")
interval = int(input("Enter the interval used: "))

decrypted_message = decrypt(encrypted_message, interval)

print(f"Decrypted message: {decrypted_message}")