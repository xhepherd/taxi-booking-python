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
    ## TODO items
    ## Log Errors to a file or log errors to Error Reporting service
    print(jsonify(error=str(e)))
    return jsonify(error="Server error, please try again later."), status_code

@app.route('/api')
def home():
    return jsonify(taxis), 200

@app.route('/api/book', methods=['POST'])
def book():
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
            return jsonify({ 'car_id': taxi_id, 'total_time': total_time }),201


@app.route('/api/tick', methods=['POST'])
def tick():
    global taxis
    jt = []
    if request.method == 'POST':
        taxis = TimeTick(taxis).taxis
        if debug:
            jt = [json.loads(taxi.toJson()) for taxi in taxis]

    if False:
        ## Breakpoint
        # code.interact(local=dict(globals(), **locals()))
        return jsonify(jt), 201
    else:
        return '', 204
    

@app.route('/api/reset', methods=['PUT'])
def reset():
    if request.method == 'PUT':
        init_taxis()

    return '', 204


if __name__ == '__main__':
    app.run(debug=debug, port=8080)
