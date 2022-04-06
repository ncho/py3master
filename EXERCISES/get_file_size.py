#!/usr/bin/env python

# Exercise 16-2

import sys
import os.path

for file in sys.argv[1:]:
    if os.path.isdir(file):
        print("{} is a directory".format(file))
        continue
    else:
        print(file, os.path.getsize(file))
