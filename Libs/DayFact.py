import requests
from bs4 import BeautifulSoup

def get_day_fact():
    link = 'https://randstuff.ru/fact/fav/'
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    fact_block = soup.find('div', id='fact')
    fact_text = fact_block.find('td').text.strip()
    return fact_text

random_fact = get_day_fact()