from tkinter import *
from .frames.main import mainFrame

class View(Tk):
    """
    View
    """

    def __init__(self) -> None:
        super().__init__()

        self.WIDTH = 800
        self.HEIGHT = 400

        self.title("Timer")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)

        self.main_frame = mainFrame(self)
        self.main_frame.pack()

