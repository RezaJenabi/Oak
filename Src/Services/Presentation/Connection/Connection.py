import tkinter as tk

from Src.Services.Presentation.Connection.Frams.FooterFrame import FooterFrame
from Src.Services.Presentation.Connection.Frams.HeaderFrame import HeaderFrame
from Src.Services.Presentation.Connection.Frams.InformationFrame import InformationFrame


class Connection(tk.Tk):

    def __init__(self):
        super().__init__()
        self.__Init()
        self.__Create()

    def __Init(self):
        self.title('Connect to Server')

    def __Create(self):
        self.__Screen()
        self.__create_widgets()
        self.mainloop()

    def __Screen(self):
        window_width = 480
        window_height = 280
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.configure(background='#f0f0f0')
        self.resizable(False, False)
        # self.attributes('-toolwindow', True)
        self.iconbitmap('./../Assets/ssms.ico')

    def __create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=1)

        header = HeaderFrame(self)
        header.grid(column=0, row=0, sticky=tk.NW)

        information = InformationFrame(self)
        information.grid(column=0, row=1, sticky=tk.NW)

        footer = FooterFrame(self)
        footer.grid(column=0, row=2, sticky=tk.NW)
