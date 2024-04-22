import cmd, signal
import asyncio
import os, time, sys
from colorama import Fore, Style, init
from libraries.pseudohacker import PseudoHacker
from libraries.ai import ArtificialInteligence
from libraries.discussionchecker import DiscussionChecker
from libraries.twentyfivezeroone import WindowTitle, EvaSociety, const
init(autoreset=True)

def signal_handler(sig, frame):
    print(f"\n{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Navigate back signal received...")
    print(f"{Fore.RESET}{Style.DIM}[2501] {Fore.YELLOW}// Cleaning up...")
    time.sleep(0.5)
    EvaSociety().execeva(f'{const().main_directory}/step.py', False)
    sys.exit(0)

class AiTerminalCLI(cmd.Cmd):
    intro = f"""{Fore.LIGHTWHITE_EX}{Style.DIM}
┌──────────────────┬────────────────────────────────────────────────────────────┐
│     {Fore.RESET}ply_Alib       Safonoff AI terminal                                       {Fore.LIGHTWHITE_EX}│
├──────────────────┴────────────────────────────────────────────────────────────┤
│                                                                               │
│{Fore.YELLOW}         ██▓███   ██▓   ▓██   ██▓       ▄▄▄       ██▓     ██▓ ▄▄▄▄             {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▓██░  ██▒▓██▒    ▒██  ██▒      ▒████▄    ▓██▒    ▓██▒▓█████▄          {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▓██░ ██▓▒▒██░     ▒██ ██░      ▒██  ▀█▄  ▒██░    ▒██▒▒██▒ ▄██         {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▒██▄█▓▒ ▒▒██░     ░ ▐██▓░      ░██▄▄▄▄██ ▒██░    ░██░▒██░█▀           {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ▒██▒ ░  ░░██████▒ ░ ██▒▓░       ▓█   ▓██▒░██████▒░██░░▓█  ▀█▓         {Fore.LIGHTWHITE_EX}│    
│{Fore.YELLOW}         ▒▓▒░ ░  ░░ ▒░▓  ░  ██▒▒▒        ▒▒   ▓▒█░░ ▒░▓  ░░▓  ░▒▓███▀▒         {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ░▒ ░     ░ ░ ▒  ░▓██ ░▒░         ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░▒░▒   ░          {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}         ░░         ░ ░   ▒ ▒ ░░          ░   ▒     ░ ░    ▒ ░ ░    ░          {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}                  ░  ░░ ░                 ░  ░    ░  ░ ░   ░                   {Fore.LIGHTWHITE_EX}│
│{Fore.YELLOW}                      ░ ░                                       ░              {Fore.LIGHTWHITE_EX}│
│                                                                               │
│  {Fore.RESET}[•]   {Fore.GREEN}Welcome to the ply_Alib script!                                        {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[!]   {Fore.GREEN}Type "help" for more information...                                    {Fore.LIGHTWHITE_EX}│
│  {Fore.RESET}[@]   {Fore.RED}To navigate back to the hub(or exit), please use {Fore.RESET}\"exit\"{Fore.RED} command.       {Fore.LIGHTWHITE_EX}│
└───────────────────────────────────────────────────────────────────────────────┘
"""
    prompt = "[2501] > "

    def do_osint(self, text):
        """[phone number] :: Checks a phone number""" 
        try:
            PseudoHacker.checkphone(text)
        except Exception as e:
            print(f"Error: {str(e)}\n")

    def do_echo(self, text):
        """[text] :: Prints text to the console"""
        print(text)

    def do_cat(self, filename):
        """[filename] :: Displays the contents of a file"""
        try:
            with open(filename, "r") as file:
                content = file.read()
            print(content + "\n")
        except Exception as e:
            print(f"Error: {str(e)}\n")

    def do_mkdir(self, dirname):
        """[dirname] :: Creates a new directory"""
        try:
            os.mkdir(dirname)
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_rmdir(self, dirname):
        """[dirname] :: Removes an empty directory"""
        try:
            os.rmdir(dirname)
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_rm(self, filename):
        """[filename] :: Removes a file"""
        try:
            os.remove(filename)
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_touch(self, filename):
        """[filename] :: Creates a new file"""
        try:
            with open(filename, "w") as file:
                pass
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_ls(self, path):
        """[dirname] :: Lists files and directories in the current directory"""
        try:
            if not path:
                cpath = os.getcwd()
                files = os.listdir(cpath)
                print("\n".join(files) + "\n")
            else:
                cpath = path
                files = os.listdir(cpath)
                print("\n".join(files) + "\n")
        except Exception as e:
            print(path)
            print(f"Error: {str(e)}\n")
        
    def do_cd(self, path):
        """[dirname] :: Changes the current directory"""
        try:
            if not path:
                print(os.getcwd())
            elif path == "..":
                os.chdir(os.path.dirname(os.getcwd()))
                print(os.getcwd())
            else:
                os.chdir(path)
                print(os.getcwd())
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_clear(self, args):
        """ :: Clears the console"""
        os.system('cls' if os.name=='nt' else 'clear')
        print(self.intro)

    def do_exit(self, args):
        """ :: Exits the console application"""
        signal_handler(None, None)

    def do_help(self, args):
        """ :: Displays available commands and their descriptions"""
        for command in self.get_names():
            if command.startswith("do_"):
                command_name = command[3:]
                print(f"    {command_name} {getattr(self, command).__doc__}")

    def do_ai(self, command):
        """[Text] :: Allows the user to send an AI request | Expect delays with response"""
        asyncio.run(self.process_text(command))

    def do_dc(self, args):
        """[Discussion ID] [Amount of posts] :: Allows the user to check any discussion"""
        try:
            discussion_id, *amount_of_posts = args.split()
            if not amount_of_posts:
                amount_of_posts = ['9999']
            else:
                amount_of_posts = amount_of_posts[:1] 
            info = DiscussionChecker.get_info(discussion_id, int(amount_of_posts[0]))
            print(info)
        except Exception as e:
            print(f"Error: {str(e)}")
            
    async def process_text(self, text):
        model = ArtificialInteligence()
        response = await model.generate_response(text)
        print("    " + response)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    WindowTitle().set("ply_Alib   //   Safonoff AI terminal")
    AiTerminalCLI().cmdloop()

if __name__ == '__main__':
    main()