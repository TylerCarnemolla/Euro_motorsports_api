from flask import Flask
from .site.routes import site
from config import Config
from .authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder
from .api.routes import api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, Marshmallow
from flask_marshmallow import Marshmallow

from flask_cors import CORS
from helpers import JSONEncoder

from flask_login import LoginManager



app = Flask(__name__)
CORS(app)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)
app.json_encoder = JSONEncoder
app.config.from_object(Config)
print(app.config['SQLALCHEMY_DATABASE_URI'])
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)