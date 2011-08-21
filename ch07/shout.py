#!/usr/bin/python

fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
    

for line in fhand:
    line = line.upper().rstrip()
    print line



