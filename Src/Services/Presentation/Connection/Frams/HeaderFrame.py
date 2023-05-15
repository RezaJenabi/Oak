from tkinter import ttk
from tkinter import *


class HeaderFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.__create_widgets()

    def __create_widgets(self):
        # cv = Canvas(self,  background="blue")
        # cv.create_rectangle(200, 200, 0, 0, fill="red")
        # cv.create_text(100, 100, text="SQL Server", fill="white")
        # cv.grid()
        cv = Canvas(self, width=480, height=70)
        cv.create_text(240, 30,
                       anchor=CENTER,
                       text="SQL Server",
                       fill="#383838",
                       font=('Segoe UI', 25))
        cv.create_line(0, 70, 480, 70, fill="#fe8718", width=3)
        cv.grid(column=0)
