# import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

x = requests.get("https://www.wikihow.com/Apologize-to-a-Cat")

print(x.text[:500])

cla_soup_html = BeautifulSoup(x.text, "html.parser")

cla_soup_text = cla_soup_html.get_text()

cla_data = open('newschool-cla.txt', 'w')
cla_data.write(cla_soup_text)
cla_data.close()


def getTitles(soupdata):  
  titles = soupdata.select("h2")
  if titles:
    for t in titles:
      print(t.text)
      
print("CLA........")
getTitles(cla_soup_html)
