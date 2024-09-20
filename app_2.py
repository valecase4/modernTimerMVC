from tkinter import *

class TimerLabel(Label):
    def __init__(self, master, controller):
        super().__init__(master)

        self.master = master
        self.controller = controller
        self.after_id = None

class View(Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        

class Controller:
    pass

class Model:
    pass