#!/usr/bin/python3

# Exercises 15-3

from datetime import date as Date
import calendar

test_dates = (
    (1991, 6, 3),
    (1991, 7, 18),
    (2021, 5, 3),
)

for year, month, day in test_dates:
    dt = Date(year, month, day)
    wday = calendar.weekday(year, month, day)
    # `wday` is a number between 0 and 6
    # the weekday that the date falls on
    wday_name = calendar.day_name[wday]
    is_leapyear = calendar.isleap(year)
    print('{} {:10s} {}'.format(dt, wday_name, is_leapyear))
