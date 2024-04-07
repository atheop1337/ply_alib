import time
import asyncio

async def curtimeget():
    current_time = time.localtime()
    hours = str(current_time.tm_hour).zfill(2)
    minutes = str(current_time.tm_min).zfill(2)
    seconds = str(current_time.tm_sec).zfill(2)
    return f"[{hours}:{minutes}:{seconds}]"

async def main():
    print(await curtimeget())

if __name__ == '__main__':
    asyncio.run(main())