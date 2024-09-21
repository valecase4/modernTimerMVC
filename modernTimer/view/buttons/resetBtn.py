from tkinter import *

class resetBtn(Canvas):
    """
    Reset button that resets timer when clicked
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            width=190,
            height=50,
            background="#303030",
            highlightthickness=0,
            border=0,
            cursor="hand2"
        )

        self.text = self.create_text(95, 25, text="Reset", fill="#e1e1e1", font=("Arial", 15))

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))
        self.bind("<Button>", lambda e : self.on_click(e))

    def grid(self, *args, **kwargs) -> None:
        """
        Override grid method
        """

        kwargs["row"] = 5
        kwargs["column"] = 0
        kwargs["padx"] = 30
        kwargs["sticky"] = "nw"

        return super().grid(*args, **kwargs)
    
    def on_enter(self, event) -> None:
        """
        Create effect when the mouse cursor is on button
        """

        self.configure(
            bg="red",
            width=210,
            height=52
        )

        self.itemconfig(self.text, fill="#ffffff", font=("Arial", 15, "bold"))
        self.coords(self.text, 105, 26)

    def on_leave(self, event) -> None:
        """
        Create effect when the mouse cursor leaves the button
        """

        self.configure(
            bg="#303030",
            width=190,
            height=50
        )

        self.itemconfig(self.text, fill="#e1e1e1", font=("Arial", 15, "normal"))
        self.coords(self.text, 95, 25)

    def on_click(self, event) -> None:
        """
        Call on_click_reset_btn() defined in controller
        """

        self.controller.on_click_reset_btn()