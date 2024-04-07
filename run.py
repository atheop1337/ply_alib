import subprocess

if __name__ == "__main__":
    subprocess.Popen(["cmd", "/c", "python", "main.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)