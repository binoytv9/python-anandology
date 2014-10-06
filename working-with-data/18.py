"""	Write a program to print each line of a file in reverse order.	"""

def reverse(line):
	for i in line:
		print " ".join(i.split()[::-1])


reverse(open('she.txt').readlines())
