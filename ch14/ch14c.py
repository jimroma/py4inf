#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('twdata.db')
cur = conn.cursor()

cur.execute('SELECT * FROM People')
count = 0 
print 'People:'
for row in cur:
	if count < 5: print row
	count = count + 1
print count, 'rows'

cur.execute('SELECT * FROM Follows')
count = 0 
print 'Follows:'
for row in cur:
	if count < 5 : print row
	count = count + 1
print count, 'rows'

cur.execute('''SELECT * FROM Follows JOIN People
	ON Follows.to_id = People.id WHERE Follows.from_id = 1''')
count = 0 
print 'Conections for id=1:'
for row in cur:
	if count < 5: print row
	count = count + 1
print count, 'rows'

cur.close()



	