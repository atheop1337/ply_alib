import configparser
import time
import signal
import sys
import os
from colorama import Fore, Style, init
from twentyfivezeroone import const, WindowTitle, EvaSociety
init(autoreset=True)

def signal_handler(sig, frame):
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.RED}// If this is your first run, restart the script!!!")
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Navigate back signal received...")
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Cleaning up...")
    time.sleep(0.5)
    EvaSociety().execeva(f'{const().data_directory}/run_setup.py', False)
    sys.exit(0)

def create_settings_ini(serverdelay, quotesammount, nicksammount, safonoff, id):
    config = configparser.ConfigParser()
    if serverdelay is None or not str(serverdelay).isdigit():
        answers_serverdelay = "60"
    else:
        answers_serverdelay = str(serverdelay)

    if quotesammount is None or not str(quotesammount).isdigit():
        answers_quotesammount = "50"
    else:
        answers_quotesammount = str(quotesammount)
    if nicksammount is None or not str(quotesammount).isdigit():
        answers_nicksammount = "50"
    else:
        answers_nicksammount = str(quotesammount)
    if id is None or not str(id).isdigit():
        answers_id = "25"
    else:
        answers_id = str(id)

    if not safonoff or not isinstance(safonoff, str):
        answers_safonoff = "True"
    else:
        answers_safonoff = safonoff

    config["serverMonitor"] = {
        "; Delay between updates in seconds": "Default: 60",
        "delay": answers_serverdelay,
    }
    config["quotesGenerator"] = {
        "; Amount of quotes to be generated": "Default: 50",
        "amount": answers_quotesammount,
    }
    config["nicksGenerator"] = {
        "; Amount of nicks to be generated": "Default: 50",
        "amount": answers_nicksammount,
    }
    config["safonoff"] = {
        "; Whether Safonoff AI terminal will run?": "Default: True",
        "boolean": answers_safonoff,
    }
    config["requests"] = {
        "; User id for requests": "Default: 1",
        "user_id": answers_id,
    }
    with open(const().directory + "/settings.ini", "w") as configfile:
        config.write(configfile)
    print(f"\n{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Settings file created successfully in {const().directory}!")
    time.sleep(2)
    signal_handler(None, None)


def main():
    WindowTitle().set("ply_Alib   //   Settings")
    signal.signal(signal.SIGINT, signal_handler)
    os.system('cls' if os.name == 'nt' else 'clear')
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
│  {Fore.RESET}[@]   {Fore.RED}Closing the terminal window is NOT SAFE!                               {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[@]   {Fore.RED}To navigate back to the hub(or exit), please use {Fore.RESET}CTRL+C{Fore.RED}.               {Fore.LIGHTWHITE_EX}│
└───────────────────────────────────────────────────────────────────────────────┘
""")
    time.sleep(0.2)
    try:
        serverdelay = input(
            f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter delay for \"serverMonitor\" section (in seconds) {Fore.RESET}(default 60) [int]: ")
        quotesammount = input(
            f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter amount for \"quotesGenerator\" section {Fore.RESET}(default 50) [int]: ")
        nicksamount = input(
            f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter amount for \"nicksGenerator\" section {Fore.RESET}(default 50) [int]: ")
        safonoff = input(
            f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Whether \"Safonoff AI terminal\" will run with all_in_one function? {Fore.RESET}(default True) [bool]: ")
        id = input(
            f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter amount for \"requests\" section {Fore.RESET}(default 1(WayZer)) [str]: ")
        create_settings_ini(serverdelay, quotesammount, nicksamount, safonoff,  id)
    except KeyboardInterrupt:
        signal_handler(None, None)


if __name__ == "__main__":
    main()
