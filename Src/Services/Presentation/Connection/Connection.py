import tkinter as tk
from Src.Services.Presentation.Connection.Frams.HeaderFrame import HeaderFrame, InputFrame, ButtonFrame


class Connection(tk.Tk):

    def __init__(self):
        super().__init__()
        self.__Init()
        self.__Create()

    def __Init(self):
        self.title('Connect to Server')

    def __Create(self):
        self.__Screen()
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=1)
        self.__create_widgets()
        self.mainloop()

    def __Screen(self):
        window_width = 800
        window_height = 800
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.attributes('-toolwindow', True)

    def __create_widgets(self):
        # create the input frame
        headerFrame = HeaderFrame(self)
        headerFrame.grid(column=0, row=0)

        # create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=1)

        # create the button frame
        button_frame = ButtonFrame(self)
        button_frame.grid(column=0, row=2)
