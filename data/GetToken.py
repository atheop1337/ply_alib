import tkinter as tk
from tkinter import messagebox
import json
import re
import os

def parse_curl(curl_string):
    headers = {}
    cookies = {}

    headers_pattern = re.compile(r'(?<=-H ")[^"]+')
    cookies_pattern = re.compile(r'(?<=-H "Cookie: )([^"]+)')
    header_matches = headers_pattern.findall(curl_string)
    cookies_match = cookies_pattern.findall(curl_string)

    for header in header_matches:
        key, value = header.split(': ')
        headers[key] = value

    cookies_list = cookies_match[0].split('; ')
    for cookie in cookies_list:
        key, value = cookie.split('=')
        cookies[key] = value

    return headers, cookies

def save_to_json(headers, cookies, filename):
    data_to_save = {
        "CSRF": headers.get("X-CSRF-Token", ""),
        "flarum": "flarum_remember=" + cookies.get("flarum_remember", "") + "; flarum_session=" + cookies.get("flarum_session", "")
    }

    directory = "C:/2501/ply_Alib/data"
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, filename)

    with open(file_path, 'w') as file:
        json.dump(data_to_save, file, indent=4)

    return file_path

def process_curl():
    curl_string = curl_entry.get()

    headers, cookies = parse_curl(curl_string)

    filename = 'headers.json'
    save_to_json(headers, cookies, filename)

    messagebox.showinfo("Готово", f"Данные успешно сохранены в файл C:/2501/ply_Alib/data/{filename}")

def paste_from_clipboard():
    clipboard_text = root.clipboard_get()
    curl_entry.insert(tk.END, clipboard_text)

root = tk.Tk()
root.title("Программа для обработки cURL")

curl_label = tk.Label(root, text="Введите cURL строку:")
curl_label.pack()

curl_entry = tk.Entry(root, width=50)
curl_entry.pack()

paste_button = tk.Button(root, text="Вставить из буфера обмена", command=paste_from_clipboard)
paste_button.pack()

confirm_button = tk.Button(root, text="Подтвердить", command=process_curl)
confirm_button.pack()

root.mainloop()
