#!/usr/bin/python3

# Exercises 5-4

# The exercise's pseudo code and the answer are different from each other

# Import system package to use commands that interact with the system the program is being run on
import sys

# Specify highest number to check on the script's command line
# A default is supplied if no limit is specified
limit = 101
# Check if a limit is specified on the command line
# `len` checks number of inputs on the command line, not the size of a number
if len(sys.argv) > 1:
    if int(sys.argv[1]) > 1:
        limit = int(sys.argv[1]) + 1
    else:
        print("A number greater than 1 must be entered.\n101 will be used as the limit instead.")

# Initialize list
# List is all Boolean values, set `True` by default
# `True` is not a string
# List is multiplied, replicates elements
# Example: flags = [True] * 3 = [True, True, True]
# Example: if limit = 5, then flags = [True, True, True, True, True]
flags = [True] * limit

print("The following are the prime numbers below {}:".format(limit - 1))

# range(start, stop)
# For every number between 2 and the limit
for num in range(2, limit):
    if flags[num]:
        # Index position is returned as number if value at index is `True` and prime
        print(num, end=' ')
        # If a number is a multiple of another number, it is `False` and non-prime
        for multiple_of_num in range(2 * num, limit, num):
            # `multiple_of_num` is the index position
            # This calculates all the even numbers up to the limit and marks them as non-prime
            flags[multiple_of_num] = False

print()

# range(start, stop , step)

# range (5, 30, 5):
# Start = 5, stop = 30, step = 5 (5 through 25 by 5)

# ---

# Wikipedia pseudocode

# A key thing is the numbers being outputted are index positions, not values

# algorithm Sieve of Eratosthenes is
#   input: an integer n > 1.
#   output: all prime numbers from 2 through n.
#
#   let A be an array of Boolean values, indexed by integers 2 to n,
#   initially all set to true.
#
#   for i = 2, 3, 4, ..., not exceeding √n do
#       if A[i] is true
#           for j = i², i²+i, i²+2i, i²+3i, ..., not exceeding n do
#                A[j] := false

# := can be used to assign variables while another expression is being evaluated.
