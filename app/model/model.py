import time

class Model:
    """
    Timer backend
    """

    def __init__(self):
        self.seconds = 0
        self.is_running = False

    def __repr__(self) -> str:
        return f"Timer is now {self.seconds} --> {self.converter()}"
    
    def end_timer(self):
        print("Timer is finished")
    
    def start(self):
        self.is_running = True

    def add_time(self, seconds):
        self.seconds += seconds

    def get_seconds(self):
        return self.seconds
    
    def countdown(self):
        if self.is_running:
            seconds = self.get_seconds()

            if seconds > 0:

                print(f"Countdown starts from {seconds}")

                time.sleep(1)

                self.seconds -= 1

                self.countdown()
            
            else:

                self.is_running = False
                self.end_timer()

        
        else:
            print("Timer is not running")


    
    def converter(self):
        seconds = self.get_seconds()

        hours_ = int(seconds / 3600)
        minutes_ = 0
        seconds_ = 0

        hours_remainder = seconds % 3600

        if hours_remainder != 0:
            minutes_ = int(hours_remainder / 60)

            minutes_remainder = hours_remainder % 60

            if minutes_remainder != 0:
                seconds_ = minutes_remainder

        hours_ = f"0{hours_}" if len(str(hours_)) == 1 else f"{hours_}"
        minutes_ = f"0{minutes_}" if len(str(minutes_)) == 1 else f"{minutes_}"
        seconds_ = f"0{seconds_}" if len(str(seconds_)) == 1 else f"{seconds_}"

        return f"{hours_}:{minutes_}:{seconds_}"

        