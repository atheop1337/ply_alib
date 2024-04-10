import discordrpc
from discordrpc.utils import timestamp
from twentyfivezeroone import GetVersion
data = GetVersion().fetch_data()

def rpc_connect():
    rpc = discordrpc.RPC(app_id=1227178799964356650, output=True)
    button = discordrpc.Button(button_one_label="Какой-то мужик", button_one_url="https://github.com/v1lmok",button_two_label="Злодей британец",button_two_url="https://github.com/PivoSteve")
    rpc.set_activity(
        state=f'{data}', #2
        details='Powered by 2501', #1
        buttons=button,
        large_image='main',
        large_text='Мейби бейби такая зайка',
        ts_start=timestamp,
        ts_end=86400000000,
        )
    rpc.run()

rpc_connect()