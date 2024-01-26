from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

# set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'
    
class Bike(db.Model):
    id = db.Column(db.String, primary_key = True)
    brand = db.Column(db.String(150), nullable = False)
    model = db.Column(db.String(200))
    engine = db.Column(db.String(20))
    color = db.Column(db.String(200))
    price = db.Column(db.String(20))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self,brand, model, engine, color, price ,user_token, id = ''):
        self.id = self.set_id()
        self.brand = brand
        self.model = model
        self.engine = engine
        self.color = color
        self.price = price
        self.user_token = user_token


    def __repr__(self):
        return f'The following bike has been added to the inventory: {self.model}'

    def set_id(self):
        return (secrets.token_urlsafe())
    
    
class ATV(db.Model):
    id = db.Column(db.String, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    model = db.Column(db.String(200))
    engine = db.Column(db.String(20))
    color = db.Column(db.String(200))
    price = db.Column(db.String(20))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)

    def __init__(self, brand, model, engine, color, price, user_token, id=''):
        self.id = self.set_id()
        self.brand = brand
        self.model = model
        self.engine = engine
        self.color = color
        self.price = price
        self.user_token = user_token

    def __repr__(self):
        return f'The following ATV has been added to the inventory: {self.model}'

    def set_id(self):
        return secrets.token_urlsafe()

class Gear(db.Model):
    id = db.Column(db.String, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    type = db.Column(db.String(100))
    size = db.Column(db.String(50))
    color = db.Column(db.String(200))
    price = db.Column(db.String(20))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)

    def __init__(self, brand, type, size, color, price, user_token, id=''):
        self.id = self.set_id()
        self.brand = brand
        self.type = type
        self.size = size
        self.color = color
        self.price = price
        self.user_token = user_token

    def __repr__(self):
        return f'The following gear has been added to the inventory: {self.type}'

    def set_id(self):
        return secrets.token_urlsafe()
    
class Helmet(db.Model):
    id = db.Column(db.String, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    size = db.Column(db.String(50))
    color = db.Column(db.String(200))
    price = db.Column(db.String(20))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)

    def __init__(self, brand, size, color, price, user_token, id=''):
        self.id = self.set_id()
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.user_token = user_token

    def __repr__(self):
        return f'The following gear has been added to the inventory: {self.brand}'

    def set_id(self):
        return secrets.token_urlsafe()



class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'g_auth_verify', 'token', 'date_created')

class BikeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'brand', 'model', 'engine', 'color', 'price', 'user_token')

class ATVSchemas(ma.Schema):
    class Meta:
        fields = ('id', 'brand', 'model', 'engine', 'color', 'price', 'user_token')

class GearSchema(ma.Schema):
    class Meta:
        fields = ('id', 'brand', 'type', 'size', 'color', 'price', 'user_token')

class HelmetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'brand', 'size', 'color', 'price', 'user_token')

# Create instances of the schemas
user_schema = UserSchema()
bike_schema = BikeSchema()
atv_schema = ATVSchemas()
gear_schema = GearSchema()
helmet_schema = HelmetSchema()

# Create instances of the collection schemas
bikes_schema = BikeSchema(many=True)
atvs_schema = ATVSchemas(many=True)
gears_schema = GearSchema(many=True)
helmets_schema = HelmetSchema(many=True)