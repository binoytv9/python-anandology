"""	 Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width	"""


def wrap(linelist,width):
	for i in linelist:
		if len(i)>width:
			print i[:30],'\n',i[30:]
		else:
			print i


import sys
if len(sys.argv)!=3:
	print '\terror : specify a filename and/or string\n\tusage : python 19.py <filename> <width>\n\n'
else:
	wrap(open(sys.argv[1]).readlines(),int(sys.argv[2]))
