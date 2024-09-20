class resetBtnController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def reset_timer(self):
        self.model.reset()

    def enable(self):
        self.view.reset_btn.enable()

    def disable(self):
        self.view.reset_btn.disable()
