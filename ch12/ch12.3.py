#!/usr/bin/python

import urllib


name = raw_input('Enter URL: ')

try:
	fhand = urllib.urlopen(name)
	s = fhand.read()
	print s[:3000]
	print 'Document length:',len(s)
except:
	print 'BAD URL'


