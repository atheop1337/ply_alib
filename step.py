import inquirer, time, subprocess, os, signal, sys, configparser, asyncio
from data.libraries.twentyfivezeroone import WindowTitle, const
from data.libraries.forumEditor import ForumEditor
from colorama import Fore, Style, init
init(autoreset=True)

def signal_handler(sig, frame):
    print(f"\n{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Navigate back signal received...")
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Cleaning up...")
    async def run_tasks():
        sendernick = ForumNickEditorHandler()
        senderbio = ForumBioEditorHandler()
        config = configparser.ConfigParser()
        config.read(const().directory + "/settings.ini")
        id = str(config.get("requests", "user_id"))
        await sendernick.send_nick_request(id)
        await senderbio.send_bio_request(id)
        print(f"\n{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Successfully changed to values from C:\\2501\\ply_Alib\\data\\setting.ini!")
        time.sleep(2)
        sys.exit(0)

    asyncio.run(run_tasks())
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
        return await self.send_request(id, data)

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
        return await self.send_request(id, data)
def run_file(file_path, show_console=True):
    if show_console:
        subprocess.Popen(["cmd", "/c", "python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen(["cmd", "/c", "python", file_path])
    return True

def all_in_one():
    # os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n{Fore.RED}THIS FUNCTION IS UNDER CONSTRUCT!')
    #run_file(f'{const().data_directory}/run_all.py', False)
    #time.sleep(1)
    #main()

def setup():
    os.system('cls' if os.name == 'nt' else 'clear')
    run_file(f'{const().data_directory}/run_setup.py', False)
    #time.sleep(1)
    #main()

def main_script():
    os.system('cls' if os.name == 'nt' else 'clear')
    run_file(f'{const().data_directory}/run_main.py', False)
    #time.sleep(1)
    #main()

def server_monitoring():
    os.system('cls' if os.name == 'nt' else 'clear')
    run_file(f'{const().data_directory}/run_serverMonitor.py', False)
    #time.sleep(1)
    #main()

def plug():
    print(f'\n{Fore.RED}THIS FUNCTION IS UNDER CONSTRUCT!')
    #time.sleep(1)
    #main()

def list_input(choice):
    choice_options = {
        '[!] all in one': all_in_one,
        '[!] setup hub': setup,
        '[•] main script': main_script,
        '[•] server monitoring': server_monitoring,
        '[•] someother shit': plug,
    }
    chosen_function = choice_options.get(choice)
    if chosen_function is not None:
        chosen_function()


def main():
    WindowTitle().set("ply_Alib   //   Hub")
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
            '[•] someother shit',
        ])
    except KeyboardInterrupt:
        signal_handler(None, None)

    list_input(choice)


if __name__ == '__main__':
    main()