#!/usr/bin/python

fhand = open('mbox-short.txt')
counts = dict()
domain = ''

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From' : continue

	domain = words[1].split('@') #use split to create a list a 2 item list
	if domain[1] not in counts:
		counts[domain[1]] = 1
	else:
		counts[domain[1]] += 1
			
			
print counts	






#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008