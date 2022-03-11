#!/usr/bin/env python

# Exercise 8-3

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


while True:
    expr = input("Enter a math expression: ")

    # Quit the program
    if expr.lower() == 'q':
        break

    # Check if input is valid
    try:
        v1, op, v2 = expr.split()
        val = int(v1)
    except ValueError:
        print("That's not a valid math expression")
        continue

    # Input string is already split, now convert numbers in string into floating-point numbers
    v1 = float(v1)
    v2 = float(v2)

    # Run operation function based on operator in input
    if op == '+':
        result = add(v1, v2)
    elif op == '-':
        result = sub(v1, v2)
    elif op == '*':
        result = mul(v1, v2)
    elif op == '/':
        result = div(v1, v2)
    else:
        print("Bad operator!")
        continue

    print("{:.3f}".format(result))
