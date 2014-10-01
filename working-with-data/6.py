""" Write a function reverse to reverse a list. Can you do this without using list slicing? """

def reverse(list):
	l=len(list)-1
	rev=[]
	for i in range(l+1):
		rev.append(list[l-i])
	return rev

print reverse([1,2,3,4,5])
