def istrcmp(x,y):
	if x.upper() == y.upper():
		return True
	else:
		return False

print istrcmp('python', 'Python')
print istrcmp('LaTeX', 'Latex')
print istrcmp('a', 'b')
