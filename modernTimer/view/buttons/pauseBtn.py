from tkinter import *

class pauseBtn(Canvas):
    """
    Pause button: when clicked, timer stops (pause state)
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            width=60,
            height=60,
            bg="#303030",
            cursor="hand2",
            highlightthickness=0,
            border=0
        )

        self.icon_left = self.create_rectangle(20, 12.5, 27.5, 47.5, fill="#ffffff", outline="#ffffff")
        self.icon_right = self.create_rectangle(35, 12.5, 42.5, 47.5, fill="#ffffff", outline="#ffffff")

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))
        self.bind("<Button>", lambda e : self.on_click(e))

        self.disable() # in the initial state, this button is disabled

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

    def on_click(self, event) -> None:
        """
        Call on_click_pause_btn() defined in controller
        """

        self.controller.on_click_pause_btn()

    def disable(self) -> None:
        """
        Disable button
        """

        self.config(
            bg="#b0b0b0"
        )

        self.itemconfig(self.icon_left, fill="#6e6d6d", outline="#6e6d6d")
        self.itemconfig(self.icon_right, fill="#6e6d6d", outline="#6e6d6d")

        self.unbind("<Enter>")
        self.unbind("<Leave>")
        self.unbind("<Button>")

    def enable(self) -> None:
        """
        Enable button
        """

        self.configure(
            bg="#303030"
        )

        self.itemconfig(self.icon_left, fill="#ffffff", outline="#ffffff")
        self.itemconfig(self.icon_right, fill="#ffffff", outline="#ffffff")

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))
        self.bind("<Button>", lambda e : self.on_click(e))