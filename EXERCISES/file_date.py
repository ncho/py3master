#!/usr/bin/python3

# Exercises 15-1

import sys
import os
from datetime import datetime as DateTime

for filename in sys.argv[1:]:
    mtime = os.path.getmtime(filename)
    file_date = DateTime.fromtimestamp(mtime)
    fmt_date = DateTime.strftime(file_date, '%b %d, %Y')
    print("{0:15s} {1}".format(filename, fmt_date))
    # the `1` is the numeric position of the variable
    # changing it to `0` will use `filename` instead of `fmt_date` there
