from tkinter import *

class startBtn(Button):
    def __init__(self, master, controller):
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            text="START",
            width=6,
            height=1,
            font=("Arial", 30),
            cursor="hand2",
            bg="lightgreen",
            fg="#ffffff",
            command=self.controller.on_click_start_btn
        )

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))

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

    def on_enter(self, event):
        self.configure(
            width=int(6 * 1.2),
            height=int(2 * 1.2)
        )

    def on_leave(self, event):
        self.configure(
            width=6,
            height=1
        )

