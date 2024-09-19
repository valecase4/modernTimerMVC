from tkinter import *
from .buttons.minutesBtn import MinutesBtn

minutes_btns_text = ["1 mins", "5 mins", "10 mins", "20 mins", "60 mins"]
minutes_btns_values = [60, 300, 600, 1200, 3600]

class View(Tk):
    """
    View
    """

    def __init__(self, controller) -> None:
        super().__init__()

        self.controller = controller
        self.after_id = None

        self.configure(
            bg="#ffffff",
            width=800,
            height=400
        )

        self.grid_propagate(False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        for i in range(5):
            self.btn = MinutesBtn(self, self.controller, minutes_btns_text[i], minutes_btns_values[i])
            self.grid_columnconfigure(i, weight=1)
            self.btn.grid(row=0, column=i)

        self.start_btn = Button(self, text="START", font=("Arial", 30), command=self.controller.start_countdown)
        self.start_btn.grid(row=1, column=0, columnspan=5)

        self.timer = Label(self, text=self.controller.get_seconds(), bg="#ffffff", font=("Arial", 40))
        self.timer.grid(row=2, column=0, columnspan=5)



