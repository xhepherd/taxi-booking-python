from location import Location


def test_location_dict_to_struct():
    location = Location({'x': 0, 'y': 1})
    assert location.x == 0
    assert location.y == 1
