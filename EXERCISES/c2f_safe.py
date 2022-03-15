#!/usr/bin/python3

# Exercises 10-1

import sys

try:
    celsius = float(input("Enter Celsius temp: "))
# except ValueError as e:
#     print("Error!", e)
#     sys.exit(1)
except Exception as e:
    print("Uh oh! ", e)
    sys.exit(1)

fahrenheit = ((9 * celsius) / 5  + 32)

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))
