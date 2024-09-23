from tkinter import *
from ..buttons.startBtn import startBtn
from ..buttons.pauseBtn import pauseBtn

class timerCanvas(Canvas):
    """
    Canvas containing timer canvas, start button and pause button
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller
        self.after_id = None
        
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
            75, 25, 305, 255, start=90, extent=359.99, fill="#0cdcf8", outline="#0cdcf8", width=25, style=ARC
        )

        self.start_btn = startBtn(self, self.controller)
        self.start_btn.pack()

        self.pause_btn = pauseBtn(self, self.controller)
        self.pause_btn.pack()

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["expand"] = True
        kwargs["fill"] = "both"

        return super().pack(*args, **kwargs)
    
    def test(self) -> None:
        """
        Implemented for test
        """

        self.itemconfig(self.timer_canvas, extent=320)

    def reset(self) -> None:
        """
        Reset to the initial state: extent = 359.99
        """

        self.itemconfig(self.timer_canvas, extent=359.99)

    def update(self, decrement) -> None:
        """
        Updating timer canvas
        """
        current_extent = float(self.itemcget(self.timer_canvas, "extent"))
        self.itemconfig(self.timer_canvas, extent=current_extent - decrement)

    def configure_after_id(self, func) -> None:
        """
        Configure after id, that is responsible to update the canvas representing the flow of time

        :param func: function responsible for updating the canvas
        """

        self.after_id = self.after(1000, func)

    def stop_after_id(self) -> None:
        """
        Stop after_id. The flow of time is stopped when pause btn or reset button is clicked

        :param func: function responsible for updating the canvas
        """

        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None



