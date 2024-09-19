class timerLabelController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        print("This is view for timerLabelController", self.view)

    def update_timer(self):
        seconds = self.model.seconds

        self.view.timer.configure(text=seconds)