class timerLabelController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_timer(self):
        seconds = self.model.seconds

        self.view.timer.configure(text=seconds)

    def start_countdown(self):
        self.view.timer.after_id = self.view.timer.after(1000, self.countdown)

    def countdown(self):
        self.model.countdown()
        self.update_timer()