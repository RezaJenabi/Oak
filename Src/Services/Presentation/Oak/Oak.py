import tkinter as tk

from Src.Services.Presentation.Oak.Frams.HeaderFrame import HeaderFrame


class Oak(tk.Tk):

    def __init__(self):
        super().__init__()
        self.__Init()
        self.__Create()

    def __Init(self):
        self.title('Oak')

    def __Create(self):
        self.__Screen()
        self.__create_widgets()
        self.mainloop()

    def __Screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f'{screen_width}x{screen_height}+0+0')
        self.configure(background='#f0f0f0')
        self.minsize(800, 800)
        self.iconbitmap('./../Assets/Oak_clipartmax.ico')

    def __create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        header = HeaderFrame(self)
        header.grid(column=0, row=0, sticky=tk.NW)


