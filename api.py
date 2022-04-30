from app import app
from flask import jsonify, request
from models import *
from decorators import *


@app.route('/api/racks', methods=['GET'])
def get_racks():
    data = {
        'racks': [rack.to_dict() for rack in db.session.query(Rack).all()]
    }
    return jsonify(data), 200


@app.route('/api/racks/occupied', methods=['GET'])
def get_racks_occupied():
    query = db.session.query(Rack.id, Rack.name, Customer.name, Room.name).outerjoin(Customer).outerjoin(Room).filter(
        Rack.state == 'occupied')
    data = {
        'racks': [{'id': item[0], 'name': item[1], 'customer_name': item[2], 'room_name': item[3]} for item in query]
    }
    return jsonify(data), 200


@app.route('/api/customers', methods=['GET'])
def get_customers():
    data = {
        'customers': [customer.to_dict() for customer in db.session.query(Customer).all()]
    }
    return jsonify(data), 200


@app.route('/api/rooms', methods=['GET'])
def get_rooms():
    data = {
        'rooms': [room.to_dict() for room in db.session.query(Room).all()]
    }
    return jsonify(data), 200


@app.route('/api/addition', defaults={'reverse': None}, methods=['GET'])
@app.route('/api/addition/<reverse>', methods=['GET'] )
@name
def addition(reverse):
    args = list(map(float, list(request.args.values())))
    if reverse:
        args.reverse()
    _addition = sum(args)
    return jsonify(_addition), 200


@app.route('/api/subtraction', defaults={'reverse': None}, methods=['GET'])
@app.route('/api/subtraction/<reverse>', methods=['GET'])
@name
def subtraction(reverse):
    args = list(map(float, list(request.args.values())))
    if reverse:
        args.reverse()
    _subtraction = ''
    for arg in args:
        if _subtraction:
            _subtraction -= arg
        else:
            _subtraction = arg
    return jsonify(_subtraction), 200


@app.route('/api/multiplication', defaults={'reverse': None}, methods=['GET'])
@app.route('/api/multiplication/<reverse>', methods=['GET'])
@name
def multiplication(reverse):
    args = list(map(float, list(request.args.values())))
    if reverse:
        args.reverse()
    _multiplication = ''
    for arg in args:
        if _multiplication:
            _multiplication *= arg
        else:
            _multiplication = arg
    return jsonify(_multiplication), 200


@app.route('/api/division', defaults={'reverse': None}, methods=['GET'])
@app.route('/api/division/<reverse>', methods=['GET'])
@name
def division(reverse):
    args = list(map(float, list(request.args.values())))
    if reverse:
        args.reverse()
    if 0 in args[1:]:
        return jsonify({'error': 'cant divide by zero'})
    else:
        _division = ''
        for arg in args:
            if _division or _division == 0:
                _division /= arg
            else:
                _division = arg
        return jsonify(_division), 200
