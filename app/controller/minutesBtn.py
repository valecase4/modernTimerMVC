class minutesBtnController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_time(self, seconds):
        self.model.add_time(seconds)

    