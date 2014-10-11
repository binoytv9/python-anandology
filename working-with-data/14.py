"""	Improve the unique function written in previous problems to take an optional key 
	function as argument and use the return value of the key function to check for uniqueness.	"""


def unique(list,key):
	uniq=[]				# list to store unique elements
	for i in list:
		if key(i) not in uniq:
			uniq.append(key(i))
	return uniq
print unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
