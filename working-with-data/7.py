""" 	Python has built-in functions min and max to compute minimum and maximum of a given list. 
	Provide an implementation for these functions. 
	What happens when you call your min and max functions with a list of strings? """

def min(list):
	min=list[0]

	for i in list:
		if min>i:
			min=i

	return min

def max(list):
	max=list[0]

	for i in list:
		if max<i:
			max=i

	return max

print "min is "+str(min([1,2,3,4,5,0]))
print "min is "+str(min(["binoy","vaishak","shibin","njaeeb"]))

print "max is "+str(max([1,2,3,4,5,0]))
print "max is "+str(max(["binoy","vaishak","shibin","njaeeb"]))
