"""	Write a function tree_reverse to reverse elements of a nested-list recursively	"""


def tree_reverse(lst,result=None):
	if result == None:
		result=[]
	for i in lst:
		if isinstance(i,list):
			result.insert(0,tree_reverse(i))
		else:
			result.insert(0,i)
	return result

print tree_reverse([1, 2, 3, 4, 5, 6])
print tree_reverse([[1, 2], [3, [4, 5]], 6])
