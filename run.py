from data.libraries.twentyfivezeroone import const, EvaSociety
import configparser, time, asyncio, json, os
from colorama import init, Fore, Style
init(autoreset=True)

async def main():
    try:
        config = configparser.ConfigParser()
        config.read(const().directory + "/settings.ini", encoding="utf-8")
        str(config.get("requests", "user_id"))
    except Exception as e:
        print(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.RED}{e}! Redirection to settings, please configure the script!")
        time.sleep(0.7)
        EvaSociety().execeva(f"{const().libraries_directory}/settings_setup.py", False)
        return
    print(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.YELLOW}Setting up...")
    if os.path.isfile(const().directory + '/startup.json'):
        with open(const().directory + '/startup.json', 'r') as file:
            data = json.load(file)
    else:
        data = {
            "Anonymous": False,
        }
        with open(const().directory + '/startup.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.YELLOW}Start the required services...")
    await EvaSociety().get_info()
    print(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.YELLOW}Deleting Flib files...")
    time.sleep(0.05)
    print(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.YELLOW}Sweeping up the tracks...")
    time.sleep(0.05)
    if not data.get('Anonymous', True):
        print(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.YELLOW}Sending non-anonymous request...")
        EvaSociety().send_discord_webhook()
    else: 
        print(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.YELLOW}Skipping non-anonymous request...")
    time.sleep(0.05)
    EvaSociety().execeva(f"{const().libraries_directory}/Inters.py", False) # <<< True для дебага, False для запуска
    EvaSociety().execeva(f"{const().data_directory}/step.py", False)

if __name__ == "__main__":
    asyncio.run(main())
