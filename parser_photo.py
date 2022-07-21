
import requests
from bs4 import BeautifulSoup

host = 'https://wall.alphacoders.com'


def get_url_photo():
    url = 'https://wall.alphacoders.com/by_resolution.php?w=3840&h=2160'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    container = soup.find('div', class_='page_container')
    container_link = soup.find_all('div', class_="thumb-container-big")

    for item in container_link:
        link = host + item.find('a').get('href')
        yield link


def arrey():
    image_number = 0
    for link in get_url_photo():
        image_number += 1
        response = requests.get(link).text
        soup = BeautifulSoup(response, 'lxml')
        page_photo = soup.find('div', class_="center img-container-desktop")
        photo_url = page_photo.find('a').get('href')

        yield photo_url, image_number


def save_photo():

    for photo_url, image_number in arrey():
        image_bytes = requests.get(f'{photo_url}').content
        with open(f'image/1/{image_number}.jpg', 'wb') as file:
            file.write(image_bytes)


save_photo()