#!/usr/bin/python

numlist = []
total = 0
c = 0

while True:
	num = raw_input('Enter a number: ')
	if num.isdigit():
	    numlist.append(num)
	else:
	    print "ENTER A NUMBER"
	if num == 'done':
	    #numlist.pop()
	    break

        
print numlist


for i in numlist:
    total = total + int(i)
print 'Sum:', total

for i in numlist:
	c = c + 1
print 'Number of items:', c

avg = float(total)/float(c)
print 'Average:', float(avg)





    

