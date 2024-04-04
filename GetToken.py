import tkinter as tk
import pyperclip
import re

# ! SandjezJ banned in gamesense.pub !

def extract_tokens(curl_command):
    browser_check = "Firefox" in curl_command
    csrf_token_pattern = r'-H "X-CSRF-Token: ([^"]+)"'
    csrf_token_match = re.search(csrf_token_pattern, curl_command)
    cookie_pattern = r'-H "Cookie: ([^"]+)"'
    cookie_match = re.search(cookie_pattern, curl_command)

    if browser_check and csrf_token_match and cookie_match:
        csrf_token = csrf_token_match.group(1)
        cookie = cookie_match.group(1)

        csrf_token_label.config(text=f'X-CSRF-Token: {csrf_token}')
        cookie_label.config(text=f'Cookie: {cookie}')
        copy_csrf_button.config(state=tk.NORMAL, command=lambda: copy_to_clipboard(csrf_token))
        copy_cookie_button.config(state=tk.NORMAL, command=lambda: copy_to_clipboard(cookie))
    else:
        csrf_token_label.config(text='Не удалось извлечь X-CSRF-Token или Cookie из строки cURL для браузера Firefox.')
        cookie_label.config(text='')
        copy_csrf_button.config(state=tk.DISABLED)
        copy_cookie_button.config(state=tk.DISABLED)

def copy_to_clipboard(text):
    pyperclip.copy(text)

def paste_from_clipboard():
    curl_entry.insert(tk.END, pyperclip.paste())

def submit_command():
    curl_command = curl_entry.get()
    extract_tokens(curl_command)

root = tk.Tk()
root.title("Извлечение токенов из cURL")
root.geometry("600x200")

curl_label = tk.Label(root, text="Введите строку cURL (100% работает только на Firefox, на остальных браузерах не проверял):")
curl_label.pack()

curl_entry = tk.Entry(root, width=50)
curl_entry.pack()

submit_button = tk.Button(root, text="Извлечь токены", command=submit_command)
submit_button.pack()

csrf_token_label = tk.Label(root, text="")
csrf_token_label.pack()

copy_csrf_button = tk.Button(root, text="Копировать CSRF", state=tk.DISABLED)
copy_csrf_button.pack()

cookie_label = tk.Label(root, text="")
cookie_label.pack()

copy_cookie_button = tk.Button(root, text="Копировать Cookie", state=tk.DISABLED)
copy_cookie_button.pack()

# Стартуем!!!
root.mainloop()
