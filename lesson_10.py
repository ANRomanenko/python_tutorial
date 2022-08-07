from bs4 import BeautifulSoup
import requests

url = 'https://office-guru.ru/python-onlajn-kurs/uroki/beautifulsoup-parsing-html-v-python-na-primerax.html'

response = requests.get(url)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all()
    # cards = []
    # for i in soup.find_all('li'):
    #     cards.append([i.name, i.text])
    # print(cards)
    
# with open('index.html', 'r', encoding='utf-8') as f:
#     contents = f.read()

    # soup = BeautifulSoup(contents, 'lxml')
    # print(soup.text)