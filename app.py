from tkinter import *

class Model:
    """
    Backend
    """

    def __init__(self) -> None:
        self.seconds = 0
    
    def __repr__(self) -> str:
        """
        For testing
        """

        return f"Timer is now {self.seconds}"
    
    def add_time(self, seconds) -> None:
        self.seconds += seconds

    def get_current_seconds(self) -> int:
        return self.seconds

    def converter(self) -> str:
        total_seconds = self.get_current_seconds()

        hours = int(total_seconds / 3600)
        minutes = 0
        seconds = 0

        hours_remainder = total_seconds % 3600

        if hours_remainder != 0:
            minutes = int(hours_remainder / 60)

            minutes_remainder = hours_remainder % 60

            if minutes_remainder != 0:
                seconds = minutes_remainder

        hours = f"0{hours}" if len(str(hours)) == 1 else f"{hours}"
        minutes = f"0{minutes}" if len(str(minutes)) == 1 else f"{minutes}"
        seconds = f"0{seconds}" if len(str(seconds)) == 1 else f"{seconds}"

        return f"{hours}:{minutes}:{seconds}"
    
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

        print(self.controller.get_current_time())

        self.timer = Label(self, text=self.controller.get_current_time())
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
        current_time = self.model.converter()

        return current_time

    def update_timer_view(self) -> None:
        current_time = self.get_current_time()

        self.view.timer.configure(text=current_time)


def converter(total_seconds) -> str:
    hours = int(total_seconds / 3600)
    minutes = 0
    seconds = 0

    hours_remainder = total_seconds % 3600

    if hours_remainder != 0:
        minutes = int(hours_remainder / 60)

        minutes_remainder = hours_remainder % 60

        if minutes_remainder != 0:
            seconds = minutes_remainder

    hours = f"0{hours}" if len(str(hours)) == 1 else f"{hours}"
    minutes = f"0{minutes}" if len(str(minutes)) == 1 else f"{minutes}"
    seconds = f"0{seconds}" if len(str(seconds)) == 1 else f"{seconds}"

    return f"{hours}:{minutes}:{seconds}"


print(converter(3900))