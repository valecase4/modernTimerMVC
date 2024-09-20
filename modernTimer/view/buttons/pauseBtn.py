from tkinter import *

class pauseBtn(Canvas):
    """
    Pause button: when clicked, timer stops (pause state)
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

        self.icon = self.create_rectangle(20, 12.5, 27.5, 47.5, fill="#ffffff", outline="#ffffff")
        self.icon = self.create_rectangle(35, 12.5, 42.5, 47.5, fill="#ffffff", outline="#ffffff")

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["padx"] = 0
        kwargs["pady"] = 20

        return super().pack(*args, **kwargs)
    
    def on_enter(self, event) -> None:
        """
        Create effect when the mouse cursor is on button
        """

        self.configure(
            background="#fac039"
        )

    def on_leave(self, event) -> None:
        """
        Create effect when the mouse cursor leaves the button
        """

        self.configure(
            background="#303030"
        )