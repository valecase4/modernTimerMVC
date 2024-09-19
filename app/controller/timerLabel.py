class timerLabelController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_timer(self):
        seconds = self.model.seconds

        # self.view.timer.configure(text=seconds)

        if self.view:
            self.view.timer.configure(text=seconds)
        else:
            print("View does not exist")