import requests
import os
import json
import asyncio
import time
import random

class ForumBioEditor:
    def __init__(self):
        self.forum_link = None
        current_directory = os.path.dirname(os.path.abspath(__file__))
        json_headers_file_path = os.path.join(current_directory, 'data/headers.json')

        with open(json_headers_file_path, 'r') as file:
            self.headers_data = json.load(file)

    async def send_message(self, id):
        headers = {
            'X-CSRF-Token': self.headers_data['Token'],
            'Cookie': self.headers_data['Cookies'],
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
    user_id = int(input('Введите ID пользователя: '))
    id = user_id
    sender = ForumBioEditor()
    asyncio.run(sender.run(id))
    while True:
        for i in range(1, 61):
            i = i + 1
            ## """
            if i == 2: print('[/-------]...')
            if i == 4: print('[-/------]...')
            if i == 6: print('[--/-----]...')
            if i == 8: print('[---/----]...')
            if i == 16: print('[----/---]...')
            if i == 32: print('[----/---]...')
            if i == 60: print('[-------/]...')
            ## """
            time.sleep(1)
        result = asyncio.run(sender.send_message(id))
        print("// Looped...")
        time.sleep(1)
        if not result:
            break


if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
    main()