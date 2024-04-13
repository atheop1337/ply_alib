import inquirer
import sys
import time
from colorama import Fore, Style

def all_in_one():
    print('THIS FUNCTION IS NOT AVAILABLE RIGHT NOW!\n\n\n\n')
    time.sleep(2)
    main()

def main_script():
    print('THIS FUNCTION IS NOT AVAILABLE RIGHT NOW!\n\n\n\n')
    time.sleep(2)
    main()

def plug():
    print('THIS FUNCTION IS NOT AVAILABLE RIGHT NOW!\n\n\n\n')
    time.sleep(2)
    main()

def list_input(choice):
    choice_options = {
        '[!] all in one': all_in_one(),
        '[•] main script': main_script(),
        '[•] gpt': plug(),
        '[•] someother shit': plug(),
        '[!] setup(Token)': plug(),
        '[!] setup(Quotes)': plug(),
    }
    choice_value = choice_options.get(choice)
    if choice_value is not None:
        if choice_value == '[!] all in one':
            all_in_one()
        elif choice_value == '[•] main script':
            main_script()
        elif choice_value == '[•] gpt':
            plug()
        elif choice_value == '[•] someother shit':
            plug()
        elif choice_value == '[!] setup(Token)':
            plug()
        elif choice_value == '[!] setup(Quotes)':
            plug()


def main():
    print(f"""{Fore.LIGHTWHITE_EX}{Style.DIM}
    ┌───────────────────────────────────────────────────────────────────────────────┐
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
    time.sleep(1)
    choice = inquirer.list_input(f"{Fore.RESET}{Style.DIM}[2501]// {Fore.GREEN}Enter your choice{Fore.RESET}", choices=['[!] all in one', '[•] main script', '[•] gpt', '[•] someother shit', '[!] setup(Token)', '[!] setup(Quotes)'])
    list_input(choice)


if __name__ == '__main__':
    main()