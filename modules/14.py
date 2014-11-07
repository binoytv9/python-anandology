"""	Create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library 
	for parsing HTML. Try using it to extract all HTML links from a webpage	"""

from bs4 import BeautifulSoup as bs
import urllib

content=urllib.urlopen("https://docs.python.org/2/library/urllib.html").read()

soup=bs(content)

for link in soup.find_all('a'):
	print link.get('href')
