#!/usr/bin/env python

# Exercise 3-2 (c2f_batch.py)

import sys

celsius = float(sys.argv[1])
fahrenheit = ((9 * celsius) / 5) + 32

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

# You can edit the configuration to run with a parameter
# In this case, an included parameter would be celsius
