from data.libraries.twentyfivezeroone import const, EvaSociety

def main():
    EvaSociety().execeva(f"{const().main_directory}/requirements.txt", True, "pip install -r ")



if __name__ == "__main__":
    main()
