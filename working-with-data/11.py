"""	Write a function dups to find all duplicates in the list.	"""

def dups(list):
	uniq=[]				# list to store unique elements
	dup=[]				# list to store duplicate elements
	for i in list:
		k=0
		for j in uniq:
			if i==j:	# checking whether i is in uniq
				k=1
				break;
		if k==0:		# if not found add i to uniq
			uniq.append(i)
		else:
			dup.append(i)	# if duplicate add i to dup
	return dup

print dups([1,2,1,3,2,5,4,5])
