from tkinter import *

class MinutesBtn(Button):
    """
    Buttons for adding time to the timer
    """

    def __init__(self, master, controller, text: str, value: int) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller
        self.text = text
        self.value = value

        self.configure(
            text=self.text,
            bg="#e3e3e3",
            fg="#ffffff",
            font=("Arial", 30),
            highlightthickness=0,
            border=0,
            cursor="hand2",
            command=lambda : self.controller.on_click_minutes_btn(self.value)
        )

    def disable(self):
        self.configure(
            bg="gray",
            fg="#000000",
            state="disabled"
        )

    def enable(self):
        self.configure(
            bg="#e3e3e3",
            fg="#ffffff",
            state="normal"
        )