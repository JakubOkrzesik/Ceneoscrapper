from asyncio.proactor_events import constants
import requests

from bs4 import BeautifulSoup

response = requests.get("https://www.ceneo.pl/63490289#tab=reviews")

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select('div.js_product-review')


opinion = opinions.pop(0)

opinion_id = opinion['data-entry-id']

author = opinion.select_one('span.user-post__author-name').get_text().strip()

recomendations = opinion.select_one('span.user-post__author-recomendation > em').get_text()

star_amount = opinion.select_one('span.user-post__score-count').get_text()

content = opinion.select_one('div.user-post__text').get_text()
useful = opinion.select_one('button.vote-yes').get_text()
useless = opinion.select_one('button.vote-no').get_text()
publish_date = opinion.select_one('span.user-post__published > time:nth-child(1)["datetime"]').get_text()
purchase_date = opinion.select_one('span.user-post__published > time:nth-child(2)["datetime"]').get_text()
 
print(content)

