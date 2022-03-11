#!/usr/bin/env python

# Exercise 8-2

def c2f(celsius):
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32

    return fahrenheit

# PyCharm suggests I add two new lines after a function definition


print()
print("Here are some common conversions:\n")

f = c2f(100)
print("100.0 C is {} F".format(f))

f = c2f(0)
print("0.0 C is {} F".format(f))

f = c2f(37)
print("37.0 C is {} F".format(f))

f = c2f(-40)
print("-40.0 C is {} F".format(f))

print()
print("Now go crazy!")

while True:
    raw_celsius = input('Enter Celsius temp: ')
    if raw_celsius.lower().startswith('q'):
        print("Bye")
        break
    if raw_celsius.lstrip("-").isdigit():
        c = float(raw_celsius)
        f = c2f(c)
        print('{:.1f} C is {:.1f} F\n'.format(c, f))
    else:
        print("Enter a number or `q` to quit")

# Need to accept negative C temperatures
# Can do so by stripping "-" when checking if input is digit
