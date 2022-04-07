#!/usr/bin/python3

# Exercises 17-2

import csv
import pickle
from collections import namedtuple

fields = 'no firstname lastname birthplace state party'
President = namedtuple('President', fields)

presidents = []
with open('../DATA/potus.csv', newline='') as presidents_in:
    reader = csv.reader(presidents_in, delimiter=',')
    for row in reader:
        president = President(*row)
        presidents.append(president)
        print(president)

print()
print(presidents)
print()

p = presidents[15]
print(p.firstname, p.lastname, p.party)

with open('potus.pic', 'wb') as POTUS:
    pickle.dump(presidents, POTUS)

# I got this to work
# the hardest parts were understanding how the CSV was being read in
# and then how to use that input to create a named tuple

# ------------------------

# the provided answer doesn't work
# I'm pretty sure it's because it isn't correctly set up to read CSVs
# when I change the script to read presidents.txt, the script works

# President = namedtuple('President', 'no lastname firstname birthday deathday birthplace state firstday lastday  party')

# presidents = []
# with open('../DATA/presidents.txt') as presidents_in:
#     for raw_line in presidents_in:
#         line = raw_line.rstrip()
#         fields = line.split(':')
#         president = President(*fields)
#         presidents.append(president)
#
# print(presidents)
#
# p = presidents[15]
# print(p.firstname, p.lastname, p.party)
#
# with open('potus.pic','wb') as POTUS:
#     pickle.dump(presidents,POTUS)
#

# ------------------------

# just testing some stuff out

# for president in map(President._make, csv.reader(open("../DATA/potus/presidents.csv"))):
#     print(president.firstname, president.lastname)
#
# p = President(1, firstname="Lucas", lastname="Cho", birthplace="Hospital", birthstate="California", party="AWESOME")
#
# print(p)
# print(p.firstname)
#
