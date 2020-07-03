import json
from location import Location


class Book:

    def __init__(self, taxis, source, destination):
        self._taxis = taxis
        self._source = source
        self._destination = destination
        self._source_to_desitnation = self.__find_time(
            self._source, self._destination)
        self._taxi_to_source = 0
        self._nearest_taxi_id = None
        self.__find_nearest_taxi()
        self._total_time = self.__total_time()
        self.__update_taxis()

    @property
    def taxi_id(self):
        return self._nearest_taxi_id

    @property
    def total_time(self):
        return self._total_time

    @property
    def taxis(self):
        return self._taxis

    def __update_taxis(self):
        self._taxis = [self.__book_taxi(taxi) for taxi in self._taxis]

    def __book_taxi(self, taxi):
        if taxi.id == self._nearest_taxi_id:
            taxi.booked_time = self._total_time
            # update origin to desitnation to simplify logic
            taxi.origin = self._destination
            taxi.set_availability(False)
        return taxi

    def __find_time(self, source, destination):
        return abs(destination.x - source.x) + abs(destination.y - source.y)

    def __find_nearest_taxi(self):
        for taxi in self._taxis:
            if taxi.is_booked:
                continue
            taxi_to_source = self.__find_time(taxi.origin, self._source)
            if self._nearest_taxi_id == None or taxi_to_source < self._taxi_to_source:
                self._taxi_to_source = taxi_to_source
                self._nearest_taxi_id = taxi.id

    def __total_time(self):
        return self._source_to_desitnation + self._taxi_to_source
