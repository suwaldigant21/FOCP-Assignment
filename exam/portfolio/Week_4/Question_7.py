"""7. Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean."""

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def remove(string):
    if len(string) <= 1:
        return string
    return string[:-1]

print("\n\t\t\t\t\t\"Please it is compulsory to add the letter 'C' after the temperature value.\"")
temperatures = []
for i in range(6):
    temperature = input(f"Enter temperature {i + 1} in degrees Celsius: ")
    if temperature[-1].upper() == 'C':
        celsius = float(remove(temperature))
        temperatures.append(celsius)
    else:
        print("Error: The input must end with the letter 'C'.")
        break

if len(temperatures) == 6:
    max_temperature = max(temperatures)
    min_temperature = min(temperatures)
    mean_temperature = sum(temperatures) / len(temperatures)

    print(f"The maximum temperature is {max_temperature} degrees Celsius.")
    print(f"The minimum temperature is {min_temperature} degrees Celsius.")
    print(f"The mean temperature is {mean_temperature} degrees Celsius.")