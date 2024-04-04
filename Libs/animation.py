import time
import random
from colorama import init, Fore, Style
import sys

init(autoreset=True)  # Инициализация colorama

def animate(repeat_count):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for _ in range(repeat_count):
        for char in ['/', '|', '\\', '-']:
            color = random.choice(colors)
            sys.stdout.write(f'\r{color}{char}{Style.RESET_ALL}')
            sys.stdout.flush()
            time.sleep(0.3)

def clear_animation():
    sys.stdout.write('\r')
    sys.stdout.flush()

if __name__ == "__main__":
    repeat_count = 3  # Количество повторений анимации
    animate(repeat_count)
    clear_animation()
