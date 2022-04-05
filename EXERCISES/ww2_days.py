#!/usr/bin/python3

# Exercises 15-2

from datetime import date as Date

ww2_start = Date(1941, 12, 7)
ww2_end = Date(1945, 8, 15)

elapsed_time = ww2_end - ww2_start

print("World War II lasted {:,} days".format(elapsed_time.days))
# adding `:,` includes commas in the output
