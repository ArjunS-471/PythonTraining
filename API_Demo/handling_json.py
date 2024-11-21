import requests
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids" : "bitcoin,ethereum", "vs_currencies" : "inr"
}

response = requests.get(url,params)

print(response.json())
print(type(response.json()['ethereum']['inr']))

resp_dict = response.json()
inner_dict = resp_dict['ethereum']
final_value = inner_dict['inr']
print(final_value)
print(response.json()['ethereum']['inr'])