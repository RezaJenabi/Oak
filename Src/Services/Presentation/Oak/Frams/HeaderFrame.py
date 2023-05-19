import tkinter as tk
from tkinter import ttk

from Src.Infrastructure.Presentation.BaseFrame import BaseFrame
from Src.Infrastructure.Presentation.BaseWidgets import BaseWidgets
from Src.Services.Presentation.Connection.Connection import Connection as Connect
from Src.Services.Entity.Share.ShareInstance import ShareInstance


class HeaderFrame(BaseFrame):

    def __init__(self, parent: BaseWidgets):
        super().__init__(parent)

    def Create(self):
        _openConnectFrame = ttk.Button(master=self, text="Open Connect", command=self.OpenConnectFrame)
        _openConnectFrame.grid(column=2, row=4, padx=15, pady=35, sticky=tk.NE)

        _testFrame = ttk.Button(master=self, text="Test", command=self.Test)
        _testFrame.grid(column=2, row=5, padx=15, pady=35, sticky=tk.NE)

    def OpenConnectFrame(self):
        Connect()

    def Test(self):
        for x in range(len(ShareInstance.instances)):
            print( ShareInstance.instances[x].Login)


