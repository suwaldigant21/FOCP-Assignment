"""6. Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format."""

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def remove(string):
    if len(string) <= 1:
        return string
    return string[:-1]

print("\n\t\t\t\t\t\"Please it is compulsory to add the letter 'C' after the temperature value.\"")
temperature = input("Enter a temperature in degrees Celsius: ")
if temperature[-1].upper() == 'C':
    celsius = float(remove(temperature))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is equivalent to {fahrenheit} degrees Fahrenheit.")
else:
    print("Error: The input must end with the letter 'C'.")