from .utils import converter

class Model:
    """
    Model: manages the backend of the application
    """

    def __init__(self) -> None:
        self.seconds = 0
        self.is_running = False
        self.time_format = self.converter(self.seconds)

        print(f"Initial state: {self.seconds}, {self.is_running}.")

    def run_timer(self) -> None:
        """
        Make the timer active
        """

        self.is_running = True
        
        print(f"\nRunning: {self.is_running}.\n")

    def add_time(self, seconds) -> None:
        """
        Add time to the timer
        """
        
        self.seconds += seconds

        print(f"Added {seconds}. New value: {self.seconds}")

    def reset(self) -> None:
        """
        Reset timer
        """

        self.seconds = 0
        self.is_running = False

        print(f"Reset timer: {self.seconds}")

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

        