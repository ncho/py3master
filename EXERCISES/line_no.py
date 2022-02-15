#!/usr/bin/env python

# Exercise 6-1

print()

import sys

for file_name in sys.argv[1:]:
    with open(file_name) as file_in:
        for i, line in enumerate(file_in, 1):
            print("{:4d}: {}".format(i, line), end='')
    print()

# Finding it easier to test these in Terminal panel instead of Run panel in PyCharm
