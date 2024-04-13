import inquirer
import time
import subprocess
import os
from colorama import Fore, Style, init
directory = "C:/2501/ply_Alib/data"
current_directory = os.path.dirname(os.path.abspath(__file__))
init(autoreset=True)

def run_file(file_path, show_console=True):
    if show_console:
        subprocess.Popen(["cmd", "/c", "python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen(["cmd", "/c", "python", file_path])
    return True

def all_in_one():
    print('THIS FUNCTION IS NOT AVAILABLE RIGHT NOW!\n\n\n\n')
    time.sleep(4)
    main()

def main_script():
    print('THIS FUNCTION IS NOT AVAILABLE RIGHT NOW!\n\n\n\n')
    time.sleep(4)
    main()

def plug():
    print('THIS FUNCTION IS NOT AVAILABLE RIGHT NOW!\n\n\n\n')
    time.sleep(4)
    main()

def quote_req():
    run_file(f'{current_directory}/data/libraries/generate_quote_jsontable.py', True)
    time.sleep(4)
    main()

def token_req():
    run_file(f'{current_directory}/data/GetToken.py', False)
    time.sleep(4)
    main()

def list_input(choice):
    choice_options = {
        '[!] all in one': all_in_one,
        '[•] main script': main_script,
        '[•] gpt': plug,
        '[•] someother shit': plug,
        '[!] setup(Token)': token_req,
        '[!] setup(Quotes)': quote_req,
    }
    chosen_function = choice_options.get(choice)
    if chosen_function is not None:
        chosen_function()


def main():
    print(f"""{Fore.LIGHTWHITE_EX}{Style.DIM}
┌──────────────────┬────────────────────────────────────────────────────────────┐
│     {Fore.RESET}ply_Alib       Launcher                                                   {Fore.LIGHTWHITE_EX}│
├──────────────────┴────────────────────────────────────────────────────────────┤
│                                                                               │
│{Fore.YELLOW}         ██▓███   ██▓   ▓██   ██▓       ▄▄▄       ██▓     ██▓ ▄▄▄▄             {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▓██░  ██▒▓██▒    ▒██  ██▒      ▒████▄    ▓██▒    ▓██▒▓█████▄          {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▓██░ ██▓▒▒██░     ▒██ ██░      ▒██  ▀█▄  ▒██░    ▒██▒▒██▒ ▄██         {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▒██▄█▓▒ ▒▒██░     ░ ▐██▓░      ░██▄▄▄▄██ ▒██░    ░██░▒██░█▀           {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▒██▒ ░  ░░██████▒ ░ ██▒▓░       ▓█   ▓██▒░██████▒░██░░▓█  ▀█▓         {Fore.LIGHTWHITE_EX}│    
│{Fore.YELLOW}         ▒▓▒░ ░  ░░ ▒░▓  ░  ██▒▒▒        ▒▒   ▓▒█░░ ▒░▓  ░░▓  ░▒▓███▀▒         {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ░▒ ░     ░ ░ ▒  ░▓██ ░▒░         ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░▒░▒   ░          {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ░░         ░ ░   ▒ ▒ ░░          ░   ▒     ░ ░    ▒ ░ ░    ░          {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}                  ░  ░░ ░                 ░  ░    ░  ░ ░   ░                   {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}                      ░ ░                                       ░              {Fore.LIGHTWHITE_EX}│
│                                                                               │
│  {Fore.RESET}[•]   {Fore.GREEN}Welcome to the ply_Alib script!                                        {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[!]   {Fore.GREEN}Choose your mode to open ply_Alib!                                     {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[!]   {Fore.RED}Closing the terminal window is NOT SAFE please use {Fore.RESET}CTRL+C{Fore.RED}.             {Fore.LIGHTWHITE_EX}│
└───────────────────────────────────────────────────────────────────────────────┘
""")
    time.sleep(0.2)
    choice = inquirer.list_input(f"{Fore.RESET}{Style.DIM}[2501]// {Fore.GREEN}Enter your choice{Fore.RESET}", choices=['[!] all in one', '[•] main script', '[•] gpt', '[•] someother shit', '[!] setup(Token)', '[!] setup(Quotes)'])
    list_input(choice)


if __name__ == '__main__':
    main()