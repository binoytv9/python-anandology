"""	Implement a function izip that works like itertools.izip	"""


def my_izip(it1,it2):
	for i in zip(it1,it2):
		yield i

for x, y in my_izip(["a", "b", "c"], [1, 2, 3]):
	print x, y

for i in my_izip(["a", "b", "c"], [1, 2, 3]):
	print i

print my_izip(["a", "b", "c"], [1, 2, 3])
