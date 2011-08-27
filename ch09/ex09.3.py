#!/usr/bin/python

fhand = open('mbox-short.txt')
counts = dict()
day = ''

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From' : continue

	day = words[2]
	if day not in counts:
		counts[day] = 1
	else:
		counts[day] += 1
			
			
print counts	


#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008