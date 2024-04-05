import requests
import os
import json
import sys
from Libs.RandomName import generate_random_name
def setup_headers():
    exe_path = sys.argv[0]
    exe_dir = os.path.dirname(os.path.abspath(exe_path))
    json_path = os.path.join(exe_dir, 'headers.json')

    if not os.path.exists(json_path):
        raise FileNotFoundError(f'File not found: {json_path}')

    with open(json_path, 'r') as f:
        headers = json.load(f)

    return headers
headers = setup_headers()

ids = int(input("Введите свое ID: "))
name = generate_random_name()
url = "https://forum.wayzer.ru/api/users/" + str(ids)

data = {
    "data": {
        "type": "users",
        "attributes": {
            "nickname": name,
        },
        "id": ids
    }
}
response = requests.post(url, headers=headers, json=data)

