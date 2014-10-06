"""	Write a program to count frequency of characters in a given file. Can you use character 
	frequency to tell whether the given file is a Python program file, C program file or a text file?	"""


def char_count(content):
	freq={}
	for i in content:
		freq[i]=freq.get(i,0)+1
	return freq

for i in char_count(open('she.txt').read()).items():
	print i
