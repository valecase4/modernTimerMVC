import time

class Model:
    """
    Timer backend
    """

    def __init__(self):
        self.seconds = 60
        self.is_running = False

    def __repr__(self) -> str:
        return f"Timer is now {self.seconds}"
    
    def start(self):
        if not self.is_running:
            self.is_running = True

            print(f"Timer is now running. {self.is_running}")

    def pause(self):
        if self.is_running:
            self.is_running = False

            print(f"Timer paused. {self.seconds}")

    def add_time(self, seconds):
        self.seconds += seconds

    def reset(self):
        self.seconds = 0
        self.is_running = False

        print(f"Timer has been stopped. {self.is_running}; {self.seconds}")

    

        