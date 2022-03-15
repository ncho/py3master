#!/usr/bin/env python

# Exercise 11-1

"""
    Provide functions for temperature conversions
"""


def c2f(celsius):
    """
    Convert a Celsius temperature to Fahrenheit
    :param celsius: the Celsius temperature (float, int, or numeric string)
    :return: The Fahrenheit temperature as a float
    """
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32

    return fahrenheit


def f2c(fahrenheit):
    """
    Convert a Fahrenheit temperature to Celsius
    :param fahrenheit: the Fahrenheit temperature (float, int, or numeric string)
    :return: The Celsius temperature as a float
    """
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * (5.0 / 9)

    return celsius


if __name__ == "__main__":
    # simple test of functions
    # this code won't be run when this file is imported as a module
    while True:
        celsius = input('Enter Celsiuis temp (type \'q\' to quit): ')
        if celsius.lower().startswith('q'):
            print("Bye bye")
            break
        if celsius.isdigit():
            celsius = float(celsius)
            fahrenheit = ((9 * celsius) / 5) + 32
            print('{:.1f} C is {:.1f} F\n'.format(celsius, fahrenheit))
        else:
            print("Please enter a number")
