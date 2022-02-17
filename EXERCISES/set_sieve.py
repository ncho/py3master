#!/usr/bin/env python

# Exercise 7-4

# Sets are useful when you want to keep track of a group of values,
# but there's no particular value associated with them.

# Import system package to use commands that interact with the system the program is being run on
import sys

# Checks to see if a limit is defined
# Otherwise the default limit is 101
if len(sys.argv) == 2:
    limit = int(sys.argv[1])
else:
    limit = 101

# Create set
flags = set()

print(2, end=' ')  # 2 is prime and does not need to be tested
# range(start, stop, step)
for num in range(3, limit, 2):  # Only test odd numbers, because all even numbers are non-prime
    if num not in flags:
        print(num, end=' ')
        # Steps are being used to determine if a number is a multiple and thus non-prime
        # For example, using 3 as the step will identify all numbers up to the limit that are divisible by 3
        for x in range(num, limit, num):
            flags.add(x)

# This is a little different from sieve.py
# The `if` conditional does the opposite of what it did before
