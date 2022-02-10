import os

class Config(object):
    TESTING = False
    SECRET_KEY = '9OLWxND4o83j4K4iuopO'
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    BOT_USERNAME = os.environ.get('BOT_USERNAME')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/db'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True