from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, Helmet, ATV, Gear, Bike, bike_schema, bikes_schema, atv_schema, atvs_schema, gear_schema, gears_schema, helmet_schema, helmets_schema

api = Blueprint('api', __name__, url_prefix='/api') #prefix means that it goes before the slug

# get all bikes
@api.route('/bikes', methods=['GET'])
@token_required
def get_user_bikes(current_user_token):
    a_user=current_user_token.token
    bikes = Bike.query.filter_by(user_token = a_user).all()
    response = bikes_schema.dump(bikes)
    return jsonify(response)

# get a bike
@api.route('/bikes/<id>', methods = ['GET'])
@token_required
def get_single_bike(current_user_token, id):
    bike = Bike.query.get(id)
    response = bike_schema.dump(bike)
    return jsonify(response)



# create bike
@api.route('/bikes', methods = ['POST'])
@token_required
def create_bike(current_user_token):
    brand = request.json['brand']
    model = request.json['model']
    engine = request.json['engine']
    color = request.json['color']
    price = request.json['price']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    bike = Bike(brand, model, engine, color, price, user_token=user_token) #we do user_token = user_toked to over-write
    #the previous value for that variable

    db.session.add(bike)
    db.session.commit()

    response = bike_schema.dump(bike)
    return jsonify(response)

# update bike

@api.route('/bikes/<id>', methods = ['POST', 'PUT'])
@token_required
def update_bike(current_user_token, id):
    bike = Bike.query.get(id)
    bike.brand = request.json['brand']
    bike.model = request.json['model']
    bike.engine = request.json['engine']
    bike.color = request.json['color']
    bike.price = request.json['price']
    bike.user_token = current_user_token.token

    db.session.commit()
    response = bike_schema.dump(bike)
    return jsonify(response)

# delete a bike


@api.route('/bikes/<id>', methods = ['DELETE'])
@token_required
def delete_bike(current_user_token, id):
    bike = Bike.query.get(id)
    db.session.delete(bike)
    db.session.commit()
    response = bike_schema.dump(bike)
    return jsonify(response)







# ATVS

@api.route('/atvs', methods=['GET'])
@token_required
def get_user_atvs(current_user_token):
    a_user=current_user_token.token
    atvs = ATV.query.filter_by(user_token = a_user).all()
    response = atvs_schema.dump(atvs)
    return jsonify(response)

# get a bike
@api.route('/atvs/<id>', methods = ['GET'])
@token_required
def get_single_atv(current_user_token, id):
    atv = ATV.query.get(id)
    response = atv_schema.dump(atv)
    return jsonify(response)



# create bike
@api.route('/atvs', methods = ['POST'])
@token_required
def create_atv(current_user_token):
    brand = request.json['brand']
    model = request.json['model']
    engine = request.json['engine']
    color = request.json['color']
    price = request.json['price']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    atv = ATV(brand, model, engine, color, price, user_token=user_token) 
    db.session.add(atv)
    db.session.commit()

    response = atv_schema.dump(atv)
    return jsonify(response)

# update atv

@api.route('/atvs/<id>', methods = ['POST', 'PUT'])
@token_required
def update_atv(current_user_token, id):
    atv = ATV.query.get(id)
    atv.brand = request.json['brand']
    atv.model = request.json['model']
    atv.engine = request.json['engine']
    atv.color = request.json['color']
    atv.price = request.json['price']
    atv.user_token = current_user_token.token

    db.session.commit()
    response =atv_schema.dump(atv)
    return jsonify(response)

# delete an atv


@api.route('/atvs/<id>', methods = ['DELETE'])
@token_required
def delete_atv(current_user_token, id):
    atv = ATV.query.get(id)
    db.session.delete(atv)
    db.session.commit()
    response = atv_schema.dump(atv)
    return jsonify(response)












# Gear
@api.route('/gear', methods=['GET'])
@token_required
def get_user_gear(current_user_token):
    a_user=current_user_token.token
    gear = Gear.query.filter_by(user_token = a_user).all()
    response = gears_schema.dump(gear)
    return jsonify(response)

# get an item
@api.route('/gear/<id>', methods = ['GET'])
@token_required
def get_single_gear(current_user_token, id):
    gear = Gear.query.get(id)
    response = gear_schema.dump(gear)
    return jsonify(response)



# create item
@api.route('/gear', methods = ['POST'])
@token_required
def create_gear(current_user_token):
    brand = request.json['brand']
    type = request.json['type']
    size = request.json['size']
    color = request.json['color']
    price = request.json['price']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    gear = Gear(brand, type, size, color, price, user_token=user_token) 
    db.session.add(gear)
    db.session.commit()

    response = gear_schema.dump(gear)
    return jsonify(response)

# update item

@api.route('/gear/<id>', methods = ['POST', 'PUT'])
@token_required
def update_gear(current_user_token, id):
    gear = Gear.query.get(id)
    gear.brand = request.json['brand']
    gear.type = request.json['type']
    gear.size = request.json['size']
    gear.color = request.json['color']
    gear.price = request.json['price']
    gear.user_token = current_user_token.token

    db.session.commit()
    response =gear_schema.dump(gear)
    return jsonify(response)

# delete an item


@api.route('/gear/<id>', methods = ['DELETE'])
@token_required
def delete_gear(current_user_token, id):
    gear = Gear.query.get(id)
    db.session.delete(gear)
    db.session.commit()
    response = gear_schema.dump(gear)
    return jsonify(response)





# helmets


@api.route('/helmets', methods=['GET'])
@token_required
def get_user_helmets(current_user_token):
    a_user=current_user_token.token
    helmets = Helmet.query.filter_by(user_token = a_user).all()
    response = helmets_schema.dump(helmets)
    return jsonify(response)

# get one
@api.route('/helmets/<id>', methods = ['GET'])
@token_required
def get_single_helmet(current_user_token, id):
    helmet = Helmet.query.get(id)
    response = helmet_schema.dump(helmet)
    return jsonify(response)



# create one
@api.route('/helmets', methods = ['POST'])
@token_required
def create_helmet(current_user_token):
    brand = request.json['brand']
    size = request.json['size']
    color = request.json['color']
    price = request.json['price']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    helmet = Helmet(brand, size, color, price, user_token=user_token) 
    db.session.add(helmet)
    db.session.commit()

    response = helmet_schema.dump(helmet)
    return jsonify(response)

# update one
@api.route('/helmets/<id>', methods = ['POST', 'PUT'])
@token_required
def update_helmet(current_user_token, id):
    helmet = Helmet.query.get(id)
    helmet.brand = request.json['brand']
    helmet.size = request.json['size']
    helmet.color = request.json['color']
    helmet.price = request.json['price']
    helmet.user_token = current_user_token.token

    db.session.commit()
    response =helmet_schema.dump(helmet)
    return jsonify(response)

# delete a helmet


@api.route('/helmets/<id>', methods = ['DELETE'])
@token_required
def delete_helmet(current_user_token, id):
    helmet = Helmet.query.get(id)
    db.session.delete(helmet)
    db.session.commit()
    response = helmet_schema.dump(helmet)
    return jsonify(response)






