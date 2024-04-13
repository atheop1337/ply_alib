import tkinter as tk
from tkinter import messagebox, ttk
import json
import re
import os
import sys

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Программа для обработки cURL")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure('TButton', foreground='white', background='#2E2E2E', bordercolor='#555', lightcolor='#2E2E2E', darkcolor='#2E2E2E', highlightbackground='#2E2E2E', highlightcolor='#2E2E2E', highlightthickness=0)
        self.style.map('TButton', background=[('active', '#ffffff')], foreground=[('active', '#2E2E2E')])
        self.style.configure('TLabel', foreground='white', background='#2E2E2E')
        self.style.configure('TFrame', background='#2E2E2E')
        self.create_widgets()
        self.disable_resizing()

    def create_widgets(self):
        mainframe = ttk.Frame(self.root, padding="50")
        mainframe.pack()

        self.curl_label = ttk.Label(mainframe, text="Введите cURL на отправку сообщения:")
        self.curl_label.grid(row=0, column=0, sticky="w", padx=47, pady=5)

        self.curl_entry = tk.Entry(mainframe, width=50)
        self.curl_entry.grid(row=1, column=0, sticky="ew")

        self.clear_button = ttk.Button(mainframe, text="Очистить", command=self.clear_entry)
        self.clear_button.grid(row=2, column=0, sticky="e", padx=65, pady=5)

        self.paste_button = ttk.Button(mainframe, text="Вставить", command=self.paste_from_clipboard)
        self.paste_button.grid(row=2, column=0, sticky="w", padx=65, pady=5)

        self.confirm_button = ttk.Button(mainframe, text="Подтвердить", command=self.process_curl, width=20)
        self.confirm_button.grid(row=3, column=0, sticky="ew", pady=5)

        # Добавление консоли
        self.console_frame = ttk.Frame(self.root, padding="10")
        self.console_frame.pack(fill="both", expand=True)
        self.console = ConsoleWindow(self.console_frame)

    def clear_entry(self):
        self.curl_entry.delete(0, tk.END)

    def paste_from_clipboard(self):
        clipboard_text = self.root.clipboard_get()
        self.curl_entry.insert(tk.END, clipboard_text)

    def process_curl(self):
        curl_string = self.curl_entry.get()
        headers, cookies = parse_curl(curl_string)
        filename = 'headers.json'
        save_to_json(headers, cookies, filename)
        messagebox.showinfo("Готово", f"Данные успешно сохранены в файл C:/2501/ply_Alib/data/{filename}")

    def disable_resizing(self):
        self.root.resizable(width=False, height=False)
        self.root.attributes("-fullscreen", False)
        self.root.bind("<F11>", self.disable_fullscreen)
        self.root.bind("<Escape>", self.disable_fullscreen)

    def disable_fullscreen(self, event):
        event.widget.attributes("-fullscreen", False)

class ConsoleWindow:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self.root, wrap="word", state="disabled")
        self.text_area.pack(fill="both", expand=True)

        # Включение прокрутки для текстового поля
        scroll = ttk.Scrollbar(self.root, orient="vertical", command=self.text_area.yview)
        scroll.pack(side="right", fill="y")
        self.text_area.configure(yscrollcommand=scroll.set)

        # Перенаправление стандартного вывода в текстовое поле
        self.original_stdout = sys.stdout
        sys.stdout = TextRedirector(self.text_area)

class TextRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str):
        self.text_widget.configure(state="normal")
        self.text_widget.insert("end", str)
        self.text_widget.see("end")  # Прокрутка к концу текста
        self.text_widget.configure(state="disabled")

    def flush(self):
        pass

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

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
