#!/usr/bin/python
import urllib

x = 0
counts = dict()
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	words = line.split()
	for c in words:
		x = x + 1
print x
print line



'''

	for word in words:
		counts[word] = counts.get(word, 0) + 1
print counts
'''