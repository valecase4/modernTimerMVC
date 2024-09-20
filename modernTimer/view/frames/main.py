from tkinter import *

class mainFrame(Frame):
    """
    Main frame: same size of root window
    """

    def __init__(self, master) -> None:
        super().__init__(master)

        self.master = master

        self.configure(
            width=800,
            height=400,
            bg="#ffffff"
        )

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["expand"] = True
        kwargs["fill"] = "both"

        return super().pack(*args, **kwargs)
    
