#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 21:39:34 2013

"""
import os
import shutil

print(os.getcwd())
files_to_copy = [f for f in os.listdir('../DATA') if f.endswith('.csv')]

for file_to_copy in files_to_copy:
    file_path_to_copy = os.path.join('../DATA', file_to_copy)
    shutil.copy(file_path_to_copy, '../TEMP')
