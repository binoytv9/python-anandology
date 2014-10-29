"""	Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.	"""

def mydoc(name):
	d=dir(name)

#	print __import__
	print name.__doc__

import inspect
import sys

if len(sys.argv) != 2:
	print 'error : invalid syntax!!\nusage : python mydoc.py <name>\n\n'
else:
	mydoc(sys.argv[1])
