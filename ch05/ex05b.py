#!/usr/bin/python

numlist = []
total = 0
c = 0

while True:
    num = raw_input('Enter a number: ')
    #print num
    numlist.append(num)
    if num == 'done':
        numlist.pop()
        break
        
print numlist
print 'Minimum', min(numlist)
print 'Maximum', max(numlist)


