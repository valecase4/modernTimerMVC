from tkinter import *

class topFrame(Frame):
    """
    Top Frame containing some buttons: 1 mins, 5 mins, 10 mins, 20 mins, 60 mins 
    """

    def __init__(self, master) -> None:
        super().__init__(master)

        self.master = master

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