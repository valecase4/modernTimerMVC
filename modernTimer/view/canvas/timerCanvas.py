from tkinter import *
from ..buttons.startBtn import startBtn
from ..buttons.pauseBtn import pauseBtn

class timerCanvas(Canvas):
    """
    Canvas containing timer canvas, start button and pause button
    """

    def __init__(self, master) -> None:
        super().__init__(master)

        self.master = master

        self.pack_propagate(False)

        self.configure(
            width=380,
            height=380,
            bg="#184d6c",
            highlightthickness=0,
            border=0
        )

        self.timer_canvas_bg = self.create_arc(
            75, 25, 305, 255, start=90, extent=359.99, fill="#12374d", outline="#12374d", width=25, style=ARC
        )

        self.timer_canvas = self.create_arc(
            75, 25, 305, 255, start=90, extent=300, fill="#0cdcf8", outline="#0cdcf8", width=25, style=ARC
        )

        self.start_btn = startBtn(self)
        self.start_btn.pack()

        self.pause_btn = pauseBtn(self)
        self.pause_btn.pack()

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["expand"] = True
        kwargs["fill"] = "both"

        return super().pack(*args, **kwargs)
