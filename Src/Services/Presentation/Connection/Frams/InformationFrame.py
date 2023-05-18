import tkinter as tk
from tkinter import ttk
from Src.Infrastructure.ReadOnly.AuthenticationType import AuthenticationType
from tkinter import *


class InformationFrame(ttk.Frame):

    __login, __password, __serverAuthenticationType, __serverName = None, None, None, None

    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1, pad=30)
        self.columnconfigure(1, weight=2, pad=30)
        self.columnconfigure(2, weight=4, pad=30)
        self.__create_widgets()

    def __create_widgets(self):

        ttk.Label(self, text="Server Name:", font=('Aerial bold', 10)).grid(column=0, row=0, sticky=tk.W, padx=5)
        self.__serverName = ttk.Entry(self, width=40)
        self.__serverName.focus()
        self.__serverName.grid(column=2, row=0, sticky=tk.NE, padx=15, pady=5)

        ttk.Label(self, text="Authentication:", font=('Aerial bold', 10)).grid(column=0, row=1, sticky=tk.W, padx=5)
        self.__serverAuthenticationType = ttk.Combobox(self, state="readonly", width=37)
        self.__serverAuthenticationType.bind("<<ComboboxSelected>>", self.__AuthenticationTypeChanged)
        self.__serverAuthenticationType['values'] = list(AuthenticationType.AuthenticationTypeDictionary.values())
        self.__serverAuthenticationType.grid(column=2, row=1, sticky=tk.NE, padx=15, pady=5)
        self.__serverAuthenticationType.current(0)

        ttk.Label(self, text="login:", font=('Aerial bold', 10)).grid(column=0, row=2, sticky=tk.W, padx=5)
        self.__login = ttk.Entry(self, width=40, state="disabled")
        self.__login.grid(column=2, row=2, sticky=tk.NE, padx=15, pady=5)

        ttk.Label(self, text="password:", font=('Aerial bold', 10)).grid(column=0, row=3, sticky=tk.W, padx=5)
        self.__password = ttk.Entry(self, width=40, state="disabled", show='*')
        self.__password.grid(column=2, row=3, sticky=tk.NE, padx=15, pady=5)

        cv = Canvas(self, width=480, height=70)
        cv.create_line(10, 10, 470, 10, fill="#c1c1c1", width=1)
        cv.grid(column=0, columnspan=3)

        _connect = ttk.Button(self, text="Connect", command=self.__Connect)
        _connect.grid(column=2, row=4, padx=100, pady=35, sticky=tk.NE)

        _cancel = ttk.Button(self, text="Cancel", command=self.__Close)
        _cancel.grid(column=2, row=4,  padx=15, pady=35, sticky=tk.NE)

    def __AuthenticationTypeChanged(self, event):
        if event.widget.get() == AuthenticationType.AuthenticationTypeDictionary.get('SqlServerAuthentication', {}):
            self.__login.configure(state="normal")
            self.__password.configure(state="normal")
        else:
            self.__login.configure(state="disabled")
            self.__password.configure(state="disabled")

    def __Close(self):
        self.ex

    def __Connect(self):
        pass
        # d= InformationFrame.callback


