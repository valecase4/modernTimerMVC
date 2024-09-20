class resetBtnController:
    """
    Controller component for reset button
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def test(self) -> None:
        """
        Implemented for testing the click on the reset button
        """

        print("\n")
        print("Button reset clicked")
        print("\n")