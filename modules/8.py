"""	Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.	"""

def links(url):
	page=urllib.urlopen(url).read()
	link=r'https?://.+?"'

	for i in re.findall(link,page):
		print i[:-1]



import re,sys,urllib

if len(sys.argv)!=2:
	print 'error : invalid syntax\nusage : python links.py <url>\n\n'
else:
	links(sys.argv[1])
