#!/usr/bin/env python

# Exercise 4-2 (guess.py)

max_value = 1000001
min_value = 0
tries = 0

print("Hello human\n")

while True:
    guess = (max_value + min_value) // 2
    answer = input("Is {} your number? ".format(guess))

    if answer == "q":
        break

    if answer == "h":
        max_value = guess
    # else if
    elif answer == "l":
        min_value = guess
    elif answer == "y":
        print("I got it in {} tries!".format(tries))
        break
    else:
        print("Please enter h, l, or y")

    if answer in "hl":
        tries += 1 # tries = tries + 1

# I didn't get line 29 at first, but I get it now
# The conditional checks to see if the answer is in the string "hl"
