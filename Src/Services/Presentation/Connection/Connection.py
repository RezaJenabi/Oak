import tkinter as tk

from Src.Infrastructure.Presentation.BaseWidgets import BaseWidgets
from Src.Services.Presentation.Connection.Frams.HeaderFrame import HeaderFrame
from Src.Services.Presentation.Connection.Frams.InformationFrame import InformationFrame


class Connection(BaseWidgets):

    def __init__(self, parent):
        title = 'Connect to Server'
        super().__init__(title, parent)

    def Screen(self):
        super().Screen(width=480, height=280, isFullScreen=False, isResizable=False,
                       icon='./../Assets/DataBaseConnect.ico')

    def CreateFrames(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        header = HeaderFrame(self)
        header.grid(column=0, row=0, sticky=tk.NW)

        # information = InformationFrame(self)
        # information.grid(column=0, row=1, sticky=tk.NW)
