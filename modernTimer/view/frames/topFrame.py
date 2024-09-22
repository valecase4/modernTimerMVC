from tkinter import *
from ..buttons.minuteBtn import minuteBtn

class topFrame(Frame):
    """
    Top Frame containing some buttons: 1 mins, 5 mins, 10 mins, 20 mins, 60 mins 
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

        self.btn_1 = minuteBtn(self, self.controller, "1 mins", 60)
        self.btn_1.grid(row=0, column=0)

        self.btn_2 = minuteBtn(self, self.controller, "5 mins", 300)
        self.btn_2.grid(row=0, column=1)

        self.btn_3 = minuteBtn(self, self.controller, "10 mins", 600)
        self.btn_3.grid(row=0, column=2)

        self.btn_4 = minuteBtn(self, self.controller, "20 mins", 1200)
        self.btn_4.grid(row=0, column=3)

        self.btn_5 = minuteBtn(self, self.controller, "60 mins", 3600)
        self.btn_5.grid(row=0, column=4)

        self.all_minute_btns = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5] # for controller component

        self.configure(
            width=800,
            height=100,
            bg="#ebebeb"
        )

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["padx"] = 0
        kwargs["pady"] = 0

        return super().pack(*args, **kwargs)