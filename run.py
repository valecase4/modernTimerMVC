from app import View, Model, Controller

if __name__ == '__main__':
    model = Model()
    controller = Controller(None, model)
    view = View(controller)
    controller.view = view
    view.mainloop()