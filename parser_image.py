import requests
import fake_useragent
from bs4 import BeautifulSoup

URL = "https://www.freestockimages.ru/recreation"

image_number = 0
responce = requests.get(URL).text
soup = BeautifulSoup(responce, 'lxml')

block = soup.find('div', class_="comp-ivb5banb")
# print(block)
all_image = block.find_all('div', class_="item-link-wrapper")

for image in all_image:
    image_number += 1
    image_link = image.find('img').get('src')

    #save_photo
    image_bytes = requests.get(f'{image_link}').content
    with open(f'image/{image_number}.jpg', 'wb') as file:
        file.write(image_bytes)




