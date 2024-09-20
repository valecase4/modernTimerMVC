class pauseBtnController:
    """
    Controller component for pause button
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def test(self) -> None:
        """
        Implemented for testing the click on the start button
        """

        print("\n")
        print("Button pause clicked")
        print("\n")