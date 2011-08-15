inp = raw_input('Enter Fahrenheit Temp to convert ')
try:
	fahr = float(inp)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print cel
except:
	print 'Please enter a number'
