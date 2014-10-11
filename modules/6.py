"""	Write a program antihtml.py that takes a URL as argument, 
	downloads the html from web and print it after stripping html tags.	"""


def antihtml(url):
	page=urllib.urlopen(url).read()
	antitag=re.sub(r'\s*<.*?>\s*','',page,flags=re.S)
	print '\ncontent without html tag :\n\n',antitag
	f=open('anti.html','w')
	f.write(antitag)
	f.close()

import urllib,re,sys

if len(sys.argv)!=2:
	print 'error : invalid usage\nusage : python antihtml.py <url>\n\n'
else:
	antihtml(sys.argv[1])
