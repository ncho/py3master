#!/usr/bin/python3

# Exercises 9-4

# sample data:
# 1:Washington:George:1732-02-22:1799-12-14:Westmoreland County:Virginia:1789-04-30:1797-03-04:no party

# list to hold all presidents (will be list of lists)
all_pres = []

with open("../DATA/presidents.txt", "r") as PRES:

    for line in PRES:
        fields = line.rstrip('\n\r').split(":")
        all_pres.append(fields) # add list of fields

print(all_pres)

# sort by lname, fname
for fields in sorted(all_pres, key=lambda e: (e[1], e[2])):
    print(fields[2], fields[1], fields[6])

# you can see the sorting happen clearly with the Bushes and the Roosevelts
