"""	Write a function unique to find all the unique elements of a list.	"""

def unique(list):
	uniq=[]				# list to store unique elements
	for i in list:
		k=0
		for j in uniq:
			if i==j:	# checking whether i is in uniq
				k=1
				break;
		if k==0:		# if not found add i to uniq
			uniq.append(i)
	return uniq

print unique([1,2,1,3,2,5])
