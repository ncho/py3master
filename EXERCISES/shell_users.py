#!/usr/bin/env python

# Exercise 7-2

# I don't really know what's happening in this exercise…
# I'm missing something fundamental…

# "Shells are command line interpreters
# which, put simply, means they take your commands
# and give them to the operating system to put into action."

users_by_shell = {}
counter = 9

# Does "passwd" really mean "password"?? I don't know
with open("../DATA/passwd") as passwd_in:
    for line in passwd_in:
        shell = line.rstrip().split(":")[-1]
        # or
        # *_, shell = line.rstrip().split(":")
        # I think the above line that uses `*_` fast-forwards to the end of the line, but I'm not sure
        # `*_` is a dummy argument?
        if shell == "":
            shell = "NONE"
        if shell in users_by_shell:
            users_by_shell[shell] = users_by_shell[shell] + 1
            counter += 1
        else:
            users_by_shell[shell] = 1

print(counter)
print()

for shell, count in users_by_shell.items():
    print("{:5d} {}".format(count, shell))

print()
print("Number of shells:", len(users_by_shell))

print()
print(1 + 31 + 1 + 1 + 13 + 15 + 8 + 1 + 9)
