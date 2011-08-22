#!/usr/bin/python

numlist = []
while True:
	num = raw_input('Enter a number: ')
	numlist.append(num)
	if num == 'done' : 
		numlist.pop()
		break
	
print numlist
print 'Maximum:',float(max(numlist))
print 'Minimum:',float(min(numlist))

