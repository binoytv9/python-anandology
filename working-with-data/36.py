"""	Write a program to find anagrams in a given list of words. Two words are called anagrams if one word 
	can be formed by rearranging letters of another. For example 'eat', 'ate' and 'tea' are anagrams.	"""

def anagrams(wlist):
	d={}
	for word in wlist:
		sword=''.join(sorted(word))
		d.setdefault(sword,[]).append(word)
	return d.values()


if __name__ == '__main__':
	print anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
