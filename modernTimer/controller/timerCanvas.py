class timerCanvasController:
    """
    Controller component for the timer canvas: circle that displays the flow of time
    Placed in the mid right frame
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        self.timer_canvas = self.view.main_frame.mid_frame.mid_frame_right.timer_canvas

    def test(self) -> None:
        """
        Implemented for test
        """

        self.timer_canvas.test()

    def update(self, decrement) -> None:
        self.timer_canvas.update(decrement)

    def reset(self) -> None:
        self.timer_canvas.reset()

    def configure_after_id(self, func) -> None:
        
        self.timer_canvas.configure_after_id(func)

    def stop_after_id(self) -> None:

        self.timer_canvas.stop_after_id()