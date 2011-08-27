#!/usr/bin/python

print 'Enter a file name: '
file = raw_input()
fhand = open(file)
counts = dict()
hour = ''

for line in fhand:
    if 'From ' in line:
        words = line.split()
        word = words[5]

        hour = word[0:2]
        if hour not in counts:
            counts[hour] = 1
        else:
            counts[hour] += 1
lst = list()
for key, val in counts.items():
    lst.append( (val, key)) 
            
for key, val in lst:
    print val, key
    

            

