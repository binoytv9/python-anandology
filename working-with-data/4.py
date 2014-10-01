""" Implement a function product, to compute product of a list of numbers """

def product(list):
	pro=1
	for i in list:
		pro*=i
	return pro

print product([1,2,3,4,5])
