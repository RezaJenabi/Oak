import tkinter as tk
from tkinter import ttk


class HeaderFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.__create_widgets()

    def __create_widgets(self):
        label = ttk.Label(self,
                          text="SQL Server",
                          font=('Aerial bold', 20))

        label.grid(column=0, row=0)


class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()

    def __create_widgets(self):
        # Find what
        ttk.Label(self, text='Find what:').grid(column=0, row=0, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)

        # Replace with:
        ttk.Label(self, text='Replace with:').grid(
            column=0, row=1, sticky=tk.W)
        replacement = ttk.Entry(self, width=30)
        replacement.grid(column=1, row=1, sticky=tk.W)

        # Match Case checkbox
        match_case = tk.StringVar()
        match_case_check = ttk.Checkbutton(
            self,
            text='Match case',
            variable=match_case,
            command=lambda: print(match_case.get()))
        match_case_check.grid(column=0, row=2, sticky=tk.W)

        # Wrap Around checkbox
        wrap_around = tk.StringVar()
        wrap_around_check = ttk.Checkbutton(
            self,
            variable=wrap_around,
            text='Wrap around',
            command=lambda: print(wrap_around.get()))
        wrap_around_check.grid(column=0, row=3, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)


class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Button(self, text='Find Next').grid(column=0, row=0)
        ttk.Button(self, text='Replace').grid(column=0, row=1)
        ttk.Button(self, text='Replace All').grid(column=0, row=2)
        ttk.Button(self, text='Cancel').grid(column=0, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)
