import requests
from bs4 import BeautifulSoup

url = "https://realpython.com"

response = requests.get(url)

#print(response.text)
#print(type(response.text))

soup = BeautifulSoup(response.text,'html.parser')

titles = soup.find_all(class_ = 'card-title')
for title in titles:
    print(title.text)