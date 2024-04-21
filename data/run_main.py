import os
import json
import time
from libraries.twentyfivezeroone import RandomStuff, const, EvaSociety

def main():
    file_path = os.path.join(const().directory, "encrypted.json")

    with open(file_path, 'w') as json_file:
        json.dump(f'{RandomStuff().generate_ascii_string(128)}&F', json_file)

    main_file_path = f"{const().main_directory}/main.py"
    rpc_file_path = f"{const().data_directory}/libraries/Inters.py"

    EvaSociety().execeva(rpc_file_path, True) # <<< True для дебага, False для запуска
    time.sleep(0.9)
    EvaSociety().execeva(main_file_path, False)



if __name__ == "__main__":
    main()
