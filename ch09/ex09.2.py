#!/usr/bin/python

def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

h = histogram('Timmy')
print h
