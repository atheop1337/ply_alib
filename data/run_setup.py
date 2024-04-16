import inquirer
import time
import subprocess
import os
import signal
import sys
from libraries.twentyfivezeroone import WindowTitle, EvaSociety, const
from colorama import Fore, Style, init
init(autoreset=True)

def signal_handler(sig, frame):
    print(f"\n{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Shutdown signal received...")
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Cleaning up...")
    time.sleep(0.5)
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Thank you for being with us!")
    time.sleep(2)
    EvaSociety().execeva(f'{const().main_directory}/step.py', False)
    sys.exit(0)


def run_file(file_path, show_console=True):
    if show_console:
        subprocess.Popen(["cmd", "/c", "python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen(["cmd", "/c", "python", file_path])
    return True

def quote_req():
    run_file(f'{const().libraries_directory}/generate_quote_jsontable.py', False)

def settings_req():
    print(f'\n{Fore.RED}THIS FUNCTION IS UNDER CONSTRUCT!')
    run_file(f'{const().libraries_directory}/settings_setup.py', False)

def token_req():
    run_file(f'{const().data_directory}/GetToken.py', False)
    time.sleep(1)
    EvaSociety().execeva(f'{const().data_directory}/run_setup.py', False)
    sys.exit(0)

def list_input(choice):
    choice_options = {
        '[!] token&cookies': token_req,
        '[!] settings': settings_req,
        '[!] quotes': quote_req,
    }
    chosen_function = choice_options.get(choice)
    if chosen_function is not None:
        chosen_function()

def main():
    WindowTitle().set("ply_Alib   //   Setup")
    signal.signal(signal.SIGINT, signal_handler)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Fore.LIGHTWHITE_EX}{Style.DIM}
┌──────────────────┬────────────────────────────────────────────────────────────┐
│     {Fore.RESET}ply_Alib       Setup                                                      {Fore.LIGHTWHITE_EX}│
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
│  {Fore.RESET}[!]   {Fore.GREEN}Choose your mode to setup ply_Alib!                                    {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[@]   {Fore.RED}Closing the terminal window is NOT SAFE!                               {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[@]   {Fore.RED}To navigate back to the hub(or exit), please use {Fore.RESET}CTRL+C{Fore.RED}.               {Fore.LIGHTWHITE_EX}│
└───────────────────────────────────────────────────────────────────────────────┘
""")
    time.sleep(0.2)
    try:
        choice = inquirer.list_input(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter your choice{Fore.RESET}", choices=[
            '[!] token&cookies',
            '[!] settings',
            '[!] quotes',
        ])
        list_input(choice)
    except KeyboardInterrupt:
        signal_handler(None, None)



if __name__ == '__main__':
    main()