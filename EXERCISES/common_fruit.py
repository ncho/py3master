#!/usr/bin/env python

# Exercise 7-3

# Create empty sets
fruit1 = set()
fruit2 = set()

# Open text file and import as object
with open("../DATA/fruit1.txt") as fruit1_in:
    # Add fruits (lines) to set, change fruits that are title-case to lower-case
    # Some of the fruits are in both files, but one is capitalized and the other isn't
    for f in fruit1_in:
        fruit1.add(f.rstrip().lower())

# Do it again
with open("../DATA/fruit2.txt") as fruit2_in:
    for f in fruit2_in:
        fruit2.add(f.rstrip().lower())

# Test
print()
print(fruit1)

# Test
print()
print(fruit2)

# Find the intersection of the sets (common fruits)
common_fruits = fruit1 & fruit2

print()
# Print intersection, with a new line before each fruit
print("\n".join(common_fruits))
