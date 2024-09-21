class minuteBtnController:
    """
    Controller component for the minutes buttons (1 mins, 5 mins, 10 mins etc...)
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def test(self, value) -> None:
        """
        Implemented for testing the click on the minutes buttons
        """

        print("\n")
        print(f"Minute button clicked {value}")
        print("\n")