import tkinter as tk
from tkinter import ttk


class Oak(tk.Tk):

    def __init__(self):
        super().__init__()

    def Create(self):
        Oak.__Init(self)
        Oak.__Screen(self)
        tk.Label(self, text='Classic Label').pack()
        ttk.Label(self, text='Themed Label').pack()
        self.mainloop()

    def __Screen(self):
        min_width = 800
        min_height = 800
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # set the position of the window to the center of the screen
        self.geometry(f'{screen_width}x{screen_height}+{0}+{0}')
        self.minsize(min_width, min_height)

    def __Init(self):
        self.title('Oak')
        self.iconbitmap('./../../../../Images/Oak_clipartmax.ico')
