#!/usr/bin/env python

# Exercise 3-1 (c2f.py)
# Test script with the following values: 100, 0, 47, -40

temp_str = input("Enter Celsius temp: ")
celsius = float(temp_str)
fahrenheit = ((9 * celsius) / 5) + 32

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))