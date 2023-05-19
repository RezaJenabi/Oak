from tkinter import *

from Src.Infrastructure.Presentation.BaseFrame import BaseFrame
from Src.Infrastructure.Presentation.BaseWidgets import BaseWidgets


class HeaderFrame(BaseFrame):

    def __init__(self, parent: BaseWidgets):
        super().__init__(parent)

    def Create(self):
        master = self.Parent
        cv = Canvas(master, width=480, height=65)
        cv.create_text(240, 30,
                       anchor=CENTER,
                       text="SQL Server",
                       fill="#383838",
                       font=('Segoe UI', 25))
        cv.create_line(0, 65, 480, 65, fill="#fe8718", width=3)
        cv.grid(column=0, row=0, columnspan=2)
