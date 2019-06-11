import requests
from bs4 import BeautifulSoup
wiki = "https://en.wikipedia.org/wiki/Deep_learning"
page = requests.get(wiki).text
soup = BeautifulSoup(page,"html.parser")
anchors = soup.find_all("a")
print("==========================Title=====================")
print(soup.title.string)
for anchor in anchors:
     print("**************Anchor tag**********")
     print(anchor.get_text())
     print("==============Href================")
     print(anchor.get('href'))

