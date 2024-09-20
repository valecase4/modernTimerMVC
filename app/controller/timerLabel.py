from ..model.utils import converter

class timerLabelController:
    def __init__(self, parent, model, view):
        self.parent = parent
        self.model = model
        self.view = view

    def update_timer(self):
        seconds = self.model.seconds

        self.view.timer.configure(text=converter(seconds))

    def start_countdown(self):
        self.view.timer.after_id = self.view.timer.after(1000, self.countdown)

    def stop_countdown(self):
        if self.view.timer.after_id:
            self.view.timer.after_cancel(self.view.timer.after_id)
            self.view.timer.after_id = None

    def countdown(self):
        self.model.countdown()
        self.update_timer()
        self.start_countdown()

        self.parent.on_end_timer()


    