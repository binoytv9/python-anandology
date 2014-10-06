"""	write a function to count frequency of words in a file	"""


def word_frequency(words):
	freq={}
	for word in words:
		freq[word]=freq.get(word,0)+1
	return freq

for word,count in word_frequency(open('she.txt').read().split()).items():
	print count,'\t',word
