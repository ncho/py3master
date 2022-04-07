#!/usr/bin/python3

# Exercises 18-2

import requests

URL = "https://www.wikipedia.org"

response = requests.get(URL)

if response.status_code == requests.codes.OK:
    link_count = 0
    page_content = response.content.decode()  # convert from bytes to string

    start = 0
    while True:
        pos = page_content.find('href', start)
        if pos == -1:  # no more strings
            # Python programming language supports negative indexing of arrays
            # this means that the index value of -1 gives the last element
            # and -2 gives the second last element of an array
            # the negative indexing starts from where the array ends
            break
        start = pos + 1
        link_count += 1

print("There are {} links on the Wikipedia main page".format(link_count))
