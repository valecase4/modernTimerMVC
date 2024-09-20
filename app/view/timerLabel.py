from tkinter import *

class timerLabel(Label):
    def __init__(self, master, controller):
        super().__init__(master)

        self.master = master
        self.controller = controller
        self.after_id = None

        self.configure(
            text=self.controller.model.seconds, 
            font=("Arial", 30), 
            bg="#ffffff"
        )
