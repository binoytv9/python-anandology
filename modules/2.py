"""	Write a program extcount.py to count number of files for each extension in the given directory. The program 
	should take a directory name as argument and print count and extension for each available file extension.	"""


def extcount(files):
	dictn={}
	for i in files:
		dictn[ext(i)]=dictn.get(ext(i),0)+1
	return dictn.items()

def ext(name):
	extn=''
	for i in name[::-1]:
		if i=='.':
			break;
		extn+=i
	return extn[::-1]

import os,sys

if len(sys.argv)!=2:
	print 'error!!!\nusage : python extcount <path>\n\n'
else:
	files=os.listdir(sys.argv[1])

	for extn,count in extcount(files):
		print count,'\t',extn
