"""3.Write and test a function that determines if a given integer is a prime number. A
 prime number is an integer greater than 1 that cannot be produced by multiplying
 two other integers."""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")