""" Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial? """

def fact(n):		# return factorial of a number
	f=1

	while(n!=0):
		f=f*n
		n-=1

	return f


def product(n):		#factorial using product function
	pro=1
	list=range(n+1)

	for i in list[1:]:
		pro*=i

	return pro

print fact(0)
print fact(5)

print product(5)
print product(0)
