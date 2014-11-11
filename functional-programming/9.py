"""	Write a function permute to compute all possible permutations of elements of a given list	"""


def permute(lst,index=0,result=None,tmp=[]):
	if result == None:
		result=[]
		result.append(lst[:])
	else:
		copy(result,tmp)

	if index == len(lst):
		return result

	tmp=[]
	for j in result:
		for i in range(index+1,len(lst)):
			tmp.append(swap(j,index,i))

	permute(lst,index+1,result,tmp)
	return result

def copy(d,s):
	for i in s:
		d.append(i)

def swap(name,index,i):
	lst=list(name)
	lst[index],lst[i] = lst[i],lst[index]
	return lst

print permute([1, 2, 3])
print permute([1, 2, 3,4])
