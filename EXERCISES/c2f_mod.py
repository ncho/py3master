#!/usr/bin/env python

# Exercise 11-2

from temp_conv import c2f as test_name

temp_str = input("Enter Celsius temp: ")
celsius = float(temp_str)
fahrenheit = test_name(celsius)

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))
