from .startBtn import startBtnController
from .pauseBtn import pauseBtnController
from .resetBtn import resetBtnController
from .minuteBtn import minuteBtnController
from .timerLabel import timerLabelController
from .timerCanvas import timerCanvasController
from tkinter import *
from tkinter import messagebox

class Controller:
    """
    Link between model and view
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        # print(f"\nView for controller component {self.view}\n") # test

        self.seconds = self.model.seconds
        self.is_running = self.model.is_running
        self.time_format = self.model.time_format
        self.extent_decrement = 0

    def initialize_view(self) -> None:
        """
        Initialize view
        """

        self.start_btn_controller = startBtnController(self.model, self.view)
        self.pause_btn_controller = pauseBtnController(self.model, self.view)
        self.reset_btn_controller = resetBtnController(self.model, self.view)
        self.minute_btn_controller = minuteBtnController(self.model, self.view)
        self.timer_label_controller = timerLabelController(self.model, self.view)
        self.timer_canvas_controller = timerCanvasController(self.model, self.view)

        self.timer_label_controller.view = self.view

    def get_seconds(self) -> int:
        """
        Get seconds from model

        :return: The number of seconds
        """

        self.seconds = self.model.get_seconds()

        # print(f"From controller --> Timer: {self.seconds}")

        return self.seconds
    
    def get_state(self) -> bool:
        """
        Get state from model

        :return: boolean value, True if timer is running, False otherwise
        """

        self.is_running = self.model.get_state()

        # print(f"From controller --> Running: {self.is_running}")

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

                # update seconds

                self.get_seconds()

                self.update_timer()

                self.timer_label_controller.configure_after_id(func=self.countdown)

                # self.timer_canvas_controller.test()

            else:
                self.model.reset()

                # update values

                self.get_state()
                self.get_seconds()

                # show pop-up to display the end of the timer

                messagebox.showinfo("End", message="Time is up.")

                # manage buttons behavior

                self.start_btn_controller.enable()
                self.pause_btn_controller.disable()
                self.reset_btn_controller.enable()
                self.minute_btn_controller.enable()

    def decrease_canvas(self) -> None:
        """
        Decrease extent of timer canvas
        """

        if self.is_running:
            if self.seconds > 0:

                print(self.extent_decrement)
                
                self.update_timer_canvas(decrement=self.extent_decrement)

                self.timer_canvas_controller.configure_after_id(func=self.decrease_canvas)

            else:
                self.timer_canvas_controller.reset()
                self.extent_decrement = 0

    def update_timer_canvas(self, decrement) -> None:
        """
        Update timer canvas: arc displaying flow of time
        """

        self.timer_canvas_controller.update(decrement=decrement)

    def get_extent_decrement(self) -> float:
        """
        Compute the increment for the extent in timer canvas
        Example: if seconds are 60 --> every second the extent decrements by 6 degrees

        360 / self.seconds

        :return: float extent decrement
        """

        seconds = self.get_seconds()
        if seconds != 0:
            extent_decrement = float(360 / seconds)

            self.extent_decrement = extent_decrement

            return extent_decrement

    def on_click_start_btn(self) -> None:
        """
        Actions to perform when start button is clicked
        Timer doesn't start if timer seconds are 0
        """

        self.get_seconds()

        if self.extent_decrement == 0:
            self.get_extent_decrement()

        if self.seconds > 0:
            # print("\nTimer is ready to run.\n") # test

            if not self.is_running:
                self.model.run_timer()

                # update values

                self.get_state()
            
                # self.start_btn_controller.test() # test

                # print(f"From controller: new state running {self.is_running}")

                self.timer_label_controller.configure_after_id(func=self.countdown)
                self.timer_canvas_controller.configure_after_id(func=self.decrease_canvas)

                # manage buttons behavior

                self.start_btn_controller.disable()
                self.pause_btn_controller.enable()
                self.reset_btn_controller.disable()
                self.minute_btn_controller.disable()
        
        elif self.seconds == 0:
            # print("\nAdd seconds to start the timer.\n")
            messagebox.showinfo(title="Invalid Timer Setting",
                                message="Please set a valid tiem before starting the timer.")

    def on_click_pause_btn(self) -> None:
        """
        Actions to perform when pause button is clicked
        """

        # self.pause_btn_controller.test() # test

        if self.is_running:
            self.model.pause_timer()
            self.get_state()
            # print(f"From controller: new state running {self.is_running}")
            self.timer_label_controller.stop_after_id()
            self.timer_canvas_controller.stop_after_id()

        # manage buttons behavior

        self.start_btn_controller.enable()
        self.pause_btn_controller.disable()
        self.reset_btn_controller.enable()

    def on_click_reset_btn(self) -> None:
        """
        Actions to perform when reset button is clicked
        """

        # self.reset_btn_controller.test() # test
        self.model.reset()
        self.update_timer()
        self.timer_label_controller.stop_after_id()
        self.timer_canvas_controller.reset()

        self.timer_canvas_controller.stop_after_id()
        self.extent_decrement = 0

        # update values

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
        self.timer_label_controller.test()

        # manage buttons behavior

        self.reset_btn_controller.enable() 

    def update_timer(self) -> None:
        """
        Update timer

        :param new_value: new text to display in the timer label
        """

        new_value = self.get_format()
        self.timer_label_controller.update(new_value)

