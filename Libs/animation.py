import sys
import time
import random

def animate(repeat_count):
    colors = [31, 32, 33, 34, 35, 36]  # Цвета
    for _ in range(repeat_count):  # Repeat the animation specified number of times
        for char in ['/', '|', '\\', '-']:
            color_code = random.choice(colors)  # Pick a random color code
            # ANSI escape sequence for changing text color and moving cursor to the beginning
            sys.stdout.write(f'\r\033[1;{color_code}m{char}\033[0m')
            sys.stdout.flush()
            time.sleep(0.3)  # Animation delay

def clear_animation():
    sys.stdout.write('\r')  # Clear animation from the console
    sys.stdout.flush()

# Define the number of times the animation should repeat
repeat_count = None  # Кол-во повторений


