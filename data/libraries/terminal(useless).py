import tkinter as tk
import datetime
import os
import platform
import traceback
import sys
from io import StringIO


class ConsoleWindow:
    def __init__(self, root):
        self.root = root
        self.create_widgets()
        self.text_to_display = ""
        self.index = 0
        self.commands = {
            "help": (self.display_help, "Displays available commands and their descriptions"),
            "clear": (self.clear_console, "Clears the console"),
            "date": (self.display_date, "Displays the current date and time"),
            "eval": (self.calculate, "Performs a mathematical calculation and displays the result"),
            "python": (self.run_python_code, "Executes Python code"),
            "exit": (self.exit_console, "Exits the console application"),
            "ls": (self.list_directory, "Lists files and directories in the current directory"),
            "cd": (self.change_directory, "Changes the current directory"),
            "echo": (self.echo_text, "Prints text to the console"),
            "uname": (self.display_system_info, "Displays system information"),
            "whoami": (self.display_username, "Displays the current user's username"),
            "cat": (self.display_file_content, "Displays the contents of a file"),
            "mkdir": (self.make_directory, "Creates a new directory"),
            "rmdir": (self.remove_directory, "Removes an empty directory"),
            "rm": (self.remove_file, "Removes a file"),
            "touch": (self.create_file, "Creates a new file")
        }
        self.command_history = []
        self.history_index = -1

    def create_widgets(self):
        self.text_area = tk.Text(self.root, wrap="word", state="normal", height=25, width=120, bg="black", fg="white")
        self.text_area.pack(fill="both", expand=True)
        self.text_area.bind("<Key>", self.key_pressed)
        self.text_area.focus_set()

        self.input_frame = tk.Frame(self.root, bg="black")
        self.input_frame.pack(fill="x")

        self.input_label = tk.Label(self.input_frame, text="> ", fg="white", bg="black")
        self.input_label.pack(side="left")

        self.input_entry = tk.Entry(self.input_frame, bg="black", fg="white", insertbackground="white")
        self.input_entry.pack(fill="x", expand=True)
        self.input_entry.bind("<Return>", self.execute_command)
        self.input_entry.bind("<Up>", self.history_up)
        self.input_entry.bind("<Down>", self.history_down)

    def write(self, msg):
        self.text_to_display += msg
        self.display_text()

    def display_text(self):
        self.text_area.configure(state="normal")
        if self.index < len(self.text_to_display):
            self.text_area.insert("end", self.text_to_display[self.index])
            self.text_area.see("end")
            self.index += 1
        self.text_area.configure(state="disabled")
        if self.index < len(self.text_to_display):
            self.root.after(25, self.display_text)

    def print_to_console(self, message):
        self.write(message + "\n")

    def display_help(self):
        for command, (func, description) in self.commands.items():
            self.print_to_console(f"    {command} >>> {description}")
        return ""

    def clear_console(self):
        self.text_area.configure(state="normal")
        self.text_area.delete(1.0, "end")
        self.text_area.configure(state="disabled")
        return ""

    def display_date(self):
        now = datetime.datetime.now()
        return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n"

    def calculate(self, expression):
        try:
            result = eval(expression)
            return f"Result: {result}\n"
        except Exception as e:
            return f"Error: {str(e)}\n"

    def run_python_code(self, code):
        try:
            if code.startswith("-p "):
                script_path = code[3:]
                with open(script_path, "r") as script_file:
                    script_content = script_file.read()
                stdout_backup = sys.stdout
                sys.stdout = StringIO()
                exec(script_content)
                result = sys.stdout.getvalue()
                return result
            else:
                stdout_backup = sys.stdout
                sys.stdout = StringIO()
                exec(code)
                result = sys.stdout.getvalue()
                return result
            return ""
        except Exception as e:
            return traceback.format_exc()
        finally:
            sys.stdout = stdout_backup

    def exit_console(self):
        self.root.destroy()

    def list_directory(self, path="."):
        try:
            files = os.listdir(path)
            return "\n".join(files) + "\n"
        except Exception as e:
            return f"Error: {str(e)}\n"

    def change_directory(self, path=None):
        try:
            if not path:
                return os.getcwd() + "\n"
            elif path == "..":
                os.chdir(os.path.dirname(os.getcwd()))
                return os.getcwd() + "\n"
            else:
                os.chdir(path)
                return os.getcwd() + "\n"
        except Exception as e:
            return f"Error: {str(e)}\n"

    def echo_text(self, text):
        return f"{text}\n"

    def display_system_info(self):
        return f"System: {platform.system()}\nNode Name: {platform.node()}\nRelease: {platform.release()}\nVersion: {platform.version()}\nMachine: {platform.machine()}\nProcessor: {platform.processor()}\n"

    def display_username(self):
        return f"Current User: {os.getlogin()}\n"

    def display_file_content(self, filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
            return content + "\n"
        except Exception as e:
            return f"Error: {str(e)}\n"

    def make_directory(self, dirname):
        try:
            os.mkdir(dirname)
            return ""
        except Exception as e:
            return f"Error: {str(e)}\n"

    def remove_directory(self, dirname):
        try:
            os.rmdir(dirname)
            return ""
        except Exception as e:
            return f"Error: {str(e)}\n"

    def remove_file(self, filename):
        try:
            os.remove(filename)
            return ""
        except Exception as e:
            return f"Error: {str(e)}\n"

    def create_file(self, filename):
        try:
            with open(filename, "w") as file:
                pass
            return ""
        except Exception as e:
            return f"Error: {str(e)}\n"

    def execute_command(self, event):
        command = self.input_entry.get()
        self.input_entry.delete(0, "end")
        self.print_to_console(f"> {command}\n")
        self.command_history.append(command)
        self.history_index = len(self.command_history)

        command_parts = command.split(" ", 1)
        if command_parts[0] in self.commands:
            if len(command_parts) > 1:
                result = self.commands[command_parts[0]][0](command_parts[1])
            else:
                result = self.commands[command_parts[0]][0]()
            if result is not None:
                self.print_to_console(result)
        else:
            self.print_to_console("Command not recognized. Type \"help\" for more information...\n")

    def key_pressed(self, event):
        if event.keysym == "Up":
            self.history_up(event)
        elif event.keysym == "Down":
            self.history_down(event)

    def history_up(self, event):
        if self.history_index > 0:
            self.history_index -= 1
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, self.command_history[self.history_index])

    def history_down(self, event):
        if self.history_index < len(self.command_history) - 1:
            self.history_index += 1
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, self.command_history[self.history_index])

if __name__ == "__main__":
    root = tk.Tk()
    console = ConsoleWindow(root)
    root.mainloop()
