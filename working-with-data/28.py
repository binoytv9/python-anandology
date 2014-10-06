"""	Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.	"""


def enumerate(list):
	return [(list.index(item),item)for item in list]

print enumerate(["a", "b", "c"])
