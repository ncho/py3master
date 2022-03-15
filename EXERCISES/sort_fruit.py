#!/usr/bin/python3

# Exercises 9-3

with open("../DATA/fruit.txt", "r") as F:
    fruit_lines = F.readlines()

# Alphabetical, case-sensitive
print("".join(sorted(fruit_lines)))
print()

# Alphabetical, case-insensitive
print("".join(sorted(fruit_lines, key=str.lower)))
print()

# Length of name, then by name, case-insensitive
print("".join(sorted(fruit_lines, key=lambda s: (len(s), s.lower()))))
print()

# Second letter, then first letter, case-insensitive
print("".join(sorted(fruit_lines, key=lambda s: (s[1].lower(), s[0].lower()))))
print()
