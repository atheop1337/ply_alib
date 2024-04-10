import asyncio
import logging
import aiohttp
import random
import inquirer
import json
from colorama import init, Fore, Style
from data.libraries.forumEditor import ForumEditor
from data.libraries.twentyfivezeroone import Clock, Animation, RandomFact
init(autoreset=True)

logging.basicConfig(format='[%(asctime)s] %(levelname)s |   %(message)s', datefmt='%H:%M:%S')
phrases = ["(☞ﾟヮﾟ)☞", "(∪.∪ )...zzz", "\\(〇_o)/", "ᕦ(ò_óˇ)ᕤ", "(^\\\\\\^)", "( •̀ ω •́ )✧", "\\^o^/",
                   "(❁´◡`❁)", "(*/ω＼*)", "^_^", "╰(*°▽°*)╯", "(¬‿¬)"] #const
directory = "C:/2501/ply_Alib/data" #const

class ForumBioEditor(ForumEditor):
    async def send_bio_request(self, id, choice, user_bio_static):
        try:
            with open(directory + "/quotes.json", "r", encoding="utf-8") as file:
                quotes = json.load(file)
        except FileNotFoundError:
            logging.error("[Bio] // File quotes.json not found! Try to run the setup.py again")
            return

        random_phrase = random.choice(phrases)
        random_quote = random.choice(quotes)
        choice_options = {
            'random fact': RandomFact().get_random_fact(),
            'random emoticone': random_phrase,
            'random quote': random_quote,
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
        random_phrase = random.choice(phrases)
        random_emoji = chr(random.randint(0x1F600, 0x1F64F))
        choice_options = {
            'clock': Clock().curtimeget(),
            'random emoticone': random_phrase,
            'random emoji': random_emoji,
        }
        choice_value = choice_options.get(choice)
        if choice_value is not None:
            data = {
                "data": {
                    "type": "users",
                    "attributes": {
                        "nickname": f"{nickname}\n{choice_value}"
                    },
                    "id": str(id)
                }
            }
            return await self.send_request(id, data)

async def Run(id, delay, nickname, biochoice, nickchoice, user_bio, senderbio, sendernick):
    loop = 0
    user_bio_static = user_bio
    while True:
        Animation().animate(delay)
        Animation().clear_animation()
        resultbio = await senderbio.send_bio_request(id, biochoice, user_bio_static)
        resultnick = await sendernick.send_nick_request(id, nickname, nickchoice)
        await asyncio.sleep(0.1)
        loop = loop + 1
        if not resultbio or not resultnick:
            logging.error(f"[2501] // Error acquired on loop {loop}...")
            break
        print(f"[2501] // Loop: {loop}")

async def fetch_data():
    url = "https://pastebin.com/raw/vdfxN6bp"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                return '?.?.?' #relocate to twentyfivezeroone

async def get_bio(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://forum.wayzer.ru/api/users/{id}") as response:
            data = await response.json()
            bio = data['data']['attributes']['bio']
            return bio
async def main():

    print(f"""{Fore.LIGHTWHITE_EX}{Style.DIM}
┌──────────────────┬────────────────────────────────────────────────────┬───────┐
│  {Fore.RESET}[BETA] ply_Alib   {Fore.RESET}v{await fetch_data()}{Fore.YELLOW}                                             {Fore.LIGHTWHITE_EX}│   {Fore.LIGHTRED_EX}x   {Fore.LIGHTWHITE_EX}│
├──────────────────┴────────────────────────────────────────────────────┴───────┤
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
│  {Fore.RESET}•  {Fore.GREEN}Welcome to the ply_Alib script, press {Fore.RESET}CTRL+C {Fore.GREEN}to exit the program          {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}•  {Fore.GREEN}if you have any questions, please contact the 2501 for help               {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}•  {Fore.GREEN}turn on debug mode for debugging purposes...                              {Fore.LIGHTWHITE_EX}│
└───────────────────────────────────────────────────────────────────────────────┘
""")
    await asyncio.sleep(0.1)
    yn = str(input('[2501] // Debug mode? [y/n]: '))
    user_id = int(input('[2501] // Enter a ID of user: '))
    delay = int(input('[2501] // Enter a delay (in seconds): '))
    user_bio = await get_bio(user_id)
    nickname = str(input('[Nick] // Enter a nickname: '))
    nickchoice = inquirer.list_input("[Nick] // Enter your choice", choices=['clock', 'random emoticone', 'random emoji'])
    biochoice = inquirer.list_input("[Bio] // Enter your choice",choices=['random fact', 'random emoticone', 'random quote', 'everytime random'])
    debug = True if yn.lower() == 'y' else False
    skibidi = True if nickname.lower() == 'skibidi' else False
    if debug: logging.debug(f'[2501] // Debug mode: {str(debug)}')
    if skibidi:
        for i in range(1, 101):
            print(f'SKIBIDI DOP DOP DOP ES ES')
            await asyncio.sleep(0.1)
        return
    logging.getLogger().setLevel(logging.DEBUG if debug else logging.INFO)
    logging.debug(f'User started bio:{user_bio}')
    await asyncio.sleep(0.1)
    senderbio = ForumBioEditor(debug=debug)
    sendernick = ForumNickEditor(debug=debug)
    await Run(user_id, delay, nickname, biochoice, nickchoice, user_bio, senderbio, sendernick)


if __name__ == "__main__":
    asyncio.run(main())