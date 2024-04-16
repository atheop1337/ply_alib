import discordrpc
import psutil
import os
import json
import time
from discordrpc.utils import timestamp
from twentyfivezeroone import Connection, RandomStr
get_version = Connection
data = Connection().get_version()

def fterminate(pid):
    process_to_terminate = psutil.Process(pid)
    process_to_terminate.terminate()
    #print("Процесс с PID", process_to_terminate, "был завершен.")

def readjsonloop(rpc):
    directory = "C:/2501/ply_Alib/data"
    file_path = os.path.join(directory, "encrypted.json")

    while True:
        time.sleep(3)
        #print("1")
        with open(file_path, 'r') as json_file:
            loaded_data = json.load(json_file)
        print(loaded_data)
        index_of_ampersand = loaded_data.find('&')
        if index_of_ampersand != -1:
            #print("2")
            #print(loaded_data[index_of_ampersand+1:])
            data_after_ampersand = loaded_data[index_of_ampersand+1:]
            if data_after_ampersand == "T":
                #print("3")
                rpc.disconnect()
                with open(file_path, 'w') as json_file:
                    json.dump(f'{RandomStr().generate_ascii_string(128)}&F', json_file)
                return True

def rpc_connect():
    rpc = discordrpc.RPC(app_id=1227178799964356650, output=True)
    button = discordrpc.Button(button_one_label="v1lmok", button_one_url="https://github.com/v1lmok",button_two_label="Pivo",button_two_url="https://github.com/PivoSteve")
    rpc.set_activity(
        state=f'Actual version: {data}', #2
        details='Powered by 2501', #1
        buttons=button,
        large_image='2501m',
        large_text='born in the sea of information',
        small_image='https://cdn.discordapp.com/attachments/678147298009546752/1229736508450275398/tumblr_7eba1b0e282033eac7e9702c4f3bbb2a_e58f7d7d_500.gif',
        small_text='Весть о наступлении Царства Божия и спасении рода человеческого',
        ts_start=timestamp,
        ts_end=86400000000,
        )
    readjsonloop(rpc)
    rpc.run()


rpc_connect()