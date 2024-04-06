import requests
import os
import json
import asyncio
import time
import random
from data.libraries.animation import animate, clear_animation

class ForumBioEditor:
    def __init__(self, debug):
        self.debug = debug
        current_directory = os.path.dirname(os.path.abspath(__file__))
        json_headers_file_path = os.path.join(current_directory, 'data/headers.json')

        with open(json_headers_file_path, 'r') as file:
            self.headers_data = json.load(file)

    async def send_request(self, id):
        self.link = "https://forum.wayzer.ru/api/users/" + str(id)
        headers = {
            'X-CSRF-Token': self.headers_data['X-CSRF-Token'],
            'Cookie': self.headers_data['Cookie'],
        }

        phrases = ["(☞ﾟヮﾟ)☞", "(∪.∪ )...zzz", "\\(〇_o)/", "ᕦ(ò_óˇ)ᕤ", "(^\\\\\\^)", "( •̀ ω •́ )✧", "\\^o^/"]

        random_phrase = random.choice(phrases)

        data = {
            "data": {
                "type": "users",
                "attributes": {
                    "bio": f"Powered by 2501\n{random_phrase}"
                },
                "id": f"{id}"
            }
        }

        response = requests.patch(self.link, json=data, headers=headers)

        if response.status_code != 200:  # Если код ответа не равен
            if self.debug == True:
                print(f"[Bio] // Waiting response...")
                time.sleep(0.01)
                print(f"[Bio] // Response code: {response.status_code}")
                time.sleep(0.01)
                print(f"[Bio] // {response.text}")
            time.sleep(0.3)
            return False  # Возвращаем False, чтобы основной код мог обработать это условие

        if self.debug == True:
            print(f"[Bio] // Waiting response...")
            time.sleep(0.01)
            print(f"[Bio] // Response code: {response.status_code}")
            time.sleep(0.01)
            print("[Bio] // Done!")
        time.sleep(0.3)
        return True  # Возвращаем True, если код ответа равен 200

    async def run(self, id):
        await self.send_request(id)


class ForumNickEditor:
    def __init__(self, debug):
        self.debug = debug
        current_directory = os.path.dirname(os.path.abspath(__file__))
        json_headers_file_path = os.path.join(current_directory, 'data/headers.json')

        with open(json_headers_file_path, 'r') as file:
            self.headers_data = json.load(file)

    async def send_request(self, id, nickname):
        self.link = "https://forum.wayzer.ru/api/users/" + str(id)
        headers = {
            'X-CSRF-Token': self.headers_data['X-CSRF-Token'],
            'Cookie': self.headers_data['Cookie'],
        }

        phrases = ["(☞ﾟヮﾟ)☞", "(∪.∪ )...zzz", "\\(〇_o)/", "ᕦ(ò_óˇ)ᕤ", "(^\\\\\\^)", "( •̀ ω •́ )✧", "\\^o^/"]

        random_phrase = random.choice(phrases)

        data = {
            "data": {
                "type": "users",
                "attributes": {
                    "nickname": f"{nickname}\n{random_phrase}"
                },
                "id": f"{id}"
            }
        }

        response = requests.patch(self.link, json=data, headers=headers)

        if response.status_code != 200:  # Если код ответа не равен 200
            if self.debug == True:
                print(f"[Nick] // Waiting response...")
                time.sleep(0.01)
                print(f"[Nick] // Response code: {response.status_code}")
                time.sleep(0.01)
                print(f"[Nick] // {response.text}")
            time.sleep(0.3)
            return False  # Возвращаем False, чтобы основной код мог обработать это условие

        if self.debug == True:
            print(f"[Nick] // Waiting response...")
            time.sleep(0.01)
            print(f"[Nick] // Response code: {response.status_code}")
            time.sleep(0.01)
            print(f"[Nick] // Done!")
        time.sleep(0.3)
        return True  # Возвращаем True, если код ответа равен 200

    async def run(self, id, nickname):
        await self.send_request(id, nickname)


def Run(id, delay, nickname, senderbio, sendernick):
    loop = 0
    while True:
        animate(delay)
        clear_animation()
        resultbio = asyncio.run(senderbio.send_request(id))
        resultnick = asyncio.run(sendernick.send_request(id, nickname))
        loop = loop + 1
        print(f"[2501] // Loop: {loop}")
        time.sleep(0.1)
        if not resultbio or not resultnick:
            break


def main():
    yn = str(input('[2501] // Debug mode? [y/n]: '))
    user_id = int(input('[2501] // Enter a ID of user: '))
    nickname = str(input('[Nick] // Enter a nickname: '))
    delay = int(input('[2501] // Enter a delay (in seconds): '))
    debug = (lambda debug: True if debug.lower() == 'y' else False)(yn)
    print(f'[2501] // Debug: {str(debug)}')
    time.sleep(0.1)
    senderbio = ForumBioEditor(debug=debug)
    sendernick = ForumNickEditor(debug=debug)
    Run(user_id, delay, nickname, senderbio, sendernick)



if __name__ == "__main__":
    main()
