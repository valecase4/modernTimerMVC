class minuteBtnController:
    """
    Controller component for the minutes buttons (1 mins, 5 mins, 10 mins etc...)
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        self.all_minute_btns = self.view.main_frame.top_frame.all_minute_btns

    def test(self, value) -> None:
        """
        Implemented for testing the click on the minutes buttons
        """

        print("\n")
        print(f"Minute button clicked {value}")
        print("\n")

    def disable(self) -> None:
        """
        Disable buttons
        """

        for btn in self.all_minute_btns:
            btn.disable()

    def enable(self) -> None:
        """
        Enable buttons
        """

        for btn in self.all_minute_btns:
            btn.enable()
