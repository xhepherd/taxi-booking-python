from taxi import Taxi
from api import default_taxi_settings


def test_taxi_default_properties():
    taxi = Taxi(1, default_taxi_settings)
    assert taxi.id == 1
    assert taxi.booked_time == 0
    assert taxi.is_booked == False
    assert taxi.origin.x == 0
    assert taxi.origin.y == 0
    assert taxi.destination.x == 0
    assert taxi.destination.y == 0


def test_taxi_change_availability():
    taxi = Taxi(1, default_taxi_settings)
    taxi.set_availability(False)
    assert taxi.is_booked == True
