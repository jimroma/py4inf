#!/usr/bin/python

inp = raw_input("Enter a number between 0.0 and 1.0 ")

def grade(inp):
	num = float(inp)
	if num < 0 or num > 1:
		return "Bad Score"
	elif num >= 0.9:
	    return "A"
	elif num >= 0.8:
	    return "B"
	elif num >= 0.7:
	    return "C"
	elif num >= 0.6:
	    return "D"
	elif num < 0.6:
	    return "F"
	
	
score = grade(inp)

#print str(score)
print score