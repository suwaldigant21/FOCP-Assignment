"""1.Write a function that accepts a positive integer as a parameter and then returns a
 representation of that number in binary (base 2).
 Hint: This is in many ways a trick question. Think!"""

def binary(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return binary(num // 2) + str(num % 2)

num = int(input("Enter a number: "))
print(binary(num))