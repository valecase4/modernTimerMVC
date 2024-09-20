from tkinter import *
from .frames.main import mainFrame

class View(Tk):
    """
    View
    """

    def __init__(self, controller) -> None:
        super().__init__()

        self.controller = controller

        self.WIDTH = 800
        self.HEIGHT = 400

        self.title("Timer")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)

        self.main_frame = mainFrame(self, self.controller)
        self.main_frame.pack()

