import aiohttp
import json
import os
import logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s |   %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')

class ForumEditor:
    """
    Класс для редактирования информации пользователей форума

    Атрибуты:
        debug (bool): Указывает, включен ли режим отладки
    """

    def __init__(self, debug):
        """
        Инициализирует объект ForumEditor

        Args:
            debug (bool): Указывает, включен ли режим отладки
        """
        self.debug = debug
        directory = "C:/2501/ply_Alib/data"
        if not os.path.exists(directory):
            logging.error(f"[{self.__class__.__name__}] // Error: {directory} not found...")
            return
        else:
            logging.debug(f"[{self.__class__.__name__}] // Headers.json acquired in: {directory}")
        json_headers_file_path = os.path.join(directory, 'headers.json')

        with open(json_headers_file_path, 'r') as file:
            self.headers_data = json.load(file)

    async def send_request(self, id, data):
        """
        Отправляет запрос на обновление информации пользователя

        Args:
            id (int): Идентификатор пользователя
            data (dict): Данные для отправки в запросе

        Returns:
            bool: True, если запрос успешно отправлен, False в противном случае
        """
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
