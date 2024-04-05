import requests
import os
import json
import asyncio
import time
import random
from Libs.animation import animate, clear_animation

class ForumBioEditor:
    def __init__(self):
        self.forum_link = None
        current_directory = os.path.dirname(os.path.abspath(__file__))
        json_headers_file_path = os.path.join(current_directory, 'data/headers.json')

        with open(json_headers_file_path, 'r') as file:
            self.headers_data = json.load(file)

    async def send_message(self, id):
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

        if response.status_code != 200:  # Если код ответа не равен 200
            print("// Waiting response...")
            time.sleep(0.01)
            print("// Response code:", response.status_code)
            time.sleep(0.5)
            print("//", response.text)
            return False  # Возвращаем False, чтобы основной код мог обработать это условие

        print("// Waiting response...")
        time.sleep(0.01)
        print("// Response code:", response.status_code)
        time.sleep(0.5)
        print("// Done!")
        return True  # Возвращаем True, если код ответа равен 200

    async def run(self, id):
        self.link = "https://forum.wayzer.ru/api/users/" + str(id)
        await self.send_message(id)

def main():
    user_id = int(input('// Enter a ID of user: '))
    delay = int(input('// Enter a delay (in seconds): '))
    id = user_id
    loop = 0
    sender = ForumBioEditor()
    asyncio.run(sender.run(id))
    while True:
        animate(delay)
        clear_animation()
        result = asyncio.run(sender.send_message(id))
        loop = loop + 1
        print(f"// Loop: {loop}")
        time.sleep(0.3)
        if not result:
            break


if __name__ == "__main__":
    main()