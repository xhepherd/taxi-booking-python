from book import Book
from location import Location
from taxi import Taxi
from api import default_taxi_settings, total_taxis

taxis = []
source = Location({'x': 1, 'y': 1})
destination = Location({'x': 2, 'y': 2})


def init_taxis():
    global taxis
    taxis = []
    for i in range(total_taxis):
        taxi = Taxi(i + 1, default_taxi_settings)
        taxis.append(taxi)


def test_booking_when_all_taxis_available():
    '''
    Also covers booking smallest taxi ID if distance to customer is same 
    '''
    global taxis
    init_taxis()
    book = Book(taxis, source, destination)
    assert book.taxi_id == 1
    assert book.total_time == 4


def test_booking_when_all_taxis_booked():
    global taxis
    init_taxis()
    taxis = [update_availability(taxi, False) for taxi in taxis]
    book = Book(taxis, source, destination)
    assert book.taxi_id == None


def test_booking_nearest_taxi():
    global taxis
    init_taxis()
    # make last taxi one unit closest to origin
    taxis[2].origin = Location({'x': 0, 'y': 1})
    book = Book(taxis, source, destination)
    assert book.taxi_id == 3


def update_availability(taxi, availability):
    taxi.set_availability(availability)
    return taxi
