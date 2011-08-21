#!/usr/bin/python

fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
c = 0
t = 0 
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:') :
        c = c + 1
        x = line.find(':')
        start = x + 1
        num = float(line[start:].lstrip())
        t = num + t

print 'Count:', c
print 'Total:', t
avg = t/c
print 'Average spam confidence:', avg






