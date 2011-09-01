#!/usr/bin/python

import re

hand = open('mbox.txt')
c = 0
nums = list()
num = 0
avg = 0

for line in hand:
	line = line.rstrip()
	#if re.findall('^New Revision: ([0-9]*)', line) :
	x = re.findall('^New Revision: ([0-9]*)', line)

	if len(x) > 0 : 
		c += 1
		num = float(x[0])
		nums.append(num)
		
print 'Number of items:', c	
total = sum(nums)
print 'Sum of items:', total
avg = total/c
print 'Average:', avg




#New Revision: 39772

		
		