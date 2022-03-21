#!/usr/bin/python3

# Exercises 13-3

import re

# copy .dat file to .txt file
# I wanted to know what's in the .dat file

with open('../DATA/custinfo.dat') as custinfo_in:
    with open('custinfo.txt', 'w') as custinfo_out:
        for line in custinfo_in:
            custinfo_out.write(line + '\n')

num = re.compile(r"\b\d{3}-\d{4}\b")

with open('../DATA/custinfo.dat') as f:
    for line in f:
        if num.search(line):
            print(line, end='')
