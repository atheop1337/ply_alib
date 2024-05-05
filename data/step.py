import inquirer, time, logging, os, signal, sys, configparser, asyncio, json, argparse
from libraries.twentyfivezeroone import WindowTitle, const, EvaSociety, RandomStuff
from libraries.forumEditor import ForumEditor
from colorama import Fore, Style, init
init(autoreset=True)

def signal_handler(sig, frame):
    print(f"\n{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Closing app signal received.")
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Cleaning up...")
    time.sleep(0.5)
    file_path = os.path.join(const().directory, "encrypted.json")
    with open(file_path, 'w') as json_file:
        json.dump(f'{RandomStuff().generate_ascii_string(128)}&T', json_file)
    async def run_tasks():
        sendernick = ForumNickEditorHandler()
        senderbio = ForumBioEditorHandler()
        config = configparser.ConfigParser()
        config.read(const().directory + "/settings.ini")
        id = str(config.get("requests", "user_id"))
        await sendernick.send_nick_request(id)
        await senderbio.send_bio_request(id)
        print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Successfully changed to values from C:\\2501\\ply_Alib\\data\\setting.ini!")
        print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// The terminal window will close after a few seconds....")
        print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.RED}// If this does not happen, close the terminal window yourself...")
        time.sleep(0.5)

    asyncio.run(run_tasks())
    sys.exit(0)

class ForumNickEditorHandler(ForumEditor):
    async def send_nick_request(self, id):
        config = configparser.ConfigParser()
        config.read(const().directory + "/settings.ini")
        nickname = str(config.get("nickname", "nickname"))
        data = {
            "data": {
                "type": "users",
                "attributes": {
                    "nickname": nickname
                },
                "id": str(id)
            }
        }
        response = await self.send_request(id, data)

        if not response:
            print(f'{Fore.RESET}[2501] // {Fore.RED} Token not found! | Invalid token!{Fore.RESET}\n[2501] // {Fore.YELLOW} Redirecting to GetToken.py..{Fore.RESET}')
            await asyncio.sleep(2)
            EvaSociety().execeva(f'{const().data_directory}/GetToken.py', False)
            sys.exit(0)
        return response


class ForumBioEditorHandler(ForumEditor):
    async def send_bio_request(self, id):
        config = configparser.ConfigParser()
        config.read(const().directory + "/settings.ini")
        bio = str(config.get("bio", "bio")).replace("\\n", "\n")
        data = {
            "data": {
                "type": "users",
                "attributes": {
                    "bio": bio
                },
                "id": str(id)
            }
        }
        response = await self.send_request(id, data)

        if not response:
            print(f'{Fore.RESET}[2501] // {Fore.RED} Token not found! | Invalid token!{Fore.RESET}\n[2501] // {Fore.YELLOW} Redirecting to GetToken.py..{Fore.RESET}')
            await asyncio.sleep(2)
            EvaSociety().execeva(f'{const().data_directory}/GetToken.py', False)
            sys.exit(0)
        return response

def all_in_one():
    os.system('cls' if os.name == 'nt' else 'clear')
    EvaSociety().execeva(f'{const().data_directory}/run_all.py', False)

def setup():
    os.system('cls' if os.name == 'nt' else 'clear')
    EvaSociety().execeva(f'{const().data_directory}/run_setup.py', False)

def main_script():
    os.system('cls' if os.name == 'nt' else 'clear')
    EvaSociety().execeva(f"{const().data_directory}/run_main.py", False)

def server_monitoring():
    os.system('cls' if os.name == 'nt' else 'clear')
    EvaSociety().execeva(f'{const().data_directory}/run_serverMonitor.py', False)

def ai():
    os.system('cls' if os.name == 'nt' else 'clear')
    EvaSociety().execeva(f'{const().data_directory}/run_ai.py', False)

def list_input(choice):
    choice_options = {
        '[!] all in one': all_in_one,
        '[!] setup hub': setup,
        '[•] main script': main_script,
        '[•] server monitoring': server_monitoring,
        '[•] safonoff AI terminal': ai,
    }
    chosen_function = choice_options.get(choice)
    if chosen_function is not None:
        chosen_function()

def main():
    WindowTitle().set("ply_Alib   //   Hub")
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    file_path = os.path.join(const().directory, "encrypted.json")
    with open(file_path, 'w') as json_file:
        json.dump(f'{RandomStuff().generate_ascii_string(128)}&F', json_file)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Fore.LIGHTWHITE_EX}{Style.DIM}
┌──────────────────┬────────────────────────────────────────────────────────────┐
│     {Fore.RESET}ply_Alib       Hub                                                        {Fore.LIGHTWHITE_EX}│
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
│  {Fore.RESET}[@]   {Fore.RED}Closing the terminal window is NOT SAFE please use {Fore.RESET}CTRL+C{Fore.RED}.             {Fore.LIGHTWHITE_EX}│
└───────────────────────────────────────────────────────────────────────────────┘
""")
    time.sleep(0.2)
    signal.signal(signal.SIGINT, signal_handler)
    try:
        choice = inquirer.list_input(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.GREEN}Enter your choice{Fore.RESET}", choices=[
            '[!] all in one',
            '[!] setup hub',
            '[•] main script',
            '[•] server monitoring',
            '[•] safonoff AI terminal',
        ])
    except KeyboardInterrupt:
        signal_handler(None, None)

    list_input(choice)


if __name__ == '__main__':
    main()