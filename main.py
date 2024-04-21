import asyncio
import logging
import aiohttp
import random
import inquirer
import json
import os
import sys
import signal
import time
import configparser
from colorama import init, Fore, Style
from data.libraries.forumEditor import ForumEditor
from data.libraries.twentyfivezeroone import Clock, Animation, RandomStuff, Connection, EvaSociety, const, WindowTitle
init(autoreset=True)
logging.basicConfig(format=f'{Fore.RESET}{Style.DIM}[%(asctime)s] %(levelname)s |   {Fore.RED}%(message)s', datefmt='%H:%M:%S')

def signal_handler(sig, frame):
    print(f"\n{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Navigate back signal received...")
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Cleaning up...")
    time.sleep(0.5)
    file_path = os.path.join(const().directory, "encrypted.json")
    with open(file_path, 'w') as json_file:
        json.dump(f'{RandomStuff().generate_ascii_string(128)}&T', json_file)
    EvaSociety().execeva(f'{const().main_directory}/step.py', False)
    sys.exit(0)

class ForumBioEditor(ForumEditor):
    async def send_bio_request(self, id, choice):
        try:
            with open(const().directory + "/quotes.json", "r", encoding="utf-8") as file:
                quotes = json.load(file)
        except FileNotFoundError:
            logging.error(f"{Fore.RESET}{Style.DIM}[Bio] // {Fore.RED}File quotes.json not found! Try to run the setup proccess again")
            signal_handler(None, None)
            return

        random_phrase = random.choice(const().emoticons)
        random_quote = random.choice(quotes)
        choice_options = {
            'random fact': RandomStuff().get_random_fact(),
            'random emoticone': random_phrase,
            'random quote': random_quote,
            'random joke': RandomStuff().generate_random_joke(),
        }

        if choice == 'everytime random':
            choice = random.choice(list(choice_options.keys()))

        choice_value = choice_options.get(choice)
        if choice_value is not None:
            data = {
                "data": {
                    "type": "users",
                    "attributes": {
                        "bio": f"Powered by 2501\n{choice_value}"
                    },
                    "id": str(id)
                }
            }
            return await self.send_request(id, data)


class ForumNickEditor(ForumEditor):
    async def send_nick_request(self, id, nickname, choice):
        random_phrase = random.choice(const().emoticons)
        random_emoji = chr(random.randint(0x1F600, 0x1F64F))
        choice_options = {
            'clock': Clock().curtimeget(),
            'random emoticone': random_phrase,
            'random emoji': random_emoji,
            'random name': RandomStuff().generate_random_name(),
            'random string': RandomStuff().generate_random_string(60),
        }
        choice_value = choice_options.get(choice)
        if choice_value is not None:
            if choice == 'random name' or choice == 'random string':
                nickname_value = choice_value
            else:
                nickname_value = f'{nickname}\n {choice_value}'

            data = {
                "data": {
                    "type": "users",
                    "attributes": {
                        "nickname": nickname_value
                    },
                    "id": str(id)
                }
            }
            return await self.send_request(id, data)


async def Run(id, delay, nickname, biochoice, nickchoice, senderbio, sendernick):
    loop = 0
    while True:
        Animation().animate(delay)
        Animation().clear_animation()
        resultbio = await senderbio.send_bio_request(id, biochoice)
        resultnick = await sendernick.send_nick_request(id, nickname, nickchoice)
        await asyncio.sleep(0.1)
        loop = loop + 1
        if not resultbio or not resultnick:
            logging.error(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.RED}An error occurred on loop {loop}...")
            signal_handler(None, None)
            break
        print(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.YELLOW}Loop: {loop}")

