import subprocess
import os
import json
import time
from libraries.twentyfivezeroone import RandomStr

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)

def run_file(file_path, show_console=True):
    if show_console:
        subprocess.Popen(["cmd", "/c", "python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen(["cmd", "/c", "python", file_path])
    return True

def main():
    directory = "C:/2501/ply_Alib/data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, "encrypted.json")

    with open(file_path, 'w') as json_file:
        json.dump(f'{RandomStr().generate_ascii_string(128)}&F', json_file)

    main_file_path = f"{parent_directory}/main.py"
    rpc_file_path = f"{current_directory}/libraries/Inters.py"

    run_file(rpc_file_path, False) #<<< True для дебага, False для запуска
    time.sleep(0.4)
    run_file(main_file_path, True)



if __name__ == "__main__":
    main()
