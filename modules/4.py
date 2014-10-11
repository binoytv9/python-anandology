"""	Write a program to print directory tree. The program should take path of a 
	directory as argument and print all the files in it recursively as a tree.	"""

A=''
def dtree(folder):
	filelist=os.listdir(folder)		# list of files and folder names
	filelist.sort()
	l=len(filelist)
	a=A
	for i in filelist:
		if l==1:
			print '%s\-- %s' %(a,i)
		else:
			print '%s|-- %s' %(a,i)
		l-=1
		path=folder+i+'/'
		if posixpath.isdir(path):	# checks folder or not
			global A
			A+='|   '
			dtree(path)

import os,sys,posixpath

if len(sys.argv)!=2:
	print 'error : invalid usage!!!\nusage : python dtree.py <directory path>\n\n'
else:
	dtree(sys.argv[1]+'/')
