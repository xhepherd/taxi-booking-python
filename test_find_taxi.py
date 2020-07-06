from find_taxi import FindTaxi
from location import Location
from taxi import Taxi
from taxis import Taxis
from api import default_taxi_settings, total_taxis

taxis = Taxis(total_taxis, default_taxi_settings)
source = Location({'x': 1, 'y': 1})
destination = Location({'x': 2, 'y': 2})


def test_find_taxi_when_all_taxis_available():
    '''
    Also covers FindTaxiing smallest taxi ID if distance to customer is same
    '''
    global taxis
    taxis.reset()
    booked_taxi = FindTaxi(taxis, source, destination)
    assert booked_taxi.taxi_id == 1


def test_find_taxi_total_time():
    global taxis
    taxis.reset()
    booked_taxi = FindTaxi(taxis, source, destination)
    assert booked_taxi.total_time == 4


def test_find_taxi_when_all_taxis_booked():
    global taxis
    taxis.reset()
    for id, taxi in taxis.all_list:
        taxis.all[id] = update_availability(taxi, False)
    booked_taxi = FindTaxi(taxis, source, destination)
    assert booked_taxi.taxi_id == None


def test_find_taxi_nearest_taxi():
    global taxis
    taxis.reset()
    # make last taxi one unit closest to origin
    taxis.all[3].origin = Location({'x': 0, 'y': 1})
    booked_taxi = FindTaxi(taxis, source, destination)
    assert booked_taxi.taxi_id == 3


def update_availability(taxi, availability):
    taxi.set_availability(availability)
    return taxi
