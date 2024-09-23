from .startBtn import startBtnController
from .pauseBtn import pauseBtnController
from .resetBtn import resetBtnController
from .minuteBtn import minuteBtnController
from .timerLabel import timerLabelController
from tkinter import *
from tkinter import messagebox

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

        print(f"From controller --> Timer: {self.seconds}")

        return self.seconds
    
    def get_state(self) -> bool:
        """
        Get state from model

        :return: boolean value, True if timer is running, False otherwise
        """

        self.is_running = self.model.get_state()

        print(f"From controller --> Running: {self.is_running}")

        return self.is_running
    
    def get_format(self) -> str:
        """
        Transform self.seconds into HH:MM:SS format
        """

        seconds = self.get_seconds()
        time_format = self.model.converter(seconds)

        return time_format

    def decrease(self) -> None:
        """
        decrease() method from model
        """

        self.model.decrease()

    def countdown(self) -> None:
        """
        Countdown: flow of time for timer
        """

        if self.is_running:
            if self.seconds > 0:
                self.decrease()
                self.get_seconds()
                self.update_timer()

                self.timer_label_controller.configure_after_id(func=self.countdown)

            else:
                self.model.reset()
                self.get_state()
                self.get_seconds()

                # manage buttons behavior

                self.start_btn_controller.enable()
                self.pause_btn_controller.disable()
                self.reset_btn_controller.enable()
                self.minute_btn_controller.enable()

    def on_click_start_btn(self) -> None:
        """
        Actions to perform when start button is clicked
        Timer doesn't start if timer seconds are 0
        """

        seconds = self.get_seconds()

        if seconds > 0:
            print("\nTimer is ready to run.\n") # test

            if not self.is_running:
                self.model.run_timer()
            
            self.start_btn_controller.test() # test
            self.get_state()
            self.timer_label_controller.configure_after_id(func=self.countdown)

            # manage buttons behavior

            self.start_btn_controller.disable()
            self.pause_btn_controller.enable()
            self.reset_btn_controller.disable()
            self.minute_btn_controller.disable()
        
        elif seconds == 0:
            print("\nAdd seconds to start the timer.\n")
            messagebox.showinfo(title="Invalid Timer Setting",
                                message="Please set a valid tiem before starting the timer.")

    def on_click_pause_btn(self) -> None:
        """
        Actions to perform when pause button is clicked
        """

        self.pause_btn_controller.test() # test

        if self.is_running:
            self.model.pause_timer()
            self.get_state()
            self.timer_label_controller.stop_after_id(self.countdown)

        # manage buttons behavior

        self.start_btn_controller.enable()
        self.pause_btn_controller.disable()
        self.reset_btn_controller.enable()

    def on_click_reset_btn(self) -> None:
        """
        Actions to perform when reset button is clicked
        """

        self.reset_btn_controller.test() # test
        self.model.reset()
        self.update_timer()
        self.get_seconds()
        self.get_state()

        # manage buttons behavior

        self.start_btn_controller.enable()
        self.reset_btn_controller.disable()
        self.minute_btn_controller.enable()

    def on_click_minute_btn(self, value) -> None:
        """
        Actions to perform when a minute button is clicked
        """

        self.minute_btn_controller.test(value) # test
        self.model.add_time(value)
        self.update_timer()
        self.reset_btn_controller.enable()
        # self.timer_label_controller.test()

    def update_timer(self) -> None:
        """
        Update timer

        :param new_value: new text to display in the timer label
        """

        new_value = self.get_format()
        self.timer_label_controller.update(new_value)

