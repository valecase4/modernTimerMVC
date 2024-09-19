class pauseBtnController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def pause_timer(self):
        self.model.pause()

    