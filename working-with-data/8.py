""" 	Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative 
	sum of a list. Does your implementation work for a list of strings?
"""

def cumulative_sum(list):
	if len(list)==0:			# if list is empty
		return "empty"

	sum = list[0]
	cumulativesum = [sum]			# assigning 1st element

	for i in list[1:]:			
		sum = sum + i
		cumulativesum.append(sum)	
	return cumulativesum


print cumulative_sum([])
print cumulative_sum([1,2,3,4,5])
print cumulative_sum(["binoy","vaishak","shibin","njaeeb"])
