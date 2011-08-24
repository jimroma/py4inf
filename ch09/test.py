#!/usr/bin/python

fhand = open('mbox-short.txt')
counts = dict()
day = ''

for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != 'From' : continue

	day = words[1]
	if day not in counts:
		counts[day] = 1
	else:
		counts[day] += 1
			
			
#print counts	

# Sort the dictionary by value
lst = list()  #create a list that we'll put the dictionary values into
for key, val in counts.items(): #run a for loop over the counts dictionary
	lst.append ( (val, key) ) #creage a list of tuples
lst.sort(reverse=True) #sort it in reverse so the largest number is listed first

for key, val in lst[:1] : # print the first item in the list
	print val, key






#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008