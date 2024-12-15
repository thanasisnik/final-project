import os


# connect to orderflow.db
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///orderflow.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = "filesystem" #flask-session