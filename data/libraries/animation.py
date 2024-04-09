import time
import sys

def animate(repeat_count):
    for _ in range(repeat_count):
        for char in ['|', '/', '—', '\\']:
            sys.stdout.write(f'\r[2501] // Delay: {char}')
            sys.stdout.flush()
            time.sleep(0.3)

def clear_animation():
    sys.stdout.write('\r')
    sys.stdout.flush()

if __name__ == "__main__":
    repeat_count = 3
    animate(repeat_count)
    clear_animation()
