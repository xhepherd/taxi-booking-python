import json
from collections import namedtuple

class Location:

    def __init__(self, location):
        self.__dict__.update(location)

    # used for debugging
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)