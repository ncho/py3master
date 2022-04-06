#!/usr/bin/env python

# Exercise 16-4

import os
import shutil

print(os.getcwd())
# get current working directory
files_to_copy = [f for f in os.listdir('../DATA') if f.endswith('.csv')]

for files_to_copy in files_to_copy:
    files_path_to_copy = os.path.join('../DATA', files_to_copy)
    shutil.copy(files_path_to_copy, '../TEMP')
