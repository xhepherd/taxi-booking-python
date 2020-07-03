class TimeTick:

    def __init__(self, taxis):
        self._taxis = taxis
        self.__update_taxis()

    @property
    def taxis(self):
        return self._taxis

    def __update_taxis(self):
        self._taxis = [self.__update_taxi_time(taxi) for taxi in self._taxis]

    def __update_taxi_time(self, taxi):
        if taxi.is_booked:
            time_left = taxi.booked_time - 1
            taxi.booked_time = time_left
            if time_left <= 0:
                taxi.set_availability(True)
        return taxi
