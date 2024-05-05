from data.libraries.twentyfivezeroone import const, EvaSociety
import configparser, time, asyncio
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
    
    await EvaSociety().get_info()
    EvaSociety().send_discord_webhook()
    EvaSociety().execeva(f"{const().libraries_directory}/Inters.py", False) # <<< True для дебага, False для запуска
    EvaSociety().execeva(f"{const().data_directory}/step.py", False)

if __name__ == "__main__":
    asyncio.run(main())
