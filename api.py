# coding=utf-8
from flask import Flask, jsonify, request, abort
import json
import code
from book import Book
from taxi import Taxi
from time_tick import TimeTick
from location import Location

app = Flask('taxi-booking-api')
app.config.from_object('config')

total_taxis = app.config['NUMBER_OF_TAXIS']
default_taxi_settings = app.config['DEFAULT_TAXI_SETTINGS']

# List to store Taxis Instances
taxis = []


def init_taxis():
    '''
    Initiate Taxi Instances and store it in taxis list
    '''
    global taxis
    taxis = []
    for i in range(total_taxis):
        taxi = Taxi(i + 1, default_taxi_settings)
        taxis.append(taxi)


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
        source = data.get('source', None)
        destination = data.get('destination', None)

        if not source or not destination:
            return jsonify(error="The fields 'source' and 'destination' are required"), 400

        book = Book(taxis, Location(source), Location(destination))
        taxi_id = book.taxi_id
        total_time = book.total_time
        taxis = book.taxis

        if taxi_id == None:
            return '', 204
        else:
            return jsonify({'car_id': taxi_id, 'total_time': total_time}), 201


@app.route('/api/tick', methods=['POST'])
def tick():
    """
    Advance service time stamp by 1 time unit for booked taxis.
    """
    global taxis
    if request.method == 'POST':
        taxis = TimeTick(taxis).taxis

    return '', 204


@app.route('/api/reset', methods=['PUT'])
def reset():
    """
    Reset all taxis data back to the initial state regardless of taxis that are currently booked
    """
    if request.method == 'PUT':
        init_taxis()

    return '', 204

init_taxis()

if __name__ == '__main__':
    app.run(port=8080)
