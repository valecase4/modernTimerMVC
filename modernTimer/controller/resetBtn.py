class resetBtnController:
    """
    Controller component for reset button
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        self.reset_btn = self.view.main_frame.mid_frame.mid_frame_left.reset_btn

    def test(self) -> None:
        """
        Implemented for testing the click on the reset button
        """

        print("\n")
        print("Button reset clicked")
        print("\n")

    def disable(self) -> None:
        """
        Disable button
        """

        self.reset_btn.disable()
        
    def enable(self) -> None:
        """
        Enable button
        """

        self.reset_btn.enable()