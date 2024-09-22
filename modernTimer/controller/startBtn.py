class startBtnController:
    """
    Controller component for start button
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        self.start_btn = self.view.main_frame.mid_frame.mid_frame_right.timer_canvas.start_btn

    def test(self) -> None:
        """
        Implemented for testing the click on the start button
        """

        print("\n")
        print("Button start clicked")
        print("\n")

    def disable(self) -> None:
        """
        Disable button
        """

        self.start_btn.disable()
        
    def enable(self) -> None:
        """
        Enable button
        """

        self.start_btn.enable()