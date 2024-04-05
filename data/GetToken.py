import tkinter as tk
from tkinter import messagebox
import json
import re
import os

def parse_curl(curl_string):
    headers = {}
    cookies = {}

    # Находим все заголовки и куки в строке cURL
    headers_pattern = re.compile(r'(?<=-H ")[^"]+')
    cookies_pattern = re.compile(r'(?<=-H "Cookie: )([^"]+)')
    header_matches = headers_pattern.findall(curl_string)
    cookies_match = cookies_pattern.findall(curl_string)

    # Извлекаем заголовки и их значения
    for header in header_matches:
        key, value = header.split(': ')
        headers[key] = value

    # Извлекаем куки и их значения
    cookies_list = cookies_match[0].split('; ')
    for cookie in cookies_list:
        key, value = cookie.split('=')
        cookies[key] = value

    return headers, cookies

def save_to_json(headers, cookies, filename):
    data_to_save = {
        "X-CSRF-Token": headers.get("X-CSRF-Token", ""),
        "Cookie": "flarum_remember=" + cookies.get("flarum_remember", "") + "; flarum_session=" + cookies.get("flarum_session", "")
    }

    with open(filename, 'w') as file:
        json.dump(data_to_save, file, indent=4)

def process_curl():
    curl_string = curl_entry.get()  # Получаем введенную строку cURL из поля ввода

    headers, cookies = parse_curl(curl_string)

    # Сохранение данных в файл headers.json
    current_directory = os.path.dirname(os.path.abspath(__file__))
    json_headers_file_path = os.path.join(current_directory, 'data/headers.json')
    save_to_json(headers, cookies, json_headers_file_path)

    messagebox.showinfo("Готово", f"Данные успешно сохранены в файл {json_headers_file_path}")

def paste_from_clipboard():
    clipboard_text = root.clipboard_get()
    curl_entry.insert(tk.END, clipboard_text)

# Создание главного окна
root = tk.Tk()
root.title("Программа для обработки cURL")

# Создание метки и поля ввода для cURL
curl_label = tk.Label(root, text="Введите cURL строку:")
curl_label.pack()

curl_entry = tk.Entry(root, width=50)
curl_entry.pack()

# Кнопка для вставки текста из буфера обмена
paste_button = tk.Button(root, text="Вставить из буфера обмена", command=paste_from_clipboard)
paste_button.pack()

# Создание кнопки для подтверждения ввода cURL
confirm_button = tk.Button(root, text="Подтвердить", command=process_curl)
confirm_button.pack()

# Запуск главного цикла обработки событий
root.mainloop()
