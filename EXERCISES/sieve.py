#!/usr/bin/python3

# Exercises 5-4

# Import system package to use commands that interact with the system the program is being run on
import sys

# The highest number to check
# 101 is the default if no limit is specified on the command line or if the specified limit is ≤1
limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

# Initialize list
flags = [True] * limit

# range(start, stop)
for num in range(2, limit):
    if flags[num]:
        print(num, end=' ')
        for multiple_of_num in range(2 * num, limit, num):
            flags[multiple_of_num] = False

# range(start, stop , step)

# range (5, 30, 5):
# Start = 5, stop = 30, step = 5 (5 through 25 by 5)
