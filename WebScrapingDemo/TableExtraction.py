import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/world-population/"

response = requests.get(url)

#print(response.text)
#print(type(response.text))

soup = BeautifulSoup(response.text,'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

master_list = []

for row in rows:
    cells = row.find_all('td')
    data = [cell.text.strip() for cell in cells]
    #print(data)
    #print(type(data))
    master_list.append(data)

#print(type(master_list))
#print(master_list)
df = pd.DataFrame(master_list, columns = ['Year','Population','Yearly % Change','Yearly Change','Median Age','Fertility Rate','Density'])
print(df)