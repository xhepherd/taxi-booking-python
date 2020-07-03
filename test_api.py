from api import app, total_taxis, json, jsonify

book_request_json = {
    "source": {"x": 1, "y": 1},
    "destination": {"x": 1, "y": 2}
}


def reset_taxis():
    with app.test_client() as client:
        response = client.put('/api/reset')
        assert response.status_code == 204


def test_book_must_return_status_201():
    with app.test_client() as client:
        response = client.post('/api/book', json=book_request_json)
        assert response.status_code == 201


def test_book_must_have_json_format():
    with app.test_client() as client:
        response = client.post('/api/book', json=book_request_json)
        assert response.content_type == 'application/json'


def test_book_must_return_valid_response():
    with app.test_client() as client:
        reset_taxis()
        response = client.post('/api/book', json=book_request_json)
        assert response.get_json() == {'car_id': 1, 'total_time': 3}


def test_return_no_content_all_taxis_booked():
    with app.test_client() as client:
        reset_taxis()
        for i in range(total_taxis):
            client.post('/api/book', json=book_request_json)
        response = client.post('/api/book', json=book_request_json)
        assert response.status_code == 204


def test_reset_must_change_taxis_availabilities():
    with app.test_client() as client:
        reset_taxis()
        for i in range(total_taxis):
            client.post('/api/book', json=book_request_json)
        response = client.post('/api/book', json=book_request_json)
        # No taxi is available as confirmed by empty response
        assert response.status_code == 204
        reset_taxis()
        # All taxis must be available for booking
        for i in range(total_taxis):
            response = client.post('/api/book', json=book_request_json)
            assert response.status_code == 201


def test_tick_mark_booked_taxi_available_on_destination():
    with app.test_client() as client:
        reset_taxis()
        # Book first available taxi
        response = client.post('/api/book', json=book_request_json)
        car_id = response.get_json()['car_id']
        total_time = response.get_json()['total_time']
        # Tick total_time times to make first taxi available for rebooking
        for i in range(total_time):
            client.post('/api/tick')
        response = client.post('/api/book', json=book_request_json)
        assert car_id == response.get_json()['car_id']
