#!/usr/bin/python

str = 'X-DSPAM-Confidence:   0.8475'
x = str.find(':')
start = x + 1
num = float(str[start:].lstrip())
print num




