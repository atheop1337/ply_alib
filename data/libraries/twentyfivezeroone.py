import time
import sys
import requests
from bs4 import BeautifulSoup

class Clock:
    def curtimeget(self):
        current_time = time.localtime()
        hours = str(current_time.tm_hour).zfill(2)
        minutes = str(current_time.tm_min).zfill(2)
        seconds = str(current_time.tm_sec).zfill(2)
        return f"[{hours}:{minutes}:{seconds}]"

    def main(self):
        print(self.curtimeget())

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

    def main(self):
        random_fact = self.get_random_fact()
        print(random_fact)

class GetVersion:
    def fetch_data(self):
        response = requests.get("https://pastebin.com/raw/vdfxN6bp")
        if response.status_code == 200:
            return response.text
        else:
            return "?.?.?"

if __name__ == '__main__':
    clock = Clock()
    clock.main()

    animation = Animation()
    repeat_count = 3
    animation.animate(repeat_count)
    animation.clear_animation()

    random_fact = RandomFact()
    random_fact.main()