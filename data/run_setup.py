import inquirer
import time
import os
import signal
import sys
from libraries.twentyfivezeroone import WindowTitle, EvaSociety, const
from colorama import Fore, Style, init
init(autoreset=True)

def signal_handler(sig, frame):
    print(f"\n{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Navigate back signal received...")
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Cleaning up...")
    time.sleep(0.5)
    EvaSociety().execeva(f'{const().main_directory}/step.py', False)
    sys.exit(0)

def quote_req():
    EvaSociety().execeva(f'{const().libraries_directory}/quotes_generate.py', False)
def nick_req():
    EvaSociety().execeva(f'{const().libraries_directory}/nicknames_generate.py', False)
def settings_req():
    print(f'\n{Fore.RED}THIS FUNCTION IS UNDER CONSTRUCT!')
    EvaSociety().execeva(f'{const().libraries_directory}/settings_setup.py', False)

def token_req():
    EvaSociety().execeva(f'{const().data_directory}/GetToken.py', False)
    time.sleep(1)
    EvaSociety().execeva(f'{const().data_directory}/run_setup.py', False)
    sys.exit(0)

def list_input(choice):
    choice_options = {
        '[!] token&cookies': token_req,
        '[!] settings': settings_req,
        '[!] quotes': quote_req,
        '[!] nicks': nick_req
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
            '[!] nicks',
        ])
        list_input(choice)
    except KeyboardInterrupt:
        signal_handler(None, None)



if __name__ == '__main__':
    main()