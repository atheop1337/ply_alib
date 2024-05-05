from data.libraries.twentyfivezeroone import const, EvaSociety
import configparser, time
from colorama import init, Fore, Style
init(autoreset=True)

def main():
    try:
        config = configparser.ConfigParser()
        config.read(const().directory + "/settings.ini")
        str(config.get("requests", "user_id"))
    except Exception as e:
        print(f"{Fore.RESET}{Style.DIM}[2501] // {Fore.RED}{e}! Redirection to settings, please configure the script!")
        time.sleep(0.7)
        EvaSociety().execeva(f"{const().libraries_directory}/settings_setup.py", False)

    EvaSociety().execeva(f"{const().libraries_directory}/Inters.py", False) # <<< True для дебага, False для запуска
    EvaSociety().execeva(f"{const().data_directory}/step.py", False)

if __name__ == "__main__":
    main()
