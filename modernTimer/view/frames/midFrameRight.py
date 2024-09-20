from tkinter import *
from ..canvas.timerCanvas import timerCanvas

class midFrameRight(Frame):
    """
    Mid Frame Right: displaying the flow of time in timer canvas and containing start and pause buttons
    """

    def __init__(self, master) -> None:
        super().__init__(master)

        self.master = master

        self.grid_propagate(False)

        self.configure(
            width=380,
            height=380,
            bg="#184d6c"
        )

        self.timer_canvas = timerCanvas(self)
        self.timer_canvas.pack()

    def grid(self, *args, **kwargs) -> None:
        """
        Override grid method
        """

        kwargs["row"] = 0
        kwargs["column"] = 1
        kwargs["padx"] = 10
        kwargs["pady"] = 10

        return super().grid(*args, **kwargs)
