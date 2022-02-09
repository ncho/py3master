#!/usr/bin/env python

# Exercise 3-3 (string_fun.py)

# Run the program, and enter "john jacob jingleheimer schmidt"

full_name = input("Enter a full name: ")

print("name: ", full_name)
print("upper: ", full_name.upper())
print("title: ", full_name.title())

j_count = full_name.lower().count('j')
print("j count: ", j_count)

print("len:", len(full_name))

print("position of 'jacob':", full_name.index('jacob'))

# This only works if 'jacob' is in the full name
# The program returns an error if the inputted full name doesn't contain 'jacob'