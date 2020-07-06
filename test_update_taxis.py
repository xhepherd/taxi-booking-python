from update_taxis import UpdateTime, Book
from taxi import Taxi
from taxis import Taxis
from location import Location
from api import default_taxi_settings, total_taxis

taxis = Taxis(total_taxis, default_taxi_settings)


def test_time_tick_for_available_taxis():
    global taxis
    taxis.reset()
    UpdateTime(taxis)
    for id, taxi in taxis.all_list:
        assert taxi.booked_time == 0


def test_time_tick_for_booked_taxis():
    global taxis
    taxis.reset()
    taxis.all[1].booked_time = 2
    taxis.all[1].set_availability(False)
    UpdateTime(taxis)
    assert taxis.all[1].booked_time == 1


def test_availablity_for_taxi_reached_destination():
    global taxis
    taxis.reset()
    taxis.all[1].booked_time = 1
    taxis.all[1].set_availability(False)
    UpdateTime(taxis)
    assert taxis.all[1].is_booked == False


def test_book_a_taxi():
    global taxis
    taxis.reset()
    taxi_id = 1
    total_time = 4
    destination = Location({'x': 2, 'y': 2})
    Book(taxis, taxi_id, total_time, destination)
    taxi = taxis.all[taxi_id]
    assert taxi.is_booked == True
    assert taxi.booked_time == total_time
    assert taxi.origin.x == destination.x
    assert taxi.origin.y == destination.y
