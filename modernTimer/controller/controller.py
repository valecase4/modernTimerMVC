from .startBtn import startBtnController
from .pauseBtn import pauseBtnController
from .resetBtn import resetBtnController
from .minuteBtn import minuteBtnController
from .timerLabel import timerLabelController

class Controller:
    """
    Link between model and view
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        print(f"\nView for controller component {self.view}\n") # test

        self.seconds = self.model.seconds
        self.is_running = self.model.is_running
        self.time_format = self.model.time_format

    def initialize_view(self) -> None:
        """
        Initialize view
        """

        self.start_btn_controller = startBtnController(self.model, self.view)
        self.pause_btn_controller = pauseBtnController(self.model, self.view)
        self.reset_btn_controller = resetBtnController(self.model, self.view)
        self.minute_btn_controller = minuteBtnController(self.model, self.view)
        self.timer_label_controller = timerLabelController(self.model, self.view)

        self.timer_label_controller.view = self.view

    def get_seconds(self) -> int:
        """
        Get seconds from model

        :return: The number of seconds
        """

        self.seconds = self.model.get_seconds()

        return self.seconds
    
    def get_format(self) -> str:
        """
        Transform self.seconds into HH:MM:SS format
        """

        seconds = self.get_seconds()
        time_format = self.model.converter(seconds)

        return time_format

    def on_click_start_btn(self) -> None:
        """
        Actions to perform when start button is clicked
        """

        self.start_btn_controller.test() # test

    def on_click_pause_btn(self) -> None:
        """
        Actions to perform when pause button is clicked
        """

        self.pause_btn_controller.test() # test

    def on_click_reset_btn(self) -> None:
        """
        Actions to perform when reset button is clicked
        """

        self.reset_btn_controller.test() # test

    def on_click_minute_btn(self, value) -> None:
        """
        Actions to perform when a minute button is clicked
        """

        self.minute_btn_controller.test(value) # test
        self.model.add_time(value)
        self.update_timer()
        # self.timer_label_controller.test()

    def update_timer(self) -> None:
        """
        Update timer

        :param new_value: new text to display in the timer label
        """

        new_value = self.get_format()
        self.timer_label_controller.update(new_value)

