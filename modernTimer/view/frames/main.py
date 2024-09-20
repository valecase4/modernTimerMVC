from tkinter import *
from .topFrame import topFrame
from .midFrame import midFrame

class mainFrame(Frame):
    """
    Main frame: same size of root window
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            width=800,
            height=400,
            bg="#ffffff"
        )

        self.top_frame = topFrame(self, self.controller)
        self.top_frame.pack()

        self.mid_frame = midFrame(self, self.controller)
        self.mid_frame.pack()

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["expand"] = True
        kwargs["fill"] = "both"

        return super().pack(*args, **kwargs)
    
