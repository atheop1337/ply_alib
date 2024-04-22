from data.libraries.twentyfivezeroone import const, EvaSociety

def main():
    EvaSociety().execeva(f"{const().main_directory}/requirements.txt", False, "pip install -r ") # <<< True для дебага, False для запуска



if __name__ == "__main__":
    main()
