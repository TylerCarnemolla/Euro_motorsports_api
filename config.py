import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
  '''
	Set config variables for the flask app
  using Environment variables where available.
  Otherwise create the config variable if not done already
  '''

  FLASK_APP = os.getenv('FLASK_APP')
  FLASK_ENV = os.getenv('FLASK_ENV')
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'Ryan will never get access to my CSS'
  SQLALCHEMY_DATABASE_URI = 'postgresql://nmgkxfwd:flUHiOXSeW73syxNq68lIK-la_PajKLR@kashin.db.elephantsql.com/nmgkxfwd'
  SQLALCHEMY_TRACK_NOTIFICATIONS = False