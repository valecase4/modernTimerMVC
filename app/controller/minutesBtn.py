class minutesBtnController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_time(self, seconds):
        self.model.add_time(seconds)

        print(self.model)


    