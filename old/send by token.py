import requests
url = 'https://forum.wayzer.ru/api/posts'
x_crf_token = 'PVYzvxbUcvxzikilqwHlJDUBESNiINS9p6JTixY9'
session_cookie = 'flarum_remember=UNTKcgOHLYHjC5haEl68pNYPQSkwCrAmnvAYlUHI; flarum_session=29nwlR4zxRxbyv2PAvjfTOarBJVpDqXdoRI4RNdb'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://forum.wayzer.ru/d/13922-123',
    'Content-Type': 'application/json; charset=utf-8',
    'X-CSRF-Token': x_crf_token,
    'Origin': 'https://forum.wayzer.ru',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
}
cookies = {
    'flarum_remember': 'UNTKcgOHLYHjC5haEl68pNYPQSkwCrAmnvAYlUHI',
    'flarum_session': '29nwlR4zxRxbyv2PAvjfTOarBJVpDqXdoRI4RNdb'
}
message = input('Enter message: ')
disid = input('Enter discussion id: ')
message_data = {
    'data': {
        'type': 'posts',
        'attributes': {
            'content': message
        },
        'relationships': {
            'discussion': {
                'data': {
                    'type': 'discussions',
                    'id': disid
                }
            }
        }
    }
}
response = requests.post(url, headers=headers, cookies=cookies, json=message_data)
if response.status_code == 200 or response.status_code == 201:
    print('Сообщение успешно отправлено!')
else:
    print('Ошибка при отправке сообщения:', response.status_code)
    print('Текст ошибки:', response.text)
