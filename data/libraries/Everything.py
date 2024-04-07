import requests
import random

def generate_citata():
    while True:
        response = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru')
        data = response.json()
        quote = data['quoteText']
        author = data['quoteAuthor']
        if author == '':
            author = 'Unknown author'
        if len(quote) <= 60:
            return quote, author

quote, author = generate_citata()
print(f'Random quote: {quote}\nAuthor: {author}\n')

random_emoji = lambda: chr(random.randint(0x1F600, 0x1F64F))
emoji = random_emoji()
print(f'Случайное эмодзи: {emoji}\n')

def get_bio():
    response = requests.get('https://forum.wayzer.ru/api/users/96') # В будущем делай https://forum.wayzer.ru/api/users/ + {user_id}
    data = response.json()
    bio = data['data']['attributes']['bio']
    return bio

bio = get_bio()
print(f'Описание пользователя:\n{bio}')