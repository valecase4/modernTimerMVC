from tkinter import *

class resetBtn(Button):
    def __init__(self, master, controller):
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            text="RESET",
            font=("Arial", 30),
            cursor="hand2",
            bg="red",
            fg="#ffffff",
            command=self.controller.on_click_reset_btn
        )

    def enable(self):
        self.configure(
            bg="red",
            fg="#ffffff",
            state="normal"
        )

    def disable(self):
        self.configure(
            bg="gray",
            fg="#000000",
            state="disabled"
        )
