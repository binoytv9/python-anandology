"""	The above wrap program is not so nice because it is breaking the line at middle of any word. Can you 
	write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?	"""

def wordwrap(linelist,width):
	for i in linelist:
		if len(i)>width:
			wid=width
			while i[wid]!=' ':
				wid-=1
			print i[:wid],'\n',i[wid:]
		else:
			print i


import sys
if len(sys.argv)!=3:
	print '\terror : specify a filename and/or string\n\tusage : python 19.py <filename> <width>\n\n'
else:
	wordwrap(open(sys.argv[1]).readlines(),int(sys.argv[2]))
