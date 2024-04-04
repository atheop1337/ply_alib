import sys
import time
import random

def animate(repeat_count):
    colors = [31, 32, 33, 34, 35, 36]
    for _ in range(repeat_count):
        for char in ['/', '|', '\\', '-']:
            color_code = random.choice(colors)
            sys.stdout.write(f'\r\033[1;{color_code}m{char}\033[0m')
            sys.stdout.flush()
            time.sleep(0.3)

def clear_animation():
    sys.stdout.write('\r') # Убираем анимацию
    sys.stdout.flush()

repeat_count = None  # Кол-во повторений


