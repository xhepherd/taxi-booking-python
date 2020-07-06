import json
from location import Location


class FindTaxi:

    def __init__(self, taxis, source, destination):
        self._taxis = taxis
        self._source = source
        self._destination = destination
        self._found = False
        self._nearest_taxi_id = None
        self._source_to_desitnation = self.__find_time(
            self._source, self._destination)
        self.__find_nearest_taxi()

    @property
    def taxi_id(self):
        return self._nearest_taxi_id

    @property
    def total_time(self):
        return self._source_to_desitnation + self._taxi_to_source

    @property
    def found(self):
        return self._found

    def __find_time(self, source, destination):
        return abs(destination.x - source.x) + abs(destination.y - source.y)

    def __find_nearest_taxi(self):
        for id, taxi in self._taxis.all_list:
            if taxi.is_booked:
                continue
            taxi_to_source = self.__find_time(taxi.origin, self._source)
            if (self._nearest_taxi_id == None) or taxi_to_source < self._taxi_to_source:
                self._found = True
                self._taxi_to_source = taxi_to_source
                self._nearest_taxi_id = taxi.id
