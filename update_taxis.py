class Book:

    def __init__(self, taxis, taxi_id, total_time, destination):
        self._taxis = taxis
        self._taxis.all[taxi_id] = self.__book_taxi(
            taxi_id, total_time, destination)

    def __book_taxi(self, taxi_id, total_time, destination):
        taxi = self._taxis.all[taxi_id]
        taxi.booked_time = total_time
        # update origin to desitnation to simplify logic
        taxi.origin = destination
        taxi.destination = destination
        taxi.set_availability(False)
        return taxi


class UpdateTime:

    def __init__(self, taxis):
        self._taxis = taxis
        self._update_time()

    def _update_time(self):
        for id, taxi in self._taxis.all_list:
            if taxi.is_booked:
                time_left = taxi.booked_time - 1
                taxi.booked_time = time_left
                if time_left <= 0:
                    taxi = self._release_taxi(taxi)
                self._taxis.all[id] = taxi

    def _release_taxi(self, taxi):
        taxi.set_availability(True)
        return taxi
