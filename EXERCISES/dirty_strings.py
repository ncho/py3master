#!/usr/bin/env python

# Exercise 8-1


def cleanup(s):
    return s.strip().lower()


spam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

# Running into an issue where white spaces aren't being stripped from the last string in the list
# Actually, this is expected behavior `strip` returns a copy of the string with leading and trailing characters removed

for old_string in spam:
    new_string = cleanup(old_string)
    print("Before: >{}<\nAfter: >{}<\n".format(old_string, new_string))
