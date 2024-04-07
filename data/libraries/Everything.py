import requests
import random

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