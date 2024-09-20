from modernTimer.view.view import View
from modernTimer.controller.controller import Controller

if __name__ == '__main__':
    controller = Controller(None, None)
    app = View(controller)
    controller.view = app
    app.mainloop()