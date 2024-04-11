import time
import sys
import json
import requests
import random
import os
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
            'Виктория', 'Константин', 'Надежда'
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
#
if __name__ == '__main__':
    print(Connection().get_version())