from tkinter import *

class startBtn(Button):
    def __init__(self, master, controller):
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            text="START",
            font=("Arial", 30),
            cursor="hand2",
            bg="lightgreen",
            fg="#ffffff",
            command=self.controller.on_click_start_btn
        )

    def enable(self):
        self.configure(
            bg="lightgreen",
            fg="#ffffff",
            state="normal"
        )

    def disable(self):
        self.configure(
            bg="gray",
            fg="#000000",
            state="disabled"
        )

