from .utils import converter

class Model:
    """
    Model: manages the backend of the application
    """

    def __init__(self) -> None:
        self.seconds = 0
        self.is_running = False
        self.time_format = self.converter(self.seconds)

        # print(f"Initial state: {self.seconds}, {self.is_running}.")

    def run_timer(self) -> None:
        """
        Make the timer active
        """

        self.is_running = True
        
        # print(f"\nFrom Model --> Running: {self.is_running}.\n")

    def pause_timer(self) -> None:
        """
        State of the timer: pause
        """

        self.is_running = False

        # print(f"From model: timer is paused.")
    

    def add_time(self, seconds) -> None:
        """
        Add time to the timer
        """
        
        self.seconds += seconds

        # print(f"Added {seconds}. New value: {self.seconds}")

    def reset(self) -> None:
        """
        Reset timer
        """

        self.seconds = 0
        self.is_running = False

        # print(f"From Model --> Running: {self.is_running}")
        # print(f"From Model --> Reset timer: {self.seconds}")

    def decrease(self) -> None:
        """
        Decrease by 1 every second
        """

        if self.seconds > 0:
            self.seconds -= 1
            # print(f"Seconds from model: {self.seconds}")


    def converter(self, total_seconds: int) -> str:
        """
        Converter() from utils.py
        """

        time_format = converter(total_seconds)

        return time_format
    
    def get_seconds(self) -> int:
        """
        Get the number of seconds at a specific time
        :return: total seconds
        """

        return self.seconds
    
    def get_state(self) -> bool:
        """
        Get the current state of the timer at a specific time
        :return: boolean value (True if timer is running, False otherwise)
        """

        return self.is_running

        