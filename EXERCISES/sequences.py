#!/usr/bin/python3

# Exercises 5-2 and 5-3

# Exercise 5-2

ctemps = [-40, 0, 37, 75, 100]

print()

for c in ctemps:
    f = ((9 * c) / 5) + 32
    print("{:.1f} C is {:.1f} F".format(c, f))
    print()

print("-" * 60)
print()

# Exercise 5-3

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

print(fruits)

print()

clean_fruits = [f.strip().lower() for f in fruits]

print(', '.join(clean_fruits))

print()

p_fruits = [fruit.title() for fruit in clean_fruits if fruit.startswith('p')]
print("Perfect Fruits:", ' '.join(p_fruits))
