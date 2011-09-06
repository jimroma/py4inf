#!/usr/bin/python

import urllib
import re
from BeautifulSoup import *


img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
fhand = open('cover.jpg', 'wb')

size = 0
while True:
	info = img.read(100000)
	if len(info) < 1 : break
	size = size + len(info)
	fhand.write(info)
	
print size, 'characters copied.'
fhand.close()


'''
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retrieve all anchor tags
tags = soup('a')
for tag in tags:
	# Look at the parts of a tag
	print 'TAG:',tag
	print 'URL:',tag.get('href', None)
	print 'Content:',tag.contents[0]
	print 'Attrs:', tag.attrs
'''
	


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