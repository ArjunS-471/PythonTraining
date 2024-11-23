import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {"_page" : 1, "_limit" : 5}

#response = requests.get(url, params = params)

# print(response)
# print(response.json())
# print(response.headers)

# limit = 5
# for count in range(20):
#     #params = {"_page" : 1, "_limit" : counter}
#     params = {"_page" : count, "_limit" : limit}
#     response = requests.get(url, params = params)
#     print("New repsonse")
#     print(len(response.json()))

master_list = []
for item in range(10):
    print("fetching page", params['_page'])
    response = requests.get(url, params = params)

    if (response.status_code == 200):
        posts = response.json()
        master_list.append(posts)
    
        if (not posts):
            print("no more posts")
            break

        params['_page'] += 1
    
    else:
        print("something went wrong")

print(len(master_list))