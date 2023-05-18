import tkinter as tk

from Src.Infrastructure.Presentation.BaseWidgets import BaseWidgets
from Src.Services.Presentation.Oak.Frams.HeaderFrame import HeaderFrame


class Oak(BaseWidgets):

    def __init__(self, parent):
        title = 'Oak'
        super().__init__(title, parent)

    def Create(self):
        super().Create()
        self.mainloop()

    def CreateFrames(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        header = HeaderFrame()
        header.grid(column=0, row=0, sticky=tk.NW)


