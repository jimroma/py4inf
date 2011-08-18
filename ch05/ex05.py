#!/usr/bin/python

numlist = []
total = 0
while True:
    num = raw_input('Enter a number: ')
    print num
    numlist.append(num)
    if num == 'done':
        numlist.pop()
        break
        
print numlist
#print min(numlist)
#print max(numlist)

for i in numlist:
    total = total + int(i)
print 'Sum:', total



    

