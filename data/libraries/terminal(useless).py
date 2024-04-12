import tkinter as tk
from tkterminal import Terminal

class EmbeddedTerminalApp:
    def __init__(self, master):

        self.master = master
        self.master.title("Embedded Terminal")

        self.terminal_frame = tk.Frame(master)
        self.terminal_frame.pack(fill=tk.BOTH, expand=True)

        self.terminal = Terminal(self.terminal_frame, background="black", foreground="white")
        self.terminal.shell = True
        self.terminal.pack(fill=tk.BOTH, expand=True)

        self.master.bind('<Return>', self.execute_command)

    def execute_command(self, event):
        command = self.terminal.get_command()
        self.terminal.write(f"\n$ {command}\n")

def main():
    root = tk.Tk()
    app = EmbeddedTerminalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
