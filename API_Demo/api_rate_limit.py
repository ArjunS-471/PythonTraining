import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params={"ids":"bitcoin", "vs_currencies":"usd"}

for item in range(500):
    print("iteration:", item)
    response = requests.get(url, params)
    print(response)
