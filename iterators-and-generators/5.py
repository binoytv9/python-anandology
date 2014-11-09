"""	Write a function to compute the total number of lines of 
	code in all python files in the specified directory recursively	"""


def getpath(directory):
	for name in os.listdir(directory):
		yield os.path.join(directory,name)

def getlines(filename):
	for line in open(filename):
		yield line

def get_no_of_lines(filename):
	count = 0
	for line in getlines(filename):
		count += 1
	return count

def findfiles(directory='.'):
	count = 0
	for path in getpath(directory):
		if os.path.isfile(path):
			if os.path.splitext(path)[1] == '.py':
				count += get_no_of_lines(path)	
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
