import tkinter as tk
from Src.Services.Presentation.Connection.Frams.HeaderFrame import HeaderFrame
from Src.Services.Presentation.Connection.Frams.InformationFrame import InformationFrame


class Connection(tk.Tk):

    def __init__(self):
        super().__init__()

    def __Init(self):
        self.title('Connect to Server')

    def Create(self):
        self.__Init()
        self.__Screen()
        self.__create_widgets()

    def __Screen(self):
        window_width = 480
        window_height = 280
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.configure(background='#f0f0f0')
        self.resizable(False, False)
        self.iconbitmap('./../Assets/DataBaseConnect.ico')

    def __create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        header = HeaderFrame(self)
        header.grid(column=0, row=0, sticky=tk.NW)

        information = InformationFrame(self)
        information.grid(column=0, row=1, sticky=tk.NW)

    def __Close(self):
        self.destroy()