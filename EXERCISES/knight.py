#!/usr/bin/env python

# Exercise 12-1

# Create a module which defines a class named **Knight**
# Initializer for the class should expect the knight's name as a parameter
# Get the information from the file knights.txt to initialize the object
# The object should have read-only properties

import os

DATA_FOLDER = os.getenv("DATADIR", "../DATA")
# don't know what `os.getenv` does, need to learn what an environment variable key is
DATA_FILE = os.path.join(DATA_FOLDER, 'knights.txt')


class UnknownKnightError(Exception):
    pass


# default base class is object
class Knight(object):

    # constructor
    def __init__(self, name):
        # instance object
        # private methods are called by other methods in the class
        # not visible to users of the class
        # conventionally named with leading underscore
        self._name = name
        # initializer expects knight's name as parameter
        with open(DATA_FILE) as knights_in:
            for line in knights_in:
                (name, title, color, quest, cmt) = line.rstrip('\n\r').split(":")
                # looking for name in text file
                # if the name in the file is exactly the same as the name in the input
                # the `name` object's value is updated in this loop based on the text file
                # but the instance object's value is not updated here
                # so `self._name` can be used to check lines in the text file
                if name == self._name:
                    # create instance objects
                    self._title = title
                    self._color = color
                    self._quest = quest
                    self._comment = cmt
                    break
            else:
                raise UnknownKnightError("No such knight as '" + self._name + "'")
            # if there are multiple inputs, that looping occurs where the class is called and not here

    @classmethod
    def get_knight_names(cls):
        # is this class method even being used?
        with open(DATA_FILE) as knights_in:
            return [line.split(':')[0] for line in knights_in]

    # these properties can be used when the class is used
    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    @property
    def color(self):
        return self._color

    @property
    def quest(self):
        return self._quest

    @property
    def comment(self):
        return self._comment


if __name__ == "__main__":
    k = Knight("Arthur")
    print(k.title, k.name, k.color, k.comment)
    try:
        k2 = Knight("Bob")
    except UnknownKnightError as err:
        print(err)
