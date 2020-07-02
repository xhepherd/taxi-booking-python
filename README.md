# Taxi Booking Python API

A simple RESTful Web API for booking taxi which includes booking, incrementing time units and reseting taxis location and availability endpoints.

- Project is developed in Python3
- Uses Flask framework for Routing
- Pytest for test coverage

## Assumptions and Design Choices

### Assumptions

- No authentication or login is required
- Logging to console instead of file to keep it simple.

### Design Choices

- Used flask as its light weight
- Used in-memory storage with key-value data structure

## TODO Items

- Improve logging
- Improve exception handling
- Enforce Python and Flask best practices (static code analysis tests)
- Static code analysis tests for vulnerabilities

## Environment
### Install Dependencies

Requires **Python 3.6** to install.

After Python installed, it is required to install all dependencies. You can use [Virtualenv](https://virtualenv.pypa.io/en/stable/). Use the following command to install from **requirements.pip** file:

```bash
$ python -m venv YOUR_ENVIRONMENT_DIRECTORY
$ source YOUR_ENVIRONMENT_DIRECTORY/bin/activate
$ pip install -r requirements.pip
```
### Database
Not using any persistent storage instead data is stored in-memory which is in key-value data structure.

## How to run

```bash
$ python app.py
* Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

## Testing

You can test the application using the development dependencies.

Install all development dependencies from **dev-requirements.txt** file if you are using **VirtualEnv**:

```bash
$ python -m venv YOUR_DEV_ENVIRONMENT_DIRECTORY
$ source YOUR_DEV_ENVIRONMENT_DIRECTORY
$ pip install -r dev-requirements.txt
```

### Unit Tests

To run unit tests, you can use PyTest as following:
```bash
$ python -m pytest
```
### Black Box Tests
To run basic tests against API server

Run API server either in background or in a separate terminal

```bash
$ python api.py #run in background or antoher terminal
```

Run basic tests
```basah
$ python basic_solution_checker.py
```  

## API Documentation

### Book
Pick the nearest available taxi to the customer location and return the total time taken to travel from the current taxi location to customer location then to customer destination.
#### HTTP Request
`POST /api/book`
#### Request Payload
```json
{
  "source": {
    "x": "x1",
    "y": "y1"
  },
  "destination": {
    "x": "x2",
    "y": "y2"
  }
}
```
|**Parameter**|**Description**|
|---|---|
|Source|`x` and `y` axis of customer current location|
|Destination|`x` and `y` axis of customer desitnation|

#### Response Payload with available taxi
```json
{
  "car_id": "id",
  "total_time": "t"
}
```
|**Parameter**|**Description**|
|---|---|
|Car ID|ID of the nearest booked car.|
|Total Time|Time taken to travel from the current taxi location to customer location then to customer destination.|


#### Response Payload with unavailable taxi
`No Content`

#### Response Status Codes
|**Code**|**Description**|
|---|---|
|`201`|Taxi Available|
|`204`|Taxi Unavailable|
|`400`|Request payload invalid|

### Tick
Advance service time stamp by 1 time unit for booked taxis.
This also mark booked taxis available which complete their destination by this time unit. 

#### HTTP Request
`POST /api/tick`

#### Request Payload
`None`

#### Response Payload
`No Content`

#### Response Status Code
|**Code**|**Description**|
|---|---|
|`204`|Booked taxis advanced by 1 time unit|

### Reset
Reset all taxis data back to the initial state regardless of cars that are currently booked 

#### HTTP Request
`PUT /api/reset`

#### Request Payload
`None`

#### Response Payload
`No Content`

#### Response Status Code
|**Code**|**Description**|
|---|---|
|`204`|Reset all taxis data|

### API Error Codes
|**Code**|**Description**|
|---|---|
|`500`|Internal Server Error|
