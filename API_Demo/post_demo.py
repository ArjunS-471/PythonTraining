import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "Python training", "body" : "training ongoing", "userId" : 1
}

response = requests.post(url,data)

print(response.status_code)

