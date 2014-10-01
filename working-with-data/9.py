"""	 Write a function cumulative_product to compute cumulative product of a list of numbers.	"""

def cumulative_product(list):
	pro=1
	cum=[]
	for i in list:
		pro*=i
		cum.append(pro)
	return cum

print cumulative_product([1,2,3,4,5])
print cumulative_product([3,6,8,9,1,3])
