import tkinter as tk


class BaseWidgets(tk.Tk):
    __title, _parent = None, None

    # @property
    # def Parent(self):
    #     return self._parent
    #
    # @Parent.setter
    # def Parent(self, value):
    #     self._parent = value

    def __init__(self, title):
        super().__init__()
        self.__title = title
        # self.Parent = parent
        self.Create()

    def __Init(self):
        self.title(self.__title)

    def Create(self):
        self.__Init()
        self.Screen()
        self.CreateFrames()

    def Screen(self, width=0, height=0, isFullScreen=True, isCenter=True, isResizable=True, backgroundColor='#f0f0f0',
               icon='./../Assets/Oak_clipartmax.ico'):
        windowWidth = width
        windowHeight = height
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        centerX, centerY = 0, 0
        if isFullScreen:
            windowWidth = screenWidth
            windowHeight = screenHeight
        if isCenter:
            centerX = int(screenWidth / 2 - windowWidth / 2)
            centerY = int(screenHeight / 2 - windowHeight / 2)

        self.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
        self.configure(background=backgroundColor)

        if isResizable is False:
            self.resizable(False, False)
        self.iconbitmap(icon)

    def CreateFrames(self):
        pass

    def Close(self):
        self.destroy()



