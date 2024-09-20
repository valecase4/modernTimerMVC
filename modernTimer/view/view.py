from tkinter import *

class View(Tk):
    """
    View
    """

    def __init__(self):
        super().__init__()

        self.WIDTH = 800
        self.HEIGHT = 400

        self.title("Timer")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)

