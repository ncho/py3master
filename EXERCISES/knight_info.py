#!/usr/bin/env python

# Exercise 12-1

# the provided answer was incomplete

import sys

from knight import Knight

import os

DATA_FOLDER = os.getenv("DATADIR", "../DATA")
DATA_FILE = os.path.join(DATA_FOLDER, 'knights.txt')

print()
text_file_knights = ', '.join(sorted(Knight.get_knight_names()))
print("Text file knights: {}".format(text_file_knights))
print()

command_line_knights = ', '.join(sys.argv[1:])
print("Command line knight(s): {}".format(command_line_knights))
print()

# for input_name in sys.argv[1:]:
#     input_name = input_name.title()
#     # Can't this conversion go in the class itself?
#     with open(DATA_FILE) as knights_in:
#         for line in knights_in:
#             if input_name in line:
#                 k = Knight(input_name)
#                 print("Name: {} {}".format(k.title, input_name))
#                 print("Favorite color: {}".format(k.color))
#                 print("Quest: {}".format(k.quest))
#                 print("Comment: {}".format(k.comment))
#                 print()
#             else:
#                 print("Not here")

for input_name in sys.argv[1:]:
    input_name = input_name.title()
    with open(DATA_FILE) as knights_in:
        contents = knights_in.read()
        if input_name in contents:
            k = Knight(input_name)
            print("Name: {} {}".format(k.title, input_name))
            print("Favorite color: {}".format(k.color))
            print("Quest: {}".format(k.quest))
            print("Comment: {}".format(k.comment))
            print()
        else:
            print("{} is not a knight!".format(input_name))
            print()

# right now the script is stopping when it raises an error
# so input like "arthur bob lancelot" is not outputting lancelot's info
# need to figure this out

# the exception is unhandled so execution is stopping

# I need conditional statements that check if the name is in the list

# if the name is not in the list, the class has no defined properties

# eventually I got this to work like how I wanted, meaning the output is correct
# but I feel like this can be better… I feel like there's too much happening in this script
# and more should be happening in the knight.py module
