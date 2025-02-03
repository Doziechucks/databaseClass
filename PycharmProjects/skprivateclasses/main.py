class OurTime:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def __hours(self):
        return self._hours

    @__hours.setter
    def __hours(self, hours):
        if hours < 0 or hours >= 23:
            raise ValueError("Invalid hour")
        self._hours = hours

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        if minutes < 0 or minutes > 59:
            raise ValueError("Invalid minute")
        self._minutes = minutes

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter

    def seconds(self, seconds):
        if seconds < 0 or seconds > 59:
            raise ValueError("Invalid seconds")
        self._seconds = seconds

    def __str__(self):
        return f"Hours:{self.__hours} Minutes:{self.minutes} Seconds:{self.seconds}"

time1 = OurTime(22, 44, 44)
print(time1)