#!/usr/bin/python3

# Exercises 18-1

import os
import sys
import requests

url = 'http://imgs.xkcd.com/comics/python.png'
saved_pdf_file = 'xkcd_requests.png'

try:
    response = requests.get(url)
except requests.HTTPError as err:
    print("Unable to open URL:", err)
    sys.exit(1)

if response.status_code == requests.codes.OK:
    with open(saved_pdf_file, 'wb') as xkcd_out:
        xkcd_out.write(response.content)

# the script in ANSWERS does not display the fetched image
# so the following needs to be added

if sys.platform == 'win32':
    cmd = saved_pdf_file
elif sys.platform == 'darwin':
    # 'darwin' is Mac OS X
    cmd = 'open ' + saved_pdf_file
else:
    cmd = 'acroread ' + saved_pdf_file

os.system(cmd)
