class resetBtnController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def reset_timer(self):
        self.model.reset()

        print(self.view)