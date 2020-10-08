from os import environ, path
basedir = path.abspath(path.dirname(__file__))
class Config:
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO =False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
