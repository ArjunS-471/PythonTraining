import requests
from bs4 import BeautifulSoup

url = "https://pixabay.com"
url = "https://unsplash.com/s/photos/nature"

response = requests.get(url)

#print(response.text)
#print(type(response.text))

soup = BeautifulSoup(response.text,'html.parser')

images = soup.find_all("img",{"srcset":True})

print(len(images))

image_url = images[-1]
image_url = image_url['src']

#print(image_url)

img_data = requests.get(image_url).content
img_path = "sample_image.jpg"

with open(img_path, "wb") as img_file_handler:
    img_file_handler.write(img_data)

for img in images:
    print("image source:", img.get("src"))