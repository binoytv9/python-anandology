"""	Implement unix command grep. The grep command takes a string and a file as 
	arguments and prints all lines in the file which contain the specified string.	"""

def grep(linelist,string):
	for i in linelist:
		if string in i:
			print i
import sys
if len(sys.argv)!=3:
	print '\terror : specify a filename and/or a string\n\tusage : python grep.py <filename> <string>\n\n'
else:
	grep(open(sys.argv[1]).readlines(),sys.argv[2])
