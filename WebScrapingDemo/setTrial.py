import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

#print(response.text)
#print(type(response.text))

soup = BeautifulSoup(response.text,'html.parser')
#print(soup)

h1_tag = soup.find('h1')
if(h1_tag):
    print(h1_tag.text)

links = soup.find_all('a')
for link in links:
    href = link.get('href')
    print(href)

# para = soup.find('p')
# if (para):
#     print(para.text)

paras = soup.find_all('p')
for para in paras:
    print(para.text)