"""	Implement a function product to multiply 2 numbers recursively using + and - operators only	"""

def product(m,n):
	if m == 0 or n == 0 :
		return 0
	return m + product(m,n-1)


print product(2,3)
print product(0,5)
print product(4,0)
