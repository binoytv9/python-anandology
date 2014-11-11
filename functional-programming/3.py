"""	Write a function unflatten_dict to do reverse of flatten_dict	"""


def unflatten_dict(d,result=None):
	if result == None:
		result={}
	for key in d:
		if '.' in key:
			string='result'
			for i in key.split('.'):
				eval(string).setdefault(i,{})		# convert string to python object
				string += '[' + "'" + i + "'"  + ']'
			exec(string + ' = d[key]')			# run string as python expression
		else:
			result[key] = d[key]
	return result

print unflatten_dict({'a': 1, 'b.y': 3, 'b.x.l': 2, 'c': 4})
print unflatten_dict({'a': 1, 'b.x.l.2': 'e', 'c': 4, 'b.x.l.1': 4, 'b.y': 3})
