"""	Write a program reverse.py to print lines of a file in reverse order.	"""

def reverse(lineslist):
	for i in lineslist[::-1]:
		print i

import sys
if len(sys.argv)==1:
	print '\terror : no filename specified\n\tusage : python reverse.py <filename>'
else:
	reverse(open(sys.argv[1]).readlines())
