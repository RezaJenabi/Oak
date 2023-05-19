from tkinter import ttk

from Src.Infrastructure.Presentation.BaseWidgets import BaseWidgets


class BaseFrame(ttk.Frame):
    _parent: BaseWidgets = None

    @property
    def Parent(self):
        return self._parent

    @Parent.setter
    def Parent(self, value):
        self._parent = value

    def __init__(self, parent: BaseWidgets):
        super().__init__()
        self.Parent = parent
        self.Create()

    def Create(self):
        pass



