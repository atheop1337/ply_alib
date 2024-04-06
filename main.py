import asyncio
import logging
import random
from data.Libs.animation import animate, clear_animation
from data.Libs.forumEditor import ForumEditor

logging.basicConfig(format='[%(asctime)s] %(levelname)s |   %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')

class ForumBioEditor(ForumEditor):
    async def send_bio_request(self, id):
        phrases = ["(☞ﾟヮﾟ)☞", "(∪.∪ )...zzz", "\\(〇_o)/", "ᕦ(ò_óˇ)ᕤ", "(^\\\\\\^)", "( •̀ ω •́ )✧", "\\^o^/"]
        random_phrase = random.choice(phrases)
        data = {
            "data": {
                "type": "users",
                "attributes": {
                    "bio": f"Powered by 2501\n{random_phrase}"
                },
                "id": str(id)
            }
        }
        return await self.send_request(id, data)

class ForumNickEditor(ForumEditor):
    async def send_nick_request(self, id, nickname):
        phrases = ["(☞ﾟヮﾟ)☞", "(∪.∪ )...zzz", "\\(〇_o)/", "ᕦ(ò_óˇ)ᕤ", "(^\\\\\\^)", "( •̀ ω •́ )✧", "\\^o^/"]
        random_phrase = random.choice(phrases)
        data = {
            "data": {
                "type": "users",
                "attributes": {
                    "nickname": f"{nickname}\n{random_phrase}"
                },
                "id": str(id)
            }
        }
        return await self.send_request(id, data)

async def Run(id, delay, nickname, senderbio, sendernick):
    loop = 0
    while True:
        animate(delay)
        clear_animation()
        resultbio = await senderbio.send_bio_request(id)
        resultnick = await sendernick.send_nick_request(id, nickname)
        loop += 1
        await asyncio.sleep(0.1)
        if not resultbio or not resultnick:
            logging.error(f"[2501] // Error acquired on loop {loop}...")
            break
        print(f"[2501] // Loop: {loop}")

async def main():
    yn = str(input('[2501] // Debug mode? [y/n]: '))
    user_id = int(input('[2501] // Enter a ID of user: '))
    nickname = str(input('[Nick] // Enter a nickname: '))
    delay = int(input('[2501] // Enter a delay (in seconds): '))
    debug = True if yn.lower() == 'y' else False
    if debug: logging.debug(f'[2501] // Debug mode: {str(debug)}')
    await asyncio.sleep(0.1)
    senderbio = ForumBioEditor(debug=debug)
    sendernick = ForumNickEditor(debug=debug)
    await Run(user_id, delay, nickname, senderbio, sendernick)

if __name__ == "__main__":
    asyncio.run(main())
