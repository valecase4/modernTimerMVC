from tkinter import *

class Model:
    """
    Backend
    """

    def __init__(self) -> None:
        self.seconds = 400
    
    def __repr__(self) -> str:
        """
        For testing
        """

        return f"Timer is now {self.seconds}"
    
    def add_time(self, seconds) -> None:
        self.seconds += seconds

    def get_current_time(self) -> int:
        return self.seconds

    def converter(self, seconds) -> str:
        pass

class View(Tk):
    """
    UI
    """

    def __init__(self, controller) -> None:
        super().__init__()

        self.controller = controller

        self.WIDTH = 800
        self.HEIGHT = 400

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.title("Modern Timer")
        self.resizable(False, False)

        self.button = Button(self, text="5 mins")
        self.button.configure(
            command=lambda : self.controller.on_click_start(300)
        )
        self.button.pack()

        self.timer = Label(self, text=self.controller.model.seconds)
        self.timer.pack()


class Controller:
    """
    Controller
    """

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def on_click_start(self, value) -> None:
        self.add_time(value)
        self.update_timer_view()

    def add_time(self, seconds) -> None:
        print("Function add time is called")
        self.model.add_time(seconds)
        print(self.model)

    def get_current_time(self) -> None:
        current_time = self.model.get_current_time()

        return current_time

    def update_timer_view(self) -> None:
        current_time = self.get_current_time()

        self.view.timer.configure(text=current_time)

       