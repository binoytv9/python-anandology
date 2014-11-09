"""	Write a function to compute the number of python files (.py extension) in a specified directory recursively	"""


def getpath(directory):
	for name in os.listdir(directory):
		yield os.path.join(directory,name)

def findfiles(directory='.'):
	count = 0
	for path in getpath(directory):
		if os.path.isfile(path):
			if os.path.splitext(path)[1] == '.py':
				count += 1	
		else:
			findfiles(path)
	if count > 0:
		print count,'\t',directory


import os
import sys

if len(sys.argv) > 1:
	findfiles(sys.argv[1])
else:
	findfiles()
