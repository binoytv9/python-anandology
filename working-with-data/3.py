"""What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well."""

def sum(list):
	ret=""
	for i in list:
		ret+=i;
	return ret

print sum(["binoy"," ","T"," ","V"])
