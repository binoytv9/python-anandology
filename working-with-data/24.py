"""	Provide an implementation for zip function using list comprehensions.	"""

def zip(lst1,lst2):
	return [(i,j) for i in lst1 for j in lst2 if lst1.index(i)==lst2.index(j)]

print zip([1, 2, 3], ["a", "b", "c"])
