#!/usr/bin/python

import urllib
import re
from BeautifulSoup import *


url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retrieve all anchor tags
tags = soup('a')
for tag in tags:
	print tag.get('href', None)




'''
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
	print link
'''

'''
counts = dict()
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
print counts
'''

'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
	data = mysock.recv(512)
	if ( len(data) < 1 ) :
		break
	print data
	
mysock.close()
'''