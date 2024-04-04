import re

curl_command = input("Введите строку cURL: ")

csrf_token_pattern = r'-H "X-CSRF-Token: ([^"]+)"'
csrf_token_match = re.search(csrf_token_pattern, curl_command)
cookie_pattern = r'-H "Cookie: ([^"]+)"'
cookie_match = re.search(cookie_pattern, curl_command)

if csrf_token_match and cookie_match:
    csrf_token = csrf_token_match.group(1)
    cookie = cookie_match.group(1)

    print(f'X-CSRF-Token: {csrf_token}')
    print(f'Cookie: {cookie}')
else:
    print('Не удалось извлечь X-CSRF-Token или Cookie из строки cURL.')
