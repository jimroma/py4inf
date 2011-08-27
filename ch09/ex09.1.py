#!/usr/bin/python
#!/usr/bin/python
try:
	name = raw_input('Enter file: ')
	handle = open(name, 'r')
except:
	print 'No file by that name'
	exit()



def wordlist(handle):
	wordlist = dict()
	num = 0
	for line in handle:
		words = line.split()
		for w in words:
			num = num + 1
			wordlist[w] = num
	return wordlist
	

lst = wordlist(handle)
#print lst


while True:
	search = raw_input('Enter word to search for (type done to exit): ')
	if search == 'done' : break
	if search in lst:
		print search, 'is in the list'
	else:
		print search, 'in not in the list'






