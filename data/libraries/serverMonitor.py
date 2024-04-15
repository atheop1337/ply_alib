import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
init(autoreset=True)

class ServerMonitor:
    ids = ["11170", "1510", "3780", "2550", "3632"]
    url_template = "https://www.myarena.ru/monitoring.php?game={id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Connection": "keep-alive",
    }

    server_info_list = []

    async def fetch_info(self, session, id):
        url = self.url_template.format(id=id)
        async with session.get(url, headers=self.headers) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')

            gs_info = soup.find('div', class_='gsinfo')
            gsimg_info = soup.find('div', class_='gsimg')

            server_name = gs_info.find('span', id='name').text.strip().split('|')[2].split(' ')[1]
            server_address = gs_info.find('span', class_='ipport').text.strip()
            current_map = gs_info.find('span', id='mapname').text.strip()
            online_players = gsimg_info.find('span', id='numplayers').text.strip().split(':')[1].split(' ')[1]

            self.server_info_list.append({
                "server_name": server_name,
                "server_address": server_address,
                "current_map": current_map,
                "online_players": online_players,
            })

    async def get_info(self):
        async with aiohttp.ClientSession() as session:
            for id in self.ids:
                await self.fetch_info(session, id)

    def return_info(self):
        info_str = ""
        for server_info in self.server_info_list:
            info_str += f"\n{Fore.LIGHTWHITE_EX}{Style.DIM}{server_info['server_name']} [{server_info['server_address']}]\n{Fore.LIGHTWHITE_EX}{server_info['current_map']} - {Fore.GREEN}{server_info['online_players']}\n"

        return info_str.strip()

    def return_time(self):
        local_time = time.localtime()
        formatted_time = time.strftime(f"{Fore.GREEN}%d.%m.%Y %H:%M", local_time)

        return formatted_time

async def main():
    server_monitor = ServerMonitor()
    await server_monitor.get_info()
    print(server_monitor.return_info())
    print(server_monitor.return_time())

if __name__ == "__main__":
    asyncio.run(main())