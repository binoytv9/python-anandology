"""	Write a program center_align.py to center align all lines in the given file.	"""


def center_align(linelist):
	ml=maxlen(linelist)
	for i in linelist:
		bl=(ml-len(i))/2
		print ' '*bl,i

def maxlen(linelist):
	ml=len(linelist[0])
	for i in linelist:
		if ml < len(i):
			ml=len(i)
	return ml

import sys
if len(sys.argv)!=2:
	print '\terror : specify a filename\n\tusage : python 19.py <filename>\n\n'
else:
	center_align(open(sys.argv[1]).readlines())
