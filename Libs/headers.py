import json
def setup_headers():
    with open('Libs/headers.json', 'r') as file:
        headers_data = json.load(file)
        headers = headers_data['headers']
    return headers