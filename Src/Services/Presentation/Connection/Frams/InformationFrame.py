import tkinter as tk
from tkinter import ttk
from tkinter import *


class InformationFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1, pad=30)
        self.columnconfigure(1, weight=2, pad=30)
        self.columnconfigure(2, weight=4, pad=30)
        self.__create_widgets()

    def __create_widgets(self):
        serverName = ttk.Label(self, text="Server Name:", font=('Aerial bold', 10))
        serverName.grid(column=0, row=0, sticky=tk.W, padx=5)

        serverNamekeyword = ttk.Entry(self, width=30)
        serverNamekeyword.focus()
        serverNamekeyword.grid(column=2, row=0, sticky=tk.NE, padx=0, pady=5)

        serverAuthenticationType = ttk.Label(self, text="Authentication:", font=('Aerial bold', 10))
        serverAuthenticationType.grid(column=0, row=1, sticky=tk.W, padx=5)
        serverAuthenticationTypekeyword = ttk.Entry(self, width=30)
        serverAuthenticationTypekeyword.focus()
        serverAuthenticationTypekeyword.grid(column=2, row=1, sticky=tk.NE, padx=0, pady=5)

        login = ttk.Label(self, text="login:", font=('Aerial bold', 10))
        login.grid(column=0, row=2, sticky=tk.W, padx=5)

        loginkeyword = ttk.Entry(self, width=30)
        loginkeyword.focus()
        loginkeyword.grid(column=2, row=2, sticky=tk.NE, padx=0, pady=5)

        password = ttk.Label(self, text="password:", font=('Aerial bold', 10))
        password.grid(column=0, row=3, sticky=tk.W, padx=5)

        passwordkeyword = ttk.Entry(self, width=30)
        passwordkeyword.focus()
        passwordkeyword.grid(column=2, row=3, sticky=tk.NE, padx=0, pady=5)



