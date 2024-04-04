import requests
from Libs.random_fact import get_random_fact
from Libs.animation import animate, clear_animation
import json
import time
import os
import sys
# ПАШЕЛ НАХУЙ
def setup_headers():
    exe_path = sys.argv[0]
    exe_dir = os.path.dirname(os.path.abspath(exe_path))
    json_path = os.path.join(exe_dir, 'headers.json')

    if not os.path.exists(json_path):
        raise FileNotFoundError(f'File not found: {json_path}')

    with open(json_path, 'r') as f:
        headers = json.load(f)

    return headers

url = "https://forum.wayzer.ru/api/users/96"
headers = setup_headers()
ids = int(input("Введите ID своего аккаунта: "))

while True:
    bio = f'Created by Star boy.\n{get_random_fact()}'
    data = {
        "data": {
            "type": "users",
            "attributes": {
                "bio": bio,
            },
            "id": ids
        }
    }

    response = requests.post(url, headers=headers, json=data)
    animate(2)
    clear_animation()

    if response.status_code == 200 or response.status_code == 201:
        print(f'\x1b[32mОписание профиля на forum.wayzer.ru успешно изменено на:\n{(bio)}!\x1b[0m\nCode - {response.status_code}')
        print(f'\x1b[33mСледующая смена через 60 секунд!')
        time.sleep(60)
    else:
        print(f'\x1b[31mОшибка при отправке сообщения: {response.status_code}\x1b[0m')
        print(f'\x1b[31mТекст ошибки: {response.text}\x1b[0m')
        quit()
