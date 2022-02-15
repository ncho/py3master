#!/usr/bin/env python

# Exercise 6-2

with open("../DATA/alt.txt") as alt_in:
    with open("a.txt", "w") as a_out:
        # "w" open for writing in text mode
        with open("b.txt", "w") as b_out:
            for line in alt_in:
                if line.startswith('a'):
                    a_out.write(line)
                elif line.startswith('b'):
                    b_out.write(line)

# Wow, this is so powerful…
