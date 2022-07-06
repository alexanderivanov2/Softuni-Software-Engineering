class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    def get_time(self):
        hh = f"0{self.hours}"if self.hours < 10 else f"{self.hours}"
        mm = f"0{self.minutes}"if self.minutes < 10 else f"{self.minutes}"
        ss = f"0{self.seconds}"if self.seconds < 10 else f"{self.seconds}"
        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        if self.hours == Time.max_hours and self.minutes == Time.max_minutes and self.seconds == self.max_seconds:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif self.minutes == Time.max_minutes and self.seconds == self.max_seconds:
            self.hours += 1
            self.minutes = 0
            self.seconds = 0
        elif self.seconds == self.max_seconds:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1
        return self.get_time()
