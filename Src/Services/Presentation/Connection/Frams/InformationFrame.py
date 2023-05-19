import tkinter as tk
from tkinter import ttk

from Src.Infrastructure.Presentation.BaseFrame import BaseFrame
from Src.Infrastructure.Presentation.BaseWidgets import BaseWidgets
from Src.Infrastructure.ReadOnly.AuthenticationType import AuthenticationType
from tkinter import *

from Src.Services.Domain.Models.Instances.Instances import Instances
from Src.Services.Share.ShareInstance import ShareInstance


class InformationFrame(BaseFrame):

    __login, __password, __serverAuthenticationType, __serverName = None, None, None, None

    def __init__(self, parent: BaseWidgets):
        super().__init__(parent)

    def Create(self):
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=2, pad=30)
        # self.rowconfigure(0, weight=1, pad=0)

        master = self.Parent

        ttk.Label(master, text="Server Name:", font=('Aerial bold', 10)).grid(column=0, row=1, sticky=W)
        self.__serverName = ttk.Entry(master, width=40)
        self.__serverName.focus()
        self.__serverName.grid(column=1, row=1)

        ttk.Label(master, text="Authentication:", font=('Aerial bold', 10)).grid(column=0, row=2, sticky=W)
        self.__serverAuthenticationType = ttk.Combobox(master, state="readonly", width=37)
        self.__serverAuthenticationType.bind("<<ComboboxSelected>>", self.__AuthenticationTypeChanged)
        self.__serverAuthenticationType['values'] = list(AuthenticationType.AuthenticationTypeDictionary.values())
        self.__serverAuthenticationType.grid(column=1, row=2)
        self.__serverAuthenticationType.current(0)

        ttk.Label(master, text="login:", font=('Aerial bold', 10)).grid(column=0, row=3, sticky=W)
        self.__login = ttk.Entry(master, width=40, state="disabled")
        self.__login.grid(column=1, row=3)

        ttk.Label(master, text="password:", font=('Aerial bold', 10)).grid(column=0, row=4, sticky=W)
        self.__password = ttk.Entry(master, width=40, state="disabled", show='*')
        self.__password.grid(column=1, row=4)

        cv = Canvas(master, width=480, height=10)
        cv.create_line(0, 10, 480, 10, fill="#c1c1c1", width=1)
        cv.grid(column=0, columnspan=2)

        _connect = ttk.Button(master, text="Connect", command=self.__Connect)
        _connect.grid(column=0, row=6)

        _cancel = ttk.Button(master, text="Cancel", command=self.__Close)
        _cancel.grid(column=1, row=6, sticky=W)

    def __AuthenticationTypeChanged(self, event):
        if event.widget.get() == AuthenticationType.AuthenticationTypeDictionary.get('SqlServerAuthentication', {}):
            self.__login.configure(state="normal")
            self.__password.configure(state="normal")
        else:
            self.__login.configure(state="disabled")
            self.__password.configure(state="disabled")

    def __Close(self):
        self.Parent.Close()

    def __Connect(self):
        # d= InformationFrame.callback
        instance: Instances = Instances()
        instance.Login = 'login Name'
        instance.Password = 'Pass'
        instance.ServerName = 'Server'
        instance.ServerAuthenticationType = 'SqlServerAuthentication'

        ShareInstance.instances.append(instance)
        self.__Close()


