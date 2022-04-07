#!/usr/bin/python3

# Exercises 18-1

import os # need this to display image
import sys
from urllib.request import urlopen
from urllib.error import HTTPError

url = 'http://imgs.xkcd.com/comics/python.png'
saved_pdf_file = 'xkcd_fetch.png'

try:
    response = urlopen(url)
except HTTPError as err:
    print("Unable to open URL:", err)
    sys.exit(1)

pdf_contents = response.read()
response.close()

with open(saved_pdf_file, 'wb') as xkcd_out:
    xkcd_out.write(pdf_contents)

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
