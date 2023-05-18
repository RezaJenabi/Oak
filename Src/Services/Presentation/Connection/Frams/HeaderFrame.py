from tkinter import ttk
from tkinter import *

from Src.Infrastructure.Presentation.BaseFrame import BaseFrame
from Src.Infrastructure.Presentation.BaseWidgets import BaseWidgets


class HeaderFrame(BaseFrame):

    def __init__(self, parent: BaseWidgets):
        super().__init__(parent)

    def Create(self):
        cv = Canvas(self, width=480, height=70)
        cv.create_text(240, 30,
                       anchor=CENTER,
                       text="SQL Server",
                       fill="#383838",
                       font=('Segoe UI', 25))
        cv.create_line(0, 70, 480, 70, fill="#fe8718", width=3)
        cv.grid(column=0)
