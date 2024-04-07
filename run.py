import subprocess
import os
current_directory = os.path.dirname(os.path.abspath(__file__))

def run_file(file_path):
    process = subprocess.Popen(["cmd", "/c", "python", file_path],
                               creationflags=subprocess.CREATE_NEW_CONSOLE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, error = process.communicate()
    print("Output:", output.decode())
    print("Error:", error.decode())

if __name__ == "__main__":
    ai_file_path = current_directory + "/main.py"
    run_file(ai_file_path)

