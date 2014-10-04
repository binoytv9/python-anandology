"""	Reimplement the unique function implemented in the earlier examples using set		"""

def unique(list):
	uniq=[]				# list to store unique elements
	for i in list:
		if i not in uniq:
			uniq.append(i)
	return uniq

print unique([1,2,1,3,2,5])
