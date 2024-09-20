from tkinter import *

class startBtn(Canvas):
    """
    Start button: when clicked, timer starts
    """

    def __init__(self, master) -> None:
        super().__init__(master)

        self.master = master

        self.configure(
            width=60,
            height=60,
            bg="#303030",
            cursor="hand2",
            highlightthickness=0,
            border=0
        )

        self.icon = self.create_polygon(
            15, 15, 15, 45, 45, 30, fill="#ffffff"
        )

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["padx"] = 0
        kwargs["pady"] = (70, 0)

        return super().pack(*args, **kwargs)

    def on_enter(self, event) -> None:
        """
        Create effect when the mouse cursor is on button
        """

        self.configure(
            background="#018f27"
        )

    def on_leave(self, event) -> None:
        """
        Create effect when the mouse cursor leaves the button
        """

        self.configure(
            background="#303030"
        )