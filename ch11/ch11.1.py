#!/usr/bin/python

import re
search = raw_input('Enter a regular expression: ')
hand = open('mbox.txt')
c = 0

for line in hand:
	line = line.rstrip()
	if re.search(search, line) :
		c += 1
		

print 'mbox.txt had', c, 'line that matched', search


		
		