"""	 Implement unix commands head and tail. The head and tail commands take a 
	file as argument and prints its first and last 10 lines of the file respectively.	"""


def head(lineslist):
	for i in lineslist[:10]:
		print i

def tail(lineslist):
	for i in lineslist[-10:]:
		print i

import sys

if len(sys.argv)==1:
	print '\terror : specify a filename\n\tusage : python 19.py <filename>\n\n'
else:
	lines=open(sys.argv[1]).readlines()
	print '-----------------head()-----------------'
	head(lines)
	print '-----------------tail()-----------------'
	tail(lines)
