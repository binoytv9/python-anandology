def count_digits(n):
	count=0
	if n<10:
		return 1
	while(n>0):
		count+=1
		n/=10
	return count


print count_digits(0)
