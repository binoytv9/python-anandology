"""	Write a program to list all the files in the given directory along with their length and last modification time. 
	The output should contain one line for each file containing filename, length and modification date separated by tabs.	"""

def stat(path):
	files=os.listdir(path)

	print 'filename\tsize(B)\tModified Date'
	for i in files:
		status=os.stat(i)
		print '%s\t\t%s\t%s\n' %(i,status[6],status[8])

import os,sys

if len(sys.argv)!=2:
	print 'error!!!\nusage : python stat.py <directory path>\n\n'
else:
	stat(sys.argv[1])
