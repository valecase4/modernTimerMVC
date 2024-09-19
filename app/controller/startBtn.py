class startBtnController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_timer(self):
        self.model.start()