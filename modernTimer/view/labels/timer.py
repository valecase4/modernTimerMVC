from tkinter import *

class Timer(Label):
    """
    Label showing the flow of time
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller
        self.after_id = None

        self.configure(
            text=self.controller.time_format,
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
    
    def update_test(self) -> None:
        """
        Update timer view when a minute button is clicked (testing)
        """

        print("Timer updated")

    def update(self, new_value) -> None:
        """
        Update timer view when a minute button is clicked

        :param new_value: new text to display in the timer label
        """

        self.configure(
            text=new_value
        )

    def configure_after_id(self, func) -> None:
        """
        After id manages the updates for the timer label

        :param func: function responsible for updating the timer (flow of time)
        """

        print("\nUpdated after id for timer label.\n")

        if not self.after_id:
            self.after(1000, func)

    def stop_after_id(self, func) -> None:
        """
        Stop after id: stop the flow of time

        :param func: function responsible for updating the timer (flow of time)
        """

        print("\nStopped after id for timer label.\n")
        
        if self.after_id:
            self.after_cancel(func)
            self.after_id = None
        else:
            print(f"After id is {self.after_id}")


