# coding=utf-8
from flask import Flask, jsonify, request, abort
import json
import code
from taxi import Taxi
from taxis import Taxis
from find_taxi import FindTaxi
from update_taxis import Book, UpdateTime
from location import Location

app = Flask('taxi-booking-api')
app.config.from_object('config')

total_taxis = app.config['NUMBER_OF_TAXIS']
default_taxi_settings = app.config['DEFAULT_TAXI_SETTINGS']

# List to store Taxis Instances
taxis = Taxis(total_taxis, default_taxi_settings)


@app.errorhandler(Exception)
def handle_error(e):
    error = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    print(error)
    return jsonify(error="Server error, please try again later."), 500


@app.route('/api/book', methods=['POST'])
def book():
    """
    Books the nearest taxi and returns taxi id and total time to destination
    {"car_id": 1, "total_time": 4}
    """
    global taxis
    taxi_id = None
    total_time = None
    if request.method == 'POST':
        data = request.json
        """
        TODO: Add validation for required params
        """
        source = Location(data.get('source', None))
        destination = Location(data.get('destination', None))

        taxi = FindTaxi(taxis, source, destination)

        if not taxi.found:
            return '', 204
        else:
            taxi_id = taxi.taxi_id
            total_time = taxi.total_time
            Book(taxis, taxi_id, total_time, destination)
            return jsonify({'car_id': taxi_id, 'total_time': total_time}), 201


@app.route('/api/tick', methods=['POST'])
def tick():
    """
    Advance service time stamp by 1 time unit for booked taxis.
    """
    global taxis
    if request.method == 'POST':
        UpdateTime(taxis)

    return '', 204


@app.route('/api/reset', methods=['PUT'])
def reset():
    """
    Reset all taxis data back to the initial state regardless of taxis that are currently booked
    """
    if request.method == 'PUT':
        taxis.reset()

    return '', 204


if __name__ == '__main__':
    app.run(port=8080)
