class pauseBtnController:
    """
    Controller component for pause button
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        self.pause_btn = self.view.main_frame.mid_frame.mid_frame_right.timer_canvas.pause_btn

    def test(self) -> None:
        """
        Implemented for testing the click on the start button
        """

        # print("\n")
        # print("Button pause clicked")
        # print("\n")

    def disable(self) -> None:
        """
        Disable button
        """

        self.pause_btn.disable()
        
    def enable(self) -> None:
        """
        Enable button
        """

        self.pause_btn.enable()