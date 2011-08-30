#!/usr/bin/python

def histogram(L):
    d = {}
    for x in L:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d
L = 'abracadabra'    
d = histogram(L)

hist = histogram(L)
print hist

lst = list()
for key, val in d.items():
    lst.append( (val, key)) 
            
for key, val in lst:
    print val, key

