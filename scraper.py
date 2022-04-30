from asyncio.proactor_events import constants
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.ceneo.pl/63490289#tab=reviews"

urls = []

all_opinions = []

while(url):
    response = requests.get(url)

    page = BeautifulSoup(response.text, 'html.parser')

    opinions = page.select('div.js_product-review')

    for opinion in opinions:
        opinion_id = opinion['data-entry-id']
        author = opinion.select_one('span.user-post__author-name').get_text().strip()
        try:
            recomendations = opinion.select_one('span.user-post__author-recomendation > em').get_text()
        except AttributeError:
            recomendations = None
        star_amount = opinion.select_one('span.user-post__score-count').get_text()
        content = opinion.select_one('div.user-post__text').get_text()
        useful = opinion.select_one('button.vote-yes').get_text()
        useless = opinion.select_one('button.vote-no').get_text()
        publish_date = opinion.select_one('span.user-post__published > time:nth-child(1)')["datetime"]
        try:
            purchase_date = opinion.select_one('span.user-post__published > time:nth-child(2)')["datetime"]
        except TypeError:
            purchase_date = "Unknown"
        pros = opinion.select('div.review-feature__title--positives ~ div.review-feature__item')
        pros_1 = [item.get_text().strip() for item in pros]
        cons = opinion.select('div.review-feature__title--negatives ~ div.review-feature__item')
        cons_1 = [item.get_text().strip() for item in cons]

        single_opinion = {
            "opinion_id": opinion_id,
            "author": author,
            "recommendation": recomendations,
            "star_amount": star_amount,
            "content": content,
            "pros": pros_1,
            "cons": cons_1,
            "publish_date": publish_date,
            "purchase_date": purchase_date

        }

        all_opinions.append(single_opinion)
    
    try:
        url = "https://www.ceneo.pl" + page.select_one('a.pagination__next')['href']
    except TypeError:
        url = None
    
    urls.append(url)


with open('opinions/63490289.json', 'w', encoding='UTF-8') as f:
    json.dump(all_opinions, f, indent=4, ensure_ascii=False)