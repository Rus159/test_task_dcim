import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask:1234@db:5432/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

