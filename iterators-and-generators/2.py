"""	Write a program that takes one or more filenames as arguments 
	and prints all the lines which are longer than 40 characters	"""


def readlines(filenames):
	for filename in filenames:
		try:
			for line in open(filename):
				yield line
		except IOError:
			print "\n\t\t'%s' file doesn't exist!!!" %filename

def printlines(lines):
	for line in lines:
		if len(line) > 40:
			print line



if __name__ == '__main__':
	import sys
	if len(sys.argv)>1:
		filenames=sys.argv[1:]
		lines=readlines(filenames)
		printlines(lines)
