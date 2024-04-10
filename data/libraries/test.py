import subprocess
import os
current_directory = os.path.dirname(os.path.abspath(__file__))

def run_file(file_path):
    subprocess.Popen(["cmd", "/c", "python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":
    ai_file_path = f"{current_directory}/main.py"
    run_file(ai_file_path)