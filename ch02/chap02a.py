#!/usr/bin/python

name = raw_input("Enter your name NOW!!!!: \n")
print "Hello", name

hours = raw_input("Enter hours: \n")
rate = raw_input("Enter your rate: \n")
x = (float(hours) * float(rate))
print "Pay:", x


cel = raw_input("Enter temp in celsius to convert to fahrenheit: \n")
far = (int(cel) * 1.8) + 32
print cel, "degrees Celsius is ", far, "degrees Fahrenheit"
