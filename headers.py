def setup_headers(auto):
    if auto.upper() == "Y":
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://forum.wayzer.ru/u/vilmok',
            'Content-Type': 'application/json; charset=utf-8',
            'X-CSRF-Token': 'OIEtpag2MrhzQzj9w3VfxaXZIxrHE4ZTm7Nv6j7M', # Введи свой токен
            'X-HTTP-Method-Override': 'PATCH',
            'Origin': 'https://forum.wayzer.ru',
            'DNT': '1',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
            'Cookie': 'flarum_remember=UNTKcgOHLYHjC5haEl68pNYPQSkwCrAmnvAYlUHI; flarum_session=BZHHT4yEOgFffbmG54DwsMi790eAyKWq8oWqmvZR', # ВВеди свои куки
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        }
    elif auto.upper() == "N":
        Cookie = input("Cookie: ")
        XCFR = input("Token: ")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://forum.wayzer.ru/u/vilmok',
            'Content-Type': 'application/json; charset=utf-8',
            'X-CSRF-Token': XCFR,
            'X-HTTP-Method-Override': 'PATCH',
            'Origin': 'https://forum.wayzer.ru',
            'DNT': '1',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
            'Cookie': Cookie,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        }
    return headers
