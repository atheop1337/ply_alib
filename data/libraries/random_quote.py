import aiohttp
import asyncio

async def generate_citata():
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru') as response:
                data = await response.json()
                quote = data['quoteText']
                author = data['quoteAuthor']
                if author == '':
                    author = 'Unknown author'
                if len(quote) <= 60:
                    return quote, author

async def main():
    quote, author = await generate_citata()
    print(f'Random citata: {quote}\nAuthor: {author}')

if __name__ == "__main__":
    asyncio.run(main())
