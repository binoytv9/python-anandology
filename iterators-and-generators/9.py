"""	The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) 
	for each value in the source. Write a function my_enumerate that works like enumerate	"""


def my_enumerate(iterable):
	index=0
	for item in iterable:
		yield index,item
		index += 1

print list(my_enumerate(["a", "b", "c"]))

for i, c in my_enumerate(["a", "b", "c"]):
	print i, c
