from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

load_dotenv()


class Config(object):
    """Base Configuration Class"""

    SECRET_KEY = "flask-secret-key"
    DEBUG = True
    TESTING = environ.get("TESTING") or False
    SQLALCHEMY_DATABASE_URI = "sqlite:///flask.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SECRET_KEY = environ.get("SECRET_KEY")


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    SECRET_KEY = environ.get("SECRET_KEY")
    DEBUG = False
    TESTING = False