async def get_bio(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://forum.wayzer.ru/api/users/{id}") as response:
            data = await response.json()
            bio = data['data']['attributes']['bio']
            return bio

async def main():
    signal.signal(signal.SIGINT, signal_handler)
    current_version = "3.2"
    config = configparser.ConfigParser()
    config.read(const().directory + "/settings.ini")
    nickname = str(config.get("nickname", "nickname"))
    user_id = str(config.get("requests", "user_id"))
    if current_version != Connection().get_version():
        print(f"{Fore.RESET}{Style.DIM} [2501] // {Fore.YELLOW}Script version: {current_version}\nSystem version: {Connection().get_version()}\nPlease update to the latest version.")
        signal_handler(None, None)
        return
    WindowTitle().set(f"ply_Alib   //   {current_version}")
    print(f"""{Fore.LIGHTWHITE_EX}{Style.DIM}
┌──────────────────┬────────────────────────────────────────────────────────────┐
│  {Fore.RESET}[BETA] ply_Alib   {Fore.RESET}v{Connection().get_version()}{Fore.YELLOW}                                                       {Fore.LIGHTWHITE_EX}│
├──────────────────┴────────────────────────────────────────────────────────────┤
│                                                                               │
│{Fore.YELLOW}         ██▓███   ██▓   ▓██   ██▓       ▄▄▄       ██▓     ██▓ ▄▄▄▄             {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▓██░  ██▒▓██▒    ▒██  ██▒      ▒████▄    ▓██▒    ▓██▒▓█████▄          {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▓██░ ██▓▒▒██░     ▒██ ██░      ▒██  ▀█▄  ▒██░    ▒██▒▒██▒ ▄██         {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▒██▄█▓▒ ▒▒██░     ░ ▐██▓░      ░██▄▄▄▄██ ▒██░    ░██░▒██░█▀           {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▒██▒ ░  ░░██████▒ ░ ██▒▓░       ▓█   ▓██▒░██████▒░██░░▓█  ▀█▓         {Fore.LIGHTWHITE_EX}│    
│{Fore.YELLOW}         ▒▓▒░ ░  ░░ ▒░▓  ░  ██▒▒▒        ▒▒   ▓▒█░░ ▒░▓  ░░▓  ░▒▓███▀▒         {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ░▒ ░     ░ ░ ▒  ░▓██ ░▒░         ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░▒░▒   ░          {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ░░         ░ ░   ▒ ▒ ░░          ░   ▒     ░ ░    ▒ ░ ░    ░          {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}                  ░  ░░ ░                 ░  ░    ░  ░ ░   ░                   {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}                      ░ ░                                       ░              {Fore.LIGHTWHITE_EX}│
│                                                                               │
│  {Fore.RESET}[•]   {Fore.GREEN}Welcome to the ply_Alib script!                                        {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[!]   {Fore.GREEN}You confirm that you have read and accept the 2501 terms of use.       {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[@]   {Fore.RED}Closing the terminal window is NOT SAFE!                               {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[@]   {Fore.RED}To navigate back to the hub(or exit), please use {Fore.RESET}CTRL+C{Fore.RED}.               {Fore.LIGHTWHITE_EX}│
└───────────────────────────────────────────────────────────────────────────────┘
""")
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    logging.getLogger().setLevel(logging.DEBUG)
    await asyncio.sleep(0.1)
    try:
        delay = int(input(f'{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter a delay (in seconds){Fore.RESET}: '))
        nickchoice = inquirer.list_input(f"{Fore.RESET}{Style.DIM}[Nick] // {Fore.GREEN}Enter your choice{Fore.RESET}", choices=['clock', 'random emoticone', 'random emoji', 'random name', 'random string'])
        biochoice = inquirer.list_input(f"{Fore.RESET}{Style.DIM}[Bio] // {Fore.GREEN}Enter your choice{Fore.RESET}",choices=['random fact', 'random emoticone', 'random quote', 'random joke', 'everytime random'])
    except KeyboardInterrupt:
        signal_handler(None, None)
    if nickname.lower() == 'skibidi':
        urls = ['https://youtu.be/6dMjCa0nqK0', 'https://ru.wikipedia.org/wiki/Skibidi_Toilet']
        for url in urls:
            EvaSociety().execeva(url, False, "start")
        for i in range(1, 101):
            print(f'{Fore.RED}SKIBIDI DOP DOP DOP ES ES{Fore.RESET}')
            await asyncio.sleep(0.1)
        return
    if delay == 1337 or delay == 228:
        for i in range(1, 101):
            print(f'{Fore.RED}ELITE 228 1337{Fore.RESET}')
            await asyncio.sleep(0.1)
        return
    #logging.debug(f'{Fore.RESET}{Style.DIM}[Bio] // {Fore.GREEN}User started bio{Fore.RESET}:\n{user_bio}')
    await asyncio.sleep(0.1)
    senderbio = ForumBioEditor()
    sendernick = ForumNickEditor()
    await Run(user_id, delay, nickname, biochoice, nickchoice, senderbio, sendernick)


if __name__ == "__main__":
    asyncio.run(main())