import subprocess
import os
import json
import time
from libraries.twentyfivezeroone import RandomStr, const

def run_file(file_path, show_console=True):
    if show_console:
        subprocess.Popen(["cmd", "/c", "python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen(["cmd", "/c", "python", file_path])
    return True

def main():
    file_path = os.path.join(const().directory, "encrypted.json")

    with open(file_path, 'w') as json_file:
        json.dump(f'{RandomStr().generate_ascii_string(128)}&F', json_file)

    main_file_path = f"{const().main_directory}/main.py"
    rpc_file_path = f"{const().data_directory}/libraries/Inters.py"

    run_file(rpc_file_path, True) # <<< True для дебага, False для запуска
    time.sleep(0.4)
    run_file(main_file_path, False)



if __name__ == "__main__":
    main()
