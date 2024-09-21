from modernTimer.view.view import View
from modernTimer.controller.controller import Controller
from modernTimer.model.model import Model

if __name__ == '__main__':
    model = Model()
    controller = Controller(model, None)
    app = View(controller)
    controller.view = app
    app.mainloop()