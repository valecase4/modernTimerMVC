class startBtnController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_timer(self):
        self.model.start()

    def enable(self):
        self.view.start_btn.enable()

    def disable(self):
        self.view.start_btn.disable()
