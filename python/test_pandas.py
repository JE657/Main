# import pandas as pd
#
# data = {'Names': ['jeff','henry'], 'Idk': ['a','b']}
#
#
# df = pd.DataFrame(data=data)
# df.to_csv('test1.csv', index=False, header=1)

import requests
from bs4 import BeautifulSoup
import time

base_url = 'https://www.mybenta.com/search?q=&cat='

_id = 317
page_no = 1

response = requests.get(base_url + str(_id) + "&page=" + str(page_no))
soup = BeautifulSoup(response.content, 'html.parser')

page_category = soup.select_one('span[data-number="{}"]'.format(_id))
print(page_category)
