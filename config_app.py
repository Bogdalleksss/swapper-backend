import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "6a56e485da1e48de9b07a844f55b031d"
    SQLALCHEMY_DATABASE_URI = "sqlite:///swapper.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
