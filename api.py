# coding=utf-8
from flask import Flask, jsonify, request, abort
import json
from book import Book
from taxi import Taxi
from time_tick import TimeTick
from location import Location

app = Flask('taxi-booking-api')
app.config.from_object('config')
debug = app.config['DEBUG']
if debug:
    import code

total_taxis = app.config['NUMBER_OF_TAXIS']
default_settings_taxi = app.config['DEFAULT_SETTINGS_TAXI']

taxis = []

def init_taxis():
    global taxis
    taxis = []
    for i in range(total_taxis):
        taxi = Taxi(i+1, default_settings_taxi)
        taxis.append(taxi)

init_taxis()

@app.errorhandler(Exception)
def handle_error(e):
    status_code = 500
    return jsonify(error=str(e)), status_code

@app.route('/api')
def home():
    return jsonify(taxis), 200

@app.route('/api/book', methods=['POST'])
def book():
    global taxis
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

        response = {}
        status_code = 200
        if taxi_id != None:
            response = { 'car_id': taxi_id, 'total_time': total_time }
            status_code = 201

        return jsonify(response), status_code

@app.route('/api/tick', methods=['POST'])
def tick():
    global taxis
    jt = []
    if request.method == 'POST':
        taxis = TimeTick(taxis).taxis
        if debug:
            jt = [json.loads(taxi.toJson()) for taxi in taxis]

    if False:
        # code.interact(local=dict(globals(), **locals()))
        return jsonify(jt), 201
    else:
        return jsonify({}), 201
    

@app.route('/api/reset', methods=['PUT'])
def reset():
    if request.method == 'PUT':
        init_taxis()

    return jsonify({}), 200


if __name__ == '__main__':
    app.run(debug=debug, port=8080)
