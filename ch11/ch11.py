#!/usr/bin/python

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]', line)
	if len(x) > 0:
		print x

		
		