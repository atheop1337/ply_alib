import asyncio
import logging
import random
from data.libraries.animation import animate, clear_animation
from data.libraries.forumEditor import ForumEditor
from data.libraries.random_fact import get_random_fact

logging.basicConfig(format='[%(asctime)s] %(levelname)s |   %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')

class ForumBioEditor(ForumEditor):
    """
    Класс для редактирования биографии пользователя на форуме

    Наследуется от класса ForumEditor

    Атрибуты:
        debug (bool): Указывает, включен ли режим отладки
    """

    async def send_bio_request(self, id, choice):
        """
        Отправляет запрос на обновление "О себе" пользователя

        Args:
            id (int): Идентификатор пользователя

        Returns:
            bool: True, если запрос успешно отправлен, False в противном случае
        """
        phrases = ["(☞ﾟヮﾟ)☞", "(∪.∪ )...zzz", "\\(〇_o)/", "ᕦ(ò_óˇ)ᕤ", "(^\\\\\\^)", "( •̀ ω •́ )✧", "\\^o^/"]
        random_phrase = random.choice(phrases)
        if choice == '1':
            data = {
                "data": {
                    "type": "users",
                    "attributes": {
                        "bio": f"Powered by 2501\n{get_random_fact()}"
                    },
                    "id": f"{id}"
                }
            }
        elif choice == '2':
            data = {
                "data": {
                    "type": "users",
                    "attributes": {
                        "bio": f"Powered by 2501\n{random_phrase}"
                    },
                    "id": f"{id}"
                }
            }
        elif choice == '3':
            choice = random.randint(1, 2)
            if choice == 1:
                data = {
                    "data": {
                        "type": "users",
                        "attributes": {
                            "bio": f"Powered by 2501\n{get_random_fact()}"
                        },
                        "id": f"{id}"
                    }
                }
            elif choice == 2:
                data = {
                    "data": {
                        "type": "users",
                        "attributes": {
                            "bio": f"Powered by 2501\n{random_phrase}"
                        },
                        "id": f"{id}"
                    }
                }
        else:
            print(f"[Bio] // Enter valid variation.")
            quit()
        return await self.send_request(id, data)

class ForumNickEditor(ForumEditor):
    """
    Класс для редактирования ника пользователя на форуме

    Наследуется от класса ForumEditor

    Атрибуты:
        debug (bool): Указывает, включен ли режим отладки
    """

    async def send_nick_request(self, id, nickname):
        """
        Отправляет запрос на обновление ника пользователя

        Args:
            id (int): Идентификатор пользователя
            nickname (str): Новый никнейм

        Returns:
            bool: True, если запрос успешно отправлен, False в противном случае
        """
        phrases = ["(☞ﾟヮﾟ)☞", "(∪.∪ )...zzz", "\\(〇_o)/", "ᕦ(ò_óˇ)ᕤ", "(^\\\\\\^)", "( •̀ ω •́ )✧", "\\^o^/"]
        random_phrase = random.choice(phrases)
        data = {
            "data": {
                "type": "users",
                "attributes": {
                    "nickname": f"{nickname}\n{random_phrase}"
                },
                "id": str(id)
            }
        }
        return await self.send_request(id, data)

async def Run(id, delay, nickname, choice, senderbio, sendernick):
    """
    Запускает основной цикл для непрерывной отправки запросов на обновление биографии и ника пользователя

    Args:
        id (int): Идентификатор пользователя
        delay (int): Задержка между запросами (в секундах)
        nickname (str): Старый никнейм
        senderbio (ForumBioEditor): Экземпляр класса ForumBioEditor
        sendernick (ForumNickEditor): Экземпляр класса ForumNickEditor
    """
    loop = 0
    while True:
        animate(delay)
        clear_animation()
        resultbio = await senderbio.send_bio_request(id, choice)
        resultnick = await sendernick.send_nick_request(id, nickname)
        loop += 1
        await asyncio.sleep(0.1)
        if not resultbio or not resultnick:
            logging.error(f"[2501] // Error acquired on loop {loop}...")
            break
        print(f"[2501] // Loop: {loop}")

async def main():
    """
    Основная функция для запуска программы
    """
    print("""
    ██▓███   ██▓   ▓██   ██▓       ▄▄▄       ██▓     ██▓ ▄▄▄▄   
    ▓██░  ██▒▓██▒    ▒██  ██▒      ▒████▄    ▓██▒    ▓██▒▓█████▄ 
    ▓██░ ██▓▒▒██░     ▒██ ██░      ▒██  ▀█▄  ▒██░    ▒██▒▒██▒ ▄██
    ▒██▄█▓▒ ▒▒██░     ░ ▐██▓░      ░██▄▄▄▄██ ▒██░    ░██░▒██░█▀  
    ▒██▒ ░  ░░██████▒ ░ ██▒▓░       ▓█   ▓██▒░██████▒░██░░▓█  ▀█▓
    ▒▓▒░ ░  ░░ ▒░▓  ░  ██▒▒▒        ▒▒   ▓▒█░░ ▒░▓  ░░▓  ░▒▓███▀▒
    ░▒ ░     ░ ░ ▒  ░▓██ ░▒░         ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░▒░▒   ░ 
    ░░         ░ ░   ▒ ▒ ░░          ░   ▒     ░ ░    ▒ ░ ░    ░ 
             ░  ░░ ░                 ░  ░    ░  ░ ░   ░      
                 ░ ░                                       ░ 
""")
    await asyncio.sleep(0.1)
    yn = str(input('[2501] // Debug mode? [y/n]: '))
    user_id = int(input('[2501] // Enter a ID of user: '))
    biochoice = str(input('[Bio] // Enter your choice (1 for random fact, 2 for random phrase, 3 for everytime random): '))
    nickname = str(input('[Nick] // Enter a nickname: '))
    delay = int(input('[2501] // Enter a delay (in seconds): '))
    debug = True if yn.lower() == 'y' else False
    if debug: logging.debug(f'[2501] // Debug mode: {str(debug)}')
    await asyncio.sleep(0.1)
    senderbio = ForumBioEditor(debug=debug)
    sendernick = ForumNickEditor(debug=debug)
    await Run(user_id, delay, nickname, biochoice, senderbio, sendernick)

if __name__ == "__main__":
    asyncio.run(main())