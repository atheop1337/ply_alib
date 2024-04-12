import aiohttp
import time
import json
import os
import logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s |   %(message)s', datefmt='%H:%M:%S')

class ForumEditor:

    def __init__(self):
        logging.getLogger().setLevel(logging.DEBUG)
        directory = "C:/2501/ply_Alib/data"
        if not os.path.exists(directory):
            time.sleep(0.1)
            logging.error(f"[{self.__class__.__name__}] // Error: {directory} not found...")
            return
        else:
            time.sleep(0.1)
            logging.debug(f"[{self.__class__.__name__}] // Headers.json acquired in: {directory}")
        json_headers_file_path = os.path.join(directory, 'headers.json')

        with open(json_headers_file_path, 'r') as file:
            self.headers_data = json.load(file)

    async def send_request(self, id, data):
        self.link = f"https://forum.wayzer.ru/api/users/{id}"
        headers = {
            'X-CSRF-Token': self.headers_data['CSRF'],
            'Cookie': self.headers_data['flarum'],
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.patch(self.link, json=data) as response:
                    response_text = await response.text()
                    if response.status != 200:
                        error_data = json.loads(response_text)
                        error_code = error_data["errors"][0]["code"]
                        logging.error(f"[{self.__class__.__name__}] // Response code: {response.status}, {error_code}")
                        return False
                    else:
                        time.sleep(0.1)
                        logging.debug(f"[{self.__class__.__name__}] // Done!")
                        return True
            except aiohttp.ClientError as e:
                logging.error(f"[{self.__class__.__name__}] // Error: {e}")
                return False
