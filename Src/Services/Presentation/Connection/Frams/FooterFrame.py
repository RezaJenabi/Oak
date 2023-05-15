from tkinter import ttk
from tkinter import *


class FooterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.__create_widgets()

    def __create_widgets(self):
        # cv = Canvas(self, width=480, height=50)
        #
        # cv.create_line(0, 0, 480, 0, fill="#fe8718", width=3)
        # cv.grid(column=0)
        label = ttk.Button(self,
                          text="Find what:")
        label.grid(column=0, row=0)