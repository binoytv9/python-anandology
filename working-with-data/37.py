"""	Write a function valuesort to sort values of a dictionary based on the key.	"""


def valuesort(dictn):
	dictn=dictn.items()
	dictn.sort()
	val=[]
	for i in dictn:
		val.append(i[1])
	return val


print valuesort({'x': 1, 'y': 2, 'a': 3})
