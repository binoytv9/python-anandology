"""	 Generalize the above implementation of csv parser to support any delimiter and comments.	"""


def parse(filename, d, c):
	lines=open(filename).readlines()
	new=[]
	for line in lines:
		if line[0] != c:
			new.append([i for i in line if i!=d and i!='\n'])

	return new

print parse('a.txt', '!', '#')
