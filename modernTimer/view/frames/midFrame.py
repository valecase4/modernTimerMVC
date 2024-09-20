from tkinter import *
from .midFrameLeft import midFrameLeft
from .midFrameRight import midFrameRight

class midFrame(Frame):
    """
    Mid frame: divided into Mid Frame Left and Mid Frame Right
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            width=800, 
            height=300,
            bg="#000000"
        )

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.mid_frame_left = midFrameLeft(self, self.controller)
        self.mid_frame_left.grid()

        self.mid_frame_right = midFrameRight(self, self.controller)
        self.mid_frame_right.grid()

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["expand"] = True
        kwargs["fill"] = "both"

        return super().pack(*args, **kwargs)

