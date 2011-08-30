#!/usr/bin/python

def histogram(L):
	d = dict()
	for c in L :
		d[c] = d.get(c, 0) + 1 #dictionary method get takes key as default value, if the key exists the default value is returned outerwise 0 is returned
	return d
	
L = 'abracadabra'    
d = histogram(L)

def listItems(d):
	lst = list()  #create a list that we'll put the dictionary values into
	for key, val in d.items(): #run a for loop over the counts dictionary
		lst.append ( (val, key) ) #creage a list of tuples
	lst.sort(reverse=True) #sort it in reverse so the largest number is listed first

	for key, val in lst[:1] : # print the first item in the list
		return val, key

x = listItems(d)
print x

'''
# Sort the dictionary by value
lst = list()  #create a list that we'll put the dictionary values into
for key, val in d.items(): #run a for loop over the counts dictionary
	lst.append ( (val, key) ) #creage a list of tuples
lst.sort(reverse=True) #sort it in reverse so the largest number is listed first

for key, val in lst[:1] : # print the first item in the list
	print val, key
'''
	
