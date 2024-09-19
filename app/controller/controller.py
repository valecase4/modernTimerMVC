class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def on_click_minutes_btn(self, seconds):
        self.add_time(seconds)
        self.update_timer()

    def start_countdown(self):
        self.model.start()
        self.model.countdown()

    def get_seconds(self):
        return self.model.get_seconds()
    
    def add_time(self, seconds):
        self.model.add_time(seconds)

        print(self.model)

    def converter(self):
        return self.model.converter()
    
    def update_timer(self):
        updated_time = self.converter()

        self.view.timer.configure(text=updated_time)

    def set_time_flow(self):
        self.view.timer.after_id(1000, self.update_timer)


    
