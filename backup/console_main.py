import aiohttp
import asyncio
import json
import os
import random
import logging
from data.Libs.animation import animate, clear_animation

logging.basicConfig(format='[%(asctime)s] %(levelname)s |   %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')

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

        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.patch(self.link, json=data) as response:
                    response_text = await response.text()
                    if response.status != 200:
                        logging.error(f"[Bio] // Response code: {response.status}, {response_text}")
                        return False
                    else:
                        logging.info("[Bio] // Done!")
                        return True
            except aiohttp.ClientError as e:
                logging.error(f"[Bio] // Error: {e}")
                return False

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

        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.patch(self.link, json=data) as response:
                    response_text = await response.text()
                    if response.status != 200:
                        logging.error(f"[Nick] // Response code: {response.status}, {response_text}")
                        return False
                    else:
                        logging.info("[Nick] // Done!")
                        return True
            except aiohttp.ClientError as e:
                logging.error(f"[Nick] // Error: {e}")
                return False

async def Run(id, delay, nickname, senderbio, sendernick):
    loop = 0
    while True:
        animate(delay)
        clear_animation()
        resultbio = await senderbio.send_request(id)
        resultnick = await sendernick.send_request(id, nickname)
        loop += 1
        print(f"[2501] // Loop: {loop}")
        await asyncio.sleep(0.1)
        if not resultbio or not resultnick:
            break

async def main():
    yn = str(input('[2501] // Debug mode? [y/n]: '))
    user_id = int(input('[2501] // Enter a ID of user: '))
    nickname = str(input('[Nick] // Enter a nickname: '))
    delay = int(input('[2501] // Enter a delay (in seconds): '))
    debug = True if yn.lower() == 'y' else False
    logging.info(f'[2501] // Debug: {str(debug)}')
    await asyncio.sleep(0.1)
    senderbio = ForumBioEditor(debug=debug)
    sendernick = ForumNickEditor(debug=debug)
    await Run(user_id, delay, nickname, senderbio, sendernick)

if __name__ == "__main__":
    asyncio.run(main())
