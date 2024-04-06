import aiohttp
import json
import os
import logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s |   %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')

class ForumEditor:
    def __init__(self, debug):
        self.debug = debug
        current_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.dirname(current_directory)
        json_headers_file_path = os.path.join(data_directory, 'headers.json') # ply_alib/data/headers.json

        with open(json_headers_file_path, 'r') as file:
            self.headers_data = json.load(file)

    async def send_request(self, id, data):
        self.link = f"https://forum.wayzer.ru/api/users/{id}"
        headers = {
            'X-CSRF-Token': self.headers_data['X-CSRF-Token'],
            'Cookie': self.headers_data['Cookie'],
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.patch(self.link, json=data) as response:
                    response_text = await response.text()
                    if response.status != 200:
                        if not self.debug:
                            return False
                        logging.error(f"[{self.__class__.__name__}] // Response code: {response.status}, {response_text}")
                        return False
                    else:
                        logging.info(f"[{self.__class__.__name__}] // Done!")
                        return True
            except aiohttp.ClientError as e:
                if not self.debug:
                    return False
                logging.error(f"[{self.__class__.__name__}] // Error: {e}")
                return False
