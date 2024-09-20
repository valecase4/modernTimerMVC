from .minutesBtn import minutesBtnController
from .startBtn import startBtnController
from .resetBtn import resetBtnController
from .timerLabel import timerLabelController
from .pauseBtn import pauseBtnController

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.minutes_btn_controller = minutesBtnController(self.model, self.view)
        self.start_btn_controller = startBtnController(self.model, self.view)
        self.reset_btn_controller = resetBtnController(self.model, self.view)
        self.timer_label_controller = timerLabelController(self, self.model, self.view)
        self.pause_btn_controller = pauseBtnController(self.model, self.view)

    def initialize_views(self):
        self.minutes_btn_controller.view = self.view
        self.start_btn_controller.view = self.view
        self.reset_btn_controller.view = self.view
        self.timer_label_controller.view = self.view
        self.pause_btn_controller.view = self.view

    def on_click_minutes_btn(self, seconds):
        self.minutes_btn_controller.add_time(seconds)
        self.timer_label_controller.update_timer()

    def on_click_start_btn(self):
        if self.model.seconds > 0:
            self.start_btn_controller.start_timer()
            self.minutes_btn_controller.disable()
            self.start_btn_controller.disable()
            self.reset_btn_controller.disable()
            self.pause_btn_controller.enable()
            self.timer_label_controller.update_timer()
            self.timer_label_controller.start_countdown()
        else:
            print("Add seconds please.")

    def on_click_reset_btn(self):
        self.reset_btn_controller.reset_timer()
        self.timer_label_controller.update_timer()
        self.minutes_btn_controller.enable()
        self.reset_btn_controller.disable()
        self.start_btn_controller.enable()
        self.timer_label_controller.stop_countdown()

    def on_click_pause_btn(self):
        self.pause_btn_controller.pause_timer()
        self.pause_btn_controller.disable()
        self.start_btn_controller.enable()
        self.reset_btn_controller.enable()
        self.timer_label_controller.stop_countdown()

    def on_end_timer(self):
        if self.model.seconds == 0:
            self.start_btn_controller.enable()
            self.pause_btn_controller.disable()
            self.reset_btn_controller.disable()
            self.minutes_btn_controller.enable()

    

    


    
