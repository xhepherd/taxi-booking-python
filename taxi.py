import json
from location import Location


class Taxi:

    def __init__(self, id, default_settings):
        self._id = id
        self.booked_time = default_settings['booked_time']
        self.origin = Location(default_settings['origin'])
        self.destination = self.origin
        self._availability = default_settings['availability']

    @property
    def id(self):
        return self._id

    @property
    def is_booked(self):
        return not self._availability

    def set_availability(self, availability):
        self._availability = availability

    # used for debgging
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
