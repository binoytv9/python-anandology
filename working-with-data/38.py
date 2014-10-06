"""	Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.	"""


def invertdict(dictn):
	new={}
	for key in dictn:
		new[dictn[key]]=key
	return new

print invertdict({'x': 1, 'y': 2, 'z': 3})
