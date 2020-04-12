from bs4 import BeautifulSoup
import requests
content=requests.get('https://economictimes.indiatimes.com/headlines.cms')
soup=BeautifulSoup(content.text,'lxml')
news=soup.find('h2',{'class':'headings'})
print(news.span.string)
new1=soup.find('ul',{'class':'headlineData'})
for new11 in new1:
	links=new11.find_all('a')
	for link in links:
		print(link.text)
		print()   