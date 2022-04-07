#!/usr/bin/python3

# Exercises 17-3

import pickle
from collections import namedtuple

fields = 'no firstname lastname birthplace state party'
President = namedtuple('President', fields)

with open('potus.pic', 'rb') as POTUS:
    presidents = pickle.load(POTUS)

print("US Presidents:\n")

for p in presidents:
    print("{1}, {0}: {2}".format(p.firstname, p.lastname, p.party))
