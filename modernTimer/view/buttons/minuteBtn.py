from tkinter import *

class minuteBtn(Canvas):
    """
    Minute Btn: add time to the timer when clicked
    """

    def __init__(self, master, controller, text: str, value: int) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller
        self.text = text
        self.value = value

        self.configure(
            width=100,
            height=50,
            bg="#b3b4b8",
            cursor="hand2",
            highlightthickness=0,
            border=0
        )

        self.canvas_text = self.create_text(50, 25, text=self.text, fill="#e8e8ea", font=("Arial", 14, "bold"))

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))
        self.bind("<Button>", lambda e : self.on_click(e))

    def grid(self, *args, **kwargs) -> None:
        """
        Override grid method
        """

        kwargs["padx"] = 30
        kwargs["pady"] = 25

        return super().grid(*args, **kwargs)
    
    def on_enter(self, event) -> None:
        """
        Create effect when the mouse cursor is actually on canvas
        """

        self.configure(
            bg="#184d6c"
        )

        self.itemconfig(self.canvas_text, fill="#0bdaf4")

    def on_leave(self, event) -> None:
        """
        Create effect when the mouse cursor leaves the canvas
        """

        self.configure(
            bg="#b3b4b8"
        )

        self.itemconfig(self.canvas_text, fill="#e8e8ea")

    def on_click(self, event) -> None:
        """
        Call on_click_minute_btn() defined in controller
        """

        self.controller.on_click_minute_btn(self.value)

    def disable(self) -> None:
        """
        Disable button
        """

        self.configure(
            bg="#b0b0b0"
        )

        self.itemconfig(self.canvas_text, fill="#6e6d6d")

        self.unbind("<Enter>")
        self.unbind("<Leave>")
        self.unbind("<Button>")

    def enable(self) -> None:
        """
        Enable button
        """

        self.configure(
            bg="#b3b4b8"
        )


        self.itemconfig(self.canvas_text, fill="#e8e8ea")

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))
        self.bind("<Button>", lambda e : self.on_click(e))




