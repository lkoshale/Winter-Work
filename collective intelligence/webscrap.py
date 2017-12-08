import requests
from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#print page.content
#print page.status_code

soup = BeautifulSoup(page.content, 'html.parser')

#print soup.prettify()

#go in depth to get the element
html = list(soup.children)[2]

body=list(html.children)[3]

p = list(body.children)[1]

p.get_text();

#finds all tag and return list
soup.find_all('p')[0].get_text()


#****-----------------------******#
# Using classes annd id 

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print soup.prettify()
print soup.find_all('p', class_='outer-text')[0]


