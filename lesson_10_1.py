import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HOST = 'https://www.moyo.ua/'
URL = 'https://www.moyo.ua/ua/telecommunication/smart/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='product-item')
    cards = []
    for item in items:
        cards.append(
            {
                'title': item.find('a', class_='product-item_name gtm-link-product').get_text(strip=True),
                'product_link': HOST + item.find('a', class_='product-item_name gtm-link-product').get('href'),
                'price': item.find('div', class_='product-item_price_oldprice').get_text(strip=True)[:-3]
            }
        )
    return cards


html = get_html(URL)
print(get_content(html.text))