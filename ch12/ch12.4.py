#!/usr/lib/python

import urllib
from BeautifulSoup import *


total = 0
url = raw_input('Enter -')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all anchor tags
tags = soup('a')
for tag in tags:
	print tag.get('href', None)
	total += 1
	
print 'total:', total
