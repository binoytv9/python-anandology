"""	Write a program split.py, that takes an integer n and a filename as command line 
	arguments and splits the file into multiple small files with each having n lines	"""


def getlines(filename):
	for line in open(filename):
		yield line

def split(filename,n):
	i=1
	count=0
	fout = open('sub0'+os.path.splitext(filename)[1],'w')
	for line in getlines(filename):
		if count == n:
			fout.close()
			fout = open('sub' + str(i) + os.path.splitext(filename)[1],'w')
			count=0
			i+=1
		fout.write(line)
		count += 1
	fout.close()



import sys
import os

if len(sys.argv) != 3:
	print 'Invalid usage!!!'
	print 'usage : python split.py <n> <filename>'
	print "splits the file 'filename' into multiple small files with each having 'n' lines"
else:
	split(sys.argv[2],int(sys.argv[1]))
