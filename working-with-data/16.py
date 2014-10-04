"""	Write a function extsort to sort a list of files based on extension.	"""


def extsort(list):					# sort the given list according to extension 
	list=aftrdotsort(list)				# multiple files with same extension are sorted alphabetically
	list=extgrp(list)
	list=b4dotsort(list)
	return list

def b4dotsort(list):					# function to sort multiple files with same extension
	for i in list:
		i.sort()

	extsortarr=[]
	for i in list:
		for j in i:
			extsortarr.append(j)

	return extsortarr

def aftrdotsort(list):					# function to sort files according to extension only
	arr=[]
	while len(list)!=0:
		minm=min(list)
		arr.append(minm)
		list.remove(minm)
	return arr

def min(list):						# returns the file which is alphabetically lowest
	minm=list[0]
	for i in list:
		if minm[dotindx(minm):]>i[dotindx(i):]:
			minm=i
	return minm

def extgrp(list):					# return list of list having same extension
	new=[]
	while len(list)!=0 :
		ext=list[0][dotindx(list[0]):]
		grp=[list[0]]

		for i in list[1:]:
			if ext == i[dotindx(i):]:
				grp.append(i)

		new.append(grp)
		list=remove(list,grp)
	return new

def dotindx(name):					# function to return index of last dot '.'
	j=0						# i.e, to find the beginning of extension
	indx=len(name)

	for i in name:
		j+=1
		if i=='.':
			indx=j
	return indx

def remove(list,grp):
	for i in grp:
		list.remove(i)
	return list

print extsort(['crt','t.py', 'la.c','a.c', 'b.py', 'par.txt', 'foo.txt','ajk', 'x.c'])
