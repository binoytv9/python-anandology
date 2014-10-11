"""	Write a program wget.py to download a given URL. The program should accept a URL as argument, download it 
	and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.	"""


def wget(url):
	content=urllib.urlopen(url).read()
	bname=basename(url)
	if bname != '':
		page = open(bname,'w')
	else:
		bname='index.html'
		page = open(bname,'w')

	print 'saving %s as %s'%(url,bname)
	page.write(content)
	page.close()

def basename(url):
	bname=''
	for i in url[::-1]:
		if i == '/':
			break
		bname+=i
	return bname[::-1]

import sys,urllib

if len(sys.argv)!=2:
	print 'error : undefined usage\nusage : python wget.py <url>\n\n'
else:
	wget(sys.argv[1])
