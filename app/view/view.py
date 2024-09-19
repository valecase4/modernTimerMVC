from tkinter import *
from .buttons.minutesBtn import MinutesBtn

class View(Tk):
    """
    View
    """

    def __init__(self, controller) -> None:
        super().__init__()

        self.controller = controller

        self.geometry("800x400")
        self.title("Timer")
        self.configure(bg="#ffffff")
        self.resizable(False, False)

        self.grid_propagate(False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.one_min_btn = MinutesBtn(self, self.controller, "1 mins", 60) 
        self.one_min_btn.grid(row=0, column=0)

        self.five_min_btn = MinutesBtn(self, self.controller, "5 mins", 300) 
        self.five_min_btn.grid(row=0, column=1)

        self.ten_min_btn = MinutesBtn(self, self.controller, "10 mins", 600) 
        self.ten_min_btn.grid(row=0, column=2)

        self.twenty_min_btn = MinutesBtn(self, self.controller, "20 mins", 1200) 
        self.twenty_min_btn.grid(row=0, column=3)

        self.sixty_min_btn = MinutesBtn(self, self.controller, "60 mins", 3600) 
        self.sixty_min_btn.grid(row=0, column=4)

        self.start_btn = Button(self, text="START", font=("Arial", 30))
        self.start_btn.configure(command=self.controller.on_click_start_btn)
        self.start_btn.grid(row=1, column=0, columnspan=5)

        self.reset_btn = Button(self, text="RESET", font=("Arial", 30), bg="red", fg="#ffffff")
        self.reset_btn.configure(command=self.controller.on_click_reset_btn)
        self.reset_btn.grid(row=2, column=0, columnspan=5)

        self.timer = Label(self, text="00:00", font=("Arial", 30), bg="#ffffff")
        self.timer.grid(row=3, column=0, columnspan=5)




