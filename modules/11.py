"""	Write a python program zip.py to create a zip file. The program should take 
	name of zip file as first argument and files to add as rest of the arguments.	"""

def zip(name,f1,f2):
	zf=zipfile.ZipFile(name,'w')
	zf.write(f1)
	zf.write(f2)
	zf.close()

import sys,zipfile

if len(sys.argv)<2:
	print 'error : invalid syntax!!\nusage : python zip.py <name.zip> <file1> <file2>\n\n'
else:
	zip(sys.argv[1],sys.argv[2],sys.argv[3])
