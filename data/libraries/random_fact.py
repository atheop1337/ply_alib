import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def get_random_fact():
    link = 'https://randstuff.ru/fact/'
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            fact_block = soup.find('div', id='fact')
            fact_text = fact_block.find('td').text.strip()
            return fact_text

async def main():
    random_fact = await get_random_fact()
    print(random_fact)

if __name__ == "__main__":
    asyncio.run(main())