#!/usr/bin/env python

# Exercises 19-1

import os
import sys
import shutil
import logging
from glob import glob

if sys.platform == 'win32':
    DEST = r'\TEMP'  # `r` means the string will be treated as a raw string
else:
    DEST = '/tmp'

logging.basicConfig(
    filename='../TEMP/copying.log',
    level=logging.INFO,
)

# for dir_path, dir_list, file_list in os.walk('../DATA'):
#     for file_name in file_list:
#         if file_name.endswith('.txt'):
#             full_name = os.path.join(dir_path, file_name)
#             message = 'copying {} to {}'.format(full_name, DEST)
#             print(message)
#             logging.info(message)
#             shutil.copy(full_name, DEST)

files = glob('../DATA/*.txt')
for file_name in files:
    message = 'copying {} to {}'.format(file_name, DEST)
    print(message)
    logging.info(message)
    shutil.copy(file_name, DEST)

# updated the script in ANSWERS to use the `glob` function
