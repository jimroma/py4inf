#!/usr/bin/python

import string
fhand = open('mbox-short.txt')
counts = dict()
       
for line in fhand:
	if 'From ' in line:
		#print line
		words = line.split()
		word = words[1]
		#print word
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
        
#print counts
        
lst = list()
for key, val in counts.items():
	lst.append( (val, key) )
	
lst.sort(reverse=True)

for key, val in lst[:1]:
	print val, key
	
#print lst



