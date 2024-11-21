import requests
import pandas as pd

#Dictionary
url = "https://api.dictionaryapi.dev/api/v2/entries/en/Computer"
url = "https://namo-memes.herokuapp.com/GET/"
url = "https://geek-jokes.sameerkumar.website/api?format=json"

#GET Method
response = requests.get(url,)

if (response.status_code == 200):
    
    print(response.json())
else:
    print("something went wrong", str(response.status_code))

# df = pd.DataFrame(response.json())
# print(df)