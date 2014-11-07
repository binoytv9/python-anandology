"""	Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. 
The name of the csv file to read as first argument and the name of the Excel file to write as the second argument	"""


import sys
import tablib

if len(sys.argv) != 3:
	print 'Invalid usage!!!'
	print 'usage : csv2xls csv_filename xls_filename'
else:
	try:
		xls=tablib.Dataset()
		
		csv=open(sys.argv[1],'r').read()
		for row in csv.split():
			xls.append(row.split(','))

		with open(sys.argv[2],'wb') as f:
			f.write(xls.xls)

	except IOError:
		print "csv file doesn't exist!!!"
