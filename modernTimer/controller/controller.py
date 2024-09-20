from .startBtn import startBtnController
from .pauseBtn import pauseBtnController
from .resetBtn import resetBtnController

class Controller:
    """
    Link between model and view
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

        self.start_btn_controller = startBtnController(self.model, self.view)
        self.pause_btn_controller = pauseBtnController(self.model, self.view)
        self.reset_btn_controller = resetBtnController(self.model, self.view)

    def on_click_start_btn(self) -> None:
        """
        Actions to perform when start button is clicked
        """

        self.start_btn_controller.test()

    def on_click_pause_btn(self) -> None:
        """
        Actions to perform when pause button is clicked
        """

        self.pause_btn_controller.test()

    def on_click_reset_btn(self) -> None:
        """
        Actions to perform when reset button is clicked
        """

        self.reset_btn_controller.test()

