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

        self.btn_1 = minuteBtn(self, text="1 mins")
        self.btn_1.grid(row=0, column=0)

        self.btn_2 = minuteBtn(self, text="5 mins")
        self.btn_2.grid(row=0, column=1)

        self.btn_3 = minuteBtn(self, text="10 mins")
        self.btn_3.grid(row=0, column=2)

        self.btn_4 = minuteBtn(self, text="20 mins")
        self.btn_4.grid(row=0, column=3)

        self.btn_5 = minuteBtn(self, text="60 mins")
        self.btn_5.grid(row=0, column=4)

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