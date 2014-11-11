"""	Write a function treemap to map a function over nested list	"""


def treemap(fun,lst,result=None):
	if result == None:
		result=[]

	for i in lst:
		if isinstance(i,list):
			result.append(treemap(fun,i))
		else:
			result.append(fun(i))

	return result

print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
