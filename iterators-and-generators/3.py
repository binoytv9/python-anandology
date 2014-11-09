"""	Write a function findfiles that recursively descends the directory 
	tree for the specified directory and generates paths of all the files in the tree	"""

def getpath(directory):
	for name in os.listdir(directory):
		yield os.path.join(directory,name)

def findfiles(directory='.'):
	for path in getpath(directory):
		if os.path.isfile(path):
			print path
		else:
			findfiles(path)

import os
import sys

if len(sys.argv) > 1:
	findfiles(sys.argv[1])
else:
	findfiles()
