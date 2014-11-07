"""	Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.	"""

def mydoc(name):
	try:
		m = __import__(name)
	except:
		print "%s module not found!!\n\n" %name
		return
	print m.__doc__
	d = dir(m)
	for i in d:
		if inspect.isfunction(getattr(m,i,False)):
			print i
			print getattr(m,i).__doc__
			print


import inspect
import sys

if len(sys.argv) != 2:
	print 'error : invalid syntax!!\nusage : python mydoc.py <name>\n\n'
else:
	mydoc(sys.argv[1])
