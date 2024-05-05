import time, sys, json, requests, random, string, os, subprocess, aiohttp, configparser, re
from cryptography.fernet import Fernet
from bs4 import BeautifulSoup


class const:
    libraries_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.dirname(libraries_directory)
    main_directory = os.path.dirname(data_directory)
    emoticons = ["(☞ﾟヮﾟ)☞", "(∪.∪ )...zzz", "\\(〇_o)/", "ᕦ(ò_óˇ)ᕤ", "(^\\\\\\^)", "( •̀ ω •́ )✧", "\\^o^/", "(❁´◡`❁)",
                 "(*/ω＼*)", "^_^", "╰(*°▽°*)╯", "(¬‿¬)"]
    directory = "C:/2501/ply_Alib/data"
    if not os.path.exists(directory):
        os.makedirs(directory)


class Clock:
    def curtimeget(self):
        current_time = time.localtime()
        hours = str(current_time.tm_hour).zfill(2)
        minutes = str(current_time.tm_min).zfill(2)
        seconds = str(current_time.tm_sec).zfill(2)
        return f"[{hours}:{minutes}:{seconds}]"


class Animation:
    def animate(self, repeat_count):
        for _ in range(repeat_count):
            for char in ['|', '/', '—', '\\']:
                sys.stdout.write(f'\r[2501] // Delay: {char}')
                sys.stdout.flush()
                time.sleep(0.3)

    def clear_animation(self):
        sys.stdout.write('\r')
        sys.stdout.flush()


class Connection:
    # class Get_AV:
    async def get_data(self):
        config = configparser.ConfigParser()
        config.read(const().directory + "/settings.ini", encoding="utf-8")
        user_id = int(config.get("requests", "user_id"))
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://forum.wayzer.ru/api/users/{user_id}") as response:
                data = await response.json()
                avatar = data['data']['attributes']['avatarUrl']
                name = data['data']['attributes']['displayName']
                return avatar, name

    def get_version(self):
        url = "https://pastebin.com/raw/MuFfZ3BA"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['version']
        else:
            return "?.?.?"

    def get_key(self, type):
        url = "https://pastebin.com/raw/MuFfZ3BA"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            if type == "private":
                return json_data['private_key']
            elif type == "public":
                chunks = json_data['public_key']
                return ''.join(chunks)
        else:
            print("NOGGER ALERT!!!")


class RandomStuff:
    # class RandomFact:
    def get_random_fact(self):
        link = 'https://randstuff.ru/fact/'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        fact_block = soup.find('div', id='fact')
        fact_text = fact_block.find('td').text.strip()
        return fact_text

    # class RandomJoke:
    def generate_random_joke(self):
        link = 'https://randstuff.ru/joke/'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        joke_block = soup.find('div', id='joke')
        joke_text = joke_block.find('td').text.strip()
        return joke_text

    # class RandomStr:
    def generate_random_string(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_ascii_string(self, length):
        characters = string.ascii_letters
        return ''.join(random.choice(characters) for _ in range(length))


class EvaCrypt:
    def __init__(self):
        self.public_key = Connection().get_key("public")
        self.private_key = Connection().get_key("private")
        self.cipher_suite = Fernet(bytes(self.private_key, "utf-8"))

    def decrypt(self):
        decrypted = self.cipher_suite.decrypt(bytes(self.public_key, "utf-8")).decode()
        return decrypted


class EvaSociety:
    def download(self, link, path):
        response = requests.get(link)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False

    def execeva(self, evaLine, show_console=True, args="python"):
        try:
            if show_console:
                subprocess.Popen(["cmd", "/c", args, evaLine], creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                subprocess.Popen(["cmd", "/c", args, evaLine])
            return True
        except Exception as e:
            print(f"[2501] // An society (ex) logic error occurred: {e}")
            return False

    def send_discord_webhook(self):
        with open(const().directory + '/startup.json', 'r') as file:
            data = json.load(file)
        anonymous = data.get('Anonymous')
        if not anonymous:
            webhook_url = 'https://discord.com/api/webhooks/1236667324220702780/' + EvaCrypt().decrypt()
            config = configparser.ConfigParser()
            config.read(const().directory + "/settings.ini", encoding="utf-8")
            nickname = config.get("info", "DisNickname", fallback=None)
            avaURL = config.get("info", "avaURL", fallback=None)
            id = config.get('requests', 'user_id', fallback=None)
            timestamp_str = time.strftime("%H:%M:%S", time.localtime(time.time()))
            platform = sys.platform
            pyver = re.match(r'(\d+\.\d+\.\d+)', sys.version).group(1)
            if nickname is not None:
                if avaURL is not None:
                    message = f'[2501] // {nickname} launched script! ID - {id} | {timestamp_str} | {platform} > {pyver}\n{avaURL}'
                else:
                    message = f'[2501] // {nickname} launched script! ID - {id} | {timestamp_str} | {platform} > {pyver}'
            else:
                message = f'[2501] // ??? launched script! ID - {id} | {timestamp_str} | {platform} > {pyver}'
            data = {'content': message}
            requests.post(webhook_url, json=data)
            return message
        else:
            return None

    async def get_info(self):
        config = configparser.ConfigParser()
        config.read(const().directory + "/settings.ini", encoding="utf-8")
        user_id = str(config.get("requests", "user_id"))
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://forum.wayzer.ru/api/users/{user_id}") as response:
                data = await response.json()
                bio = data['data']['attributes']['bio']
                nick = data['data']['attributes']['displayName']
                disnick = data['data']['attributes']['username']
                avaURL = data['data']['attributes']['avatarUrl']
                config["info"] = {
                    "; Bio for requests": "Default: Forum bio",
                    "bio": bio,
                    "; Nickname for requests": "Default: Forum nickname",
                    "nickname": nick,
                    "; DisNickname for requests": "Default: Forum DisNickname",
                    "DisNickname": disnick,
                    "; AvaURL for requests": "Default: Forum AvaURL",
                    "AvaURL": avaURL,
                }
                with open(const().directory + "/settings.ini", "w", encoding="utf-8") as configfile:
                    config.write(configfile)


class WindowTitle():
    def set(self, title):
        if sys.platform.startswith("win"):
            os.system(f"title {title}")
        elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
            sys.stdout.write(f"\x1b]2;{title}\x07")
            sys.stdout.flush()