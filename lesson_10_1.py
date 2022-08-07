import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HOST = 'https://tviy.club/'
URL = 'https://tviy.club/sumki-genskiekoganye-genskie-sumki'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}


def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='product-thumb')
    cards = []
    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='product-name').get_text(strip=True)
            }
        )

    return cards


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        write = csv.writer(file, delimiter=';')
        write.writerow(['Название карточки товара'])
        for item in items:
            write.writerow([item['title']])


def parser():
    PAGINATION = input('Введите число для парсинга страниц: ')
    PAGINATION = int(PAGINATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGINATION +1):
            print(f'Парсинг страницы №: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            save_doc(cards, CSV)
        print('Парсинг закончен! Спарсено', len(cards), 'карточек товара!')
    else:
        print('Error')


parser()