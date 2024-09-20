class pauseBtnController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def pause_timer(self):
        self.model.pause()

    def enable(self):
        self.view.pause_btn.enable()

    def disable(self):
        self.view.pause_btn.disable()