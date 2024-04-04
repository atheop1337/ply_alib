import requests
from Libs.headers import setup_headers
from Libs.random_fact import get_random_fact
from Libs.animation import animate, clear_animation
import time

url = "https://forum.wayzer.ru/api/users/96"
auto = input("Auto?:\n(Y/N): ")
headers = setup_headers(auto)


while True:
    bio = f'Discord: lkqas\n{get_random_fact()}'

    data = {
        "data": {
            "type": "users",
            "attributes": {
                "bio": bio,
            },
            "id": "96" # Айди вашего аккаунта
        }
    }
    response = requests.post(url, headers=headers, json=data) # Запрос на смену
    animate(2)  # Анимация
    clear_animation()  # Килл
    if response.status_code == 200 or response.status_code == 201:
        print(f'\x1b[32mОписание профиля на forum.wayzer.ru успешно изменен на:\n{(bio)}!\x1b[0m\nCode - {response.status_code}')
        print(f'\x1b[33mСледующия смена через 60 секунд!')
        time.sleep(60) # 60 - кол-во секунд через которое меняется рнд факт
    else:
        print(f'\x1b[31mОшибка при отправке сообщения: {response.status_code}\x1b[0m')
        print(f'\x1b[31mТекст ошибки: {response.text}\x1b[0m')
        quit()
