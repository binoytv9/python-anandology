"""	 Write a function group(list, size) that take a list and splits into smaller lists of given size.	"""

def group(list,size):
	grp=[]				# list to store split lists
	i=0				# starting index
	j=size				# stopping index
	l=len(list)

	while(i<l):
		grp.append(list[i:j])
		i=j
		j+=size

	return grp

print group(range(13),5)
