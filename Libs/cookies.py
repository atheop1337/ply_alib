import json
import requests
import shlex
import os
import tkinter as tk
from tkinter import ttk

class CurlExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("cURL Extractor")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Настройка цветов
        self.style.configure('TButton', foreground='white', background='#2E2E2E', bordercolor='#555', lightcolor='#2E2E2E', darkcolor='#2E2E2E', highlightbackground='#2E2E2E', highlightcolor='#2E2E2E', highlightthickness=0)
        self.style.map('TButton', background=[('active', '#555')])
        self.style.configure('TLabel', foreground='white', background='#2E2E2E')
        self.style.configure('TFrame', background='#2E2E2E')

        self.mainframe = ttk.Frame(root, padding="20")
        self.mainframe.grid(row=0, column=0)

        self.url_label = ttk.Label(self.mainframe, text="Введите cURL на отправку сообщения:")
        self.url_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.curl_text = tk.Text(self.mainframe, height=5, width=50, bg="#4D4D4D", fg="white")
        self.curl_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.extract_button = ttk.Button(self.mainframe, width=60, text="Извлечь", command=self.extract_headers)
        self.extract_button.grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)

        self.cookies_label = ttk.Label(self.mainframe, text="Cookies:")
        self.cookies_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

        self.cookies_text = tk.Text(self.mainframe, height=5, width=50, bg="#4D4D4D", fg="white")
        self.cookies_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.token_label = ttk.Label(self.mainframe, text="Token:")
        self.token_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)

        self.token_text = tk.Text(self.mainframe, height=1, width=50, bg="#4D4D4D", fg="white")
        self.token_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.extracted_json_label = ttk.Label(self.mainframe, text="Извлеченные данные сохранены в файле 'headers.json'")
        self.extracted_json_label.grid(row=7, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)
        self.extracted_json_label.grid_remove()

    def extract_headers(self):
        curl_url = self.curl_text.get("1.0", tk.END).strip()
        cookies, token = extract_headers_from_curl(curl_url)
        flarum_remember = extract_flarum_remember_from_curl(curl_url)
        json_file_path = os.path.join(os.path.dirname(__file__), 'headers.json')
        create_json_file(cookies, token, flarum_remember, json_file_path)

        self.cookies_text.delete("1.0", tk.END)
        self.cookies_text.insert(tk.END, cookies + "\n" + "flarum_remember=" + flarum_remember)

        self.token_text.delete("1.0", tk.END)
        self.token_text.insert(tk.END, token)

        self.extracted_json_label.grid()  # Показать метку после успешного извлечения данных

def extract_headers_from_curl(curl_url):
    url = extract_url_from_curl(curl_url)
    response = requests.get(url, timeout=10)
    headers = response.headers
    cookies_raw = headers.get('Set-Cookie')
    cookies = extract_cookies(cookies_raw)
    token = headers.get('X-CSRF-Token')
    return cookies, token

def extract_cookies(cookies_raw):
    cookies_list = cookies_raw.split('; ')
    filtered_cookies = [cookie for cookie in cookies_list if 'flarum_session=' in cookie]
    return '; '.join(filtered_cookies)

def extract_flarum_remember_from_curl(curl_command):
    tokens = shlex.split(curl_command)
    for i in range(len(tokens)):
        if tokens[i] == "-H" and "cookie:" in tokens[i+1]:
            cookie_part = tokens[i+1].split("cookie:")[1].strip()
            cookies = cookie_part.split(";")
            for cookie in cookies:
                if cookie.strip().startswith("flarum_remember="):
                    return cookie.strip().split("=")[1]
    return None

def extract_url_from_curl(curl_command):
    tokens = shlex.split(curl_command)
    url_index = tokens.index("curl") + 1
    return tokens[url_index]

def create_json_file(cookies, token, flarum_remember, file_path):
    data = {
        "Cookies": "; ".join([cookies, "flarum_remember=" + flarum_remember]),
        "Token": token,
    }
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = CurlExtractorGUI(root)
    root.mainloop()
