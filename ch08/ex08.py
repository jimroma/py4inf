#!/usr/bin/python


fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 : continue
    #if len(words) == 1 : continue
    
    if words[0] != 'From' : continue
    if words[2] == None : continue
    print words[2]



  
