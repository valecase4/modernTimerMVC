class timerLabelController:
    """
    Controller component for the label showing the flow of time
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        self.timer = self.view.main_frame.mid_frame.mid_frame_left.timer

    def test(self) -> None:
        """
        Implemented for testing: timer is updated when a minute button is clicked (testing)
        """

        self.timer.update_test()

    def update(self, new_value) -> None:
        """
        Timer is updated when a minute button is clicked
        Example: 5 mins is clicked -> timer label becomes 00:05:00

        :param new_value: new text to display in the timer label
        """

        self.timer.update(new_value)

    def configure_after_id(self, func) -> None:
        """
        Configure timer.after_id, that stores the countdown

        :param func: function responsible for updating the timer
        """

        self.timer.configure_after_id(func)

    def stop_after_id(self) -> None:
        """
        Stop timer.after_id. The flow of time is stopped when pause btn or reset button is clicked

        :param func: function responsible for updating the timer
        """

        self.timer.stop_after_id()

