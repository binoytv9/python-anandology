"""	Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator	"""


def peep(it):
	i1,i2 = itertools.tee(it)
	return  list(i1)[0],i2


import itertools

it = iter(range(2,8))
x, it1 = peep(it)
print x, list(it1)
