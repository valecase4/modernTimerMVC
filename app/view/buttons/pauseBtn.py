from tkinter import *

class pauseBtn(Button):
    def __init__(self, master, controller):
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            text="PAUSE",
            font=("Arial", 30),
            cursor="hand2",
            bg="gray",
            fg="#ffffff",
            command=self.controller.on_click_pause_btn,
            state="disabled"
        )

    def enable(self):
        self.configure(
            bg="orange",
            fg="#ffffff",
            state="normal"
        )

    def disable(self):
        self.configure(
            bg="gray",
            fg="#000000",
            state="disabled"
        )
