#!/usr/bin/env python

# Exercise 4-1 (c2f_loop.py)

while True:
    celsius = input('Enter Celsiuis temp (type \'q\' to quit): ')
    if celsius.lower().startswith('q'):
        print("Bye bye")
        break
    # elif celsius.startswith(""):
    #    print("Huh? Please enter a temp")
    #    continue
    if celsius.isdigit():
        celsius = float(celsius)
        fahrenheit = ((9* celsius) / 5) + 32
        print('{:.1f} C is {:1f} F\n'.format(celsius, fahrenheit))
    else:
        print("Please enter a number")
