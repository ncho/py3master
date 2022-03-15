#!/usr/bin/python3

# Exercises 9-1

scores = {}
# `{}` is a dictionary object
total_of_scores = 0

with open("../DATA/testscores.dat") as f:
    for line in f:
        (name, score) = line.split(":")
        score = int(score)
        scores[name] = score
        # Adding items to dictionary
        total_of_scores += score
        # Adding scores together so average can be calculated later

for student, score in sorted(scores.items(), key=lambda e: (e[1]), reverse=True):
    grade = None
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
    print("{:<20s} {:2d} {}".format(student, score, grade))

average = total_of_scores / len(scores)
print("\nAverage score is  {:.2f}\n".format(average))
