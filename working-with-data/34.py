"""	Improve the word_frequency to print the words in the descending order of the number of occurrences.	"""


def word_frequency(words):
	freq={}
	for word in words:
		freq[word]=freq.get(word,0)+1
	return freq

freqlst=word_frequency(open('she.txt').read().split()).items()
freqlst.sort(key=lambda x: x[1],reverse=True)

for word,count in freqlst:
	print count,'\t',word
