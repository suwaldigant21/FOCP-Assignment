"""2.Write and test a function that takes an integer as its parameter and returns the
 factors of that integer. (A factor is an integer which can be multiplied by another to
 yield the original)."""

def factors(num):
    factor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list

num = int(input("Enter a number: "))
print(factors(num))