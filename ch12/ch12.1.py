#!/usr/bin/python

import socket

name = raw_input('Enter URL: ')
names = name.split('//')
#print names[1]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	mysock.connect((names[1], 80))
	mysock.send('GET name HTTP/1.0\n\n')
except:
	print 'BAD URL'


while True:
	data = mysock.recv(512)
	if ( len(data) < 1 ) :
		break
	print data
	
mysock.close()


