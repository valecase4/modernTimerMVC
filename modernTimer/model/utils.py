"""
Some functions for the backend
"""

def converter(total_seconds: int) -> str:
        """
        Convert the amount of seconds to the HH:MM:SS format+
        For instance: 3860 seconds --> 01:04:20

        :param total_seconds: number of seconds
        :return: HH:MM:SS time format
        """

        hours = int(total_seconds / 3600)
        minutes = 0
        seconds = 0

        hours_remainder = total_seconds % 3600

        if hours_remainder != 0:
            minutes = int(hours_remainder / 60)

            minutes_remainder = hours_remainder % 60

            if minutes_remainder != 0:
                seconds = minutes_remainder

        hours = f"0{hours}" if len(str(hours)) == 1 else f"{hours}"
        minutes = f"0{minutes}" if len(str(minutes)) == 1 else f"{minutes}"
        seconds = f"0{seconds}" if len(str(seconds)) == 1 else f"{seconds}"

        return f"{hours}:{minutes}:{seconds}"
