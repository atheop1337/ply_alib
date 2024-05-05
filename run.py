from data.libraries.twentyfivezeroone import const, EvaSociety

def main():
    EvaSociety().execeva(f"{const().libraries_directory}/Inters.py", False) # <<< True для дебага, False для запуска
    EvaSociety().execeva(f"{const().data_directory}/step.py", False)

if __name__ == "__main__":
    main()
