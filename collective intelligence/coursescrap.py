import requests
from bs4 import BeautifulSoup


def printTable(clist):
    for x in clist[:]:
        setr = ""
        for y in x[:]:
            setr += str(y) + "\t"
        print setr


page = requests.get('http://www.cse.iitm.ac.in/courses.php?full=1')
# print page.status_code

soup = BeautifulSoup(page.content, 'html.parser')

container = soup.find(id='container')
table = container.find_all('table')[0]

content = table.select("tr")

cList = []

for x in content[1:]:
    td = x.select("td")
    det = [y.get_text() for y in td]
    cList.append(det)

# print len(content)
printTable(cList)
