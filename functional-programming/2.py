"""	Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character	"""

def flatten_dict(d,result=None,prefix=''):
	if result == None:
		result = {}

	for key in d:
		if isinstance(d[key],dict):
			flatten_dict(d[key],result,prefix + str(key) + '.')
		else:
			result[prefix+str(key)] = d[key]
	return result

print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
print flatten_dict({'a': 1, 'b': {'x': {'l': {1: 4, 2: 'e'}}, 'y': 3}, 'c': 4})
