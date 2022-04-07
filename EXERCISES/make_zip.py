#!/usr/bin/python3

# Exercises 17-4

import zipfile

zfile = zipfile.ZipFile('potus.zip', 'w')
zfile.write('save_potus_info.py')
zfile.write('read_potus_info.py')
zfile.write('potus.pic')
zfile.close()
