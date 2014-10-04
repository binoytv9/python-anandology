"""	Write a function lensort to sort a list of strings based on length.	"""

def lensort(list):
	nlist=[]
	while (len(list)!=0):
		min=list[0]
		for i in list:
			if len(min)>len(i):
				min=i
		nlist.append(min)
		list.remove(min)
	return nlist

print lensort(['binoy', 'aaaaaa', 'india', 'ancd'])
print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
