from tkinter import *
from ..labels.timer import Timer
from ..buttons.resetBtn import resetBtn

class midFrameLeft(Frame):
    """
    Mid Frame Left: displaying the flow of time and containing reset button
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.grid_propagate(False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

        self.grid_columnconfigure(0, weight=1)

        Label(self, 
              text="Timer", 
              fg="#878787", 
              bg="#000000", 
              font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="nw", padx=30, pady=(20, 0))
        
        self.timer = Timer(self)
        self.timer.grid()

        self.reset_btn = resetBtn(self, self.controller)
        self.reset_btn.grid()

        self.configure(
            width=380,
            height=380,
            bg="#000000"
        )

    def grid(self, *args, **kwargs) -> None:
        """
        Override grid method
        """

        kwargs["row"] = 0
        kwargs["column"] = 0
        kwargs["padx"] = 10
        kwargs["pady"] = 10

        return super().grid(*args, **kwargs)
