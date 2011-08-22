#/usr/bin/python

fhand = open('mbox-short.txt')
c = 0
for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] == 'From:':
            print words[1]
            c = c + 1

print 'There were', c, 'lines in the file with From as the first word'

