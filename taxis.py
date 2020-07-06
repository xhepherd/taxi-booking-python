import json
from taxi import Taxi


class Taxis:

    def __init__(self, total_taxis, default_taxi_settings):
        self._taxis = {}
        self._total_taxis = total_taxis
        self._default_taxi_settings = default_taxi_settings
        self.reset()

    def reset(self):
        self._booked = []
        for i in range(self._total_taxis):
            self._taxis[i + 1] = Taxi(i + 1, self._default_taxi_settings)
        return self._taxis

    @property
    def all(self):
        return self._taxis

    # Caching the dict view as a List for faster iteration
    @property
    def all_list(self):
        return list(self._taxis.items())

    def to_json(self):
        return json.dumps(self.all, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
