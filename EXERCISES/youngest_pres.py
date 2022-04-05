#!/usr/bin/python3

# Exercises 15-4

import datetime


def make_date(date_string):
    raw_year, raw_month, raw_day = date_string.split('-')
    year = int(raw_year)
    month = int(raw_month)
    day = int(raw_day)

    return datetime.date(year, month, day)


all_presidents = []

with open("../DATA/presidents.txt") as PRES:
    for rec in PRES:
        _, last_name, first_name, birthday, _, _, _, inauguration_day, *_ = rec.split(":")

        birth_date = make_date(birthday)
        took_office_date = make_date(inauguration_day)

        raw_age_at_inauguration = took_office_date - birth_date
        # outputs the number of days between when the president took office and when they were born
        # this is then divided by 365.25, the number of days in a year
        # age is a number of years
        raw_age_at_inauguration = round(raw_age_at_inauguration.days / 365.25, 1)

        full_name = '{} {}'.format(first_name, last_name)

        all_presidents.append((raw_age_at_inauguration, full_name))

for age, name in sorted(all_presidents):
    print(name, age)
