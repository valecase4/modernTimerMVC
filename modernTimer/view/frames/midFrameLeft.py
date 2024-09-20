from tkinter import *

class midFrameLeft(Frame):
    """
    Mid Frame Left: displaying the flow of time and containing reset button
    """

    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.configure(
            width=380,
            height=380,
            bg="#000000"
        )

    def grid(self, *args, **kwargs):
        """
        Override grid method
        """

        kwargs["row"] = 0
        kwargs["column"] = 0
        kwargs["padx"] = 10
        kwargs["pady"] = 10

        return super().grid(*args, **kwargs)
