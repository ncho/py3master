#!/usr/bin/env python

# Exercise 11-4

from temp_conv import c2f

while True:
    temp_str = input('Enter Celsiuis temp (type \'q\' to quit): ')
    if temp_str.lower().startswith('q'):
        print("Bye bye")
        break
    if temp_str.lstrip("-").isdigit():
        celsius = float(temp_str)
        fahrenheit = c2f(celsius)
        print('{:.1f} C is {:.1f} F\n'.format(celsius, fahrenheit))
    else:
        print("Please enter a number")
