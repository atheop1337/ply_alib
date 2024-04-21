import discordrpc
import psutil
import os
import json
import time
import asyncio
from discordrpc.utils import timestamp
from twentyfivezeroone import Connection, RandomStuff, const
get_version = Connection
data = Connection().get_version()

def fterminate(pid):
    process_to_terminate = psutil.Process(pid)
    process_to_terminate.terminate()

def readjsonloop(rpc):
    file_path = os.path.join(const().directory, "encrypted.json")
    while True:
        time.sleep(3)
        with open(file_path, 'r') as json_file:
            loaded_data = json.load(json_file)
        print(loaded_data) # FOR DEBUG
        index_of_ampersand = loaded_data.find('&')
        if index_of_ampersand != -1:
            data_after_ampersand = loaded_data[index_of_ampersand+1:]
            if data_after_ampersand == "T":
                rpc.disconnect()
                with open(file_path, 'w') as json_file:
                    json.dump(f'{RandomStuff().generate_ascii_string(128)}&F', json_file)
                return True

def rpc_connect():
    rpc = discordrpc.RPC(app_id=1227178799964356650, output=True) # True FOR DEBUG
    avatar, name = asyncio.run(Connection().get_data())
    button = discordrpc.Button(
        button_one_label="v1lmok",
        button_one_url="https://github.com/v1lmok",
        button_two_label="Pivo",
        button_two_url="https://github.com/PivoSteve"
    )
    rpc.set_activity(
        state=f'Actual version: {data}',
        details='Powered by 2501',
        buttons=button,
        large_image='2501m',
        large_text='Born in the sea of information',
        small_image=avatar,
        small_text=name,
        ts_start=timestamp,
        ts_end=86400000000,
    )
    readjsonloop(rpc)
    rpc.run()

rpc_connect()
