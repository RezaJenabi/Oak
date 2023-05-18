import tkinter as tk
from tkinter import ttk

from Src.Services.Presentation.Connection.Connection import Connection as Connect


class HeaderFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.__create_widgets()

    def __create_widgets(self):
        _cancel = ttk.Button(self, text="Open Connect", command=self.__Close)
        _cancel.grid(column=2, row=4, padx=15, pady=35, sticky=tk.NE)

    def __Close(self):
        connect = Connect()
        connect.Create()