from libraries.twentyfivezeroone import RandomStuff, const, EvaSociety

def main():
    main_file_path = f"{const().main_directory}/main.py"
    rpc_file_path = f"{const().data_directory}/libraries/Inters.py"

    EvaSociety().execeva(rpc_file_path, False) # <<< True для дебага, False для запуска
    EvaSociety().execeva(main_file_path, False)



if __name__ == "__main__":
    main()
