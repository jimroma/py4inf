#!/usr/bin/python

import re

hand = open('mbox.txt')


for line in hand:
	line = line.rstrip()
	x = re.findall('^New Revision: ([0-9]*)', line)
	if x > 0 : 
		print x
	
		




# New Revision: 39772

		
		