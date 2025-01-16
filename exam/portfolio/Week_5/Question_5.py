"""5. Last week you wrote a program that processed a collection of temperature readings
 entered by the user and displayed the maximum, minimum, and mean. Create a
 version of that program that takes the values from the command-line instead. Be
 sure to handle the case where no arguments are provided !"""

import sys

if len(sys.argv) > 1:
    temperatures = [float(arg) for arg in sys.argv[1:]]
    max_temperature = max(temperatures)
    min_temperature = min(temperatures)
    mean_temperature = sum(temperatures) / len(temperatures)

    print(f"The maximum temperature is {max_temperature} degrees Celsius.")
    print(f"The minimum temperature is {min_temperature} degrees Celsius.")
    print(f"The mean temperature is {mean_temperature} degrees Celsius.")
else:
    print("Error: No temperature values provided.")