import requests
from bs4 import BeautifulSoup

def get_random_fact():
        link = 'https://randstuff.ru/fact/'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        fact_block = soup.find('div', id='fact')
        fact_text = fact_block.find('td').text.strip()
        return fact_text

def main():
    random_fact = get_random_fact()
    print(random_fact)

if __name__ == "__main__":
    main()