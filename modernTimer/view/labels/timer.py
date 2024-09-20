from tkinter import *

class Timer(Label):
    """
    Label showing the flow of time
    """

    def __init__(self, master) -> None:
        super().__init__(master)

        self.master = master

        self.configure(
            text="15:00",
            bg="#000000",
            fg="#ffffff",
            font=("Arial", 56, "normal"),
            cursor="hand2",
        )

    def grid(self, *args, **kwargs) -> None:
        """
        Override grid method
        """

        kwargs["row"] = 1
        kwargs["column"] = 0
        kwargs["sticky"] = "nw"
        kwargs["padx"] = 25

        return super().grid(*args, **kwargs)

