#!/usr/bin/env python

# Exercise 7-1

# Notes

# ---

# d1 = dict()
#
# airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma', 'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}
#
# d2 = {}
# d3 = dict(red=5, blue=10, yellow=1, brown=5, black=12)
#
# pairs = [('Washington', 'Olympia'), ('Virgina', 'Richmond'), ('Oregon', 'Salem'), ('California', 'Sacramento')]
#
# state_caps = dict(pairs)
#
# print(d3['red'])
# print(airports['LAX'])
#
# airports['SLC'] = 'Salt Lake City'
# airports['LAX'] = 'Dodgers Nation'
#
# print(airports['SLC'])
# print(airports['LAX'])
#
# key = 'PSP'
# if key in airports:
#     print(airports[key])
#
# print(airports.get(key))
# # 'PSP' is not in the dictionary
# print(airports.get('IAD'))
# print(airports.get(key, 'NO SUCH AIRPORT'))
#
# print(airports.setdefault(key, 'Palm Springs'))
#
# print(key in airports)
# print(airports.get(key))

# ---

# airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma', 'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}
#
# for abbr, airport in airports.items():
#     print(abbr, airport)

# ---

# from pprint import pprint
#
# knight_info = {}
#
# with open("../DATA/knights.txt") as knight_in:
#     for line in knight_in:
#         (name, title, color, quest, comment) = line.rstrip('\n\r').split(":")
#         knight_info[name] = title, color, quest, comment
#
# pprint(knight_info)
# print()
#
# for name, info in knight_info.items():
#     print(info[0], name)
#
# print()
# print(knight_info['Robin'][2])

#  ---

# from collections import namedtuple
#
# # Declaring namedtuple()
# knight = namedtuple('knight', 'title color quest comment')
#
# knight_info = {}
# with open('../DATA/knights.txt') as knights_in:
#     for line in knights_in:
#         (knight_name, title, color, quest, comment) = line.rstrip('\n\r').split(":")
#         # Adding values
#         knight_info[knight_name] = knight(title, color, quest, comment)
#     # Test
#     for knight_name, info in knight_info.items():
#         print(info[0], knight_name)
#
# print()
# for knight_name, knight in knight_info.items():
#     print(knight.title, knight_name)
#     # Test
#     print(knight[0], knight_name)
#     print()
#
# print()
# print('Arthur' in knight_info)
#
# key = 'Test'
# print()
# print(knight_info.get(key))

#  ---

# Create empty dict
scores_by_student = {}
sum_of_scores = 0.0

# Open and import data file as an object
with open("../DATA/testscores.dat") as scores_in:

    for line in scores_in:
        (name, score) = line.split(":")
        # Convert `score` to integer from string
        score = int(score)
        # Add to dict, where name is key and score is value
        scores_by_student[name] = score
        # Add to sum of scores so average can be calculated later
        sum_of_scores += score

count = 0

# Numbers are sorted in ascending order by default, this can be reversed
# The dict is being sorted alphabetically using the key, student name
for student, score in sorted(scores_by_student.items()):

    count += 1
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'

    # Using `{:20s}` helps format output into even columns
    print("Student {:02d}: {:20s} {} {}".format(count, student, score, grade))

# Looks like `len` returns
average = sum_of_scores/len(scores_by_student)
# `\n` creates a new line
print("\naverage score is {:.2f}\n".format(average))

print(len(scores_by_student))
