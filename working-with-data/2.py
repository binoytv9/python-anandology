""" Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum """

def sum(list):
	ret=0
	for i in list:
		ret+=i
	return ret

print sum([1,2,3,4,5])

