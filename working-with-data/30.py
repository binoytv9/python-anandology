"""	Write a python function parse_csv to parse csv (comma separated values) files.	"""


def parse_csv(filename):
	csv=[]
	lines=open(filename).readlines()

	for line in lines:
		csv.append([i for i in line if i != ',' and i != '\n'])
	return csv

print parse_csv('a.csv')
