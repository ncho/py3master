#!/usr/bin/env python
import os
from datetime import datetime


def format_time(time_stamp):
    """convert time stamp to YYYY-MM-DD HH:MM string"""
    date_time = datetime.fromtimestamp(time_stamp)  # <1>
    time_string = date_time.strftime('%Y-%m-%d %H:%M')  # <2>

    return time_string


filenames = (  # <3>
    '../DATA/alice.txt',
    '../ANSWERS/sieve.py',
    'file_attrib.py',
)

for filename in filenames:
    size = os.path.getsize(filename)  # <4>
    mtime_ts = os.path.getmtime(filename)  # <5>
    mtime = format_time(mtime_ts)

    atime_ts = os.path.getatime(filename)  # <6>
    atime = format_time(atime_ts)

    print('{0:20s} {1:8d}  {2}  {3}'.format(filename, size, mtime, atime))
