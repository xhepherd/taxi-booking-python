from time_tick import TimeTick
from taxi import Taxi
from api import default_taxi_settings, total_taxis

taxis = []


def init_taxis():
    global taxis
    taxis = []
    for i in range(total_taxis):
        taxi = Taxi(i + 1, default_taxi_settings)
        taxis.append(taxi)


def test_time_tick_for_available_taxis():
    global taxis
    init_taxis()
    taxis = TimeTick(taxis).taxis
    for taxi in taxis:
        assert taxi.booked_time == 0


def test_time_tick_for_booked_taxis():
    global taxis
    init_taxis()
    taxis[0].booked_time = 2
    taxis[0].set_availability(False)
    taxis = TimeTick(taxis).taxis
    assert taxis[0].booked_time == 1


def test_availablity_for_taxi_reached_destination():
    global taxis
    init_taxis()
    taxis[0].booked_time = 1
    taxis[0].set_availability(False)
    taxis = TimeTick(taxis).taxis
    assert taxis[0].is_booked == False
