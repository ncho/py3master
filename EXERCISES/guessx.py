#!/usr/bin/env python

# Exercise 4-3 (guessx.py)

import sys

max_value = 26
if len(sys.argv) > 1:
    max_value = int(sys.argv[1]) + 1

min_value = 0
tries = 0

while True:
    guess = (max_value + min_value) // 2
    answer = input("Is {} your number? ".format(guess))

    if answer == "q":
        break

    tries = tries + 1
    # Can I use tries += 1 here?

    if answer == "h":
        max_value = guess
    elif answer == "l":
        min_value = guess
    elif answer == "y":
        if tries == 1:
            print("I got it in {} try!".format(tries))
            break
        else:
            print("I got it in {} tries!".format(tries))
            break
    else:
        print("Please enter h, l, or y")
