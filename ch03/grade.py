try:
	inp = raw_input("Enter a number between 0.0 and 1.0 ")
	num = float(inp)
	if num < 0 or num > 1:
		print "Bad Score"
	elif num >= 0.9:
	    print "A"
	elif num >= 0.8:
	    print "B"
	elif num >= 0.7:
	    print "C"
	elif num >= 0.6:
	    print "D"
	elif num < 0.6:
	    print "F"
except:
	print "Bad Score"