"""8.Modify the previous program so that it can process any number of values. The input
terminates when the user just presses "Enter" at the prompt rather than entering a
value."""

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("\n\t\t\t\t\t\"Please it is compulsory to add the letter 'C' after the temperature value.\"")
temperatures = []
while True:
    temperature = input("Enter a temperature in degrees Celsius: ")
    if temperature == "":
        break
    if temperature[-1].upper() == 'C':
        celsius = float(temperature[:-1])
        temperatures.append(celsius)
    else:
        print("Error: The input must end with the letter 'C'.")

if temperatures:
    max_temperature = max(temperatures)
    min_temperature = min(temperatures)
    mean_temperature = sum(temperatures) / len(temperatures)

    print(f"The maximum temperature is {max_temperature} degrees Celsius.")
    print(f"The minimum temperature is {min_temperature} degrees Celsius.")
    print(f"The mean temperature is {mean_temperature} degrees Celsius.")
else:
    print("No valid temperatures were entered.")