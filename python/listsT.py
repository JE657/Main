from bs4 import BeautifulSoup
import requests
# import lxml
import time


# games-list-container is-windows - div
response = requests.get('https://www.roblox.com/games#/')
time.sleep(2)

soup = BeautifulSoup(response.content, 'html.parser')

d = soup.find_all('ul')
for _d in d:
    print(_d['class'])
