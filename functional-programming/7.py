"""	Implement a program dirtree.py that takes a directory as argument and 
	prints all the files in that directory recursively as a tree	"""


def dirtree(dname='.',p=''):
	namelist=os.listdir(dname)
	for name in namelist:
		path=os.path.join(dname,name)

		if name is namelist[-1]:
			print p+'`--',
		else:
			print p+'|--',
		if os.path.isdir(path):
			print name,'/'
			dirtree(path,'|   '+p)
		else:
			print name


import os,sys

if len(sys.argv) == 2:
	dirtree(sys.argv[1])
else:
	dirtree()
