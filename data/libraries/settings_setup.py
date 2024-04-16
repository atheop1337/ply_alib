import configparser
import inquirer
import time
import os
import signal
import sys
from colorama import Fore, Style, init
from twentyfivezeroone import const, WindowTitle
current_directory = os.path.dirname(os.path.abspath(__file__))
init(autoreset=True)

def signal_handler(sig, frame):
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Shutdown signal received...")
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Cleaning up...")
    time.sleep(0.5)
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Thank you for being with us!")
    time.sleep(2)
    sys.exit(0)

def create_settings_ini(answers):
    config = configparser.ConfigParser()
    config["serverMonitor"] = {
        "; Delay between updates in seconds": "Default 60",
        "delay": answers["server_delay"]
    }
    config["quotesGenerator"] = {
        "; Amount of quotes to be generated": "Default 50",
        "amount": answers["quotes_amount"]
    }
    config["requests"] = {
        "; User id": "Default ?",
        "amount": answers["requests"]
    }
    with open(const().directory + "/settings.ini", "w") as configfile:
        config.write(configfile)
    print(f"\n{Fore.RESET}{Style.DIM}[2501] // {Fore.YELLOW}Settings file created successfully in {const().directory}!")
    time.sleep(2)
    signal_handler(None, None)


def main():
    WindowTitle().set("ply_Alib   //   Settings")
    signal.signal(signal.SIGINT, signal_handler)
    print(f"""{Fore.LIGHTWHITE_EX}{Style.DIM}
┌──────────────────┬────────────────────────────────────────────────────────────┐
│     {Fore.RESET}ply_Alib       Settings                                                   {Fore.LIGHTWHITE_EX}│
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
│  {Fore.RESET}[@]   {Fore.RED}Closing the terminal window is NOT SAFE please use {Fore.RESET}CTRL+C{Fore.RED}.             {Fore.LIGHTWHITE_EX}│
└───────────────────────────────────────────────────────────────────────────────┘
""")
    time.sleep(0.2)
    try:
        questions = [
            inquirer.Text("server_delay", message=f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter delay for \"serverMonitor\" section (in seconds){Fore.RESET}", default="60"),
            inquirer.Text("quotes_amount", message=f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter amount for \"quotesGenerator\" section{Fore.RESET}", default="50"),
            inquirer.Text("requests", message=f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter default id for \"requests\"{Fore.RESET}", default=""),
        ]
    except KeyboardInterrupt:
        signal_handler(None, None)

    answers = inquirer.prompt(questions)
    create_settings_ini(answers)


if __name__ == "__main__":
    main()
