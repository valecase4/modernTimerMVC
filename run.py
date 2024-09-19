'''from app import View, Model, Controller

if __name__ == '__main__':
    model = Model()
    controller = Controller(None, model)
    view = View(controller)
    controller.view = view
    view.mainloop()'''

from app.view.view import View
from app.controller.controller import Controller
from app.model.model import Model

if __name__ == "__main__":
    model = Model()
    controller = Controller(model, None)
    view = View(controller)
    controller.view = view

    view.mainloop()

