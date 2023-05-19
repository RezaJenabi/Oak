import tkinter as tk

from Src.Infrastructure.Presentation.BaseWidgets import BaseWidgets
from Src.Services.Presentation.Connection.Frams.HeaderFrame import HeaderFrame
from Src.Services.Presentation.Connection.Frams.InformationFrame import InformationFrame


class Connection(BaseWidgets):

    def __init__(self):
        title = 'Connect to Server'
        super().__init__(title)

    def Screen(self):
        super().Screen(width=480, height=240, isFullScreen=False, isResizable=False,
                       icon='./../Assets/DataBaseConnect.ico')

    def CreateFrames(self):
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=2)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=2)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        header = HeaderFrame(self)
        header.grid(sticky=tk.NW)

        information = InformationFrame(self)
        information.grid(sticky=tk.NE)
        # self.tkraise()
