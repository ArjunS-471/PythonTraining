import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

#GET Method
response = requests.get(url)

if (response.status_code == 200):
    print("everything went well")
    #print(response.json())
else:
    print("something went wrong", str(response.status_code))

df = pd.DataFrame(response.json())
print(df)