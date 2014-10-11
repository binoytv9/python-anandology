"""	Write a regular expression to validate a phone number.	"""

def validate(num):
	pat=r'^([+]?\d{1,2})?(\d{10})$'
	if re.search(pat,num):
		print '\n\n%s is a valide mobile number!!\n\n'%num
	else:
		print '\n\n%s is not a valide mobile number!!\n\n'%num

import re,sys

if len(sys.argv)!=2:
	print 'error : invalid syntax!!\nusage : python validate.py <mobile number>\n\n'
else:
	validate(sys.argv[1])
