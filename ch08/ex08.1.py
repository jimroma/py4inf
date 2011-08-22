#!/usr/bin/python

alph = [1, 2, 3, 4, 5]

def chop(l):
    del l[0]
    del l[len(l) - 1]
    
def mid(l):
    del l[0]
    del l[len(l) - 1]    
    return l
    
print alph  
#chop(alph)
#print alph
x = mid(alph)
print x


'''
fhand = open('mbox-short.txt')
for line in fhand:
    line =  line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print words[2]


'''

#t = 0
#c = 0
#while ( True ):
#    inp = raw_input('Enter a number: ')
#    if inp == 'done' : break
#    v = float(inp)
#    t = t + v
#    c = c + 1
#    
#avg = t/c
#print 'Average:', avg
#

  
