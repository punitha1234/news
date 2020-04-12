from bs4 import *
import requests
import re
content=requests.get('https://en.wikipedia.org/wiki/Wikipedia')
soup=BeautifulSoup(content.text,'lxml')
text=""
for p in soup.find_all('p')[:5]:
	text+=p.text
text=re.sub(r'[[0-9]*\]',' ',text)	
print(text)
print(soup.h2.string)
news=soup.find('div',{'class':'toctitle'})
new1=soup.find('ul')
sp=new1.find_all('a')
for spp in sp:
	s1=spp.find('span')
	s11=s1.string 
	for spp in sp:	
		s2=spp.find('span',{'class':'toctext'}) 
		s22=s2.string
	print(s11+s22)	