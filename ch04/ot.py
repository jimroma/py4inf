#!/usr/bin/python


def rate(h, r):
	try:
		if float(h) > 40.0:
			ot = float(h) - 40.0
			otRate = float(r) * 1.5
			otPay = ot * otRate
			pay = (float(r) * 40.0) + otPay
			return pay
		elif float(h) < 40.0:	
			x = (float(h) * float(r))
			return x
	except:
		print "invalid imput"
		
h = raw_input('Enter Hours ')
r = raw_input('Enter Rate ')


pay = rate(h, r)

print str(pay)

