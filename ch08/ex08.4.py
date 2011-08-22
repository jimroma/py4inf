#!/usr/bin/python


wordlist = []

fhand = open('romeo.txt')
for line in fhand:
	words = line.split()
	for word in words:
		if word in wordlist : continue
		wordlist.append(word)
	
wordlist.sort()
print wordlist